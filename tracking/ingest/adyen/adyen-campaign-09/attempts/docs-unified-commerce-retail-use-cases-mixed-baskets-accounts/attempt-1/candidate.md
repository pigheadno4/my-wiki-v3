---
title: "Adyen account structures for mixed baskets"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/retail-use-cases/mixed-baskets-accounts"
raw_files:
  - "adyen/docs/unified-commerce/retail-use-cases/mixed-baskets-accounts/2026-09-15.md"
tags: [adyen, unified-commerce, mixed-baskets, merchant-accounts, reconciliation]
---

## Overview

This 2026-09-15 Adyen guide compares account structures for a **mixed basket** containing online items offered on an ecommerce site and in-store items available in a physical store. It applies to merchants with both online and in-person payment channels. The choice changes how the basket is split into payment requests, which configured methods each channel uses, and how sales are attributed and reconciled. Adyen recommends discussing the structure with an implementation engineer or account manager before choosing one.

## Account-structure options

- **One merchant account without stores:** The same merchant account handles ecommerce and POS transactions. The guide says to authorize the full amount for all items, and to use separate partial capture requests if items are delivered or picked up at different times. Setup is simple, but configurations, terminals and credentials are more complex, and ecommerce/POS transactions are not separated in reconciliation. See `One merchant account without stores`.
- **Separate merchant accounts:** One ecommerce account and one POS account require **two payment requests**. Each portion uses methods configured for its account (or a store under the POS account). Reconciliation is separate by merchant account. See `Separate merchant accounts`.
- **One merchant account with POS stores:** The combined account has POS stores and still requires **two payment requests**, both processed through that account. Online items use account-level methods; in-store items use methods configured for the POS store. Methods need priorities, and the two channels can be distinguished within the same reconciliation file. See `One merchant account with POS stores`.
- **One merchant account with ecommerce and POS stores:** The combined account has separate ecommerce and POS stores, again with **two payment requests** through the same merchant account. Each portion uses methods configured for its relevant store; reconciliation remains within the merchant account. See `One merchant account with ecommerce and POS stores`.

## Evidence boundary

This page concerns Adyen merchant-account/store configuration, payment-request count, method setup and reconciliation. It does not name the legal entity that sells each item, assign merchant-of-record responsibility, state settlement accounts or payout recipients, or describe a full funds flow. One combined order or merchant account must not be read as proof of one payment, one legal entity, one settlement destination, or a completed capture. The separate linked retail use-case pages are navigation until read on their own.

## Detail locators

- `Requirements`: the dual online/in-person channel scope and linked account-structure setup guides.
- Four account-structure headings: diagrams, capture timing, payment-request counts, method configuration and reconciliation consequences.
- `See also`: click-and-collect and endless-aisle scenario routes; no additional behavior is inferred from their titles.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[adyen-payment-capture]]

## Raw Sources

- [[raw/adyen/docs/unified-commerce/retail-use-cases/mixed-baskets-accounts/2026-09-15|Adyen mixed-basket account structures, 2026-09-15 snapshot]]
