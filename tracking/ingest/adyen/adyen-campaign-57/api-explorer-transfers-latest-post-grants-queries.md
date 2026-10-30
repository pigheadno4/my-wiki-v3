# Fixed query audit: POST /grants

Source: `wiki/sources/adyen/source-adyen-api-explorer-transfers-latest-post-grants.md` — https://docs.adyen.com/api-explorer/transfers/latest/post/grants

## Q1

For `transfers/latest/post/grants`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

The captured Transfers API v4 TEST `POST /grants` requests payout of a selected grant offer (raw lines 5–10). `grantAccountId` identifies the grant account and `grantOfferId` the selected offer; both are required properties. Optional counterparty fields distinguish the receiving account holder's balance account from the legal entity's transfer instrument, without a stated choice rule (lines 20–27). The optional `Idempotency-Key` is limited to 64 characters, with UUID recommended, but no retry semantics are specified (lines 14–17). The page lists 401 authentication and 403 permission errors without naming a role (lines 98–119).

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The 200 response has grant-reference ID, account/offer IDs, balance amounts and status. Status can be `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed`, or `Revoked`; the example is `Pending` (raw lines 43–75, 197–232). Repayment fields describe deductions/thresholds; they do not prove any repayment occurred (lines 68–74). The endpoint does not show offer acceptance, payout booking or recipient receipt. Errors are 400/401/403/404/422/500; 404 says a *payment* was not found, so its grant-object meaning is unclear (lines 78–195). The `latest` URL displays a test `/btl/v4` server (lines 1, 9–10), not current version or live funding evidence.
