# Fixed retrieval queries: api-explorer-management-latest-overview

Canonical source: `source-adyen-api-explorer-management-latest-overview` — https://docs.adyen.com/api-explorer/Management/latest/overview

## Q1

For `Management/latest/overview`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** This captured Management API v3 page orients company and merchant account, store and payment-terminal management (raw lines 5–7). Each request uses an API key in `X-API-Key`; live calls need a new key from the live Customer Area (lines 9–13). Version 3 is in the URL, with test and live bases shown (lines 15–25, 31–32). The endpoint table catalogs company, merchant, credential, user, webhook, payment-method, payout-setting, split-configuration, store, terminal and donation paths (lines 34–178). This is a Management API catalog, distinct from Balance Platform Configuration API account-holder/balance-account operations. The overview does not state operation-level required fields or roles, so the catalog alone cannot supply them.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** The page has no operation response or error schemas and no request/response examples; after endpoint summaries it ends at line 178. The table includes POST `/merchants/{merchantId}/activate` as a **request** to activate and POST merchant payment-method settings as a **request** for a payment method (lines 94, 107), not proof of approval. It lists DELETE routes for allowed origins, webhooks, payout settings, split configurations and donation campaigns (lines 54, 81, 102, 115, 123, 154, 175), but does not define their operation-specific effects. It also lists terminal reassignment/action routes (lines 166–172) without completion or device-state evidence. The test URL, stated live URL and live-key distinction are explicit (lines 13–25, 31–32); the `latest` route does not itself prove current version, authorization, merchant eligibility, payment, payout or funds movement.
