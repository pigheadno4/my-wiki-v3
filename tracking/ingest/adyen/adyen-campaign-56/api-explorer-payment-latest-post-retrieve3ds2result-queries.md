# api-explorer-payment-latest-post-retrieve3ds2result fixed retrieval check

Read log: entire pinned raw lines 1–160 read as one numbered, untruncated contiguous range. SHA-256 verified: 30c8d4aa1e1c5dac14e33609277444c6a3079a318986667998d132280c29c0ed.

Canonical source: [[source-adyen-api-explorer-payment-latest-post-retrieve3ds2result]] — https://docs.adyen.com/api-explorer/Payment/latest/post/retrieve3ds2Result

- Q1: For `Payment/latest/post/retrieve3ds2Result`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - Answer: Classic Payment API `POST /retrieve3ds2Result` retrieves the 3DS2 result after authentication only (5–7), on the captured TEST `Payment/v68` server (9–10). The request table marks `merchantAccount` and the `pspReference` returned by `/authorise` required (14–18). It does not separately state whole-body requiredness.
- Q2: For `Payment/latest/post/retrieve3ds2Result`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - Answer: HTTP 200 means retrieval succeeded; its optional `threeDS2Result` holds optional authentication fields, including `transStatus` and `transStatusReason` (29–51). This is no proof of payment authorization, capture or settlement, and the page has no 200 example. It lists 400/401/403/422/500 API errors (54–121), with only 400/401/500 examples (123–160). There is no deletion, propagation, async payment-outcome or retry contract here. TEST v68 and the captured `latest` URL do not establish live/current availability or a Checkout API contract (1–10).
