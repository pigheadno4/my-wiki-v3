# PayBright Web Drop-in retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the captured PayBright Drop-in guide describe, and can a new integration use it?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paybright-web-drop-in]] → [[raw/adyen/docs/payment-methods/paybright/web-drop-in/2026-09-15]]. It describes Sessions/Advanced additions for an existing Web Drop-in integration (raw lines 15–44), but expressly says Adyen accepts no new PayBright integrations (raw line 19). The later live Customer Area request sentence (raw line 1434) is historical procedure, not evidence of current availability. [[source-adyen-docs-payment-methods-paybright]] carries the CA/CAD product scope.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which data and lifecycle conditions matter for the described existing Drop-in route?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paybright-web-drop-in]] → [[raw/adyen/docs/payment-methods/paybright/web-drop-in/2026-09-15]]. Sessions is the stated Drop-in v5+ default; both `/sessions` and `/payments` tables require shopper identity/contact/country/billing fields, with delivery address optional and lineItems marked optional/recommended despite the opening instruction (raw lines 23–26, 50–65, 794–809). Advanced Java/PHP examples use USD with CA, unlike the CA/CAD overview and other examples (raw lines 880–967). The Advanced Java Discount line uses positive `amountExcludingTax` and `amountIncludingTax` values, unlike negative discounts in the other samples, so it is not a validated amount/line-item recipe (raw lines 953–959). Capture is automatic by default; partial capture needs delayed/manual capture, and an unclaimed remainder is cancelled unless multiple partial captures are enabled through Support (raw lines 1321–1380). Cancel before capture, refund afterward; the partial-refund prose and legacy example name different endpoint shapes (raw lines 1382–1426).
