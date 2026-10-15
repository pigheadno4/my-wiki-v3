# Classic Pix retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** When should this Adyen Pix guide be used, and does a returned QR code prove the payment was completed?

**Expected route:** `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-pix]]`; pinned raw `# Pix (classic)` lines 15–44, `## Make a payment` lines 116–134, `## Payment result` lines 161–165.

**Expected answer:** This snapshot is for an existing older Classic API `/authorise` integration; Checkout API users are sent to the separate Pix documentation. The Classic response's `Received` result and QR data enable shopper action and do not prove payment. A completed shopper payment produces an asynchronous webhook result. The example `AUTHORISATION` success event is illustrative, not a guarantee or evidence of a particular transaction.

## Q2 — Central capability, prerequisites, warnings

**Query:** What must a Classic Pix merchant send and verify, and what Brazil, currency, expiry, and amount-change conditions govern the flow?

**Expected route:** Same source; pinned raw lines 25–50 for local entity, BR/BRL and feature table; `## Build your payment form` and `## Make a payment` lines 52–86; `### Transaction conditions` lines 136–149; `## Match the original and the paid amount` lines 234–236; `## Refunds` and `## Test and go live` lines 238–255.

**Expected answer:** The page says the merchant needs a Brazilian local entity, and the table limits this route to Brazil and BRL. After test-account Pix setup, the merchant collects shopper name and CPF/CNPJ and sends Classic `/authorise` with `selectedBrand=pix`, amount, `shopperName`, and `socialSecurityNumber`. QR expiry defaults to 24 hours with a five-day maximum. Approval depends on Pix and acquirer checks. Because the shopper can edit the amount in the bank or wallet app, reconcile original and paid amounts from the webhook; the page recommends cancel/refund when they differ. Full refunds have a 90-day window in this snapshot. Test promotion simulates sale; live acceptance requires a separate live Customer Area request.
