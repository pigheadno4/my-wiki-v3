# Fixed retrieval answers: api-explorer-balanceplatform-latest-get-cardorders

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-get-cardorders.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/get/cardorders

## Q1: For `balanceplatform/latest/get/cardorders`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API v2 test-server reference defines `GET /cardorders` as a paginated card-order list. The card-order object has its own `id` and may expose a card-manufacturing-profile ID, service center, dates and status. All query filters are optional: `limit` defaults to 10, `offset` to 0; date filters require ISO 8601 and `serviceCenter` is case-sensitive. Authentication and permission failures are listed, but a named role is absent. No request body or card-creation prerequisite is established. [Raw lines 5–27, 31–47, 50–71.]

## Q2: What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

A 200 response describes optional `cardOrders` plus required `hasNext` and `hasPrevious` flags. `endDate` reflects manual closure, while the text says orders automatically close by the end of their creation day; `lockDate` and `closedDate` mark processing start/end. Listed failures are 401, 403, 422 and 500. The schema says `Open`/`Closed`, but the success example has lowercase `closed`. The generic 422/500 examples describe payment-instrument operations, not a demonstrated card-order error. The captured server is test `/bcl/v2`, despite `latest` in the documentation URL. This lookup proves no manufacturing completion, delivery, verification, approval, live availability, payment result or funds movement. [Raw lines 9–10, 31–47, 50–127, 129–204.]
