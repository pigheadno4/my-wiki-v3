# SFTP recurring authorisation request retrieval checks

## Q1 — Purpose, scope, and non-inference

**Query:** Does the `Recurring` sub-line create a token or prove a new charge succeeded, and what is this page's actual scope?

**Expected route:** `[[adyen-index]]` → `[[adyen-batch-processing]]` → `[[source-adyen-docs-development-resources-batch-processing-advanced-sftp-batch-files-batch-request-file-authorisation-request-file-authorisation-for-a-recurring-payment]]`; pinned raw `## Mandatory sub-lines` lines 16–18, `### Recurring` lines 40–50, and dedicated example lines 80–89.

**Expected answer:** This is an SFTP `Authorisation` request-file format for a recurring payment using stored details. `RECURRING` plus a specific 16-character detail token or `LATEST` selects an existing stored data set for a new authorization request; it does not create the stored credential or prove validation, issuer authorization, capture, or final payment. The sample is a request structure only.

## Q2 — Central capability, prerequisites, warnings

**Query:** What exact sub-lines and field positions matter for a recurring authorization, and does the optional order-reference sample make CVC mandatory?

**Expected route:** Same source; raw `### PaymentDetails` lines 20–38, `### Recurring` lines 40–50, `### ShopperInteraction` lines 52–89, `### Address` lines 95–128, and `### MerchantOrderReference` lines 130–148.

**Expected answer:** `PaymentDetails`, `Recurring`, and `ShopperInteraction` are mandatory. `PaymentDetails` field 4 is amount, field 5 currency exponent, field 6 three-letter currency, and field 7 unique shopper reference; blank optional fields still retain delimiter commas. `Recurring` field 4 is `RECURRING` and field 5 selects a token or `LATEST`. For this recurring use, the page says `ContAuth` unless MOTO. Optional Address and MerchantOrderReference sub-lines have their own field layouts. Both optional examples leave required `PaymentDetails` field 7 (`shopperReference`) blank (raw line 34 versus Address example lines 117–128 and MerchantOrderReference example lines 139–148), so neither is a copyable complete recurring request. The MerchantOrderReference sample includes `PaymentDetails` and `Card` with CVC but omits mandatory `Recurring` and `ShopperInteraction`; it is not a complete alternate recurring request and does not make CVC mandatory for stored-detail selection.
