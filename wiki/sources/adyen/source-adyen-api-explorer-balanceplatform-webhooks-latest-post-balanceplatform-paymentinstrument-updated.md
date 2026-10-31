---
title: "Adyen Balance Platform webhook: payment instrument updated"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.updated/2026-09-15.md"
tags: [adyen, balance-platform, webhooks, payment-instruments]
---

## Overview

Captured API Explorer `latest` POST reference for the incoming `balancePlatform.paymentInstrument.updated` webhook. Adyen says it sends the event when a payment instrument is successfully updated. The schema spans `card` and `bankAccount` instruments; a resource update or receiver acknowledgement does not establish an authorization, transfer, or funds outcome. See [[adyen]], [[adyen-issuing]], [[adyen-business-accounts]], and [[adyen-webhooks]].

## Key takeaways

- The table requires top-level `data`, `environment`, and `type`, but marks `data.paymentInstrument` optional. **If that object is present**, its table marks `balanceAccountId`, `id`, `issuingCountryCode`, and `type` required. `type` is `card` or `bankAccount`; the balance-account ID and payment-instrument ID identify distinct resources.
- The object has optional bank-account and card branches, description/reference/group IDs, and replacement IDs. Some branch descriptions say they are returned **when creating** a payment instrument, despite this page's update-event heading; do not treat those descriptions as a guarantee of branch presence in every update. The request example shows one suspended virtual card only.
- Optional `status` lists `active`, `inactive`, `suspended`, and `closed`; `closed` is permanently closed and cannot be undone. The text says creation defaults to `active` when unspecified, with card exceptions by form factor and issuing country (including inactive US physical cards). That creation-default wording is not a rule for interpreting a missing `status` in this update webhook. Optional `statusReason` includes listed reasons; for `other`, the source describes sending `statusComment`.
- `environment` is `test` or `live`; optional `timestamp` records when the event was queued. Any HTTP `2xx` accepts the webhook, separately from the instrument's state. The captured `latest` route does not itself establish a numbered API version, current availability, or delivery behavior.

## Detail locators

- Event purpose and type: raw lines 5–7 and 65–67.
- Requiredness, resource IDs, instrument branches, status and reasons: raw lines 9–34.
- Illustrative suspended-card payload: raw lines 36–69.
- Receiver acknowledgement: raw lines 70–78.

## Related

- [[adyen]]
- [[adyen-issuing]]
- [[adyen-business-accounts]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.paymentInstrument.updated/2026-09-15|Captured payment-instrument-updated webhook reference]]
