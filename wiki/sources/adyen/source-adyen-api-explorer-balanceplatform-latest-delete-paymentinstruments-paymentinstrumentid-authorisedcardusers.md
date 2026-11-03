---
title: "Adyen Balance Platform API v2: DELETE card authorized-user list"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md"
tags: [adyen, balance-platform, issuing, cards, api]
---

## Overview

This 2026-11-02 Balance Platform API reference describes deleting the list of authorized users assigned to a card via `DELETE /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers`. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not proof of current live availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The only listed input is required string path `paymentInstrumentId`, identifying the payment instrument whose card-user list is targeted. The path names a payment instrument, not an account holder, balance account, individual user ID, or card transaction. The page lists no request body, query parameter, or individual authorized-user selection.
- The documented success is HTTP 204, “Successful operation,” with no success response body shown. This supports deletion of the assigned authorized-user list as the operation's stated purpose; it does not prove card cancellation, payment-instrument deletion, removal of a single named user, immediate propagation to all card rails, or any authorization/capture/settlement outcome. The page gives no restoration, reversal, or timing rule.
- Documented failures are 401 Unauthorized and 403 Forbidden. The 403 sample detail says “Not allowed for card partner yet”; it is one example, not a universal eligibility rule or a specific required caller role. This reference does not state an idempotency key, retry contract, version conflict, or asynchronous result mechanism.

## Detail locators

- Purpose, TEST server and required payment-instrument path ID: pinned raw lines 5–17.
- 204 success and 401/403 error response schemas: pinned raw lines 19–60.
- 401/403 example payloads: pinned raw lines 62–87.

## Related

- [[adyen-issuing]] — card/payment-instrument context.
- [[adyen-platforms]] — platform resource context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02|Balance Platform DELETE authorized card users snapshot]]