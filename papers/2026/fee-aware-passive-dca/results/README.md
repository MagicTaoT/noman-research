# Published aggregate tables

[tables.json](tables.json) exports all **12 tables** from the English
[manuscript](../paper.md) and [appendix](../appendix.md), in source order.

Every table includes its source filename, section title, column labels and
rows. All cell values remain strings so that published units, signs, rounding
and display precision are preserved. This is a faithful table transcription,
not a recomputation or a release of individual candle, order or obligation rows.

The tables cover the primary design, fee scenarios, frozen sample, primary
decomposition, policy comparison, yearly episodes, operational sensitivities,
falling-market summaries and the three retail-use-case matrices.

Interpret each table with its surrounding paper text. In particular:

- Bps are execution-quantity measures, not annualized investment returns.
- Primary, post-plan exploratory and illustrative-minimum results are distinct.
- Fee inputs and the USD 5 minimum are scenarios, not verified historical rules.
- The annual edge-value proxy is not investment profit.
- Overlapping falling-market panels are not independent market experiments.

The repository validator checks every exported cell against its Markdown
source. This verifies packaging fidelity, not the validity of the model or
the private backtest implementation. Raw/derived market data and the backtest
engine are excluded; the complete experiment cannot be rerun from this package alone.
