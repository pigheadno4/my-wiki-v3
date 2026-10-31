# Fixed queries — Payout API POST /confirmThirdParty

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-confirmthirdparty.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/confirmThirdParty

## Q1

For `Payout/latest/post/confirmThirdParty`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: Deprecated TEST Payout v68 `POST /confirmThirdParty` confirms a previously submitted payout; `/declineThirdParty` is named for cancellation. Required `merchantAccount` identifies the processing merchant, and required `originalReference` is the PSP reference from `/submitThirdParty`, distinct from this confirmation response's `pspReference`. Optional `additionalData` may be required for a particular payout, without a stated general condition. The page lists 401/403 but no named credential or reviewer role. New integrations are directed to Transfers API; existing users are directed to Adyen for migration. See full canonical source stem and URL above; pinned raw `raw/adyen/api-explorer/Payout/latest/post/confirmThirdParty/2026-09-15.md` lines 5–47, 75–100.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: HTTP 200 says the request succeeded; required `response` can say `payout-confirm-received` or `payout-decline-received`, and required `pspReference` identifies the confirmation transaction. The example shows `[payout-confirm-received]` with brackets, contrary to the unbracketed description. Receipt of a confirmation is not proof of recipient payment, bank receipt, or a final payout status. Errors listed are 400, 401, 403, 422 and 500. The capture lists only a TEST v68 server and does not establish live eligibility or migration completion. See full canonical source stem and URL above; pinned raw lines 27–28, 48–58, 61–152.
