# Clearpay iOS Drop-in retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-clearpay-ios-drop-in`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-clearpay-ios-drop-in.md` → `raw/adyen/docs/payment-methods/clearpay/ios-drop-in/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does this Clearpay iOS Drop-in page add, and do its GB/GBP TEST examples or live request establish enablement?

**Expected:** It adds method-specific instructions to existing iOS Drop-in Sessions or Advanced flows. The linked overview scopes Clearpay to GB/GBP and distinguishes regional Afterpay; the TEST examples do not prove account eligibility or payment success. Sessions requires Checkout API v68+ and Customer Area setup. Advanced requires an existing Advanced Drop-in flow, redirect handling and Customer Area setup. Live acceptance requires submitting a Clearpay request in live Customer Area, which does not prove approval. Evidence: raw `# Clearpay iOS Drop-in` lines 15–34, `## Advanced flow Drop-in` lines 213–223, TEST examples lines 53–75/248–273 and live lines 211/419.

## Q2 — Required fields, capture/refund and example warnings

**Query:** Which fields and redirect result matter, and what are the capture and modification conditions?

**Expected:** Both request tables mark shopper name/email/reference (minimum three characters), country, billing/delivery addresses and line items required; telephone optional. Advanced example uses `paymentMethod.type: clearpay`. The Advanced `RedirectShopper` action is a redirect, not final success. No method-specific Drop-in configuration is needed. Capture is automatic or manual by account settings; partial capture requires manual capture. Capture within 13 days; first installment charged at authorisation and refunded on cancellation for noncapture; TEST authorisations expire after one day. Initial partial capture cancels balance unless multiple partial captures are enabled through Support, with new invoice per capture. Uncaptured can cancel; captured needs refund; full/partial refund specifies amount.value and optional lineItems. Both curl examples lack continuation between `-X POST` and `-d`, and the discount prose calls it GBP 1 while the example has quantity 2 at -100 minor units each, taking GBP 10 (1000) to GBP 8 (800), a GBP 2 discount; the discount JSON also lacks a comma. Evidence: raw tables lines 42–51/237–246, redirect lines 312–326, config lines 114–118/225–229, capture/refund lines 120–154/328–362, examples lines 55–61/250–256, discounts lines 156–192/364–400.
