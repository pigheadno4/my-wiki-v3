---
title: "Adyen Unified Commerce shopper engagement"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/shopper-engagement"
raw_files:
  - "adyen/docs/unified-commerce/shopper-engagement/2026-09-15.md"
tags: [adyen, unified-commerce, shopper-engagement, loyalty, digital-receipts, privacy]
---

## Overview

Adyen's Unified Commerce shopper-engagement overview, last modified 2021-07-06 and captured 2026-09-15, groups ways a merchant might personalize online and in-person interactions: terminal prompts and display, payment-detail-based loyalty recognition, digital receipts, donations and localization. It routes readers to separate terminal-interaction, loyalty and digital-receipt guides. The overview is a feature map, not proof that a merchant has matched a shopper across channels, collected consent, delivered a receipt or completed a financial action. [[adyen]] [[adyen-unified-commerce]]

## Key takeaways

- Bespoke terminal interaction uses POS-app Terminal API **Input** requests to collect information or **Display** requests to show information. The page names possible consent questions, email/phone collection, QR codes and marketing content, but gives no request schema, response semantics, proof-of-consent model or data handling workflow. The specific terminal operation routes belong to [[adyen-pos-shopper-engagement]].
- Loyalty is presented as recognizing program members from payment details returned in Adyen API responses through a tokenization feature. That is a described possibility, not automatic identity matching or proof that a cardholder joined a program. The linked loyalty guide owns identifier and eligibility conditions.
- For digital receipts, the page describes emailing or texting in-person shoppers instead of printing: recognize an existing customer from the payment request, or ask a new customer for an email address or phone number. It does not specify delivery ownership, address verification, shopper consent capture or an actual send. Donations through Giving and localization of language/payment methods are additional overview routes; this page does not specify their request or settlement behavior.
- Before storing customer data, including payment data, the guide tells merchants to consider privacy rules, consult legal or qualified advice, ask for explicit permission and explain intended use. It says Adyen's Data Protection API can remove customer-related data **stored with Adyen** upon a removal request; that does not establish deletion from a merchant CRM or prove a request has been fulfilled. The 2021-modified snapshot is not current legal advice or proof of compliance.

## Detail locators

- Raw `# Shopper engagement` (lines 15–34): merchant-facing feature examples and the distinct terminal, loyalty, receipt, donation and localization routes.
- Raw `## Data privacy` (lines 36–43): explicit-permission and intended-use guidance, jurisdiction review, and scope of Adyen-held data removal.
- Raw `## Next steps` (lines 45–57): links to terminal interaction, loyalty and digital receipt guides; their mechanisms require their own evidence.

## Related

- [[adyen-unified-commerce]] — cross-channel merchant offering and engagement route.
- [[adyen-pos-shopper-engagement]] — specific POS terminal Input/Display interactions.
- [[adyen-terminal-api]] — terminal message architecture; no message payload is specified here.
- [[adyen]] — provider context.

## Related raw API references

Navigation named in this overview, not further behavior reviewed for this entry:

- Bespoke terminal interaction — https://docs.adyen.com/unified-commerce/terminal-interaction
- Loyalty — https://docs.adyen.com/unified-commerce/loyalty-program
- Digital receipts — https://docs.adyen.com/unified-commerce/digital-receipts
- Data Protection API — https://docs.adyen.com/development-resources/data-protection-api

## Raw Sources

- [[raw/adyen/docs/unified-commerce/shopper-engagement/2026-09-15|Shopper engagement, fetched 2026-09-15]]
