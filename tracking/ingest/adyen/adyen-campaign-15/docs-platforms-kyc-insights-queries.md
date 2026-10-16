# Fixed retrieval checks — KYC verification insights

Q1. What is this source's purpose and scope, and what must not be inferred?
- Expected: A 2026-09-15 Adyen for Platforms Customer Area KYC analytics guide for aggregate onboarding and verification trends on a balance platform. The Overview is selected-date account-holder status; Errors is historical affected-holder/error-category reporting. Individual holder detail belongs to its KYC summary/timeline. Do not infer current individual legal-entity verification, capability allowed/enabled status, product eligibility, causal improvement or successful payment/payout from dashboard counts.
- Raw locators: `raw/adyen/docs/platforms/kyc-insights/2026-09-15.md:15-47`, `:59-76`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-kyc-insights.md` → `[[adyen-platforms]]`.

Q2. What access, metric-grain and timing warnings govern interpretation?
- Expected: One of three listed Customer Area roles is required; sharing a filter view stays within users who have a required role. Dashboard refresh is daily at 3:00 AM CET. Holder count is grouped by creation date, not onboarding completion/error date; verified can change after more checks and Classic upgrades initially appear unsuccessful until verification. First-attempt success uses all starters as denominator, attempts count submissions regardless of success, median time spans first capability request to valid checks, and error categories overlap and persist after resolution. Filters are location, legal-entity type, integration type and date range; use cases are diagnostic, not individual finality.
- Raw locators: `raw/adyen/docs/platforms/kyc-insights/2026-09-15.md:27-47`, `:55-86`, `:88-134`.
- Canonical route: `wiki/sources/adyen/source-adyen-docs-platforms-kyc-insights.md` → `[[adyen-platforms]]`.
