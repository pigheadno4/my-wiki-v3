# Business Accounts consent retrieval checks

## Q1 — As a third-party provider, what can I check before using an account holder's consent?

**Answer:** After Adyen onboarding and the separate consent-grant flow, a TPP can GET consent status, GET the authorization resource's SCA progress, and GET consent details. `consentStatus` must reach `valid` for use; `received` calls for another check, while rejected/revoked/expired/terminated states are distinct. `scaStatus` describes authorization progress and is a separate resource. Consent details show `validUntil` and the allowed account/balance/transaction access in the example, so a status alone does not prove a particular action is in scope. The sample 2023 expiry date is not a current consent.

**Evidence:** `raw/adyen/docs/business-accounts/consent/2026-09-15.md:19-38,48-57,69-116,120-149`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-consent]]` → `[[raw/adyen/docs/business-accounts/consent/2026-09-15]]`.

## Q2 — What does a TPP's DELETE consent call establish, and which revoked status follows?

**Answer:** The page says a TPP may DELETE `/consents/{consent_id}` on the account holder's behalf; successful deactivation returns HTTP 200, with `revokedByPsu` on later checks. Its status table separately defines `terminatedByTpp` for TPP termination. That naming tension is unresolved in the captured guide, so HTTP 200 or an example does not establish the exact future status for every scenario. Revocation withdraws permission for the consented account-information access or payment-initiation action; it says nothing about payment execution or bank receipt.

**Evidence:** `raw/adyen/docs/business-accounts/consent/2026-09-15.md:19-24,52-57,152-166`. **Forward route:** `[[index]]` → `[[adyen-index]]` → `[[adyen-business-accounts]]` → `[[source-adyen-docs-business-accounts-consent]]` → `[[raw/adyen/docs/business-accounts/consent/2026-09-15]]`.
