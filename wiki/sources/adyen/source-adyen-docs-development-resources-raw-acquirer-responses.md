---
title: "Adyen Docs: Raw acquirer responses"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/raw-acquirer-responses"
raw_files:
  - "adyen/docs/development-resources/raw-acquirer-responses/2026-09-15.md"
tags: [adyen, online-payments, raw-acquirer-responses, refusal-reasons, response-codes]
---

## Overview

This Adyen development-resources catalog, last modified 2024-10-16 and captured 2026-09-15, explains common raw responses for online payment declines, cancellations and related modification failures. Schemes and issuers can change raw text; Adyen maps failed-transaction raw responses to normalized `resultCode` and `refusalReason`. The tables also show last Customer Area journal type and, for some providers, API error codes or HTTP statuses. A raw code, journal label, HTTP status, normalized refusal and final payment outcome are different layers. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For online payments, enable **Raw acquirer result** under merchant-account **Developers → Additional data** to receive `additionalData.refusalReasonRaw` on declines. `refusalCodeRaw`, the numeric portion, is available only for Visa and Mastercard on Adyen's own acquiring platform. The example raw `51 : Insufficient funds/over credit limit` maps to normalized `refusalReason=Not enough balance` and `resultCode=Refused`. Do not expose raw response details to shoppers because of misuse risk. See raw lines 19–82.
- The Visa/Mastercard table contains network- and context-specific meanings. Code `65` is both withdrawal-count limit and Mastercard authentication-required soft decline; `70` differs for Mastercard contact issuer and Visa PIN data; `82` differs by network; `91` appears as both Refused and Error. `85` can be an authorized zero-value verification. Interpret a code with network, full raw text and journal context, not as a universal outcome. See raw lines 90–150. Similar code strings mean different things in Discover, Mexico and other network/provider sections.
- Retry guidance is **row and provider specific**. Visa/Mastercard raw codes can inform a merchant's own Visa excessive-retry-fee handling (raw 84–88), while Mastercard Merchant Advice Codes (MACs) are a separate `additionalData.merchantAdviceCode` field that some issuers return automatically for approved or refused payments. The MAC table ranges from no-retry `03`/`21` to prescribed delayed retries `02`/`24`–`30`; an unknown MAC gives no actionable advice. See raw lines 519–543. Do not turn a general timeout or insufficient-funds label into a universal retry permission.
- Cash App Pay's listed errors are provider `errors[].code` values with payment/payout-processing categories and HTTP 400, not general Adyen HTTP or card-network refusal codes. The table distinguishes permanent declines from conditionally retryable merchant-state errors and correctable amount/currency/refund requests. PayTo's payment table explicitly labels retriable with the **same payment details**, whereas its agreement-refusal table has no such column. See raw lines 256–286 and 822–866.
- The catalog extends beyond simple initial card refusals: Klarna includes pending, authorized, expired offer and pre-authorization-token cases; Alipay, PayPal, Swish, Ratepay and other sections include capture/refund failures or asynchronous provider states. PayPal is split between traffic moved to a newer API and traffic still on an older API; an error-code lookup must select the applicable table. See raw lines 182–209, 491–518, 749–821 and 885–967.

## Important qualifications

- This is an **online payments** guide; it separately points to Terminal API raw responses for in-person integration (raw 19–36, 978–982). Individual catalog rows can still describe POS-specific circumstances, such as Alipay merchant cancellation and its `TRADE_NOT_EXIST` online/POS split (raw 190–194). Preserve each row's stated context.
- The general rule not to show **raw response details** to shoppers (raw 42–43) has a distinct Japan-specific field: the page recommends showing `additionalData.domesticShopperAdvice` on a Japanese checkout, alongside `domesticRefusalReasonRaw` diagnostics (raw 440–472). Do not substitute the raw diagnostic for that shopper-advice text.
- Some rows are internally awkward or contingent: Visa/Mastercard `00` has journal `Authorised` yet describes later cancellation (raw 92); MB WAY generic refusal/timeout rows say a shopper-completed app payment may still settle (raw 552–559); Swish `No response from ACM` appears under Refused and Error (raw 956, 964). Treat the table as a diagnostic snapshot, not a complete or timeless truth table.
- The wording of a raw response can change without notice, and this snapshot does not prove current network rules, account configuration, or an individual payment's final state (raw 23–29, 40–43).

## Detail locators

- Online requirements, receiving fields, normalization example and shopper-data warning: raw lines 19–82.
- Visa/Mastercard common responses and Adyen for Platforms validation: raw lines 84–163.
- Accel, Afterpay, Alipay/AlipayHK, American Express and BLIK: raw lines 165–254.
- Cash App Pay provider codes/HTTP 400, Diners, Discover and GoPay: raw lines 256–420.
- GrabPay, Japan domestic issuer advice, KCP and Klarna: raw lines 422–518.
- Mastercard Merchant Advice Codes, MB WAY, Mexico and Nyce: raw lines 519–695.
- Oney, Czech/Poland/Slovakia online banking, Pay by Bank US: raw lines 697–747.
- PayPal newer versus older API, PayTo agreement/payment retriability, Pix refund codes: raw lines 749–883.
- Ratepay, SEPA Direct Debit, Star, Swish and TWINT: raw lines 885–976.

## Related

- [[adyen-online-payments]] — provider online-payment architecture and source routes.
- [[source-adyen-docs-development-resources-overview-response-handling]] — separate overview of HTTP request, raw response, normalized refusal and payment-result layers.
- [[source-adyen-docs-development-resources-refusal-reasons]] — normalized refusal reasons and result-code handling.
- [[source-adyen-docs-development-resources-raw-acquirer-responses-visa-integrity-fees]] — separate Visa retry-fee category mapping.

## Raw Sources

- [[raw/adyen/docs/development-resources/raw-acquirer-responses/2026-09-15|Raw acquirer responses, 2026-09-15 capture]]
