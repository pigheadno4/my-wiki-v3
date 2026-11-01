# C61 fixed-query answers — api-explorer-a2aissuer-api-latest-post-payments-confirm

Pinned raw: `raw/adyen/api-explorer/a2aissuer-api/latest/post/payments/confirm/2026-09-15.md`. Canonical retrieval route: [[source-adyen-api-explorer-a2aissuer-api-latest-post-payments-confirm]]; URL: https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/confirm

## Q1

This is A2A Issuer API v1 `POST /payments/confirm` on listed test/live balance-platform hosts (raw lines 5–25). Adyen says confirmation uses two calls: first initiates SCA and returns `WWW-Authenticate`, then the user completes the challenge and the second call includes an updated header; its response guides the user to a success/failure page (7–16). The header table marks `WWW-Authenticate` optional (28–31), while the request body requires source `balanceAccountId` and the payment-details `token` (34–48). HTTP 200 returns required `links`; cancel and success branches are optional, with `href` required inside a present branch (49–61). The 200 example shows only `links.success.href` (139–152). Listed error categories are 400, 401, 422 and 500 (64–138); examples include SCA needed under 401 and invalid challenge/token, expired/final-state payment, missing fields and unknown balance account under 422 (168–266).

## Q2

HTTP 200 says the confirm request succeeded and provides a redirect link structure, but does not itself prove a booked debit, final payment settlement or recipient-bank receipt (raw lines 49–61, 139–152). The first-call SCA challenge and second-call response are distinct stages (7–14). The generic 401 description says invalid credential or permissions, whereas its example says user SCA is needed; neither alone defines all 401 cases (83–99, 168–180). Expired token and final-state payment examples appear under 422, without stating the payment's actual terminal outcome (195–226). No idempotency/retry-safety or financial-finality rule is stated in the full 301-line raw. Retrieval route: [[source-adyen-api-explorer-a2aissuer-api-latest-post-payments-confirm]]; https://docs.adyen.com/api-explorer/a2aissuer-api/latest/post/payments/confirm
