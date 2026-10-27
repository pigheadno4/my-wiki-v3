# docs-payment-methods-bacs retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bacs]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 Adyen overview describes GB/GBP BACS Direct Debit collection, the shopper's DDI/mandate, delayed processing, advance notice, chargeback rights and implementation routes (pinned raw lines 15–39, 60–74, 125–167). It is not a one-time bank-transfer guide and does not prove a valid mandate, account eligibility or cleared funds. Shopper confirmation precedes Adyen's DDI/payment submission, and clearing/settlement can take four to six days (line 27). Canonical source stem: `source-adyen-docs-payment-methods-bacs`.

## Q2 — What are the central conditions and warnings?

The page supports one-off and recurring debits but advises against one-off/physical goods because of chargebacks (pinned raw line 25). It requires shopper name, bank account, sort code and email plus ownership/agreement confirmation in the described flow (line 27). Adyen strongly recommends advance notice; source-stated scheme risk cites 10 days before charge, while its email template is recommended eight working days before capture and says charge appears two to three working days later (lines 35–39). Shoppers can cancel a DDI at any time; unpaid debits and various disputes become chargebacks that cannot be defended (lines 60–74). The `CHARGEBACK` webhook example has `success: true`, which is event success, and a Service User Number **298288** versus prose **182827**; it does not establish the merchant's bank statement identifier (lines 29, 76–118). Canonical source stem: `source-adyen-docs-payment-methods-bacs`.
