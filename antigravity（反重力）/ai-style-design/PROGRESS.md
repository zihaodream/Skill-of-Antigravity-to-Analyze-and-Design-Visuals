# AI 设计流派 Skill 语料库与双接口开发进度看板

> **项目目标**：将《全球近现代设计美学与文字叙事风格全景图谱》中的世界各大设计与文字流派，系统化工程落地为高辨识度、抗同质化的 AI Design Skill 语料库，并在反重力 (Antigravity) 等 Agent 环境中提供**「风格分析接口」**与**「智能设计接口」**两大核心调用能力。

---

## 📊 总体进度仪表盘

```
[整体开发进度] ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100% (语料库、集中索引、双接口与反重力全局 Skill 库导入全部竣工就绪！)
├── 阶段 0：架构定义与规范制定  [100% 已完成 ✅]
├── 阶段 1：底层 Skill 语料库建设 [100% 已完成 ✅] (36/36 全量已就绪)
├── 阶段 2：索引与检索矩阵构建  [100% 已完成 ✅] (corpus_index.json 38模块已就绪)
├── 阶段 3：反重力双接口封装    [100% 已完成 ✅] (style-analyzer / style-designer)
└── 阶段 4：反重力技能库导入挂载 [100% 已完成 ✅] (~/.gemini/antigravity/skills/)
```

---

## 🗂️ 目录与资产拓扑

```
f:\ai风格设计\
├── README.md                          # 全景知识库原典与项目总入口
├── PROGRESS.md                        # 本文件：工程化进度看板与状态追踪
├── DESIGN_SKILLS_FRAMEWORK.md         # 架构总纲与开发规范
├── corpus_index.json                  # [已就绪] 全量 36 大语料库结构化特征索引矩阵 (20视觉 + 16叙事)
├── scripts/                           # 工程化辅助与接口驱动脚本
│   ├── build_corpus_index.py          # 索引构建脚本
│   ├── build_visual_skills.py         # 视觉 Skill 自动化生成器
│   ├── build_narrative_skills.py      # 叙事 Skill 自动化生成器
│   ├── style_analyzer.py              # [已就绪] 风格分析与 5 维同质化诊断 Python 引擎
│   └── style_designer.py              # [已就绪] 智能设计调度器 Python 引擎 (模式A/模式B/模式C)
└── skills/                            # 技能根目录
    ├── visual/                        # 视觉设计流派语料库 (共20个，全部就绪 ✅)
    │   ├── style-haipai-artdeco/      # [已就绪] 民国海派与月份牌
    │   ├── style-socialist-realism/   # [已就绪] 新中国现实主义工业美学
    │   ├── style-neo-chinese-zen/     # [已就绪] 当代东方文人写意/新中式
    │   ├── style-neo-guochao/         # [已就绪] 新国潮与东方赛博机能
    │   ├── style-wabi-sabi/           # [已就绪] 日本物哀、侘寂与原白
    │   ├── style-tropical-modernism/  # [已就绪] 拉美热带现代主义
    │   ├── style-islamic-geometric/   # [已就绪] 伊斯兰现代几何与当代书写
    │   ├── style-arts-crafts/         # [已就绪] 工艺美术运动
    │   ├── style-art-nouveau/         # [已就绪] 新艺术运动
    │   ├── style-constructivism/      # [已就绪] 构成主义与风格派
    │   ├── style-bauhaus/             # [已就绪] 包豪斯与功能主义
    │   ├── style-art-deco/            # [已就绪] 装饰艺术风格
    │   ├── style-swiss-international/ # [已就绪] 瑞士国际主义排版
    │   ├── style-midcentury-modern/   # [已就绪] 中世纪现代主义 (MCM)
    │   ├── style-pop-psychedelic/     # [已就绪] 波普与迷幻艺术
    │   ├── style-brutalist/           # [已就绪] 粗野主义与反设计
    │   ├── style-memphis/             # [已就绪] 后现代孟菲斯风格
    │   ├── style-grunge-acid/         # [已就绪] 垃圾排版与解构酸性
    │   ├── style-ui-waves/            # [已就绪] 数字交互三次浪潮
    │   └── style-y2k-cyberpunk/       # [已就绪] 千禧未来与赛博谱系
    ├── narrative/                     # 叙事修辞流派语料库 (共16个，全部就绪 ✅)
    │   ├── voice-luxun/               # [已就绪] 鲁迅冷峻匕首体
    │   ├── voice-zhangailing/         # [已就绪] 张爱玲世俗苍凉工笔
    │   ├── voice-wangzengqi/          # [已就绪] 汪曾祺/阿城民间白描
    │   ├── voice-wangjiawei/          # [已就绪] 王家卫都市疏离体
    │   ├── voice-xushunying/          # [已就绪] 许舜英消费符号学
    │   ├── voice-lixinpian/           # [已就绪] 李欣频感官避难所
    │   ├── voice-neo-oriental/        # [已就绪] 当代新东方风土嗅觉体
    │   ├── voice-yemaozhong/          # [已就绪] 叶茂中冲突穿透体
    │   ├── voice-ogilvy-fact/         # [已就绪] 奥格威事实密集流
    │   ├── voice-bernbach-negative/   # [已就绪] 伯恩巴克自嘲反常识体
    │   ├── voice-neilfrench/          # [已就绪] 尼尔·法兰奇傲慢长文
    │   ├── voice-hemingway/           # [已就绪] 海明威冰山电报体
    │   ├── voice-wieden-kennedy/      # [已就绪] W&K 存在主义运动史诗
    │   ├── voice-jobs-clarity/        # [已就绪] 乔布斯激进清澈体
    │   ├── voice-proust/              # [已就绪] 普鲁斯特微观通感
    │   └── voice-japanese-restraint/  # [已就绪] 日系日常节制絮语
    └── interfaces/                    # [已全部就绪 ✅] 反重力直接调用核心双接口
        ├── style-analyzer/            # [已就绪] 接口1：风格与内容分析诊断接口
        └── style-designer/            # [已就绪] 接口2：智能设计与生成调度接口
```

---

## 📋 详细任务清单与状态跟踪 (Checklist)

### 阶段 0：架构与规范制定 (Completed ✅)
- [x] 深度剖析 AI 风格同质化病征（塑料感次表面散射、滥用赛博霓虹、通用水果糖渐变、假大空公关套话）
- [x] 制定 5 维反同质化硬约束规则（微观物理材质锚定、受限调色盘、数学网格/空间度规、负向禁忌词库、骨力注入）
- [x] 确立标准 `SKILL.md` 数据规范（Schema）
- [x] 沉淀工程开发规范文档 [`DESIGN_SKILLS_FRAMEWORK.md`](./DESIGN_SKILLS_FRAMEWORK.md)

---

### 阶段 1：底层全量 Skill 语料库建设 (Completed ✅ 36/36)

#### 1. 视觉美学体系 (共 20 大流派全部就绪)

| 序号 | 标识符 (ID) | 中文流派名 | 核心特征提取重点 | 当前状态 | 责任模块 |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 1 | `style-haipai-artdeco` | 民国海派与月份牌 | 擦笔水彩、石库门、老报纸美术字、旗袍缎面 | ✅ 已就绪 | visual |
| 2 | `style-socialist-realism`| 新中国现实主义工业美学 | 新兴木刻刀痕、英雄仰角、红光亮、苏式重工业 | ✅ 已就绪 | visual |
| 3 | `style-neo-chinese-zen` | 当代东方文人写意/新中式 | 计白当黑(留白≥65%)、瓦石灰度、生宣纤维水渗 | ✅ 已就绪 | visual |
| 4 | `style-neo-guochao` | 新国潮与东方赛博机能 | 汉字结构异化、朱砂红与机能黑高反差、马面裙战术 | ✅ 已就绪 | visual |
| 5 | `style-wabi-sabi` | 日本物哀、侘寂与原白 | 枯山水、残缺粗陶、无光素白、风化木纹、低照度 | ✅ 已就绪 | visual |
| 6 | `style-tropical-modernism`| 拉美热带现代主义 | 墨西哥粉与钴蓝高墙、暴烈光影、流线混凝土、仙人掌 | ✅ 已就绪 | visual |
| 7 | `style-islamic-geometric` | 伊斯兰现代几何与当代书写 | 八角星轮无限拓扑、镂空木屏风微气候、涂鸦阿拉伯字 | ✅ 已就绪 | visual |
| 8 | `style-arts-crafts` | 工艺美术运动 | 自然藤蔓植物交织、反工业异化、中世纪手工木作 | ✅ 已就绪 | visual |
| 9 | `style-art-nouveau` | 新艺术运动 | 鞭绳曲线、拜占庭神性女性、有机流动、自然花茎 | ✅ 已就绪 | visual |
| 10 | `style-constructivism` | 构成主义与风格派 | 三原色与绝对几何、第三国际对角线力场、机械工业 | ✅ 已就绪 | visual |
| 11 | `style-bauhaus` | 包豪斯与功能主义 | 形式追随功能、无衬线字体、纯几何结构、悬挑钢管 | ✅ 已就绪 | visual |
| 12 | `style-art-deco` | 装饰艺术风格 | 机器时代速度、阶梯金字塔、闪烁金属铜金、流线对称 | ✅ 已就绪 | visual |
| 13 | `style-swiss-international`| 瑞士国际主义风格 | 严格 12 栏数学网格、Helvetica、客观中立黑白摄影 | ✅ 已就绪 | visual |
| 14 | `style-midcentury-modern`| 中世纪现代主义 (MCM) | 人机工学曲木、战后原子时代乐观、落地窗室内外交融 | ✅ 已就绪 | visual |
| 15 | `style-pop-psychedelic` | 波普与迷幻艺术 | 本戴点网印、大众消费品崇拜、荧光撞色、熔岩扭曲字 | ✅ 已就绪 | visual |
| 16 | `style-brutalist` | 粗野主义与反设计 | 原始木模板清水混凝土(Béton Brut)、单宽字体、裸露框架 | ✅ 已就绪 | visual |
| 17 | `style-memphis` | 后现代孟菲斯风格 | 戏谑少即是无聊、水磨石塑料波浪、几何糖果高撞色 | ✅ 已就绪 | visual |
| 18 | `style-grunge-acid` | 垃圾排版与解构酸性 | 3D液态金属、撕裂复印机噪点、过度拉伸哥特字 | ✅ 已就绪 | visual |
| 19 | `style-ui-waves` | 数字交互三次浪潮 | 拟物化光泽 -> 纯色扁平化 -> 空间玻璃磨砂拟态 | ✅ 已就绪 | visual |
| 20 | `style-y2k-cyberpunk` | 千禧未来与赛博谱系 | 充气糖果透明机壳、高科技低生活霓虹雨夜、机械义体 | ✅ 已就绪 | visual |

#### 2. 叙事与文案修辞体系 (共 16 大流派全部就绪)

| 序号 | 标识符 (ID) | 修辞流派名 | 核心语言特征与语法法则 | 当前状态 | 责任模块 |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 1 | `voice-luxun` | 鲁迅冷峻匕首体 | 金石碑帖骨力、白描短促、冷面刺破本质、零温吞 | ✅ 已就绪 | narrative |
| 2 | `voice-zhangailing` | 张爱玲世俗苍凉工笔 | 浓郁感官显微镜、市井浮世绘、华美衣料与彻骨悲凉 | ✅ 已就绪 | narrative |
| 3 | `voice-wangzengqi` | 汪曾祺/阿城民间白描 | 家常洗练口语、风物本真考据、人间烟火、干脆动词 | ✅ 已就绪 | narrative |
| 4 | `voice-wangjiawei` | 王家卫都市疏离体 | 精确时间与距离量度、隐秘保质期代码、私密内心独白 | ✅ 已就绪 | narrative |
| 5 | `voice-xushunying` | 许舜英消费符号学 | 知性傲慢、后现代语法长句、中产阶级身体与空间哲学 | ✅ 已就绪 | narrative |
| 6 | `voice-lixinpian` | 李欣频感官避难所 | 散文蒙太奇、温度节气大师串联、纸张气味朝圣 | ✅ 已就绪 | narrative |
| 7 | `voice-neo-oriental` | 当代新东方风土嗅觉体 | 零形容词法则、风土植物微观气味通感、短句沉静定力 | ✅ 已就绪 | narrative |
| 8 | `voice-yemaozhong` | 叶茂中冲突穿透体 | 直击核心心智冲突、拒绝修辞废话、单句铁锤押韵 | ✅ 已就绪 | narrative |
| 9 | `voice-ogilvy-fact` | 奥格威事实密集流 | 严密工程师测试数据、否定主观吹捧、客观纪实长文 | ✅ 已就绪 | narrative |
| 10 | `voice-bernbach-negative`| 伯恩巴克自嘲反常识体 | 逆向否定切入（"Lemon."）、先扬后抑、诚实建立信任 | ✅ 已就绪 | narrative |
| 11 | `voice-neilfrench` | 尼尔·法兰奇傲慢长文 | 贵族冷淡蔑视、层层铺垫逼仄、结局冷酷反转 | ✅ 已就绪 | narrative |
| 12 | `voice-hemingway` | 海明威冰山电报体 | 极简短句切割、大量省去副词、八分之七水下情感蓄积 | ✅ 已就绪 | narrative |
| 13 | `voice-wieden-kennedy` | W&K 存在主义运动史诗 | 身体极限挑战、反英雄叙事、宿命与意志对抗（Just do it）| ✅ 已就绪 | narrative |
| 14 | `voice-jobs-clarity` | 乔布斯激进清澈体 | 1000首歌装进口袋、极高信噪比、打破常规重新定义 | ✅ 已就绪 | narrative |
| 15 | `voice-proust` | 普鲁斯特微观通感 | 一块玛德琳蛋糕引发的时空记忆风暴、五感细密交织 | ✅ 已就绪 | narrative |
| 16 | `voice-japanese-restraint`| 日系日常节制絮语 | “这样就好”克制哲学、小站微风、微小生活的无声体认 | ✅ 已就绪 | narrative |

#### 3. 集中式特征矩阵索引构建 (Completed ✅)
- [x] 整合全量 36 个流派的参数字典，生成 `corpus_index.json` (175KB)，供 Agent 极速读取与语义相似度比对。

---

### 阶段 2：反重力 (Antigravity) 核心双接口封装 (Completed ✅)

#### 接口 1：`style-analyzer`（风格与内容分析诊断接口）
- **规范路径**：[`skills/interfaces/style-analyzer/SKILL.md`](./skills/interfaces/style-analyzer/SKILL.md)
- **底层驱动脚本**：[`scripts/style_analyzer.py`](./scripts/style_analyzer.py)
- **交付能力清单**：
  - [x] **流派溯源**：对照 36 大语料库（20 视觉 + 16 叙事），输出视觉与文本的置信度分值（0-100%）、判定依据证据链及官方协同搭档。
  - [x] **基因提取**：解析显式/推断 HEX 色彩、物理材质微观肌理、网格度规（留白率/多栏网格）与修辞句式特征。
  - [x] **同质化诊断**：5 维同质化审查（材质塑料感、色彩媚俗霓虹、空间大头拥挤、假大空公关辞令、精神骨力缺失），输出「AI 平庸度指数 (0-100%)」与精确扣分明细。
  - [x] **优化改进与纯化重构**：向目标正统流派深度纯化，输出工业级结构化生图 Prompt（Midjourney v6.1 / SDXL 格式）与落地风骨文案。

#### 接口 2：`style-designer`（智能设计与生成调度接口）
- **规范路径**：[`skills/interfaces/style-designer/SKILL.md`](./skills/interfaces/style-designer/SKILL.md)
- **底层驱动脚本**：[`scripts/style_designer.py`](./scripts/style_designer.py)
- **交付能力清单**：
  - [x] **模式 A（自主情境分析 / 智能协同推荐）**：
    - 针对未指定流派的用户需求，自动识别产品类别、受众定位与情绪基调；
    - 从 36 大库中智能推荐最佳「声色合一」搭配（例如：当代文人写意 + 新东方风土嗅觉体）；
    - 支持跨流派先锋实验融合对撞（如：粗野主义混凝土 × 装饰艺术金）。
  - [x] **模式 B（严格正统限定流派锁定）**：
    - 用户指定流派 ID 时，系统强制锁死该流派参数并激活 100% 纯正血统硬性负向约束；
    - 坚决剔除一切无关杂质与平庸 AI 元素，确保时代质感；
    - 输出 100% 纯度的设计方案书、受限色盘 Tokens（严格 60:30:10 阶梯）、材质网格规范与开箱即用 Prompt 资产包。

### 阶段 4：反重力全局 Skill 库打包与导入挂载 (Completed ✅)

- [x] **安装到全局物理路径**：`~/.gemini/antigravity/skills/ai-style-design/` (完整打包 38 模块与 Python 脚本)
- [x] **反重力全局技能暴露**：在 `~/.gemini/antigravity/skills/` 下建立：
  - `style-analyzer` Junction 快捷调用入口
  - `style-designer` Junction 快捷调用入口
  - `ai-style-design` Junction 总控套件入口
- [x] **配置中心注册挂载**：更新 `~/.gemini/config/skills.json`，并将 Junction 同步到 `~/.gemini/config/skills/` 与 `~/.gemini/config/plugins/`
- [x] **工作区优先发现配置**：在 `F:\ai风格设计\.agents\skills/` 建立符号挂载，确保本地与全局双重免配置生效。

---

## 🎯 系统工程化交付成果总结

1. **底层语料全量就绪**：20 个视觉流派 + 16 个叙事修辞流派共 36 个标准 `SKILL.md` 语料库全部构建完毕；
2. **特征索引极速比对**：集中式检索矩阵 [`corpus_index.json`](./corpus_index.json) 使得上层调度器无需重复扫描磁盘即可毫秒级锁定任意流派参数；
3. **反重力双接口全部闭环**：
   - 诊察端：`style-analyzer` 承担 AI 同质化质检与流派溯源重构；
   - 调度端：`style-designer` 承担设计意图分析、声色搭档调度与工业级方案生成；
   - 自动化：配套提供 `style_analyzer.py` 与 `style_designer.py` 命令行驱动引擎，兼顾 Agent 自主调用与开发者脚本化批处理。
