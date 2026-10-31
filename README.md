# 视觉与叙事风格 Skill：Antigravity 原版与 Codex 适配版

Just a skill available for the anti-gravity AI to call: used to create or analyze content in different styles：I'm fed up with AI designs being almost homogeneous and ugly, so I collected different cultural and aesthetic styles from human history and made them into skills for AI to use.

这份目录可整体上传到GitHub。两套版本独立保存，源项目未修改。

| 目录 | 内容 | 入口 |
| --- | --- | --- |
| [antigravity（反重力）](antigravity（反重力）/README.md) | Gemini／Antigravity原版文件快照 | `ai-style-design/SKILL.md` |
| [chatgpt（codex）](chatgpt（codex）/README.md) | 可独立安装的Codex版本 | `ai-style-design/SKILL.md` |

## 快速开始

Codex用户进入 `chatgpt（codex）/`，运行 `python install.py`，下一轮使用 `$ai-style-design`。安装目标、其他发现目录与使用示例见该目录README。反重力用户参见原版目录说明。

两版都包含20个视觉流派和16个叙事流派。原版还保留两个平台接口及其已有副本；Codex以一个技能入口按需读取资料，不把接口数算作新的流派。

## 校验

需要Python 3.10+；在本目录执行：

```shell
python tools/verify_release.py
```

原源目录仍在本机时，还可比对源文件没有变化：

```shell
python tools/verify_release.py --source "原项目目录"
```

`antigravity（反重力）/SOURCE_MANIFEST.json` 记录原版文件哈希；`RELEASE_MANIFEST.json` 覆盖本次发布文件。`VERIFICATION.md` 记录本次已做的检查。

## 上传GitHub

可以把本目录的全部内容放到仓库根目录，也可以保留为已有仓库的子目录。GitHub网页上传时保留文件夹层级和中文目录名；建议通过Git客户端提交整个目录，以包含 `.agents` 等隐藏目录。`.gitignore` 排除了Python缓存和常见本地临时文件。

本次交付仅整理本地发布文件，没有创建GitHub仓库、提交或推送。没有将机器账号配置、密钥或外部安装目录打包。完整原版为忠实备份仍含原作者本地路径；Codex执行入口采用相对路径。

## 来源与许可

内容来自同一份反重力设计风格知识库。快照日期：2026-10-31。Codex迁移细节见 [MIGRATION.md](chatgpt（codex）/MIGRATION.md)。原版 `package.json` 有MIT声明但未提供LICENSE文件，本次未另行补写许可证。

Codex技能结构与本地发现位置参考 [OpenAI官方技能文档](https://learn.chatgpt.com/docs/build-skills)。
