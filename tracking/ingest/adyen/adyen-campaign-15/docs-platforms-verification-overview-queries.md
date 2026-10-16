# Fixed queries — docs-platforms-verification-overview

## Q1 — purpose, scope, and non-inference

**Query:** What is Adyen's Platforms verification process, and does account-holder creation or a capability request mean the user may process payments or receive payouts?

**Answer:** Adyen verifies platform users as KYC before allowing the capabilities needed for actions such as processing payments, payout or financial products (raw lines 15–23). Default capabilities are requested on account-holder onboarding; additional requests can require checks, and the user's **specific capability settings** determine allowed actions (lines 30–40). Creation, request, sample flags or an active deadline does not prove an allowed capability, account compliance or any payment/payout execution. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-verification-overview]] → pinned raw.

## Q2 — central capability, prerequisites, and warnings

**Query:** When do checks recur, how do deadlines and asynchronous statuses affect allowed use, and what should a platform inspect?

**Answer:** Data changes re-trigger checks; after a failed check Adyen may grant a deadline during which previously allowed capabilities continue, then disallow unresolved ones. Account-holder capability webhooks do not fire for legal-entity data changes alone (raw lines 44–52). Required or proactive review checks legal-entity/associated-entity data; users must both confirm data and resolve errors before review finalizes (lines 56–64, 191–208). Deadlines are LEM API v3/v4 only; the 30/60-day table is standard but can be shortened or removed, and documents must be submitted **and verified** by the final date (lines 66–101). Multiple checks can yield errors while overall status remains `pending`; await completion and inspect the current account-holder capability settings, deadline, errors and webhook outcomes instead of reading `requested`, `enabled`, `allowed` or `verificationStatus` as interchangeable (lines 103–173). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-verification-overview]] → pinned raw.
