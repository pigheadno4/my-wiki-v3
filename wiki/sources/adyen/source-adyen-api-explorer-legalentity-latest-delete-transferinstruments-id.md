---
title: "Adyen Legal Entity Management API v4: Delete a transfer instrument"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/legalentity/latest/delete/transferInstruments/(id)"
raw_files:
  - "adyen/api-explorer/legalentity/latest/delete/transferInstruments/(id)/2026-11-03.md"
tags: [adyen, legal-entity-management, platforms, transfer-instruments, api]
---

## Overview

Captured Legal Entity Management API v4 reference for `DELETE /transferInstruments/{id}` at the TEST server `https://kyc-test.adyen.com/lem/v4`. It deletes the transfer-instrument resource identified by required path `id`. The separate [[source-adyen-docs-platforms-manage-transfer-instruments|Platforms guide]] describes this resource as an external bank-account representation and states the deletion's downstream payout effect. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The required string `id` is the transfer-instrument identifier, not the legal-entity, account-holder, balance-account or payout ID. The reference lists no request body, query parameter, conditional input or idempotency key.
- The documented success response is 204 with an instruction to inspect the actual response code; no success body, replacement resource or payout state is returned. The separate Platforms guide says deletion cannot be undone and future scheduled or on-demand payouts referencing the deleted ID will fail. If the same bank account is needed again, the guide directs creation of a new transfer instrument (guide raw line 986). The DELETE result is resource deletion, not reversal of a payout already sent or proof of bank receipt.
- Captured limits are 700 requests per five seconds in live, 200 per five seconds in test, and five failed requests per ten seconds. These are documented limits in the pinned snapshot, not evidence of present eligibility or access to a live account.
- The page lists 400 request, 401 authentication, 403 insufficient permission, 422 validation and 500 server errors. Each error schema marks `errorCode`, `errorType`, `message`, `pspReference` and HTTP `status` optional; `pspReference` is labeled a payment PSP reference in this generic schema and is not a documented deletion result. No particular credential role, deletion propagation timing, asynchronous review/approval, version conflict or recovery behavior is specified here.

## Detail locators

- Purpose, rate limits, TEST v4 server and path ID: pinned raw lines 5–25.
- Bodyless 204 response and generic error schemas: pinned raw lines 27–95. The pinned page has no response examples.
- Separate Platforms guide's irreversible deletion and future payout failure: guide raw lines 838–844 and 986.

## Related

- [[adyen-platforms]] — platform and resource context.
- [[source-adyen-docs-platforms-manage-transfer-instruments]] — resource ownership, irreversible deletion and payout-reference effect.
- [[source-adyen-api-explorer-legalentity-latest-post-transferinstruments]] — separate creation of a new transfer instrument.

## Raw Sources

- [[raw/adyen/api-explorer/legalentity/latest/delete/transferInstruments/(id)/2026-11-03|Captured DELETE /transferInstruments/{id} API reference (2026-11-03)]]