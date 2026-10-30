# Fixed query check — PATCH /scaAssociations

Canonical target: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-latest-patch-scaassociations.md`
Canonical URL: https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/scaAssociations

## Q1

For `balanceplatform/latest/patch/scaAssociations`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Balance Platform API test-server `bcl/v2` page says `PATCH /scaAssociations` approves a previously created pending association. The association is between an SCA device and an `accountHolder`, `legalEntity`, or `paymentInstrument` entity. Its header table marks `WWW-Authenticate` required for SCA authentication; its request-property table marks `entityId`, `entityType`, `scaDeviceIds`, and `status` required. `status` lists `active` and `pendingApproval`, while the approval example uses `active`; the enum does not prove another approval transition. The page does not separately mark the body itself required or name a role. (Raw lines 5–26, 28–40.)

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

`200 Success` is labeled successful approval and returns an array of SCA associations with entity/device identifiers and status. `401` means authentication required, `403` insufficient permissions, and `500` server processing failure. The only server shown is the test `bcl/v2` URL, despite `latest` in the canonical page path. The page documents approval of a pending association, not initial creation, deletion, a live endpoint, another user authentication, legal-entity verification, card authorization, funds movement, propagation timing, or idempotency. (Raw lines 5–10, 41–110, 112–128.)
