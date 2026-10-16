# Fixed retrieval queries — Adyen platform capabilities

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does this capabilities guide describe, and what does a capability listing not prove?

**Answer:** It describes Adyen for Platforms account-holder action permissions, product-specific capability names, verification statuses, and the `requested`, `allowed`, `enabled` settings. A default or additional request can trigger KYC; a listed/requested capability is not proof that a user passed verification, that access is enabled, or that any payment, transfer or payout occurred. This 2024-modified page was captured 2026-09-15. Canonical route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-verification-overview-capabilities]]; the coordinator must publish the currently absent provider-index concept link. Raw: `raw/adyen/docs/platforms/verification-overview/capabilities/2026-09-15.md`, lines 5–27 and 111–122.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How do requested, allowed, enabled and verification status interact, including product gates and rechecks?

**Answer:** `requested` records a default or explicit request, which may require KYC. `allowed` is Adyen’s permission; `enabled` is the access setting the platform can turn on or off without itself triggering verification. Use requires both allowed and enabled. Initial `pending` is requested=true/allowed=false, but an already allowed capability may stay allowed=true while changed data is checked; `invalid` generally blocks use but can temporarily coexist with allowed=true after previously successful verification when data changes or is missing, with remediation due by an unspecified deadline. `valid` allows and `rejected` is final/blocked. Core capabilities distinguish payment receipt, split funds and balance/verified-instrument transfers; business-account, issuing and Capital sets depend on the business offering those products. Issuing levels use per-card/day thresholds; from LEM API v3, issuing transfer-instrument verification is per instrument. Raw lines 19–23, 29–36, 38–93, 95–122. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-verification-overview-capabilities]].
