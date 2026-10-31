---
name: style-swiss-international
description: 国际主义平面设计风格（瑞士风格）Skill。基于严密数学网格、客观中立黑白摄影与无衬线字体，消灭主观装饰与泛滥插画，构建严谨信息构架。
---

# 风格定义：瑞士国际主义风格 (Swiss International Typographic Style)

> 源自《全球近现代设计美学全景图谱》第三篇第13章。

## 1. 风格灵魂与反同质化主张 (Soul & Anti-Homogenization)
- **核心哲学**：形式由内容与结构决定，设计师应当是客观中立的信息传递者。取法约瑟夫·米勒-布罗克曼 (Josef Müller-Brockmann) 与阿明·霍夫曼 (Armin Hofmann)。
- **AI 常见同质化缺陷**：文字排版漂浮无章、字阶混乱、随意添加发光装饰球、破坏网格对齐。
- **本 Skill 矫正法则**：
  1. 引入绝对的数学多栏柱状网格（Modular Column Grid）。
  2. 严禁用手绘乱线或华丽插画填充，必须使用客观纪实高反差黑白摄影。
  3. 字体强制左对齐右无拘（Flush left, ragged right），形成严格字阶对比。

## 2. 视觉 DNA 参数表 (Visual Parameter Matrix)
- **调色盘 (Precise 3-Color Hierarchy)**:
  - 纯黑印刷墨 (Solid Carbon Black): `#0A0A0A`
  - 极白纸张底 (Swiss Poster White): `#FFFFFF`
  - 信号瑞士红 (Signage Swiss Red): `#FF1801` (仅用于焦点信息点缀，比例 ≤5%)
- **版式系统与字体规范**:
  - 主标题：Helvetica Neue 75 Bold / Akzidenz-Grotesk，极大字号建立强烈的视觉锚点。
  - 正文：Helvetica Neue 55 Roman，9pt/13pt 严格基线网格（Baseline Grid）。
  - 对齐方式：左齐右不齐，严禁两端强制对齐导致的不规则字距。
- **空间与数学网格**:
  - 采用标准 12 栏或 8 栏网格系统，栏间距（Gutter）恒定为 16px/24px。
  - 对角线黄金分割构图，色块与文字紧贴网格线。

## 3. 负向禁忌词库 (Negative Prompt & Anti-Patterns)
`FORBIDDEN`:
- NO ornamental borders, NO decorative drop shadows (严禁装饰花边与投影)
- NO pastel color gradients, NO skeuomorphic textures (严禁马卡龙渐变与仿皮质/玻璃拟物)
- NO centered text alignments for long paragraphs (严禁长段落文字居中)
- NO serif calligraphy or cursive handwritten scripts (严禁衬线书法手写花体)

## 4. 图像与版面生成提示词引擎 (Prompt Engine)
- **Positive Prompt**:
  > Vintage Swiss Graphic Design poster from 1968, designed by Josef Müller-Brockmann, asymmetric 12-column modular grid composition, ultra-clean typography in Helvetica Neue bold and regular, high contrast black and white documentary photography of mechanical turbine geometry, bold red solid rectangle accent `#FF1801`, pure white background, flush left ragged right, mathematical precision, matte uncoated paper texture, museum exhibition grade archival print.
- **Negative Prompt**:
  > decorative ornaments, gradient background, 3d glossy, soft focus, neon glow, watercolor, handwritten calligraphy, centered typography, messy layout, lens flare.

## 5. 平面与排版指南
- 强制使用无衬线字体体系，严禁任何投影、描边与外发光。
- 图片严格贴合栅格边界，禁止随心所欲的不规则裁切或圆角（除非网格模块本身为圆弧）。

## 6. 配套文字修辞推荐
- 协同 Skill：`voice-jobs-clarity`（激进清澈体）或 `voice-ogilvy-fact`（事实密集流）。
