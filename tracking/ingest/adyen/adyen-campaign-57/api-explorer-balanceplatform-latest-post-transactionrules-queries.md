# Fixed retrieval queries: api-explorer-balanceplatform-latest-post-transactionrules

Canonical source: `source-adyen-api-explorer-balanceplatform-latest-post-transactionrules` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/transactionRules

## Q1

For `balanceplatform/latest/post/transactionRules`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** It documents creating a transaction rule scoped through `entityKey` to a balance platform, payment-instrument group, account holder, balance account or payment instrument (raw lines 5–7, 20–22). The captured server is API v2 TEST (lines 9–10). Request properties marked required are `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` (lines 18–37, 116); no separate whole-body requiredness is shown. Velocity/maxUsage aggregation defaults to payment instrument and must be at or below the entity scope (line 17). Rolling/sliding intervals need duration, capped at 90 days; minutes/hours only for sliding (lines 23–31). Default outcome is hardBlock; scoreBased requires a bounded score and excludes bankTransfer; enforceSCA is authentication-only (lines 32, 113). Bypass requires `overridesRule` and empty restrictions (line 116), an exception to the general one-or-more condition wording (line 37). Transfer-pattern restrictions carry velocity/interval/matchingTransactions prerequisites (lines 68, 86, 89). 401/403 cover authentication/permissions (lines 369–390).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A supplied `startDate` creates an active rule; without one, startDate is set upon activation, while omitted `endDate` runs until inactivity (lines 19, 114–115). The 200 schema lists rule `id` as optional (line 252); four illustrative 200 responses show IDs in active and inactive configurations (lines 448–587), but do not make the ID universally required. Documented errors are 400, 401, 403, 422 and 500 (lines 349–447); 422/500 JSON examples mention payment instruments, not a transaction-rule-specific failure (lines 628–654). Request examples are illustrative (lines 118–237), and 200 creation does not prove any actual card authorization, authentication, bank-transfer decision, funds movement or propagation. The only displayed host is TEST `/bcl/v2`; `latest` in the URL alone does not prove current live version or eligibility (lines 1, 9–10). The interval table states CET fixed resets but UTC default timezone, and two day-of-week lists differ (lines 25, 30–31, 55), so exact reset behavior needs scoped verification.
