# Retrieval checks — docs-marketplaces-identify-account-holder-risk

Q1. What does Marketplace Score do, and which enablement/access scope does this snapshot state?

A1. Score analyzes account-holder/sub-merchant/seller verification and transactions to flag possible risk, score users and link accounts for case review (raw lines 19–23, 31–33, 45–66). The page says default enablement applies to platforms integrated after October 2024 and forecasts all-merchants enablement from October 31, 2026; the latter is future-facing at capture and the 2023 metadata conflicts with 2025/2026 body dates (raw lines 5–11, 27–29, 76–79). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-identify-account-holder-risk]] → [[raw/adyen/docs/marketplaces/identify-account-holder-risk/2026-09-15]].

Q2. Does a risk signal or score 100 automatically stop payouts or prove fraud, and is device-data inspection generally available?

A2. No. Adyen says a signal alone does not disable payouts/processing; the marketplace reviews cases or sets automated action (raw lines 31–41). A score of 100 is high possibility, not confirmed fraud, and itself triggers no automatic action (raw line 60). Device/session collection is marked limited availability, restricted in the described pilot to interested Score customers using hosted onboarding or components; broader rollout is only a stated plan (raw lines 76–91). Route: [[index]] → [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-marketplaces-identify-account-holder-risk]] → [[raw/adyen/docs/marketplaces/identify-account-holder-risk/2026-09-15]].
