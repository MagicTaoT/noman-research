# Publishing a paper

## Structure

1. Reserve a unique `NR-YYYY-NNN` paper ID and a stable lowercase slug.
2. Create `papers/YYYY/<slug>/` using the checklist in
   [the template](../templates/paper/README.md).
3. Keep that paper's manuscripts, PDFs, figures, aggregate results, metadata,
   citation and changelog inside its directory. Use relative links within it.
4. Add the paper to `catalog.json` and the English and Chinese root indexes.

Catalog entries contain `id`, `slug`, `year`, `title`, `author`, `version`,
`path`, `release_tag`, `status` and `website_url`. The catalog indexes the
current version of each paper; prior versions remain available through tags.

## Evidence and rights review

Confirm author names, affiliation, funding, conflicts, AI-assistance disclosure,
license, manuscript date and peer-review status. Never invent a DOI or call a
working paper peer reviewed. Label retrospective, registered and exploratory
analyses accurately. State whether code and underlying data are actually included.

Read [the data policy](DATA_POLICY.md). Start from an explicit list of approved
files, not a copy of a research workspace. Review PDF metadata and attachments
when adding a new or revised PDF. Inspect all staged filenames and contents.

## Validation and versioning

After an approved paper change, regenerate its checksum file:

```sh
python3 tools/validate.py --write-checksums
python3 tools/validate.py
git diff --check
```

The validator does not change research results. It checks local links, table
export parity, metadata, inventories and hashes; CI repeats the checks. A
successful CI run is not scientific peer review or proof of reproducibility.

Use a paper-specific tag: `<slug>-v<version>`, for example
`fee-aware-passive-dca-v1.0`. Do not reuse or move a published paper tag. For a
correction, add a changelog entry, update the paper/catalog versions and publish
a new tag. Other papers keep their own versions.

## Release

Create an annotated tag on the reviewed commit and push it. Create a GitHub
Release for that exact tag, using the paper's release notes and approved PDFs.
Attach a separate `release-assets.sha256` covering the downloadable assets.
Verify the uploaded PDF hashes against the reviewed local originals.

The initial release includes English and Chinese PDFs, a paper-specific ZIP,
and their checksum list. GitHub's automatically generated source archives cover
the whole repository at the tag; the paper ZIP contains only that publication
and its research-material license.

Record the final public URL and commit. Do not imply that GitHub publication
provides a DOI, peer review, external validation or live-performance evidence.
GitHub Pages is not required: the reading site remains NomanTrade.
