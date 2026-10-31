---
name: style-ui-waves
description: 数字交互三次浪潮 Skill。系统解析拟物化(皮革/金属高光) -> 纯色扁平化(极速响应) -> 空间玻璃拟态(多维深度/Backdrop-blur)的度规法则，杜绝混乱劣质UI。
---

# 风格定义：数字交互三次浪潮 (UI Evolution: Skeuomorphic, Flat & Spatial Glassmorphism)

> 源自《全球近现代设计美学全景图谱》第三篇第19章。

## 1. 风格灵魂与反同质化主张 (Soul & Anti-Homogenization)
- **核心哲学**：自2007年初代iPhone至今人机交互界面的三次深刻审美跃迁：1. 拟物化（Skeuomorphism, 建立人机信任的皮革缝线与真实玻璃反光）；2. 扁平化（Flat Design, 移动互联网爆发期的效率优先与纯色无阴影）；3. 空间计算玻璃拟态（Spatial Glassmorphism / visionOS, 空间维度中具有真实物理光学厚度与景深微模糊的多维悬浮面板）。
- **AI 常见同质化缺陷**：生成混乱无逻辑的假发光UI按钮、脏乱的渐变马卡龙色块、缺乏圆角连续性（Squircle）与基线对齐的漂浮文字。
- **本 Skill 矫正法则**：
  1. **空间多维物理玻璃拟态 (Spatial Glass Optics)**：背景毛玻璃实时模糊（Backdrop-filter: blur 30px）、精细 1px 半透明内描边高光（Inner border highlight 0.5px rgba(255,255,255,0.2)）。
  2. **精确的 8pt 空间网格度规**：所有外边距、内边距与组件高度均严格倍乘于 8px/4px 黄金模度。
  3. **超高动态多层弥散投影**：多层透明度深度衰减微投影（0 10px 40px rgba(0,0,0,0.08)），构建克制通透的悬浮空间层级。

## 2. 视觉 DNA 参数表 (Visual Parameter Matrix)
- **调色盘 (Restricted Palette)**:
  - 空间深空灰黑 (Spatial Dark Obsidian): `#1C1C1E` (高维空间操作界面背景, 占50%)
  - 苹果纯透玻璃白 (Frosted Crystal Glass White): `rgba(255,255,255,0.65)` (悬浮多维卡片基座, 占30%)
  - 系统电光聚焦蓝 (System Electric Focus Blue): `#007AFF` (主行动按钮与状态指示, 占10%)
  - 次级层级微光灰 (Subtle Interface Slate): `#8E8E93` (次级辅助信息与分割基线, 占10%)
- **材质微观肌理 (Materials & Textures)**:
  - 精细喷砂物理亚克力与半透明多层光学毛玻璃 (Fine-sandblasted translucent optical frosted glass with real-time dynamic refraction)
  - 边缘极细高光倒角切面 (Precision 1px inner border specular highlight edge chamfer)
  - 空间深度微多层弥散空气阴影 (Multi-layered ultra-soft spatial ambient occlusion shadows)
  - 超清视网膜高像素点对点显示面板 (Retina crystal display precision with vector subpixel rendering)
- **光学系统与镜头 (Lighting & Optics)**:
  - 悬浮于虚空中的环境漫射全色域天光，透过半透卡片显现后方背景微妙的色相折射与景深虚化 (Depth-of-field blur)。
  - 严禁刺眼的人工荧光外发光球与油腻廉价的塑料高光。
- **版式系统与构图网格 (Composition & Grid)**:
  - 构图：严格 8pt 柱状网格系统，圆角采用苹果连续曲率超椭圆（Continuous Squircle Corner Radius 24px/32px）。
  - 排版：SF Pro Display / Inter 字体体系，严格 110%/130% 基线网格（Baseline rhythm）。

## 3. 负向禁忌词库 (Negative Prompt & Anti-Patterns)
`FORBIDDEN`:
- NO messy random button gradients, NO arbitrary irregular corner radiuses
- NO heavy muddy black drop shadows, NO unaligned floating text elements
- NO outdated 90s web bevel emboss, NO unreadable neon text without contrast

## 4. 图像生成提示词注入模板 (Prompt Engine)
- **Positive Prompt**:
  > Ultra-premium Spatial Operating System Glassmorphism UI dashboard concept, inspired by Apple visionOS and modern spatial interfaces. Floating multi-layered translucent frosted glass cards with authentic optical backdrop blur (30px blur), crisp 1px subtle white inner border highlight `rgba(255,255,255,0.2)`. Deep space obsidian backdrop `#1C1C1E` with subtle ambient light refraction. Elegant system blue `#007AFF` action toggles, perfectly aligned typographic hierarchy in San Francisco Pro font. Flawless 8pt grid structure, continuous smooth squircle corners, pristine digital clarity, 8k UI/UX portfolio presentation.
- **Negative Prompt**:
  > messy ui, ugly gradients, bad typography, heavy black drop shadow, blurry icons, 90s bevel, skeuomorphic fake leather, misaligned buttons, low resolution.

## 5. 平面与排版指南 (Graphic Layout Rules)
- **主标题与数字**：SF Pro Rounded / Inter SemiBold，极大字阶形成强烈的数字仪表盘视觉锚点。
- **正文与微标签**：SF Pro Text Regular 13pt / 11pt 等宽数字，字距紧致整洁。

## 6. 配套文字修辞推荐 (Harmonized Copywriting Voice)
- 协同 Skill：`voice-jobs-clarity`（激进清澈体）或 `voice-ogilvy-fact`（事实密集流）。
