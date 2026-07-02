# synthetic-data-check

> Audit synthetic data plans for leakage, label balance, and privacy claims.

## Workflow Overview

Audit synthetic data plans for leakage, label balance, and privacy claims. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 18

Accepts synthetic data plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 18

```bash
python -m pip install -e ".[dev]"
synthetic-data-check examples/sample.txt
synthetic-data-check examples/sample.txt --json --fail-on medium
python -m synthetic_data_check --help
```

## Rule Surface 18

| Rule | Severity | Meaning |
|---|---:|---|
| `leakage-possible` | high | synthetic data leakage risk |
| `unknown-balance` | medium | class balance unclear |
| `privacy-unchecked` | low | privacy checks missing |

## Validation Notes 18

```bash
ruff check .
pytest
python -m synthetic_data_check --help
```

Example risky input:

```text
synthetic from production leakage possible balance unknown privacy unchecked
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
