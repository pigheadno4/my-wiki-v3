# Afterpay Flutter Drop-in retrieval check

- Canonical source stem: `source-adyen-docs-payment-methods-afterpaytouch-flutter-drop-in`.
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-afterpaytouch-flutter-drop-in.md` → `raw/adyen/docs/payment-methods/afterpaytouch/flutter-drop-in/2026-09-15.md`.

## Q1 — Purpose, scope, and inference limit

**Query:** What does this Flutter Drop-in page cover, and do its AUD/AU example or US sandbox choice prove live availability?

**Expected:** It provides Afterpay-specific additions for an existing Flutter Drop-in integration in Sessions and Advanced server flows. Sessions says Checkout API v68+ and redirect handling; Advanced has its own base-flow and redirect requirement. The examples are TEST and the US choice is for sandbox account creation; neither proves merchant enablement or expands the linked overview's AU/CA/NZ product table. The Sessions prerequisite text links an Advanced base guide despite saying Sessions. Evidence: raw `# Afterpay Flutter Drop-in` lines 15–36; TEST example lines 55–67; `## Advanced flow Drop-in` lines 789–799; sandbox/live lines 768–787.

## Q2 — Central fields, redirect, capture, and warnings

**Query:** Which fields and setup are specified, what does the redirect response mean, and what happens with late or partial captures?

**Expected:** The Sessions and Advanced tables require shopper name/email/reference, country, billing/delivery addresses and line items; telephone is optional. Advanced additionally requires `paymentMethod: afterpaytouch`. Sessions says contact Support to add the method in Customer Area, while Advanced says add it in Customer Area; preserve this flow-specific wording. No method-specific Drop-in configuration is needed, but base integration and redirect handling remain prerequisites. The Advanced `RedirectShopper` action is not final payment success. Capture is automatic or manual by account configuration; partial capture requires manual capture. Capture deadline is 13 days after authorisation, with first installment charged at authorisation and refunded if Afterpay cancels after noncapture; TEST authorisations expire in one day. An initial partial capture cancels the remainder unless multiple partial captures are enabled through Support, which creates an invoice per capture. Evidence: raw tables lines 44–53/813–823; setup lines 33–36/797–799; configuration lines 739–743/801–805; redirect lines 1538–1552; capture lines 747–766/1554–1573.
