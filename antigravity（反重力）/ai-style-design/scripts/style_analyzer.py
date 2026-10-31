# -*- coding: utf-8 -*-
"""
style_analyzer.py - 反重力风格与内容分析引擎 (Style Analyzer)
功能：
1. 流派溯源：对照 36 大语料库（20 视觉 + 16 叙事），计算匹配度与置信度。
2. 基因提取：解析色彩 HEX、物理材质、网格排版及语言修辞特征。
3. 同质化诊断：检测 5 维 AI 模板通病，输出平庸度指数与扣分项。
4. 深度纯化改造：向正统流派深度纯化，输出重构生图 Prompt 与修辞文案。
"""

import os
import sys
import json
import re
import argparse
from collections import Counter

# 强制标准输出为 utf-8 编码，兼容 Windows 终端
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# 5 维同质化检测词库与规则
HOMOGENIZATION_RULES = {
    "plastic_cgi_gloss": {
        "name": "材质塑料感与 3D 渲染高光 (Plastic CGI Gloss)",
        "weight": 25,
        "keywords": [
            "octane render", "unreal engine 5", "3d render", "glossy plastic", "subsurface scattering",
            "volumetric lighting", "god rays", "hyperrealistic", "4k wallpaper", "8k resolution",
            "trending on artstation", "ray tracing", "smooth surface", "plastic", "shiny metal",
            "塑料感", "次表面散射", "油腻高光", "体积光", "丁达尔效应", "光泽塑料", "完美无瑕", "超逼真"
        ],
        "deduction": 5,
        "advice": "去除虚幻引擎/体积光等渲染套话，强制锚定纸浆纤维、生宣水渗、粗糙木模清水混凝土或未涂层纸张等真实物理介质。"
    },
    "color_kitsch_neon": {
        "name": "色彩媚俗与霓虹渐变滥用 (Color Kitsch & Neon Clutter)",
        "weight": 20,
        "keywords": [
            "cyberpunk neon", "purple and blue", "neon glow", "gradient background", "macaron colors",
            "rainbow glow", "holographic colorful", "vibrant pastel", "oversaturated",
            "蓝紫霓虹", "水果糖渐变", "马卡龙渐变", "彩虹发光", "高饱和度发光", "霓虹光影", "梦幻渐变"
        ],
        "deduction": 5,
        "advice": "废除泛滥的蓝紫/水果糖渐变，严格使用受限特调色盘（Restricted Palette 2-4色），明确 60:30:10 色阶配比。"
    },
    "composition_bloat": {
        "name": "空间臃肿与大头居中填满 (Composition Bloat & Center Cram)",
        "weight": 20,
        "keywords": [
            "centered subject", "crowded", "close up face", "fill frame", "busy background",
            "extreme bokeh", "blurred background", "dramatic closeup",
            "大头居中", "填满画面", "景深过度虚化", "杂乱无章", "居中膨胀", "毫无留白"
        ],
        "deduction": 5,
        "advice": "引入数学多栏网格（12-Column Grid）或极端不对称构图，硬性规定留白率（≥60% 计白当黑）。"
    },
    "corporate_fluff": {
        "name": "假大空公关辞令与心灵鸡汤 (Corporate Fluff & Chicken Soup)",
        "weight": 20,
        "keywords": [
            "赋能", "闭环", "打法", "链路", "极致体验", "未来可期", "温馨", "治愈", "岁月静好",
            "温柔以待", "心灵洗礼", "小确幸", "在当今快节奏的社会中", "带来前所未有的体验", "为您的生活增添",
            "全方位", "多维度", "尊贵享受", "轻奢", "不忘初心", "匠心独运", "奢华典雅"
        ],
        "deduction": 5,
        "advice": "坚决剔除假大空虚词与廉价鸡汤，采用动名词骨力结构、短句切割或具象微观感官通感。"
    },
    "spiritual_flaccidity": {
        "name": "精神骨力与微观物理锚点缺失 (Spiritual Flaccidity & Lack of Anchor)",
        "weight": 15,
        "keywords": [
            "beautiful", "amazing", "stunning", "perfect", "elegant", "luxury", "dreamy",
            "唯美", "高端大气", "美丽", "惊艳", "梦幻", "优雅", "完美", "好看", "意境深远"
        ],
        "deduction": 3,
        "advice": "禁止堆砌空洞形容词（Beautiful/Luxury/高端），必须用客观事实参数、时代物理印记与具体物象构建张力。"
    },
    "craftsman_archetype": {
        "name": "样板戏人设与“吃了不烧心”式刻奇民间哲人 (Craftsman Archetype & False Profundity)",
        "weight": 20,
        "keywords": [
            "吃了不烧心", "是它的本分", "先把规矩立住", "立住规矩", "咬在嘴里没点", "咬着没点的烟",
            "咬在嘴里，没点", "没点，咬在嘴里", "看透世事", "扫地僧", "一生只做一件事", "宁可少赚"
        ],
        "deduction": 5,
        "advice": "坚决剔除短视频爽文式‘抽烟不点+道出土味哲理’的刻奇民间哲人剧本，还原真实的世俗疲倦、算账、粗糙毛刺、无效碎嘴与生活尴尬。"
    },
    "satire_overexplaining": {
        "name": "叙事潜台词直白化与金句强迫症 (Over-explaining Satire & Punchline Cliché)",
        "weight": 20,
        "keywords": [
            "致全体耗材", "下一具遗体", "全体生还者立即转场", "下一颗废料星球", "可悲的耗材"
        ],
        "deduction": 5,
        "advice": "严格恪守死鱼眼冷面笑匠法则（Deadpan），越是荒谬越要官方正经，禁止将讽刺写成直白恶毒，禁止结尾强行升华对仗工整的二律背反金句预制菜。"
    }
}

class StyleAnalyzer:
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
            raise FileNotFoundError(f"Corpus index file not found at: {self.corpus_path}")
        with open(self.corpus_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def analyze(self, text, target_style_id=None, domain="auto"):
        """
        全维综合分析
        domain: 'auto' | 'visual' | 'narrative'
        """
        tokens = self._tokenize(text)
        
        # 1. 基因提取
        dna = self._extract_dna(text, tokens)

        # 2. 同质化诊断
        homogenization = self._diagnose_homogenization(text, tokens)

        # 3. 流派溯源与匹配打分
        style_matches = self._trace_styles(text, tokens, domain)

        # 4. 优化建议与重构 Prompt
        recommended_target = target_style_id
        if not recommended_target and style_matches["top_visual"]:
            recommended_target = style_matches["top_visual"][0]["id"]
        elif not recommended_target and style_matches["top_narrative"]:
            recommended_target = style_matches["top_narrative"][0]["id"]

        refactoring = self._generate_purification(text, recommended_target, homogenization)

        return {
            "input_text": text,
            "dna": dna,
            "homogenization": homogenization,
            "style_matches": style_matches,
            "recommended_target_style": recommended_target,
            "refactoring": refactoring
        }

    def _tokenize(self, text):
        # 混合英文单词与中文分词片段
        words = re.findall(r"[a-zA-Z0-9_\-#]+|[\u4e00-\u9fa5]{2,6}", text.lower())
        return words

    def _extract_dna(self, text, tokens):
        # 提取 HEX 颜色代码
        explicit_hex = list(set([h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}", text)]))
        
        # 常见色彩中文名映射提取
        color_keywords = {
            "朱红": "#C91B1B", "宣纸白": "#F5F2EB", "瓦黛灰": "#2C2F33", "墨青": "#1E3F66",
            "墨西哥粉": "#E03576", "钴蓝": "#154388", "纯黑": "#0A0A0A", "纯白": "#FFFFFF",
            "瑞士红": "#FF0000", "土黄": "#D8861B", "松石绿": "#00A896", "铬银": "#C0C0C0",
            "水泥灰": "#808588", "酸性绿": "#CCFF00", "帝国金": "#D4AF37", "胭脂红": "#9E2A2B"
        }
        inferred_hex = []
        for name, hex_code in color_keywords.items():
            if name in text and hex_code not in explicit_hex:
                inferred_hex.append(f"{name} ({hex_code})")

        # 提取微观材质关键词
        material_keywords = [
            "宣纸", "水墨", "青砖", "瓦爿", "素陶", "竹", "木模清水混凝土", "铸铁", "生铁",
            "无缝镀铬钢管", "水磨石", "全息镭射", "胶木", "铜绿", "砂石", "原木", "粗麻",
            "handmade paper", "concrete", "chrome steel", "terrazzo", "bakelite", "brass",
            "uncoated paper", "rough plaster", "weathered wood", "basalt"
        ]
        detected_materials = [m for m in material_keywords if m.lower() in text.lower()]

        # 提取构图与网格特征
        layout_keywords = [
            "网格", "12栏", "网格系统", "留白", "计白当黑", "轴对称", "不对称", "左对齐",
            "黄金分割", "对角线", "多栏", "极端留白", "阶梯退台",
            "grid", "modular grid", "asymmetric", "flush left", "negative space", "symmetry"
        ]
        detected_layout = [l for l in layout_keywords if l.lower() in text.lower()]

        # 提取修辞与叙事特征
        rhetoric_keywords = [
            "短句", "白描", "冷峻", "反讽", "长句", "意识流", "事实密集", "数据证明",
            "通感", "风土嗅觉", "冲突", "冰山理论", "日常节制", "清澈", "激进"
        ]
        detected_rhetoric = [r for r in rhetoric_keywords if r in text]

        return {
            "explicit_hex_colors": explicit_hex,
            "inferred_colors": inferred_hex,
            "detected_materials": detected_materials,
            "detected_layout": detected_layout,
            "detected_rhetoric": detected_rhetoric
        }

    def _diagnose_homogenization(self, text, tokens):
        text_lower = text.lower()
        score = 0
        deductions = []

        for rule_id, rule in HOMOGENIZATION_RULES.items():
            matched_terms = []
            for kw in rule["keywords"]:
                if kw in text_lower:
                    matched_terms.append(kw)
            
            if matched_terms:
                penalty = min(rule["weight"], len(matched_terms) * rule["deduction"])
                score += penalty
                deductions.append({
                    "dimension": rule["name"],
                    "penalty_points": penalty,
                    "matched_terms": matched_terms,
                    "advice": rule["advice"]
                })

        score = min(100, score)
        
        # 评级
        if score <= 15:
            purity_tier = "纯血正统 (Authentic Masterpiece / 极高个性)"
            status = "PASS"
        elif score <= 40:
            purity_tier = "轻度泛化 (Slightly Homogenized / 含有少量常见套路)"
            status = "WARNING"
        elif score <= 70:
            purity_tier = "严重同质化 (Severely Homogenized / 充斥模板病征)"
            status = "FAIL"
        else:
            purity_tier = "重度 AI 废料 (Generic AI Sludge / 毫无灵魂与骨力)"
            status = "CRITICAL"

        return {
            "homogenization_index": score,
            "status": status,
            "purity_tier": purity_tier,
            "deductions_count": len(deductions),
            "deductions": deductions
        }

    def _trace_styles(self, text, tokens, domain="auto"):
        text_lower = text.lower()
        
        results_visual = []
        results_narrative = []

        # 遍历视觉流派
        if domain in ("auto", "visual"):
            for s_id, s_data in self.corpus["skills"]["visual"].items():
                score, matched_cues = self._calculate_match_score(text_lower, tokens, s_data)
                results_visual.append({
                    "id": s_id,
                    "name": s_data["name"],
                    "category": "visual",
                    "score": round(score, 1),
                    "confidence": self._get_confidence_label(score),
                    "matched_cues": matched_cues,
                    "recommended_partner": s_data.get("recommended_partner", "")
                })

        # 遍历叙事流派
        if domain in ("auto", "narrative"):
            for s_id, s_data in self.corpus["skills"]["narrative"].items():
                score, matched_cues = self._calculate_match_score(text_lower, tokens, s_data)
                results_narrative.append({
                    "id": s_id,
                    "name": s_data["name"],
                    "category": "narrative",
                    "score": round(score, 1),
                    "confidence": self._get_confidence_label(score),
                    "matched_cues": matched_cues,
                    "recommended_partner": s_data.get("recommended_partner", "")
                })

        results_visual.sort(key=lambda x: x["score"], reverse=True)
        results_narrative.sort(key=lambda x: x["score"], reverse=True)

        return {
            "top_visual": results_visual[:3] if results_visual else [],
            "top_narrative": results_narrative[:3] if results_narrative else []
        }

    def _calculate_match_score(self, text_lower, tokens, skill_data):
        score = 0.0
        cues = []

        # 1. 匹配 ID 和流派名称
        s_id = skill_data["id"].lower()
        s_name = skill_data["name"].lower()
        if s_id in text_lower:
            score += 45
            cues.append(f"明确提及流派标识符: {skill_data['id']}")
        
        # 提取流派核心中文名
        clean_name = re.sub(r"\(.*?\)", "", s_name).strip()
        for part in clean_name.split():
            if len(part) >= 2 and part in text_lower:
                score += 25
                cues.append(f"命中流派核心词: {part}")

        # 2. 匹配标签 tags
        for tag in skill_data.get("tags", []):
            if tag.lower() in text_lower:
                score += 10
                cues.append(f"命中流派标签: {tag}")

        # 3. 匹配描述与核心段落中的专业名词
        full_text_corpus = (skill_data.get("description", "") + " " + " ".join(skill_data.get("tags", []))).lower()
        for sec_name, sec_val in skill_data.get("raw_sections", {}).items():
            full_text_corpus += " " + sec_val.lower()

        # 针对输入文本切词进行比对
        for token in tokens:
            if len(token) >= 2 and token not in ["设计", "风格", "skill", "破除", "包装", "产品", "进行"]:
                if token in full_text_corpus:
                    score += 8
                    cues.append(f"命中核心特征词: {token}")
                    if len(cues) > 10:
                        break

        # 4. 匹配特调调色盘
        for h in skill_data.get("color_hex_palette", []):
            if h.lower() in text_lower:
                score += 15
                cues.append(f"命中专属 HEX 色彩: {h}")

        # 归一化为 0-100 分
        score = min(100.0, score)
        return score, list(dict.fromkeys(cues))[:5]

    def _get_confidence_label(self, score):
        if score >= 75:
            return "极高 (Very High)"
        elif score >= 50:
            return "较高 (High)"
        elif score >= 25:
            return "中等 (Medium)"
        elif score >= 10:
            return "微弱 (Low)"
        else:
            return "极低 (Trace)"

    def _generate_purification(self, input_text, target_style_id, homogenization):
        if not target_style_id:
            return None

        # 查找目标流派数据
        target_data = self.corpus["skills"]["visual"].get(target_style_id)
        is_visual = True
        if not target_data:
            target_data = self.corpus["skills"]["narrative"].get(target_style_id)
            is_visual = False

        if not target_data:
            return {"error": f"Target style ID '{target_style_id}' not found in corpus index."}

        # 提取核心主题
        cleaned_subject = re.sub(r"(octane render|unreal engine|hyperrealistic|4k|8k|plastic|温馨|治愈|赋能|极致体验|打造|的设计)", "", input_text, flags=re.I).strip()
        if not cleaned_subject:
            cleaned_subject = "A signature iconic subject"

        # 构造纯化提示词
        if is_visual:
            base_pos = target_data.get("positive_prompt", "")
            base_neg = target_data.get("negative_prompt", "")
            palette = target_data.get("color_hex_palette", [])
            hex_str = " ".join(palette[:4])

            # 结构化重构 Prompt
            purified_prompt = (
                f"Definitive {target_data['name']} aesthetic, focusing on {cleaned_subject}. "
                f"Anchored in authentic physical materials and restrained color palette ({hex_str}). "
                f"{base_pos} --ar 16:9 --style raw --v 6.1"
            )
            
            # 强化负向禁忌词
            forbidden_pool = base_neg
            if homogenization["deductions"]:
                forbidden_additions = []
                for d in homogenization["deductions"]:
                    forbidden_additions.extend(d["matched_terms"])
                if forbidden_additions:
                    forbidden_pool = f"{base_neg}, " + ", ".join(list(set(forbidden_additions)))

            return {
                "target_style": target_data["name"],
                "target_id": target_style_id,
                "type": "visual",
                "purified_positive_prompt": purified_prompt,
                "purified_negative_prompt": forbidden_pool,
                "recommended_palette": palette,
                "recommended_partner_voice": target_data.get("recommended_partner", ""),
                "actionable_steps": [
                    f"1. 强制注入受限特调色盘：{', '.join(palette[:4])}，维持 60:30:10 阶梯分布。",
                    "2. 剔除所有 AI 虚幻引擎/3D渲染套话，启用 '--style raw' 保证摄影与印刷物质真实度。",
                    "3. 严格遵循该流派版式网格（如 12 栏柱状网格或 ≥65% 极端留白），严禁主体膨胀填满。"
                ]
            }
        else:
            raw_sections = target_data.get("raw_sections", {})
            exemplars = raw_sections.get("4. 全真文本范例", "")
            return {
                "target_style": target_data["name"],
                "target_id": target_style_id,
                "type": "narrative",
                "rules": raw_sections.get("1. 声音灵魂与反同质化主张", ""),
                "formula": raw_sections.get("2. 词汇与意象阵列", ""),
                "forbidden_words": raw_sections.get("3. 负向禁忌词库", ""),
                "exemplars": exemplars,
                "recommended_partner_visual": target_data.get("recommended_partner", ""),
                "actionable_steps": [
                    "1. 立即删除所有‘温馨/治愈/赋能/闭环’等公关废词。",
                    "2. 采用该流派专属句式骨力，单句长度严格控制在规范区间内。",
                    "3. 引入具象的微观物理风土与感官意象，强化真实存在感。"
                ]
            }

    def format_markdown_report(self, result):
        """格式化输出专业级分析诊断报告"""
        md = []
        md.append("# 🧬 反重力风格与同质化诊断报告 (Style Analysis & Diagnostics)")
        md.append(f"**输入分析内容**：\n> {result['input_text']}\n")
        
        # 1. 同质化诊断
        homo = result["homogenization"]
        status_emoji = "🟢" if homo["status"] == "PASS" else ("🟡" if homo["status"] == "WARNING" else "🔴")
        md.append(f"## 1. AI 同质化与平庸度诊断 {status_emoji}")
        md.append(f"- **同质化指数 (Homogenization Index)**: **`{homo['homogenization_index']}/100`** ({homo['purity_tier']})")
        md.append(f"- **合规评估结果**: **`{homo['status']}`**")
        
        if homo["deductions"]:
            md.append("\n### ⚠️ 检出同质化扣分项：")
            for idx, d in enumerate(homo["deductions"], 1):
                md.append(f"{idx}. **{d['dimension']}** (扣分: -{d['penalty_points']})")
                md.append(f"   - 命中通病词汇: `{', '.join(d['matched_terms'])}`")
                md.append(f"   - 矫正法则: {d['advice']}")
        else:
            md.append("\n✅ **未检出明显 AI 模板套路，保持了优良的风格纯净度与物质真实感。**")

        # 2. 基因提取
        dna = result["dna"]
        md.append("\n## 2. 设计基因提取 (Design DNA Extraction)")
        md.append(f"- **显式 HEX 色彩**: {', '.join([f'`{c}`' for c in dna['explicit_hex_colors']]) if dna['explicit_hex_colors'] else '未显式指定 (建议注入特调色盘)'}")
        if dna["inferred_colors"]:
            md.append(f"- **推断色彩映射**: {', '.join(dna['inferred_colors'])}")
        md.append(f"- **微观物理材质**: {', '.join([f'`{m}`' for m in dna['detected_materials']]) if dna['detected_materials'] else '缺失具体物质锚点 (存在虚浮塑料感风险)'}")
        md.append(f"- **构图与网格律令**: {', '.join([f'`{l}`' for l in dna['detected_layout']]) if dna['detected_layout'] else '未指定数学网格 (易导致居中拥挤)'}")
        md.append(f"- **修辞句式特征**: {', '.join([f'`{r}`' for r in dna['detected_rhetoric']]) if dna['detected_rhetoric'] else '通用平铺叙述'}")

        # 3. 流派溯源
        matches = result["style_matches"]
        md.append("\n## 3. 流派溯源与匹配置信度 (Style Lineage Tracing)")
        if matches["top_visual"]:
            md.append("### 🎨 视觉流派匹配排行 (Top Visual Styles):")
            for idx, s in enumerate(matches["top_visual"], 1):
                md.append(f"{idx}. **{s['name']}** (`{s['id']}`) - 匹配度: **{s['score']}%** [{s['confidence']}]")
                if s["matched_cues"]:
                    md.append(f"   - 判定依据: {'; '.join(s['matched_cues'])}")
                if s["recommended_partner"]:
                    md.append(f"   - 官方推荐修辞搭档: {s['recommended_partner']}")
        
        if matches["top_narrative"]:
            md.append("\n### ✍️ 叙事修辞流派匹配排行 (Top Narrative Styles):")
            for idx, s in enumerate(matches["top_narrative"], 1):
                md.append(f"{idx}. **{s['name']}** (`{s['id']}`) - 匹配度: **{s['score']}%** [{s['confidence']}]")
                if s["matched_cues"]:
                    md.append(f"   - 判定依据: {'; '.join(s['matched_cues'])}")
                if s["recommended_partner"]:
                    md.append(f"   - 官方推荐视觉搭档: {s['recommended_partner']}")

        # 4. 深度纯化重构方案
        ref = result["refactoring"]
        if ref:
            md.append(f"\n## 4. 深度纯化重构方案 (Deep Purification Engine)")
            md.append(f"**目标流派锁定**：`{ref['target_style']}` (`{ref['target_id']}`)\n")
            
            if ref.get("type") == "visual":
                md.append("### 🎯 纯化重构图像生成提示词 (Midjourney v6.1 / SDXL 工业级资产):")
                md.append(f"```text\n{ref['purified_positive_prompt']}\n```")
                md.append("### 🚫 硬性负向禁忌词 (Negative Prompt):")
                md.append(f"```text\n{ref['purified_negative_prompt']}\n```")
                md.append(f"- **受限特调色盘**: `{' | '.join(ref['recommended_palette'][:4])}`")
            else:
                md.append("### 📝 流派核心句式与修辞范式:")
                md.append(f"{ref['formula']}\n")
                md.append("### 🚫 严禁词汇与表达:")
                md.append(f"{ref['forbidden_words']}\n")
                if ref.get("exemplars"):
                    md.append(f"### 📖 全真范例文本:\n{ref['exemplars']}\n")

            md.append("### 🛠️ 改造执行步骤:")
            for step in ref["actionable_steps"]:
                md.append(f"- {step}")

        return "\n".join(md)

def main():
    parser = argparse.ArgumentParser(description="Style Analyzer - 反重力风格与内容分析引擎")
    parser.add_argument("--input", "-i", type=str, help="输入分析文本或提示词")
    parser.add_argument("--file", "-f", type=str, help="从文件读取输入内容")
    parser.add_argument("--target", "-t", type=str, help="指定纯化目标流派 ID (如 style-neo-chinese-zen)")
    parser.add_argument("--domain", "-d", choices=["auto", "visual", "narrative"], default="auto", help="分析领域")
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出结果")

    args = parser.parse_args()

    input_text = ""
    if args.input:
        input_text = args.input
    elif args.file and os.path.isfile(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            input_text = f.read()
    else:
        # 演示默认测试输入
        input_text = (
            "A futuristic cyberpunk electric tea kettle, octane render, unreal engine 5, "
            "trending on artstation, 8k wallpaper, volumetric lighting, glossy plastic, "
            "purple and blue neon glow, centered composition. "
            "旨在为年轻都市白领赋能极致的生活体验，让每一刻都充满温馨与治愈。"
        )

    analyzer = StyleAnalyzer()
    result = analyzer.analyze(input_text, target_style_id=args.target, domain=args.domain)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(analyzer.format_markdown_report(result))

if __name__ == "__main__":
    main()
