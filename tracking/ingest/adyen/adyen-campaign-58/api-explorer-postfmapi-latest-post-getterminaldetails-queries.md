# Fixed queries — POS Terminal Management API POST /getTerminalDetails

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-post-getterminaldetails.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/post/getTerminalDetails

## Q1

For `postfmapi/latest/post/getTerminalDetails`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

Answer: Deprecated TEST POS Terminal Management v1 `POST /getTerminalDetails` requires a terminal ID in `[Device model]-[Serial number]` form and returns fleet/assignment detail for that physical terminal. `companyAccount` and `terminal` are required response fields; merchant, store, inventory, storeDetails, terminalStatus and network fields are optional. Company-only account level means company inventory; merchant without store means merchant assignment. `merchantInventory=true` means merchant inventory/cannot board, while false means in-store assignment and ready to board or already boarded. The page lists authentication/permission errors but no named role. See full canonical source stem and URL above; pinned raw `raw/adyen/api-explorer/postfmapi/latest/post/getTerminalDetails/2026-09-15.md` lines 5–19, 29–73, 89–112.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

Answer: A 200 says the lookup request succeeded. Optional `storeDetails.status` describes store activation, while optional `terminalStatus` describes recent online or pending reassignment; neither proves boarding, payment-method readiness, or payment execution. The example pairs store assignment and `merchantInventory=false` with `SwitchedOff`. Last activity/transaction timestamps are omitted beyond 14 days. Errors are 400, 401, 403, 422 and 500. The page states this v1 API was deprecated 2025-01-01 and support stopped 2025-04-01, directing automation to Management API; its TEST capture cannot prove current live service. See full canonical source stem and URL above; pinned raw lines 5–12, 29–73, 76–222.
