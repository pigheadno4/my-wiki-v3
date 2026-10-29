# Alma overview retrieval checks

## Q1 — Purpose, scope and what not to infer

**Canonical source stem:** `source-adyen-docs-payment-methods-alma`
**Full pinned raw:** `raw/adyen/docs/payment-methods/alma/2026-09-15.md`
**Verified locators:** `# Alma`, lines 15–25; capability matrix lines 27–29; `## How do you want to integrate?`, lines 31–73.
**Route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-alma.md` → pinned raw.
**Answer boundary:** This is a captured Alma method overview. It describes France/EUR redirect BNPL and three or four installments, with conditional risk and payout wording. It does not prove current merchant eligibility, an approved shopper, a completed payment or a precise settlement timeline.

## Q2 — Central capability, prerequisites and warnings

**Verified locators:** shopper installments, risk checks and conditional fraud-risk/upfront-payment statement line 23; widget line 25; capability matrix lines 27–29; platform and API-only routes lines 31–73.
**Answer boundary:** The matrix marks recurring and multiple partial captures unsupported, while refunds, partial/multiple partial refunds and partial capture have checkmarks. Its separate-capture checkmark and chargeback `x` each carry an unexplained `See note` in this capture, so preserve that qualification. The widget is a product-page display option; Web, mobile, API-only and Pay by Link links are implementation routes, not live enablement proof.
