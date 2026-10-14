---
title: "Adyen Unified Commerce digital receipts for in-person payments"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/digital-receipts"
raw_files:
  - "adyen/docs/unified-commerce/digital-receipts/2026-09-15.md"
tags: [adyen, unified-commerce, point-of-sale, digital-receipts, shopper-recognition, email]
---

## Overview

Adyen's digital-receipts guide, captured 2026-09-15, describes an **in-person** merchant journey using Adyen-supplied payment terminals to recognize a returning customer, ask whether they want an emailed receipt, and then use a merchant CRM or email tool to send a receipt. It belongs to [[adyen-unified-commerce]] and uses terminal shopper input described by [[adyen-pos-shopper-engagement]]. The merchant must have software to generate a receipt from a Terminal API payment response and deliver it to the email address; the terminal prompt and Adyen response do not themselves send the email.

## Key takeaways

- The prerequisites are cross-channel customer-profile creation and returning-customer recognition, plus merchant software that builds a receipt from the Terminal API `PaymentReceipt` data and sends it. The flow starts with a **CardAcquisition** request; this pre-payment response can include a `shopperReference` and, only if previously stored with Adyen, a `shopperEmail` in `AdditionalResponse` (Base64 JSON or form-encoded key-value pairs). An absent `shopperReference` means the card is unrecognized; the shopper may be new **or a returning customer using a new card**. The merchant can compare a collected email against its customer database. Saving a newly presented card is a separately asked choice, not a consequence of receipt preference.
- When an email is already known, the POS app can send a Terminal API **GetConfirmation** input request displaying that address on the Adyen terminal and asking whether the shopper wants the receipt emailed. `Input.ConfirmedFlag=true` records the shopper's **receipt preference** in this flow. It is not payment authorization or general marketing consent. The page also allows staff to ask and enter the address in the POS app. Displaying an existing email and collecting a new one are personal-data touchpoints; the guide does not specify a comprehensive privacy, retention or legal-consent policy.
- When no email is linked, the guide first asks whether the shopper wants an emailed receipt. If yes, collect the email on the terminal's on-screen keyboard through the linked profile flow and create a customer profile; if no, continue to payment with the paper-receipt preference. The page points to the separate create-profile documentation for its exact collection and payment parameters. Do not infer that the confirmation request itself stores or validates the address.
- The POS app continues with a Terminal API payment request. The illustrated known-customer request includes a `CardAcquisitionReference`; a new customer's email/profile parameters are delegated to the linked create-profile guide. The payment response can contain `shopperEmail` in `AdditionalResponse` and receipt material in `PaymentReceipt`; the **merchant's CRM or email tool** uses that email and data to generate and send the receipt. The example's `Result: Success` and EUR 10.99 amount are sample data, not evidence of an executed payment or delivered email. The linked compliant-receipt guide must be read for actual receipt-content duties.

## Detail locators

- Raw `# Digital receipts` and `## Requirements` (lines 15–28): in-person terminal scope and merchant profile/receipt-generation/delivery prerequisites. No terminal model, software version or credential role is established by this page.
- Raw `## Step 1: Recognize customer` (lines 30–108): CardAcquisition request/response, `AdditionalResponse` formats, `shopperReference`/`shopperEmail` interpretation and new-card ambiguity. Example alias, email, IDs and amount are illustrative.
- Raw `## Step 2: Request customer input`, `### Email address is known` and `### Email address is unknown` (lines 110–263): known-email display, GetConfirmation, `Input.ConfirmedFlag`, staff/POS alternative and linked new-email/profile collection route. The prompt is a receipt-channel choice; it does not establish broader consent.
- Raw `## Step 3: Continue with payment` (lines 265–340): merchant POS payment request, example acquisition reference, payment-response email and `PaymentReceipt`, then CRM/email-tool delivery. The compliance link is navigation, not evidence of a compliant merchant receipt.

## Related

- [[adyen-unified-commerce]] — primary merchant cross-channel journey.
- [[adyen-pos-shopper-engagement]] — terminal GetConfirmation shopper input.
- [[adyen-card-recognition]] — pre-payment card-recognition context.
- [[adyen-terminal-api]] — acquisition, input and payment message boundary.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/digital-receipts/2026-09-15|Digital receipts, fetched 2026-09-15]]
