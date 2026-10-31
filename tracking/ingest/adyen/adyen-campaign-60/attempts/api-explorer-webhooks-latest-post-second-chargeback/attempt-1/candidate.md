---
title: "Adyen SECOND_CHARGEBACK webhook reference"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK/2026-09-15.md"
tags: [adyen, webhooks, disputes, chargebacks]
---

## Overview

The 2026-09-15-captured Webhooks `latest` `POST /SECOND_CHARGEBACK` reference describes an incoming dispute notification: the issuing bank declined material submitted in defense of the original chargeback, and the disputed amount is deducted from the merchant account. It is a notification reference, not a merchant operation to initiate a second chargeback.

## Key takeaways

- The request-body table marks outer `live`, `notificationItems`, and nested `NotificationRequestItem` optional, while it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required within the item. This is nested-property requiredness, not a claim that the outer body or wrapper is required.
- `merchantReference` is the merchant's payment reference; `pspReference` is Adyen's transaction/request reference. `originalReference` is optional, described generically for modifications as the original payment-request reference, and absent from the shown `SECOND_CHARGEBACK` example. Do not require it for this event based on the generic row.
- The `amount` row says the payment amount is an object but also says HTTP POST currency and value are URL parameters. The example instead nests `currency` and `value` in JSON `amount`. The snapshot does not reconcile these representations or prove the delivery format. Its narrative separately says the disputed amount is deducted; the generic amount row calls this the payment amount, so the example's EUR 1000 must not be asserted as a guaranteed deduction amount.
- `success` is scoped to execution of the event code. The example's `SECOND_CHARGEBACK` and `success: "true"` accompany a declined defense; they are not a successful defense. The example also has a nonempty `reason` despite the schema describing `reason` as an explanation if `success=false`; the page does not resolve that mismatch. Its `additionalData` values are example data, not required fields.
- Under `200 Success`, the page says webhook events are accepted on the basis of HTTP status code. Receiver acceptance is separate from the issuing bank's decision and deduction. This page does not specify a response body or delivery, ordering, retry, deduplication or signature rules.

## Detail locators

- Raw lines 5–7: event identity and declined-defense/deduction meaning.
- Raw lines 11–27: request-body table, nested required flags, identities and success semantics.
- Raw lines 31–59: sample `SECOND_CHARGEBACK` item, nested amount, `additionalData`, reason and success.
- Raw lines 60–63: HTTP-status acceptance.

## Related

- [[adyen]] — company route.
- [[adyen-webhooks]] — Adyen webhook family and receipt concepts.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/SECOND_CHARGEBACK/2026-09-15|SECOND_CHARGEBACK reference, captured 2026-09-15]]
