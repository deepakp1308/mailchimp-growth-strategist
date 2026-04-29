# Mailchimp Growth Strategist Agent

A Cursor-native, multi-agent **"Mailchimp Strategy & Growth Analyst"** that ingests FY26 strategy, launches, experiment results, BigQuery metrics, and Slack signal — then runs McKinsey-style strategic analysis on a recurring basis to:

1. **Reconcile plan vs. execution** — what we said we'd do vs. what we shipped
2. **Identify what worked / what didn't** — experiment portfolio synthesis
3. **Recommend the highest-leverage moves** to add **$50M incremental revenue**

## Quick start

```bash
# Trigger a full weekly run
cursor agent "run mailchimp-growth-strategist for this week"

# Ask a specific question
cursor agent "what should I work on this week to move active churn?"
cursor agent "did the Annual Plan experiment beat target?"
cursor agent "grade my open predictions from last week"
```

## Architecture

**Orchestrator + 7 specialist subagents + 4 QC subagents** following Anthropic's 2026 multi-agent guidance (orchestrator-worker primary, adversarial dual-analysis for QC, parallel fan-out for independent diagnostics).

```
mailchimp-growth-strategist (orchestrator)
├── ingestion (parallel fan-out)
│   ├── mc-slack-harvester
│   ├── mc-bigquery-runner
│   ├── mc-doc-parser
│   └── mc-external-researcher
├── diagnostic (parallel fan-out)
│   ├── mc-strategy-execution-reconciler
│   ├── mc-experiment-synthesizer
│   ├── mc-cohort-churn-diagnostician
│   ├── mc-gtm-lever-analyst
│   └── mc-competitive-intel-analyst
├── synthesis (sequential)
│   ├── mc-growth-tree-50m
│   └── mc-recommendation-ranker
└── qc (adversarial dual-analysis)
    ├── mc-self-eval-rubric
    ├── mc-adversarial-reviewer
    ├── mc-numeric-round-tripper
    └── mc-prediction-grader
```

## Repository layout

| Tier | Files | Who edits |
|---|---|---|
| **Human-only** | `program.md`, `canon/*`, `queries/*.sql` | Deepak only — agent reads but never writes |
| **Append-only** | `findings-ledger.jsonl`, `predictions-ledger.jsonl`, `knowledge/**` | Agent appends — never overwrites or deletes |
| **Agent-editable** | `analyses/YYYY-WW/*`, `dashboards/*`, `contradictions.md` | Agent regenerates freely |

Access tier separation enforced by `.git-hooks/pre-commit` (per G13).

## The falsifiable-prediction loop (borrowed from `karpathy/autoresearch`)

Every recommendation must include `{predicted_metric, predicted_delta, predicted_window_days}` written to `predictions-ledger.jsonl`. The next weekly run **grades open predictions before generating new ones**. Hit rate is reported in every executive brief; subagents with rolling hit rate <40% get auto-downgraded confidence.

## Outputs & cadence

- **On-demand**: Q&A inside Cursor chat
- **Weekly (Mon 7am PT)**: Executive brief (Slack DM + GH Pages dashboard + `analyses/YYYY-WW/`)
- **Monthly**: Strategy-vs-execution scorecard, Three-Horizons rebalance
- **Quarterly**: $50M Growth Tree re-baseline + FY26 narrative reality-check

## See also

- `program.md` — current research agenda (the single human-edited control surface)
- `canon/fy26-strategy.md` — the FY26 narrative distilled
- `canon/metrics-canon.md` — canonical metric definitions mapped to BigQuery
- `.cursor/skills/` — all 12 skill specifications
