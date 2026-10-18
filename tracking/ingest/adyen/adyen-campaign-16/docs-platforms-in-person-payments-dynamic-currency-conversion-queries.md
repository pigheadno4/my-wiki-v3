# C16 DCC retrieval checks

## Q1 — Purpose, scope, and inference boundary

Query: What does Adyen for Platforms in-person DCC do, and does this source prove live account eligibility, merchant of record, a specific FX return, or completed settlement?

Expected route: `wiki/sources/adyen/source-adyen-docs-platforms-in-person-payments-dynamic-currency-conversion.md` via `wiki/concepts/adyen-currencies-and-fx.md` and the Adyen index. Answer: dated pilot guide for eligible terminal customer choice between local and billing currency; accepted DCC adds conversion/markup. Pilot status and account/card/region qualifications remain. It does not establish account enablement, legal seller/MOR, a merchant-specific rate/share, or executed funds movement. Raw locators: lines 19–26, 372–378, 398–470.

## Q2 — Capability, prerequisites, and warnings

Query: For a platform's in-person DCC payment, what setup and markup split route is described, and which constraints would block a general claim that every terminal/payment can use it?

Expected route: same source and raw. Answer: Terminal API/payment or standalone setup, signed DCC addendum, enabled terminal settings and role/reporting prerequisites; split profile or per-payment `platformDccLogic` with per-payment precedence, user percentage in basis points, remaining post-Adyen-share amount otherwise to liable balance account. The shopper chooses local versus card-billing currency; the worked example equates local and settlement currency but does not establish a universal equivalence. Ordinary payment splits still allocate the original amount (USD 620 example: USD 600 user and USD 20 platform commission), while post-Adyen-share DCC markup follows separate DCC instructions; the broad reconciliation sentence about paying the full original amount to the user is context-specific. Customer choice/receipt duties; no same-transaction surcharge or offline POS; standalone authorization cannot include individual split instructions; dated version behavior; pilot and card/currency/region restrictions, plus Visa/Mastercard/Maestro versus VPay source-list discrepancy. Raw locators: lines 28–47, 49–58, 70–112, 114–120, 177–199, 281–296, 372–378, 398–470.
