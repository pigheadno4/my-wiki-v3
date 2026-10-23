# C31 retrieval checks: ecommerce card receipts

Q1. When does the guide call for a receipt and what are the delivery/access prerequisites?

It says provide a receipt for an online card payment or an online-card refund (raw line 19). Email receipts have static-format, business-name and receipt/link identification conditions (raw lines 21–25). A website/app receipt link needs access instructions, must lead directly to the receipt and must remain available for at least 120 calendar days after capture (raw lines 27–31). The field list is at raw lines 33–49. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-card-receipts]] → [[raw/adyen/docs/payment-methods/cards/card-receipts/2026-09-15]].

Q2. What prohibited data and outcome boundary must be retained?

No more than the last four card digits, no PIN or representation of it, no CVC/CVV and no competing-scheme promotion may appear on the receipt (raw lines 51–67). The listed authorization code and captured/refunded amount are content fields, not proof that payment, capture or refund completed (raw lines 40–44). The page does not demonstrate actual receipt generation, access or delivery. Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-cards-card-receipts]] → [[raw/adyen/docs/payment-methods/cards/card-receipts/2026-09-15]].
