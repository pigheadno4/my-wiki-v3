# C44 worker query check: Klarna Android Drop-in earlier versions

## Q1 — purpose, scope, non-inference

**Query:** What does this earlier-version guide cover?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-android-drop-in-earlier-versions]] routes to a 2026-09-15 snapshot for Klarna Android Drop-in v4.x.x with an Advanced-flow requirement. A country/product table is a discovery aid, not proof of merchant enablement or payment success. Pinned full source: `raw/adyen/docs/payment-methods/klarna/android-drop-in/earlier-versions/2026-09-15.md`. Verified raw locators: identity 15–23, requirements 25–30, matrix 32–62.

## Q2 — capability, prerequisites, warnings

**Query:** What happens after Drop-in shows Klarna, and how is the outcome known?

**Answer:** Drop-in passes `paymentComponentData.paymentMethod` for the merchant server's /payments request with shopper data and matching line items; an action redirects the shopper; on return the server posts `actionComponentData.details` to /payments/details. Authorised still needs capture under the immediate/24-hour shipping condition or manual within 90 days. A received capture response awaits CAPTURE webhook. Later legacy /capture examples differ from the main Checkout /captures request. The introduction and See also point to Sessions though the Requirements table says Advanced. For recurring eligibility, the [[source-adyen-docs-payment-methods-klarna|Klarna overview]] directs merchants to contact Adyen Support before offering recurring; Pay over time is limited to long-term subscriptions and excludes monthly subscriptions and one-off/on-demand tokenized purchases, subject to the overview's product/country matrix (overview raw lines 31–38). Verified raw locators: payment 63–126, action/return 848–913, capture 915–931 and 1377–1410, legacy examples 1412–1490, See also 1637.
