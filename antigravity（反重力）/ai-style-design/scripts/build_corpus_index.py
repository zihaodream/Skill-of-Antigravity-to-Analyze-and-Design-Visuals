# -*- coding: utf-8 -*-
import os
import json
import re

def parse_markdown_skill(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Parse YAML frontmatter
    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    metadata = {}
    if fm_match:
        fm_text = fm_match.group(1)
        for line in fm_text.splitlines():
            line = line.strip()
            if ":" in line:
                k, v = line.split(":", 1)
                k = k.strip()
                v = v.strip().strip('"')
                if v.startswith("[") and v.endswith("]"):
                    # list of tags
                    items = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
                    metadata[k] = items
                else:
                    metadata[k] = v

    # Extract title
    title_match = re.search(r"^#\s+(?:风格定义：|叙事修辞：)?(.*)$", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else metadata.get("name", "")

    # Extract sections
    sections = {}
    current_sec = None
    sec_content = []
    
    for line in content.splitlines():
        sec_header = re.match(r"^##\s+(\d+\.\s+[^(\n]+)", line)
        if sec_header:
            if current_sec:
                sections[current_sec] = "\n".join(sec_content).strip()
            current_sec = sec_header.group(1).strip()
            sec_content = []
        elif current_sec:
            sec_content.append(line)
    if current_sec:
        sections[current_sec] = "\n".join(sec_content).strip()

    # Extract color hex codes if visual
    hex_codes = re.findall(r"#[0-9a-fA-F]{6}", content)
    unique_hex = list(dict.fromkeys([h.upper() for h in hex_codes]))

    # Extract recommended pair
    rec_match = re.search(r"(?:协同 Skill|最佳搭档视觉 Skill)[：:]\s*(.*)", content)
    rec_pair = rec_match.group(1).strip() if rec_match else ""

    # Positive prompt & Negative prompt if present
    pos_match = re.search(r"- \*\*Positive Prompt\*\*:\s*\n\s*>\s*(.*?)(?=\n- \*\*Negative Prompt\*\*|\Z)", content, re.DOTALL)
    neg_match = re.search(r"- \*\*Negative Prompt\*\*:\s*\n\s*>\s*(.*?)(?=\n##|\Z)", content, re.DOTALL)
    pos_prompt = pos_match.group(1).strip() if pos_match else ""
    neg_prompt = neg_match.group(1).strip() if neg_match else ""

    return {
        "id": metadata.get("name", os.path.basename(os.path.dirname(file_path))),
        "name": title,
        "description": metadata.get("description", ""),
        "version": metadata.get("version", "1.0.0"),
        "tags": metadata.get("tags", []),
        "color_hex_palette": unique_hex,
        "recommended_partner": rec_pair,
        "positive_prompt": pos_prompt,
        "negative_prompt": neg_prompt,
        "raw_sections": sections
    }

def main():
    corpus = {
        "metadata": {
            "version": "1.1.0",
            "title": "AI 设计流派与叙事修辞结构化特征索引矩阵",
            "total_skills": 0,
            "visual_count": 0,
            "narrative_count": 0,
            "interfaces_count": 0,
            "created_at": "2026-10-30"
        },
        "skills": {
            "visual": {},
            "narrative": {},
            "interfaces": {}
        }
    }

    visual_dir = os.path.join("skills", "visual")
    for d in sorted(os.listdir(visual_dir)):
        skill_file = os.path.join(visual_dir, d, "SKILL.md")
        if os.path.isfile(skill_file):
            parsed = parse_markdown_skill(skill_file)
            parsed["category"] = "visual"
            corpus["skills"]["visual"][parsed["id"]] = parsed
            corpus["metadata"]["visual_count"] += 1

    narrative_dir = os.path.join("skills", "narrative")
    for d in sorted(os.listdir(narrative_dir)):
        skill_file = os.path.join(narrative_dir, d, "SKILL.md")
        if os.path.isfile(skill_file):
            parsed = parse_markdown_skill(skill_file)
            parsed["category"] = "narrative"
            corpus["skills"]["narrative"][parsed["id"]] = parsed
            corpus["metadata"]["narrative_count"] += 1

    interfaces_dir = os.path.join("skills", "interfaces")
    if os.path.isdir(interfaces_dir):
        for d in sorted(os.listdir(interfaces_dir)):
            skill_file = os.path.join(interfaces_dir, d, "SKILL.md")
            if os.path.isfile(skill_file):
                parsed = parse_markdown_skill(skill_file)
                parsed["category"] = "interface"
                corpus["skills"]["interfaces"][parsed["id"]] = parsed
                corpus["metadata"]["interfaces_count"] += 1

    corpus["metadata"]["total_skills"] = corpus["metadata"]["visual_count"] + corpus["metadata"]["narrative_count"] + corpus["metadata"]["interfaces_count"]

    index_path = "corpus_index.json"
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(corpus, f, ensure_ascii=False, indent=2)

    print(f"Generated {index_path} with {corpus['metadata']['total_skills']} skills ({corpus['metadata']['visual_count']} visual, {corpus['metadata']['narrative_count']} narrative, {corpus['metadata']['interfaces_count']} interfaces).")

if __name__ == "__main__":
    main()
