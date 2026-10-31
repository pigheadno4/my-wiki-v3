# Fixed-query audit: api-explorer-payout-latest-post-payout

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-payout.md` — https://docs.adyen.com/api-explorer/Payout/latest/post/payout
Pinned evidence: `raw/adyen/api-explorer/Payout/latest/post/payout/2026-09-15.md` (SHA-256 `f6e97990e371edc139071c447c86eec0c513ee477cbb3b2cda274949909c3d58`).

## Q1

For `Payout/latest/post/payout`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

**Answer:** The page calls `POST /payout` an instant card payout, limits support to Visa/Mastercard cards, makes the 30-minute cardholder-bank availability issuer-dependent, and marks the endpoint deprecated for new integrations. It directs new users to Transfers API `POST /transfers` and existing users to their Adyen contact for migration (raw lines 5–26). Required request properties are `amount` with currency/minor-unit value, `merchantAccount`, and `reference` (lines 30–35, 76, 83); uniqueness of `reference` is recommended, not required (line 83). The top-level `card` describes recipient data, whereas optional `fundSource` describes the funding person/entity and can carry a separate card (lines 43–75, examples 93–176). Conditional `billingAddress`, nested address fields, recurring `shopperReference`, stored detail, 3DS2 contact alternatives, and channel values are in lines 36–42 and 77–91. The generic bankAccount/card and zero-value verification descriptions do not document a bank-payout route or a zero-value payout. 401/403 identify authentication and permission failures (lines 217–232). Retrieve `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-payout.md` at https://docs.adyen.com/api-explorer/Payout/latest/post/payout.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

**Answer:** A 200 says the request succeeded, but its optional fields and `resultCode` vocabulary are payment/authorisation-style: `Received` is received for processing, `Pending` lacks final payment status, and `Authorised` is described as final payment authorisation (raw lines 177–200). They do not establish completed card payout, issuer posting, or cardholder bank receipt. The page lists 400, 401, 403, 422, and 500 error responses and one illustrative 400 JSON body (lines 203–284). It gives no payout-specific approval, settlement, reversal, or delivery-confirmation contract in this capture. The sole listed server is Payout v68 TEST (lines 25–26), fetched 2026-09-15 (line 2); the snapshot proves neither current live availability nor merchant enablement or a real payout. Retrieve `wiki/sources/adyen/source-adyen-api-explorer-payout-latest-post-payout.md` at https://docs.adyen.com/api-explorer/Payout/latest/post/payout.
