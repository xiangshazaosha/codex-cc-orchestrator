# 点将台许可历史与过渡

| 范围/节点 | 根目录许可 | 说明 |
|---|---|---|
| [484fc7f 初始提交](https://github.com/xiangshazaosha/codex-cc-orchestrator/commit/484fc7f05825deb66780e99c5caa950093224dfc) | 未指定根 LICENSE | pyproject 当时亦无许可字段，不能推断默认 MIT |
| [2c596af](https://github.com/xiangshazaosha/codex-cc-orchestrator/commit/2c596afc29e38a9d1867295a59818a2c13bf0e30) 至 `3d08a41`，包括 `v0.4.0` | Non-Commercial Reciprocal Source License 1.0 | 已有禁商用、署名、分发/联网同许可公开源码及后三年提供义务 |
| 本次明确采用 2.0 的提交及 `0.4.1` 元数据 | 笑爷非商业同许可源码公开许可 2.0 | 功能仍同 0.4.0；升级许可，补清第三方/生成结果/敏感数据/贡献/补救及历史边界 |

旧正文保存在 [ncrs-1.0.txt](license-history/ncrs-1.0.txt)。其中原账号名 `zjgxkj` 作为历史署名原样保留；账号现名 `xiangshazaosha`，不以改名主张新取得全部贡献权利。

2.0 不追溯撤回旧版有效授权，也不自动将新改动按 1.0 授权。使用者可以依其合法取得的旧版授权判断旧版代码；包含新受保护改动时另看其适用许可。`v0.4.0` 标签保持不动，本次不发布新标签、发行包或改写 Git 历史。

尚未查到自有部分以 MIT/GPL 根许可证发布的历史记录，不是不存在其他授权或权属问题的证明。依赖 SDK 的 MIT 不等于本项目采用 MIT。
