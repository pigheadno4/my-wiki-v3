# C56 fixed-query audit — api-explorer-binlookup-latest-post-get3dsavailability

Full raw read: numbered contiguous lines 1–154; SHA-256 4d6024c9ce43ec1964c1ee00902ae73d7d18e6e32c40475bc1f8f6be9f7ec29f.

Canonical source: [[source-adyen-api-explorer-binlookup-latest-post-get3dsavailability]] — https://docs.adyen.com/api-explorer/BinLookup/latest/post/get3dsAvailability

- Q1: For `BinLookup/latest/post/get3dsAvailability`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: BinLookup API v54 `POST /get3dsAvailability` checks 3DS availability for a specified BIN or card brand and can return 3DS2 fingerprinting keys (raw lines 5–12). The only request property marked required is `merchantAccount`; `cardNumber` (card or BIN), `brands`, `recurringDetailReference`, `shopperReference` and `additionalData` are optional in the table (16–24). The example uses `cardNumber` (26–34). No explicit required-one-of or body-requiredness constraint is shown.
- Q2: For `BinLookup/latest/post/get3dsAvailability`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: A 200 can include optional 3DS1/3DS2 support booleans, 3DS2 card-range/version/method URL data, DS keys and issuer country (35–59). The example has 3DS1 true and 3DS2 false, with empty card-range details; it is not universal support or merchant eligibility evidence (131–142). Availability is not actual authentication or payment authorization/capture/settlement. Errors listed are 400/401/403/422/500, with only a 400 example (62–154). The captured host is test v54 despite `latest` in the URL; no current-version or live result follows (1, 11–12).
