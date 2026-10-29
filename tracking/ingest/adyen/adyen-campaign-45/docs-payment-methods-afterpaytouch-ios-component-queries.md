# Afterpay iOS Component retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-ios-component`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-ios-component.md` → `raw/adyen/docs/payment-methods/afterpaytouch/ios-component/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does this iOS Component page add, and does its AUD/AU example or US sandbox option prove live product availability?

**Expected:** It supplies method-specific additions to an existing iOS Components integration, separated by Sessions and Advanced flows. Sessions requires Checkout API v68+, redirect handling and Customer Area setup; Advanced requires its own base flow, redirect handling and setup. AUD/AU is a TEST example, and the US choice is for a sandbox shopper account. Neither establishes a merchant's live eligibility; the linked overview's table gives AU/CA/NZ. Evidence: pinned raw `# Afterpay iOS Component` lines 15–36, `## Advanced flow Component` lines 811–821, examples lines 55–67/872–884, and test/live lines 790–809.

## Q2 — Central integration, lifecycle, and warnings

**Query:** Which fields and Component actions are needed, what does the redirect response mean, and what capture constraints apply?

**Expected:** The Sessions and Advanced tables require shopper name/email/reference, country, billing/delivery addresses and line items; telephone is optional. Advanced also requires `paymentMethod: afterpaytouch`. Both use `InstantPaymentComponent` and no method-specific configuration; Sessions delegates to session and Advanced to the merchant handler. The Advanced `RedirectShopper` action is a redirect step, not final success. Capture may be automatic or manual by account configuration; partial capture requires manual capture. Capture within 13 days; first installment is charged at authorisation and refunded if Afterpay cancels an uncaptured payment after the deadline. TEST authorisation expires after one day. Initial partial capture cancels remainder unless multiple partial captures are enabled through Support; each such capture creates an invoice. The Advanced Components prerequisite text links a Drop-in base guide, so do not treat that link as Components implementation evidence. Evidence: raw tables lines 44–53 and 856–866; setup lines 739–765 and 823–848; redirect lines 1581–1595; capture lines 769–788/1597–1616; mismatch line 819.
