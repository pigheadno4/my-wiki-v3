# Fixed retrieval answers: api-explorer-transfers-latest-post-transfers-cancel

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-post-transfers-cancel.md` — https://docs.adyen.com/api-explorer/transfers/latest/post/transfers/cancel

## Q1: For `transfers/latest/post/transfers/cancel`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Transfers API v4 `POST /transfers/cancel` initiates cancellation of listed **transfers that triggered additional review**. It requires the `TransferService Approve` credential role and required account-holder capabilities, with Adyen-contact permission setup. `Idempotency-Key` is an optional header capped at 64 characters; UUID is recommended. The table marks request-body `transferIds` optional, though the example supplies two IDs; it does not separately establish body requiredness or a maximum batch size. [Raw lines 5–31, 33–43.]

## Q2: What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 passage points to request status and the example is an empty object; Adyen says cancel-request **outcome** arrives through webhooks. Errors listed are 401, 403, 422 and 500 with generic schemas, including optional routing details. The test server is `/btl/v4` despite the `latest` URL. The page does not show a cancellation outcome, webhook schema, eligibility beyond additional review, reversal of a booked transfer, bank receipt, verification approval, live availability or any actual funds movement. [Raw lines 7, 17–18, 44–156.]
