# C20 approval and cancellation retrieval checks

## Q1 — Who can approve or cancel, and what happens to the transfer?

Route: `wiki/index.md` → `wiki/adyen-index.md` (Business Accounts catalog and `[[adyen-business-accounts]]`) → `wiki/concepts/adyen-business-accounts.md` → candidate `wiki/sources/adyen/source-adyen-docs-business-accounts-send-funds-approve-cancel-transfers.md` → `raw/adyen/docs/business-accounts/send-funds/approve-cancel-transfers/2026-09-15.md`.

The initiator requests extra review through `review` in POST `/transfers`; the request remains pending until a reviewer decides (raw lines 38–48). The web-service API key needs the TransferService Approval role and Transfer Webhooks subscription is listed (lines 23–30). POST `/transfers/approve` or `/transfers/cancel` takes one to 500 transfer IDs in the body `transferIds` array (lines 52–58, 272–278). Approval authorizes Adyen to continue processing; cancellation or 30 days without action makes the pending request fail and prevents further processing (lines 44–50). The IDs are transfer resources, distinct from source balance-account and recipient bank-account identities.

## Q2 — What SCA and state/failure boundaries must be preserved?

If SCA is required, authenticate the initiating user or approving reviewer. For SCA at approval, set `review.scaOnApproval` true on the initial POST `/transfers` request (raw lines 261–270). The approve/cancel calls describe HTTP 200 success (lines 259, 479), but review status comes from transfer webhooks: created `received/pending` with one required approval (lines 498–506), updated `authorised/approved` (574–582), or `cancelled/unknown` (664–671). These states do not prove final settlement or bank receipt. The guide states a 30-day failure deadline (48, 487–489) without an expiry payload example. Its introductory event list omits approved updates (485–494), but the later approved tab explicitly includes them (574–582). TEST SDK snippets use idempotency keys (e.g. 95, 313) without stating a replay guarantee. Page metadata is 2020-modified and captured in 2026; use it as historical documentation, not current eligibility or live-operation proof.
