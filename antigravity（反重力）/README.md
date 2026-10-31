# Antigravity（反重力）原版备份

这是原项目的独立快照，供 Gemini／Antigravity 相关环境保留、迁移和研究。`ai-style-design/` 中的原文件逐字节保留，未进行Codex适配。

## 内容

- `ai-style-design/SKILL.md`：原版总入口。
- `ai-style-design/skills/visual/`：20个视觉流派。
- `ai-style-design/skills/narrative/`：16个叙事流派。
- `ai-style-design/skills/interfaces/`：分析与设计接口；顶层两个接口目录为原项目已有副本。
- `ai-style-design/scripts/`：原版构建、分析、设计和安装脚本。
- `ai-style-design/README.md`：原版美学长文；`PROGRESS.md`、框架文档、JSON索引及清单一并保留。
- `SOURCE_MANIFEST.json`：原版文件相对路径及SHA-256。`.agents/skills/` 下的两个Windows目录联接在快照中展开为普通文件夹，以便GitHub存储和跨机复制。

## 使用

先从本目录的 `ai-style-design/` 阅读原版 `SKILL.md`。原版命令示例：

```shell
cd ai-style-design
python scripts/style_analyzer.py --input "需要分析的设计描述"
python scripts/style_designer.py --query "高山乌龙茶包装"
```

原版 `scripts/install_to_antigravity.py` 会复制技能、创建目录联接并修改Gemini配置；迁移时先阅读该脚本，再在目标环境中自行决定是否运行。本次整理没有运行它。原版包含作者机器的绝对路径、旧版模型参数和历史描述差异，这些为保证备份一致而保留。若要使用Codex，请安装相邻 `chatgpt（codex）/` 中的版本。

## 完整性

在整个发布目录运行 `python tools/verify_release.py` 可以核对备份。校验信息和适配说明放在备份目录外，原载荷不插入额外文件。
