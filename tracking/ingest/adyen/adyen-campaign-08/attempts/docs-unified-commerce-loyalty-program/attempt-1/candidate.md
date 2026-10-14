---
title: "Adyen Unified Commerce shopper loyalty overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/loyalty-program"
raw_files:
  - "adyen/docs/unified-commerce/loyalty-program/2026-09-15.md"
tags: [adyen, unified-commerce, loyalty, shopper-recognition, customer-profiles, data-privacy]
---

## Overview

Adyen's Shopper loyalty overview, captured 2026-09-15, introduces a merchant-run loyalty pattern using payment-response identifiers to recognize a shopper or presented card and decide what benefit to offer. It sits under [[adyen-unified-commerce]], with a related [[adyen-pos-loyalty]] route for in-store use. The page gives examples and sends readers to separate profile-creation and customer-recognition guides; it does not itself define an API request, enrollment transaction, reward ledger or completed payment.

## Key takeaways

- In **payment-linked loyalty**, Adyen's platform returns identifiers in API responses; the merchant uses them to look up its loyalty-program record and chooses any discount or reward. The other example is purchase-history-based product recommendations using the merchant backend's lookup. These are possible uses, not automatic Adyen reward calculation, benefit application or evidence that a shopper made a purchase.
- The page distinguishes a **card alias**, which recognizes a presented payment card, from merchant-created identifiers returned in API responses that can be linked to an individual in the merchant's own system. This is merchant profile association, not a claim that the card alias establishes civil identity or that all identifiers are interchangeable, stable across cards/channels or usable to charge. Exact identifier definitions and matching mechanics belong to the linked detailed guides.
- The stated prerequisite is a merchant **backend customer-profile system** containing card and shopper identifiers together with use-case data such as purchase history. The page does not say Adyen automatically creates, merges or maintains those merchant profiles. Its next-step links are **Create customer profiles** and **Recognize customers**, the latter explicitly spanning online and in-person purchase contexts; their detailed data flow must be read separately.
- Before storing customer or payment data, the page advises reviewing applicable regional privacy rules with legal counsel or an accredited third party, asking the shopper's **explicit permission** to store data, and explaining its intended use. A website terms page or terminal interaction is offered as a possible collection route, not proof of a valid consent record. The linked **Data Protection API** is described for deleting customer-related data stored **with Adyen** after a removal request; it does not cover the merchant's own CRM copies by itself. This overview is not legal advice or evidence of consent, retention, erasure or payment success.

## Detail locators

- Raw `# Shopper loyalty` (lines 15–25): merchant loyalty examples, API-response identifiers, merchant lookup and card-alias versus own-identifier framing. It does not enumerate identifier fields or API versions.
- Raw `## Requirements` (lines 27–31): merchant backend profile and data prerequisites.
- Raw `## Data privacy` (lines 33–40): regional/privacy review, explicit permission and intended-use disclosure, plus Data Protection API scope for Adyen-stored data.
- Raw `## Next steps` (lines 42–54): links to profile creation and online/in-person recognition. These are navigation, not imported child-guide behavior.

## Related

- [[adyen-unified-commerce]] — primary cross-channel merchant concept.
- [[adyen-pos-loyalty]] — in-store recognition and loyalty route.
- [[adyen-card-recognition]] — card alias recognition boundary.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/unified-commerce/loyalty-program/2026-09-15|Shopper loyalty overview, fetched 2026-09-15]]
