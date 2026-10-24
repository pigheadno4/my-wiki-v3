# Adyen C36 coordinator full-read exemplars

**PASS** — 2026-10-25. Three predetermined raws independently read in full by coordinator, compared against final promoted source and Q1/Q2. No output truncations.

| Pinned raw | Lines | Result |
| --- | ---: | --- |
| raw/adyen/docs/payment-methods/grabpay/2026-09-15.md | 76 | PASS |
| raw/adyen/docs/payment-methods/grabpay/api-only/2026-09-15.md | 992 | PASS |
| raw/adyen/docs/payment-methods/paynow/web-component/2026-09-15.md | 151 | PASS |

GrabPay overview retains shopper redirect/phone/OTP/selection, Wallet vs PayLater timing and country exclusions, Wallets-scoped capabilities, exact refund reference limits, and navigation-only integration links. Historical user numbers omitted rather than presented as current measurement. Final source and Q1/Q2 preserve material scope.

GrabPay API-only full ranges 1–250, 251–500, 501–750 and 751–992: final source and Q1/Q2 retain Web Sessions/Advanced prerequisites vs detailed payments/details sequence, MY/MYR SG/SGD PH/PHP mapping, PH PayLater exclusion, Wallet and PayLater reference distinction, PayLater deliveryAddress/lineItems/nonzero tax-inclusive amount, redirect vs authorization, mobile browser/security recommendations, URL-decoded redirectResult, response methodVariant vs initial type, Pending/Received webhook finality and no-return behavior, AUTHORISATION and OFFER_CLOSED events, Support test credentials/simulator vs live request, and mixed v68/v72 sample qualification. Routine code/version/value detail remains at verified locators; examples do not establish execution.

PayNow Web Component fully read 1–151: final source and Q1/Q2 retain Sessions v68+ plus required countdownTime in minutes; 5 is example, no universal expiry. Advanced qrCode action and no extra payment fields remain separate; Sessions configuration applicability isn't inferred for Advanced. Support live gate and live penny-test wording stay distinct from explicit warning that TEST bank transfers debit funds and cannot be reversed. No actual payment operations.

All three final comparisons pass; no material sample failure and no expansion triggered. Read-time catalog routes checked exhaustively at campaign close. Immutable raw and source-snapshot authority preserved.
