---
title: "Adyen Docs: Point-of-sale solutions"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/solutions"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/solutions/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, standalone-terminals, mobile-payments, plugins]
---

## Overview

Adyen's “Solutions” page is an in-person payments route map, fetched 2026-09-15 with raw metadata last modified 2020-03-16. It presents POS-to-Adyen-terminal Terminal API integration as the main route, plus standalone terminals, mobile solutions, and partner-platform plugins. The page names these paths and sends readers to their separate guides; it does not establish current merchant eligibility, terminal or SDK versions, country coverage, payment-method support, or the behavior of an unread linked integration. [[adyen]] · [[adyen-terminal-api]]

## Key takeaways

- **Integrated terminals:** A POS system communicates with Adyen-supplied, PCI-certified payment terminals through the nexo-based Terminal API. This is the page's main integration route, with a linked checklist for setup; the statement is not a compatibility matrix for all terminal models, markets, or features.
- **Standalone terminals:** Adyen presents direct initiation on an Adyen-supplied standalone terminal as an option that does not require POS development or integration. The page also proposes standalone terminals as a fallback when an integrated POS has an internet-access problem; this is a dated option description, not proof that every network failure leaves a standalone route operational.
- **Mobile solutions:** The described Tap to Pay/card-reader path integrates the POS system with Terminal API, adds Mobile SDK to the POS app, and routes payments through that SDK using the Terminal API specification. The page separately mentions connecting a POS app to an Adyen Payments app that includes Mobile SDK. These are two described paths, not a statement that a specific device, OS, market, or payment method is currently supported.
- **Partner plugins:** A retail or hospitality platform that partners with Adyen may use a plugin; the page says Adyen terminals then communicate directly with the partner platform. Its named partner products and directory are navigation, not evidence of current plugin version, configuration, merchant eligibility, or broader ecommerce checkout behavior.

## Detail locators

- **Overview and Terminal API integration:** raw lines 17–27, including Adyen-provided terminal and nexo descriptions and the separate checklist link.
- **Standalone:** lines 29–35, including direct terminal initiation and the qualified internet-access fallback claim.
- **Mobile:** lines 37–45, separating POS app + Mobile SDK from POS app + Adyen Payments app, and distinguishing Terminal API specification from SDK routing. The linked mobile documentation carries specific requirements.
- **Plugins:** lines 47–53, with partner-platform communication and named examples; consult linked provider pages for current integration and market details.
- This page has no endpoint schema, SDK version, firmware floor, market table, payment-method matrix, or implementation procedure. It covers in-person solution categories, not online ecommerce checkout support.

## Related

- [[adyen-terminal-api]] — integrated terminal messages and the mobile specification boundary
- [[adyen-online-payments]] — separate website/app checkout area

## Related raw API references

The linked Terminal API checklist, standalone, mobile, plugin, partner-directory, and nexo pages were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/solutions/2026-09-15|Adyen POS solutions overview, fetched 2026-09-15]]
