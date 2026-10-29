# Fixed retrieval checks — Raw acquirer responses

Source stem: `source-adyen-docs-development-resources-raw-acquirer-responses`
Canonical URL: https://docs.adyen.com/development-resources/raw-acquirer-responses
Pinned raw: `raw/adyen/docs/development-resources/raw-acquirer-responses/2026-09-15.md` (SHA-256 `0370b8229032a9b40f86e7b8c4d86593f74981f12c383c710410308e74b12a2a`).

## Q1

**Question:** Where does an online merchant obtain raw decline diagnostics, and how do raw codes differ from normalized refusal and HTTP/payment outcomes?

**Answer:** In the merchant account Customer Area, enable **Developers → Additional data → Raw acquirer result**. Declined responses then include `additionalData.refusalReasonRaw`; `refusalCodeRaw` is the numeric portion only for Visa/Mastercard transactions through Adyen's own acquiring platform. The example raw `51 : Insufficient funds/over credit limit` maps to normalized `refusalReason=Not enough balance` and `resultCode=Refused`. Raw wording varies by scheme and can change. The tables show journal labels and, in some provider sections, provider HTTP statuses; a code or HTTP status alone is not a universal payment outcome. Do not display raw response details to shoppers. The Japan-specific `domesticShopperAdvice` is a separate field that the page recommends showing in Japan. Raw lines 19–82, 256–286, 440–472.

**Retrieval route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-development-resources-raw-acquirer-responses.md` → pinned raw lines 19–82, 256–286 and 440–472.

## Q2

**Question:** Can a merchant decide whether to retry from a raw response code alone, such as 65, a Mastercard MAC, or a PayTo refusal?

**Answer:** No universal retry rule follows from a raw code alone. The Visa/Mastercard table uses `65` both for withdrawal-count limit and for Mastercard authentication-required soft decline; `70`, `82`, and `91` also vary by network or journal context. Mastercard MAC is a separate `additionalData.merchantAdviceCode` that some issuers return automatically on approved or refused payments; its rows give distinct no-retry or scheduled-delay advice. PayTo's **payment** table has a Retriable column specifically for reuse of the same payment details; its **agreement** table does not. Cash App Pay's provider `errors[].code` entries all carry HTTP 400 in this table yet distinguish permanent declines, conditionally retryable merchant-state problems and correctable requests. PayPal's newer-API and older-API tables must be selected by actual traffic path. Follow the relevant raw row and provider-specific conditions, including customer/merchant state and modification outcome, and check final payment state separately. Raw lines 84–150, 256–286, 519–543, 749–866.

**Retrieval route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → source stem above → pinned raw lines 84–150, 256–286, 519–543 and 749–866.
