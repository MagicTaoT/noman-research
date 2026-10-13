# 费用感知型被动定投

**比特币积累策略的 K 线证据与零售规模可行性**

陶涛 · 独立研究者  
NR-2026-001 · 工作论文 v1.0 · 2026 年 10 月 9 日 · 未经同行评审

[English](README.md) · [全部论文](../../../README.zh-CN.md)

## 阅读与下载

- [完整中文正文](paper.zh-CN.md)与[技术附录 A–M](appendix.zh-CN.md)。
- [中文 PDF](pdf/fee-aware-passive-dca-working-paper-v1.0-zh-CN.pdf)。
- [完整英文正文](paper.md)、[英文附录](appendix.md)与[英文 PDF](pdf/fee-aware-passive-dca-working-paper-v1.0.pdf)。
- [NomanTrade 全文阅读版](https://nomantrade.com/research/can-limit-orders-improve-dca/)。
- [GitHub 版本发布与下载](https://github.com/MagicTaoT/noman-research/releases/tag/fee-aware-passive-dca-v1.0)。

## 主要发现

在既定定投现金投入计划上，加入限价挂单、显式未成交现金与有界 taker 补单，
能否扣除手续费后取得更多 BTC？本研究使用 5,837,137 根 Coinbase BTC-USD
一分钟 K 线检验这一问题。

在 15/30 bps maker/taker 主费率情景下，五档策略的现金加权数量优势为
9.5065 bps。其中价格路径贡献为 −0.8710 bps，手续费贡献为 +10.3775 bps。
固定单档策略达到 12.8327 bps，优于复杂的五档策略。

优势主要来自费率差，而非预测低点。论文还包括不同固定费率、下跌市场、
每月 2,500、10,000 与 100,000 美元预算及最小订单限制的探索性分析。
这些数值不是年化收益，K 线触价也不等于真实 maker 成交。

## 发布范围

本目录包含完整中英文论文与附录、原版 PDF、原创图表以及已发表的
[聚合表](results/README.md)。不包含原始或衍生行情、回测引擎、实盘交易代码、
账户账本和生产配置，因此不能仅凭此发布包独立重跑全部回测。

GitHub 发布时间为 2026 年 10 月 13 日，论文版本日期保持为 10 月 9 日。
PDF 与网站版本一致；Markdown 仅本地化图片链接与文档文件名，不更改研究结果。
附录中的历史证据包标识是溯源信息，不代表相关私有工作区已经公开。

[引用信息](citation.bib) · [元数据](metadata.json) · [校验清单](SHA256SUMS)

论文未分配 DOI，未经同行评审，不构成投资建议。资金、利益冲突及 AI 工具
使用情况见正文声明。原创研究材料采用 [CC BY 4.0](../../../LICENSE)。
