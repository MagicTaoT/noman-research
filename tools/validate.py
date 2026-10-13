#!/usr/bin/env python3
"""Validate publication packaging, not backtest results. Standard library only."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def extract_tables(text, source):
    """Keep displayed units and precision as strings; do not reinterpret values."""
    lines = text.splitlines()
    section = ""
    tables = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("#"):
            section = lines[i].lstrip("# ").strip()
        if (lines[i].startswith("|") and i + 1 < len(lines)
                and re.fullmatch(r"[|:\-\s]+", lines[i + 1])
                and "---" in lines[i + 1]):
            cells = lambda line: [cell.strip() for cell in line.strip().strip("|").split("|")]
            columns = cells(lines[i])
            rows = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                row = cells(lines[i])
                assert len(row) == len(columns), f"Ragged table: {source}, {section}"
                rows.append(row)
                i += 1
            tables.append({"source": source, "section": section, "columns": columns, "rows": rows})
            continue
        i += 1
    return tables


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def public_files(directory):
    return sorted(p for p in directory.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts)


def validate(write=False):
    catalog = json.loads((ROOT / "catalog.json").read_text())
    assert catalog["schema_version"] == 1
    seen_ids, seen_slugs = set(), set()
    total_tables = 0
    for entry in catalog["papers"]:
        assert entry["id"] not in seen_ids and entry["slug"] not in seen_slugs
        seen_ids.add(entry["id"])
        seen_slugs.add(entry["slug"])
        folder = ROOT / entry["path"]
        assert folder.resolve().is_relative_to(ROOT / "papers")
        assert folder.relative_to(ROOT).as_posix() == f"papers/{entry['year']}/{entry['slug']}"
        meta = json.loads((folder / "metadata.json").read_text())
        for key in ("id", "slug", "title", "version", "release_tag", "status", "website_url"):
            assert meta[key] == entry[key], f"Catalog/metadata mismatch: {key}"
        assert entry["release_tag"] == f"{entry['slug']}-v{entry['version']}"
        assert meta["release_scope"]["raw_market_data"] is False
        assert meta["release_scope"]["derived_market_records"] is False
        assert meta["license"] == "CC-BY-4.0", "Review validator policy for any new paper license"
        for name in ("README.md", "paper.md", "metadata.json", "citation.bib", "CHANGELOG.md", "RELEASE_NOTES.md", "results/README.md"):
            assert (folder / name).is_file(), f"Missing {entry['slug']}/{name}"
        for language in meta["languages"]:
            for key in ("manuscript", "appendix", "pdf"):
                assert (folder / language[key]).is_file(), f"Missing {language[key]}"
            assert (folder / language["pdf"]).read_bytes().startswith(b"%PDF-")
        tables = []
        for name in ("paper.md", "appendix.md"):
            tables.extend(extract_tables((folder / name).read_text(), name))
        exported = json.loads((folder / "results/tables.json").read_text())
        assert exported["tables"] == tables, f"Aggregate export differs from approved tables: {entry['slug']}"
        total_tables += len(tables)
        files = [p for p in public_files(folder) if p.name != "SHA256SUMS"]
        expected = "".join(f"{sha(p)}  {p.relative_to(folder).as_posix()}\n" for p in files)
        if write:
            (folder / "SHA256SUMS").write_text(expected)
        assert (folder / "SHA256SUMS").read_text() == expected, f"Stale file inventory or checksums: {entry['slug']}"

    blocked_suffixes = {".pem", ".key", ".db", ".sqlite", ".sqlite3", ".parquet", ".feather", ".jsonl", ".log"}
    blocked_parts = {"data", "raw", "raw_data", "private", "secrets", "credentials", "backups", "node_modules"}
    link_count = 0
    for path in public_files(ROOT):
        rel = path.relative_to(ROOT)
        assert not path.is_symlink(), f"Symlink forbidden: {rel}"
        assert path.suffix not in blocked_suffixes and not blocked_parts.intersection(rel.parts), f"Out-of-scope file: {rel}"
        assert not path.name.startswith(".env"), f"Environment file: {rel}"
        if path.suffix in {".md", ".json", ".bib", ".yml"}:
            text = path.read_text()
            assert not re.search(r"/(?:Users|home)/[^\s/]+/", text), f"Local machine path: {rel}"
            assert not re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}", text), f"Credential-like content: {rel}"
        if path.suffix != ".md":
            continue
        for href in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", path.read_text()):
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), f"Broken or escaping local link: {rel}: {href}"
            link_count += 1
    print(json.dumps({"status": "passed", "papers": len(seen_ids), "aggregate_tables": total_tables,
                      "local_links": link_count, "publication_files": len(public_files(ROOT))}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-checksums", action="store_true", help="Refresh approved paper inventories before validation")
    args = parser.parse_args()
    validate(args.write_checksums)
