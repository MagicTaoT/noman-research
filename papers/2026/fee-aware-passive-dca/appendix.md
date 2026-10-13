# Appendix: Fee-Aware Passive DCA

**Tao Tao** — Working Paper v1.0  
This appendix accompanies `paper.md`. Sections A–H report the locked study; Sections I–L report post-plan exploratory extensions.

## A. Terminology and evidence levels

- **Obligation:** cash created at a scheduled slot.
- **Simulated passive fill:** cash satisfying the registered candle penetration, delay, haircut, and capacity rules. It is not a confirmed maker fill.
- **Backlog:** obligation cash not yet resolved by a simulated passive fill or taker catch-up.
- **Catch-up:** cash moved from passive backlog to pending taker execution under the cap rule.
- **Cash-weighted edge:** cash-weighted mean of obligation-level relative BTC quantity differences, in bps.
- **Registered evidence:** frozen protocol `MLDCA-EP-1.1`, including the two-minute USD 10 primary test.
- **Exploratory evidence:** fee, down-period, wealth, and retail-use-case extensions designed after the primary work.

## B. State transitions

For arrival `c_t`, prior backlog `B_t^-`, catch-up speed `alpha`, and maximum passive multiple `M`:

`I_t = B_t^- + c_t`,

`P_t = min(I_t, c_t + alpha B_t^-, M c_t)`.

For rung weights `w_k`, limits `L_tk`, acceptance indicators `a_tk`, and fill fractions `phi_tk`:

`m_tk = a_tk phi_tk P_t w_k`.

After passive processing, `J_t = I_t - sum(m_tk)`. For backlog cap `H`, the registered controller moves `max(0, J_t - H)` to pending taker execution no earlier than the next executable slot. Pending cash remains pending if capacity prevents completion.

## C. Registered order lifecycle

Each registered order lives for the two one-minute candles in its slot. With a one-minute activation delay, only the second candle can trigger. The low must penetrate the limit by 1 bp. A triggered rung requests 50% of planned cash and shares capacity equal to 1% of that minute's `volume × open`. Triggered rungs receive capacity pro rata. At slot end, unfilled passive cash returns to backlog. During the 24-hour settlement buffer, no new obligations arrive.

## D. Frozen sample

| Item | Frozen value |
|---|---:|
| Product | BTC-USD |
| One-minute OHLCV rows | 5,837,137 |
| First timestamp | 2015-07-20 00:00 UTC |
| Last timestamp | 2026-10-06 23:59 UTC |
| Duplicate / out-of-order / invalid OHLC rows | 0 / 0 / 0 |
| Below-USD-10 minute-notional rows | 13,130 |
| Development cut | 2022-04-13 00:00 UTC |
| Test cut | 2024-07-10 00:00 UTC |
| Test obligations | 588,240 |
| Cash per test counterfactual | USD 5,882,400 |

## E. Registered primary result and decomposition

| Metric | Result |
|---|---:|
| Cash-weighted edge | 9.5065 bps |
| One-sided lower 95% bound | 9.2565 bps |
| Percentile upper 95% bound | 9.7626 bps |
| One-sided p-value vs 1 bp | 0.00010 |
| Aggregate-unit edge | 9.4487 bps |
| Cash-weighted price component | -0.8710 bps |
| Cash-weighted passive-fee component | +10.3775 bps |
| Simulated passive cash share | 69.27% |
| Taker catch-up share | 30.73% |
| Average backlog | USD 134.31 |
| Maximum pre-catch-up backlog | USD 2,090.00 |

## F. Registered strategy comparison

| Strategy | Edge | Passive share | Average backlog |
|---|---:|---:|---:|
| Fixed one-level passive | 12.8327 bps | 95.60% | USD 67.92 |
| Adaptive one-rung | 11.0270 bps | 79.12% | USD 112.25 |
| Adaptive five-rung | 9.5065 bps | 69.27% | USD 134.31 |

Five-minus-fixed was -3.3262 bps, 95% interval [-3.4900, -3.1543].

## G. Independent registered year episodes

| Episode | Cash-weighted edge | Status |
|---|---:|---|
| 2015 | 4.8555 bps | Partial year |
| 2016 | 4.1096 bps | Full year |
| 2017 | 2.6003 bps | Full year |
| 2018 | 5.4409 bps | Full year |
| 2019 | 7.3855 bps | Full year |
| 2020 | 8.1129 bps | Full year |
| 2021 | 9.4031 bps | Full year |
| 2022 | 10.3973 bps | Full year |
| 2023 | 8.8116 bps | Full year |
| 2024 | 9.3948 bps | Full year |
| 2025 | 9.5266 bps | Full year |
| 2026 | 9.5616 bps | Partial year |

Episodes are initialized and settled independently. They are serially and economically related, not 12 independent markets.

## H. Registered operational sensitivities

| Change from primary | Edge | Passive share |
|---|---:|---:|
| Activation delay 0 min | 11.7561 bps | 76.72% |
| Activation delay 1 min | 9.5065 bps | 69.27% |
| Activation delay 2 min | -0.0438 bps | 0.00% |
| Participation 0.1% | 9.4916 bps | 69.16% |
| Participation 100% | 9.5066 bps | 69.27% |
| Full-on-breach catch-up | 8.1850 bps | 60.24% |
| Age-cap catch-up | 9.4825 bps | 69.08% |

Across 732 dynamic runs, 687 were valid and 45 ended with unresolved cash. Invalid rows retain missing edge.

## I. Exploratory constant-fee scenarios

| Strategy | Component | 15/30 | 35/75 | 50/90 |
|---|---|---:|---:|---:|
| Fixed one-level | Total edge | 12.8327 | 36.6180 | 36.5611 |
| Adaptive one-rung | Total edge | 11.0270 | 30.7164 | 30.6693 |
| Adaptive five-rung | Total edge | 9.5065 | 26.7472 | 26.7060 |
| Adaptive five-rung | Price | -0.8710 | -0.8710 | -0.8710 |
| Adaptive five-rung | Fee | 10.3775 | 27.6182 | 27.5770 |

The execution path is held fixed while fees are repriced. These are scenario labels, not current official tier claims.

## J. Exploratory falling-market panels

Mechanical selection produced 15 observations across three panels:

| Panel | Selection | Positive price observations |
|---|---|---:|
| D1 | Negative full years: 2018, 2022, 2025 | 0 / 3 |
| D2 | Five consecutive negative-month episodes | 0 / 5 |
| D3 | Seven severe negative months | 2 / 7 |
| Combined | All observations | 2 / 15 |

The positive price observations were June 2022 (+0.9151 bps) and June 2026 (+0.4290 bps). All 15 fee-inclusive observations were positive under all three fixed fee scenarios. Minimum total edges were 5.0444 bps at 15/30, 20.2436 bps at 35/75, and 20.2082 bps at 50/90.

## K. Exploratory retail-use-case matrices

### K.1 Initial slot sizes in a 31-day month

| Slot | Monthly budget | One-level order | Five-rung child |
|---:|---:|---:|---:|
| 5 min | USD 2,500 | USD 0.280 | USD 0.056 |
| 5 min | USD 10,000 | USD 1.120 | USD 0.224 |
| 5 min | USD 100,000 | USD 11.201 | USD 2.240 |
| 60 min | USD 2,500 | USD 3.360 | USD 0.672 |
| 60 min | USD 10,000 | USD 13.441 | USD 2.688 |
| 60 min | USD 100,000 | USD 134.409 | USD 26.882 |

### K.2 Fractional-order branch

Maximum cross-budget edge difference was 2.198e-10 bps. One representative budget is shown.

| Slot | Strategy | 35/75 edge | 50/90 edge | 35/75 passive share |
|---:|---|---:|---:|---:|
| 5 min | Fixed one-level | 37.0716 | 37.0142 | 96.34% |
| 5 min | Adaptive one-rung | 28.0981 | 28.0558 | 71.00% |
| 5 min | Adaptive five-rung | 25.5483 | 25.5095 | 65.05% |
| 60 min | Fixed one-level | 26.0523 | 26.0118 | 68.06% |
| 60 min | Adaptive one-rung | 14.1318 | 14.1105 | 35.70% |
| 60 min | Adaptive five-rung | 12.1106 | 12.0923 | 30.72% |

### K.3 Illustrative USD 5 minimum, 35/75 scenario

| Slot | Monthly budget | Strategy | Edge | Passive share | Annual edge-value proxy |
|---:|---:|---|---:|---:|---:|
| 5 min | USD 2,500 | Fixed one | -0.3062 | 0.00% | USD -0.92 |
| 5 min | USD 2,500 | Adaptive five | -0.3062 | 0.00% | USD -0.92 |
| 5 min | USD 10,000 | Fixed one | -0.1762 | 0.00% | USD -2.11 |
| 5 min | USD 10,000 | Adaptive five | -0.1762 | 0.00% | USD -2.11 |
| 5 min | USD 100,000 | Fixed one | 37.0633 | 96.34% | USD 4,447.60 |
| 5 min | USD 100,000 | Adaptive five | 25.5434 | 65.04% | USD 3,065.21 |
| 60 min | USD 2,500 | Fixed one | 25.8548 | 68.06% | USD 77.56 |
| 60 min | USD 2,500 | Adaptive five | -0.4484 | 0.00% | USD -1.35 |
| 60 min | USD 10,000 | Fixed one | 26.0728 | 68.06% | USD 312.87 |
| 60 min | USD 10,000 | Adaptive five | -0.4347 | 0.00% | USD -5.22 |
| 60 min | USD 100,000 | Fixed one | 26.0523 | 68.06% | USD 3,126.27 |
| 60 min | USD 100,000 | Adaptive five | 12.1106 | 30.72% | USD 1,453.27 |

The annual proxy equals annual contribution multiplied by modeled bps; it is not investment profit. The USD 5 threshold is illustrative, not a dated historical Coinbase rule.

## L. Wealth identity and unsupported claims

For a common terminal mark `P_T`, no sales, and no reinvestment, terminal crypto wealth is `W = q P_T`. Therefore

`W_S / W_B - 1 = q_S / q_B - 1`.

There is no extra compounding factor beyond the acquired-quantity edge under this policy. Exploratory independently reset calendar-year episodes produced combined quantity edges of 4.8228, 14.0256, and 14.0036 bps under the three fee scenarios.

The evidence does **not** support these claims:

- DCA is superior to lump-sum investing.
- A candle penetration is a real maker fill.
- The fee scenarios are current official Coinbase tiers.
- The model earns the stated bps live or in the future.
- Five adaptive rungs forecast short-term lows.
- Falling markets reliably create price advantage.
- Execution bps compound exponentially without reinvestment.
- Small child orders satisfied every historical venue rule.
- Results generalize beyond Coinbase BTC-USD.
- Exchanges intentionally choose recurring-order mechanics to exploit users.

## M. Reproducibility anchors

- Governing protocol SHA-256: `22cbbdcc33576bff02a77e1516def4d1f475cf88869521143fdc7ce2f13d8cc8`
- Registered manifest: `evidence_release_v1/RELEASE_MANIFEST.json`
- Registered checksums: `evidence_release_v1/RELEASE_SHA256SUMS`
- Fee/down/wealth extension: `MLDCA-EXT-1.0.1_dbd6152d`
- Retail-use-case extension: `MLDCA-RETAIL-1.0_e69f0a29`
- Raw market data are intentionally excluded from public release.
