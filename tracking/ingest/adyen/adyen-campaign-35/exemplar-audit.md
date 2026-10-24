# Adyen C35 coordinator full-read exemplars

**PASS** — 2026-10-25. Three predetermined pinned raws were read independently in full by the coordinator and compared against the final promoted source and both query answers. All reads were untruncated.

| Pinned raw | Full lines | Result |
| --- | ---: | --- |
| raw/adyen/docs/payment-methods/dana/2026-09-15.md | 98 | PASS |
| raw/adyen/docs/payment-methods/momo-wallet/android-component/2026-09-15.md | 726 | PASS |
| raw/adyen/docs/payment-methods/gcash/android-component/2026-09-15.md | 724 | PASS |

DANA retains ID/IDR, shopper login/PIN/confirmation, five-minute default redirect-page timeout, 300-IDR method-display floor, exact recurring/refund versus capture/chargeback matrix, and child navigation scope. Return is distinct from final merchant outcome.

MoMo Android Component read in complete ranges 1–245, 246–490, 491–726. Final source and Q1/Q2 preserve Sessions-only API v68+, distinct Advanced prerequisites and redirect, InstantPaymentComponent and Compose choices, ordinary base request versus conditional recurring request, settled initial payment before token-created webhook, same shopper and stored token with ContAuth/model choices, Java recurringDetailReference versus storedPaymentMethodId discrepancy, test app/scenario credentials versus live Customer Area request. Routine example values remain at locators.

GCash Android Component read in complete ranges 1–245, 246–490, 491–724. Final source and Q1/Q2 preserve Sessions v68+ versus Advanced, redirect/additional action and Customer Area prerequisites, instant component/Compose, ordinary versus recurring fields, shopperReference minimum three characters, settled-payment token lifecycle webhook and later same-shopper stored-token requests. Mixed “test successful GCash live payments”, real registered mobile number, test payment-list checks and live request remain qualified. Snippets and request steps do not prove outcomes.

No material sample failure; no expanded sample triggered. Read-time catalogs and all link routes are checked exhaustively at close. Raw remains immutable. No provider, wallet, credential, account or payment operations.

Coordinator cross-page follow-up: independently read the entire 341-line DANA API-only raw and compared its country table (50–51), example (65–70), minimum (91) and final source. Independently reviewed reciprocal warnings on DANA overview and API-only now preserve the IN/INR versus ID/IDR conflict, without changing raw or asserting current discovery behavior. Original DANA sample retained its own matrix accurately; this follow-up adds the newly discovered cross-page qualification. Passing sample retained. See coordinator-repairs.json.
