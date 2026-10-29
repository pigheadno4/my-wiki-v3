# C44 Klarna for airlines retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-klarna-airlines`

Full pinned raw path: `raw/adyen/docs/payment-methods/klarna/airlines/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-klarna-airlines]]` → `[[raw/adyen/docs/payment-methods/klarna/airlines/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does the Klarna airline guide add, and what does it not establish?

**Answer path:** The source entry and raw line 19 identify extra travel fields in both `/sessions` and `/payments`, not a standalone payment integration. Raw `## Additional data` lines 21–159 and `## Line items` lines 161–183 define airline-specific request shape. It contains no complete returned-shopper/payment-result flow or proof of a particular airline's eligibility, accepted risk data, capture or settlement. The root/provider/concept/source route above leads to the pinned page for exact fields.

## Q2 — central capability, prerequisites and warnings

**Query:** What airline travel and invoice fields must be sent, how can optional risk data silently fail, and when is immediate capture described?

**Answer path:** Raw `/sessions` table lines 25–42 and `/payments` table lines 93–110 require `additionalData.additionalDataAirline` with customer reference, leg airport/carrier/date and numbered passenger fields. `## Line items` lines 165–183 requires quantity, description and amount including tax in minor units. Optional Base64 JSON `merchantData` is at lines 87–91 and 155–159; Klarna does not consume malformed data and returns no validation error. The general [[source-adyen-docs-payment-methods-klarna-web-drop-in]] guide says not to send it in TEST because test values cause an error. `## Capture payments` line 187 says airline immediate capture is supported for locked bookings and manual capture also remains; the general Web Drop-in source has an immediate-plus-24-hour-shipping automatic-capture condition. Read both contexts and verify configuration rather than infer an automatic-capture exception.
