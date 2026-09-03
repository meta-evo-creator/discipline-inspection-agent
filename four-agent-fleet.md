# DI Four-Agent Fleet (v3.0) — Technical Description

> Companion document to the DI v3.0 README. Everything here is a **desensitized, methodology-level description** — no real case, person, institution, or amount is referenced.

## 1. Architecture Overview

```
         ┌──────────────────────────────────────────────────┐
         │   Joint Foundation (all four agents share)       │
         │   §1-§4: subject & scope · dual-track search      │
         │   (local law library + official database) ·      │
         │   article citation & audit · clause verification │
         └──────────────────────────────────────────────────┘
                 │
   Lead ──► [CT] Clue Triage ──► [IO] Interview Outline ──► [CD] Determination ──► [PD] Recommendation
                 │ (disposition)        │ (handbook)              │ (opinion)          │ (document)
                 └──────────────────────┴─────────────────────────┴────────────────────┘
                  Each handover is acceptance-checked before the next phase starts.
```

## 2. CT — Clue Triage Specialist

**Skill**: `clue-triage` · **Entry**: any new lead / complaint material.

### Structure (five segments)
1. Lead source & content
2. Subject identity & relationship (role, authority boundaries)
3. Checkability analysis (specificity, directionality, timeliness)
4. Related-lead hints (cross-references, no proactive association with unrelated persons)
5. Disposition proposal

### Workflow
```
Intake & register → identity verification → checkability analysis → disposition proposal
→ hand off (close / shelve / consult-verify / interview & inquiry)
```

### Sample artifact (desensitized illustration)
> A department director is reported to have repeatedly attended banquets hosted by vendors.
> - Clear subject · specific events → recommend preliminary verification
> - No benefit-seeking evidence → consult-verify (interview & inquiry)
> - Source not credible → close

## 3. IO — Interview Outline Specialist

**Skill**: `interview-outline` · **Entry**: before any interview / inquiry conversation.

### Structure (five segments)
1. Subject basics
2. Interview objective
3. Question list (with follow-up plans)
4. Discipline & safety items
5. Appendix: regulation base list

### Workflow
```
Master the case facts → set the interview objective → design questions (four elements each)
→ write follow-up plans → finalize the handbook
```

### Four elements per question
**What to ask · Why ask it · How to follow up · Expected answer (pre-judged)**

### Sample artifact (desensitized illustration)
> Banquet of May 12 at a restaurant:
> - Who organized · who paid · any official basis → verifying facts
> - Were any management-service objects present → determining nature
> - How was the bill settled · any receipts → fixing evidence

## 4. CD — Case Determination Specialist

**Skill**: `case-determination` (+ `case-evidence-argumentation`) · **Entry**: after facts are verified.

### Structure (five steps)
1. Behavior determination: violation + culpability (dual-factor)
2. Sentencing three questions: benefit-seeking? exchange of favors? violation only?
3. Grading rules: penalty-coordinate mapping
4. Eight-dimension review: amount · frequency · relationship · intention · consequences · remorse · record · time/place
5. Adversarial debate: charge → defense → rebuttal → re-rebuttal

### Workflow
```
Fact verification (verbatim against case files) → determination mapping (behavior → clause)
→ sentencing deduction (three questions + grading) → eight-dimension check
→ adversarial debate → opinion output with clause citations
```

### Sample artifact (desensitized illustration)
> Twelve banquets + a gift worth 18,000; no benefit-seeking evidence.
> - Determination: violation of the central eight-point rules spirit; **excluded** from power-for-money trading (no benefit-seeking)
> - Sentencing: serious warning within the Party (aligned with the public-discipline mark)

## 5. PD — Proposal Drafting Specialist

**Skill**: `proposal-drafting` · **Entry**: case handling stage (after CD).

### Structure (five parts)
1. Basic facts
2. Verification results
3. Determination analysis
4. Recommendation (penalty tier + basis)
5. Closing (with clause citations incl. version status)

### Workflow
```
Collect all phase products → draft five parts → first scoring (80-point gate)
→ revise against the checklist → re-score (≥80) → issue the formal recommendation
```

### Quality gate (80 points)
Citation completeness · version accuracy · factual wording (no exaggeration) · logical chain · sensitivity of expression. A first pass below 80 goes back for revision.

## 6. Operational Notes

- **Model tier**: all four agents use the primary deep-analysis model. Free/local tiers are never the main carrier; they exist only as emergency fallback after explicit review.
- **Fail-closed**: `fallback_providers` is empty in every agent config. No automatic switch to third-party providers — L2 material never crosses machines by accident.
- **Toolset narrowing**: each agent keeps terminal/file/code/skills/todo/web only; no browser, no delegation, no global memory writes, no cron, no gateway ops — structural, not advisory.
- **Skill anti-drift**: each agent loads only its own skill(s) + shared bases; any public skill changes require explicit synchronization.
- **Desensitization**: all sample artifacts use placeholders (subjects, dates, amounts). No real case data is used in this repository.
