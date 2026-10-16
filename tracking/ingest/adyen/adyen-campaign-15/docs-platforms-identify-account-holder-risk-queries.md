# Fixed retrieval queries — Adyen Score platform risk

## Q1 — Purpose, scope, and what it does not infer

**Question:** What does this Score page describe, and why is a signal or score not fraud proof?

**Answer:** It introduces Score for platform account holders, sub-merchants and sellers: verification/transaction-data analysis produces potential-risk signals, weighted 0–100 scores and linked-account groupings. A 100 score does not confirm fraud and, by itself, causes no automatic action. A signal alone does not disable Adyen processing or payouts. The 2026-09-15 capture has 2023 last-modified metadata despite references to 2025/2026 events; its future rollout is not confirmed current enablement. Canonical route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-identify-account-holder-risk]]. Raw: `raw/adyen/docs/platforms/identify-account-holder-risk/2026-09-15.md`, lines 5–35 and 45–74.

## Q2 — Central capability, prerequisites, and warnings

**Question:** What does Score surface, who chooses mitigation, and what limits its device-data feature?

**Answer:** Score surfaces risk-rule/model signals and case information. The platform reviews cases and chooses controls, or configures automation, including payout disablement, account suspension or stricter KYC; Adyen says it does not automatically stop processing/payouts upon signal detection. Default KYC signals are described as real-time and transactional signals daily; custom high-risk-list and rule signals are real-time. Linked users can share propagated signals and a group score, which remains an indicator. The page says Score default-enablement applies to post-October-2024 integrations and forecasts broader enablement from October 31, 2026, but this dated capture cannot prove any merchant’s current access. Device/behavior inspection is a limited pilot for interested Score customers using hosted onboarding or components; API-only customers are told to contact an account manager about an SDK pilot. Expansion is only planned in the page. Raw lines 21–29, 31–62, 64–91. Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-identify-account-holder-risk]].
