---
title: "Adyen Docs: Greece in-person tax signature flow"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/make-a-payment/greece-tax"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/make-a-payment/greece-tax/2026-09-15.md"
tags: [adyen, point-of-sale, greece, terminal-api, aade, e-invoicing]
---

## Overview

This Adyen webpage, last modified 2024-11-28 and captured 2026-09-15, describes its Greek in-person Terminal API payment flow with an e-invoicing-provider signature and an autonomous fallback when the POS cannot reach that provider. It assigns signature retrieval and result handoff to the merchant POS, signature validation/payment processing to the terminal/Adyen, and tax-office forwarding to the selected e-invoicing system. Its dated statements about Greek obligations, standalone terminals, provider support, and compliant fallback are source claims, not a current legal determination or evidence of a merchant's live approval.

## Key takeaways

- The page states a December 31, 2024 Greek POS/terminal/e-invoicing integration obligation and says standalone terminals can no longer be used in Greece. Its documented path is a Terminal API integration on terminal software 1.109.10 or later; autonomous mode needs 1.124 or later. Support must configure the merchant account to Greece and Europe/Athens. These are dated Adyen setup and regulatory statements that require current official confirmation before legal or go-live reliance. See **Greece tax regulations** and **Requirements**.
- In the normal path, the merchant POS obtains a signature from its chosen e-invoicing provider for the target terminal and purchase amount, sends Base64-encoded `aadeData` in `SaleData.SaleToPOIData`, and sets `RequestedAmount` no higher than the signed payable amount. The terminal checks the signature using the provider public key; after processing, it returns a transaction identifier. The POS sends the transaction result to the provider, which forwards it to AADE. Adyen's support for the page's AADE-listed provider route does not mean Adyen owns the merchant POS-to-provider integration. See **How it works**, **Integrate with an e-invoicing provider**, and **Make a payment**.
- `aadeData` includes provider ID, a transaction-unique provider signature, and verification data. For the Terminal API exchange, the page says not to send the signature in a request other than the payment request, yet later directs the POS to send the returned signature to its e-invoicing system after a successful signed payment; it does not reconcile those instructions. The verification-data timestamp must be neither in the future nor older than 24 hours, its `TID` must equal the header `POIID`, and the requested amount must fit the signed amount. On a successful signed-flow payment, save `aadeTransactionID` and `aadeProviderSignature` from `AdditionalResponse` for that POS-to-provider handoff. The autonomous Success example does not show those identifiers. See **Make a payment** and **Errors** for exact fields and failure messages.
- If the POS cannot obtain a provider signature, the page's autonomous flow sends Base64-encoded `aadeData` with `unbound_pos: "1"`. It describes Adyen contacting AADE for this unsigned path; if Adyen cannot reach AADE, `Result` is `Failure` with an autonomous-mode connection message. The normal signed flow resumes when provider connectivity returns. This is a conditional fallback, not proof that an unsigned transaction always succeeds or is currently compliant. See **Make a payment without e-invoicing signature**.
- A referenced refund follows the linked standard `ReversalRequest` route. An unreferenced refund needs another unique provider signature in `aadeData`, or the page's autonomous `unbound_pos` route during provider-connection loss. Detailed refund operation behavior belongs to the linked refund pages. See **Refunds**.
- Both illustrated successful response bodies request EUR 10 but show `AuthorizedAmount` EUR 8 and `Result: Success`; the page does not explain that mismatch. Do not use the examples to infer full authorization, tax reporting completion, capture, or settlement. The listed AADE validation failures return `Failure` and a Base64-encoded `AdditionalResponse` error. See **Make a payment**, **Make a payment without e-invoicing signature**, and **Errors**.

## Detail locators

- **Greece tax regulations** — dated obligation and Adyen's described signature-to-transaction-ID role.
- **Requirements** — Terminal API/firmware gates, standalone limitation, Support merchant-account settings, and provider-integration prerequisite.
- **How it works** — POS, provider, terminal/Adyen, and tax-office handoff sequence.
- **Integrate with an e-invoicing provider** — merchant-owned provider connection and AADE-list route.
- **Make a payment** — `aadeData` fields, request-only signature wording and later provider-result handoff, signature timing/uniqueness, TID/POIID and amount checks, Base64 placement, signed-flow response fields, and illustrative payload.
- **Make a payment without e-invoicing signature** — autonomous `unbound_pos` request, example response, and AADE-unreachable failure.
- **Refunds** — referenced versus unreferenced refund signature/fallback routes.
- **Errors** — terminal validations, including future-dated or older-than-24-hour signature data, and Base64 `AdditionalResponse` messages.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/make-a-payment/greece-tax/2026-09-15|Adyen Docs — Greece tax regulations (2026-09-15)]]
