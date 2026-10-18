---
title: "Split Adyen Platforms in-person transactions between balance accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, split-payments, balance-accounts]
---

## Overview

This Adyen for Platforms overview, last modified 2024-04-23 and captured 2026-09-15, routes in-person transaction split instructions between a user's balance accounts and the platform's liable balance account. It distinguishes automatic store split configuration from request-level instructions for authorization, capture, and referenced refund. It names chargeback split purposes but directs chargeback detail to a separate online-payments page. This overview describes booking instructions, not proof that a payment was authorized, funds booked, or a payout completed.

## Key takeaways

- Split configuration profiles can automatically apply to transactions through a user's store. Split instructions in a specific API request override those profiles. If neither route supplies instructions, the page says the entire transaction amount and fees are booked to the platform's liable balance account. A missing `account` within a split instruction also routes that split amount to the liable balance account; these are different fallback conditions.
- The stated per-request integration requires Terminal API with payment terminals or a Mobile solution, in addition to general in-person Platforms requirements. Standalone does not support adding split instructions to individual payments or refunds. This does not rule out automatic store profiles for standalone; their setup belongs to the linked configuration guide.
- Authorization uses a Terminal API payment request; capture uses Checkout API `/payments/{paymentPspReference}/captures`; refunds use Terminal API *referenced* refund requests. Terminal API payment and referenced-refund splits go in `SaleToAcquirerData` as form-encoded key-value pairs or Base64-encoded JSON. Capture uses the original authorization PSP reference and a `splits` array in the Checkout capture request. The `## Split types` prose broadly mentions `SaleToAcquirerData`, but the page's capture-specific instructions use `splits`; follow the operation-specific path.
- The page lists payment booking purposes including sale amount, platform commission, transaction fees, and user top-up; refund purposes include returned sale amount, returned commission, and refund fees. Its chargeback tab lists disputed amount and chargeback fees but does not document an in-person chargeback request or booking sequence. The table identifies `BalanceAccount`, `Commission`, fee components and aggregates, `VAT`, `Surcharge`, and `Tip`; `BalanceAccount` requires an account, amount, and reference, while `Commission` requires amount. See the raw table for other fields and fee variants.
- This overview does not specify split currency units, partial capture/refund rules, original split references, invalid-target behavior, payment-method eligibility, webhook outcome evidence, or settlement ownership. Use its linked operation-specific guides and current API contracts for those details. The user balance account and platform liable balance account are distinct destinations; their mention does not establish Merchant of Record, legal seller, or funds ownership.

## Detail locators

- `## Requirements` and `## Split specific transactions`: Terminal API/Mobile scope, standalone limitation, request-over-profile precedence.
- `## When to provide split instructions`: separate authorization, Checkout capture, referenced refund routes; `### Tab: Chargebacks` lists booking purposes only.
- `## Send split instructions`: Terminal `SaleToAcquirerData` encoding versus capture `splits` array and payment PSP reference.
- `## Split types`: required/recommended fields by split type and omitted-account liable fallback.
- `## Next steps`: linked operation-specific guides for authorization, capture, and refund.

## Related

- [[adyen-platforms]] — main Platforms concept and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/2026-09-15|Adyen split transactions between balance accounts (fetched 2026-09-15)]]
