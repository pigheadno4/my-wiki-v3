---
title: "Adyen Notification latest: BENEFICIARY_SETUP"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Notification/latest/post/BENEFICIARY_SETUP"
raw_files:
  - "adyen/api-explorer/Notification/latest/post/BENEFICIARY_SETUP/2026-09-15.md"
tags: [adyen, classic-platforms, notifications, beneficiary-setup]
---

## Overview

This 2026-09-15 snapshot of the API Explorer `Notification/latest` `POST /BENEFICIARY_SETUP` reference describes an incoming Adyen notification for a Classic benefactor/beneficiary relationship setup. It says Adyen sends the notification when the relationship is created. The payload also supplies `content.invalidFields` to identify fields that caused the Setup Beneficiary request to fail; an empty list means that request succeeded. Read the event's fields rather than treating the heading alone as proof of a successful setup. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Required top-level notification fields are `eventDate`, `eventType`, `executingUserKey`, `live`, and `pspReference`. `pspReference` identifies the request from which the notification originates; `live` distinguishes live from test origin. `content` and `error` are optional in this table.
- Optional `content` fields identify source benefactor account and account holder, destination beneficiary account and account holder, merchant reference, `invalidFields`, and `transferDate`. The table describes `transferDate` as the date the beneficiary was set up and funds transferred; its presence in the example does not independently establish a completed transfer for another event.
- The 200 response body documents optional `notificationResponse` set to `[accepted]` to acknowledge receipt. This receiver response is separate from whether the underlying Setup Beneficiary request succeeded. The example contains a nonempty `invalidFields` array and an `error` object, so it is not evidence of successful setup.

## Detail locators

- Request body and requiredness: raw `## Parameters` → `### Request body`, lines 9–32; account/holder identifiers and error detail, lines 14–27.
- Illustrative `beneficiarySetup` JSON: raw `## Request examples`, lines 34–68.
- Receiver response: raw `## Responses` → `### 200 Success`, lines 69–77.

## Related

- [[adyen-classic-platforms]] — Classic account and holder context.
- [[adyen-webhooks]] — general webhook context; this event's response is documented in the raw reference.
- [[source-adyen-api-explorer-fund-latest-post-setupbeneficiary]] — separate Fund API setup request reference; its request/response contract is distinct from this incoming notification.

## Raw Sources

- [[raw/adyen/api-explorer/Notification/latest/post/BENEFICIARY_SETUP/2026-09-15|API Explorer BENEFICIARY_SETUP snapshot (2026-09-15)]]
