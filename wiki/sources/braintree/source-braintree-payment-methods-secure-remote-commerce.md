---
title: "Braintree Secure Remote Commerce"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/payment-methods/secure-remote-commerce"
raw_files:
  - "braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16.md"
tags: [braintree, secure-remote-commerce, click-to-pay, digital-wallets, payment-methods]
---

## Overview

This collected Braintree guide describes Secure Remote Commerce (SRC), presented to customers as Click to Pay, as a Visa single-sign-in digital wallet for stored major debit and credit cards used on websites or mobile apps. It is a retrieval route for the page's merchant and SDK prerequisites, credit-card-like processing, dispute and fraud-tool routes, vaulting and recurring-billing statement, and an unresolved support-status conflict; the 2026-09-16 snapshot does not establish current availability.

## Key takeaways

- The opening note says Visa Click to Pay (Secure Remote Commerce) would no longer be supported effective January 20, 2026, and that transactions attempted after that date would receive a `Payment method not supported` error and risk decline.
- The same page also describes SRC in current-tense limited-release language. It names merchant locations, requires eligible merchants to use iOS v4 or JavaScript v3 SDKs, and directs merchants to contact Braintree to request limited-release access. These statements do not resolve the end-of-support notice or establish that an individual merchant can currently enable SRC.
- The page says SRC transactions process and settle like credit-card transactions and use the same pricing as other credit-card transactions. It routes disputes according to the merchant-account setup, names compatible fraud tools and 3D Secure, and says SRC payment methods can be vaulted and used for recurring billing. Use the exact raw sections before relying on those behaviors for a specific account.

## Evidence boundaries

> [!warning] Unresolved support-status conflict
> The guide's opening note says Visa Click to Pay (Secure Remote Commerce) would no longer be supported after January 20, 2026, while its availability and setup sections say SRC is currently in limited release and invite merchants to request access. Preserve both statements: collection success, current-tense wording and the stored snapshot do not resolve the conflict or prove current support.

## Detail locators

- End-of-support date, attempted-transaction error and decline risk: opening `**NOTE**`, lines 14-15.
- Replacement context, Click to Pay identity and stored-card purpose: first `## Availability`, lines 21-25.
- Merchant-country list, iOS v4 or JavaScript v3 requirement and limited-release access route: second `## Availability`, lines 28-48.
- Supported wallet card brands: `## Customer availability`, lines 51-60.
- Credit-card-like processing and pricing: `## Processing` and `### Fees`, lines 63-70.
- Dispute, fraud-tool, 3D Secure, vaulting and recurring-billing routes: lines 73-85.
- Limited-release contact and developer-docs route: `## Setup`, lines 88-90.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Authentication route named by the guide: [[braintree-3d-secure]]

## Raw Sources

- [[raw/braintree/articles/guides/payment-methods/secure-remote-commerce-2026-09-16|Braintree Secure Remote Commerce guide]] - complete collected page covering the support notice, Click to Pay identity, limited-release prerequisites, processing, disputes, fraud tools, vaulting, recurring billing and setup route
