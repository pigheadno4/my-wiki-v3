# Adyen C22 coordinator full-read exemplars

**PASS** — three manifest-fixed exemplars, independently compared by the coordinator against their complete pinned raw, promoted entries and both retrieval answers. Long output was reread in bounded ranges to cover omitted portions. Raw remains unchanged. No material final-sample error requiring expansion was found.

## Add and manage funds

- Job: `docs-issuing-add-manage-funds`; all 39 raw lines read.
- Preserved the card-associated balance account's sufficient-funds prerequisite, funding from a verified external transfer instrument, transfers within the same balance platform, and acquired-revenue booking only when acquiring with Adyen. The source and Q1/Q2 distinguish an overview from executed transfers or outcomes.
- Route: index → Adyen index → adyen-issuing → source → exact dated raw. Direct company and reciprocal concept routes checked.

## Transaction components

- Job: `docs-issuing-components-overview-after-payment-transactions-component`; all 893 raw lines read, including repeat reads of lines 85–231 to fill truncated table output.
- Preserved the Adyen for Platforms requirement despite the Issuing URL, platform session product, server/session View and Manage Refunds roles, account-holder policy, HTTPS live origin and TEST example. Source/Q1/Q2 retain CSV's first-100 limit, account-timezone filters, exact-reference searches constrained by other filters, conditional details, refund method/partial-total limits and UI-status versus settlement boundaries. Version/localization settings remain locator-backed.
- Main route uses adyen-platform-components. A missing direct company navigation link was repaired without factual changes and independently approved in the navigation repair records.

## Raise disputes

- Job: `docs-issuing-raise-disputes`; all 162 raw lines read, with lines 85–112 reread to cover a truncated lifecycle passage.
- Preserved captured issued-card scope, platform action on cardholders' behalf, roles/webhook prerequisites, Customer Area pilot, reasons and 35-dispute limit, differing 120-day clocks, irreversible closure, provisional chargeback versus final win, scheme challenge periods, second presentment funds direction, and transaction/dispute/ARN correlation. Source and Q1/Q2 checked.
- Later cross-page reconciliation found conflicting transfer types and dispute status names in the webhook catalog. The reciprocal source/Q2 warning was independently reviewed and applied with before/after evidence in `coordinator-repairs/dispute-events/`; it preserves both snapshot mappings without claiming a live schema.

## Disposition

All three final entries and their two answers preserve central meaning, material qualifications and usable raw locators. Required navigation and reciprocal contradiction repairs are retained separately from worker receipts and backed by independent review. No provider execution, current eligibility, successful payment, settlement or final dispute outcome is inferred.
