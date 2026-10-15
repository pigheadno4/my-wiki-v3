---
title: "Adyen instant card funding"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/instant-card-funding"
raw_files:
  - "adyen/docs/online-payments/instant-card-funding/2026-09-15.md"
tags: [adyen, instant-card-funding, card-payments, wallet-top-up, money-transfer, checkout-api]
---

## Overview

This Adyen guide describes **card-sourced funding**: a shopper moves money from a Visa or Mastercard card toward another card, digital wallet or bank account. Examples include prepaid/wallet top-ups and funding a person-to-person transfer. The documented pay-in is a Checkout API `/payments` request with sender and, where applicable, recipient data. It is not an ordinary merchant goods purchase, an outbound card payout, or proof that a downstream P2P transfer completed. The raw metadata says last modified 2025-10-13; the page was captured 2026-09-15. See [[adyen]], [[adyen-online-payments]] and [[adyen-card-payouts]].

## Key takeaways

- **Enablement is gated:** the merchant must submit compliance documents, identify its use case and meet card-scheme compliance requirements, discuss them with its Adyen Account Manager, then contact Support for configuration after completing the compliance process. The page's Visa/Mastercard statement does not prove a particular merchant, card, country, currency, MCC, scheme program or transaction is eligible.
- The `/payments` request must add funding context. The **top-up** table identifies the sender's name, billing address, email and phone plus a unique recipient wallet/account identifier; sender name and address need not be repeated under `fundOrigin` when supplied in the standard `shopperName`/`billingAddress` request fields. The **P2P funding** table also identifies the origin wallet/account and the recipient's name, address and wallet/account identifier. Missing required data can cause refusal. These wallet identifiers are merchant-supplied references, not proof of the destination's financial account ownership or movement of funds after the card pay-in.
- Additional validation applies when Adyen facilitates money transfers **between different entities**; nonconforming data is declined. The page says only ASCII is supported and gives restrictions on name/address placeholders, lengths and repeated values. However its allowed-special-character list includes an em dash, which is non-ASCII; this internal mismatch is unresolved. Use the raw field list for exact constraints and obtain Adyen clarification before treating the em dash as accepted.
- The page's **Partial authorization** paragraph recommends partial authorizations “for online payouts” despite appearing in this instant-card-**funding** guide. It does not establish partial-authorization availability for a particular funding transaction or change the separately documented card-payout flow. The `## See also` link points to instant card payouts, a different outbound operation.
- The example `/payments` payloads contain test-style card and personal data and no response or webhook outcome. They do not establish authorization success, capture, payout timing, end-recipient credit, chargeback allocation, seller/payee or merchant-of-record roles, or a complete P2P money-movement service. The page gives no region, MCC, amount/velocity limit or settlement timetable for the funding product.

## Detail locators

- Lines 14–26: card-source purpose, Visa/Mastercard statement, top-up and P2P funding examples.
- `## Enable instant card funding` (lines 28–36): compliance/use-case and Support configuration gates.
- `## Process an instant card funding transaction` and **Top-up** (lines 38–90): Checkout `/payments`, origin/recipient table, standard-field alternatives and example.
- **Person to person money transfer** (lines 92–156): origin and recipient identity/address/wallet-identifier table and illustrative request.
- `## Data validation` (lines 158–178): different-entity condition, ASCII and detailed value restrictions, including inconsistent em-dash allowance.
- `## Partial authorization` and `## See also` (lines 180–186): payout-worded recommendation and separate instant-card-payout navigation.

## Related

- [[adyen-online-payments]] — Checkout API provider concept and reciprocal funding source route.
- [[adyen-card-payouts]] — distinct outbound card payout operation.
- [[source-adyen-docs-online-payments-online-payouts-instant-payouts]] — separately documented legacy payout flow.

## Raw Sources

- [[raw/adyen/docs/online-payments/instant-card-funding/2026-09-15|Instant card funding, captured 2026-09-15]]
