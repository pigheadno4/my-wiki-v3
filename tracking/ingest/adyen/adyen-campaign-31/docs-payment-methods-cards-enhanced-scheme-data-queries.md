# Retrieval checks — docs-payment-methods-cards-enhanced-scheme-data

Q1. What is ESD for, and what prerequisites and eligibility limits does this overview state?

A1. ESD is extra card-transaction data in payment or capture requests; optional Visa/Mastercard Level 2/3 or travel data can lower interchange fees by up to 1% without changing authorization rates, whereas other ESD serves compliance/eligibility without that fee benefit (raw lines 22–29). The guide requires Advanced-flow online integration and AUTHORISATION/CAPTURE webhooks (raw lines 31–39), maps type by scheme/MCC, and excludes specific MCCs entirely (raw lines 57–97). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]] → [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/2026-09-15]].

Q2. What happens to invalid or ineligible ESD, and which capture/API boundaries apply?

A2. Adyen says it processes the payment without ESD when the business is ineligible or ESD incomplete/invalid; after processing the ESD cannot be changed or fixed, ESD types cannot be combined, and refunds/reversals do not use ESD (raw lines 40–54, 85–97). In this snapshot Checkout API captures do not support car-rental or lodging ESD, while an existing Classic API integration may use /capture; Visa discounts require AVS setup and request data (raw lines 47–55). Child guide links at raw lines 99–123 are navigation, not proof of availability or successful savings. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-enhanced-scheme-data]] → [[raw/adyen/docs/payment-methods/cards/enhanced-scheme-data/2026-09-15]].
