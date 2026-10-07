---
title: "Braintree In-Person Solution Coverage"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/about/solution-coverage"
raw_files:
  - "braintree/in-person/about/solution-coverage-2026-09-16.md"
tags: [braintree, in-person, payment-methods, card-reader, geography]
---

## Overview

This collected, unversioned [[braintree|Braintree]] website page is a coverage overview for the Braintree In-Person solution. It catalogs the page's captured card brands, digital wallets, QR-code methods, payment entry modes, and supported U.S. geographies.

> [!warning] Snapshot and scope boundary
> This is Braintree In-Person provider documentation fetched on 2026-09-16, not a current availability or merchant/account-eligibility determination. The page does not state supported currencies or distinguish Sandbox from Production, and its lists do not prove enablement, reader compatibility, or successful payment execution for a particular merchant or location.

## Key takeaways

- The captured credit-card list is Visa, Mastercard, Discover, AMEX, JCB, and China Union Pay; the debit-card list is Visa, Mastercard, Discover, and AMEX. For AMEX merchants over the annual AMEX volume threshold, the page says a direct AMEX contract and provision of AMEX Service Establishment identifiers to Braintree may be required.
- Apple Pay, Google Pay, Fitbit Pay, Samsung Pay, and Garmin Pay are listed as digital wallets supported natively for in-store transactions. The page says no additional development is required by the merchant or POS provider because the Braintree card reader handles the wallet interaction; this snapshot statement remains subject to the scope boundary above.
- PayPal and Venmo are listed as QR-code-based payment methods, with implementation details routed to the separate PayPal and Venmo QRC guide. The page's captured entry modes are EMV chip, magstripe, contactless NFC, and PayPal/Venmo QR-code scanning.
- The captured geography statement covers the entire United States, Puerto Rico, and the US Virgin Islands. The page invites conversations about possible use cases in other countries, but does not state that those countries are supported.
- Puerto Rican ATH debit cards are excluded when they are not co-branded with a major processing network.

## Detail locators

- Page purpose: introduction, raw line 16.
- Captured credit-card and debit-card lists, including the conditional AMEX direct-contract and Service Establishment identifier warning: `## Payment Methods Overview`, `### Credit Cards Supported`, and `### Debit Cards Supported`, raw lines 19-32.
- Native in-store digital-wallet statement and the Apple Pay, Google Pay, Fitbit Pay, Samsung Pay, and Garmin Pay list: `### Digital Wallets Supported`, raw lines 33-37.
- PayPal/Venmo QR-code list and route to the separate QRC guide: `### QR Code-Based Payment Methods`, raw lines 38-42.
- EMV chip, magstripe, contactless NFC, and PayPal/Venmo QR-code-scanning list: `## Entry Modes Supported`, raw lines 43-45.
- United States, Puerto Rico, and US Virgin Islands coverage statement, other-country conversation language, and the non-co-branded Puerto Rican ATH debit-card exclusion: `## Countries Supported`, raw lines 46-53.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/guides/paypal-and-venmo-qrc-2026-09-16|PayPal and Venmo QRC]] - linked implementation navigation only; not read as evidence for this entry
- [[raw/braintree/in-person/about/technical-overview-2026-09-16|Technical Overview]] - final navigation only; not read as supporting evidence for this entry
- [[raw/braintree/in-person/hardware/verifone-p400-2026-09-16|Verifone P400]] - final navigation only; not read as supporting evidence for this entry

## Raw Sources

- [[raw/braintree/in-person/about/solution-coverage-2026-09-16|Braintree In-Person Solution Coverage (fetched 2026-09-16)]]
