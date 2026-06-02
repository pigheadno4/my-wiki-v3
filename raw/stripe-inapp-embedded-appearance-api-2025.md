<!-- Source URL: https://docs.stripe.com/elements/appearance-api/embedded-mobile -->
<!-- Fetched: 2026-04-22 -->

# Customize appearance

Customize your in-app integration with the Appearance API.

# iOS

> This is a iOS for when platform is ios. View the full page at https://docs.stripe.com/elements/appearance-api/embedded-mobile?platform=ios.

The Payment Element supports visual customization, which allows you to match the design of your app. The layout stays consistent but you can modify colors, fonts, and more by using the [appearance](https://github.com/stripe/stripe-ios/blob/c7c0cfa57411d39b8f26b205b35a0793e0998fe8/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElementConfiguration.swift#L83) property on your [EmbeddedPaymentElement.Configuration](https://github.com/stripe/stripe-ios/blob/c7c0cfa57411d39b8f26b205b35a0793e0998fe8/StripePaymentSheet/StripePaymentSheet/Source/PaymentSheet/Embedded/EmbeddedPaymentElementConfiguration.swift#L12) object.

1. Customize the [font](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#fonts-ios)
1. Customize [colors](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#colors-ios) to match your app
1. Customize [shapes](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#shapes-ios) like corner radius
1. Fine-tune [specific components](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#specific-ui-components-ios)
1. Customize look and feel of Payment Element
   ![](assets/stripe-inapp-ios-embedded-appearance-example.png)

```swift
var configuration = EmbeddedPaymentElement.Configuration()
// The following code creates the appearance shown in the screenshot abovevar appearance = PaymentSheet.Appearance()
appearance.font.base = UIFont(name: "AvenirNext-Regular", size: UIFont.systemFontSize)!
appearance.cornerRadius = 8
appearance.shadow = .disabled
appearance.borderWidth = 0
appearance.selectedBorderWidth = 2
appearance.colors.background = UIColor(red: 23/255, green: 47/255, blue: 86/255, alpha: 1)
appearance.colors.primary = UIColor(red: 199/255, green: 217/255, blue: 255/255, alpha: 1)
appearance.colors.text = .white
appearance.colors.textSecondary = UIColor(red: 255/255, green: 255/255, blue: 255/255, alpha: .7)
appearance.colors.componentText = .white
appearance.colors.componentPlaceholderText = UIColor(red: 255/255, green: 255/255, blue: 255/255, alpha: .5)
appearance.colors.componentBorder = .clear
appearance.colors.componentDivider = UIColor(red: 255/255, green: 255/255, blue: 255/255, alpha: .1)
appearance.colors.componentBackground = UIColor(red: 44/255, green: 73/255, blue: 119/255, alpha: 1)
appearance.colors.icon = .white
configuration.appearance = appearance
let embeddedPaymentElement = try await EmbeddedPaymentElement.create(/* ... */, configuration: configuration)
```

## Fonts

Customize the font by setting [font.base](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance/Font.html#/s:6Stripe12PaymentSheetC10AppearanceV4FontV4baseSo6UIFontCvp) to any variant of your custom font at any size and weight. The mobile Payment Element uses the font family of your custom font, but determines sizes and weights itself.

To increase or decrease the size of all text, set [font.sizeScaleFactor](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance/Font.html#/s:6Stripe12PaymentSheetC10AppearanceV4FontV15sizeScaleFactor12CoreGraphics7CGFloatVvp). We multiply font sizes by this value before displaying them. This is useful if your custom font is slightly larger or smaller than the system font.

```swift
var configuration = EmbeddedPaymentElement.Configuration()
configuration.appearance.font.base = UIFont(name: "CustomFont-Regular", size: UIFont.systemFontSize)
configuration.appearance.font.sizeScaleFactor = 1.15 // Increase the size of all text by 1.15x
```

## Colors

Customize the colors in the mobile Payment Element by modifying the color categories defined in [Appearance.Colors](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance.html#/s:6Stripe12PaymentSheetC10AppearanceV6ColorsV). Each color category determines the color of one or more components in the UI. For example, [primary](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance/Colors.html#/s:6Stripe12PaymentSheetC10AppearanceV6ColorsV7primarySo7UIColorCvp) defines the color of the **Pay** button and selected items like the **Save this card** checkbox. Refer to the diagram below to see some of the UI elements associated with each color category.
![](assets/stripe-inapp-ios-embedded-colors.png)

> To support dark mode, initialize your custom UIColors with [init(dynamicProvider:)](https://developer.apple.com/documentation/uikit/uicolor/3238041-init).

## Shapes

Besides fonts and colors, you can also customize the [corner radius](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance.html#/s:6Stripe12PaymentSheetC10AppearanceV12cornerRadius12CoreGraphics7CGFloatVvp), [border width](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance.html#/s:6Stripe12PaymentSheetC10AppearanceV11borderWidth12CoreGraphics7CGFloatVvp), and [shadow](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance.html#/s:6Stripe12PaymentSheetC10AppearanceV6shadowAE6ShadowVvp) used throughout the mobile Payment Element.
![](assets/stripe-inapp-ios-embedded-shapes.png)

## Specific UI components

The sections above describe customization options that affect the mobile Payment Element broadly, across multiple UI components. We also provide customization options specifically for the primary button (for example, the **Pay** button). Refer to [Appearance.PrimaryButton](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Appearance/PrimaryButton.html) for the full list of customization options.

Customization options for specific UI components take precedence over other values. For example, `appearance.primaryButton.cornerRadius` overrides the value of `appearance.cornerRadius`.

> [Let us know](https://github.com/stripe/stripe-ios/issues/new/choose) if you think we need to add more customization options.

## Payment Element

The Payment Element has the following styles: flat with radio buttons, flat with checkmarks, flat with disclosure icons, and floating buttons. Each style has specific options corresponding to that style.

### Flat with radio

![Embedded payment element styled using flat with radio](assets/stripe-inapp-ios-embedded-flat-radio.png)

```swift
var configuration = EmbeddedPaymentElement.Configuration()

var appearance = PaymentSheet.Appearance.default
appearance.embeddedPaymentElement.row.style = .flatWithRadio
appearance.embeddedPaymentElement.row.flat.bottomSeparatorEnabled = false // Hide the bottom separator
appearance.embeddedPaymentElement.row.flat.topSeparatorEnabled = false // Hide the top separator
appearance.embeddedPaymentElement.row.flat.separatorColor = .gray // Change the separator color to gray
appearance.embeddedPaymentElement.row.flat.separatorInsets = .zero // Make separators full width
appearance.embeddedPaymentElement.row.flat.separatorThickness = 2.0 // Increase separator thickness to 2
appearance.embeddedPaymentElement.row.flat.radio.selectedColor = .blue // Change color of radio button when selected to blue
appearance.embeddedPaymentElement.row.flat.radio.unselectedColor = .darkGray // Change color of radio button when unselected to darkGray

configuration.appearance = appearance
```

### Flat with checkmark

![Embedded payment element styled using flat with checkmark](assets/stripe-inapp-ios-embedded-flat-checkmark.png)

```swift
var configuration = EmbeddedPaymentElement.Configuration()

var appearance = PaymentSheet.Appearance.default
appearance.embeddedPaymentElement.row.style = .flatWithCheckmark
appearance.embeddedPaymentElement.row.flat.bottomSeparatorEnabled = false // Hide the bottom separator
appearance.embeddedPaymentElement.row.flat.topSeparatorEnabled = false // Hide the top separator
appearance.embeddedPaymentElement.row.flat.separatorColor = .gray // Change the separator color to gray
appearance.embeddedPaymentElement.row.flat.separatorInsets = .zero // Make separators full width
appearance.embeddedPaymentElement.row.flat.separatorThickness = 2.0 // Increase separator thickness to 2
appearance.embeddedPaymentElement.row.flat.checkmark.color = .blue // Change color of the checkmark


configuration.appearance = appearance
```

### Flat with disclosure

The FlatWithDisclosure style requires you to set the `immediateAction` row selection behavior. After the customer selects a payment method, move them to a new screen (for example, back to your main checkout screen) because the row of their selected payment method won’t appear selected.
![Embedded payment element styled using flat with disclosure](assets/stripe-inapp-ios-embedded-flat-disclosure.png)

```swift
var configuration = EmbeddedPaymentElement.Configuration()
// The flatWithDisclosure style requires the .immediateAction row selection behavior, which accepts a handler for a user selecting a payment method.
configuration.rowSelectionBehavior = .immediateAction(didSelectPaymentOption: myHandlingFunction)

var appearance = PaymentSheet.Appearance.default
appearance.embeddedPaymentElement.row.style = .flatWithDisclosure
appearance.embeddedPaymentElement.row.flat.bottomSeparatorEnabled = false // Hide the bottom separator
appearance.embeddedPaymentElement.row.flat.topSeparatorEnabled = false // Hide the top separator
appearance.embeddedPaymentElement.row.flat.separatorColor = .gray // Change the separator color to gray
appearance.embeddedPaymentElement.row.flat.separatorInsets = .zero // Make separators full width
appearance.embeddedPaymentElement.row.flat.separatorThickness = 2.0 // Increase separator thickness to 2
appearance.embeddedPaymentElement.row.flat.disclosure.color = .black // Change color of the disclosure icon

configuration.appearance = appearance
```

### Floating button

![Embedded payment element styled using floating button](assets/stripe-inapp-ios-embedded-floating.png)

```swift
var configuration = EmbeddedPaymentElement.Configuration()

var appearance = PaymentSheet.Appearance.default
appearance.embeddedPaymentElement.row.style = .floatingButton
appearance.embeddedPaymentElement.row.floating.spacing = 20 // Increase spacing
appearance.embeddedPaymentElement.row.additionalInsets = 10 // Increase row height

configuration.appearance = appearance
```

### Common row customizations

You can customize row properties that apply across all row styles:

```swift
var configuration = EmbeddedPaymentElement.Configuration()

var appearance = PaymentSheet.Appearance.default
appearance.embeddedPaymentElement.row.additionalInsets += 1 // Increase row height by 1 point
appearance.embeddedPaymentElement.row.paymentMethodIconLayoutMargins = .init(top: 0, leading: 10, bottom: 0, trailing: 10) // Custom margins for the payment method icon (for example, the Klarna logo)
appearance.embeddedPaymentElement.row.titleFont = UIFont.systemFont(ofSize: 16, weight: .medium) // Custom font for the row title (for example, "Klarna")
appearance.embeddedPaymentElement.row.subtitleFont = UIFont.systemFont(ofSize: 14, weight: .medium) // Custom font for the row subtitle (for example, "Buy now or pay later with Klarna")
```

# Android

> This is a Android for when platform is android. View the full page at https://docs.stripe.com/elements/appearance-api/embedded-mobile?platform=android.

The Payment Element supports visual customization, which allows you to match the design of your app. The layout stays consistent, but you can modify colors, fonts, and more by creating your `EmbeddedPaymentElement.Configuration` object with an [appearance](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-configuration/index.html#-431946322%2FProperties%2F2002900378) object.

1. Customize the [font](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#fonts-android)
1. Customize [colors](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#colors-android) to match your app
1. Customize [shapes](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#shapes-android) like corner radius
1. Fine-tune [specific components](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#specific-ui-components-android)
   ![](assets/stripe-inapp-android-embedded-appearance-example.png)

```kotlin
// The following code creates the appearance shown in the screenshot aboveimport androidx.compose.ui.graphics.Color

val appearance = PaymentSheet.Appearance(
   colorsLight = PaymentSheet.Colors(
       primary = Color(red = 36, green = 36, blue = 47),
       surface = Color.White,
       component = Color(red = 243, green = 248, blue = 245),
       componentBorder = Color.Transparent,
       componentDivider = Color.Black,
       onComponent = Color.Black,
       subtitle = Color.Black,
       placeholderText = Color(red = 115, green = 117, blue = 123),
       onSurface = Color.Black,
       appBarIcon = Color.Black,
       error = Color.Red,
   ),
   shapes = PaymentSheet.Shapes(
       cornerRadiusDp = 12.0f,
       borderStrokeWidthDp = 0.5f
   ),
   typography = PaymentSheet.Typography.default.copy(
       fontResId = R.font.avenir_next
   ),
   primaryButton = PaymentSheet.PrimaryButton(
   shape = PaymentSheet.PrimaryButtonShape(
            cornerRadiusDp = 20f
        ),
    ),
    embeddedAppearance = PaymentSheet.Appearance.Embedded(
        style = PaymentSheet.Appearance.Embedded.RowStyle.FloatingButton(
            spacingDp = 20f,
            additionalInsetsDp = 10f
        )
    )
)

// ...

embeddedPaymentElement.configure(
    intentConfiguration = intentConfiguration,
    configuration = EmbeddedPaymentElement.Configuration.Builder(merchantName).appearance(appearance)
        .build()
)

```

## Fonts

Customize the font by setting [typography.fontResId](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-typography/index.html#-786783041%2FProperties%2F2002900378) to your custom font’s resource ID. The mobile Payment Element uses the font family of your custom font, but determines sizes and weights itself.

To increase or decrease the size of text, set [typography.sizeScaleFactor](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-typography/index.html#1477076499%2FProperties%2F2002900378). Stripe multiplies font sizes by this value before displaying them. This setting is useful if your custom font is slightly larger or smaller than the system font.

```kotlin
val appearance = PaymentSheet.Appearance(
    // …typography = PaymentSheet.Typography.default.copy(
        sizeScaleFactor = 1.15f, // Increase the size of all text by 1.15x
        fontResId = R.font.myFont,
    ),
)
val configuration = EmbeddedPaymentElement.Configuration(merchantName).Builder()
    .appearance(appearance)
    .build()
```

## Colors

Customize the colors in the mobile Payment Element by modifying the color categories defined in [PaymentSheet.Colors](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-colors/index.html). Each color category determines the color of one or more components in the UI. For example, [primary](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-colors/index.html#1242160296%2FProperties%2F2002900378) defines the color of the **Pay** button and selected items like the **Save this card** checkbox. Refer to the diagram below to see some of the UI elements associated with each color category.

> To support dark mode, set [appearance.colorsDark](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-appearance/index.html#945237406%2FProperties%2F2002900378). You can effectively disable dark mode by setting [appearance.colorsDark](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-appearance/index.html#945237406%2FProperties%2F2002900378) to the same value as [appearance.colorsLight](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-appearance/index.html#2092498352%2FProperties%2F2002900378)
> ![](assets/stripe-inapp-android-embedded-colors.png)

## Shapes

In addition to customizing fonts and colors, you can also customize the [corner radius](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-shapes/index.html#-1129752289%2FProperties%2F2002900378) and [border width](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-shapes/index.html#495484314%2FProperties%2F2002900378) used throughout the mobile Payment Element by setting [appearance.shapes](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-appearance/index.html#-2108514638%2FProperties%2F2002900378).
![](assets/stripe-inapp-android-embedded-shapes.png)

## Specific UI components

The sections above describe customization options that affect the mobile Payment Element broadly, across multiple UI components. We also provide customization options specifically for the primary button (for example, the **Pay** button). Refer to [Appearance.PrimaryButton](https://stripe.dev/stripe-android/paymentsheet/com.stripe.android.paymentsheet/-payment-sheet/-primary-button/index.html) for the full list of customization options.

Customization options for specific UI components take precedence over other values. For example, `appearance.primaryButton.shapes.cornerRadius` overrides the value of `appearance.shapes.cornerRadius`.

> If you have ideas for additional customization options, [let us know](https://github.com/stripe/stripe-android/issues/new/choose).

## Payment Element

The Payment Element has the following styles: flat with radio buttons, flat with checkmarks, flat with disclosure, and floating buttons. Each style has its own options.

### Flat with radio buttons

To use the flat with radio buttons style, set the `FlatWithRadio` properties as shown in the code example.
![Embedded payment element styled using flat with radio buttons](assets/stripe-inapp-android-embedded-flat-radio.png)

```kotlin
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb

val embeddedColors = PaymentSheet.Appearance.Embedded.RowStyle.FlatWithRadio.Colors(
    selectedColor = Color.Yellow.toArgb(), // Change color of radio button when selected to yellow
    unselectedColor = Color.DarkGray.toArgb(), // Change color of radio button when unselected to darkGray
    separatorColor = Color.Gray.toArgb(), // Change the separator color to gray
)
val embeddedAppearance = PaymentSheet.Appearance.Embedded.Builder()
    .rowStyle(
      PaymentSheet.Appearance.Embedded.RowStyle.FlatWithRadio.Builder()
        .separatorThicknessDp(2f) // Increase separator thickness to 2
        .startSeparatorInsetDp(0f) // Make start separator full width
        .endSeparatorInsetDp(0f) // Make end separator full width
        .topSeparatorEnabled(false) // Hide the top separator
        .bottomSeparatorEnabled(false) // Hide the bottom separator
        .additionalVerticalInsetsDp(10f) // Increase row height
        .horizontalInsetsDp(10f)
        .colorsLight(embeddedColors)
        .colorsDark(embeddedColors)
        .build()
    )
    .build()

val appearance = PaymentSheet.Appearance(
    embeddedAppearance = embeddedAppearance,
)

val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")
    .appearance(appearance)
    .build()
```

### Flat with checkmarks

To use the flat with checkmarks style, set the `FlatWithCheckmark` properties, as shown in the code example.
![Embedded payment element styled using flat with checkmarks](assets/stripe-inapp-android-embedded-flat-checkmark.png)

```kotlin
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb

val embeddedColors = PaymentSheet.Appearance.Embedded.RowStyle.FlatWithCheckmark.Colors(
    checkmarkColor = Color.Blue.toArgb(), // Change color of the checkmark
    separatorColor = Color.Gray.toArgb(), // Change the separator color to gray
)
val embeddedAppearance = PaymentSheet.Appearance.Embedded.Builder()
    .rowStyle(
      PaymentSheet.Appearance.Embedded.RowStyle.FlatWithCheckmark.Builder()
        .separatorThicknessDp(2f) // Increase separator thickness to 2
        .startSeparatorInsetDp(0f) // Make start separator full width
        .endSeparatorInsetDp(0f) // Make end separator full width
        .topSeparatorEnabled(false) // Hide the top separator
        .bottomSeparatorEnabled(false) // Hide the bottom separator
        .checkmarkInsetDp(2f) // Inset the checkmark
        .additionalVerticalInsetsDp(10f) // Increase row height
        .horizontalInsetsDp(10f)
        .colorsLight(embeddedColors)
        .colorsDark(embeddedColors)
        .build()
    )
    .build()

val appearance = PaymentSheet.Appearance(
    embeddedAppearance = embeddedAppearance,
)

val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")
    .appearance(appearance)
    .build()
```

### Flat with disclosure

To use the flat with disclosure style, set the `FlatWithDisclosure` properties, as shown in the code example below.

The FlatWithDisclosure style requires you to set the `immediateAction` row selection behavior. After the customer selects a payment method, move them to a new screen (for example, back to your main checkout screen) because the row of their selected payment method won’t appear selected.
![Embedded payment element styled using flat with disclosure](assets/stripe-inapp-android-embedded-flat-disclosure.png)

```kotlin
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb

// EmbeddedPaymentElement initialization

val embeddedBuilder = EmbeddedPaymentElement.Builder(
  ...,
)
  // The FlatWithDisclosure style requires the immediateAction row selection behavior, which accepts a handler for a user selecting a payment method.
  .rowSelectionBehavior(EmbeddedPaymentElement.RowSelectionBehavior.immediateAction { embeddedPaymentElement ->
    // Handle the customer tapping a payment method row here
  })

...

// Configuration

val embeddedColors = PaymentSheet.Appearance.Embedded.RowStyle.FlatWithDisclosure.Colors(
    disclosureColor = Color.Blue.toArgb(), // Change color of the disclosure
    separatorColor = Color.Gray.toArgb(), // Change the separator color to gray
)
val embeddedAppearance = PaymentSheet.Appearance.Embedded.Builder()
    .rowStyle(
      PaymentSheet.Appearance.Embedded.RowStyle.FlatWithDisclosure.Builder()
        .separatorThicknessDp(2f) // Increase separator thickness to 2
        .startSeparatorInsetDp(0f) // Make start separator full width
        .endSeparatorInsetDp(0f) // Make end separator full width
        .topSeparatorEnabled(false) // Hide the top separator
        .bottomSeparatorEnabled(false) // Hide the bottom separator
        .additionalVerticalInsetsDp(10f) // Increase row height
        .horizontalInsetsDp(10f)
        .colorsLight(embeddedColors)
        .colorsDark(embeddedColors)
        .build()
    )
    .build()


val appearance = PaymentSheet.Appearance(
    embeddedAppearance = embeddedAppearance,
)

val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")
  .appearance(appearance)
  .build()
```

### Floating buttons

To use the floating buttons style, set the `FloatingButton` properties, as shown in the code example.
![Embedded payment element styled using floating button](assets/stripe-inapp-android-embedded-floating.png)

```kotlin
val embeddedAppearance = PaymentSheet.Appearance.Embedded.Builder()
    .rowStyle(
      PaymentSheet.Appearance.Embedded.RowStyle.FloatingButton.Builder()
        .additionalInsetsDp(10f) // Increase row height
        .spacingDp(20f) // Increase spacing
    )
    .build()


val appearance = PaymentSheet.Appearance(
    embeddedAppearance = embeddedAppearance,
)

val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")
    .appearance(appearance)
    .build()
```

### Common row customizations

You can customize row properties that apply across all row styles:

```kotlin
@OptIn(AppearanceAPIAdditionsPreview::class)
val embeddedAppearance = PaymentSheet.Appearance.Embedded.Builder()
    // Custom margins for the payment method icon (for example, the Klarna logo)
    .paymentMethodIconMargins(
      PaymentSheet.Insets(
        horizontalDp = 10f,
        verticalDp = 5f
      )
    )
    // Custom font for the row title (for example, "Klarna")
    .titleFont(
      PaymentSheet.Typography.Font(
        fontFamily = R.font.custom_font,
        fontSizeSp = 20f,
        fontWeight = 50,
        letterSpacingSp = 8f
      )
    )
    // Custom font for the row subtitle (for example, "Buy now or pay later with Klarna")
    .titleFont(
      PaymentSheet.Typography.Font(
        fontFamily = R.font.custom_font,
        fontSizeSp = 14f,
        fontWeight = 50,
        letterSpacingSp = 8f
      )
    )
    .build()

val appearance = PaymentSheet.Appearance(
    embeddedAppearance = embeddedAppearance,
)

val configuration = EmbeddedPaymentElement.Configuration.Builder("Powdur")
    .appearance(appearance)
    .build()
```

# React Native

> This is a React Native for when platform is react-native. View the full page at https://docs.stripe.com/elements/appearance-api/embedded-mobile?platform=react-native.

The Payment Element supports visual customization, which allows you to match the design of your app. The layout stays consistent but you can modify colors, fonts, and more by using the [appearance](https://github.com/stripe/stripe-react-native/blob/fcb661364030a44639a58fc378ed514093226c5c/src/types/EmbeddedPaymentElement.tsx#L132) property on your [EmbeddedPaymentElementConfiguration](https://github.com/stripe/stripe-react-native/blob/fcb661364030a44639a58fc378ed514093226c5c/src/types/EmbeddedPaymentElement.tsx#L98) object.

1. Customize the [font](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#fonts-react-native)
1. Customize [colors](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#colors-react-native) to match your app
1. Customize [shapes](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#shapes-react-native) like corner radius
1. Fine-tune [specific components](https://docs.stripe.com/elements/appearance-api/embedded-mobile.md#specific-ui-components-react-native)
1. Customize look and feel of Payment Element
   ![](assets/stripe-inapp-ios-embedded-appearance-example.png)

```js
// The following code creates the appearance shown in the screenshot aboveimport { Platform } from 'react-native';
import type { AppearanceParams, EmbeddedPaymentElementConfiguration } from '@stripe/stripe-react-native';

const appearance: AppearanceParams = {
  font: {
    family: Platform.OS === 'android' ? 'avenirnextregular' : 'AvenirNext-Regular',
    scale: 1,
  },
  shapes: {
    borderRadius: 8,
    borderWidth: 0,
    shadow: {
      color: '#000000',
      opacity: 0,
      offset: { x: 0, y: 0 },
      blurRadius: 0,
    },
  },
  colors: {
    primary: '#C7D9FF',
    background: '#172F56',
    componentBackground: '#2C4977',
    componentBorder: '#00000000',
    componentDivider: '#1AFFFFFF',
    primaryText: '#FFFFFF',
    secondaryText: '#B3FFFFFF',
    componentText: '#FFFFFF',
    placeholderText: '#80FFFFFF',
    icon: '#FFFFFF',
  },
};

// Set the appearance property on your configuration
const config: EmbeddedPaymentElementConfiguration = {
  appearance: appearance,
};
```

## Fonts

Customize the font by passing a [FontConfig](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#FontConfig) to `font` and setting `family`. On iOS, the value of `family` should be the “PostScript name” found in Font Book. On Android, copy the `.ttf` or `.otf` file from `android/app/src/main/assets/font/<your-font>` to `android/app/src/main/res/font/<your-font>` and use the name of the font file (containing only lowercase, alphanumeric characters). The Mobile Payment Element uses the font family of your custom font, but determines sizes and weights itself.

To increase or decrease the size of text, set `scale`. We multiply font sizes by this value before displaying them. This is useful if your custom font is slightly larger or smaller than the system font.

```js
 ...const appearance: AppearanceParams = {
   font: {
     family: Platform.OS === 'android' ? 'avenirnextregular' : 'AvenirNext-Regular',
     scale: 1.15,
   },
 },
```

## Colors

Customize the colors in the Mobile Payment Element by modifying the color categories defined in [GlobalColorConfig](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#GlobalColorConfig). Each color category determines the color of one or more components in the UI. For example, `primary` defines the color of the **Pay** button and selected items like the **Save this card** checkbox. Refer to the diagram below to see some of the UI elements associated with each color category.

> To support dark mode, pass maps for both `light` and `dark` colors to [colors](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#AppearanceParams).
> ![](assets/stripe-inapp-rn-embedded-colors.png)

## Shapes

Besides fonts and colors, you can also customize the [border radius](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#AppearanceParams), [border width](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#AppearanceParams), and [shadow](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#ShadowConfig) used throughout the mobile Payment Element.
![](assets/stripe-inapp-rn-embedded-shapes.png)

## Specific UI components

The previous sections describe customization options that affect the mobile Payment Element broadly, across multiple UI components. We also provide customization options specifically for the primary button (for example, the **Pay** button). Refer to the [PrimaryButtonConfig](https://stripe.dev/stripe-react-native/api-reference/modules/PaymentSheet.html#PrimaryButtonConfig) for the full list of customization options.

Customization options for specific UI components take precedence over other values. For example, `primaryButton.shapes.borderRadius` overrides the value of `shapes.borderRadius`.

> [Let us know](https://github.com/stripe/stripe-react-native/issues/new/choose) if you think we need to add more customization options.

## Payment Element

The Payment Element has the following styles: flat with radio buttons, flat with checkmarks, flat with disclosure icons, and floating buttons. Each style has specific options corresponding to that style.

### Flat with radio

![Embedded payment element styled using flat with radio](assets/stripe-inapp-ios-embedded-flat-radio.png)

```js
import { RowStyle } from '@stripe/stripe-react-native';

const appearance: AppearanceParams = {
  embeddedPaymentElement: {
    row: {
      style: RowStyle.FlatWithRadio,
      additionalInsets: 10, // Increase row height
      flat: {
        bottomSeparatorEnabled: false, // Hide the bottom separator
        topSeparatorEnabled: false, // Hide the top separator
        separatorColor: 'gray', // Change the separator color to gray
        separatorInsets: { top: 0, left: 0, bottom: 0, right: 0 }, // Make separators full width
        separatorThickness: 2.0, // Increase separator thickness to 2
        radio: {
          selectedColor: 'blue', // Change color of radio button when selected to blue
          unselectedColor: 'darkgray', // Change color of radio button when unselected to darkGray
        },
      },
    },
  },
};
```

### Flat with checkmark

![Embedded payment element styled using flat with checkmark](assets/stripe-inapp-ios-embedded-flat-checkmark.png)

```js
import { RowStyle } from '@stripe/stripe-react-native';

const appearance: AppearanceParams = {
  embeddedPaymentElement: {
    row: {
      style: RowStyle.FlatWithCheckmark,
      additionalInsets: 10, // Increase row height
      flat: {
        bottomSeparatorEnabled: false, // Hide the bottom separator
        topSeparatorEnabled: false, // Hide the top separator
        separatorColor: 'gray', // Change the separator color to gray
        separatorInsets: { top: 0, left: 0, bottom: 0, right: 0 }, // Make separators full width
        separatorThickness: 2.0, // Increase separator thickness to 2
        checkmark: {
          color: 'blue', // Change color of the checkmark
        },
      },
    },
  },
};
```

### Flat with disclosure icons

![Embedded payment element styled using flat with disclosure icons](assets/stripe-inapp-ios-embedded-flat-disclosure.png)

```js
import { RowStyle } from '@stripe/stripe-react-native';

const appearance: AppearanceParams = {
  embeddedPaymentElement: {
    row: {
      style: RowStyle.FlatWithDisclosure,
      additionalInsets: 10, // Increase row height
      flat: {
        bottomSeparatorEnabled: false, // Hide the bottom separator
        topSeparatorEnabled: false, // Hide the top separator
        separatorColor: 'gray', // Change the separator color to gray
        separatorInsets: { top: 0, left: 0, bottom: 0, right: 0 }, // Make separators full width
        separatorThickness: 2.0, // Increase separator thickness to 2
        disclosure: {
          color: 'black', // Change color of the disclosure
        },
      },
    },
  },
};
const newElementConfig: EmbeddedPaymentElementConfiguration = {
  appearance: appearance,
    // The FlatWithDisclosure style requires the immediateAction row selection behavior, which accepts a handler for a user selecting a payment method.
  rowSelectionBehavior: {
    type: 'immediateAction',
    onSelectPaymentOption: myHandlerFunction,
  },
};
```

### Floating button

![Embedded payment element styled using floating button](assets/stripe-inapp-ios-embedded-floating.png)

```js
import { RowStyle } from '@stripe/stripe-react-native';

const appearance: AppearanceParams = {
  embeddedPaymentElement: {
    row: {
      style: RowStyle.FloatingButton,
      additionalInsets: 10, // Increase row height
      floating: {
        spacing: 20, // Increase spacing
      },
    },
  },
};
```
