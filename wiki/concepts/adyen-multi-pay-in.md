---
title: "Adyen multi pay-in"
type: concept
category: technology
tags: [adyen, platforms, multi-pay-in, third-party-payments, balance-accounts]
---

## Definition

Adyen multi pay-in is an Adyen for Platforms online-payment service for consolidating Adyen-acquired and third-party pay-in-partner volume within a balance platform. Third-party partner payouts reach a distinct multi pay-in account, which the 2026-09-15 overview says Adyen legally holds solely for users' benefit until allocation to user and platform liable balance accounts. The platform must allocate received funds within 24 hours. This service does not support separate authorization and capture. [[source-adyen-docs-platforms-multi-pay-in]]

## Evidence boundary

The overview requires Checkout/Transfers API credentials, transfer and/or transaction webhooks, and account-holder send/receive balance-account capabilities. It says a request without split instructions books all funds and fees to the platform liable balance account. The pay-in partner generally handles the customer's external refund while Adyen handles the balance-account debit and multi pay-in offset. The overview does not prove account or partner enablement, Merchant-of-Record status, exact legal ownership of a particular payment, regional/currency support, successful allocation, payout or customer receipt. Its refund diagram mixes EUR deductions with a USD transfer; treat example values as illustrative.

## Sources

- [[source-adyen-docs-platforms-multi-pay-in]] — 2026-09-15 service overview, prerequisites, 24-hour allocation rule, account role and refund boundary.

## Related

- [[adyen-platforms]] — broader platform account and payment context.
- [[source-adyen-docs-platforms-multi-pay-in-payments]] — allocation request and event detail.
- [[source-adyen-docs-platforms-multi-pay-in-refunds]] — refund request and event detail.
- [[source-adyen-docs-platforms-multi-pay-in-top-up-multi-pay-in]] — internal top-up route.
