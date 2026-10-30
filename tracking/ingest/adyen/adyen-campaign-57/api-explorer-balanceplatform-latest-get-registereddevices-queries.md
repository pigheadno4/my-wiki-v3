# Fixed retrieval queries: api-explorer-balanceplatform-latest-get-registereddevices

Source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-get-registereddevices.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/get/registeredDevices
Pinned raw: `raw/adyen/api-explorer/balanceplatform/latest/get/registeredDevices/2026-09-15.md` (SHA-256 `f314163e8fd92e47edd18f8762e4466458d24390e768895a452946482e97b100`).

## Q1

For `balanceplatform/latest/get/registeredDevices`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `GET /registeredDevices` lists currently registered SCA devices for one payment instrument in pages (raw lines 5–7). The payment instrument is the required `paymentInstrumentId` query filter, distinct from each returned device `id` and associated `paymentInstrumentId` field (lines 19, 29–33). `pageNumber` is optional, zero based and defaults to 0; `pageSize` is optional, defaults to 20 and has maximum 100 (lines 17–18). The page names no specific credential role or prior registration procedure, but documents 401 authentication required and 403 insufficient permission (lines 69–90). Its only listed server is Balance Platform API v2 TEST (lines 9–10).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 means the list request succeeded; the schema shows optional `data`, device fields, `itemsTotal`, page links and `pagesTotal` (lines 23–46). It lists device types `ios`, `android`, `browser` (line 33), and errors 400, 401, 403, 422 and 500 (lines 49–146). The 422 and 500 JSON examples mention balance-account changes and payment-instrument creation (lines 189–215); those generic examples cannot define this GET endpoint's mutation rules. This read-only page establishes no registration, deregistration, SCA verification/approval, propagation timing, payment or funds outcome. The captured TEST v2 server and `latest` URL do not establish current live eligibility or a stable latest version (lines 1–10).

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-get-registereddevices.md` — https://docs.adyen.com/api-explorer/balanceplatform/latest/get/registeredDevices
