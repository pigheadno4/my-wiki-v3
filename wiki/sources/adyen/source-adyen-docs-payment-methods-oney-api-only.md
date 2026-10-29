---
title: "Oney for API only | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/oney/api-only"
raw_files:
  - "adyen/docs/payment-methods/oney/api-only/2026-09-15.md"
tags: [adyen, oney, api-only, installments, redirect, capture]
---

## Overview

This [[adyen]] API-only Oney guide was last modified 2023-01-16 and captured 2026-09-15. It describes adding Oney to an **existing API-only integration** with a merchant-built payment form, server `/payments` request, shopper redirect and `/payments/details` result check (raw lines 15–32, 880–950). The related [[source-adyen-docs-payment-methods-oney]] overview supplies the European-entity and shopper-risk context and FR/ES/IT EUR scope. These captured instructions do not establish current merchant eligibility, an Oney credit decision or a completed payment. See [[adyen-online-payments]].

## Key takeaways

- **Before payment and installment selection:** The page calls for an existing API-only integration and adding Oney in **test** Customer Area. It tells the merchant to collect shopper details, include `lineItems`, and ensure successful authorisation and capture **before shipping** (raw lines 21–45). If `/paymentMethods` is used for discovery, send FR, ES or IT, EUR and payment value. The method types are `facilypay_3x` and `facilypay_4x` for FR/ES/IT; `facilypay_6x` for ES; and `facilypay_10x`/`facilypay_12x` for FR/ES (raw lines 47–61). The overview's card and installment matrix remains the product-scope reference; the generic `countryCode` formatting note mentioning QZ in this guide does not extend Oney eligibility (raw lines 101–102).
- **Form and server request:** The form table marks full name, email, telephone, billing address and delivery address required; date of birth is optional (raw lines 34–45). For server `/payments`, the guide asks for the chosen `paymentMethod.type`, shopper name (maximum 32 characters), email, mobile international telephone with country-specific prefixes, addresses with five-character postal codes, country, locale, `lineItems`, shopper reference (minimum three characters) and return URL with protocol and maximum 1024 characters (raw lines 65–112). It says Oney approves only if the `lineItems` total equals `amount.value` (raw line 108). The FR/EUR `facilypay_3x` TEST request is an example; its `+33 1...` telephone does **not** match the prose's FR `+336`/`+337` mobile prefixes, so do not use it as a validated phone-format recipe (raw lines 87–91, 138–203). The Go SDK example parses a date-only birth date with an RFC3339 parser, another example/prose mismatch (raw lines 81–85, 627–630).
- **Optional risk/fee controls:** `additionalData.oneydata.trustFlag` is an optional trusted-shopper signal **only when Oney enables the trust setting on the account**; listed values are 2, 1, 0, -1 and -2. `additionalData.oneydata.merchantPays` optionally overrides the default interest-fee payer configured on the merchant account (true: merchant; false: shopper). Neither field proves an approved credit decision (raw lines 114–135).
- **Redirect and result:** The `/payments` example returns `RedirectShopper` and a redirect `action`; that is not final success. Send the shopper to `action.url`; after return, POST `/payments/details` with URL-decoded `redirectResult`. Use its `resultCode` to present the shopper result and retain `pspReference` for the transaction (raw lines 880–937). The page recommends secure browser handling for mobile redirects; that advice is not an additional API-only requirement (raw lines 896–905).
- **Asynchronous outcome and fulfillment:** `Authorised` is successful in the result table, but shipping follows **successful capture**; `Cancelled` and `Refused` are separate paths. For **FR only**, `Pending` or `Received` can mean no final status, including suspected fraud. If not authorised within 24 hours the payment is automatically cancelled; wait for the **AUTHORISATION webhook** for the final result. The page says ES payments are accepted or rejected immediately (raw lines 939–950). Do not ship merely from a redirect or pending response.
- **Capture and refund:** Capture can be manual or automatic, with or without delay by settings. If captured after **more than six days**, the authorization expires and must be authorised again; the guide does not promise a capture by day six succeeds (raw lines 952–958). Uncaptured payments can be cancelled; captured payments require refund to return funds. It states **EUR 1** minimum refund and refund availability until **13 months after capture**; partial refund uses `/payments/{paymentPspReference}/refunds` and specifies `amount` (raw lines 960–972). This guide does not define a partial-capture procedure; see the overview's capability matrix separately.
- **Testing and live gate:** The test section provides FR and ES test data, FR amount-based result ranges, a separate 10x/12x test flow, country/installment minimum **test** amounts, and a Support route for full-flow testing (raw lines 974–1048). It says live acceptance requires requesting **Oney 3x4x** in live Customer Area (raw lines 1050–1052). The live-request label is narrower than the 6x/10x/12x method types listed earlier; neither the request instruction nor test examples prove live enablement for any installment count.

## Detail locators

- Identity, requirements, form fields and payment-method discovery: pinned raw lines 15–63.
- `/payments` field requirements, Oney line-item total gate, optional risk/fee fields: pinned raw lines 65–135.
- FR/EUR TEST request and versioned SDK examples, including phone and Go date mismatch: pinned raw lines 138–878.
- Redirect, `/payments/details` and FR-only asynchronous result table: pinned raw lines 880–950.
- Capture, cancellation and refund boundaries: pinned raw lines 952–972.
- Test data, minimum test amounts and live request: pinned raw lines 974–1052.

## Related

- [[adyen-online-payments]] — provider checkout architecture.
- [[source-adyen-docs-payment-methods-oney]] — Oney product, entity, region and capability overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/oney/api-only/2026-09-15|Oney API-only guide, captured 2026-09-15]]
