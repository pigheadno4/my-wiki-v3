---
title: "Adyen Balance Platform webhook: payment instrument created"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.created"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.created/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, payment-instruments, issuing, business-accounts]
---

## Overview

This captured Balance Platform Webhooks API Explorer POST reference describes the incoming `balancePlatform.paymentInstrument.created` event Adyen sends after successful payment-instrument creation. It covers card and `bankAccount` instruments; the event is separate from the merchant's creation request. The `latest` route label gives no numbered webhook API version. See [[adyen-webhooks]], [[adyen-issuing]], [[adyen-business-accounts]], and [[adyen]].

## Key takeaways

- The event body requires `data`, `environment` (`test` or `live`), and `type`. `timestamp` is optional queue time; `data.balancePlatform` and `data.paymentInstrument` are marked optional. Within a supplied `paymentInstrument`, `balanceAccountId`, `id`, `issuingCountryCode`, and `type` are marked required; `type` is `card` or `bankAccount`. `card` details are conditional on card type, while `bankAccount` and optional additional account identifications are conditional on bank-account type.
- The schema describes `status` as active by default when unspecified, with card exceptions based on form factor and issuing country; a US physical card is given as an inactive-default example. It lists `active`, `inactive`, `suspended`, and irreversibly `closed`. If `statusReason` is `other`, the description requires `statusComment`. These are resource-field descriptions, not proof that this event activated a card, opened a usable bank account, or moved funds.
- **Card-number conflict:** The prose explicitly says the webhook does not include the number for a newly created virtual card and says the number is available only in the `POST /paymentInstruments` response. Yet the virtual-card test example contains `card.number`. Do not use that example to assume number disclosure in a delivered webhook. The second test example shows a `bankAccount` instrument with an IBAN; neither example establishes live availability, verification or account funding.
- Any HTTP `2xx` is documented as accepting this webhook, with optional `notificationResponse`. This page does not define delivery order, retry, deduplication, signature verification, or a later financial outcome.

## Detail locators

- Event trigger and virtual-card number statement: pinned raw lines 5–9.
- Required envelope, nested requiredness, conditional types and status behavior: pinned raw lines 13–36.
- Contradictory virtual-card and illustrative bank-account examples: pinned raw lines 38–94.
- Acknowledgment response: pinned raw lines 95–103.

## Related

- [[adyen-webhooks]] — event and acknowledgment context.
- [[adyen-issuing]] — card-instrument context.
- [[adyen-business-accounts]] — bank-account instrument context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-paymentinstruments]] — separate creation API and its response boundary.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.created/2026-09-15|Payment instrument created webhook reference, captured 2026-09-15]]
