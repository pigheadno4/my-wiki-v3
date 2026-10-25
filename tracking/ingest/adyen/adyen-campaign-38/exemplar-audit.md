# Adyen C38 coordinator full-read exemplars

**PASS** — 2026-10-25. Three predetermined pinned raws independently read in full by coordinator and compared with final promoted source and Q1/Q2. All reads untruncated.

| Pinned raw | Lines | Result |
| --- | ---: | --- |
| raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/2026-09-15.md | 80 | PASS |
| raw/adyen/docs/payment-methods/online-banking-thailand/api-only/2026-09-15.md | 803 | PASS |
| raw/adyen/docs/payment-methods/payme/web-component/2026-09-15.md | 270 | PASS |

FPX overview retains PayNet through RMS/formerMOLPay, MY/MYR bank redirect, asynchronous webhook finality, exact refund versus recurring/separate-partial-capture/chargeback capability marks, and navigation-only routes. General capture link does not supersede method matrix.

Thailand API-only read fully in ranges 1–210, 211–420, 421–630, 631–803. Source/Q1Q2 retain existing API-only/redirect/Customer Area setup, shopper bank selection/issuer server handoff, TH/THB discovery and issuer list, required type versus blank required cells/conditional issuer-redirect returnUrl and QR mention without full QR procedure, sample PHP TH vs molpay_ebanking_TH conflict, no-extra-parameters versus issuer/item prose conflicts, redirectResult URL decode/details, Pending/Received minutes/hours and final AUTHORISATION webhook, no-return handling, TEST Component wording versus API-only title and live request gate. Routine examples stay raw-located; no runtime outcome inferred.

PayMe Web Component read fully 1–140 and 141–270. Final source/Q1Q2 retain desktop QR/mobile app flows and requirement to implement both, support floor 5.56.0 versus generic v5 Sessions default, v6 import/constructor and v5 create, import link's Drop-in mismatch, blank Required cells, SKU-only Checkout v70 condition, mobile Web vs Web/iOS/Android channel conflict, base-guide outcome route, sandbox no-app and amount-ending outcome fixtures with default ten-minute expiry. These are no production outcomes or live-enablement procedure.

All three final comparisons pass; no material sample failure, no expansion triggered. Read-time catalog gaps closed exhaustively at campaign close. Raw immutable; no provider, account, wallet, bank or financial operations performed.
