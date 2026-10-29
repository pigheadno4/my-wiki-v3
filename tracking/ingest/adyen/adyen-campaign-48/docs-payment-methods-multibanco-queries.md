# Retrieval checks: Multibanco

## Q1 — Purpose and scope
Query: What does Adyen's Multibanco overview describe, and what does it not establish?
Expected: It is a 2026-09-15-captured method overview for Portugal: the shopper gets a voucher at checkout and later pays at an ATM with a debit card or using online banking. It routes to platform-specific integration guides but does not itself give a complete API/SDK recipe, prove current merchant enablement, or show live payment completion. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-multibanco]] → [[raw/adyen/docs/payment-methods/multibanco/2026-09-15|pinned raw]]. Verify canonical stem `/payment-methods/multibanco`, raw lines 15–23 and **How do you want to integrate?** lines 38–86.

## Q2 — Voucher and capabilities
Query: What fields and expiry control does the Multibanco voucher have, and how should the capability matrix be read?
Expected: Voucher has payment reference, entity number, payable amount and expiry; the page says contact Support to set expiry. Table labels Cash and ATM, Direct, PT/EUR; recurring, captures and chargebacks are marked unsupported while refunds, partial refunds and multiple partial refunds are marked supported. “Direct” is a table label and does not override the later voucher redemption step. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-multibanco]] → [[raw/adyen/docs/payment-methods/multibanco/2026-09-15|pinned raw]]. Verify canonical stem and raw lines 23–36.
