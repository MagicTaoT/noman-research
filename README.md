# Noman Research

Independent research on trading execution and market structure.

[中文](README.zh-CN.md) · [Read on NomanTrade](https://nomantrade.com/research/) · [Publication guide](docs/PUBLISHING.md)

This is a public library of papers, methods, original figures and aggregated
results. Each paper has its own directory, citation, version and release tag.
It is not the Noman trading application or a distribution of market data.

## Papers

| ID | Paper | Author | Version | Read |
| --- | --- | --- | --- | --- |
| NR-2026-001 | **Fee-Aware Passive DCA** — Candle-Only Evidence and Retail-Scale Feasibility for Bitcoin Accumulation | Tao Tao, Independent Researcher | v1.0 · 9 Oct 2026 | [Paper & downloads](papers/2026/fee-aware-passive-dca/README.md) · [中文](papers/2026/fee-aware-passive-dca/README.zh-CN.md) · [Website](https://nomantrade.com/research/can-limit-orders-improve-dca/) |

The machine-readable index is [catalog.json](catalog.json).

## Featured study: can limit orders improve DCA?

[![Pixel-art overview of the passive DCA study](papers/2026/fee-aware-passive-dca/figures/cover-pixel.png)](papers/2026/fee-aware-passive-dca/README.md)

The study examines 5,837,137 Coinbase BTC-USD one-minute candles. Under the
primary 15/30 bps fee scenario, the five-level controller produced a modeled
cash-weighted quantity edge of **9.5065 bps**. The decomposition was
**+10.3775 bps from fees** and **−0.8710 bps from the price path**. A fixed
one-level reference did better: **12.8327 bps**.

These are historical candle-model results, not demonstrated live fills or
annual investment returns. The working paper is not peer reviewed.

## Repository layout

```text
catalog.json                      Machine-readable paper index
papers/<year>/<paper-slug>/        One self-contained publication
  README.md                       Overview, downloads and evidence limits
  metadata.json                   Authors, dates, version and public links
  paper.md / paper.zh-CN.md        Full manuscripts
  appendix.md / appendix.zh-CN.md  Full technical appendices
  pdf/                            Versioned paper PDFs
  figures/                        Original figures and cover
  results/                        Published aggregate tables only
  citation.bib                    Citation for this paper
  SHA256SUMS                      File-integrity checksums
docs/                             Publication and data-release rules
templates/paper/                  Starting point for the next paper
tools/                            Publication checks, not trading/backtest code
```

## Versions and citation

Releases use **`<paper-slug>-v<version>`**, so papers can evolve independently.
The first is [fee-aware-passive-dca-v1.0](https://github.com/MagicTaoT/noman-research/releases/tag/fee-aware-passive-dca-v1.0).
Cite the individual paper using its `citation.bib`, rather than treating this
multi-paper repository as one research result. No DOI has been assigned to the
first paper.

## Data and licensing

Only approved publication materials belong here. Raw and derived candle
records, order-book feeds, account journals, credentials and production
configuration are excluded. See [the data policy](docs/DATA_POLICY.md).
The first release does **not** include the backtest engine or market data;
it is a publication package, not a standalone reproduction of the experiment.

Original research text, figures and aggregate tables are licensed under
[CC BY 4.0](LICENSE). The small repository-maintenance tools have a separate
[MIT license](tools/LICENSE). Linked third-party material and market data are
not covered by either grant.

For corrections or methodological questions, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Validate a checkout

```sh
python3 tools/validate.py
```

This checks the catalog, local publication links, aggregate-table exports,
file inventories and checksums. It does not run a backtest or certify the
research conclusions.
