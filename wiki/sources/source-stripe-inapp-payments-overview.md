---
title: "Build an In-App Payments Integration"
type: source
date_ingested: 2026-04-22
original_format: notes
raw_files:
  - "stripe-inapp-payments-overview-2025.md"
tags: [stripe, mobile, ios, android, react-native, payment-sheet, flow-controller, payment-element, in-app-payments, setup-future-usage]
---

## Summary

Overview of Stripe's In-App Payments for iOS, Android, and React Native. Covers three UI options and three API patterns for charging customers in mobile apps.

## Three UI Options

| UI | Integration effort | Key characteristic |
| --- | --- | --- |
| **Payment Sheet** | Low code | All-in-one sheet (display + collect + confirm) |
| **Flow Controller** | Some code | Sheet for selection; you control confirmation UI |
| **Payment Element** | Some code | Embeddable view — embed payment methods anywhere |

Payment Sheet recommended for most use cases. Supports 50+ Appearance API customizations.

## Three API Patterns

### PaymentIntent — Charge Now

```
Charge immediately. Optional "Save my info" checkbox shown automatically.
Supports: single-use and reusable payment methods.
```

### SetupIntent — Save Without Charging

```
Save PM for future use, no charge now.
Supports: reusable PMs only (not BNPLs, one-time methods).
Use cases: onboarding, free trials, crowdfunding (charge if goal met).
```

### PaymentIntent + `setup_future_usage` — Charge + Save

```
Charge now AND save for future.
Two approaches:
- Top-level setup_future_usage: requires all PMs to be reusable (disables BNPLs)
- Per-PM: payment_method_options[card][setup_future_usage] — mix one-time + reusable
```

## Saved Payment Methods

Supported: **card**, **US Bank Account**, **SEPA Debit**

CustomerSessions API controls:
- Show/hide save consent checkbox
- Show/hide saved PMs list
- Allow/prevent PM removal
- Prevent removal of last saved PM

Consent collection handled automatically for global compliance.

## Features

- 100+ payment methods including Apple Pay, Google Pay, Link, Amazon Pay
- Custom payment methods supported
- Fraud protection included
- SDK: iOS, Android, React Native
- Wallet PMs require domain registration

![Payment Sheet overview](../raw/assets/stripe-inapp-payment-sheet-overview.png)
![Saved payment methods](../raw/assets/stripe-inapp-saved-payment-methods.png)

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[stripe-saved-payment-methods]] — saved PM patterns

## Raw Sources

- [[stripe-inapp-payments-overview-2025]] — verbatim in-app payments overview
