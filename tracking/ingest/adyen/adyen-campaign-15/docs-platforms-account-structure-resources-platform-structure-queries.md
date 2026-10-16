# Fixed queries — docs-platforms-account-structure-resources-platform-structure

## Q1 — purpose, scope, and non-inference

**Query:** What account model does Adyen's “Platform account structure” page describe, and does it decide the seller or merchant of record?

**Answer:** It describes a conditional Adyen for Platforms **payment-facilitator** setup and an Example Travel LLC illustration. The page says users contract with payment methods while the platform relates to its users; it distinguishes platform-owned and user-owned resources (raw lines 23–41). Payment-facilitator onboarding is stated for the listed registered-facilitator, individual in-person-user or high-risk-MCC cases, not all platforms (lines 25–33). These relationships do not alone determine a particular transaction's legal seller/MOR, current account eligibility or any financial outcome. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-account-structure-resources-platform-structure]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** How do the platform and user resources connect, and what does the illustrated fund flow show?

**Answer:** A platform registered and acquiring in a region needs a regional balance platform and merchant account; the example has company/merchant/balance-platform resources plus a platform liable account holder/balance account and legal entity (raw lines 35–60). Each user has stores tied to merchant accounts, an account holder per operating country, base-currency balance account(s), verified transfer instrument(s) for payout, and country legal-entity/business-line records (lines 62–78). The example routes a customer payment via store and merchant account, settles/splits balances between platform liable and user accounts, holds the user portion and describes later payout to the user's verified bank instrument (lines 86–94). This is illustrative architecture, not a role/credential guide, KYC approval, configured split, live payment or bank receipt. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-account-structure-resources-platform-structure]] → pinned raw.
