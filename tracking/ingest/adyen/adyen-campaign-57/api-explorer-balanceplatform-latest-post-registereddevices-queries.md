# Fixed query audit: POST /registeredDevices

Source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-post-registereddevices.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/post/registeredDevices

## Q1

For `balanceplatform/latest/post/registeredDevices`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API v2 TEST endpoint initiates registration of a user's SCA device for Business Accounts or Adyen-issued cards, requiring that the device be SCA eligible (raw lines 5–12). The request table marks `paymentInstrumentId` and `strongCustomerAuthentication.sdkOutput` required properties; SDK output is base64-encoded SDK data. An optional device `name` is auto-generated when absent (lines 14–22). The table does not explicitly establish body requiredness. Authentication and permission failures are documented as 401/403, without a named role (lines 58–79).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 fields are optional; `sdkInput` is for SDK continuation and `success` indicates successful **initiation** only (raw lines 26–35). The page does not show completion, device association or SCA approval, deletion, propagation timing, idempotency, a financial operation or final outcome. Errors are 400/401/403/422/500 (lines 38–135). The generic 422/500 examples describe payment-instrument changes/creation, so they cannot establish registration-specific failure behavior (lines 178–204). `latest` is a captured URL label; the displayed server is test `/bcl/v2` (lines 1, 11–12), not evidence of current version or live access.
