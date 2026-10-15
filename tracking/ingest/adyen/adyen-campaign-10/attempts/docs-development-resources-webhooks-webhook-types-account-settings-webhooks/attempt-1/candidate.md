---
title: "Account settings webhooks | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/webhooks/webhook-types/account-settings-webhooks"
raw_files:
  - "adyen/docs/development-resources/webhooks/webhook-types/account-settings-webhooks/2026-09-15.md"
tags: [adyen, webhooks, account-settings, merchant-accounts, stores]
---

## Overview

This Adyen account-settings webhook guide was collected on 2026-09-15; its raw metadata says last modified 2023-05-26. It describes notifications for changes to company-account, merchant-account, and store settings, such as account or store status, payout blocking, merchant name, settlement currency, and merchant category code. These notifications report settings changes; a `pspReference` here identifies the change and is explicitly not a payment PSP reference. The page does not establish a payment, payout, settlement, or refund outcome. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- To receive this webhook type, expose a server endpoint, accept and verify the HMAC signature, and acknowledge every notification with a successful HTTP status code within 10 seconds. The Customer Area setup selects **Account settings details** and JSON. Configure it again in the live Customer Area; if using HMAC-signed webhooks, generate and verify a new live HMAC key. See raw `## Set up account settings webhooks`.
- The documented triggers are changes to `accountStatus`, `blockPayout`, `merchantName`, `settlementCurrency`, or `merchantCategoryCode` for the stated company, merchant, or store account scope. For `accountStatus`, the raw lists lifecycle states and states that closing a merchant account also closes underlying stores. Consult the full field table for the state-specific meanings; a status notification itself is not evidence of a successful financial transaction.
- The payload table gives the changed entity, execution time and actor, field name, new value, optional old value, and a change-specific `NO_PSP_REF`-prefixed reference. Its `entityKey` description also mentions a user-level format, while the trigger introduction names company, merchant, and store fields; the page does not describe a separate user-change trigger. See raw `## Structure of account settings webhooks`.
- SOAP is an alternative notification format with field exclusion in the WSDL. Excluding a field stops new webhooks for that field, but already-pending unsent events are still processed and retain the excluded field. See raw `### Exclude account fields from SOAP webhooks`.

## Detail locators

- `## Set up account settings webhooks`: receiver, HMAC, 10-second acknowledgment, Customer Area format, and separate live setup.
- `### Exclude account fields from SOAP webhooks`: test/live WSDL routes and the pending-event effect of excluding a field.
- `## Events that trigger account settings webhooks`: exact account fields, status values, and status meanings.
- `## Structure of account settings webhooks`: field presence and payload semantics; `oldValue` is not included by default.
- `## Examples`: illustrative account status, payout-block, name, and settlement-currency change payloads; example timestamps are not current events.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/development-resources/webhooks/webhook-types/account-settings-webhooks/2026-09-15|Adyen account settings webhooks, 2026-09-15]]
