# Fixed retrieval audit — postfmapi overview

Canonical source: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-overview.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/overview

## Q1

For `postfmapi/latest/overview`, what purpose and object identities does this captured page establish, and which required/conditional fields, permissions, prerequisites or consequential constraints govern use?

This is the deprecated POS Terminal Management API v1 catalog for terminal/store lookup and assigning terminals to merchant accounts or stores. Its five POST operations are `assignTerminals`, `findTerminal`, `getStoresUnderAccount`, `getTerminalDetails` and `getTerminalsUnderAccount`. Each request needs an API key in `X-API-Key` and the POS Terminal Management API role, set up through Adyen. The page says new web-service-user credentials and a live Customer Area API key are needed for live use. This overview has no operation-specific fields. Locators: pinned raw lines 5–26, 39–58. Route: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-overview.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/overview.

## Q2

What do the response/errors establish, and which lifecycle, deletion, verification/approval, propagation, asynchronous financial outcome, version/environment or missing-evidence boundaries prevent broader inference?

The page states deprecation from January 1, 2025 and support stop on April 1, 2025, directing automation to the Management API. It gives test and live v1 base URLs and says versioned Boolean responses are strings whereas unversioned values are Booleans. It contains an endpoint catalog, no per-operation responses/errors, deletion contract, assignment-completion evidence, runtime terminal readiness, or payment outcome. This captured overview is not evidence of present live access. Locators: pinned raw lines 9–11, 28–58. Route: `wiki/sources/adyen/source-adyen-api-explorer-postfmapi-latest-overview.md` — https://docs.adyen.com/api-explorer/postfmapi/latest/overview.
