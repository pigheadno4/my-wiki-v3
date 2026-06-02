---
title: "Customize Appearance — Mobile Appearance API"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-appearance-api-2025.md"
tags: [stripe, mobile, ios, android, react-native, appearance-api, payment-sheet, fonts, colors, shapes]
---

## Summary

Mobile Appearance API reference for iOS, Android, and React Native. All three platforms share the same conceptual structure (fonts, colors, shapes, primary button) but use platform-specific APIs.

## Customization Areas (All Platforms)

1. **Fonts**: set font family; element controls sizes/weights; `sizeScaleFactor`/`scale` for global size adjustment
2. **Colors**: color categories map to UI components (e.g. `primary` = Pay button + checkboxes)
3. **Shapes**: corner radius, border width, shadow
4. **Primary button**: component-specific overrides; **takes precedence** over global settings

## iOS

```swift
var appearance = PaymentSheet.Appearance()
appearance.font.base = UIFont(name: "AvenirNext-Regular", size: UIFont.systemFontSize)!
appearance.font.sizeScaleFactor = 1.15
appearance.cornerRadius = 12
appearance.shadow = .disabled
appearance.borderWidth = 0.5
appearance.colors.primary = UIColor(red: 36/255, green: 36/255, blue: 47/255, alpha: 1)
appearance.primaryButton.cornerRadius = 20
configuration.appearance = appearance
```

Dark mode: use `UIColor(dynamicProvider:)`.

![iOS appearance example](../raw/assets/stripe-inapp-ios-appearance-example.png)
![iOS colors diagram](../raw/assets/stripe-inapp-ios-appearance-colors.png)
![iOS shapes diagram](../raw/assets/stripe-inapp-ios-appearance-shapes.png)

## Android

```kotlin
val appearance = PaymentSheet.Appearance(
    colorsLight = PaymentSheet.Colors(primary = Color(36, 36, 47), /* ... */),
    colorsDark = /* same as colorsLight to disable dark mode */,
    shapes = PaymentSheet.Shapes(cornerRadiusDp = 12.0f, borderStrokeWidthDp = 0.5f),
    typography = PaymentSheet.Typography.default.copy(fontResId = R.font.avenir_next, sizeScaleFactor = 1.15f),
    primaryButton = PaymentSheet.PrimaryButton(shape = PaymentSheet.PrimaryButtonShape(cornerRadiusDp = 20f)),
)
```

Dark mode: set `appearance.colorsDark`. Disable dark mode: set `colorsDark` = `colorsLight`.

![Android appearance example](../raw/assets/stripe-inapp-android-appearance-example.png)
![Android colors diagram](../raw/assets/stripe-inapp-android-appearance-colors.png)
![Android shapes diagram](../raw/assets/stripe-inapp-android-appearance-shapes.png)

## React Native

```js
const customAppearance = {
  font: {
    family: Platform.OS === 'android' ? 'avenirnextregular' : 'AvenirNext-Regular',
    scale: 1.15,
  },
  shapes: { borderRadius: 12, borderWidth: 0.5 },
  primaryButton: { shapes: { borderRadius: 20 } },
  colors: { primary: '#fcfdff', background: '#ffffff', /* ... */ },
};
await initPaymentSheet({ appearance: customAppearance });
```

**Font names**: iOS = PostScript name (Font Book); Android = filename in `res/font/` (lowercase alphanumeric).

![React Native shapes diagram](../raw/assets/stripe-inapp-rn-appearance-shapes.png)

## Related Pages

- [[stripe-inapp-payments]] — concept page
- [[source-stripe-inapp-payment-sheet]] — Payment Sheet detail (mentions Appearance API)

## Raw Sources

- [[stripe-inapp-appearance-api-2025]] — verbatim mobile Appearance API guide (242 lines, 7 images)
