# Retrieval checks — Business Accounts transaction-history SCA

## Q1 — purpose and prerequisites

**Question:** What does this SCA guide enable, and what access and device setup does it name?

**Located answer:** The dated guide describes authenticating a user before returning balance-account transaction history via the Transfers API. It says EEA users must authenticate each time, while supporting Adyen for Platforms or Classic integrations (raw lines 15-30). It names an API key or basic authentication, the TransferService Webservice Retrieve role, an installed Authentication SDK and a registered user device (raw lines 29-32). This snapshot does not establish current regional law or a specific account's access.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-sca-for-transaction-history]] → [[raw/adyen/docs/business-accounts/sca-for-transaction-history/2026-09-15]].

## Q2 — material boundary or failure

**Question:** Does the first `GET /transactions` return usable history, and what can stop completion?

**Located answer:** The first request includes eligibility `sdkOutput` in `WWW-Authenticate` with realm `Transaction`; the guide documents an HTTP 401 challenge and `auth-param1` response, then SDK authentication and a second GET using the authenticated `sdkOutput` (raw lines 145-161, 335-356, 424-432). It allows 10 minutes to authenticate and finalize (raw line 356). A web browser without SCA support throws `SCA_UNAVAILABLE` (raw line 139); the Android example also handles cancellation and authentication errors (raw lines 366-390). Only the final response's `data` array is presented as history (raw lines 606-667). Several sample requests have shell or Java syntax defects (raw lines 165-191), so they are not executable proof.

**Forward route:** [[index]] → [[adyen-index]] → [[adyen-business-accounts]] → [[source-adyen-docs-business-accounts-sca-for-transaction-history]] → [[raw/adyen/docs/business-accounts/sca-for-transaction-history/2026-09-15]].
