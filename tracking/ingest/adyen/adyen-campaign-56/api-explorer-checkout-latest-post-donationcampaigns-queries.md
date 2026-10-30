# api-explorer-checkout-latest-post-donationcampaigns query answers

Full source: `source-adyen-api-explorer-checkout-latest-post-donationcampaigns` — https://docs.adyen.com/api-explorer/Checkout/latest/post/donationCampaigns

Read audit: numbered contiguous raw lines 1–85, 86–170, and 171–247; SHA-256 verified.

- Q1: For `post/donationCampaigns`, what is the endpoint purpose and object identity, and which central required or conditional inputs/prerequisites govern using it?
  - A: It queries active donation **campaigns** for donation context, not a donation payment (raw 5–7). The request body table requires currency and merchantAccount, with optional label and locale; store is table-optional but conditionally required for Adyen for Platforms platform-model integrations, with different reference identifiers for balance platform versus classic integration (raw 20–27). Idempotency-Key is optional (raw 14–17).
- Q2: For `post/donationCampaigns`, what does the documented response or failure establish, and which lifecycle, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - A: HTTP 200 indicates a successful query; its optional donationCampaigns array lists active merchant-account campaigns and optional campaign ID, nonprofit and donation-configuration details (raw 38–64). It is not evidence of campaign creation, a donation transaction, authorization or settlement. Errors 400/401/403/422/500 are listed (raw 67–134); the generic 422 example's missing Return URL is not a request-body requirement here (raw 20–27, 223–234). Captured server is test v72 under a latest URL; current/live behavior is unproved (raw 1–10).
