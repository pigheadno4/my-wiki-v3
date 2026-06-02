---
title: "Customize Appearance — Embedded Mobile Payment Element"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-embedded-appearance-api-2025.md"
tags: [stripe, mobile, ios, android, react-native, embedded-payment-element, appearance-api, row-style, flat-radio, flat-checkmark, flat-disclosure, floating-button]
---

## Summary

Appearance API specifically for `EmbeddedPaymentElement`. Extends the standard font/color/shape Appearance API with `embeddedPaymentElement.row` customization for the 4 row styles.

> See also [[source-stripe-inapp-appearance-api]] for the standard Payment Sheet Appearance API (same base: font, colors, shapes, primary button).

## New iOS Property: `selectedBorderWidth`

```swift
appearance.selectedBorderWidth = 2  // border width when a row is selected
```

## Row Styles — `appearance.embeddedPaymentElement.row.style`

| Style | iOS value | Notes |
| --- | --- | --- |
| Flat with radio | `.flatWithRadio` | Radio button indicator |
| Flat with checkmark | `.flatWithCheckmark` | Checkmark indicator |
| Flat with disclosure | `.flatWithDisclosure` | Disclosure chevron; **requires `rowSelectionBehavior = .immediateAction`** |
| Floating button | `.floatingButton` | Card-style floating buttons |

## Key: `flatWithDisclosure` Requires `immediateAction`

```swift
configuration.rowSelectionBehavior = .immediateAction(didSelectPaymentOption: myHandler)
appearance.embeddedPaymentElement.row.style = .flatWithDisclosure
```

After selection, move customer away (back to checkout) — the selected row won't show as selected.

## Per-Style Properties

### Flat styles (radio/checkmark/disclosure)

```swift
appearance.embeddedPaymentElement.row.flat.bottomSeparatorEnabled = false
appearance.embeddedPaymentElement.row.flat.topSeparatorEnabled = false
appearance.embeddedPaymentElement.row.flat.separatorColor = .gray
appearance.embeddedPaymentElement.row.flat.separatorInsets = .zero
appearance.embeddedPaymentElement.row.flat.separatorThickness = 2.0
// Radio:
appearance.embeddedPaymentElement.row.flat.radio.selectedColor = .blue
appearance.embeddedPaymentElement.row.flat.radio.unselectedColor = .darkGray
// Checkmark:
appearance.embeddedPaymentElement.row.flat.checkmark.color = .blue
// Disclosure:
appearance.embeddedPaymentElement.row.flat.disclosure.color = .black
```

### Floating button

```swift
appearance.embeddedPaymentElement.row.style = .floatingButton
appearance.embeddedPaymentElement.row.floating.spacing = 20
appearance.embeddedPaymentElement.row.additionalInsets = 10
```

## Common Row Properties (All Styles)

```swift
appearance.embeddedPaymentElement.row.additionalInsets += 1
appearance.embeddedPaymentElement.row.paymentMethodIconLayoutMargins = .init(...)
appearance.embeddedPaymentElement.row.titleFont = UIFont.systemFont(ofSize: 16, weight: .medium)
appearance.embeddedPaymentElement.row.subtitleFont = UIFont.systemFont(ofSize: 14, weight: .medium)
```

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-appearance-api]] — standard Payment Sheet Appearance API
- [[source-stripe-inapp-accept-payment-embedded]] — EmbeddedPaymentElement integration guide

## Raw Sources

- [[stripe-inapp-embedded-appearance-api-2025]] — verbatim embedded Appearance API (670 lines, 16 images)
