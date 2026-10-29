# C44 PayBright Web Component retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-paybright-web-component`

Full pinned raw path: `raw/adyen/docs/payment-methods/paybright/web-component/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-paybright-web-component]]` → `[[raw/adyen/docs/payment-methods/paybright/web-component/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** Can a merchant newly integrate PayBright through this Web Component guide?

**Answer path:** No new-integration support is claimed: the pinned raw explicitly says PayBright was acquired by Affirm and Adyen will not accept new PayBright integrations (line 19). The guide covers adding PayBright to existing Web Components (line 21) and later provides Customer Area/live-request instructions at lines 28–44 and 1456–1462; those do not override the opening restriction or prove an exception. The source entry preserves this distinction and does not claim live merchant eligibility or a completed payment.

## Q2 — central capability, prerequisites and warnings

**Query:** What fields, Component version and capture/refund conditions matter for an existing PayBright Web Components integration?

**Answer path:** Raw `## Requirements` lines 28–44 gives Sessions/Advanced prerequisites. `## API reference` field tables at lines 54–65 and 797–809 mark shopper name, birth date, email, phone, country, billing address and reference required; `lineItems` is table-optional/recommended despite the introductory instruction at line 26. Several Sessions library request snippets omit required `dateOfBirth` (Java 191–204, PHP 280–296, C# 380–395), so they are incomplete for these fields. `## Component configuration` lines 1317–1347 distinguishes v6 `Redirect` from v5 `checkout.create`. `## Capture the payment` lines 1349–1408 gives automatic-capture default, first installment, manual/delayed partial-capture route, unclaimed cancellation and Support-gated multiple partial captures; the JSON sample has a trailing comma at line 1400 before the `additionalData` object closes at 1401. `## Refunds` lines 1410–1454 distinguishes cancel before capture and refund after capture. Its labeled Checkout `/payments/{paymentPspReference}/refunds` route uses legacy-shaped `originalReference`/`modificationAmount` in the PayBright sample; the general [[source-adyen-docs-online-payments-refund]] guide, raw lines 56–67, calls for the PSP reference in the path and `amount`. Verify the endpoint-specific schema before adapting this historical sample; no runtime success or failure is established. CA/CAD and TEST snippets are examples; Advanced Java/PHP USD and positive-discount examples should not be treated as authoritative currency or arithmetic rules.
