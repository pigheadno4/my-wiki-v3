# Fixed retrieval queries: api-explorer-foreignexchange-latest-post-rates-calculate

Source: `wiki/sources/adyen/source-adyen-api-explorer-foreignexchange-latest-post-rates-calculate.md` — https://docs.adyen.com/api-explorer/foreignexchange/latest/post/rates/calculate
Pinned raw: `raw/adyen/api-explorer/foreignexchange/latest/post/rates/calculate/2026-09-15.md` (SHA-256 `62228ee5299377f75f5eeaf47a97d1666eb6894ac1b53f081560834c5bf14a69`).

## Q1

For `foreignexchange/latest/post/rates/calculate`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** `POST /rates/calculate` returns calculated amounts and rates for currency conversion, on listed test and live Foreign Exchange API v1 URLs (raw lines 5–15). The body requires an `exchangeCalculations` array; each entry requires `exchangeSide` buy/sell, source currency and integer minor-unit value, target currency, and `splitPayment` or `splitRefund` type (lines 19–28). The page supplies no pair list, rate validity period, array-size limit, named credential role, or account-specific eligibility conditions. 401 and 403 are listed, but the latter example's token-policy message does not define an FX permission (lines 77–112, 183–195).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 is a successful calculation. Response entries may include source/target amounts and an applied rate that includes Adyen's markup; calculated amounts can be used in payment requests (lines 59–74). The response example is illustrative and does not lock the rate or prove a payment, refund, actual conversion, booking or settlement (lines 133–169). Listed errors are 401, 403 and 422; the 422 example shows invalid currency and negative source amount but is not an exhaustive constraints catalog (lines 77–131, 197–219). Both test and live URLs are listed, yet the snapshot and `latest` path do not prove current account access or a stable latest release (lines 1–15).

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-foreignexchange-latest-post-rates-calculate.md` — https://docs.adyen.com/api-explorer/foreignexchange/latest/post/rates/calculate
