# Fixed retrieval checks — docs-payment-methods-gift-cards-stored-value-api

## Q1 — Define the API purpose and payment boundary

- Query: What can Adyen's Stored Value API manage, and can it make, cancel or refund gift-card payments?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api.md` → `raw/adyen/docs/payment-methods/gift-cards/stored-value-api/2026-09-15.md`.
- Expected: JSON-only management API for online/POS gift cards (raw lines 15–19); issue, status, load, balance, same-provider merge and void a prior Stored Value API transaction from last 24 hours (21–26); Terminal API suggested for in-person operations except issue (28). It explicitly cannot make, cancel or refund payments; follow separate online/POS payment routes (30–38). `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md` supplies cross-channel method context.
- Scope: The 2022-modified snapshot is not evidence of current provider access, account permission, payment completion or an executed stored-value operation.

## Q2 — Recover provider matrix, exceptions and result outcomes

- Query: Which provider/channel operations are marked available, what SVS exception and conflict matter, and how is API success distinguished?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api.md` → pinned raw; compare fully read status-change child `raw/adyen/docs/payment-methods/gift-cards/stored-value-api/change-status/2026-09-15.md` lines 33–39.
- Expected: Supported-card list names Intersolve/SVS/Fiserv but matrix includes Givex (raw lines 40–54). Online issue Givex/Fiserv only, activate/activate+load SVS only, deactivate-no-amount Givex only, load/check/void all, merge Fiserv only (56–63). In-person issue/merge crossed all, activate/activate+load/load/check/void checked all, deactivate Givex only (65–76). New SVS integrations cannot issue; existing issuers may continue (78–81). Status-change child crosses all online activation, conflicting with overview's SVS checks (child raw 33–39). Endpoint list and result codes show Success completed, Refused/Error with reason, NotEnoughBalance for insufficient card value (83–106). Simulator data includes past 12/2020 expiries; use provider test data for end-to-end checks (108–122).
- Scope: Matrix and endpoint examples do not prove live availability or operation outcome. The two activation matrices are unreconciled; retain both dated scopes and verify current provider/channel support separately.
