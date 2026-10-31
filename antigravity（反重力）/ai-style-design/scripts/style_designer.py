# -*- coding: utf-8 -*-
"""
style_designer.py - 反重力智能设计与生成调度器 (Style Designer)
功能：
1. 模式 A（自主分析 / 智能融合模式）：
   - 识别应用场景（包装、海报、UI、汽车、建筑、文案等）；
   - 从 36 大库中智能匹配最强视听协同搭档；
   - 支持跨媒介先锋实验组合 (Experimental Cross-Style Hybrid)。
2. 模式 B（严格限定模式）：
   - 锁定指定视觉流派与修辞流派；
   - 开启 100% 纯正血统硬性负向约束，剔除所有 AI 通用平庸杂质；
   - 输出开箱即用的工业级 Midjourney/SDXL Prompt 与全套文案、网格版式规格。
"""

import os
import sys
import json
import re
import random
import argparse

# 强制标准输出为 utf-8 编码
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 典型应用场景与流派亲和度映射字典 (Scenario Affinity Matrix)
SCENARIO_AFFINITY = [
    {
        "keywords": ["茶", "东方", "中式", "香氛", "庭院", "文房", "白酒", "丝绸", "禅意", "茶器", "tea", "oriental", "zen"],
        "recommended_visual": "style-neo-chinese-zen",
        "recommended_narrative": "voice-neo-oriental",
        "rationale": "当代东方文人写意的计白当黑与瓦黛灰度，配搭新东方风土植物微观嗅觉叙事，彻底剥离庸俗龙凤烫金，回归风骨。"
    },
    {
        "keywords": ["开发者", "编程", "终端", "效率", "工具", "代码", "框架", "系统", "工程师", "tech", "developer", "tool"],
        "recommended_visual": "style-bauhaus",
        "recommended_narrative": "voice-jobs-clarity",
        "rationale": "包豪斯功能主义的无衬线与严谨纯粹几何，配搭乔布斯式激进清澈与极高信噪比句式，直击技术本质。"
    },
    {
        "keywords": ["企业", "年报", "官网", "金融", "瑞士", "排版", "中立", "纪实", "数据", "报告", "corporate", "swiss"],
        "recommended_visual": "style-swiss-international",
        "recommended_narrative": "voice-ogilvy-fact",
        "rationale": "瑞士国际主义 12 栏数学网格与 Helvetica 客观纪实，配合奥格威事实密集流长文，以无可辩驳的证据赢得信任。"
    },
    {
        "keywords": ["硬核", "工业", "重工", "制造", "卡车", "机械", "机床", "基建", "力量", "heavy", "industrial", "machinery"],
        "recommended_visual": "style-socialist-realism",
        "recommended_narrative": "voice-luxun",
        "rationale": "新兴木刻版画刀痕、粗糙铸铁重机与英雄仰角，配以鲁迅金石碑帖般的沉着骨力与冷峻短句，如凿如铁。"
    },
    {
        "keywords": ["先锋", "独立杂志", "反叛", "地下", "小众", "批判", "解构", "艺术展", "underground", "brutalist"],
        "recommended_visual": "style-brutalist",
        "recommended_narrative": "voice-xushunying",
        "rationale": "粗野主义未经修饰的木模清水混凝土与裸露骨架，配合许舜英后现代意识流与消费符号学批判，颠覆中产阶级平庸审美。"
    },
    {
        "keywords": ["奢华", "豪宅", "珠宝", "高端酒店", "贵宾", "鸡尾酒", "高定", "钟表", "爵士", "luxury", "jewelry", "hotel"],
        "recommended_visual": "style-art-deco",
        "recommended_narrative": "voice-neilfrench",
        "rationale": "克莱斯勒大厦阶梯金字塔、拉丝帝国金与黑曜石对称，配合尼尔·法兰奇傲慢冷酷的贵族长文，构筑令人神往的阶层威仪。"
    },
    {
        "keywords": ["年轻人", "潮牌", "赛博", "未来", "数码", "电竞", "元宇宙", "科幻", "虚拟", "cyberpunk", "y2k", "esports"],
        "recommended_visual": "style-y2k-cyberpunk",
        "recommended_narrative": "voice-wangjiawei",
        "rationale": "千禧透明机壳与雨夜霓虹义体，搭配王家卫都市疏离体与时间延宕代码，勾勒数字时代赛博游民的虚无宿命。"
    },
    {
        "keywords": ["运动", "户外", "极限", "健身", "跑鞋", "探险", "马拉松", "挑战", "意志", "sport", "outdoor", "fitness"],
        "recommended_visual": "style-constructivism",
        "recommended_narrative": "voice-wieden-kennedy",
        "rationale": "构成主义第三国际对角线力场与红色动能，配合 W&K 存在主义运动史诗（Just do it），唤醒人类直面极限的原始意志。"
    },
    {
        "keywords": ["咖啡", "面包", "文创", "书店", "手工", "手作", "器皿", "陶艺", "慢生活", "cafe", "craft", "pottery"],
        "recommended_visual": "style-wabi-sabi",
        "recommended_narrative": "voice-japanese-restraint",
        "rationale": "无釉粗陶、风化木纹与低照度阴翳幽暗，配合日系“这样就好”节制生活絮语，在浮躁喧嚣中构筑精神锚地。"
    },
    {
        "keywords": ["热带", "度假", "庄园", "拉美", "建筑", "阳光", "色彩", "泳池", "仙人掌", "tropical", "architecture"],
        "recommended_visual": "style-tropical-modernism",
        "recommended_narrative": "voice-hemingway",
        "rationale": "巴拉甘式的墨西哥粉与钴蓝大体量实墙硬光影，配合海明威八分之七水下的冰山硬汉电报体，粗粝而深邃。"
    },
    {
        "keywords": ["音乐节", "派对", "酸性", "锐舞", "潮流艺术", "海报", "rave", "acid", "techno", "festival"],
        "recommended_visual": "style-grunge-acid",
        "recommended_narrative": "voice-bernbach-negative",
        "rationale": "液态金属镀铬与高噪点拉伸哥特字，配搭伯恩巴克自嘲反常识体，以刺穿视网膜的先锋反设计挑战庸常。"
    },
    {
        "keywords": ["国潮", "机能", "汉服", "改良旗袍", "汉字", "仙侠", "武侠", "guochao", "hanfu"],
        "recommended_visual": "style-neo-guochao",
        "recommended_narrative": "voice-wangzengqi",
        "rationale": "朱砂红与机能黑的东方赛博战术解构，配合汪曾祺/阿城朴素洗练的民间白描，使古老民俗焕发硬核新生。"
    }
]

class StyleDesigner:
    def __init__(self, corpus_path=None):
        if corpus_path is None:
            # 多级自适应探测 corpus_index.json 路径
            candidate_paths = [
                os.environ.get("AI_STYLE_CORPUS_PATH", ""),
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "corpus_index.json"),
                os.path.join(os.getcwd(), "corpus_index.json"),
                os.path.expanduser("~/.gemini/antigravity/skills/ai-style-design/corpus_index.json"),
                r"C:\Users\zhaoz\.gemini\antigravity\skills\ai-style-design\corpus_index.json",
                r"F:\ai风格设计\corpus_index.json"
            ]
            for p in candidate_paths:
                if p and os.path.isfile(p):
                    corpus_path = p
                    break
            if not corpus_path:
                corpus_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "corpus_index.json")
        self.corpus_path = corpus_path
        self.corpus = self._load_corpus()

    def _load_corpus(self):
        if not os.path.isfile(self.corpus_path):
            raise FileNotFoundError(f"Corpus index not found: {self.corpus_path}")
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def design(self, scene_or_subject, mode="auto", visual_id=None, narrative_id=None, hybrid_pair=None):
        """
        核心调度接口
        mode: 'auto' | 'strict' | 'hybrid'
        """
        if mode == "strict":
            return self._design_strict_mode(scene_or_subject, visual_id, narrative_id)
        elif mode == "hybrid":
            return self._design_hybrid_mode(scene_or_subject, hybrid_pair)
        else: # auto
            return self._design_auto_mode(scene_or_subject, visual_id, narrative_id)

    def _design_auto_mode(self, query, preferred_visual=None, preferred_narrative=None):
        """模式 A：自主情境分析与智能协同推荐"""
        query_lower = query.lower()
        matched_scenario = None
        best_count = 0

        # 基于关键词检索场景匹配
        for sc in SCENARIO_AFFINITY:
            hits = sum(1 for kw in sc["keywords"] if kw in query_lower)
            if hits > best_count:
                best_count = hits
                matched_scenario = sc

        # 若无精确命中，基于默认前卫推荐（当代文人写意 + 新东方嗅觉）
        if not matched_scenario:
            matched_scenario = SCENARIO_AFFINITY[0]

        v_id = preferred_visual or matched_scenario["recommended_visual"]
        n_id = preferred_narrative or matched_scenario["recommended_narrative"]

        v_data = self.corpus["skills"]["visual"].get(v_id)
        n_data = self.corpus["skills"]["narrative"].get(n_id)

        design_pkg = self._build_design_package(
            query=query,
            mode_name="模式 A：自主情境识别与声色协同推荐 (Auto-Affinity Mode)",
            rationale=matched_scenario["rationale"],
            visual_data=v_data,
            narrative_data=n_data,
            is_hybrid=False
        )
        return design_pkg

    def _design_strict_mode(self, query, visual_id, narrative_id=None):
        """模式 B：严格限定单流派锁定（零杂质渗透）"""
        if not visual_id:
            visual_id = "style-bauhaus" # 默认严格包豪斯

        v_data = self.corpus["skills"]["visual"].get(visual_id)
        if not v_data:
            # 尝试在叙事库中查找
            n_data = self.corpus["skills"]["narrative"].get(visual_id)
            if n_data:
                # 用户传入的是叙事流派
                return self._design_narrative_focused(query, n_data)
            raise ValueError(f"Visual style ID '{visual_id}' not found in corpus.")

        # 如果没有指定修辞流派，自动选择官方推荐搭档
        if not narrative_id:
            rec_partner = v_data.get("recommended_partner", "")
            found = re.search(r"`(voice-[a-z0-9\-]+)`", rec_partner)
            narrative_id = found.group(1) if found else "voice-jobs-clarity"

        n_data = self.corpus["skills"]["narrative"].get(narrative_id)

        rationale = (
            f"严格锁定【{v_data['name']}】正统血统规范。绝不允许任何无关杂质风格渗入，"
            f"强制执行 5 维反同质化硬约束，坚决剔除 AI 默认平庸元素，输出纯度 100% 的设计资产。"
        )

        design_pkg = self._build_design_package(
            query=query,
            mode_name="模式 B：严格正统限定流派锁定 (Strict Pureblood Mode)",
            rationale=rationale,
            visual_data=v_data,
            narrative_data=n_data,
            is_hybrid=False,
            strict_level="100% PURE"
        )
        return design_pkg

    def _design_hybrid_mode(self, query, hybrid_pair=None):
        """模式 C：跨流派先锋实验融合模式"""
        # 如果未指定融合流派，随机选择一对高反差碰撞流派
        if not hybrid_pair:
            v_keys = list(self.corpus["skills"]["visual"].keys())
            pair_candidates = [
                ("style-swiss-international", "style-tropical-modernism"), # 瑞士数学排版 + 拉美热带原色
                ("style-brutalist", "style-art-deco"),                     # 粗野混凝土 + 爵士时代金饰
                ("style-neo-chinese-zen", "style-grunge-acid"),             # 文人写意水渗 + 酸性液态铬
                ("style-bauhaus", "style-wabi-sabi")                       # 包豪斯纯几何 + 日本侘寂粗陶
            ]
            v1_id, v2_id = random.choice(pair_candidates)
        else:
            v1_id, v2_id = hybrid_pair

        v1_data = self.corpus["skills"]["visual"].get(v1_id)
        v2_data = self.corpus["skills"]["visual"].get(v2_id)

        # 融合视觉调色盘与材质
        combined_palette = (v1_data.get("color_hex_palette", [])[:2] + v2_data.get("color_hex_palette", [])[:2])
        combined_prompt = (
            f"Avant-garde experimental design hybrid: Combining the structural discipline of {v1_data['name']} "
            f"with the aesthetic soul of {v2_data['name']}. "
            f"Subject: {query}. Restricted palette ({' '.join(combined_palette)}). "
            f"{v1_data.get('positive_prompt', '')} fused with {v2_data.get('positive_prompt', '')} --ar 16:9 --style raw --v 6.1"
        )
        combined_neg = f"{v1_data.get('negative_prompt', '')}, {v2_data.get('negative_prompt', '')}"

        rec_partner = v1_data.get("recommended_partner", "")
        n_id_match = re.search(r"`(voice-[a-z0-9\-]+)`", rec_partner)
        n_id = n_id_match.group(1) if n_id_match else "voice-xushunying"
        n_data = self.corpus["skills"]["narrative"].get(n_id)

        rationale = f"先锋跨界对撞：以【{v1_data['name']}】的骨架结构支撑【{v2_data['name']}】的情感色彩，制造高辨识度审美冲击。"

        return {
            "mode": "模式 C：跨流派先锋实验融合 (Avant-Garde Hybrid Mode)",
            "query": query,
            "rationale": rationale,
            "hybrid_styles": [v1_data["name"], v2_data["name"]],
            "visual_dna": {
                "combined_palette": combined_palette,
                "materials": "双流派物理对撞（如精工金属与粗糙夯土 / 数学无衬线与手作肌理）",
                "grid_law": "在严密几何框架下引入破坏性动能"
            },
            "image_prompt_engine": {
                "positive_prompt": combined_prompt,
                "negative_prompt": combined_neg,
                "aspect_ratio": "--ar 16:9",
                "engine_flags": "--style raw --v 6.1"
            },
            "narrative_strategy": {
                "voice_name": n_data["name"] if n_data else "意识流符号学",
                "copy_exemplar": n_data["raw_sections"].get("4. 全真文本范例", "") if n_data else ""
            }
        }

    def _build_design_package(self, query, mode_name, rationale, visual_data, narrative_data, is_hybrid=False, strict_level=None):
        palette = visual_data.get("color_hex_palette", [])
        v_raw = visual_data.get("raw_sections", {})
        n_raw = narrative_data.get("raw_sections", {}) if narrative_data else {}

        # 结构化正向生图提示词
        base_pos = visual_data.get("positive_prompt", "")
        engineered_pos_prompt = (
            f"Masterpiece design execution of {query}, authentic {visual_data['name']} aesthetic. "
            f"Defined by strict color hierarchy ({' '.join(palette[:4])}), tactile micro-textures, "
            f"and absolute architectural clarity. {base_pos} --ar 16:9 --style raw --v 6.1"
        )

        engineered_neg_prompt = visual_data.get("negative_prompt", "")

        return {
            "mode": mode_name,
            "strict_level": strict_level,
            "query": query,
            "rationale": rationale,
            "visual_style": {
                "id": visual_data["id"],
                "name": visual_data["name"],
                "philosophy": v_raw.get("1. 风格灵魂与反同质化主张", ""),
                "color_palette": {
                    "hex_codes": palette,
                    "color_tokens": v_raw.get("2. 视觉 DNA 参数表", "")
                },
                "materials_and_textures": "提取自原典之时代物理介质与微观纤维",
                "layout_rules": v_raw.get("5. 平面与排版指南", ""),
                "anti_patterns": v_raw.get("3. 负向禁忌词库", "")
            },
            "narrative_voice": {
                "id": narrative_data["id"] if narrative_data else "None",
                "name": narrative_data["name"] if narrative_data else "None",
                "tone_philosophy": n_raw.get("1. 声音灵魂与反同质化主张", ""),
                "formula_and_syntax": n_raw.get("2. 词汇与意象阵列", ""),
                "forbidden_words": n_raw.get("3. 负向禁忌词库", ""),
                "copywriting_exemplar": n_raw.get("4. 全真文本范例", "")
            },
            "generation_assets": {
                "midjourney_v6_prompt": engineered_pos_prompt,
                "negative_prompt": engineered_neg_prompt,
                "suggested_aspect_ratios": ["16:9 (展示海报)", "9:16 (手机端/短视频封面)", "1:1 (画册/包装方形展板)"],
                "recommended_render_engine": "Midjourney v6.1 / SDXL 1.0 (Flag: --style raw)"
            }
        }

    def format_markdown_solution(self, pkg):
        """格式化输出专业级设计解决方案方案书"""
        md = []
        md.append(f"# 🏛️ 反重力智能设计调度方案书 (Antigravity Style Design Matrix)")
        md.append(f"**调度模式**：`{pkg['mode']}`" + (f" | 纯度等级：`{pkg['strict_level']}`" if pkg.get("strict_level") else ""))
        md.append(f"**设计主题 / 场景需求**：\n> **{pkg['query']}**\n")
        md.append(f"**策略推演与调性定调 (Rationale)**：\n> {pkg['rationale']}\n")

        # 视觉流派规范
        v = pkg.get("visual_style")
        if v:
            md.append("---")
            md.append(f"## 🎨 视觉系统规范：{v['name']} (`{v['id']}`)")
            if v["color_palette"]["hex_codes"]:
                md.append("### 1. 受限特调色盘 (Restricted Color Tokens 60:30:10):")
                hex_badges = "  ".join([f"`{h}`" for h in v["color_palette"]["hex_codes"]])
                md.append(f"{hex_badges}\n")
            
            md.append(f"### 2. 视觉 DNA 矩阵 (参数规范):\n{v['color_palette']['color_tokens']}\n")
            md.append(f"### 3. 版式网格与字阶系统 (Typography & Grid):\n{v['layout_rules']}\n")
            md.append(f"### 4. 负向禁忌词库 (Anti-Patterns):\n{v['anti_patterns']}\n")

        # 叙事文案系统
        n = pkg.get("narrative_voice")
        if n and n["id"] != "None":
            md.append("---")
            md.append(f"## ✍️ 叙事文案系统：{n['name']} (`{n['id']}`)")
            md.append(f"### 1. 声音灵魂与修辞主张:\n{n['tone_philosophy']}\n")
            md.append(f"### 2. 句式公式与意象阵列:\n{n['formula_and_syntax']}\n")
            md.append(f"### 3. 禁忌词库 (剔除假大空与廉价抒情):\n{n['forbidden_words']}\n")
            if n["copywriting_exemplar"]:
                md.append(f"### 4. 全真范例文案 (开箱即用):\n{n['copywriting_exemplar']}\n")

        # 工业级资产生成
        gen = pkg.get("generation_assets")
        if gen:
            md.append("---")
            md.append("## 🚀 工业级图像生成资产引擎 (Image Generation Engine)")
            md.append("### 正向结构化提示词 (Positive Prompt for Midjourney v6.1 / SDXL):")
            md.append(f"```text\n{gen['midjourney_v6_prompt']}\n```")
            md.append("### 硬性负向排除词 (Negative Prompt):")
            md.append(f"```text\n{gen['negative_prompt']}\n```")
            md.append(f"- **推荐渲染参数与画幅**: `{', '.join(gen['suggested_aspect_ratios'])}`")
            md.append(f"- **工业标志参数**: `{gen['recommended_render_engine']}`")

        # 混合模式特有输出
        if "hybrid_styles" in pkg:
            md.append("---")
            md.append(f"## ⚡ 先锋实验融合对撞：{' × '.join(pkg['hybrid_styles'])}")
            md.append(f"- **融合调色盘**: `{' | '.join(pkg['visual_dna']['combined_palette'])}`")
            md.append(f"- **对撞机理**: {pkg['visual_dna']['materials']}")
            md.append(f"### 融合正向生成 Prompt:\n```text\n{pkg['image_prompt_engine']['positive_prompt']}\n```")
            md.append(f"### 融合负向生成 Prompt:\n```text\n{pkg['image_prompt_engine']['negative_prompt']}\n```")

        return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="Style Designer - 反重力智能设计与生成调度器")
    parser.add_argument("--query", "-q", type=str, help="设计需求描述、产品名称或应用场景")
    parser.add_argument("--mode", "-m", choices=["auto", "strict", "hybrid"], default="auto", help="设计调度模式")
    parser.add_argument("--visual", "-v", type=str, help="严格指定视觉流派 ID (如 style-neo-chinese-zen)")
    parser.add_argument("--narrative", "-n", type=str, help="严格指定叙事流派 ID (如 voice-neo-oriental)")
    parser.add_argument("--json", action="store_true", help="输出结构化 JSON")

    args = parser.parse_args()

    query = args.query
    if not query:
        query = "高端高山乌龙茶与冷萃茶具礼盒，面向注重生活品质的当代雅士与设计师人群"

    designer = StyleDesigner()
    pkg = designer.design(
        scene_or_subject=query,
        mode=args.mode,
        visual_id=args.visual,
        narrative_id=args.narrative
    )

    if args.json:
        print(json.dumps(pkg, indent=2, ensure_ascii=False))
    else:
        print(designer.format_markdown_solution(pkg))

if __name__ == "__main__":
    main()
