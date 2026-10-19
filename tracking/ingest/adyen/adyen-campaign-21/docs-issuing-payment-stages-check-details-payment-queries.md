# Q1 — purpose and prerequisites

**Query:** How does this Issuing-path guide retrieve payment or transfer details, and what access does it specify?

**Answer:** It describes GET `/transfers` for a list, GET `/transfers/{id}` for a specific transfer, and Customer Area **Balances > Transfers**; it recommends webhooks for recurring tracking (raw lines 19–33, 47–56, 463–484). Its requirements table says an **Adyen for Platforms integration**, `TransferService Webservice Retrieve role` for API retrieval and **Balance platform base role** for Customer Area transfer viewing, with separate confirmation-letter and unmasked-PII roles (raw lines 35–45). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-payment-stages-check-details-payment]] → [[raw/adyen/docs/issuing/payment-stages/check-details-payment/2026-09-15]].

# Q2 — boundary and conflicting examples

**Query:** Can the list example be copied as a valid query, and does a displayed `booked` card transfer prove payment success?

**Answer:** The query table marks `createdSince`/`createdUntil` required with an under-six-month window, and text requires at least one unique identifier (raw lines 74–83). The prose example spans May 2025 to May 2026, while curl uses one day in May 2026 and no unique identifier (raw lines 85–95); use the applicable Transfers API schema and observed response to resolve this. A sample list object has `status: booked` alongside `reason: counterpartyAccountNotFound` (raw lines 294–310); sample data is not proof of a successful real card payment, capture or settlement. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-payment-stages-check-details-payment]] → [[raw/adyen/docs/issuing/payment-stages/check-details-payment/2026-09-15]].
