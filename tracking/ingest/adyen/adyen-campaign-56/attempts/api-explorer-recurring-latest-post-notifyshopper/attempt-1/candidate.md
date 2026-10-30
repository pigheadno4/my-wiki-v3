---
title: "Adyen Recurring API POST /notifyShopper (captured v68)"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/notifyShopper"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/notifyShopper/2026-09-15.md"
tags: [adyen, recurring-api, india, pre-debit-notification, api-explorer]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Recurring API `POST /notifyShopper` on the displayed test `https://pal-test.adyen.com/pal/servlet/Recurring/v68` server. It asks the issuer to inform a shopper about an upcoming recurring payment and is scoped to **local acquiring in India**. It is a notification request, not the later recurring payment, issuer delivery proof, mandate approval, or payment authorization. See [[adyen]] and [[adyen-tokenization]].

## Key takeaways

- The request property table marks upcoming `amount.currency` and minor-unit `amount.value`, `merchantAccount`, the merchant's pre-debit notification `reference`, and `shopperReference` required. The shopper reference must match the one used in the initial payment. `billingDate` and `billingSequenceNumber` are optional in this table; `displayedReference` defaults to `reference` if omitted. `recurringDetailReference` and `storedPaymentMethodId` are shown as optional token-identifying fields; the example supplies the latter, which does not make it universally required by the table.
- The 200 response schema lists `resultCode`, `message`, request `pspReference`, downstream `shopperNotificationReference`, stored-payment-method ID and references as optional properties. Its example has `resultCode: Success` and `Request Processed Successfully`, establishing the illustrated request processing only. It does not prove issuer delivery to the shopper or authorize/settle the subsequent recurring charge.
- The page lists 400, 401, 403, 422 and 500 generic request/error schemas. It gives a 200 response example but no example for those failures and no `resultCode` enum. The wider India recurring-card guide provides separate pre-debit timing, payment-request and webhook steps; those details are not specified by this endpoint contract.
- The captured `latest` URL displays a test Recurring v68 server; it does not establish today's latest version, live India acquiring eligibility, or a successful notification/payment.

## Detail locators

- Purpose, India local-acquiring scope and displayed server: raw lines 5–10.
- Request table, token and shopper identity: lines 14–27; example: 29–45.
- 200 response fields: lines 46–60; generic error schemas: 63–130; 200 response example: 132–147.

## Related

- [[source-adyen-docs-payment-methods-cards-cards-recurring-india]] — broader historical India mandate, pre-debit and later charge guide; review its timing/version qualifications.
- [[adyen-tokenization]] — provider concept and reciprocal source route.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/notifyShopper/2026-09-15|Recurring API POST /notifyShopper snapshot (2026-09-15)]]
