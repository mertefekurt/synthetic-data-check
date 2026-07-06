<p align="center">
  <img src="assets/readme-cover.svg" alt="Synthetic Data Check cover" width="100%" />
</p>

# Synthetic Data Check

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Audit synthetic data plans for leakage, label balance, and privacy claims.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `synthetic-data-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
synthetic-data-check examples/sample.txt
synthetic-data-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `leakage-possible` | high | synthetic data leakage risk |
| `unknown-balance` | medium | class balance unclear |
| `privacy-unchecked` | low | privacy checks missing |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
synthetic from production leakage possible balance unknown privacy unchecked
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m synthetic_data_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Synthetic Data Check policy easy to review.
