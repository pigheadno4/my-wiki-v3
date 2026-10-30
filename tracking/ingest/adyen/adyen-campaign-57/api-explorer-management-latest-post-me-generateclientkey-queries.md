# Fixed query audit: POST /me/generateClientKey

Source: `wiki/sources/adyen/source-adyen-api-explorer-management-latest-post-me-generateclientkey.md` — https://docs.adyen.com/api-explorer/Management/latest/post/me/generateClientKey

## Q1

For `Management/latest/post/me/generateClientKey`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Management API v3 TEST endpoint generates a client key for requests from the payment environment, distinct from the caller's API credential/API key. The API credential needs the `Management API—API credentials read and write` role (raw lines 5–16). This page specifies no request fields or body. The new client key can be used a few minutes after generation; the old client key stops working after 24 hours (lines 8–9).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 response requires a generated `clientKey` (raw lines 18–26). Errors cover 400, 401, 403, 422 and 500 (lines 29–126). The stated propagation and expiry apply to the client key; the page does not document API-key rotation, client-side authentication success, payment execution or live readiness. The displayed server is `management-test.adyen.com/v3` (lines 15–16); the URL's `latest` label is a captured route, not current-version proof.
