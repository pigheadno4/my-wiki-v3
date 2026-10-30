# Fixed query check — POST /transferInstruments

Canonical target: `wiki/sources/adyen/source-adyen-api-explorer-legalentity-latest-post-transferinstruments.md`
Canonical URL: https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments

## Q1

For `legalentity/latest/post/transferInstruments`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured test `lem/v4` reference creates a transfer instrument: a bank account owned by the legal entity identified by `legalEntityId`. The request-property table marks `bankAccount`, `legalEntityId`, and `type` required; `bankAccount` is the sole listed type. Nested `accountIdentification`, `accountType`, `bankName`, and `countryCode` are marked optional in this table, and the page does not separately mark the body itself required. IBAN, UK local, and US local examples show different account-identification shapes but do not establish a complete country/type-required-field matrix. The US response includes `accountType: checking` although the US request example omits it. Limits are 700 requests per five seconds live, 200 per five seconds test, and five failed requests per ten seconds. The optional `x-requested-verification-code` header is test-only and accepts one suberror code. No specific permission role is named. (Raw lines 5–41, 43–87, 246–269.)

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

`200` says the create request succeeded and returns the transfer instrument ID, owner legal-entity ID, bank account, and type, with optional capability and verification-problem fields. Verification may be pending, invalid, valid, or rejected; the EUR and US examples show `sendToTransferInstrument` requested but disallowed while pending, while the UK example omits the capability field. Adyen reports verification results by webhook or API response, and the page conditions sending balance-platform funds to the instrument on passing verification. Thus creation is not approval, payout eligibility, funds movement, or bank receipt. Error cases are `400`, `401`, `403`, `422`, and `500`. The only server shown is test `lem/v4` despite `latest` in the URL; no delete flow, propagation timing, idempotency rule, or live approval is established. (Raw lines 9–22, 88–198, 200–270.)
