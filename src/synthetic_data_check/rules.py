from __future__ import annotations

from synthetic_data_check.models import Rule

PROJECT_NAME = 'synthetic-data-check'
SUMMARY = 'Audit synthetic data plans for leakage, label balance, and privacy claims.'
SAMPLE_RISK = 'synthetic from production leakage possible balance unknown privacy unchecked'
SAMPLE_CLEAN = (
                   'synthetic generated from schema leakage none balance reviewed privacy ch'
                   'ecked'
               )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='leakage-possible',
        severity='high',
        pattern='leakage\\s+possible',
        message='synthetic data leakage risk',
        recommendation='run nearest-neighbor and privacy checks',
    ),
    Rule(
        code='unknown-balance',
        severity='medium',
        pattern='balance\\s+(unknown|missing|none)',
        message='class balance unclear',
        recommendation='report label distribution',
    ),
    Rule(
        code='privacy-unchecked',
        severity='low',
        pattern='privacy\\s+unchecked',
        message='privacy checks missing',
        recommendation='document privacy validation',
    ),
)
