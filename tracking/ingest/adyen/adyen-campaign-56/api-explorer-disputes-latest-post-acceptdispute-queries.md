# C56 fixed-query audit — api-explorer-disputes-latest-post-acceptdispute

Full pinned raw read: numbered contiguous lines 1–117; SHA-256 e08b582fd7dc836c258955c85e29a71393dfc66992e4aeaebd5d1c629b869ea5. Related guide passages checked at Disputes API raw lines 143–145 and Manage Disputes raw lines 52–64.

Canonical source: [[source-adyen-api-explorer-disputes-latest-post-acceptdispute]] — https://docs.adyen.com/api-explorer/Disputes/latest/post/acceptDispute

- Q1: For `Disputes/latest/post/acceptDispute`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: Disputes API v30 `POST /acceptDispute` on the `ca-test` server accepts a specific dispute (raw lines 5–10). Required request properties are `disputePspReference`, the reference assigned to the **dispute**, and `merchantAccountCode` (14–18). The page does not separately label the body required. Related API workflow says acceptance is chosen instead of defending after retrieving dispute details (related Disputes API raw 143–145).
- Q2: For `Disputes/latest/post/acceptDispute`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: A 200 body contains required `disputeServiceResult.success`, which indicates whether the **request** succeeded; the example shows true (raw 29–39, 106–117). HTTP success alone is not a defense win or immediate final dispute status. Related Manage Disputes guidance says acceptance followed by defense-period expiry yields `Lost` and ends the cycle (related raw 52–64). Endpoint errors listed are 400/401/403/422/500, without error examples or timing details (42–104). The captured host is test v30 despite `latest` in the URL; no live eligibility or current-version result follows (1, 9–10).
