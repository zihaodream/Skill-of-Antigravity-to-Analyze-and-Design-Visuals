# ChatGPT / Codex 风格设计 Skill

基于Antigravity反重力原版语料独立适配，技能名为 **`ai-style-design`**。适用于能读取本地技能文件的Codex环境；本目录不会给普通ChatGPT网页聊天自动安装本地技能。

## 能力

- 风格溯源、颜色／材质／网格与叙事特征分析。
- 七项关键词初筛，以及结合上下文的同质化诊断和重写。
- 模式A情境推荐、模式B指定流派、模式C明确跨流派融合。
- 20个视觉流派和16个叙事流派，按需加载。
- 配色、材质、字阶、原创文案和通用生图提示词；实际图片生成取决于当前环境的生成工具。

## 安装

需要Python 3.10+。在本目录运行：

```shell
python install.py
```

默认安装到 `$CODEX_HOME/skills/ai-style-design`，未设置环境变量时是 `~/.codex/skills/ai-style-design`。目录已存在时拒绝覆盖。也可指定其他技能父目录：

```shell
python install.py --dest "目标技能父目录"
```

当前[官方本地发现文档](https://learn.chatgpt.com/docs/build-skills)还列出 `~/.agents/skills` 作为用户技能目录。若你的Codex只扫描该位置，可使用 `--dest` 安装到该目录；只选择一个发现位置，避免保留同名独立副本。

也可手动将整个 `ai-style-design/` 目录放入目标工程的 `.agents/skills/`。复制整个目录，不能只复制 `SKILL.md`。安装后下一轮输入 `$ai-style-design`，未显示时重启Codex。

## 使用示例

```text
使用 $ai-style-design，分析这张海报的流派、配色、材质与同质化问题。
使用 $ai-style-design，为高山冷萃乌龙茶制定包装与文案方案，先推荐流派。
使用 $ai-style-design，严格采用包豪斯，设计机械键盘宣传海报的视觉规范。
使用 $ai-style-design，融合瑞士网格与热带现代主义，为音乐节设计主视觉。
使用 $ai-style-design，修改这段文案，保留事实，去除套话和强制金句。
```

## 结构

```text
ai-style-design/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── catalog.md
│   ├── analyzer.md
│   ├── designer.md
│   ├── narrative-quality.md
│   ├── corpus_index.json
│   ├── diagnostic_rules.json
│   ├── visual/       # 20份原典
│   └── narrative/    # 16份原典
└── scripts/style_library.py
```

CLI只需Python标准库。例如在本目录运行：

```shell
python ai-style-design/scripts/style_library.py list --category visual
python ai-style-design/scripts/style_library.py show style-bauhaus
python ai-style-design/scripts/style_library.py search "茶 包装" --limit 3
python ai-style-design/scripts/style_library.py diagnose --text "赋能极致体验，蓝紫霓虹"
```

`search` 是词语子串匹配，中文可用空格拆分关键词，不是语义搜索。`diagnose` 是关键词初筛，不是AI检测；未命中不等于设计优秀。查看 `MIGRATION.md` 了解与原版的区别。新脚本未调用原版Gemini安装程序，不需要账号、API密钥或Node依赖。
