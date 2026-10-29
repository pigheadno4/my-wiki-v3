# C45 Clearpay API-only retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-clearpay-api-only`

Full pinned raw path: `raw/adyen/docs/payment-methods/clearpay/api-only/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-clearpay-api-only]]` → `[[raw/adyen/docs/payment-methods/clearpay/api-only/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does Clearpay API-only integration require the merchant to build, and does a GB/GBP test response prove availability?

**Answer path:** Raw lines 15–50 scope the page to Clearpay-specific additions to an existing API-only Advanced flow and a merchant-built form collecting name, email and addresses for risk checks. `/paymentMethods` lines 52–91 specify GB/GBP and show a TEST response containing `clearpay`. The linked overview `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31 identifies UK/GB/GBP Clearpay. Neither an example response nor a sandbox status proves a particular merchant's live eligibility or settled payment.

## Q2 — central capability, prerequisites and warnings

**Query:** How does Clearpay discovery lead to redirect, and what capture/refund/discount constraints follow?

**Answer path:** Requirements lines 23–29 specify existing API-only integration, redirect handling and Customer Area addition. `/paymentMethods` lines 52–60 requires GB/GBP for discovery; `/payments` table lines 93–106 marks shopper/country/address/items required, phone optional, and request example lines 108–170 sets `paymentMethod.type: clearpay`. Initial redirect response lines 172–186 does not prove final authorisation; the linked base flow handles return. Capture lines 188–207 specify 13-day expiry, one-day test expiry and partial-capture remainder cancellation unless multiple partial capture is enabled. Cancel/refund lines 209–218 distinguish before/after capture. Discount lines 220–254 say £1 off Item #2 and show quantity two at -100 minor units, lowering total from 1000 to 800. This reconciles as £1 per unit; the prose does not settle per-unit versus total intent. The illustrative JSON omits a comma, so it is not copy-ready. Both curl examples omit continuation before `-d` at lines 64–69 and 111–116. Test/live lines 256–271 require sandbox account/card setup and a live Customer Area request.
