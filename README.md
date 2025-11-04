# Data Anonymization Pipeline

## The Real Problem

"We need to share customer data with [vendor/partner/researcher] but our lawyer says we can't share PII."

**Who has this problem:**

- ML teams needing realistic test data (can't use production)
- Companies sharing data with vendors (analytics, ML training)
- Researchers needing datasets for studies
- Compliance teams proving GDPR Article 25 (data minimization)

**Current solutions are bad:**

- Manual redaction (slow, error-prone, doesn't scale)
- "Just delete names/emails" (insufficient - still re-identifiable)
- Vendor tools ($$$, black box, still leaks data)
- Legal says "no" → innovation stops

## Core Purpose

"Transform production data into shareable data that's legally safe and actually useful."

**Success criteria:** Data scientist can still train accurate models, but can't identify individuals.