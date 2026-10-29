# Fixed retrieval checks — docs-payment-methods-gift-cards-stored-value-api-change-status

## Q1 — Purpose, card state and provider/channel gates

- Query: What does Stored Value API `/changeStatus` do, and when do activation and deactivation appear available in the captured matrix?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api-change-status.md` → `raw/adyen/docs/payment-methods/gift-cards/stored-value-api/change-status/2026-09-15.md`.
- Expected: Activate/deactivate and optional load during activation (raw lines 15–19). Active releases stored funds; virtual cards autoactivate at issue; plastic cards may activate with or without amount, but preloaded card amount must be omitted or exact (21–25). Inactive is an end state, card unusable and remaining value unavailable (27–29). Online activation and activation+load are crossed for Givex/SVS/Fiserv-ValueLink/Intersolve; only Givex online deactivation without amount checked. In-person activation and activation+load checked for all four; only Givex deactivation without amount checked (31–47).
- Scope: This is a 2020-modified, 2026-09-15-captured provider/channel matrix, not current availability or merchant onboarding. The SVS activation example at lines 100–118 does not override the online matrix. The separate gift-card overview `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards.md` gives cross-channel context.

## Q2 — Request identity, token path and response meaning

- Query: How do activation and token/no-token deactivation requests identify the card, and what result proves a status change?
- Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gift-cards-stored-value-api-change-status.md` → pinned raw.
- Expected: Activation `status: active`, optional amount, merchant account, optional in-person store, card type/number/conditional security code and reference (raw lines 49–98); activation type list includes Intersolve-supported card types (74). No-token deactivation uses card number and type; tokenized deactivation uses type, `recurringDetailReference`, `shopperReference`, `shopperInteraction` and reference (143–250). Deactivation lists Givex/SVS/ValueLink types, not Intersolve (165, 230). Responses include `currentBalance`, `pspReference`, `resultCode`; `Success` means change carried out, other codes need interpretation, and deactivated remaining value stays unavailable (120–141, 207–215, 253–261). Separate `/void` navigation says undo a previous Stored Value API transaction from last 24 hours, but gives no reactivation guarantee here (273–278).
- Scope: Request examples and sample Success response do not prove any actual status change or value movement. No live API or financial operation was performed.
