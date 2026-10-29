# Riverty API-only worker retrieval queries

## Q1 — Purpose and product scope

**Query:** What does the Riverty API-only guide cover, and which Riverty types and method-discovery inputs does it distinguish?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-riverty-api-only.md` → `raw/adyen/docs/payment-methods/riverty/api-only/2026-09-15.md`.

**Evidence locator:** Canonical stem `https://docs.adyen.com/payment-methods/riverty/api-only`; full pinned raw `raw/adyen/docs/payment-methods/riverty/api-only/2026-09-15.md`, `# Riverty for API only` lines 15–31, `## Get Riverty as an available payment method` lines 80–121, and `## Add additional parameters to your /payments request` lines 123–141. Preserve AT/BE/DE/NL/CH and EUR/CHF as discovery values, with four distinct method types; do not infer every combination or merchant/shopping eligibility.

## Q2 — Risk, redirect, capture and refund conditions

**Query:** Which risk-data qualifications and post-payment steps are mandatory for Riverty API-only, and what happens with partial captures and refunds?

**Expected route:** Same root → Adyen index → online-payments concept → Riverty API-only source → pinned raw.

**Evidence locator:** Same canonical stem and full pinned raw path: `### Profile tracking` lines 47–61, payment table lines 127–141, redirect lines 220–239, `## Capture the payment` lines 241–258, remainder cancellation lines 321–330, `## Refunds and cancellations` lines 553–565, and go-live requirements lines 997–1003. Distinguish recommended tracking from required profileTrackingShopId when implementing it, conditional IBAN, delivery-name requirements and the first-time shopper fallback to billingAddress-only delivery after a differing-address risk rejection (raw line 132), mandatory manual capture after shipment, 30-day expiry, matching partial line items, release of uncaptured remainder, and capture-specific refund reference. Invoice sender is unresolved: the merchant is named at raw line 45, Riverty at line 137, and capture triggers the invoice at line 243 without identifying the sender. The table/prose/example disagree on `deviceFingerprint` placement (lines 43, 61, 139, 158), and capture curl has malformed `https: //` (line 265). The `-X POST` examples lack a shell continuation before `-d` (for example lines 96–97, 149–150, 268–269); inspect raw, not copy-ready snippets.
