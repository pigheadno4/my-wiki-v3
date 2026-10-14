---
title: "Adyen Unified Commerce bespoke terminal interaction"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/terminal-interaction"
raw_files:
  - "adyen/docs/unified-commerce/terminal-interaction/2026-09-15.md"
tags: [adyen, unified-commerce, point-of-sale, shopper-engagement, terminal-api, data-privacy]
---

## Overview

Adyen's bespoke-terminal-interaction overview, captured 2026-09-15, describes using **Terminal API Input requests** to collect customer or staff responses and **Display requests** to show content on payment-terminal screens. The primary route is [[adyen-unified-commerce]], with a narrower [[adyen-pos-shopper-engagement]] route for terminal interaction. This is merchant-directed interaction, not a Checkout API guide or evidence that any payment, enrollment, consent record or legal obligation was completed.

## Key takeaways

- The stated integration requirement is Terminal API with **cloud or local communications**. For Input requests, the merchant must implement **backend logic to process collected input**. The page says this input communication is between the merchant POS app and terminal and does not involve Adyen's backend; treat that as its stated interaction/data-processing boundary, while architecture-specific transport remains in the linked Terminal API guides. It gives no terminal-model, software-version, account-role or session-lifetime contract.
- Input requests can ask for confirmation, signature, one or multiple menu choices, whole-number digits, an amount with two decimal places, phone number, 0–10 rating or text such as email. The user responds through terminal keypad/on-screen controls. The page places input before or after payment, or in a shopper-recognition flow, but an input value or confirmation is not by itself a payment authorization, stored profile, verified identity or durable consent record. The merchant must supply prompt text and process the response.
- Display requests show an image, a QR code with a URL, or a **virtual receipt/purchase overview before payment**. They are presented outside a payment flow in this overview. Showing the purchase overview is distinct from generating a final paid receipt or proving that a shopper scanned a QR code. Device- and format-specific behavior belongs to the linked Display guides; the images and use cases here are examples.
- Before storing customer or payment data, the page advises reviewing applicable regional privacy rules with legal counsel or an accredited third party, obtaining the customer's **explicit permission to store data**, and explaining the intended use. The terminal may be one way to ask, but a sample prompt is not proof of compliant consent collection. The linked **Data Protection API** is described for removing customer-related data stored **with Adyen** after a removal request; it does not establish deletion of the merchant's own POS/CRM copies. This source gives privacy guidance, not legal advice or a full retention/deletion design.

## Detail locators

- Raw `# Bespoke interaction on the terminal` and `## Requirements` (lines 15–30): Input versus Display purpose, Terminal API cloud/local integration, merchant backend processing and privacy prerequisite.
- Raw `### Data privacy` (lines 32–39): regional/legal review, explicit permission and intended-use disclosure, plus Data Protection API scope for Adyen-stored customer data.
- Raw `## Collect information` (lines 41–71): input-type navigation, user controls, timing around payment, and the page's POS-to-terminal/merchant-processing statement. Linked Input pages require separate reading for exact request/response behavior.
- Raw `## Show information` (lines 73–91): image/QR/purchase-overview examples and links to Display guides. `## See also` (lines 93–97) is navigation only; this overview does not define Checkout API, specific device support or actual shopper action.

## Related

- [[adyen-unified-commerce]] — primary merchant cross-channel concept.
- [[adyen-pos-shopper-engagement]] — terminal Input/Display interaction route.
- [[adyen-terminal-api]] — local/cloud message and payment boundaries.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/terminal-interaction/2026-09-15|Bespoke interaction on the terminal, fetched 2026-09-15]]
