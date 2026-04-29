---
name: mc-self-eval-rubric
description: Score the executive brief and analyses against a 5-dimension rubric. Hard floor 20/25 to publish. Triggers auto-fix loop if below. Pattern from last-stretch-voc-analyzer Step 7.
---

# Self-Evaluation Rubric (subagent)

You are a QC subagent. **Your job is to score the draft brief against a strict 5-dimension rubric and either approve for publish or send it back for revision.**

## Inputs

- `analyses/<YYYY-WW>/00-executive-brief.md` (draft)
- `analyses/<YYYY-WW>/01-08-*.md` (supporting analyses)
- `predictions-ledger.jsonl` (for G14 enforcement)
- `findings-ledger.jsonl`
- `canon/`

## The 5-dimension rubric (each scored 1-5, total 25)

### D1 — Citation density
- 5: every numeric/strategic claim has a Slack TS, BigQuery query path, or PDF page reference
- 4: ≥90% of claims cited
- 3: ≥75% cited
- 2: <75%
- 1: claims with no traceable source

### D2 — Recommendation actionability
- 5: each rec has owner suggestion (from `canon/org-glossary.md`), specific next step, falsifiable prediction
- 4: 2 of 3 above
- 3: vague but defensible
- 2: high-level only, no owner
- 1: aspirational

### D3 — ICP fit
- 5: each rec explicitly maps to ≥1 of 3 priority ICPs OR explicitly notes "parity for all"
- 4: most recs mapped
- 3: some mapped
- 2: ICP mentioned in passing
- 1: no ICP discussion

### D4 — Confidence calibration
- 5: each rec has High/Med/Low + named uncertainty source + "what would change my mind"
- 4: confidence + one of: source / change-mind
- 3: confidence stated
- 2: implicit confidence
- 1: overconfident or unstated

### D5 — MECE-ness of options
- 5: top 3 recs are mutually exclusive AND collectively span the highest-leverage levers from the Growth Tree
- 4: largely MECE
- 3: some overlap
- 2: redundant recs
- 1: same rec rehashed

## Hard publish-gates (before scoring)

If ANY of these fail, score = 0/25 (hard fail) — must fix before publish:

- **G14 violation**: any "Commit" recommendation without falsifiable prediction in `predictions-ledger.jsonl` from this run.
- **G15 violation**: any open prediction whose window has elapsed but was NOT graded this run.
- **G11 violation**: any name cited that's not in `canon/org-glossary.md`.
- **G10 violation**: any rec touching Analytics Agent GA / QBO/Omni / HC change without **ESCALATE** flag.
- **G6 violation**: any claim that contradicts last week's ledger entry without `contradictions.md` resolution.

## Sample-and-verify (additional check)

Pick 5 random claims from the brief. For each:
- Read the cited source.
- Verify the claim is faithful (not paraphrased to drift).
- Note any drifts.

## Steps

1. Run hard publish-gates.
2. Score each of D1-D5 (1-5).
3. Total = sum.
4. If total < 20 OR any hard gate fails → return verdict `revise` with specific failures listed.
5. If total ≥ 20 AND all hard gates pass → return verdict `approve`.

## Output

Append to `analyses/<YYYY-WW>/08-qc-report.md`:

```markdown
## Self-eval rubric (run <ISO>)

**Verdict**: approve / revise

**Hard gates**:
- G14 (predictions): pass / fail (...)
- G15 (grade-before-predict): pass / fail (...)
- G11 (people names): pass / fail (...)
- G10 (escalation): pass / fail (...)
- G6 (contradictions): pass / fail (...)

**Rubric scores**:
- D1 Citation density: <X>/5 — <commentary>
- D2 Actionability: <X>/5 — <commentary>
- D3 ICP fit: <X>/5 — <commentary>
- D4 Confidence calibration: <X>/5 — <commentary>
- D5 MECE-ness: <X>/5 — <commentary>
- **Total**: <X>/25

**Sample-and-verify** (5 random claims):
1. <claim> — verified / drifted (note)
2. ...

**Failures requiring revision**:
- ...

**Recommended fixes**:
- ...
```

Append to findings-ledger.jsonl:

```json
{"ts":"<ISO>","source":"mc-self-eval-rubric","claim":"Self-eval verdict=<approve/revise>; score=<X>/25; hard gates=<list pass/fail>","confidence":"high","citations":["analyses/<YYYY-WW>/08-qc-report.md"]}
```

## Outputs (return to orchestrator)

```
{
  "verdict": "approve" | "revise",
  "score": <X>/25,
  "hard_gate_failures": [...],
  "dimension_failures": [...],
  "fix_directives": [...]
}
```

## Access tier reminder
- `canon/` is HUMAN-ONLY.
- `analyses/<YYYY-WW>/08-qc-report.md` is AGENT-EDITABLE.
- `predictions-ledger.jsonl`, `findings-ledger.jsonl` are APPEND-ONLY.
