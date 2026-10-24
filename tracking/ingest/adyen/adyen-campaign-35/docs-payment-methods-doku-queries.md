# DOKU retrieval check

Q1. What is the scope and purpose of the DOKU overview, and what cannot be inferred from it?

It describes DOKU-partnered Indonesia bank transfers and convenience-store cash payments, with a historical Cash/ATM additional-action matrix marked ID/IDR; it is also a chooser for Web, API-only and Pay by Link child routes (raw lines 15–30, 115–133). Its matrix and link cards do not establish present variant/merchant eligibility, current pricing, SDK/API versions, successful authorization, capture, settlement or refund. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-doku]] → [[raw/adyen/docs/payment-methods/doku/2026-09-15]].

Q2. How do the two DOKU paths differ, and which prerequisites and outcome warnings matter?

For bank transfer, collect shopper first/last name and email, request payment, show the returned order-specific virtual-account number, expiry and instructions, and await shopper transfer before expiry; the page places an authorization webhook/Customer Area check before delivery (raw lines 32–62). BCA and BRI virtual-account types are specifically marked local-entity-only (raw lines 64–76). For store cash, the response instead supplies an order-specific voucher code, expiry and instructions; the shopper pays at a cashier, and the same authorization-before-delivery boundary applies (raw lines 78–113). Creating a VA or voucher is not payment completion, and no fixed expiry duration is given. Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-doku]] → [[raw/adyen/docs/payment-methods/doku/2026-09-15]].
