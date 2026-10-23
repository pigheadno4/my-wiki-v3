# C31 retrieval checks: airline enhanced scheme data

Q1. What is this guide for, and which merchants/flows does it qualify?

It describes airline ESD on US domestic card transactions for specified travel MCCs, subject also to parent ESD requirements (raw lines 17–28). MCC 3000–3350 and 4511 are listed for Mastercard/Visa; MCC 4722 has separate Mastercard commercial/consumer and Visa card-present/card-not-present limits (raw lines 35–54). Automatic/delayed automatic capture uses `/payments` `additionalData.airline`, while manual single/multiple partial capture uses `/captures` `enhancedSchemeData.airline` (raw lines 56–68). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-airline]] → [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/airline/2026-09-15]].

Q2. What field conflicts and outcome limits make the examples unsafe as a complete recipe?

The mapping marks airline/ticket/passenger/leg and issue-date fields required (raw lines 69–88), but its capture table spells `legs.depatureAirportCode` while the example uses `departureAirportCode` (raw lines 80, 188–190); its `/payments` example omits table-required `issue_date` (raw lines 82, 96–148). The v72 test examples include a plain card number/CVC and no response or interchange result; they do not establish PCI compliance, eligibility, discount, capture or settlement (raw lines 94–221). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data-airline]] → [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/airline/2026-09-15]].
