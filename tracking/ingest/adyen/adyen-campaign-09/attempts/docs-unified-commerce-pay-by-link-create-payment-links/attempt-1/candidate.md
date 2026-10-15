---
title: "Adyen Pay by Link creation overview"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/pay-by-link/create-payment-links"
raw_files:
  - "adyen/docs/unified-commerce/pay-by-link/create-payment-links/2026-09-15.md"
tags: [adyen, pay-by-link, payment-links, hosted-payments, link-expiry, unified-commerce]
---

## Overview

This Adyen Pay by Link overview compares creating payment links through the **Pay by Link API**, **Customer Area**, and **iOS app**, then explains the shopper link, link lifetime and payment-result routes. Customer Area and app creation need no development work; the API path supports additional use cases. The page was captured 2026-09-15 but its metadata says last modified 2024-08-28. See [[adyen]], [[adyen-unified-commerce]] and [[source-adyen-docs-unified-commerce-pay-by-link]].

## Key takeaways

- A merchant supplies order context such as amount, currency and country/region, sends the link by email or chat, and the shopper opens an Adyen payment page showing methods available in that country/region. After the shopper completes the payment, the guide points to a webhook or email result route. Link creation, sending and opening do not themselves prove payment authorization, capture or settlement.
- The comparison table marks subscription tokenization, forced expiry, reusable links and page customization for all three creation channels. It marks saved-card display and buy-now-pay-later for API creation, and email service for Customer Area. This is a dated capability matrix, not proof that a particular account, shopper or method is enabled. **BNPL remains unresolved across related pages:** the supported-method matrix marks certain BNPL methods for Customer Area, while the Customer Area creation guide says that channel excludes BNPL. Do not use this page to assert blanket BNPL availability; check the specific method/account route.
- By default, a link expires after **24 hours** and supports **one successful payment**. The expiry can be extended to at most **70 days from creation**; five unsuccessful attempts on the same link expire it earlier. The guide allows overriding default expiry and non-reusability at creation, for example to reuse a donation link. Link expiry and reuse are link controls, not a refund, authorization-expiry or funds-capture rule. The related Pay by Link overview separately says links are removed automatically after three months.
- Pay by Link payments are standard ecommerce payments subject to the merchant account's risk and capture settings. If the account uses manual capture, the merchant must also capture Pay by Link payments; a payment result message alone should not be treated as completed capture. The page's broad 3D Secure and liability-shift language is dated and does not prove a particular transaction's authentication, financial authorization or liability treatment.
- Tokenization in the table is a capability label, not evidence that a shopper consented or that a stored credential was created. Follow the channel-specific creation guides for consent, roles, API fields, notification semantics and actual outcomes.

## Detail locators

- Lines 19–29: creation-channel comparison, including tokenization, forced expiry, reuse, saved-card display, BNPL and email-service marks.
- `## How it works` (lines 31–37): create/send/open steps, country/region method presentation and webhook/email result route.
- `## Link expiry and reusability` (lines 39–45): 24-hour default, 70-day maximum, five-failure early expiry, one-success default and override.
- `## Risk and capture settings` (lines 47–51): ecommerce account settings, manual capture and dated 3DS/liability statement.
- Lines 53–69: Customer Area creation-settings and API/Customer Area child-guide navigation.

## Related

- [[adyen-unified-commerce]] — provider concept and reciprocal source route.
- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-customer-area]] — Customer Area roles, link status, consent and payment outcome distinctions.
- [[source-adyen-docs-unified-commerce-pay-by-link-supported-payment-methods]] — dated method/channel matrix and BNPL conflict.
- [[adyen-payment-capture]] — authorization and manual-capture lifecycle.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/pay-by-link/create-payment-links/2026-09-15|Create payment links, captured 2026-09-15]]
