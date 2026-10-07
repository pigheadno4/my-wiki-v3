---
title: "Braintree Masterpass Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/overview"
raw_files:
  - "braintree/docs/guides/masterpass/overview-2026-09-16.md"
tags: [braintree, masterpass, mastercard, digital-wallets, secure-remote-commerce]
---

## Overview

This 2026-09-16 [[braintree|Braintree]] website snapshot is a historical overview of Masterpass, a Mastercard digital wallet that the page says let customers use one sign-in for web purchases. It identifies the guide's purpose as processing Masterpass payments through Braintree and routes the method through [[braintree-payment-methods]]. It does not establish current Masterpass or successor availability, merchant enablement, exact SDK behavior, client/server implementation, or payment execution.

## Key takeaways

- The page says Masterpass was replaced by Visa Secure Remote Commerce (SRC) and directs prior Masterpass users to integrate with SRC. That is a captured migration direction, not evidence of a completed or currently safe migration.
- The same notice limits SRC to eligible merchants in a limited release, says its API is subject to change, and directs merchants to contact Braintree to request access. It names Android v2, iOS v4 and JavaScript v3 as the Client SDK generations in which SRC was introduced; those labels apply to the stated SRC history, not to a current package version or to the unversioned Masterpass overview.
- The page describes Masterpass as a Mastercard digital wallet for a single-sign-in web-purchase experience and says Braintree SDKs enabled acceptance alongside other payment methods. These are historical product-purpose statements, not present buyer eligibility, platform availability, account support, client/server procedure, settlement, or funding evidence.

> [!warning] Unresolved successor-support conflict
> This snapshot directs former Masterpass users to limited-release SRC. Separately retained [[source-braintree-payment-methods-secure-remote-commerce|SRC authority]] says Visa Click to Pay/SRC would no longer be supported effective January 20, 2026 while also retaining current-tense limited-release language. Preserve both statements: the collected material does not establish current Masterpass or SRC support, merchant eligibility, or a safe executable migration path.

## Detail locators

- Masterpass replacement and direction to integrate with SRC: opening `**AVAILABILITY**`, raw line 18.
- SRC limited-release eligibility, API-change warning and access-request route: opening `**AVAILABILITY**`, raw line 18.
- Android v2, iOS v4 and JavaScript v3 Client SDK introduction labels for SRC: opening `**AVAILABILITY**`, raw line 18.
- Historical Masterpass identity, single-sign-in web purpose and Braintree processing-guide scope: raw lines 20-25.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Historical product authority: [[source-braintree-articles-guides-payment-methods-masterpass]]
- Successor support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]

## Related raw API references

- [[raw/braintree/articles/guides/payment-methods/masterpass-2026-09-16|Braintree Masterpass support article]] - linked eligibility and availability route; navigation only for this source entry

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/overview-2026-09-16|Braintree Masterpass overview (captured 2026-09-16)]] - complete collected page containing the replacement notice, qualified SRC direction, historical wallet identity and processing-guide purpose
