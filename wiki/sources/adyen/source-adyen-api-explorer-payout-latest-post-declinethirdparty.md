---
title: "Adyen Payout API v68: Decline a submitted third-party payout"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payout/latest/post/declineThirdParty"
raw_files:
  - "adyen/api-explorer/Payout/latest/post/declineThirdParty/2026-09-15.md"
tags: [adyen, payouts, payout-api, cancellation, deprecated]
---

## Overview

This 2026-09-15 API Explorer snapshot documents POST `/declineThirdParty` on the displayed Payout v68 test server. It cancels a previously submitted payout in the legacy Payout API flow. The endpoint is deprecated and does not support new integrations; the page directs new integrations to Transfers API and existing Payout API users to their Adyen contact for migration. [[adyen]] [[adyen-payouts]]

## Key takeaways

- The request requires `merchantAccount` and `originalReference`, explicitly the PSP reference returned by `/submitThirdParty`; optional `additionalData` may be required for a particular payout request (raw lines 30–47). The original submission reference is distinct from the reference returned for this decline response.
- The 200 response requires a `pspReference` associated with this response and a `response` string. The schema says success can be `payout-confirm-received` or `payout-decline-received`, although this endpoint is the decline operation. Its decline example puts brackets around `[payout-decline-received]`; preserve that schema/example discrepancy rather than treating either exact spelling as a universal value (raw lines 50–58, 130–140).
- A received decline response is acknowledgement of the request, not evidence of a final payout outcome, recipient credit or reversal of already moved funds. The page states cancellation of a previously submitted payout but gives no timing window, payout-state eligibility rule, final event or bank-receipt example (raw lines 23–25, 48–58).
- Error headings list 400 request reading/understanding, 401 authentication, 403 insufficient permissions, 422 validation and 500 server processing. The page names no specific permission role; the 400 code shown is a generic example (raw lines 61–152).

## Detail locators

- Deprecation, migration routes, operation purpose, confirm counterpart and test server: raw lines 5–28.
- Request fields and example: raw lines 30–47. Required 200 fields and success/error response wording: raw lines 48–58; bracketed decline example: raw lines 130–140.
- Error categories and response fields: raw lines 61–128; generic 400 example: raw lines 142–152.

## Related

- [[adyen-payouts]] — legacy Payout API versus newer Payout Service context and reciprocal route.
- [[source-adyen-docs-online-payments-online-payouts-payouts-to-bank-accounts-and-wallets]] — separate staged-payout reviewer flow.
- [[source-adyen-docs-online-payments-online-payouts-payout-webhook]] — separate payout lifecycle event guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Payout/latest/post/declineThirdParty/2026-09-15|Payout API Explorer POST declineThirdParty, captured 2026-09-15]]
