---
title: "Braintree PINless Debit Optimized Routing: Managing Authorizations"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/pinless-debit/optimized-debit-routing/managing-authorization"
raw_files:
  - "braintree/docs/guides/pinless-debit/optimized-debit-routing/managing-authorization-2026-09-16.md"
tags: [braintree, pinless-debit, optimized-debit-routing, authorization, settlement]
---

## Overview

This captured unversioned [[braintree|Braintree]] webpage describes authorization-management options and limits for transactions routed to debit networks under PINless debit optimized routing. It covers network-specific authorization honor periods and amount changes before or during settlement. The snapshot does not establish current availability, account eligibility, approval, an individual authorization outcome, settlement, or funding.

## Key takeaways

- The captured honor-period table lists STAR at 10 days; ACCEL, MAESTRO, NYCE, PULSE and Visa at 7 days; and Mastercard at 30 days. These are page-stated expiration periods, not proof that a particular account or transaction receives that window.
- An authorization amount cannot be adjusted up or down unless the merchant's industry, card BIN and debit network support the adjustment. The page's network table identifies captured eligible network/MCC combinations and lists their amount limit as "No limit"; it directs merchants to their technical account manager for more detail.
- For settlement submission, the amount must be greater than zero. Settling above the authorized amount requires support from the industry and debit network for a percentage-based settlement adjustment; settling below it causes the transaction object to return the settled amount. The captured network/MCC table supplies the stated percentage limits.
- The page routes Visa- and Mastercard-specific authorization management to a separate article. This source uses settlement-submission terminology and does not independently establish a capture API, current network rules, merchant-specific configuration or successful lifecycle completion.

## Detail locators

- **Scope:** `Managing authorization`, lines 14–16.
- **Authorization honor periods by network:** `Authorization honor period`, lines 19–31.
- **Amount adjustment before settlement:** `Authorization adjustments without settlement`, lines 34–49.
- **Settlement amount adjustment and network/MCC percentage table:** `Authorization adjustments during settlement`, lines 54–69.
- **Separate Visa/Mastercard route:** line 73.

## Related

- [[braintree]]
- [[braintree-payment-methods]] — main provider concept route for PINless debit optimized-routing documentation.

## Raw Sources

- [[raw/braintree/docs/guides/pinless-debit/optimized-debit-routing/managing-authorization-2026-09-16|Braintree — Managing Authorizations (2026-09-16)]]
