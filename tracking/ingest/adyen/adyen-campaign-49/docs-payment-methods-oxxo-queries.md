# OXXO overview retrieval checks

## Q1 — What is OXXO in the captured Adyen overview, and what does voucher issuance establish?
Expected route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-oxxo.md` → `raw/adyen/docs/payment-methods/oxxo/2026-09-15.md`.
Expected answer: OXXO is described as a Mexican cash voucher method: online shopper selects it, receives and prints a voucher, and pays at an OXXO cashier. Issuing the voucher does not establish payment. On successful payment OXXO confirms to Adyen, typically within one business day but sometimes longer. Raw locators: lines 23–29. The page is an overview, not a complete integration or evidence of a paid transaction.

## Q2 — What expiry, capability, and integration qualifications must be retained?
Expected route: same root/provider/concept/source/raw chain.
Expected answer: if unpaid before the due date, the transaction remains open in Customer Area for seven days before voucher expiry; the source does not calculate the due date or say seven days from issuance. The captured matrix lists Cash and ATM/voucher/MX/MXN and marks recurring, all listed refund variants, all listed capture variants, and chargebacks unavailable. It routes to Web, API-only, Pay by Link and in-person guidance without giving child implementation behavior. Raw locators: lines 29–35 and 37–61. These are historical method-level statements, not current merchant eligibility or a live outcome.
