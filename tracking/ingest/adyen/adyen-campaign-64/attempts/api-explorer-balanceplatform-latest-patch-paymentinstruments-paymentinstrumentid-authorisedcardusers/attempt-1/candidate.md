---
title: "Adyen Balance Platform API v2: PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02.md"
tags: [adyen, balance-platform, issuing, cards, authorised-users, api]
---

## Overview

This 2026-11-02 Balance Platform API v2 reference describes `PATCH /paymentInstruments/{paymentInstrumentId}/authorisedCardUsers` to update the authorized-user list for a card. The documented request **replaces all existing authorized users** for that card. The page shows only the TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not independent proof of live availability. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- `paymentInstrumentId` is a required **path** parameter. The request-body table lists `legalEntityIds`, an array of the authorized card users' legal-entity IDs linked to that payment instrument, as **optional**. The page does not separately declare whether the entire body is required. Its JSON example supplies two IDs, but no requirement that two be sent follows from that example.
- The prose says the request replaces the whole existing authorized-user list, so a caller must treat supplied IDs as a replacement set rather than an additive change. The page does not specify what an omitted `legalEntityIds` field or an empty array does; neither can safely be equated with a documented clear operation.
- The success response is 204 with no documented response body. It reports success of this user-list update, not card creation, activation, legal-entity verification, a card authorization, capture or settlement. No propagation timing, asynchronous outcome or idempotency behavior is specified here.
- Errors listed are 400 bad request, 401 unauthorized, 403 forbidden and 422 validation. The 400 example says an instrument lacks a linked legal-entity reference and suggests POST; the 403 example says a card partner is not allowed yet. A 422 **example** says the request must have at most 10 legal-entity references, but the request schema states no maximum. Treat these example details as illustrative, not general eligibility or a complete numeric contract.

## Detail locators

- Replacement behavior, TEST server, path and body table: pinned raw lines 5–25.
- Request JSON and 204 success: pinned raw lines 27–41.
- Error schemas and 400/401/403/422 examples: pinned raw lines 44–173.

## Related

- [[adyen-issuing]] — issued-card and legal-entity context.
- [[source-adyen-docs-issuing-create-cards]] — separate card-creation guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/paymentInstruments/(paymentInstrumentId)/authorisedCardUsers/2026-11-02|Authorized card users PATCH snapshot]]