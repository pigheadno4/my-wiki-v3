# Fixed queries — Received payment details report

## Q1 — purpose, scope, and what must not be inferred

**Query:** What does Adyen's Received payment details report describe, at what grain, and does a row or Amount establish capture or settlement?

**Answer:** It gives details of authorised and refused payments processed through Adyen, including shopper interaction, risk score and acquirer response. Each line after the header is a separate entry, and one report may include multiple merchant accounts. The standard Amount is a positive authorisation amount even when the payment was cancelled before capture. Acquirer Response is not necessarily final status. These report fields do not establish capture, settlement or payout. Raw: `raw/adyen/docs/reporting/received-payment-details-report/2026-09-15.md:17-25,35-37,49-69`. Canonical route: `[[source-adyen-docs-reporting-received-payment-details-report]]` → `[[adyen-reporting]]`.

## Q2 — central capability, prerequisites, and warnings

**Query:** How can the report be obtained and configured, and what operational cautions apply to automated ingestion and sensitive fields?

**Answer:** The page routes to manual and automatic retrieval; it says the report is available for company and merchant accounts and uses the account time-zone setting. Customer Area column configuration requires one of Merchant admin, Merchant report role, Merchant financial or Merchant POS Report role. Adyen's migration may require ingestion-pipeline updates; column order and added columns are configurable, and removing Creation Date removes the sorting guarantee. Standard fields may include shopper IP/email/address data; Shopper PAN contains the card's last four digits for cards but IBAN/BIC for SEPA. Availability and listed roles do not prove a particular user's access. Raw: `raw/adyen/docs/reporting/received-payment-details-report/2026-09-15.md:21-27,43-45,54-69,71-88,186-207`. Canonical route: `[[source-adyen-docs-reporting-received-payment-details-report]]` → `[[adyen-reporting]]`.
