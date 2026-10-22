---
title: "Adyen Payout Service bank transfer routes"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts/transfer-routes"
raw_files:
  - "adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/transfer-routes/2026-09-15.md"
tags: [adyen, payout-service, bank-payouts, transfer-routes, configuration-api]
---

## Overview

This [[adyen]] Payout Service guide, last modified 2023-03-13 and captured 2026-09-15, recommends calculating available routes before sending funds to a new **third-party bank recipient** because banks or regulators may constrain priority or amount. It belongs under [[adyen-payouts]]. POST `/transferRoutes/calculate` is a **Configuration API route inquiry**, separate from the later Transfers API payout request; a returned route does not mean a transfer has been requested, booked or credited to a bank.

## Key takeaways

- A Payouts integration and a Configuration API credential with **Balance Platform BCL role** are listed prerequisites. Calculate routes by recipient country/region or by concrete counterparty bank details. The recommendation is framed as failure prevention when paying a new recipient, not a guarantee of payout success. See raw lines 19–34.
- Country/region inquiry requires `balancePlatform`, three-character `currency`, `category: bank`, and two-character recipient `country`; `priorities` is optional. The TEST example asks about USD/NL with regular, crossBorder and wire. Returned `transferRoutes` entries give currency, priority and route-specific requirements such as amount bounds, address fields, bank-account identification type and payment-instrument type. The numbers and route options in the sample are examples, not a current universal matrix. See raw lines 36–71 and 301–357.
- Counterparty inquiry requires `balancePlatform`, `currency`, `category: bank` and `counterparty` (third-party bank account or transfer instrument); priorities remain optional. **Source `balanceAccountId` is conditionally required when counterparty contains `transferInstrumentId`**. The example uses an NL IBAN directly, and the response shows NL EUR instant/wire routes with distinct amount caps and bank-ID requirements. See raw lines 359–401 and 716–780.
- The document's next steps explicitly route to a separate bank-payout request and webhook tracking. Route calculation is preflight information about supported choices and additional requirements, not a transfer instruction or evidence of funds movement. See raw lines 782–790.

## Evidence boundary

The guide does not prove that the recipient bank will accept a specific payment, that source funds are available, that a transfer was authorised or booked, or that a beneficiary received funds. Bank/regulatory limits and account details may change after the dated snapshot. TEST code examples are illustrative; consult the API schema and response for the relevant environment and recipient.

## Detail locators

- Purpose, credential gate and country query: raw lines 19–71.
- Country response requirements: raw lines 301–357.
- Counterparty query and conditional source ID: raw lines 359–401.
- Counterparty route response and separate payout next step: raw lines 716–790.

## Related

- [[adyen-payouts]]
- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts]]
- [[source-adyen-docs-payouts-payout-service-pay-out-to-bank-accounts-verify-counterparty]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/pay-out-to-bank-accounts/transfer-routes/2026-09-15|Payout Service bank transfer-route guide, 2026-09-15 capture]]
