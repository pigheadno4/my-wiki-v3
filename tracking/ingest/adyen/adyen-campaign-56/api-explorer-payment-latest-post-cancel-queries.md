# api-explorer-payment-latest-post-cancel query answers

Full source: `source-adyen-api-explorer-payment-latest-post-cancel` — https://docs.adyen.com/api-explorer/Payment/latest/post/cancel

Read audit: numbered contiguous raw lines 1–70, 71–135, and 136–189; SHA-256 verified.

- Q1: For `Payment/latest/post/cancel`, what purpose, API/version and object identity does this captured page establish, and what central required/conditional inputs or prerequisites govern its use?
  - A: Classic Payment API v68 `POST /cancel` requests release of the authorisation hold after authorisation, only for methods supporting separate authorisation and capture (raw 5–20). It is inactive for new integrations and directs them to a distinct Checkout cancels endpoint (raw 11–15). The body table requires merchantAccount and originalReference, which is the original **payment** PSP reference; optional reference identifies the **modification** (raw 24–48). Other optional schema fields have conditional meanings at raw 27–58.
- Q2: For `Payment/latest/post/cancel`, what does the documented response or failure establish, and which lifecycle, deletion/propagation, asynchronous outcome, version/environment or missing-evidence boundaries prevent broader inference?
  - A: HTTP 200 has a new request pspReference and a response indicating the modification request was **received for processing**, not that cancellation completed (raw 70–80). Error tables list 400/401/403/422/500 (raw 83–150). This reference does not document the eventual notification outcome, capture/refund reversal or Checkout endpoint schema. The `latest` page captures a v68 **test** PAL server (raw 1–20), not current/live availability.
