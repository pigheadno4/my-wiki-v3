# Oney API-only retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-oney-api-only`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oney-api-only.md` → `raw/adyen/docs/payment-methods/oney/api-only/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does this Oney API-only page cover, for which installment/country combinations, and what does its live instruction prove?

**Expected:** It adds Oney to an existing API-only checkout with merchant-built form, server payment request, redirect and details result. Discovery and method tables list FR/ES/IT in EUR: 3x/4x all three, 6x ES, 10x/12x FR/ES. Oney's overview adds European-entity/risk scope. The page's generic QZ country-code note does not expand Oney eligibility. It instructs merchants to request “Oney 3x4x” in live Customer Area, a narrower label than the listed types; neither test setup nor request proves enablement. Evidence: raw `# Oney for API only` lines 15–32, `## Build your payment form for Oney` lines 47–61, `## Make a payment` lines 69–75 and 101–102, `### Go live` lines 1050–1052.

## Q2 — Required conditions and outcome/lifecycle warnings

**Query:** Which form/request and risk conditions matter, when is the result final, and what are the capture/refund limits?

**Expected:** Form requires name/email/phone/billing/delivery; birth date is optional. Request must include a matching line-item total; shopper name max 32, shopper reference min 3, five-character address postcodes and protocol-bearing return URL max 1024 are specified. The optional trust flag needs Oney account enablement and merchantPays overrides configured fee payer. The FR TEST example's +33 1 phone conflicts with FR mobile-prefix prose; Go date parser conflicts with date-only prose. RedirectShopper is not success; after return, POST URL-decoded redirectResult to /payments/details. FR Pending/Received awaits AUTHORISATION webhook and auto-cancels if unauthorised after 24 hours; ES result is immediate per page. Ship only after successful capture. Capture after more than six days needs reauthorisation. Uncaptured can cancel; captured refunds have EUR 1 minimum and 13-month limit; partial refund uses amount on /payments/{paymentPspReference}/refunds. Evidence: raw `## Build your payment form for Oney` lines 34–45; `## Make a payment` lines 77–135, 138–203 and 627–630; `## Handle the redirect` lines 896–937; `## Present the payment result` lines 939–950; `## Capture the payment` lines 952–958; `## Refund the payment` lines 960–972.
