# Adyen C37 coordinator full-read exemplars

**PASS** — 2026-10-25. Three predetermined pinned raws independently read fully by coordinator, then compared with final promoted source and Q1/Q2. All reads untruncated.

| Pinned raw | Lines | Result |
| --- | ---: | --- |
| raw/adyen/docs/payment-methods/rakutenpay/2026-09-15.md | 80 | PASS |
| raw/adyen/docs/payment-methods/bank-transfer-kcp/api-only/2026-09-15.md | 684 | PASS |
| raw/adyen/docs/payment-methods/napas-card/web-component/2026-09-15.md | 97 | PASS |

Rakuten Pay overview retains desktop/mobile website redirect/return, Ecommerce and undefined IPP wording, JP/JPY wallet matrix, positive capability marks with missing See note qualifications and negative multiple partial captures, plus navigation-only child references. Missing note is unresolved rather than invented. Return doesn't establish payment outcome.

KCP Bank Transfer API-only read completely in 1–230, 231–460 and 461–684. Source/Q1Q2 preserve existing API-only and redirect handling, method added in Customer Area, no additional method-specific form fields, KR/KRW discovery with kcp_banktransfer, sample v72 versus unstated API minimum, ordinary request parameters and RedirectShopper/additional redirect action, item-information prose versus no-additional-parameter/sample conflict, no testing credentials because Public Identification Certificate authorization. TEST code is no successful test, live readiness or financial execution proof. Routine full examples remain raw-located.

Napas Card Web Component fully read 1–97. Source/Q1Q2 preserve existing Web Sessions/Advanced and Customer Area requirements, no extra Napas fields, Components v5.0.0 default Sessions rather than API minimum, v6 Redirect vs v5 create snippets, Napas title with momo_atm identifier unresolved, test scenario fixtures and separate live request. Card/OTP values remain only in raw; no live/card/security action performed. Import/base configuration and final return/webhook sequence aren't invented from snippet.

All three final comparisons pass without material sample failure; no expanded sample triggered. Read-time catalog gaps and all links are checked exhaustively at close. Raw immutable, historical snapshot scope preserved.
