# Noman Research · 研究资料库

[English](README.md) · [NomanTrade 研究网站](https://nomantrade.com/research/)

这是用于持续发布多篇独立研究的公开仓库，关注交易执行与市场结构。
每篇论文拥有独立目录、版本、引用信息和 Release，不与交易系统仓库混用。

## 已发布论文

| 编号 | 论文 | 作者 | 版本 |
| --- | --- | --- | --- |
| NR-2026-001 | [费用感知型被动定投：比特币积累策略的 K 线证据与零售规模可行性](papers/2026/fee-aware-passive-dca/README.zh-CN.md) | 陶涛 · 独立研究者 | v1.0 · 2026-10-09 |

第一篇论文包含完整中英文正文、附录、中英文 PDF、原创图表和已发表聚合表。
主实验中，五档策略的模型数量优势为 9.5065 bps，其中手续费贡献为
+10.3775 bps、价格路径贡献为 −0.8710 bps；固定单档策略更好，为 12.8327 bps。
这些结果不是年化收益，也不证明真实 maker 成交。论文尚未经过同行评审。

[网站阅读全文](https://nomantrade.com/research/can-limit-orders-improve-dca/) · [下载首篇论文 Release](https://github.com/MagicTaoT/noman-research/releases/tag/fee-aware-passive-dca-v1.0)

## 后续发布方式

论文按 `papers/<年份>/<论文标识>/` 存放；版本标签采用
`<论文标识>-v<版本号>`，避免多篇论文共用一个全局版本号。
[catalog.json](catalog.json) 是机器可读目录；
[发布指南](docs/PUBLISHING.md) 与 [论文模板](templates/paper/README.md)
用于后续新增论文。

只发布审核后的研究材料，不发布原始或衍生 K 线、L2 数据、账户账本、
密钥及生产服务器配置。首篇发布包不包含回测引擎，不能仅凭此仓库独立重跑回测。

论文、原创图表及聚合表采用 [CC BY 4.0](LICENSE)；仓库维护工具采用
[MIT](tools/LICENSE)。第三方材料与市场数据不在授权范围内。
AI 工具使用情况见各论文声明，作者对研究内容承担责任。
