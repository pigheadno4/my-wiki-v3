---
title: "Stripe Docs — UPI on Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-upi-on-link-2025.md"
tags: [stripe, link, upi, india, inr, us-only, real-time-payments, qr-code]
---

## Summary

Guide for UPI (India's real-time payment system) on Link. US businesses can accept UPI payments from Indian customers via Link with zero integration changes.

## Key Facts

- **US businesses only**, INR only; 1–100,000 INR; one-time + on-session only
- **Supported integrations**: Payment Links, Stripe Checkout (Hosted), Elements only
- **Device-specific UX**: desktop → QR code to scan with UPI app; mobile → list of UPI apps → redirect to selected app
- **Saved details**: name, address, virtual payment address stored in Link account

## Refunds

- Window: up to **60 days** after original payment
- Async; up to **7 business days** to complete
- Webhooks: `refund.updated` / `refund.failed`
- Failed refunds: amount returned to Stripe balance; merchant must arrange alternative

## Disputes

Cannot contest — if bank/PSP accepts customer's return request, Stripe immediately removes funds from account. Low fraud risk (authentication required), but disputes may occur for debited-but-failed transactions or goods/services issues.

## Related Pages

- [[stripe-link]] — Link concept page (UPI on Link section)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-upi-on-link-2025]] — verbatim webpage content (61 lines)
