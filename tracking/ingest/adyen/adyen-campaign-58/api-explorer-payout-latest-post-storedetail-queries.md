# Fixed retrieval audit: api-explorer-payout-latest-post-storedetail

Canonical route: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetail.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetail

## Q1

For `Payout/latest/post/storeDetail`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** Deprecated Payout API v68 test-host `/storeDetail` stores bank/card details under a `PAYOUT` recurring contract for later `/submitThirdParty`; new integrations are directed to Transfers API and existing users to Adyen for migration (raw lines 5–26). Required table fields are `dateOfBirth`, `entityType`, `merchantAccount`, `nationality`, `recurring`, `shopperEmail`, and `shopperReference`; date of birth is described as mandatory for natural persons, while the `recurring` object must set `contract: PAYOUT` despite the nested row's No marker (lines 60–76). `bank` is mandatory without `card`, and `card` mandatory without `bank` (lines 33–34, 51). Address is required for cross-border payouts to/from Canada, with nested required fields and US/Canada state condition; optional shopper name has nested required names and Company last-name rule (lines 44–50, 73–75). Bank-owner name transliteration/validation and non-stored CVC/client-encryption warning are at lines 42 and 52. Authentication and permissions appear as 401/403 errors, without named roles (lines 108–123). Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetail.md`; URL: https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetail.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** HTTP 200 returns required `pspReference`, `recurringDetailReference` and `resultCode`; `Success` says details were stored, and the token is for later payout submission (raw lines 82–91, 163–174). This is neither `/submitThirdParty` nor approval, execution, card/bank receipt or payout completion (lines 23, 89–91). Errors 400, 401, 403, 422 and 500 and an illustrative 400 body appear at lines 94–186. The source is a captured deprecated v68 **test** page and offers no proof of current availability, live merchant enablement or a successful payout (lines 1–26). Full canonical route: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetail.md`; URL: https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetail.
