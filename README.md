# Synthetic Data Check

Audit synthetic data plans for leakage, label balance, and privacy claims.

## First impression

![Synthetic Data Check cover](assets/readme-cover.svg)

When this tool reports something, I want the finding to be boringly explicit: what matched, how severe it is, and what a reviewer should clean up.

## Tripwires

- `leakage-possible` (high): synthetic data leakage risk. Fix: run nearest-neighbor and privacy checks.
- `unknown-balance` (medium): class balance unclear. Fix: report label distribution.
- `privacy-unchecked` (low): privacy checks missing. Fix: document privacy validation.

## Runbook

```bash
git clone https://github.com/mertefekurt/synthetic-data-check.git
cd synthetic-data-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Then:

```bash
synthetic-data-check examples/sample.txt
synthetic-data-check examples/sample.txt --json
```

## Development note

The policy lives in `rules.py`; parsing and rendering stay separate so the rule list is easy to audit.
