# Fixed retrieval audit — setupBeneficiary

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-setupbeneficiary.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/setupBeneficiary

## Q1

For `Fund/latest/post/setupBeneficiary`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

This Classic Fund API v6 operation defines a benefactor/beneficiary relationship between two accounts. Required `sourceAccountCode` identifies the benefactor; required `destinationAccountCode` identifies the beneficiary; `merchantReference` is optional. The page says current source funds are transferred to the destination at setup and later payments to the benefactor are automatically sent to the beneficiary. A series cannot exceed four beneficiaries or contain a cycle. The page does not specify a same-holder or same-platform requirement. 403 is insufficient permissions. Locators: pinned raw lines 5–20, 93–94. Route: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-setupbeneficiary.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/setupBeneficiary.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 says the request succeeded; HTTP 202 says accepted for processing but incomplete. Both response schemas offer validation fields, request `pspReference` and `resultCode`, without a posted transfer amount or resulting balance. Thus the 202 receipt is not proof that the described current-balance transfer or future routing has completed; the page provides no separate final-transfer confirmation. Errors listed are 400, 401, 403, 422 and 500. This 2026-09-15 v6 test-server capture is no proof of current live availability, account eligibility or actual movement. No deletion or verification/approval result is specified. Locators: pinned raw lines 9–10, 31–129. Route: `wiki/sources/adyen/source-adyen-api-explorer-fund-latest-post-setupbeneficiary.md` — https://docs.adyen.com/api-explorer/Fund/latest/post/setupBeneficiary.
