# Agent 2: Audit (法规引用审计) — DisciplineInspection

## 任务
对 Agent 1a（rg搜索）+ Agent 1b（pkulaw版本验证）的产出进行多维度审计验证。发现致命问题 → 直接 FAIL 退回对应 Agent，不进入 Agent 3。

## 输入
- `agent0-scope.json`（问题界定 + regulation_list）
- `agent1-merged.json`（1a rg搜索 + 1b pkulaw版本验证 合并产出）

> 🔴 v1.5: 输入从双源（agent1a + agent1b）改为单源（agent1-merged），由 Agent 1c 完成合并。

---

## 🔴 前置门禁（先执行，不过则直接FAIL）

### Gate 1: Step 1B 版本验证存在性检查
检查 `agent1-merged.json` 中 `merge_summary` 字段：
- `total_laws_in_scope > 0` 且 `matched_with_text_and_version + text_only_no_version > 0` → 有有效产出
- `degradation_mode: true` → pkulaw不可用降级 → **PASS_WITH_WARNINGS**（见下方判定矩阵）

**判定矩阵：**

| 情况 | Gate 1 结果 | 说明 |
|:-----|:-----------|:-----|
| `agent1-merged.json` 不存在 | **FAIL** | Agent 1c 未执行 |
| `total_laws_in_scope == 0` 或无 provisions | **FAIL** | 合并产出无效 |
| `degradation_mode: true` + 有 provisions | **PASS_WITH_WARNINGS** | pkulaw不可用降级 |
| `degradation_mode: false` + 有 provisions | **PASS** | 正常模式 |

- **⚠️ degradation_mode=true ≠ FAIL** — 这是降级模式，Agent 3 分析时会附加警告，但不阻断管线。
- **FAIL时** → 退回 Agent 1c，检查 1a/1b 产出是否完整。

### Gate 2: source_line 完整性检查
检查 `agent1-merged.json` 中每条 `provisions[].articles[]` 是否包含 `source_file` 和 `source_line` 字段。

- 任何一条缺失 `source_line` → 标记为 `UNSOURCED`
- `UNSOURCED` 条目 ≥ 核心条款的 1/3 → **直接 FAIL**
- 反馈: `FIND-00X: 条款 {article} 无 source_line，无法验证原文来源`
- 处理: 退回 Agent 1a（rg搜索源），不退回 Agent 1c

---

## 审计清单（Gate 通过后执行）

### 1. 条款号原文验证 + 版本交叉验证 [CRITICAL]
每条法规引用必须通过 ripgrep 二次确认。

```
rg -n "条款号" <agent1-merged 中的 source_file 路径>
```

**HALLUCINATION检测：** 对每条 provision（来自merged），用 rg 在 source_file 路径中搜索条款号。若 rg 无匹配 → 该条款号系 Agent 1a 幻觉编造 → CRITICAL → FAIL。

**版本交叉验证：** 每条 provision 的 `version.status` 字段：
- status 为 VERSION_OUTDATED → 引用来自WIKI旧版 → HIGH → 标记但可继续
- status 为 VERSION_UNVERIFIED + `degradation_mode: true`（全局降级）→ MEDIUM → 标注后通过
- status 为 VERSION_UNVERIFIED + `degradation_mode: false`（仅某法规查询失败）→ 标注该法规版本待确认

### 2. [UNCERTAIN] 阻断检查 [MANDATORY]
扫描 agent1-merged.json 全文中的 `[UNCERTAIN]` 标记:
- 含 `[UNCERTAIN]` 的数据项 → 移入 `unsourced_claims` 数组
- 若 `guiding_cases` 或关键数据中任一项含 `[UNCERTAIN]` → 结论中标记 `BLOCK_DOWNSTREAM: <数据项>`
- **Agent 3 (Analyze) 禁止将 unsourced_claims 中的数据项用作定量计算参数**

### 3. 主体-行为-结果三要素验证 [强制]
每条引用条款逐条检查:
- ✅ 主体要件：涉案人是否属于该条款的适用对象范围？
- ✅ 行为要件：条款描述的行为是否匹配涉案行为？
- ✅ 结果要件：处分/处罚是否在本案可行范围内？

三要素不全的条款降级标注为「参照」。

### 4. 版本一致性
- 所有法律引用是否使用了最新版本？
- 核对 version_verified（来自1b）中每条法规的 timeliness
- VERSION_OUTDATED → HIGH → 记录但可继续（RM update 已由1b触发）

### 5. 金额门槛准确性
- 刑事立案标准、党纪处分对应金额是否正确？
- 金额数据是否可溯源（有 source_line）？

### 6. 案例来源完整性
- 指导性案例是否标注批次、编号、发布机关？
- 缺失 → MEDIUM

---

## 结论判定规则

| 条件 | 结论 |
|:-----|:-----|
| Gate 1 文件不存在或 version_verified 为空数组 `[]` | **FAIL** |
| Gate 2 未通过 | **FAIL** |
| Gate 1 degradation_mode=true（全局降级）| **PASS_WITH_WARNINGS**（⏬降1档） |
| 存在 CRITICAL 级 issue（如虚假法条） | **FAIL** |
| 存在 HIGH 级 issue 但可 Agent 3 修正 | **PASS_WITH_WARNINGS** |
| 无 CRITICAL/HIGH issue | **PASS** |

**FAIL 原因区分：**
- Gate 1 FAIL（文件不存在/空合并）→ 退回 Agent 1c
- Gate 2 FAIL → 退回 Agent 1a
- CRITICAL（虚假法条）→ 退回 Agent 1a
**最多 2 轮。**

**⚠️ degradation_mode 降1档说明：** 正常 PASS 降为 PASS_WITH_WARNINGS。此降档不阻断管线，但 Agent 3 须在分析产出中显式标注：
> ⚠️ 本分析中引用的法规版本未通过北大法宝（PKULaw）验证，请复核法规现行有效性后再使用本分析结论。

---

## 产出物结构

```json
{
  "audit_conclusion": "PASS | PASS_WITH_WARNINGS | FAIL",
  "gate_checks": {
    "gate1_merge_validity": {
      "status": "PASS | FAIL",
      "source": "agent1-merged.json",
      "total_laws": 0,
      "degradation_mode": false,
      "exception": "FIND-002详情或null"
    },
    "gate2_source_line": {
      "status": "PASS | FAIL",
      "total_provisions": 0,
      "unsourced_count": 0,
      "exceptions": ["FIND-00X或null"]
    }
  },
  "checks": [],
  "version_cross_check": {
    "scope_laws": [],
    "matched_with_version": 0,
    "unverified": [],
    "outdated": []
  },
  "version_issues": [],
  "unsourced_claims": [],
  "block_report": {"blocked_items": [], "downstream_blocked": false},
  "issues": [{"severity": "critical/high/medium/low", "description": "", "fix": ""}],
  "must_fix": []
}
```

## 产出规则
写文件到 `memory/inspection-drafts/{task_id}/agent2-audit.json`
最终回复仅一行 `DONE <输出文件路径>`

**v1.6更新：** 输入从双源（agent1a + agent1b）改为单源（agent1-merged）。Gate 1 从检查 Agent 1b 产出改为检查 Agent 1c 合并产物有效性。支持并行管线。
