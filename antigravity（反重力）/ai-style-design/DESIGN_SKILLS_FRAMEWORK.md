# 世界设计流派转化为 AI 抗同质化 Skill 开发总纲与工程规范

> 本规范基于本项目《全球近现代设计美学与文字叙事风格全景图谱》(README.md) 精炼并拓展而来。旨在为后续构建全套“世界各大设计风格”的 AI Agent Skill 提供标准化的开发架构、参数字典、反同质化负向约束及提示词注入引擎。

---

## 目录
1. [AI 设计同质化的核心病征与破局机理](#1-ai-设计同质化的核心病征与破局机理)
2. [Skill 架构分层与目录拓扑](#2-skill-架构分层与目录拓扑)
3. [风格精简与基因提取全景图 (Visual & Voice DNA)](#3-风格精简与基因提取全景图)
4. [标准设计 Skill 规范模板 (SKILL.md Specification)](#4-标准设计-skill-规范模板)
5. [标杆示范 1：当代东方文人写意 Skill (`style-neo-chinese-zen`)](#5-标杆示范-1当代东方文人写意-skill)
6. [标杆示范 2：瑞士国际主义风格 Skill (`style-swiss-international`)](#6-标杆示范-2瑞士国际主义风格-skill)
7. [标杆示范 3：拉美热带现代主义 Skill (`style-tropical-modernism`)](#7-标杆示范-3拉美热带现代主义-skill)
8. [后续工程化路线图与持续演进](#8-后续工程化路线图与持续演进)

---

## 1. AI 设计同质化的核心病征与破局机理

通用大模型（Midjourney、Stable Diffusion、DALL-E、各类 LLM 文案工具）在缺乏精准约束时，极易陷入**高频统计众数的平庸陷阱**：

| 同质化病征维度 | AI 默认同质化表现 (Default Output) | Skill 破局机理 (Skill Anti-Homogenization Engine) |
| :--- | :--- | :--- |
| **材质肌理** | 塑料感、光滑次表面散射(SSS)、无瑕疵3D渲染 | **物理物质锚定**：强制指定纸浆纤维、宣纸洇散、粗糙混凝土气孔、生铁氧化、木纹裂理等时代物理痕迹。 |
| **色彩体系** | 泛滥的蓝紫赛博霓虹、通用水果糖马卡龙渐变 | **受限特调色盘 (Restricted Palette)**：限定 2-4 种高辨识度主辅色，附带精准 HEX 码与色阶比例（如60-30-10原则）。 |
| **构图与空间** | 大头居中、主体膨胀填满、景深虚化过度 | **空间拓扑与留白率**：强制数学网格（如九宫格、对角线构图）、极端不对称、规定负空间留白率（如 ≥60% 计白当黑）。 |
| **光影与光学** | 戏剧性体积光、泛滥的高光边缘光(Rim Light) | **特定光学模拟**：指定日光角度（如正午垂直热带硬光、清晨漫射天光）、老胶片颗粒度、无暗房阴极光。 |
| **文案修辞** | “在当今快节奏的社会中”、“打造极致体验”等套话 | **冷硬骨力与微观感官注入**：限定动名词比例，剔除虚饰副词，采用短句切割或精准心理通感。 |
| **样板戏人设** | “咬着没点的烟”、“吃了不烧心/是它的本分”式的刻奇民间哲人 | **世俗毛刺与去表演化**：坚决剔除扫地僧式装逼，注入真实生活中的疲倦、算账、粗糙、尴尬与未闭环动作。 |
| **叙事与反讽** | 潜台词打在公屏上（“致全体耗材”）、设定词过载、金句强迫症 | **死鱼眼冷面法则 (Deadpan)**：越是荒谬越要官方正经，留白由读者自行心领神会，拒绝三段式金句预制菜。 |

---

## 2. Skill 架构分层与目录拓扑

项目后续将以模块化、高复用、即插即用的方式组织技能仓库：

```
f:\ai风格设计\
├── README.md                          # 全景知识库原典
├── DESIGN_SKILLS_FRAMEWORK.md         # 架构总纲与开发规范（本文件）
└── skills/                            # 标准化 Skill 根目录
    ├── visual/                        # 视觉设计流派 Skills
    │   ├── style-haipai-artdeco/      # 民国海派与月份牌
    │   ├── style-socialist-realism/   # 红色现实主义与工业木刻
    │   ├── style-neo-chinese-zen/     # 当代东方写意/新中式
    │   ├── style-neo-guochao/         # 新国潮与赛博机能
    │   ├── style-wabi-sabi/           # 日系物哀/侘寂与原白
    │   ├── style-tropical-modernism/  # 拉美热带现代主义
    │   ├── style-islamic-geometric/   # 伊斯兰几何与当代书写
    │   ├── style-arts-crafts/         # 英国工艺美术运动
    │   ├── style-art-nouveau/         # 新艺术运动
    │   ├── style-bauhaus/             # 包豪斯功能主义
    │   ├── style-art-deco/            # 装饰艺术风格
    │   ├── style-swiss-international/ # 瑞士国际主义排版
    │   ├── style-midcentury-modern/   # 中世纪现代主义 (MCM)
    │   ├── style-pop-art/             # 波普与迷幻艺术
    │   ├── style-brutalist/           # 粗野主义与反设计
    │   ├── style-memphis/             # 后现代孟菲斯风格
    │   ├── style-grunge-acid/         # 垃圾排版与解构酸性
    │   └── style-y2k-cyberpunk/       # 千禧未来与赛博谱系
    ├── narrative/                     # 叙事文案流派 Skills
    │   ├── voice-luxun/               # 鲁迅冷峻匕首体
    │   ├── voice-zhangailing/         # 张爱玲世俗苍凉工笔
    │   ├── voice-wangzengqi/          # 汪曾祺民间平淡白描
    │   ├── voice-wangjiawei/          # 王家卫都市疏离体
    │   ├── voice-xushunying/          # 许舜英意识流符号学
    │   ├── voice-lixinpian/           # 李欣频感官避难所体
    │   ├── voice-neo-oriental/        # 新东方风土嗅觉体
    │   ├── voice-yemaozhong/          # 叶茂中冲突铁锤体
    │   ├── voice-ogilvy-fact/         # 奥格威事实密集流
    │   ├── voice-bernbach-negative/   # 伯恩巴克自嘲逆向体
    │   ├── voice-neilfrench/          # 尼尔·法兰奇傲慢长文
    │   ├── voice-hemingway/           # 海明威冰山电报体
    │   ├── voice-wieden-kennedy/      # W&K 存在主义运动史诗
    │   ├── voice-jobs-clarity/        # 乔布斯激进清澈体
    │   ├── voice-proust-synesthesia/  # 普鲁斯特微观通感
    │   └── voice-japanese-restraint/  # 日系日常节制絮语
    └── presets/                       # 跨媒介声色合一完整预设 (Presets)
        ├── preset-oriental-salonavant/# [新中式视觉 + 新东方嗅觉文案]
        ├── preset-swiss-precision/    # [瑞士排版 + 乔布斯激进清澈体]
        ├── preset-vintage-shanghai/   # [民国海派 + 张爱玲苍凉工笔]
        └── preset-brutalist-critique/ # [粗野主义 + 许舜英符号批判]
```

---

## 3. 风格精简与基因提取全景图

从 README 原典中提取世界 17 大视觉风格与 16 种修辞流派的**极简基因锁（Style DNA Keys）**：

### 3.1 视觉风格基因提取表 (Visual Style DNA)

| 技能标识符 | 核心视觉符号 | 材质物理特征 | 经典调色盘 (Hex) | 空间/网格律令 |
| :--- | :--- | :--- | :--- | :--- |
| `style-haipai-artdeco` | 擦笔水彩、修长旗袍、留声机、西式壁炉 | 缎面高光、铜绿铸铁、旧石库门砖雕 | 胭脂红 `#9E2A2B`、洋金 `#D4AF37`、墨青 `#1E3F66` | 装饰画框居中，四周对称花纹包边 |
| `style-socialist-realism`| 仰视工农兵、麦穗齿轮、朝阳曙光、粗红旗 | 新兴木刻刀刻刮痕、粗糙牛皮纸、铸铁重机 | 革命朱红 `#C91B1B`、工业亮黄 `#F6BA13`、苏式暖褐 `#5E3A24` | 仰角对角线透视，巨大体量感压迫 |
| `style-neo-chinese-zen` | 瓦爿残砖、水墨浓淡、竹节光影、枯石 | 生宣自然水渗、哑光素烧陶瓷、原木细纹 | 瓦黛黑 `#2B2B2B`、宣纸原白 `#F4EFEA`、冷灰竹青 `#7B8B6F` | 留白率 ≥65%，极端非对称，气韵流动 |
| `style-wabi-sabi` | 枯山水、残缺茶碗、飘落枯叶、单色几何 | 风化木材、砂石表面、无釉粗陶、原棉麻布 | 枯草灰 `#8C877D`、泥土赭 `#5A4D41`、素白灰 `#E6E5E1` | 去中心化，边缘留白，幽暗低照度阴翳 |
| `style-tropical-modernism`| 粗实粉墙、热带仙人掌、穿透性柱光、水池 | 粗拉毛水泥灰浆、手工烧结陶砖、静止平水面 | 墨西哥粉 `#E03576`、暴烈钴蓝 `#154388`、铁锈黄 `#D8861B` | 极高对比硬阴影，纯几何大体量实墙切割 |
| `style-islamic-geometric`| 八角星轮、阿拉伯藤蔓纹、无尽细密拓扑 | 镂空黄铜屏风(Mashrabiya)、彩色釉面瓷砖(Zellige) | 绿松石青 `#00A896`、纯金箔 `#E5A93B`、深群青 `#1A237E` | 全对称自相似迭代几何，数学逻辑无限延展 |
| `style-bauhaus` | 红黄蓝纯色、悬挑钢管、无衬线粗体、机械齿轮 | 镀铬冷光钢管、压铸胶木、工业平板玻璃 | 纯三原色：红 `#DE3831`、蓝 `#0055A5`、黄 `#FFCC00`、纯黑白 | 严格功能主义网格，90度直角与标准正圆 |
| `style-swiss-international`| Helvetica 粗体、纯黑白摄影、三段式网格 | 无纹理铜版纸、高对比柯达黑白底片 | 印刷实黑 `#0A0A0A`、纯白 `#FFFFFF`、警示瑞士红 `#FF0000` | 严格数学多栏网格系统，左对齐右无拘排版 |
| `style-brutalist` | 暴露外墙、脚手架、未精修 Raw 元素、等宽字 | 原始木模板清水混凝土(Béton Brut)、锈蚀铁板 | 水泥青灰 `#808588`、无油墨单色白 `#FFFFFF`、荧光绿 `#00FF66` | 反对称，反美学排版，极高密度信息平铺 |
| `style-grunge-acid` | 液态金属 3D、撕裂复印噪点、拉伸尖锐哥特字 | 熔融铬合金、全息镭射膜、黑白复印机撕裂噪波 | 镭射紫 `#9D00FF`、铬合金冷银 `#C0C0C0`、荧光酸绿 `#CCFF00` | 反可读性排版，重叠倾斜，视网膜信息超载 |

---

## 4. 标准设计 Skill 规范模板 (SKILL.md Specification)

每个风格 Skill 必须包含以下七大标准段落：

```markdown
---
name: "style-[name]"
description: "精准触发该风格的 AI 视觉/设计/排版引擎。破除通用 AI 的塑料感与模版同质化。"
version: "1.0.0"
author: "AI Style Architecture Lab"
tags: ["visual-style", "anti-homogenization", "[sub-tag]"]
---

# 风格定义：[风格正式中文名] ([英文名])

## 1. 风格灵魂与反同质化主张 (Soul & Anti-Homogenization)
- **核心哲学**：...
- **AI 同质化致命缺陷**：...
- **本 Skill 矫正法则**：...

## 2. 视觉 DNA 参数表 (Visual Parameter Matrix)
- **色彩规范 (Color Tokens)**：限定主色、辅色、背景色 HEX 及色比（60:30:10）。
- **光学与镜头 (Lighting & Optics)**：指定打光类型、相机视角与色彩科学。
- **材质与微观肌理 (Materials & Textures)**：指定真实的物理介质。
- **构图与几何模度 (Composition & Grid)**：指定排版网格与留白率。

## 3. 负向禁忌词库 (Negative Prompt & Anti-Patterns)
- 必须严格禁止的高频 AI 垃圾元素、陈词滥调与渲染效果。

## 4. Midjourney / Stable Diffusion / 图像生成提示词注入模板 (Prompt Engine)
- 正向结构化 Prompt 公式。
- 负向固定 Prompt。

## 5. UI / 平面排版应用指南 (Graphic & UI Layout Rules)
- 字阶系统 (Typography)。
- 间距与网格规范 (Grid System)。

## 6. 配套文字修辞推荐 (Harmonized Copywriting Voice)
- 推荐配合使用的叙事 Skill（如新中式配新东方嗅觉体）。
```

---

## 5. 标杆示范 1：当代东方文人写意 Skill

创建路径：`skills/visual/style-neo-chinese-zen/SKILL.md`

```markdown
---
name: "style-neo-chinese-zen"
description: "当代东方文人写意与新中式设计风格 Skill。拒绝大红大绿龙凤堆砌，以计白当黑、瓦石灰度与气韵生动重构当代空间与视觉。"
version: "1.0.0"
tags: ["oriental", "minimalism", "wabi-sabi", "architecture", "graphic-design"]
---

# 当代东方文人写意与新中式 (Neo-Chinese Zen Literati)

## 1. 风格灵魂与反同质化主张
- **核心哲学**：“大音希声，大象无形”。取法宋徽宗瑞鹤图的宋画克制风骨、贝聿铭苏州博物馆与王澍中国美院象山校区瓦爿墙。
- **AI 常见同质化缺陷**：粗暴生成金色龙纹、红色祥云、大红灯笼、大理石烫金贴片，俗不可耐且缺乏精神呼吸感。
- **本 Skill 矫正法则**：
  1. 彻底剔除宫廷龙凤符号，转入“宋明文人骨相”。
  2. 画面必须保有 60% 以上高洁的负空间（计白当黑）。
  3. 强调微观物理风土材质（生宣纸、旧青砖瓦、无光素烧陶、粗竹、自然天光）。

## 2. 视觉 DNA 参数表
- **调色盘 (Restricted 4-Color Palette)**:
  - 宣纸本白 (Rice Paper White): `#F5F2EB` (主背景, 占65%)
  - 瓦黛深灰 (Tile Slate Gray): `#2C2F33` (主体结构, 占25%)
  - 冷山墨青 (Cold Mountain Ink Blue): `#3D4C53` (微调着色, 占7%)
  - 极淡竹青 (Pale Bamboo): `#8A9A86` (呼吸点睛, 占3%)
- **材质微观肌理**:
  - Raw handmade Xuan paper fibers (生宣纤维暗纹)
  - Rammed earth and reclaimed roof tiles (夯土与风化旧瓦爿)
  - Unglazed matte ceramics (无光素烧哑光陶)
  - Bamboo stalk shadows cast by soft ambient light (自然竹影漫射)
- **光学系统**:
  - Overcast skylight, soft diffuse daylight entering through courtyard (多云漫射天光，庭院漫射天光)
  - 严禁强烈的彩色点光源与霓虹高光。
- **排版与构图**:
  - 留白率：≥65%
  - 构图：极端非对称，一角或半边留白（如马远“马一角”构图）。

## 3. 负向禁忌词库 (Anti-Patterns)
`FORBIDDEN`:
- NO golden dragons, NO shiny gold foil stamping (禁止金龙、闪亮烫金)
- NO red lantern festivity, NO traditional red and yellow kitsch (禁止大红灯笼与春节喜庆风)
- NO heavy 3D CGI gloss, NO oversaturated cyberpunk neon (禁止油腻3D塑料高光与高饱和赛博霓虹)
- NO crowded compositions without breathing space (禁止毫无呼吸感的拥挤填满)

## 4. 图像生成提示词注入模板 (Prompt Engine)
- **Positive Prompt**:
  > Contemporary Neo-Chinese literati minimalism, architectural photography inspired by I.M. Pei and Wang Shu, an asymmetrical quiet courtyard with reclaimed dark roof tile wall, smooth gray river stone floor, single withered pine branch casting sharp delicate shadow on raw white textured plaster wall. Matte finish, overcast diffused morning light, subtle ink bleeding atmosphere, 70% negative space, poetic tranquility, ultra-high dynamic range, 8k resolution, Hasselblad medium format color fidelity.
- **Negative Prompt**:
  > gold, shiny, dragon, ornate palace decorations, red lanterns, oversaturated colors, cyberpunk, neon, glossy plastic, 3d render shine, chaotic background, centered symmetrical framing, text watermark.
```

---

## 6. 标杆示范 2：瑞士国际主义风格 Skill

创建路径：`skills/visual/style-swiss-international/SKILL.md`

```markdown
---
name: "style-swiss-international"
description: "国际主义平面设计风格（瑞士风格）Skill。基于严密数学网格、客观中立黑白摄影与无衬线字体，消灭主观装饰与泛滥插画。"
version: "1.0.0"
tags: ["swiss-style", "grid-system", "helvetica", "graphic-design", "typography"]
---

# 瑞士国际主义风格 (Swiss International Typographic Style)

## 1. 风格灵魂与反同质化主张
- **核心哲学**：形式由内容与结构决定，设计师应当是客观中立的信息传递者。取法约瑟夫·米勒-布罗克曼 (Josef Müller-Brockmann) 与阿明·霍夫曼 (Armin Hofmann)。
- **AI 常见同质化缺陷**：文字排版漂浮无章、字阶混乱、随意添加渐变发光装饰球、破坏网格对齐。
- **本 Skill 矫正法则**：
  1. 引入绝对的数学多栏柱状网格（Modular Column Grid）。
  2. 严禁用手绘乱线或华丽插画填充，必须使用客观纪实高反差黑白摄影。
  3. 字体强制左对齐右无拘（Flush left, ragged right），形成严格字阶对比。

## 2. 视觉 DNA 参数表
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

## 3. 负向禁忌词库 (Anti-Patterns)
`FORBIDDEN`:
- NO ornamental borders, NO decorative drop shadows (严禁装饰花边与投影)
- NO pastel color gradients, NO skeuomorphic textures (严禁马卡龙渐变与仿皮质/玻璃拟物)
- NO centered text alignments for long paragraphs (严禁长段落文字居中)
- NO serif calligraphy or cursive handwritten scripts (严禁衬线书法手写花体)

## 4. 图像与版面生成提示词引擎
- **Positive Prompt**:
  > Vintage Swiss Graphic Design poster from 1968, designed by Josef Müller-Brockmann, asymmetric 12-column modular grid composition, ultra-clean typography in Helvetica Neue bold and regular, high contrast black and white documentary photography of mechanical turbine geometry, bold red solid rectangle accent `#FF1801`, pure white background, flush left ragged right, mathematical precision, matte uncoated paper texture, museum exhibition grade archival print.
- **Negative Prompt**:
  > decorative ornaments, gradient background, 3d glossy, soft focus, neon glow, watercolor, handwritten calligraphy, centered typography, messy layout, lens flare.
```

---

## 7. 标杆示范 3：拉美热带现代主义 Skill

创建路径：`skills/visual/style-tropical-modernism/SKILL.md`

```markdown
---
name: "style-tropical-modernism"
description: "拉美热带现代主义风格 Skill。融合巴拉甘与尼迈耶的狂烈原色光影、流线雕塑混凝土与热带植物地景，打破西欧玻璃盒子的冰冷乏味。"
version: "1.0.0"
tags: ["tropical-modernism", "barragan", "niemeyer", "architecture", "vibrant-color"]
---

# 拉美热带现代主义 (Latin American Tropical Modernism)

## 1. 风格灵魂与反同质化主张
- **核心哲学**：以火热的原色实墙和奔放的混凝土曲面，抵抗西欧功能主义冷冰冰的钢与玻璃盒子。唤醒前哥伦布古文明对烈日与大地的崇拜。
- **AI 常见同质化缺陷**：生成热带场景时千篇一律的度假村棕榈树加千篇一律泳池蓝，缺乏巴拉甘式的深邃形而上学光影沉思。
- **本 Skill 矫正法则**：
  1. 采用大体量实墙（Solid Monolithic Walls），绝无琐碎小窗格。
  2. 极高饱和度暖色原色墙体撞色（墨西哥粉、钴蓝、明黄）。
  3. 暴烈正午阳光投射出极其锋利、深邃的几何黑色硬投影。
  4. 引入雕塑般多肉龙舌兰、巨大仙人掌与静止水池的哲学倒影。

## 2. 视觉 DNA 参数表
- **调色盘 (Barragán Palette)**:
  - 墨西哥粉 (Mexican Hot Pink): `#E03576` (主墙面，占40%)
  - 暴烈钴蓝 (Deep Cobalt Blue): `#1338BE` (对撞墙面，占25%)
  - 烈日铬黄 (Chrome Sun Yellow): `#FDB813` (光影折射面，占15%)
  - 深火山玄武岩灰 (Volcanic Basalt): `#323232` (地面基座，占20%)
- **物理与光影特征**:
  - 粗拉毛抹灰墙面（Stucco rough texture），肉眼可见手抹凹凸颗粒感。
  - 水面如同黑色玄武岩镜面，无波纹，倒映着纯净蓝天与粉红高墙。
  - 正午垂直顶光（Harsh overhead midday sunlight），产生边缘极其分明的几何切角阴影。

## 3. 负向禁忌词库 (Anti-Patterns)
`FORBIDDEN`:
- NO cold corporate curtain wall glass facades (严禁冷淡企业幕墙玻璃)
- NO pastel faded desaturated filters (严禁发灰发暗的低饱和日系滤镜)
- NO soft cloudy ambient lighting (严禁没有方向感的阴天平光)
- NO cluttered furniture arrangements (严禁杂乱无章的家具堆砌)

## 4. 图像生成提示词注入模板
- **Positive Prompt**:
  > Architectural photography of Luis Barragán inspired modernist courtyard in Mexico, massive high monolithic stucco walls painted in vibrant Mexican pink `#E03576` and deep cobalt blue `#1338BE`, a solitary giant sculptural saguaro cactus growing from black volcanic lava gravel, pristine reflective still water pond creating sharp geometric reflections, intense brutal overhead tropical sunlight casting razor-sharp architectural shadows, pure blue clear sky, tactile rough plaster texture, 70mm architectural lens perspective, cinematic stillness.
- **Negative Prompt**:
  > clouds, overcast light, soft shadows, glass skyscraper, European classical ornaments, muted pastel colors, grainy noise, cluttered interior, blurry details.
```

---

## 8. 后续工程化路线图与持续演进

按照本规范，后续将系统化推进各大流派的工程化落地：

1. **第一阶段：核心视觉 Skill 批量实现（17 个）**
   - 东方体系：海派月份牌、红色工业、新国潮赛博；
   - 欧美体系：包豪斯、装饰艺术、粗野主义、孟菲斯、酸性垃圾排版、Y2K；
   - 区域非欧美：日本物哀侘寂、伊斯兰无尽几何。
2. **第二阶段：叙事与文案修辞 Skill 实现（16 个）**
   - 中文语系：鲁迅体、张爱玲体、汪曾祺白描体、王家卫疏离体、许舜英符号学体、观夏风土体、叶茂中冲突体；
   - 欧美全球语系：奥格威事实密集流、伯恩巴克自嘲体、海明威电报体、W&K 存在主义运动史诗、乔布斯清澈体。
3. **第三阶段：跨媒介声色合一 Presets 封装**
   - 打通视觉 Prompt 引擎与文案修辞引擎，使得设计团队在开发品牌、包装、UI 页面、社交海报时，能够“一键调用风格技能包”，实现真正具有文化深度、风格独立性与极致反同质化的 AI 辅助设计体系。
