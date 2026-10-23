# Adyen C31 coordinator full-read exemplars

**PASS** — 2026-10-24. Three fixed manifest-selected pages, including the longest. The coordinator read all raw content independently in bounded, untruncated chunks, then compared final promoted source entries and both retrieval answers. Read-time provider catalog gaps are checked exhaustively at campaign close.

| Pinned raw | Full line count | Result |
| --- | ---: | --- |
| `raw/adyen/docs/payment-methods/cards/2026-09-15.md` | 95 | PASS |
| `raw/adyen/docs/payment-methods/cards/custom-card-integration/2026-09-15.md` | 2773 | PASS |
| `raw/adyen/docs/payment-methods/apple-pay/apple-pay-certificate/web/2026-09-15.md` | 206 | PASS |

Cards root retains most rather than all methods, raw-card full-PCI gate, conditional LIVE documentation, default capture versus alternatives, dated regional guidance and navigation-only channel routes. It proves no actual authorization, capture or settlement.

The full custom-card raw was read at lines 1–600, 601–1300, 1301–2000 and 2001–2773. Its final entry and answers retain Web hosted iframes versus native app collection/encryption, setup/client/server boundaries, versioned illustrative snippets and Go import conflict, resultCode/webhook/manual-capture boundaries, regional/co-badged/split funding scope, consent/token lifecycle, Ecommerce creation versus ContAuth reuse examples, and JWE/origin conditions. Its broad SAQ A closing sentence is qualified against the separately retained PCI guide. A narrow independently reviewed coordinator repair adds explicit reciprocal Contradiction callouts in both source pages, preserving SAQ A eligibility and leaving the custom mobile encryption examples unclassified. Proposals, prior review, revised approvals, before/after and diffs are retained under coordinator-repairs/.

The Web certificate entry and answers retain roles and integration prerequisites, separate TEST/LIVE identifiers, processing versus identity certificates and distinct CSRs, upload ownership, approximately four-hour renewal overlap, old-key non-failure, authorized-payment new-key check, and both Salesforce Commerce Cloud exceptions. Commands remain illustrative; setup proves no deployed certificate, current eligibility or payment outcome.

All three final source/Q1/Q2 comparisons pass. No material final sample failure required expanded sampling. Raw is unchanged; no provider, key, certificate, token or payment operation was performed.
