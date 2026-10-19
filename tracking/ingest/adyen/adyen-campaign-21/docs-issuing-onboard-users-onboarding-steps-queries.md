# C21 worker retrieval checks: docs-issuing-onboard-users-onboarding-steps

Q1. What does this onboarding-steps capture provide, and what selection is already made?
Answer: It is a verification-requirements selector intended to identify required user information and submission method (raw lines 19–21). The current selection is Hosted onboarding, version 4 (lines 30–33). Available filters include onboarding type, version, location and legal-entity/arrangement type (lines 23–28). Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-onboard-users-onboarding-steps]] → [[raw/adyen/docs/issuing/onboard-users/onboarding-steps/2026-09-15]].

Q2. Why can this capture not establish a concrete user's onboarding requirements?
Answer: Location and legal entity/legal arrangement type are unselected. The raw instructs selecting all required filters or adding missing query parameters to export a concrete result (line 35); it contains no filtered country/entity checklist. Do not infer documents, data fields, completed verification, or an issued card from this selector. Route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-onboard-users-onboarding-steps]] → [[raw/adyen/docs/issuing/onboard-users/onboarding-steps/2026-09-15]].
