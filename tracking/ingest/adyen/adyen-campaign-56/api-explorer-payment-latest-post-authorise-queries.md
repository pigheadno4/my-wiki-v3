# Fixed retrieval checks — api-explorer-payment-latest-post-authorise

Canonical source: [[source-adyen-api-explorer-payment-latest-post-authorise]] — https://docs.adyen.com/api-explorer/Payment/latest/post/authorise
Pinned capture: `raw/adyen/api-explorer/Payment/latest/post/authorise/2026-09-15.md` (2026-09-15); Classic Payment API v68 TEST server. Read audit: contiguous numbered raw lines 1–100, 101–200 (reread after truncated aggregate output), 201–300 (reread), 301–400, 401–500, 501–600, 601–705; SHA-256 verified against trusted input.

## Q1: For `Payment/latest/post/authorise`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?

The inactive Classic Payment API `POST /authorise` creates a payment with an Adyen `pspReference` and attempts an authorization hold; new integrations are directed to Checkout `/payments`, existing ones to migration contact (raw lines 5–18). The v68 TEST request table marks `amount`, `merchantAccount` and merchant `reference` required (lines 49–51, 217, 263). It says either `bankAccount` or `card` is needed (lines 74, 102), but a recurring ContAuth example uses stored detail IDs without either (lines 469–487), so that sentence cannot be generalized to the example. 3DS browser/mobile, Visa/JCB, authentication-only, and recurring conditions are detailed at lines 84–100, 262, 274–281, 294–369.

## Q2: For `Payment/latest/post/authorise`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?

HTTP 200 establishes request success; the optional `resultCode` differentiates `Authorised` and other final outcomes from pending/received states, 3DS/shopper steps and authentication-only outcomes (raw lines 573–596). For cards, a hold can be captured or cancelled later; non-card methods typically auto-capture, so response success or a hold does not prove later capture/settlement (line 7). Refusal information and 400/401/403/422/500 error shapes are at lines 595, 599–666; examples cover only selected errors (668–705). This inactive v68 TEST capture under a `latest` URL does not establish current latest/live status or Checkout schema (lines 1–2, 9–18).
