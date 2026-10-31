# -*- coding: utf-8 -*-
"""
install_to_antigravity.py - 将 ai-style-design 套件完整安装并导入反重力全局与工作区 Skill 库
"""

import os
import sys
import shutil
import json
import subprocess

# 强制标准输出为 utf-8 编码
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def create_junction(src, dst):
    """创建 Windows Junction 链接"""
    if os.path.exists(dst) or os.path.islink(dst):
        try:
            if os.path.islink(dst):
                os.unlink(dst)
            elif os.path.isdir(dst):
                # 检查是否为 junction
                subprocess.run(f'rmdir "{dst}"', shell=True, check=True)
            else:
                os.remove(dst)
        except Exception as e:
            print(f"Warning removing old link {dst}: {e}")
    
    cmd = f'cmd /c mklink /J "{dst}" "{src}"'
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"  [Link OK] {dst} -> {src}")
    else:
        # 如果创建 Junction 失败，直接复制目录作为安全降级方案
        print(f"  [Junction failed, copying directory instead]: {res.stderr}")
        shutil.copytree(src, dst, dirs_exist_ok=True)

def main():
    workspace_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"=== 开始安装 ai-style-design 至反重力 (Antigravity) 技能库 ===")
    print(f"当前源目录: {workspace_root}")

    # 1. 确保工作区本地 skills/ 下具备顶层平铺的 style-analyzer 和 style-designer
    src_analyzer = os.path.join(workspace_root, "skills", "interfaces", "style-analyzer")
    src_designer = os.path.join(workspace_root, "skills", "interfaces", "style-designer")
    dst_analyzer_local = os.path.join(workspace_root, "skills", "style-analyzer")
    dst_designer_local = os.path.join(workspace_root, "skills", "style-designer")

    shutil.copytree(src_analyzer, dst_analyzer_local, dirs_exist_ok=True)
    shutil.copytree(src_designer, dst_designer_local, dirs_exist_ok=True)
    print("✓ 本地 skills/ 顶层接口平铺完成 (skills/style-analyzer & skills/style-designer)")

    # 2. 反重力全局安装目标
    global_base = os.path.expanduser("~/.gemini/antigravity")
    global_target = os.path.join(global_base, "skills", "ai-style-design")
    os.makedirs(global_target, exist_ok=True)
    print(f"\n目标安装根路径: {global_target}")

    # 复制核心资产文件
    files_to_copy = [
        "plugin.json", "package.json", "SKILL.md", "README.md",
        "PROGRESS.md", "DESIGN_SKILLS_FRAMEWORK.md", "corpus_index.json"
    ]
    for f in files_to_copy:
        src_f = os.path.join(workspace_root, f)
        if os.path.isfile(src_f):
            shutil.copy2(src_f, os.path.join(global_target, f))
    print(f"✓ 核心元数据与索引文件复制完成 ({len(files_to_copy)} 个文件)")

    # 复制 scripts 目录
    shutil.copytree(os.path.join(workspace_root, "scripts"), os.path.join(global_target, "scripts"), dirs_exist_ok=True)
    print("✓ 驱动脚本目录复制完成 (scripts/)")

    # 复制 skills 目录 (包含 visual, narrative, interfaces, style-analyzer, style-designer)
    shutil.copytree(os.path.join(workspace_root, "skills"), os.path.join(global_target, "skills"), dirs_exist_ok=True)
    print("✓ 全量技能语料库复制完成 (skills/ 38 个模块)")

    # 3. 在 C:\Users\zhaoz\.gemini\antigravity\skills 创建全局 Junction 快捷识别
    antigravity_skills_dir = os.path.join(global_base, "skills")
    print(f"\n配置反重力技能暴露链接至: {antigravity_skills_dir}")
    create_junction(global_target, os.path.join(antigravity_skills_dir, "ai-style-design"))
    create_junction(os.path.join(global_target, "skills", "style-analyzer"), os.path.join(antigravity_skills_dir, "style-analyzer"))
    create_junction(os.path.join(global_target, "skills", "style-designer"), os.path.join(antigravity_skills_dir, "style-designer"))

    # 4. 更新 ~/.gemini/config/skills.json
    config_dir = os.path.expanduser("~/.gemini/config")
    skills_json_path = os.path.join(config_dir, "skills.json")
    if os.path.isfile(skills_json_path):
        try:
            with open(skills_json_path, "r", encoding="utf-8") as f:
                skills_cfg = json.load(f)
        except Exception:
            skills_cfg = {"entries": []}
    else:
        skills_cfg = {"entries": []}

    target_skills_path_normalized = os.path.join(global_target, "skills").replace("\\", "/")
    existing_paths = [e.get("path") for e in skills_cfg.get("entries", [])]
    if target_skills_path_normalized not in existing_paths:
        skills_cfg["entries"].append({"path": target_skills_path_normalized})
        with open(skills_json_path, "w", encoding="utf-8") as f:
            json.dump(skills_cfg, f, indent=2, ensure_ascii=False)
        print(f"✓ 已将 {target_skills_path_normalized} 成功注册到 {skills_json_path}")
    else:
        print(f"✓ {skills_json_path} 中已存在该挂载项，无需重复写入")

    # 5. 在 ~/.gemini/config/plugins/ 和 ~/.gemini/config/skills/ 建立链接
    cfg_plugins_dir = os.path.join(config_dir, "plugins")
    cfg_skills_dir = os.path.join(config_dir, "skills")
    os.makedirs(cfg_plugins_dir, exist_ok=True)
    os.makedirs(cfg_skills_dir, exist_ok=True)

    print(f"\n配置全局配置目录链接:")
    create_junction(global_target, os.path.join(cfg_plugins_dir, "ai-style-design"))
    create_junction(global_target, os.path.join(cfg_skills_dir, "ai-style-design"))
    create_junction(os.path.join(global_target, "skills", "style-analyzer"), os.path.join(cfg_skills_dir, "style-analyzer"))
    create_junction(os.path.join(global_target, "skills", "style-designer"), os.path.join(cfg_skills_dir, "style-designer"))

    # 6. 为当前工作区配置 .agents/skills (本地优先发现)
    workspace_agents_skills = os.path.join(workspace_root, ".agents", "skills")
    os.makedirs(workspace_agents_skills, exist_ok=True)
    create_junction(os.path.join(workspace_root, "skills", "style-analyzer"), os.path.join(workspace_agents_skills, "style-analyzer"))
    create_junction(os.path.join(workspace_root, "skills", "style-designer"), os.path.join(workspace_agents_skills, "style-designer"))
    print(f"✓ 工作区本地优先发现配置完成 (.agents/skills/)")

    print("\n🎉 === 全量导入与安装成功！===")
    print("反重力 (Antigravity) 现已无缝识别以下技能：")
    print("1. [style-analyzer] : 反重力风格溯源与 5 维同质化诊断器")
    print("2. [style-designer] : 反重力智能设计与工业级 Prompt 调度器")
    print("3. [ai-style-design]: 全球近现代设计美学与文字叙事风格总控套件")

if __name__ == "__main__":
    main()
