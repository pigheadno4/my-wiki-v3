# Fixed retrieval checks — docs-payment-methods-gift-cards-stored-value-api-check-balance

## Q1 — Identify balance inquiry and card paths

- Query: How does Stored Value API `/checkBalance` identify untokenized versus tokenized gift cards, and what does it return?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api-check-balance.md` → `raw/adyen/docs/payment-methods/gift-cards/stored-value-api/check-balance/2026-09-15.md`.
- Expected: Remaining-balance inquiry purpose (raw lines 15–19). No-token request uses merchant account, card type/number, conditional security code, optional in-store store/expiry/holder and reference (35–79). Tokenized request uses card type, prior `recurringDetailReference`, matching `shopperReference`, `shopperInteraction`, merchant account/reference and optional in-store store (117–148). Response reports `currentBalance` currency/value in minor units, `pspReference` and `resultCode` (96–115, 150–169).
- Scope: This is a balance inquiry, not a payment, load, authorization or future-spend guarantee. No card or API operation was performed.

## Q2 — Recover provider/channel and sample conflicts

- Query: Which provider/channel combinations are marked for balance checks, and what contradictions limit the examples?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api-check-balance.md` → pinned raw; compare fully read Stored Value API overview `raw/adyen/docs/payment-methods/gift-cards/stored-value-api/2026-09-15.md` lines 108–116.
- Expected: Both online and in-person matrices check Givex, SVS, Fiserv/ValueLink and Intersolve (balance raw lines 21–33), while both request type lists restrict Givex to in-person (55, 129). No-token sample is called SVS but uses number `603628672882001915092` and code `5754` (81–94), labeled Givex in the overview simulator table (overview raw 108–116). The sample `Success`/EUR 5600 output is illustrative and does not prove a real query or payment (96–115). Load, merge, issue, status and void links are distinct operations (171–189).
- Scope: The 2026-09-15 capture does not resolve provider eligibility or the brand/number mismatch. Verify actual channel/provider support and credential source separately.
