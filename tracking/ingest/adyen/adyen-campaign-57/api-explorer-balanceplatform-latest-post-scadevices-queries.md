# Fixed query check — POST /scaDevices

Canonical target: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-scadevices.md`
Canonical URL: https://docs.adyen.com/api-explorer/balanceplatform/latest/post/scaDevices

## Q1

For `balanceplatform/latest/post/scaDevices`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API test-server `bcl/v2` page says `POST /scaDevices` begins registration of a new SCA device. Its request-property table marks `name` and base64-encoded Authentication SDK `sdkOutput` required; the page does not separately mark the body itself required or explain the SDK output-generation step. It identifies the device resource by ID, name and `ios`, `android`, or `browser` type in the response. The page names no permission role, although it documents a possible `403` insufficient-permissions response. (Raw lines 5–18, 29–41, 82–98.)

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

`201` creates a device resource and completes only the initial registration step; the page expressly says the device is not ready for use. `scaDevice` and `sdkInput` are response fields marked optional, and `sdkInput` must be passed to the Authentication SDK to continue; this page provides no follow-up request/response or final-ready schema. It lists `400` invalid input, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` server error. The only listed server is test `bcl/v2` despite `latest` in the page path. The response does not establish completed device registration, entity association, successful SCA authentication, account verification, payment or financial outcome, deletion, propagation, or live availability. (Raw lines 9–10, 29–41, 44–136, 138–152.)
