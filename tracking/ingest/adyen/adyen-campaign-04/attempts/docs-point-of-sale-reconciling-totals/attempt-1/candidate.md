---
title: "Adyen POS terminal totals reconciliation overview"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/reconciling-totals"
raw_files:
  - "adyen/docs/point-of-sale/reconciling-totals/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-totals, reconciliation, operator-shift]
---

## Overview

This Adyen Docs page is a navigation overview for reconciling point-of-sale transaction totals directly from a payment terminal. It routes readers to separate pages for terminal login/logout, retrieving and filtering totals, and comparing terminal totals with the POS app to investigate a balance mismatch. See [[adyen]] and [[adyen-terminal-api]] for provider and in-person terminal context. The snapshot does not supply the detailed procedure, total-field definitions, report schema, or evidence of settlement or money received.

## Key takeaways

- The page directs operators to log in before processing payments and log out when the operator changes or a shift ends. It does not describe credentials, login messages, or the effect of logout on accounting boundaries; those details belong to the linked guide.
- It directs readers to retrieve terminal totals and filter by group or operator, then obtain a reconciliation-period total to compare with the POS app and investigate mismatches. It does not give the request/response format, exact group or period semantics, or a worked mismatch calculation.
- Financial reporting is linked as a separate route. Terminal transaction totals and a terminal-versus-POS app comparison are operational reconciliation inputs; this overview does not show sales-to-settlement matching, payout, bank deposit, or accounting sign-off.
- The requirements table says the linked next-step pages are relevant for Adyen point-of-sale payments; it does not narrow this overview to a specific terminal model, merchant account, Terminal API version, or deployment architecture.

## Detail locators

- Purpose and three linked tasks: `# Reconciling totals`, raw lines 15–27.
- POS scope statement: `## Requirements`, raw lines 29–35.
- Login/logout, terminal-total retrieval, and mismatch-guide navigation: `## Next steps`, raw lines 37–49.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person terminal operations and separate versioned implementation evidence.

## Related raw API references

- The raw page links to terminal login/logout, retrieval of terminal totals, reconciliation of terminal/POS balance mismatches, and financial reporting. Those destinations are navigation until independently read; see raw lines 23–27 and 37–49.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/reconciling-totals/2026-09-15|Adyen Docs: Reconciling totals (2026-09-15 snapshot)]]
