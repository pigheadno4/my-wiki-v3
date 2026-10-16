# Fixed retrieval checks — docs-industries-peak-season-afp

## Q1 — Purpose, scope, and what not to infer

**Query:** What is the Adyen for Platforms peak-season page for, and what must not be inferred?

**Answer:** It adds platform/marketplace-specific readiness advice to the broader peak-season guide, focused on chargeback split logic and outstanding KYC reviews for users. It does not establish a particular platform's current configuration or eligibility, identify merchant of record or funds owner, define transfers, show payout execution or bank receipt, or certify KYC compliance. It was last modified and captured 2026-09-15. Evidence: raw lines 11, 15–21, 23–45. Canonical route: [[adyen-index]] → [[adyen-peak-season-readiness]] → ## Sources → [[source-adyen-docs-industries-peak-season-afp]] → [[raw/adyen/docs/industries/peak-season/afp/2026-09-15]].

## Q2 — Central capability, prerequisites, and warnings

**Query:** What platform-specific chargeback and verification conditions should be checked before peak season?

**Answer:** Without chargeback logic, the full disputed amount is withdrawn from the platform/marketplace liable balance account. Configurable alternatives put the amount on the platform's or user's liable balance account or split it according to the original payment; payment-specific splits override balance-platform-level splits. The page recommends split-configuration profiles for platforms. Onboarded users can require re-verification, such as for expiring ID; they retain needed capabilities during an initial response period but may lose capabilities and have payouts blocked if they miss the deadline. Monitor `balancePlatform.accountHolder.updated` webhook verification errors and ask the account holder to fix them; `3_10` is one example. These are conditional operational rules, not proof of actual KYC clearance, payout, funds ownership or an individual chargeback posting. Evidence: raw lines 23–45. Canonical route: [[adyen-index]] → [[adyen-peak-season-readiness]] → ## Sources → [[source-adyen-docs-industries-peak-season-afp]] → [[raw/adyen/docs/industries/peak-season/afp/2026-09-15]].
