---
title: "Adyen tax-free shopping with secure card capture"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-recognition/tax-free-shopping"
raw_files:
  - "adyen/docs/point-of-sale/shopper-recognition/tax-free-shopping/2026-09-15.md"
tags: [adyen, point-of-sale, shopper-recognition, tax-free-shopping, secure-card-capture, consent]
---

## Overview

Adyen's tax-free-shopping (TFS) guide, captured 2026-09-15, describes **secure card capture** in a Terminal API integration with payment terminals or a Mobile solution. In the documented flow, Adyen sends a notification containing the shopper's **encrypted card number** to the TFS provider to make a card refund easier. The TFS provider refunds the shopper and handles paperwork with authorities; the merchant POS app and provider own eligibility and tax-free-form steps. This is a [[adyen-card-recognition]] source with a separate provider/refund boundary, not evidence that a payment, export validation or tax refund occurred.

## Key takeaways

- The captured page limits this integration to **Global Blue** as TFS provider, and to locations where Terminal API or Mobile solutions are supported **and** VAT refunds are allowed. These are dated product/region constraints, not a current eligibility or tax-law determination. The merchant must arrange the TFS process with the provider, involve the POS-system provider for app support, and configure a **Send card number to <TFS provider>** webhook for both test and live use.
- Adyen's stated role is limited to sharing card data with the provider after consent. The notification contains the transaction PSP reference, encrypted card number and BIN. `taxfree.indicator` in the payment request controls whether it is sent; the Customer Area POS tile can show **Tax Free Indicator** and a provider-returned **Tax Free Identifier** acknowledging card details. Neither field proves that the TFS provider paid a refund or that customs validated export. The shopper may still claim a refund through the provider without this encrypted-card notification.
- For a **payment-terminal Terminal API** flow, the POS app may optionally acquire card data to help check eligibility. The acquisition response can supply issuer country code, BIN, expiry date, payment method and funding source; the POS app checks eligibility locally or with the TFS provider and tells staff the result. This acquisition is an information step, not payment or an automatic eligibility decision. The terminal can show an Adyen-enabled automatic consent screen, or the merchant can use a custom confirmation `InputRequest` or POS UI. A custom/POS-UI flow requires the automatic account flow disabled. If consent is absent or the purchase is ineligible, omit `taxfree.indicator` or set it **false**; the automatic flow changes it to false when the shopper declines. If an acquisition was made, the payment request refers to its returned `POIData.POITransactionID` timestamp and transaction ID.
- For the **Mobile solution**, the merchant checks eligibility against the TFS provider's requirements using the shopper's passport or already-saved CRM details, asks for verbal or POS-screen consent, and sends `taxfree.indicator=true` only when eligible and consented. The passport/CRM checks are merchant-side eligibility inputs in this guide, not fields described as sent in Adyen's encrypted-card webhook. Otherwise the flag is false or omitted.
- After a completed payment, staff give the shopper the POS-issued tax-free form and a receipt. The shopper uses the form and receipt with the TFS provider; the guide describes customs export validation and returning the validated form to the provider. The test section says the TFS provider usually organizes an end-to-end test, asks merchants to agree on allowed test-card PANs/BINs, and checks for the provider identifier in Customer Area; an empty identifier goes to the provider for investigation. Sample `Result: Success`, amounts and card data are examples, not observed payment or refund proof.

## Detail locators

- Raw `# Tax-free shopping with secure card capture`, `## Requirements` and `## How it works` (lines 15–82): actor boundaries, Global Blue and country/VAT limits, separate payment-terminal and Mobile consent/eligibility flows, and form/customs handoff.
- Raw `## Set up tax-free shopping` and `## Set up notifications to your TFS provider` (lines 84–133): provider/POS setup, automatic consent enablement versus custom flow, issuer-data settings for terminal route, webhook payload, flag control and Customer Area acknowledgement. The page names no general tax-refund guarantee or current data-retention policy.
- Raw `### 1. Optional: Acquire card details` (lines 147–269): Terminal API CardAcquisition request and response locators for `POIData.POITransactionID`, issuer country, BIN, expiry, payment method and funding source. Example values and partially malformed sample JSON are not a schema guarantee.
- Raw `### 2. Optional: Use a custom input request to ask for consent` (lines 270–380): automatic-flow disablement, confirmation prompt and `Input.ConfirmedFlag` meaning.
- Raw `### 3. Make a payment` (lines 382–548) and `### Make a TFS payment` (lines 552–653): `SaleToAcquirerData` flag placement and encoding, conditional acquisition reference, automatic-consent response, terminal versus Mobile payment examples and staff form/receipt step.
- Raw `## Test the tax-free flow` (lines 655–667): provider-led test, eligible BIN/allowed test PAN, Customer Area identifier check and empty-field escalation. Linked card-acquisition, input and notification pages under `## See also` are navigation only.

## Related

- [[adyen-card-recognition]] — provider shopper-recognition route; this source covers tax-free secure card capture.
- [[adyen-terminal-api]] — terminal payment, acquisition and input request interface.
- [[adyen-mobile-pos]] — Mobile solution route named by the guide.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-recognition/tax-free-shopping/2026-09-15|Tax-free shopping with secure card capture, fetched 2026-09-15]]
