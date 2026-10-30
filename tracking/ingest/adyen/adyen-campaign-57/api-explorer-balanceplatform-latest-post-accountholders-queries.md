# Fixed retrieval queries: api-explorer-balanceplatform-latest-post-accountholders

Canonical source: `source-adyen-api-explorer-balanceplatform-latest-post-accountholders` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders

## Q1

For `balanceplatform/latest/post/accountHolders`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The captured API v2 test-server page documents POST creation of an account holder linked by required `legalEntityId` to a distinct legal entity (raw lines 5–10, 14–17, 36). `balancePlatform` is required if credentials span multiple balance platforms (line 17). An optional capabilities map requests actions and levels, but `requested` is distinct from `allowed`, which reflects permission after verification (lines 18–21, 60–74). Contact-detail child fields are marked required within that optional object (lines 22–34); the page does not separately mark the entire body required. Authentication and permission errors appear as 401/403 (lines 138–159). Full field schema and request example are at lines 14–50.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** The 200 response schema provides required account-holder `id` and `legalEntityId` (lines 53–59, 104–105). The example has `status: active` while requested capabilities remain `allowed: false` and `verificationStatus: pending` (lines 223–264), so success does not prove capability approval. The status schema says suspension blocks payouts and closure is final (line 110). It describes verification deadlines (lines 112–115), primary balance account assignment only after first account creation (line 108), and metadata omission deletion only during an update (line 106). Error statuses 400/401/403/422/500 are documented (lines 118–215), but the 422/500 examples discuss payment instruments (lines 305–331), so they do not establish account-holder-specific failure rules. The only listed server is test `/bcl/v2` (lines 9–10); neither a live request nor completed verification, funds movement, payout or bank receipt is shown. The `latest` route does not establish present current version or merchant eligibility.
