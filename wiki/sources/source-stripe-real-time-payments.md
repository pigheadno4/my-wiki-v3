---
title: "Stripe: Real-Time Payments Overview"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-real-time-payments-2025.md"
tags: [stripe, real-time-payments, paynow, payto, promptpay, swish, pay-by-bank]
---

## Summary

Overview and support matrices for Stripe's 5 real-time payment methods (Pay by Bank, PayNow, PayTo, PromptPay, Swish). UPI (India) in beta. PayTo is the standout with SetupIntents, setup_future_usage, and Express Checkout Element support.

## Key Details

**5 real-time methods**: Pay by Bank (Brazil), PayNow (Singapore), PayTo (Australia), PromptPay (Thailand), Swish (Sweden). UPI (India) in beta.

**No manual capture** for any method.

**Redirect required**: Pay by Bank and Swish only.

**PayTo standout**: only real-time method with SetupIntents, `setup_future_usage`, and Express Checkout Element.

**PayNow**: also supports Terminal.

**Subscriptions/Invoicing**: only via `send_invoice` collection method.

## Raw Sources

- [[stripe-real-time-payments-2025]] — verbatim webpage content (44 lines)
