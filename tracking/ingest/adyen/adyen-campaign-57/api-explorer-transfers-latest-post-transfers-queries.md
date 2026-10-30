# Fixed query check — POST /transfers

Canonical target: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-post-transfers.md`
Canonical URL: https://docs.adyen.com/api-explorer/transfers/latest/post/transfers

## Q1

For `transfers/latest/post/transfers`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured test `btl/v4` Transfers API endpoint starts requests to balance accounts, transfer instruments, third-party bank accounts, or third-party cards; versions 1 and 2 are deprecated. It requires the TransferService Webservice Initiate role and required account-holder capabilities, with Adyen-contact setup. The request-property table marks `amount` (currency and minor-unit value), `category`, and `counterparty` required; the counterparty identifies a balance account, bank account, card, or transfer instrument. The source `balanceAccountId` is distinct from counterparty IDs; virtual `bankAccount` source use requires `paymentInstrumentId`, while balance-account-only source selection uses an assigned default physical bank-account payment instrument. For bank category, both `priorities` and `priority` are described as required despite `No` row flags, and examples use only `priority`; do not infer their exact combined rule. Optional `executionDate` is within 30 days; the timezone defaults to Europe/Amsterdam. Optional review SCA applies only to Adyen Business Accounts. `Idempotency-Key` is optional and capped at 64 characters, with no stated outcome guarantee. (Raw lines 5–71, 94–204, 295–312.)

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Both `200` and `202` say the request is accepted for processing but not completed. Adyen sends outcomes through webhooks. The response status descriptions distinguish `received`, `refused`, `authorised` (funds reserved), `booked` (source balance deducted), `failed` and `returned`; future execution stays `received`/`pending` until its date. Errors shown are `401`, `403`, `422` and `500`. The page shows a test `btl/v4` server even though the URL says `latest`, so it does not prove live/current eligibility. Acceptance, approval or source deduction does not establish beneficiary-bank receipt, final card payment, completed internal two-leg transfer, or settled funds. The page does not define a delete operation, propagation timing, or idempotent retry result. (Raw lines 7–30, 60–70, 313–316, 359–375, 399–400, 443–458, 483–568, 570–930.)
