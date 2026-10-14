---
title: "Adyen POS card recognition overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/shopper-recognition"
raw_files:
  - "adyen/docs/point-of-sale/shopper-recognition/2026-09-15.md"
tags: [adyen, point-of-sale, card-recognition, card-acquisition, shopper-identifiers]
---

## Overview

Adyen's card-recognition overview, last modified 2020-03-27 and captured 2026-09-15, introduces using payment data to check which card a shopper presents in specific POS journeys. It points to card acquisition for obtaining card and shopper identifiers before a next step, without yet making a payment. The use-case route is [[adyen-card-recognition]]; it is distinct from stored-payment-credential [[adyen-tokenization]]. The overview alone does not establish a person's identity, a universal identifier-matching rule, consent or privacy compliance, current feature eligibility, or an authorized payment.

## Key takeaways

- The page gives **examples**, not blanket capabilities: card acquisition at parking-garage entry and exit to calculate an amount; same-card checking before an unreferenced refund; detecting a gift card before deciding whether to cancel acquisition or offer a later payment discount; and using issuer country/region and card BIN from an acquisition response in a tax-free-shopping scenario. Tax-refund eligibility requires its own rules and evidence.
- Card acquisition is the common preparation step and can return card and shopper identifiers before a subsequent action, without itself making a payment. The overview sends implementers to a separate identifiers guide for what is returned, and to the card-acquisition guide for mechanics. It does not enumerate card alias, PAN, token, fingerprint or shopper-reference field semantics; do not equate those identifiers or treat them as proof of civil identity.
- The separate scenario guides cover card-based identification, same-card check before unreferenced refund, and tax-free shopping. The overview is a navigation page, not evidence that any specific scenario is enabled for a merchant or that a refund, discount or payment succeeded.

## Detail locators

- Raw `# Card recognition` (lines 15–27): definition and four example journeys.
- Raw `## General preparation` (lines 29–34): separate identifier and card-acquisition references; acquisition is described as pre-payment.
- Raw `## What do you want to do?` (lines 36–48): links to card-based identification, before-refund and tax-free scenario guides; read those targets for their own conditions.

## Related

- [[adyen-card-recognition]] — POS recognition use cases and boundaries.
- [[source-adyen-docs-point-of-sale-card-acquisition]] — separately reviewed Terminal API acquisition operation and payment/cancellation boundaries.
- [[adyen-terminal-api]] — POS messaging context.
- [[adyen-tokenization]] — stored payment credentials, a different purpose.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/shopper-recognition/2026-09-15|Card recognition, fetched 2026-09-15]]
