# Fixed retrieval audit — storeDetailAndSubmitThirdParty

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetailandsubmitthirdparty.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty

## Q1

For `Payout/latest/post/storeDetailAndSubmitThirdParty`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The deprecated Payout API v68 operation submits a third-party payout and stores details for later payouts; it does not support new integrations. The request requires merchant account, amount/currency/minor-unit value, entity type, nationality, recurring object with `contract=PAYOUT`, merchant payout `reference`, shopper email and shopper reference, plus bank or card details. The table marks date of birth Yes while its description says mandatory for natural persons. Billing address is conditional for cross-border Canada payouts; company entity type requires company name in shopperName.lastName. `reference` uniqueness is recommended, not required. The submitted payout still requires reviewer confirmation/decline or corresponding API calls. 403 means insufficient permissions. Locators: pinned raw lines 5–85, 129–130. Route: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetailandsubmitthirdparty.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 says the request succeeded, with required `pspReference` identifying this request and `resultCode` success value `payout-submit-received`; `refusalReason` is optional. Submission is not reviewer confirmation, final payout, settlement or bank receipt. The page lists 400, 401, 403, 422 and 500 error schemas. It supplies no deletion operation here. This 2026-09-15 captured test-server v68 endpoint is deprecated for new integrations, directing them to Transfers API and existing integrators to Adyen for migration; the capture proves no live eligibility or current production outcome. Locators: pinned raw lines 7–28, 87–182. Route: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-storedetailandsubmitthirdparty.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/storeDetailAndSubmitThirdParty.
