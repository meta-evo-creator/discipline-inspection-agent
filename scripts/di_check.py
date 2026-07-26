#!/usr/bin/env python3
"""
DI First-Run Verification Script
Check all dependencies → Run a sample query → Output analysis report
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
    print("DI Discipline Inspection Agent — First-Run Check")
    print("=" * 50)
    all_ok = True

    # 1. Configuration file
    print("\n[1/5] Configuration")
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config = yaml.safe_load(f)
        source = config.get('regulation_source', 'not set')
        check(f"di-config.yaml exists → regulation_source={source}")
    else:
        all_ok &= check("di-config.yaml not found — using builtin defaults", True)
        config = {'regulation_source': 'builtin'}

    # 2. Regulation pack
    print("\n[2/5] Regulation Pack")
    builtin = SKILL_DIR / "providers/default/knowledge/regulations"
    regs = list(builtin.glob("*.md")) if builtin.exists() else []
    all_ok &= check(f"Built-in regulations: {len(regs)} documents", len(regs) >= 3)

    # 3. Agent files
    print("\n[3/5] Agent Files")
    agents = SKILL_DIR / "agents"
    required = ["scope", "search-rg", "search-pkulaw", "merge", "audit",
                "analyze", "draft", "review", "revise", "publish"]
    for a in required:
        ok = (agents / f"{a}.md").exists()
        all_ok &= check(f"agents/{a}.md", ok)

    # 4. ripgrep availability
    print("\n[4/5] ripgrep Search Tool")
    try:
        r = subprocess.run(["rg", "--version"], capture_output=True, text=True, timeout=5)
        all_ok &= check(f"rg {r.stdout.strip()[:40]}", r.returncode == 0)
    except Exception:
        all_ok &= check("rg unavailable — install: https://github.com/BurntSushi/ripgrep", False)

    # 5. Quick test — rg search built-in regulations
    print("\n[5/5] Functional Test — rg search built-in regulations")
    test_query = "Article 97"
    try:
        r = subprocess.run(
            ["rg", "-l", test_query, str(builtin)],
            capture_output=True, text=True, timeout=10
        )
        hits = len(r.stdout.strip().split('\n')) if r.stdout.strip() else 0
        all_ok &= check(f'rg "{test_query}" → {hits} regulation hits', hits > 0)
    except Exception as e:
        all_ok &= check(f"Search failed: {e}", False)

    # Summary
    print("\n" + "=" * 50)
    if all_ok:
        print("✅ All checks passed. DI is ready to run.")
        print("\nNext steps:")
        print("  1. Edit di-config.yaml to configure your environment")
        print("  2. Send a discipline inspection case to the DI Agent to begin analysis")
        print("  3. Optional: Set WIKI_PATH to access the full 45+ regulation library")
        print("  4. Optional: Configure PKULaw subscription for authoritative version verification")
    else:
        print("❌ Some checks failed. Fix the ❌ items above and re-run.")
    print("=" * 50)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
