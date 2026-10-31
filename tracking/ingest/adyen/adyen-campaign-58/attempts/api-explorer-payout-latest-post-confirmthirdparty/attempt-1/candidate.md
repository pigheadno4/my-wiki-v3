---
title: "Adyen Payout API: POST /confirmThirdParty"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/confirmThirdParty"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/confirmThirdParty/2026-09-15.md"
tags: [adyen, payout-api, legacy-payouts, confirmation]
---

## Overview

This 2026-09-15 API Explorer capture documents `POST /confirmThirdParty` on the listed TEST Payout v68 server. It confirms a payout previously submitted through `/submitThirdParty`; `/declineThirdParty` is the cancellation route. The endpoint is deprecated and no longer supports new integrations. Adyen directs new integrations to the Transfers API and existing Payout API users to their Adyen contact for migration information. See [[adyen]] and [[adyen-payouts]].

## Key takeaways

- Required request fields are `merchantAccount` and `originalReference`. The latter is the PSP reference returned by the earlier `/submitThirdParty` response, not the PSP reference newly returned by this confirmation request. Optional `additionalData` may be required for a particular payout request; the page gives no general condition.
- A 200 response says the request succeeded and requires `pspReference` and `response`. The response description says success can be `payout-confirm-received` or `payout-decline-received`; error returns an informational message. The confirmation example wraps `payout-confirm-received` in square brackets, unlike the unbracketed value in the schema description. Treat that as an example/description discrepancy, not a literal-value guarantee.
- `payout-confirm-received` is confirmation receipt, not proof that money was paid out or received by the recipient. This page contains no final payout or bank-delivery status, no 202 response, and no stated named reviewer role or credential. It lists 401 authentication and 403 insufficient permissions. The separate legacy payout workflow sources govern operational review and payout-outcome tracking.
- Error classes are 400 request reading/understanding, 401 authentication, 403 permissions, 422 validation, and 500 server processing. The generic 400 example does not establish a payout-specific recovery action.

## Detail locators

- Deprecation, migration direction, operation and TEST v68 server: raw lines 5–28.
- Request fields and example: raw lines 30–47.
- 200 response and received-label description: raw lines 48–58; error schemas: 61–128.
- Bracketed confirmation-response example and generic 400 example: raw lines 130–152.

## Related

- [[adyen-payouts]] — legacy payout scope and separate Payout Service/Transfers API routes.
- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — legacy payout outcome route.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/confirmThirdParty/2026-09-15|Payout API Explorer POST /confirmThirdParty capture]]
