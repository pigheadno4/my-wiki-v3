# Fixed queries — docs-platforms-payout-descriptions

## Q1 — purpose, scope, and non-inference

**Query:** What can a Platforms payout description control, and does submitted text prove bank-statement display or delivery?

**Answer:** A transfer or scheduled payout can carry `description` and `referenceForBeneficiary`; originator name and identifiers are other descriptor components (raw lines 15–35). Adyen passes the submitted data through the clearing network, whose capabilities and limits affect transmission, while the beneficiary bank decides how much to show (lines 23–27). A configured or accepted descriptor does not prove statement visibility, payout booking, beneficiary bank credit, legal ownership or live eligibility. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-payout-descriptions]] → [[raw/adyen/docs/platforms/payout-descriptions/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** How do scheduled and on-demand descriptors differ, and which precedence and route-specific limits matter?

**Answer:** Managed/custom scheduled payouts can use placeholders in `description` or `referenceForBeneficiary`, including account-holder/balance-account data and generated transfer references; `$shortTransferReference` is custom-scheduled-only. An Adyen contact can set platform-wide values, while custom scheduled balance-account-level settings take precedence over platform-level settings (raw lines 37–69). On-demand Transfers API and Cashout requests use static strings; placeholders are unsupported (lines 71–76). Originator name can be Adyen's or the platform's legal-entity name by region, and changing the latter to a DBA requires onboarding/LEM input plus Adyen-contact setup (lines 29–35). Country, currency and priority tables distinguish accepted characters/maxima from visible statement lengths; some accepted text has zero visibility, including PLN regular and SGD wire rows (lines 78–255). The statement that short references are provided by all banks must be read with those limits and beneficiary-bank display discretion (lines 62–67, 23–27). This page states no Transfer API role, approval, test/live setting or completed delivery. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-payout-descriptions]] → [[raw/adyen/docs/platforms/payout-descriptions/2026-09-15|pinned raw]].
