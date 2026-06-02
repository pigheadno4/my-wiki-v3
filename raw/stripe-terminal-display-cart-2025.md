<!-- Source URL: https://docs.stripe.com/terminal/features/display -->
<!-- Fetched: 2026-05-01 -->

# Display cart details

Dynamically update cart details on the reader screen.

The built-in screen of the [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400.md), [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) can display line items. During the checkout process, you can update the reader’s screen to show individual items in the transaction, along with the total price.
![Cart details](assets/stripe-terminal-display-cart-details.png)

Cart details screen

## Set the reader display

- [setReaderDisplay (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)setReaderDisplay:completion:>)
- [setReaderDisplay (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)
- [setReaderDisplay (JavaScript)](https://docs.stripe.com/terminal/references/api/js-sdk.md#set-reader-display)
- [setReaderDisplay (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#setReaderDisplay)
- [setReaderDisplay (Java)](https://stripe.dev/stripe-terminal-java/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)

To display the line items and total on the reader, call `setReaderDisplay` before processing the payment and pass the information in the [cart](https://docs.stripe.com/api/terminal/readers/set_reader_display.md#set_reader_display-cart) parameter.

The amounts passed to the `setReaderDisplay` method are only used for display purposes. The reader won’t automatically calculate tax or the total—your application must calculate the tax and total before displaying the values. You can use the [Stripe Tax API](https://docs.stripe.com/tax/custom.md#calculate-tax) to calculate taxes. Similarly, the total passed to `setReaderDisplay` doesn’t control the amount charged to the customer. Make sure the amount displayed on the reader matches the amount you’re charging your customer.

# Server-driven

> This is a Server-driven for when terminal-sdk-platform is server-driven. View the full page at https://docs.stripe.com/terminal/features/display?terminal-sdk-platform=server-driven.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const reader = await stripe.terminal.readers.setReaderDisplay(
  'tmr_xxx',
  {
    type: 'cart',
    cart: {
      line_items: [
        {
          description: 'Caramel latte',
          amount: 659,
          quantity: 1,
        },
        {
          description: 'Dozen donuts',
          amount: 1239,
          quantity: 1,
        },
      ],
      currency: 'usd',
      tax: 100,
      total: 1998,
    },
  }
);
```

To clear reader display on the server-driven integration, call the [cancel_action](https://docs.stripe.com/api/terminal/readers/cancel_action.md) endpoint.

# JavaScript

> This is a JavaScript for when terminal-sdk-platform is js. View the full page at https://docs.stripe.com/terminal/features/display?terminal-sdk-platform=js.

```javascript
terminal.setReaderDisplay({
  type: 'cart',
  cart: {
    line_items: [
      {
        description: "Caramel latte",
        amount: 659,
        quantity: 1,
      },
      {
        description: "Dozen donuts",
        amount: 1239,
        quantity: 1,
      },
    ],
    tax: 100,
    total: 1998,
    currency: 'sgd',
  },
});
```

To reset the reader’s display from a line item interface to the splash screen, call the [clearReaderDisplay](https://docs.stripe.com/terminal/references/api/js-sdk.md#clear-reader-display) method.

# iOS

> This is a iOS for when terminal-sdk-platform is ios. View the full page at https://docs.stripe.com/terminal/features/display?terminal-sdk-platform=ios.

#### Swift

```swift
let lineItems = [
    try CartLineItemBuilder(displayName: "Caramel latte").setQuantity(1).setAmount(659).build(),
    try CartLineItemBuilder(displayName: "Dozen donuts").setQuantity(1).setAmount(1239).build(),
]

let cart = try CartBuilder(currency: "sgd")
    .setTax(100)
    .setTotal(1998)
    .setLineItems(lineItems)
    .build()

Terminal.shared.setReaderDisplay(cart) { (error) in
    // Check for errors
}
```

To reset the reader’s display from a line item interface to the splash screen, call the [clearReaderDisplay](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)clearReaderDisplay:>) method.

# Android

> This is a Android for when terminal-sdk-platform is android. View the full page at https://docs.stripe.com/terminal/features/display?terminal-sdk-platform=android.

#### Kotlin

```kotlin
val cart = Cart.Builder(currency = "usd", tax = 100, total = 1998)
cart.lineItems = listOf(
    CartLineItem.Builder(description = "Caramel latte", quantity = 1, amount = 659).build(),
    CartLineItem.Builder(description = "Dozen donuts", quantity = 1, amount = 1239).build(),
)

Terminal.getInstance().setReaderDisplay(
    cart.build(),
    object : Callback {
        override fun onSuccess() {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

To reset the reader’s display from a line item interface to the splash screen, call the [clearReaderDisplay](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html) method.

# React Native

> This is a React Native for when terminal-sdk-platform is react-native. View the full page at https://docs.stripe.com/terminal/features/display?terminal-sdk-platform=react-native.

```js
const { error } = await setReaderDisplay({
  currency: 'usd',
  tax: 100,
  total: 1998,
  lineItems: [
    {
      displayName: 'Caramel latte',
      quantity: 1,
      amount: 659,
    },
    {
      displayName: 'Dozen donuts',
      quantity: 1,
      amount: 1239,
    },
  ],
});
if (error) {
  // Placeholder for handling exception
}

// Placeholder for handling successful operation
```

## Pre-dip a card

> Pre-dipping a card is only supported for payments in the US.

The [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400.md), [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md), and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support the ability to present a card to the reader before the transaction amount is finalized.

This option is known as _pre-dip_, _pre-tap_, or _pre-swipe_, and can help speed up transaction times by allowing a customer to present a payment method before the end of the transaction.

The `setReaderDisplay` method prepares the reader for pre-dipping. Your customer can present a payment method at any point after this method is called. You can call `setReaderDisplay` multiple times to update the information displayed without impacting the pre-dipping process. Updating the display doesn’t invalidate a pre-dip, if one has already occurred.

Pre-dipping allows your customer to present a card early in the payment process without completing the associated transaction. Instead, the reader captures the presented payment method and saves it to use later, although Stripe doesn’t provide updates or events to indicate that the customer pre-dipped their card. You can process the transaction normally. For example, you can create and process a `PaymentIntent` to complete the transaction without special handling.

## Pre-dip disabled

If pre-dip isn’t available in your country, the screen shows only the subtotal and line items.
![Pre-dip disabled](assets/stripe-terminal-display-no-predip.png)

Pre-dip disabled
