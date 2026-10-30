# api-explorer-recurring-latest-post-createpermit query answers

Full source: `source-adyen-api-explorer-recurring-latest-post-createpermit` — https://docs.adyen.com/api-explorer/Recurring/latest/post/createPermit

Read audit: numbered contiguous raw lines 1–60 and 61–111; SHA-256 verified.

- Q1: For `Recurring/latest/post/createPermit`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - A: Recurring API v68 `POST /createPermit` creates permits for an existing recurring contract (raw 5–10). The body table requires merchantAccount, permits array, recurringDetailReference for that contract, and shopperReference for the shopper (raw 14–28). Per-permit partnerId and profileReference apply to distinct permit sharing models; restrictions and expiry are optional (raw 19–26). No permit child property is marked required.
- Q2: For `Recurring/latest/post/createPermit`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - A: A 200 request success may return permitResultList with optional resultKey and partner-payment permit token, plus optional request pspReference (raw 30–41). It does not prove a later payment or that every requested permit produced a token. The page lists 400/401/403/422/500, including authentication and permission failures (raw 44–111). No disable/delete or propagation timing is specified here. The captured server is test Recurring v68 under a latest URL, not proof of current/live availability (raw 1–10).
