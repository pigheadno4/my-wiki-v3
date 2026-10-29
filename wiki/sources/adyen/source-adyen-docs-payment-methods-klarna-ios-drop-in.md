---
title: "Klarna iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/klarna/ios-drop-in/2026-09-15.md"
tags: [adyen, klarna, ios, drop-in, sessions, capture, recurring]
---

## Overview

This [[adyen|Adyen]] guide, fetched and last-modified on 2026-09-15, adds Klarna to an existing iOS Drop-in integration. It gives separate Sessions and Advanced server-flow requirements, then payment, capture, tokenization, and test/live instructions. It is method-specific guidance within [[adyen-online-payments]]; the captured examples do not establish current merchant enablement or successful payment execution.

## Key takeaways

- Start with an existing iOS Drop-in integration for the chosen Sessions or Advanced flow and add Klarna in Customer Area. The page calls `/sessions` the default with Drop-in v5.0.0 or later; `/payments` is shown for an additional use case. The Drop-in configuration section says there is no required Klarna-specific client integration for v5.0.0+ or v4.x.x.
- For either server endpoint, the table says Klarna approval depends on `lineItems` totaling `amount.value`, with a `description` per item. `countryCode` must match the billing-address country, and `shopperLocale` is said to match country and currency. `shopperEmail` is marked required with a note saying to include it to defend against potential disputes. Name and billing address are recommended, while delivery address defaults to billing if omitted; a different recipient requires delivery name fields. Some products or business models can require Base64-encoded attachment data in `additionalData.openinvoicedata.merchantData`; the page says not to include test values in the test environment because they cause an error. See the raw parameter tables for exact fields and market-specific Klarna links.
- Capture is conditional. The page permits configuring automatic capture in live Customer Area only when capture delay is immediate and shipping complies with Klarna's 24-hour Scheme Rules. Otherwise, manually capture within 90 days after authorization, even if merchant-account automatic capture is enabled; the authorization expires without manual capture. Its newer manual-capture path is `POST /payments/{paymentPspReference}/captures`, using the original payment PSP reference and required merchant, amount and invoice line items. A `status: received` response is not final: await the CAPTURE webhook and inspect `success`; after failure, review its reason, fix the issue and resubmit.
- The same capture section's optional shipping/tracking and partial-capture subsections use the legacy `/capture` endpoint and `modificationAmount` plus `additionalData.openinvoicedata`, while the preceding manual subsection uses `/payments/{paymentPspReference}/captures`, `amount` and `lineItems`. Treat these as distinct documented request shapes; the page does not reconcile their API versions or show that fields transfer unchanged. It says a partial amount must be less than authorized and the invoice amounts must be correct. Optional shipping/tracking details cannot assign different delivery addresses within one multi-item order.
- Recurring instructions are for `/payments`: create a token with `storePaymentMethod: true` and `shopperReference`; after settlement, receive `recurring.token.created` and its `storedPaymentMethodId` on the server. Future token payments use that ID, the same shopper reference, `shopperInteraction: ContAuth`, a recurring processing model, and the usual Klarna request parameters. The sample future request is specifically Klarna Pay Now with an active shopper, so it does not establish support for every Klarna product or every recurring model.
- Before live use, the page calls for testing, live Customer Area enablement, legal/privacy and presentation review, correct invoice lines/VAT, and an alternative method for shoppers Klarna rejects. It says live tests can be refused by shopper-data, amount and velocity checks bypassed in test. These are page instructions, not proof of live eligibility or approval.

> [!warning] Example and prose mismatch
> The parameter table says `shopperLocale` must match `countryCode` and currency, but both endpoint examples use `en_US` with `SE`/`SEK`. Do not copy that locale combination as a validated market rule; follow the stated matching condition and market-specific Klarna requirements.

## Detail locators

- Existing-flow setup and Customer Area prerequisites: pinned raw lines 15–37. Sessions v5 default and server parameter conditions: lines 39–60; Sessions code examples: 62–755.
- Advanced `/payments` parameter conditions and note: lines 757–774; request examples: 776–1496. Both curl requests are test examples (`/v70/sessions`, `/v72/payments`); other language snippets name their own API library versions.
- No Klarna-specific Drop-in client configuration: lines 1498–1506. Capture gate and 90-day expiry: lines 1508–1510. Newer manual request fields and examples: lines 1512–1968. Received response and CAPTURE webhook finality: lines 1970–2003.
- Optional shipping/tracking and legacy `/capture` shape: lines 2005–2074. Partial-capture conditions: lines 2076–2083. Recurring token lifecycle and Pay Now sample: lines 2085–2197. Test/live gates and Refused result: lines 2199–2226.

## Related

- [[adyen-online-payments]] — main provider integration concept
- [[adyen-tokenization]] — provider token lifecycle concept
- [[source-adyen-docs-online-payments-capture]] — general Adyen capture guidance

## Related raw API references

- [[raw/adyen/docs/payment-methods/klarna/invoice-lines/2026-09-15|Klarna invoice lines and discounts]]
- [[raw/adyen/docs/payment-methods/klarna/airlines/2026-09-15|Klarna for airlines]]
- [[raw/adyen/docs/payment-methods/klarna/raw-responses/2026-09-15|Klarna raw acquirer responses]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/ios-drop-in/2026-09-15|Klarna iOS Drop-in guide, fetched 2026-09-15]]
