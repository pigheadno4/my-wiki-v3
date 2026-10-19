---
title: "Adyen Issuing: View payment and transfer details"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/payment-stages/check-details-payment"
raw_files:
  - "adyen/docs/issuing/payment-stages/check-details-payment/2026-09-15.md"
tags: [adyen, issuing, transfers, payments, balance-platform]
---

## Overview

This Issuing-path guide (last modified 2019-12-06; captured 2026-09-15) describes how to view balance-platform payment and transfer details through GET `/transfers`, GET `/transfers/{id}`, or Customer Area **Balances > Transfers**. It recommends webhooks for recurring transfer tracking such as reconciliation. A transfer represents funds credited to or debited from a balance account, and the guide distinguishes initiation, authorization, then capture for payment events or booking for other events. The page is a lookup guide, not evidence that a particular card payment was authorized, captured, booked or settled. [[adyen]] [[adyen-issuing]]

## Key takeaways

- **Access is scoped.** Although the URL is under Issuing, the requirements table says an **Adyen for Platforms integration** is required. For API retrieval it names the `TransferService Webservice Retrieve role`; Customer Area viewing requires the **Balance platform base role**. It separately names roles for downloading transfer confirmation letters and viewing unmasked PII in those letters. The page does not establish that an Issuing integration alone meets the listed requirement or that a particular credential has these roles. See raw lines 35-45.
- **List lookup:** GET `/transfers` or the Customer Area Transfers view lists activity; Customer Area results are limited to one balance platform at a time. The API table marks `createdSince` and `createdUntil` required and says the window must be under six months, and the prose says to provide at least one unique identifier. `paymentInstrumentId` requires `balanceAccountId`, `accountHolderId` or `balancePlatform` alongside it. Returned `data` contains matching transfers, with `_links` for next/previous pages when applicable. See raw lines 47-83 and 264-269.
- **Specific lookup:** Customer Area can search by transfer/payment instrument ID and open a Transfer ID; GET `/transfers/{id}` retrieves one transfer by path ID. The response guide highlights amount/currency, direction, event history, payment instrument, reference and current status such as `received`, `authorised` or `booked`. See raw lines 463-484 and 630-639.
- **Examples are internally inconsistent with the list-query rules.** The prose describes May 2025 to May 2026, longer than the stated six-month window; the displayed curl uses May 12 to May 13 **2026**, and neither that curl nor the prose supplies the unique identifier that the text says is required. Do not copy the examples as a validated request contract; confirm against the applicable Transfers API schema and observed response. See raw lines 76-95. The list response also illustrates a `booked` issued-card payment with reason `counterpartyAccountNotFound`, so its sample combination should not be treated as a successful real payment. See raw lines 294-310.
- **Status is contextual.** The response examples include accounting events and balances and are test/example data; a `booked` transfer in a sample is not proof that every card payment is captured or externally settled. For recurring operations, follow the guide's webhook recommendation rather than relying on a one-time GET snapshot. See raw lines 19-33, 271-461 and 641-739.

## Detail locators

- **Requirements**, raw lines 35-45: integration and role requirements, including confirmation-letter/PII roles.
- **View a list of payments and transfers**, raw lines 47-83: Customer Area navigation/filters and GET `/transfers` query table.
- **List request and response examples**, raw lines 85-461: test endpoint, language-specific examples, pagination shape and illustrative payment/internal-transfer objects; several examples conflict with the query prose.
- **View a specific payment or transfer**, raw lines 463-484: Customer Area search and GET `/transfers/{id}`.
- **Specific request and response examples**, raw lines 486-739: sample SDK calls, response fields, accounting-event history and issued-card payment object.

## Related

- [[adyen-issuing]] — Issuing product context and evidence boundary.
- [[source-adyen-docs-issuing]] — Issuing account/balance/card overview; separate lifecycle context.

## Raw Sources

- [[raw/adyen/docs/issuing/payment-stages/check-details-payment/2026-09-15|Adyen Issuing payment and transfer details guide, captured 2026-09-15]]
