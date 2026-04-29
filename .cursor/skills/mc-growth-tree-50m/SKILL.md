---
name: mc-growth-tree-50m
description: Decompose $50M incremental revenue target into a metric tree (Paid Users x ARPU x (1 - Churn) x (1 + Expansion)). Calculate delta needed per lever, historical base rates, and sensitivity. Output Pareto-ranked levers by realistic_delta x probability x time_to_impact. Writes to analyses/YYYY-WW/06-growth-tree.md.
---

# Growth Tree Decomposer ($50M) (subagent)

You are a synthesis subagent. **Your job is to decompose the $50M incremental target into testable levers and rank them by realistic-delta × probability × time-to-impact.**

This is the centerpiece analysis. It's the equivalent of a McKinsey "growth cube" or Lean Analytics "metric tree."

## Inputs

- `knowledge/bigquery/_growth_tree_summary.json` — pre-computed summary stats (from `60-growth-tree-inputs.sql`)
- `knowledge/bigquery/<various>__latest.json` — for component metrics
- All diagnostic outputs: `analyses/<YYYY-WW>/01-05-*.md`
- `canon/fy26-strategy.md` — for strategy fit
- `canon/metrics-canon.md` — for metric definitions
- `findings-ledger.jsonl` — historical context

## Steps

### 1. Establish the tree

```
Annualized Revenue
  = Avg Paid Users
    × ARPU (annualized)
    × (1 - annual churn rate)
    × (1 + net expansion rate)
```

From `_growth_tree_summary.json`, extract:

- `avg_total_paid_users` (current run-rate)
- `arpu_per_paid_user` (weekly) → × 52 for annualized
- `weekly_active_churn_rate`, `weekly_passive_churn_rate` → annualized churn
- Net expansion: derived from SMS purchase + tier upgrades (proxy)

Compute current annualized revenue: `paid_users × annual_arpu` (this is a steady-state estimate).

### 2. The $50M ask — what does it require?

`$50M = current_annual_revenue × X%`

What % growth does $50M represent vs. current run-rate? (If current is ~$1B, $50M = 5%; if $500M, $50M = 10%.)

### 3. Decompose levers

For EACH input metric, compute the delta required to add $50M assuming all other levers held constant. This is the "1-at-a-time sensitivity."

| Lever | Current | Delta needed alone | % change | Realistic? |
|---|---|---|---|---|
| **Paid Users** | N | +X users | +X% | ... |
| **ARPU** | $Y | +$Z | +Z% | ... |
| **Active churn rate** | A% weekly | -B% weekly | (e.g., halve current) | ... |
| **Passive churn rate** | C% weekly | -D% weekly | ... | ... |
| **Net expansion (SMS)** | E% | +F% | ... | ... |
| **Activation rate** (free → paid) | G% | +H% | ... | ... |
| **AP take rate** (post-Apr 23 launch) | TBD | >10% target | ... | ... |
| **Free Trial → Paid conversion** | I% | +J% | ... | ... |

For each lever, use historical signals from your inputs:

- **AP take rate**: target >10% (per Annual Plans launch post). At 10% take rate with 20% AP discount and historical 67% 90d retention, FY27 incremental MRR = $1.3M-$3.9M (per Annual Plans launch announcement).
- **SMS expansion**: 6 stacked wins → $1.08M FY26 / $3.96M FY27 cumulative (per Connor Callahan).
- **Active churn -1pt**: requires what mechanism? (FY26 levers: MM billing flex, Annual Plans for retention lock-in, churn-prediction analytics.)
- **Activation rate +1pt**: most recent data point — OTP at activation: +3.74% activation rate (per Margarita Caraballo Apr 27).

### 4. Rank levers — Pareto

For each lever, score:

- `realistic_delta` ($, capped by historical proof): e.g., AP take rate realistic delta = $3.9M (the ceiling claimed)
- `probability_of_success` (0-1): based on (a) experiment evidence, (b) FY26 priority backing, (c) competitive position
- `time_to_impact` (months): when will most of the impact land?
- **Score** = `realistic_delta × probability × (12 / time_to_impact)`

Sort descending. The top 5 are the highest-leverage levers.

### 5. Combine top levers — additive scenario

Build a scenario: "If we hit P50 on top 5 levers, what's total incremental?" Compute:

- Sum of `realistic_delta × probability` for top 5
- Compare to $50M target
- If sum ≥ $50M: target is feasible with stack of known bets.
- If sum < $50M: gap; we need new (un-explored) levers.

### 6. Identify NEW levers (not yet in motion)

If $50M is bigger than current bets can deliver, surface candidate NEW levers:

- **Pricing optimization** — list-price changes (not just AP discount)
- **MM Premium tier** — a new MM-specific tier above Premium with multi-entity billing (FY26 P1 area)
- **International SMS short-codes** — adoption of standalone SMS plans in UK/EU (per FY26 narrative)
- **Cross-Intuit referral program** — QBO → MC bundling (FY27+ exploration)
- **Loyalty/rewards revenue** — exploration priority for Ecomm
- **Content gen API monetization** — agentic AI as separate paid tier
- **Vertical-specialized templates** — verticalized content as upsell (per FY26 P1 in MM Subscription)

For each, score: addressable market × adoption probability × impact.

### 7. Output

Write `analyses/<YYYY-WW>/06-growth-tree.md`:

```markdown
# Growth Tree → $50M Incremental — <YYYY-WW>

## Current trajectory (steady state)

- Avg Paid Users: <N> (trailing-13w)
- Annualized ARPU: $<Y>
- Annualized Active Churn rate: <X>%
- Annualized Passive Churn rate: <Y>%
- Net expansion (SMS proxy): <Z>%
- **Implied annual revenue run-rate**: $<R>

## $50M target context

- $50M = <X>% of current run-rate
- Equivalent to closing <X>% of annualized churn
- OR adding <Y> net new paid users
- OR moving ARPU from $<a> to $<b>

## Single-lever sensitivity (1-at-a-time)

(Table)

## Pareto-ranked levers (top 5)

### #1 — <lever name>
- Realistic delta: $<X>
- Probability: <Y>
- Time to impact: <Z> months
- Score: <number>
- Mechanism: <why it works>
- Backing experiment(s): <list>
- FY26 priority match: <list>

### #2 — ...

## Stack scenario (top 5 combined)

- P50 sum: $<X>
- Vs $50M target: <gap or buffer>

## Candidate NEW levers (not in motion)

- ...

## Gaps / Open questions

- ...

## Headline recommendation hint (NOT a recommendation — for ranker)

The single highest-leverage move appears to be: <lever name>. Justification: ...
```

### 8. Append to findings-ledger.jsonl

```json
{"ts":"<ISO>","source":"mc-growth-tree-50m","claim":"Top lever: <name> with $X realistic delta; top 5 stack = $Y vs $50M target; gap/buffer = $Z","confidence":"medium","citations":["analyses/<YYYY-WW>/06-growth-tree.md"]}
```

## Outputs (return to orchestrator)

```
{
  "current_run_rate_annualized": $...,
  "top_5_levers": [...],
  "stack_p50": $...,
  "gap_to_50M": $...,
  "candidate_new_levers": [...],
  "file_written": "..."
}
```

## Access tier reminder
- `canon/`, `queries/` are HUMAN-ONLY.
- `analyses/<YYYY-WW>/` is AGENT-EDITABLE.

## Quality bar

- **Honesty about base rates.** Historical 6mo new-user churn = 43% (per FY26 narrative). A "lift to 5% reduction" is realistic; "halve to 21%" is not.
- **Explicit P50 vs P90.** Don't conflate "ceiling" with "expected value".
- **Compounding caveats.** When stacking levers, account for overlap (e.g., AP retention + churn reduction overlap on existing Paid).
- **Cite experiments.** Every realistic_delta should cite the experiment(s) that underpin it.

## Related strategic frameworks

- Lean Analytics (Yoskovitz/Croll) — One Metric That Matters → metric tree
- McKinsey Three Horizons — H1 levers vs H2 explorations vs H3 vision
- Hamilton Helmer 7 Powers — defensibility of each lever's mechanism
