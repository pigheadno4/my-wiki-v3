---
title: "Adyen Mirakl connector payment-flow setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/mirakl/set-up-payment-flows"
raw_files:
  - "adyen/docs/plugins/mirakl/set-up-payment-flows/2026-09-15.md"
tags: [adyen, mirakl, marketplace, payment-splits, refunds, chargebacks]
---

## Overview

This guide describes the marketplace operator's **separately implemented pay-in, capture, refund and chargeback flows** while integrated with Adyen's Mirakl connector. The connector synchronizes account/order-related data but **does not manage marketplace payment flows**. The marketplace needs its own ecommerce payment implementation for seller transactions. The page describes account and balance splits, not a universal merchant-of-record allocation, an executed transaction, or bank-received seller payout.

## Key takeaways

- To keep Mirakl synchronized, the guide says captures and refunds must be performed **from Mirakl**; operations outside Mirakl require manual balance adjustment there. In the described operator process, a pending Mirakl debit is resolved by the operator obtaining pending debits through PA11, seller account-holder/balance-account IDs through S20, and sending an Adyen Checkout `/payments` or eligible capture request with the specified `applicationInfo` and `splits` data. S20 is rate-limited, so the guide suggests maintaining a local shop/account mapping instead of calling it for every transaction.
- Online payment methods are limited to those supported for marketplaces, and a new method must first be requested for the merchant account. Payment funds may be split among platform balance accounts, including the liable balance account. Split data can be sent at payment authorization or at capture **only for methods supporting separate captures**. Multi-seller orders require split entries for all sellers. The split account is a balance-account ID; amount value is in minor units and reference is a unique split identifier. The `PaymentFee` split type needs Adyen contact and has a stated seller-available-balance and initial-payout-failure/retry warning.
- A `CAPTURE` webhook follows processing of the capture request but can be followed by `CAPTURE_FAILED`; likewise a `REFUND` webhook can later be followed by `REFUND_FAILED`. Adyen recommends waiting **15 minutes** before changing Mirakl order status after either webhook because Mirakl order statuses cannot be reverted. That delay is a recommendation for this integration, not a guarantee of finality.
- Mirakl marketplace operators and sellers can issue refunds in Mirakl; its billing cycle adjusts seller balances after a refund. Following a Mirakl-initiated refund, the operator can process and split the refund across platform balance accounts. For chargebacks, the disputed amount can be booked entirely to the platform's liable balance account or according to the payment's original split ratio. The guide routes seller payouts and commissions to a separate page; it does not establish payout or bank receipt here.
- The sample Checkout test request is an example, including a test endpoint and placeholder credentials/account values. Use the linked API references for executable schema and lifecycle details; the sample does not prove a payment or production configuration.

## Detail locators

- Raw lines 15–29: connector exclusion, Mirakl-origin capture/refund synchronization rule, and marketplace payment-method request.
- Raw lines 31–66, `Payments`: balance-account splits, capture-method condition, PA11/S20 identities and rate limit, `applicationInfo`, split fields, `PaymentFee` warning.
- Raw lines 68–117: illustrative Checkout test request; endpoint and values are examples.
- Raw lines 119–143, `Captures` and `Refunds`: webhooks, later failures, Mirakl irreversible order-status timing, billing-cycle balance adjustment.
- Raw lines 145–166, `Chargebacks` and `Next steps`: disputed-amount allocation options and separate payout/commission/reconciliation routes.

## Related

- [[adyen-mirakl]] — connector's seller-onboarding, account sync, balance and payout boundary.
- [[adyen-payouts]] — separate payout lifecycle; not established by this payment-flow setup page.

## Raw Sources

- [[raw/adyen/docs/plugins/mirakl/set-up-payment-flows/2026-09-15|Mirakl payment-flow setup, fetched 2026-09-15]]
