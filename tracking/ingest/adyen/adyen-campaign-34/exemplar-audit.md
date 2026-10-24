# Adyen C34 coordinator full-read exemplars

**PASS** — 2026-10-24. Three predetermined samples were independently read in full by the coordinator, then compared with final promoted source entries and both retrieval answers. Long table truncations were repaired with bounded reads before comparison. Read-time catalog gaps are closed exhaustively at campaign close.

| Pinned raw | Full lines | Result |
| --- | ---: | --- |
| `raw/adyen/docs/payment-methods/wechat-pay/2026-09-15.md` | 71 | PASS |
| `raw/adyen/docs/payment-methods/upi/upi-autopay/api-only/2026-09-15.md` | 509 | PASS |
| `raw/adyen/docs/payment-methods/kakaopay/android-component/2026-09-15.md` | 728 | PASS |

WeChat overview retains mobile-web initiation from WeChat versus broad desktop-QR/H5 navigation, separate native and Mini Program routes, capability marks, broad country/currency labels versus actual eligibility, and the minority outcomes requiring webhook confirmation. Historical usage numbers are not current measurements. Final source and Q1/Q2 pass.

UPI AutoPay raw was read at 1–270 and 271–509, with truncated table content recovered at 49–61 and 355–412. Final source and Q1/Q2 retain shopper-approved mandate registration, initial versus later charge, conditional Intent app ID/mobile and Android/iOS return handling, QR/Collect differences, Pending/Received versus final AUTHORISATION, 24-hour pre-debit and IST windows, amount-rule inconsistency, merchant alphanumeric versus spaces conflict, malformed examples, recurring retry and notification reset, merchant delete versus shopper cancellation and disabled webhook, and TEST setup/LIVE onboarding. Detailed fields and scenario amounts remain at raw locators. No operation was executed.

KakaoPay Android Component raw was read fully in untruncated 1–360 and 361–728 ranges. Final source and answers retain Sessions-only v68+ minimum, distinct Advanced prerequisites, redirect/instant/Compose configuration, base no-extra-field claim versus recurring requirements, request fields triggering shopper confirmation, settled-payment recurring.token.created before reusable token availability, same shopper reference and ContAuth model choices, varying example amount/returnUrl, and mixed TEST/LIVE wording. Requests, shopper confirmation and test examples do not prove payment or token outcome.

All three final comparisons pass without material sample failure; no expanded sample was triggered. Sources remain historical snapshot evidence. Raw was unchanged and no account, app, wallet, mandate, key or payment action was performed.

Coordinator cross-page follow-up: fully read the 53-line desktop QR/H5 overview as well. Independently reviewed reciprocal Contradiction callouts were applied to the overview and desktop QR/H5 source, preserving last-modified dates 2023-03-09 and 2019-07-04, app-initiated versus mobile-browser-start wording, and unresolved current availability. The original overview sample already retained the qualification; the clarification preserves that passing result. Evidence: coordinator-repairs.json and coordinator-repairs/.
