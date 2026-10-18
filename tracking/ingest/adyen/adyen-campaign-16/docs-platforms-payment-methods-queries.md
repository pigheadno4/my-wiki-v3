# C16 Platforms payment-method catalog retrieval checks

## Q1 — Purpose, scope, and inference boundary

Query: Does the Adyen for Platforms supported-payment-method table show which ecommerce or POS methods are active for a particular user's store?

Expected route: `wiki/sources/adyen/source-adyen-docs-platforms-payment-methods.md` through the Adyen Platforms concept. Answer: it is a dated method/variant catalog with separate ecommerce/POS indicators. Methods are configured per store during onboarding or additionally requested through Customer Area/Management API. A listed row is not evidence of current country/currency eligibility, approval, store activation, or completed payment. Raw locators: lines 15–29, 31–76, 80–88.

## Q2 — Capability, prerequisites, and warnings

Query: What conditions must be checked before requesting a listed method for a platform user, especially a payment facilitator using aggregated acquiring accounts?

Expected route: same source and raw. Answer: inspect the method's exact variant and ecommerce/POS row, store country, listed currency and any approval, shopper-interaction or additional-parameter note; footnoted ecommerce methods do not support aggregated acquiring accounts and call for business lines and stores for those users. The catalog does not specify credential roles, account-holder capability checks, request limits or activation semantics; follow its separate API/Customer Area management routes and actual account state. Raw locators: lines 23–29, 31–78, 80–88.
