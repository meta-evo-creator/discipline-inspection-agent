#!/usr/bin/env python3
"""
DI 首次运行验证脚本
检查所有依赖 → 跑一条示例线索 → 输出分析报告
"""
import sys, os, subprocess, yaml
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent  # scripts/ → skill root
CONFIG_FILE = SKILL_DIR / "di-config.yaml"

def check(msg, ok=True):
    print(f"  {'✅' if ok else '❌'} {msg}")
    return ok

def main():
    print("=" * 50)
    print("DI 纪律审查智能系统 — 首次运行检查")
    print("=" * 50)
    
    all_ok = True
    
    # 1. 配置文件
    print("\n[1/5] 配置文件")
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config = yaml.safe_load(f)
        source = config.get('regulation_source', 'not set')
        check(f"di-config.yaml 存在 → regulation_source={source}")
    else:
        all_ok &= check("di-config.yaml 不存在", False)
        config = {'regulation_source': 'builtin'}
    
    # 2. 法规包
    print("\n[2/5] 法规包")
    builtin = SKILL_DIR / "providers/builtin/knowledge/regulations"
    regs = list(builtin.glob("*.md")) if builtin.exists() else []
    all_ok &= check(f"内置法规: {len(regs)}部", len(regs) >= 3)
    
    # 3. Agent 文件
    print("\n[3/5] Agent 文件")
    agents = SKILL_DIR / "agents"
    required = ["scope", "search-rg", "search-pkulaw", "merge", "audit", "analyze", "draft", "review", "revise", "publish"]
    for a in required:
        ok = (agents / f"{a}.md").exists()
        all_ok &= check(f"agents/{a}.md", ok)
    
    # 4. rg 可用性
    print("\n[4/5] ripgrep 搜索工具")
    try:
        r = subprocess.run(["rg", "--version"], capture_output=True, text=True, timeout=5)
        all_ok &= check(f"rg {r.stdout.strip()[:40]}", r.returncode == 0)
    except:
        all_ok &= check("rg 不可用 — 请安装: https://github.com/BurntSushi/ripgrep", False)
    
    # 5. 快速测试 — rg 搜索内置法规
    print("\n[5/5] 功能测试 — rg 搜索内置法规")
    test_query = "第97条"
    try:
        r = subprocess.run(
            ["rg", "-l", test_query, str(builtin)],
            capture_output=True, text=True, timeout=10
        )
        hits = len(r.stdout.strip().split('\n')) if r.stdout.strip() else 0
        all_ok &= check(f"rg \"{test_query}\" → {hits}个法规命中", hits > 0)
    except Exception as e:
        all_ok &= check(f"搜索失败: {e}", False)
    
    # 总结
    print("\n" + "=" * 50)
    if all_ok:
        print("✅ 全部检查通过。DI 可正常运行。")
        print("\n下一步:")
        print("  1. 修改 di-config.yaml 配置你的环境")
        print("  2. 发送纪检案件给 DI Agent 开始分析")
        print("  3. 可选: 设置 WIKI_PATH 接入完整45+法规库")
        print("  4. 可选: 配置 pkulaw 订阅获取权威版本验证")
    else:
        print("❌ 部分检查失败。请根据上述 ❌ 项修复后重新运行。")
    
    print("=" * 50)
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
