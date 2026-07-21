# DI 纪律审查智能系统 ⚔️

> **AI 驱动的纪律审查管线——从线索到谈话提纲，全流程自动化。**
> 10 Agent · 双因素分析 · 六维评分 · 开箱即用

---

## 30 秒安装

```bash
# 1. 确保已安装 Hermes Agent
hermes --version

# 2. 下载 DI skill
cd ~/AppData/Local/hermes/skills/
git clone https://github.com/meta-evo-creator/discipline-inspection.git

# 3. 首次验证
python skills/discipline-inspection/scripts/di_check.py
```

看到 `✅ 全部检查通过` 即可使用。**零配置，内置 3 部核心法规。**

---

## 三种用法

### 快速咨询
直接问 DI Agent：
> "王某是中共党员、外科主任，2023年5月收了医药代表一台5000元的咖啡机。帮我分析。"

### 谈话提纲
发送完整线索，Agent 自动生成谈话手册：
> "我院收到以下线索：1.……2.……3.……帮我写谈话提纲。"

### 完整案件分析
标准 10-Agent 全管线——法规检索 → 版本验证 → 双因素分析 → 对抗辩论 → 质量评分 → 报告生成。

---

## 配置（可选）

编辑 `di-config.yaml`：

```yaml
regulation_source: builtin   # builtin | wiki | web
wiki_path: ""               # WIKI 法规库路径（wiki模式需要）
pkulaw: disabled            # 北大法宝版本验证
ima:
  enabled: false            # IMA 知识库上传
  kb_id: ""
```

默认 `builtin` 模式无需配置任何东西。

---

## 能力

| | builtin（免费） | wiki + pkulaw（完整） |
|:-----|:--:|:--:|
| 法规数量 | 3 部核心法规 | 45+ 部全文 |
| 版本验证 | ❌ | ✅ pkulaw 权威验证 |
| 指导性案例 | ❌ | ✅ 11 个 CCDI 案例 |
| 通用案例模式 | ❌ | ✅ P01-P05 违规模式 |
| 知识图谱 | ❌ | ✅ 131 节点/136 边 |
| IMA 上传 | ❌ | ✅ |
| 分析方法论 | ✅ 双因素+六维评分 | ✅ 全部 |

---

## 文档

- [双因素分析方法论](METHODOLOGY.md) — 违规+有责分析框架
- [配置文件说明](di-config.yaml) — 所有可配置项
- [Agent 管线架构](SKILL.md) — 10 Agent 完整说明

---

## 许可

MIT License
