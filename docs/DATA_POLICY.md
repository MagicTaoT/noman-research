# Public-material boundary

## Allowed after review

- Author-approved full manuscripts and technical appendices.
- Paper PDFs, original explanatory figures and covers.
- Aggregated tables already approved for publication.
- Publication metadata, citations, changelogs and file-integrity checksums.
- Explicitly reviewed methodology and evidence-limit statements.

## Excluded

- Raw or derived candle rows, L2 books and tick/trade datasets.
- Account- or order-level journals, user records, portfolio information and logs.
- Credentials, private keys, environment files, machine paths and server access details.
- Production trading code and internal operations/deployment documents.
- Unreviewed workspace exports or third-party content without redistribution rights.

A new paper does not automatically authorize new data or code disclosures.
Each paper's `metadata.json` and README must state its actual release scope.
Aggregated tables are not raw market records and do not substitute for the
data and code needed to rerun an empirical study.

The first paper publishes results only. Backtest code is not included. Its
published appendix contains historical protocol identifiers and hashes as
provenance references; the underlying private research workspace is not shipped.

The `.gitignore` and automated validation are preventive checks, not a
complete secret scanner or a substitute for a human review. Before publication,
inspect every staged filename and review the contents of newly added files.
