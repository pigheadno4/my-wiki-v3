---
title: "Payment Element — Mobile"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-payment-element-2025.md"
tags: [stripe, mobile, ios, android, react-native, payment-element, embeddable, layout, appearance-api, wallets, saved-payment-methods]
---

## Summary

Overview of the mobile Payment Element — an embeddable alternative to Payment Sheet. Embeds payment method list directly in any app screen; a sheet below collects details when a method is selected. More flexible layout than Payment Sheet.

## Key Distinction vs Payment Sheet

| | Payment Sheet | Payment Element |
| --- | --- | --- |
| UI placement | Full-screen sheet | Embeds anywhere in app |
| Layout | Fixed | Radio / Checkmark / Floating buttons |
| When details collected | In the sheet | In a sheet below the list |

## Three Layout Options

- **Radio buttons** — standard radio list
- **Checkmarks** — checkmark selection style
- **Floating buttons** — button-style presentation

![Layout options](../raw/assets/stripe-inapp-pe-layout.png)

## Features

- 100+ payment methods; Apple Pay and Link shown inline as options
- Appearance API: colors, fonts, borders, shadows
- Saved PMs: cards, US bank accounts, SEPA debit; CustomerSessions API controls visibility/removal
- Address collection: name, email, phone, billing address
- CVC recollection for saved cards
- Card brand filtering

![Payment Element example](../raw/assets/stripe-inapp-payment-element-example.png)
![Appearance](../raw/assets/stripe-inapp-pe-appearance.png)
![Payment methods](../raw/assets/stripe-inapp-pe-payment-methods.png)
![Wallets](../raw/assets/stripe-inapp-pe-wallets.png)
![Saved PMs](../raw/assets/stripe-inapp-pe-saved-payment-methods.png)
![Address collection](../raw/assets/stripe-inapp-pe-address-collection.png)

## Related Pages

- [[stripe-inapp-payments]] — concept page (includes Payment Sheet, Flow Controller, Payment Element comparison)
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet detail

## Raw Sources

- [[stripe-inapp-payment-element-2025]] — verbatim Payment Element overview (92 lines, 8 images)
