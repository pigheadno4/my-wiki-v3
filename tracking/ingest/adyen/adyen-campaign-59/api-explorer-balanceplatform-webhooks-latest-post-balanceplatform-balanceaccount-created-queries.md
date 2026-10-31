# api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccount-created fixed query answers

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created/2026-09-15.md` (SHA-256 `70c6c453e27699f807856127911270802ad51d9bcd0bd33de031faf669556423`). Canonical source route: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccount-created.md`. Canonical URL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccount.created

## Q1

The captured API Explorer POST page is the incoming `balancePlatform.balanceAccount.created` notification Adyen sends after successful balance-account creation (raw lines 5–7, 48). The request envelope requires `data`, `environment` (`test` or `live`), and `type`; `timestamp` is optional queue time. `data.balanceAccount` and `data.balancePlatform` are marked optional, while `accountHolderId` and balance-account `id` are required within a supplied `balanceAccount` object (raw lines 11–30). The example contains a test balance platform, account holder, balance account, EUR and active status (raw lines 32–50). The optional status defaults to active; default currency defaults to EUR and is immutable after creation (raw lines 18, 25).

## Q2

The reference establishes the event's creation trigger and schema, with a sample resource representation. It does not itself establish funding, verification, eligibility, payout or bank receipt. The only acknowledgment detail here is that any HTTP 2xx accepts the webhook and `notificationResponse` is optional (raw lines 51–59). The raw contains no event-specific ordering, retry, deduplication, signature, failure/reversal or final financial-state rule (full raw lines 1–59); those cannot be inferred from the test example. `latest` is a path label, not a numbered version in the captured page. The metadata omission/deletion warning is explicitly about an update, not the creation notification (raw line 21).
