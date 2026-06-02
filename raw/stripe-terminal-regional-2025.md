<!-- Source: Stripe Terminal — Regional considerations (all supported countries) -->
<!-- Fetched: 2026-04-24 -->

# Regional considerations

Learn about regional considerations for integrating Terminal in different countries.

​​For the most part, you’ll be able to use a single Terminal integration in all supported countries. However, due to local payment methods or regulations there are some country-specific requirements. After going through the [sample integration](https://docs.stripe.com/terminal/quickstart.md), use this guide to learn about country-specific requirements for Terminal.

> To process Terminal payments, both the Stripe account receiving the funds and the [location](https://docs.stripe.com/terminal/fleet/locations-and-zones.md) associated with the reader must be in the same country, accepting local currency only.

## Availability

Refer to the following table to understand which readers you can use in each country.

| Country | [Smart readers](https://docs.stripe.com/terminal/smart-readers.md) | [Mobile readers](https://docs.stripe.com/terminal/mobile-readers.md) | [Tap to Pay](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md) |
| ------- | ------------------------------------------------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| US      | - BBPOS WisePOS E                                                  |

- Stripe Reader S710
- Stripe Reader S700
- Verifone readers (Public preview) | - Stripe Reader M2 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | - AU
- BE
- NZ | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | CA | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700
- Verifone readers (Public preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | - IE
- GB | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, UX700, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | SG | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700
- Verifone V660p, P630 (Private preview) | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | - AT
- CZ
- DK
- FI
- FR
- IT
- LU
- NL
- NO
- PL
- PT
- ES
- SE
- CH | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | DE | - BBPOS WisePOS E
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | JP | - Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on iPhone |
  | MY | - BBPOS WisePOS E
- Stripe Reader S710
- Stripe Reader S700 | - BBPOS WisePad 3 | - Tap to Pay on Android
- Tap to Pay on iPhone (Public preview) |
  | - LI
- CY
- EE
- HR
- LT
- LV
- MT
- SI
- SK
- HU
- RO
- BG | | | - Tap to Pay on Android
- Tap to Pay on iPhone |
  | - GI | | | - Tap to Pay on Android |

## Regional considerations by country

Select a country to view its specific regional considerations

# United States (US)

> This is a United States (US) for when integration-country is US. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=US.

## Integrate Terminal in the United States

Stripe supports Visa, Mastercard, American Express, and Discover payments in the United States. All transactions must be made in US dollars (USD). To accept Terminal charges in the United States, either your platform account or connected account must be in the United States.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in US and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in US. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in US must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1272 Valencia Street",
    city: "San Francisco",
    state: "CA",
    country: "US",
    postal_code: "94110",
  },
});
```

# Canada (CA)

> This is a Canada (CA) for when integration-country is CA. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=CA.

## Integrate Terminal in Canada

Stripe supports Visa, Mastercard, American Express, Discover, and [Interac](https://docs.stripe.com/terminal/payments/regional.md?integration-country=CA#interac-payments) payments in Canada. All transactions must be made in Canadian dollars (CAD). To accept Terminal charges in Canada, either your platform account or connected account must be in Canada.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in CA and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in CA. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in CA must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "3040 Bur Oak Ave",
    city: "Markham",
    state: "ON",
    country: "CA",
    postal_code: "L6B 0R1",
  },
});
```

### Reader software version

Verifone P400 readers operating in Canada must use the reader software version `3.0.1.15` or later. Read about [Verifone P400 software updates](https://docs.stripe.com/terminal/readers/verifone-p400.md#stripe-reader-software) for details.

Similarly, BBPOS WisePad 3 readers must use the reader software version `4.01.03.00_Prod_NA_off_v30_480001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

[Language regulations](http://www.legisquebec.gouv.qc.ca/en/showdoc/cs/C-11#ga:l_i-gb:l_vii-h1) require that services, including point-of-sale services, be provided in French unless English has been agreed upon by the cardholder and their card issuer. Terminal is built to help you comply with these requirements if they apply to your business.

#### Default reader language

The [Verifone P400](https://docs.stripe.com/terminal/readers/verifone-p400.md) interface displays text in French in addition to English if it’s registered to a location with an address in CA.

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in CA, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Transaction language

After the cardholder has presented their card, the reader determines the cardholder’s preferred language. Each screen after that point is translated according to the cardholder’s preferences.

#### Other translations

If you’re required to provide services in or would like to translate text into French in addition to English, ensure that any of your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

## Interac payments

Interac is the interbank network that handles routing of debit payments in Canada. Consumer debit cards in Canada are branded with an Interac logo and might also be co-branded with another payment network’s logo. Even if the card is co-branded, however, all Interac debit transactions must be routed through Interac. To maximize card acceptance, you should build Interac support into your integration.

> Interac isn’t supported while [operating offline](https://docs.stripe.com/terminal/features/operate-offline/overview.md).

### Create a PaymentIntent

To accept Interac transactions you need to create your payments using the `interac_present` payment method type. Include the `card_present` payment method type as well if you accept Visa, Mastercard, and American Express payments.

> Learn more about the [in-person PaymentIntent flow](https://docs.stripe.com/terminal/payments/collect-card-payment.md).

**Client-side**

Create a `PaymentIntent` from your client using one of the following options:

#### Server-driven

> Client-side `PaymentIntent` creation is possible with the iOS, Android, and React Native SDKs. If you’re using the server-driven integration, create a `PaymentIntent` server-side.

#### JavaScript

> Client-side `PaymentIntent` creation is possible with the other client SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a `PaymentIntent` server-side.

#### iOS

- [createPaymentIntent (iOS)](<https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)createPaymentIntent:completion:>)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the iOS SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Swift

```swift
import UIKit
import StripeTerminal

class PaymentViewController: UIViewController {

    // ...

    // Action for a "Checkout" button
    func checkoutAction() throws {
        let params = PaymentIntentParametersBuilder(amount: 1000, currency: "cad")
                        .setPaymentMethodTypes([.cardPresent, .interacPresent])
                        .build()
        Terminal.shared.createPaymentIntent(params) { createResult, createError in
            if let error = createError {
                print("createPaymentIntent failed: \(error)")
            }
            else if let paymentIntent = createResult {
                print("createPaymentIntent succeeded")
                // ...
            }

        }
    }

    // ...
}
```

#### Android

- [createPaymentIntent (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/create-payment-intent.html)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the Android SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `Terminal.retrievePaymentIntent` method in the SDK.

#### Kotlin

```kotlin
val params = PaymentIntentParameters.Builder(
    listOf(
        PaymentMethodType.CARD_PRESENT,
        PaymentMethodType.INTERAC_PRESENT
    )
)
    .setAmount(1000)
    .setCurrency("cad")
    .build()
Terminal.getInstance().createPaymentIntent(
    params,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

#### React Native

- [createPaymentIntent (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#createPaymentIntent)

> If your app is connected to the Verifone P400, you can’t create a `PaymentIntent` from the React Native SDK.
>
> Instead, you must [create the PaymentIntent server-side](https://docs.stripe.com/terminal/payments/collect-card-payment.md#create-server-side), and retrieve the `PaymentIntent` in your app using the `retrievePaymentIntent` method in the SDK.

```js
const { error, paymentIntent } = await createPaymentIntent({
  amount: 1000,
  currency: "cad",
  paymentMethodTypes: ["cardPresent", "interacPresent"],
});
```

Alternatively, if you want to use manual capture for other payment methods while still accepting Interac payments (which require automatic capture), use `manual_preferred`:

#### Server-driven

> Client-side `PaymentIntent` creation is possible with the iOS, Android, and React Native SDKs. If you’re using the server-driven integration, create a `PaymentIntent` server-side.

#### JavaScript

> Client-side `PaymentIntent` creation is possible with the other client SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a `PaymentIntent` server-side.

#### iOS

#### Swift

```swift
let cardPresentParams = try CardPresentParametersBuilder()
    .setCaptureMethod(.manualPreferred)
    .build()
let paymentMethodOptionsParams = try PaymentMethodOptionsParametersBuilder()
    .setCardPresentParameters(cardPresentParams)
    .build()
let params = try PaymentIntentParametersBuilder(amount: 1000, currency: "cad")
    .setPaymentMethodTypes([.cardPresent, .interacPresent])
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
    .build()
Terminal.shared.createPaymentIntent(params) { createResult, createError in
    if let error = createError {
        print("createPaymentIntent failed: \(error)")
    }
    else if let paymentIntent = createResult {
        print("createPaymentIntent succeeded")
        // ...
    }
}
```

#### Android

#### Kotlin

```kotlin
val cardPresentParams = CardPresentParameters.Builder()
    .setCaptureMethod(CardPresentCaptureMethod.ManualPreferred)
    .build()
val paymentMethodOptionsParams = PaymentMethodOptionsParameters.Builder()
    .setCardPresentParameters(cardPresentParams)
    .build()
val params = PaymentIntentParameters.Builder(
    listOf(
        PaymentMethodType.CARD_PRESENT,
        PaymentMethodType.INTERAC_PRESENT
    )
)
    .setAmount(1000)
    .setCurrency("cad")
    .setPaymentMethodOptionsParameters(paymentMethodOptionsParams)
    .build()
Terminal.getInstance().createPaymentIntent(
    params,
    object : PaymentIntentCallback {
        override fun onSuccess(paymentIntent: PaymentIntent) {
            // Placeholder for handling successful operation
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

#### React Native

```js
const { error, paymentIntent } = await createPaymentIntent({
  amount: 1000,
  currency: "cad",
  paymentMethodTypes: ["cardPresent", "interacPresent"],
  paymentMethodOptions: {
    captureMethod: "manual_preferred",
  },
});
```

**Server-side**

- [Create a PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md)

The JavaScript SDK and the server-driven integration require you to create the `PaymentIntent` on your server. For the other client SDKs, you can create the `PaymentIntent` on your server if the information required to start a payment isn’t readily available in your app.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 999,
  currency: "cad",
  payment_method_types: ["card_present", "interac_present"],
  capture_method: "automatic",
});
```

Alternatively, if you want to use manual capture for other payment methods while still accepting Interac payments (which require automatic capture), use `manual_preferred`:

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=999 \
  -d currency=cad \
  -d "payment_method_types[]=card_present" \
  -d "payment_method_types[]=interac_present" \
  -d "payment_method_options[card_present][capture_method]=manual_preferred"
```

### Collect and process a payment

After you [process the payment](https://docs.stripe.com/terminal/payments/collect-card-payment.md), the reader determines whether to route the payment across Interac rails based on the profile of the card presented.

In cases where the Interac card is co-branded, the `payment_method_details.interac_present.brand` field on a PaymentIntent’s returned [charge](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-interac_present-brand) reports the co-brand. The type field on the `payment_method` for an Interac transaction is always `interac_present`.

There are further Interac requirements that Stripe handles automatically for you, without additional integration work on your side:

- Before a card is presented, on-screen prompts are in the default reader language. After the card information has been collected, the localization is based on the language preference specified by the presented card.
- The reader automatically prompts for PIN in cases where it’s required.
- Interac Flash (contactless) payments are limited to 250 CAD and generally up to three consecutive transactions. Transactions higher than 100 CAD or the fourth contactless transaction in a row require the customer to insert their Interac card and enter their PIN.

### Capture and reconcile

Interac only supports payments that are authorized and captured in a single step. Unlike networks like Visa and Mastercard, Interac doesn’t support placing a “hold” on a card and capturing the funds later. Only payments with `automatic`, `automatic_async`, or `manual_preferred` capture type can be processed on Interac.

| Capture type         | Implementation                                                                                                                                                                                                                             | Result                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| **automatic**        | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) on the PaymentIntent to `automatic`.                                                                                     | All card payments are authorized and captured in a single step.                |
| **automatic_async**  | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) on the PaymentIntent to `automatic_async`.                                                                               | All card payments are authorized and captured asynchronously in a single step. |
| **manual_preferred** | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-capture_method) on the nested `payment_method_options.card_present` attribute to `manual_preferred`. | Interac card payments are authorized and captured in a single step.            |

Non-Interac card payments are authorized only. To [capture the funds](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment), make a separate request. |
| **manual** | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) on the PaymentIntent to `manual`. | Interac card payments are always declined.

Non-Interac card payments are authorized only. To [capture the funds](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment), make a separate request. |

Make sure that your application doesn’t continue to capture the `PaymentIntent` for Interac transactions. If you attempt to capture an `interac_present` payment, the Stripe API returns an error. Make sure that you prevent unintended and duplicate payments in your integration; if failures or declines occur while processing Interac, you can attempt to re-use the same `PaymentIntent` from the original transaction to safeguard against double-charging.

> As of the `2025-03-31.basil` API version, `interac_present` payments require the [capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) parameter to be set to `automatic`, `automatic_async`, or `manual_preferred` on the `PaymentIntent`.

### Refund an Interac payment

In-person refunds are mandatory for Interac transactions in Canada. You can’t create refunds in the API or in the Dashboard for these payments. In this flow, the reader prompts the cardholder to present the card used in the original charge. After the card details are read successfully, your application processes the refund. Like online refunds, you can perform partial refunds by passing in an amount less than the transaction value.

The currency and the card used for refund processing must match those of the original charge, otherwise the request fails with an error.

As a fallback, you can offer refunds to different payment methods such as store credit or cash.

#### Server-driven

To initiate an in-person refund for an Interac payment, call the [refund_payment](https://docs.stripe.com/api/terminal/readers/refund_payment.md) endpoint:

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const reader = await stripe.terminal.readers.refundPayment("tmr_xxx", {
  payment_intent: "pi_xxx",
  amount: 2000,
});
```

The [status of the reader action](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-status) is `in_progress`, as shown in the following example, until the customer presents a card on the reader:

```json
{
  "id": "tmr_xxx",
  "object": "terminal.reader",
  "action": {"type": "refund_payment",
    "refund_payment": {
      "payment_intent": "pi_xxx"
    },
    "status": "in_progress",
    "failure_code": null,
    "failure_message": null
  },
  …
}
```

If you’re using a [simulated reader](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven&reader=simulated), you can simulate payment method presentment with the [present_payment_method](https://docs.stripe.com/api/terminal/readers/present_payment_method.md) endpoint:

```curl
curl https://api.stripe.com/v1/test_helpers/terminal/readers/tmr_xxx/present_payment_method \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d type=interac_present
```

A successful refund generates a [terminal.reader.action_succeeded](https://docs.stripe.com/api/events/types.md#event_types-terminal.reader.action_succeeded) event. The reader’s `action.status` value changes to `succeeded`, and the `action.refund_payment` has a [refund](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-refund_payment-refund) attribute under it.

A failed refund generates a [terminal.reader.action_failed](https://docs.stripe.com/api/events/types.md#event_types-terminal.reader.action_failed) event. The reader’s `action.status` value changes to `failed`, and the [action.failure_code](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-failure_code) and [action.failure_message](https://docs.stripe.com/api/terminal/readers/object.md#terminal_reader_object-action-failure_message) properties each have a detailed failure explanation under them. The `action.refund_payment` property won’t have a `refund` attribute set under it.

We recommend using [webhooks](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#webhooks) to track when the reader action status changes.

#### JavaScript

```javascript
const result = await this.terminal.collectRefundPaymentMethod(
  "ch_xxxxxxxxxx",
  2000,
  "cad",
);

if (result.error) {
  // Placeholder for handling result.error
} else {
  const refund = await this.terminal.processRefund();
  if (refund.error) {
    // Placeholder for handling refund.error
  } else {
    console.log("Charge fully refunded!");
    return refund;
  }
}
```

#### iOS

#### Swift

```swift
let refundParams = try RefundParametersBuilder(
    chargeId: "ch_1FLyVV2eZvKYlo2C9Z8rmX02",
    amount: 1000,
    currency: "cad"
).build()

self.refundCancelable = Terminal.shared.processRefund(refundParams) { processedRefund, processError in
    if let error = processError {
        print("processRefund failed. \(error)")
    } else if let refund = processedRefund, refund.status == .succeeded {
        print("processRefund successful! \(refund)")
    } else {
        print("Refund pending or unsuccessful.")
    }
}
```

#### Android

#### Kotlin

```kotlin
val refundParams = RefundParameters.ByChargeId(
  id = "ch_1FLyVV2eZvKYlo2C9Z8rmX02",
  amount = 1000,
  currency = "cad"
).build()

val refundCancelable = Terminal.getInstance().processRefund(
    refundParams,
    object : RefundCallback {
        override fun onSuccess(refund: Refund) {
            if (refund.status == "succeeded") {
                println("processRefund successful!")
            } else {
                println("Refund pending or unsuccessful.")
            }
        }

        override fun onFailure(e: TerminalException) {
            // Placeholder for handling exception
        }
    }
)
```

#### React Native

```js
const { refund, error } = await processRefund({
  chargeId: "ch_1FLyVV2eZvKYlo2C9Z8rmX02",
  amount: 2000,
  currency: "cad",
});

if (error) {
  // Handle error
  return;
}

if (!refund || refund.status !== "succeeded") {
  // Refund pending or unsuccessful.
  return;
}

// Process refund successful!
```

# Singapore (SG)

> This is a Singapore (SG) for when integration-country is SG. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=SG.

## Integrate Terminal in Singapore

Stripe supports Visa, Mastercard, and American Express payments in Singapore. All transactions must be made in Singapore dollars (SGD). To accept Terminal charges in Singapore, either your platform account or connected account must be in Singapore.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in SG and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in SG. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in SG must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "19 Keppel Road",
    country: "SG",
    postal_code: "089058",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Singapore must use the reader software version `4.01.03.00_Prod_APAC1_off_v17_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

# United Kingdom (GB)

> This is a United Kingdom (GB) for when integration-country is GB. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=GB.

## Integrate Terminal in the United Kingdom

Stripe supports Visa, Mastercard, American Express, and Discover payments in the United Kingdom. All transactions must be made in British pounds (GBP). To accept Terminal charges in United Kingdom, either your platform account or connected account must be in United Kingdom.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in GB and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in GB. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in GB must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "448A Crownhill Rd",
    city: "Plymouth",
    country: "GB",
    postal_code: "PL5 2QT",
  },
});
```

### Reader software version

BBPOS WisePOS E readers operating in the United Kingdom must use the reader software version `1.5.0.0` or later. Read about [BBPOS WisePOS E software updates](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md#reader-software-version) for details.

Similarly, BBPOS WisePad 3 readers must use the reader software version `4.01.03.00_Prod_EU_W1_off_v23_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In GB, contact transactions authenticated with a PIN satisfy the SCA requirements. The chip represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Contactless card transactions, however, might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements.

When using Terminal hardware, the reader prompts the customer to insert their card for a chip-and-PIN transaction. You see two charges associated with these transactions if the customer re-enters their card. The first is a soft-declined charge with an `offline_pin_required` decline message and `contactless_emv` read method. The second is the authorized or hard-declined charge with `contact_emv` read method.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Ireland (IE)

> This is a Ireland (IE) for when integration-country is IE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=IE.

## Integrate Terminal in Ireland

Stripe supports Visa, Mastercard, American Express, and Discover payments in Ireland. All transactions must be made in euros (EUR). To accept Terminal charges in Ireland, either your platform account or connected account must be in Ireland.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in IE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in IE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in IE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Grand Canal Street Lower",
    city: "Dublin",
    country: "IE",
    postal_code: "D02 H210",
  },
});
```

### Reader software version

BBPOS WisePOS E readers operating in Ireland must use the reader software version `1.5.0.0` or later. Read about [BBPOS WisePOS E software updates](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md#reader-software-version) for details.

Similarly, BBPOS WisePad 3 readers must use the reader software version `4.01.03.00_Prod_EU_W1_off_v23_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In IE, contact transactions authenticated with a PIN satisfy the SCA requirements. The chip represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Contactless card transactions, however, might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements.

When using Terminal hardware, the reader prompts the customer to insert their card for a chip-and-PIN transaction. You see two charges associated with these transactions if the customer re-enters their card. The first is a soft-declined charge with an `offline_pin_required` decline message and `contactless_emv` read method. The second is the authorized or hard-declined charge with `contact_emv` read method.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Australia (AU)

> This is a Australia (AU) for when integration-country is AU. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=AU.

## Integrate Terminal in Australia

Stripe supports Visa, Mastercard, American Express, and [eftpos](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#eftpos-payments) payments in Australia. All transactions must be made in Australian dollars (AUD). To accept Terminal charges in Australia, either your platform account or connected account must be in Australia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in AU and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in AU. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in AU must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1234 Victoria Street",
    city: "Melbourne",
    state: "Victoria",
    country: "AU",
    postal_code: "3000",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Australia must use the reader software version `4.01.03.00_Prod_APAC1_on_v28_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

## eftpos payments

[Eftpos](https://www.eftposaustralia.com.au/) is Australia’s local debit card network. More than 90% of eftpos cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either network supported by the card.

Stripe processes co-branded eftpos cards over eftpos, Visa, or Mastercard depending on the [least cost routing requirements](https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia) and the [type of transaction](https://docs.stripe.com/terminal/payments/regional.md?integration-country=AU#identify-which-network-a-payment-was-processed-on).

### Availability

Eftpos is available to any business that uses Stripe in Australia, with the following exceptions:

- Massage parlors ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 7297)
- Financial institutions—manual cash disbursements ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 6010)
- Financial institutions—merchandise and services ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 6012)
- Non-financial institutions—foreign currency, money orders and travelers’ checks. ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 6051)
- Remote stored value load—merchant ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 6530)
- Stored value card purchase/load ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 6540)
- Wires, money orders ([MCC](https://docs.stripe.com/connect/setting-mcc.md) 4829)

Cash out transactions, where the business disburses cash to a customer, aren’t supported on Terminal.

### Integration requirements

To process in-person payments over the eftpos network, you need to make sure that your Terminal integration:

- Uses up-to-date Terminal SDKs

  If you use the Terminal [iOS SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=ios), [Android SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=android), or [React Native SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=react-native), you need to use the following minimum SDK versions to accept eftpos payments:
  - [iOS SDK 2.20.0](https://github.com/stripe/stripe-terminal-ios/releases), released on May 3, 2023
  - [Android SDK 2.20.0](https://github.com/stripe/stripe-terminal-android/releases), released on May 11, 2023
  - [React Native SDK 0.0.1-beta.12](https://github.com/stripe/stripe-terminal-react-native/releases), released on June 1, 2023

  You don’t need to make any changes if you use the Terminal [Javascript SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=js) or [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven).

- Uses `automatic`, `manual_preferred`, or `automatic_delayed` capture type on your payments

  Eftpos only supports payments that are authorized and captured in a single step. Unlike networks like Visa and Mastercard, eftpos doesn’t support placing a “hold” on a card and capturing the funds later. Only payments with `automatic`, `manual_preferred`, or `automatic_delayed` capture type can be processed on eftpos. When `automatic_delayed` is set, eftpos payments are authorized and captured immediately (equivalent to `automatic`), while non-eftpos card payments are authorized and automatically captured after a delay.

| Capture type         | Implementation                                                                                                                                                                                                                             | Result                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **automatic**        | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) on the PaymentIntent to `automatic`.                                                                                     | All card payments will be authorized and captured in a single step.    |
| **manual_preferred** | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-capture_method) on the nested `payment_method_options.card_present` attribute to `manual_preferred`. | eftpos card payments will be authorized and captured in a single step. |

    Non-eftpos card payments will be authorized only. To [capture the funds](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment), make a separate request.                                                                                                                                              |

| **automatic_delayed** | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-capture_method) on the nested `payment_method_options.card_present` attribute to `automatic_delayed`. | eftpos card payments will be authorized and captured in a single step (eftpos doesn’t support deferred capture).

    Non-eftpos card payments will be authorized and automatically captured after the delay period. Set [capture_delay_days](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-capture_delay_days) on `payment_method_options.card_present` to configure the delay. |

| **manual** | Set [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) on the PaymentIntent to `manual`. | ⚠ eftpos card payments will always decline.

    Non-eftpos card payments will be authorized only. To [capture the funds](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#capture-payment), make a separate request.                                                                                                                                                                         |

Alternatively, if you want to use manual capture for other payment methods while still accepting eftpos payments (which require automatic capture), use `manual_preferred`:

```curl
curl https://api.stripe.com/v1/payment_intents \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=999 \
  -d currency=aud \
  -d "payment_method_types[]=card_present" \
  -d "payment_method_options[card_present][capture_method]=manual_preferred"
```

### Refund an eftpos payment

Eftpos supports online refunds through the [API](https://docs.stripe.com/refunds.md?dashboard-or-api=api) or [Dashboard](https://docs.stripe.com/refunds.md?dashboard-or-api=dashboard). The cardholder isn’t required to present their card again at the point of sale.

### Routing multi-network debit cards

For co-branded, multi-network debit cards supporting both eftpos domestic debit and international card networks, Stripe uses the following default routing:

| Capture type          | Default routing for contact payments    | Default routing for contactless payments |
| --------------------- | --------------------------------------- | ---------------------------------------- |
| **automatic**         | Customer selects on the Terminal reader | eftpos                                   |
| **manual_preferred**  | Customer selects on the Terminal reader | International network                    |
| **automatic_delayed** | International network                   | International network                    |
| **manual**            | International network                   | International network                    |

You can optionally request a preferred network routing choice on PaymentIntent creation, by setting the [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute.

| Routing    | Implementation                                                                                                                                                                                                                                           | Result                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **eftpos** | Set [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute to `domestic` | For co-branded eftpos cards, Stripe prioritizes the eftpos network. |

Stripe will continue to authorize all other cards as-is. |
| **International networks** | Set [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute to `international` | For co-branded eftpos cards, Stripe prioritizes the international network.

Stripe will continue to authorize all other cards as-is. |

> Tap to Pay on iPhone supports [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) and [​capture_method](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-capture_method) for routing only in [Terminal iOS SDK](https://github.com/stripe/stripe-terminal-ios/releases) version 4.6.0 or newer.

### Identify which network a payment was processed on

To identify which network a payment was processed on, inspect the [network](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-network) field on the [Charge](https://docs.stripe.com/api/charges/object.md) object associated with a successful [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md).

```javascript
{
  "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
  "object": "charge",
  ...
  "payment_method_details": {
    "card_present": {
      "brand": "visa",
      ...
      "network": "eftpos_au"
    },
    "type": "card_present"
  }
}
```

# New Zealand (NZ)

> This is a New Zealand (NZ) for when integration-country is NZ. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=NZ.

## Integrate Terminal in New Zealand

Stripe supports Visa, Mastercard, and American Express payments in New Zealand. All transactions must be made in New Zealand dollars (NZD). To accept Terminal charges in New Zealand, either your platform account or connected account must be in New Zealand.

### eftpos payments

eftpos is the interbank network that handles routing of debit payments in New Zealand. Consumer debit cards in New Zealand are branded with an eftpos logo and might also be co-branded with Visa or Mastercard. Stripe can support co-branded eftpos over the co-brand rails.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in NZ and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in NZ. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in NZ must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "203 Victoria Street",
    city: "Auckland Central",
    country: "NZ",
    postal_code: "1010",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in New Zealand must use the reader software version `4.01.03.00_Prod_APAC1_on_v28_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

# France (FR)

> This is a France (FR) for when integration-country is FR. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=FR.

## Integrate Terminal in France

Stripe supports Visa, Mastercard, American Express, Discover, and Cartes Bancaires payments in France. All transactions must be made in euros (EUR). To accept Terminal charges in France, either your platform account or connected account must be in France.

### Reader software version

BBPOS WisePad 3 readers operating in France must use the reader software version `4.01.03.00_FR_v26_511001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

## Cartes Bancaires payments

Cartes Bancaires is the interbank network that handles routing of debit payments in France. Consumer debit cards in France are branded with a Cartes Bancaires logo and might also be co-badged with Visa or Mastercard. You can process these cards using either Cartes Bancaires or the international network. Terminal supports processing Cartes Bancaires cards by insert or NFC-based mechanisms, such as tap and mobile wallets (Apple Pay, Google Pay, and Samsung Pay).

### Enable Cartes Bancaires

French Stripe accounts can process Cartes Bancaires payments after providing their business tax ID in the Dashboard settings.

If you’re a Connect platform, and your connected accounts don’t have access to the full Stripe Dashboard (includes Express and Custom accounts) you must request the `cartes_bancaires_payments` [capability](https://docs.stripe.com/connect/account-capabilities.md#payment-methods) on behalf of your connected accounts.

### Integration requirements

To accept Cartes Bancaires payments, you must use:

- [BBPOS WisePad 3](https://stripe.com/fr/terminal/wisepad3) reader
- [Stripe Reader S700](https://stripe.com/fr/terminal/s700)
- [Stripe Reader S710](https://stripe.com/fr/terminal/s710)
- [Tap to Pay on Android](https://stripe.com/fr/terminal/tap-to-pay)

If you want to process transactions over Cartes Bancaires on Tap to Pay on iPhone, email us at [terminal-cb-beta@stripe.com](mailto:terminal-cb-beta@stripe.com).

If you use the BBPOS WisePad 3 reader, you must use the following minimum Terminal SDK versions:

- [iOS SDK](https://github.com/stripe/stripe-terminal-ios/releases) 3.2.0: Released on 17 November 2023
- [Android SDK](https://github.com/stripe/stripe-terminal-android/releases) 3.2.0: Released on 17 November 2023
- [React Native SDK](https://github.com/stripe/stripe-terminal-react-native/releases) v0.0.1-beta.14: Released on 6 December 2023

The minimum supported SDK version for Tap to Pay on Android is 5.2.0.

If you use the Terminal [JavaScript SDK](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=js) or [server-driven integration](https://docs.stripe.com/terminal/payments/setup-integration.md?terminal-sdk-platform=server-driven), you don’t need to make any changes.

If you use the embedded [Tap to Pay on iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) reader, you must use the following minimum Terminal SDK versions:

- [iOS SDK](https://github.com/stripe/stripe-terminal-ios/releases) 4.6.0: Released on 30 July 2025

The [BBPOS WisePOS E](https://stripe.com/fr/terminal/wisepose) reader doesn’t support the Cartes Bancaires network, and processes transactions from co-badged cards through only the international network.

### Routing co-badged debit cards

Co-badged Cartes Bancaires cards support both Cartes Bancaires and international card networks. If your integration supports Cartes Bancaires, you can choose to process the payment directly through Cartes Bancaires or through the international network.

When you create a PaymentIntent, specify your choice in the [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) parameter. [SetupIntents](https://docs.stripe.com/payments/setup-intents.md), which collect card details without charging the card, always process using the international network.

| Routing                             | Setting                                      | Result                                                                      |
| ----------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------- |
| Cartes Bancaires                    | Set `requested_priority` to `domestic`.      | - Co-badged Cartes Bancaires cards prioritize the Cartes Bancaires network. |
| - All other cards process normally. |
| International networks              | Set `requested_priority` to `international`. | - Co-badged Cartes Bancaires cards prioritize the international network.    |
| - All other cards process normally. |

Stripe Terminal provides default support for [compliance with customer card brand choice](https://docs.stripe.com/co-badged-cards-compliance.md) on the [BBPOS WisePad 3](https://stripe.com/fr/terminal/wisepad3), [Stripe Reader S700](https://stripe.com/fr/terminal/s700), and [Stripe Reader S710](https://stripe.com/fr/terminal/s710) readers. Customers who use a co-badged Cartes Bancaires card on a supported device can override your priority selection and choose their preferred network routing option, as shown in the following image.
![An application selection screen showing two card brands, one with Cartes Bancaires (CB) and the other Visa, on the WisePad 3 device.](assets/stripe-terminal-wisepad-cartes-bancaires-selection.png)

BBPOS WisePad 3
![An application selection screen showing two card brands, one with Cartes Bancaires (CB) and the other Visa, on the Stripe Reader S700/S710 device.](assets/stripe-terminal-s700-cartes-bancaires-selection.png)

Stripe Reader S700/S710

If you use [Tap to Pay on iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) to accept payments on co-badged cards, your integration must facilitate [card brand choice](https://docs.stripe.com/co-badged-cards-compliance.md) by allowing customers to select their preferred network at any point before initiating the tap. You must also pass the relevant [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) to Stripe before the customer initiates the tap.

### Refund a Cartes Bancaires payment

You can refund Cartes Bancaires payments through the [API](https://docs.stripe.com/refunds.md?dashboard-or-api=api) or [Dashboard](https://docs.stripe.com/refunds.md?dashboard-or-api=dashboard). Refunds don’t require the cardholder to present their card again at the point of sale.

### Identify the network

To identify which network a payment was processed on, inspect the [network](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-network) value of the [Charge](https://docs.stripe.com/api/charges/object.md) object associated with a successful [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md).

```javascript
{
  "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
  "object": "charge",
  ...
  "payment_method_details": {
    "card_present": {
      "brand": "visa",
      ..."network": "cartes_bancaires",
    },
    "type": "card_present"
  }
}
```

### Provide receipts

For Cartes Bancaires payments, Stripe includes additional metadata in the [prebuilt receipts](https://docs.stripe.com/terminal/features/receipts.md#prebuilt). For [custom receipts](https://docs.stripe.com/terminal/features/receipts.md#custom), the following required fields are available in the PaymentIntent as soon as the payment is [confirmed](https://docs.stripe.com/terminal/payments/collect-card-payment.md#confirm-payment).

| Field                                               | Description                                                                                                                                                                                                  |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `transaction_trace_number`                          | The transaction number generated by the acceptance system.                                                                                                                                                   |
| `siret_number`                                      | The [système d’identification du répertoire des établissements (establishment directory identification system)](https://support.stripe.com/questions/siren-and-siret-numbers) code assigned to the business. |
| `bank_code`                                         | The code for the bank that issued the card.                                                                                                                                                                  |
| `acceptor_identifier`                               | The acceptor identifier.                                                                                                                                                                                     |
| `acceptance_system_terminal_application_identifier` | The identifier for the terminal application used to process the transaction.                                                                                                                                 |
| `card_acceptor_logical_number`                      | The logical number of the card acceptance point.                                                                                                                                                             |
| `system_acceptor_logical_number`                    | The logical number of the acceptance system.                                                                                                                                                                 |

## Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in FR and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in FR. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in FR must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "19 Rue de Vienne",
    city: "Paris",
    country: "FR",
    postal_code: "75008",
  },
});
```

## Translation

Language regulations require that services, including point-of-sale services, be provided in French unless English has been agreed upon by the cardholder and their card issuer. Terminal is built to help you comply with these requirements if they apply to your business.

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in FR, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you’re required to provide services in or would like to translate text into French in addition to English, ensure that any of your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

## Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In FR, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Germany (DE)

> This is a Germany (DE) for when integration-country is DE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=DE.

## Integrate Terminal in Germany

Stripe supports Visa, Mastercard, American Express, Discover, and girocard payments in Germany. All transactions must be made in euros (EUR). To accept Terminal charges in Germany, either your platform account or connected account must be in Germany.

## girocard payments

[girocard](https://www.girocard.eu/) is an interbank network that handles routing of debit card payments in Germany. Most consumer debit cards in Germany are branded with a girocard logo and co-badged with Visa or Mastercard (or their sub-brands like V-Pay or Maestro). You can process these cards over either supported network.

### Integration requirements

To accept girocard payments, you must use one of the following readers:

- [BBPOS WisePad 3](https://stripe.com/de/terminal/wisepad3) with the following minimum Terminal SDK versions:
  - [iOS SDK](https://github.com/stripe/stripe-terminal-ios/releases) 2.17.0: Released on 31 January 2023
  - [Android SDK](https://github.com/stripe/stripe-terminal-android/releases) 2.17.0: Released on 2 February 2023
  - [React Native SDK](https://github.com/stripe/stripe-terminal-react-native/releases) 0.0.1-beta.12: Released on 1 June 2023

- [Stripe Reader S700](https://stripe.com/de/terminal/s700)

The [BBPOS WisePOS E](https://stripe.com/de/terminal/wisepose) reader doesn’t support girocard. This device can continue to process transactions from co-badged cards with Visa and Mastercard.

### Routing co-badged debit cards

Co-badged girocard debit cards support both girocard and international card networks. If your integration supports girocard, then when you create a PaymentIntent you can choose whether to process the payment directly through girocard or the co-badged network.

To do so, set the [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute for this purpose.

| Routing                | Implementation                                                                                                                                                                                                                                                | Result                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| girocard               | Set [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute to `domestic`      | For co-badged girocard cards, the girocard network is prioritized. All other cards will be processed as-is.      |
| International networks | Set [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) on the nested `payment_method_options.card_present.routing` attribute to `international` | For co-badged girocard cards, the international network is prioritized. All other cards will be processed as-is. |

Stripe Terminal also supports customer [card brand choice](https://docs.stripe.com/co-badged-cards-compliance.md) by default to help you meet [applicable requirements](https://docs.stripe.com/co-badged-cards-compliance.md). Customers who insert a co-badged girocard card into a supported device can override your priority selection to exercise choice by selecting their preferred network routing option.
![wisepad-3](assets/stripe-terminal-wisepad-girocard-selection.png)

[SetupIntents](https://docs.stripe.com/payments/setup-intents.md), which are used to collect card details without charging the card, are always routed to the international network. This is because girocard doesn’t support [off-session](https://support.stripe.com/questions/what-is-the-difference-between-on-session-and-off-session-and-why-is-it-important) payments initiated by a business.

### Refund a girocard payment

You can refund girocard payments through the [API](https://docs.stripe.com/refunds.md?dashboard-or-api=api) or [Dashboard](https://docs.stripe.com/refunds.md?dashboard-or-api=dashboard). The cardholder isn’t required to present their card again at the point of sale.

The girocard network doesn’t natively support refunds. As a workaround, Stripe sends the refund by SEPA transfer to the customer’s bank account, using the IBAN associated with their girocard.

To check the status of the transfer, inspect the [Refund](https://docs.stripe.com/api/refunds/object.md) object. Be aware that the refund might fail—for instance, if the customer closes their bank account or the transfer can’t be processed.

### Identify the network

To identify which network a payment was processed on, inspect the [network](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-network) value of the [Charge](https://docs.stripe.com/api/charges/object.md) object associated with a successful [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md).

```javascript
{
  "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
  "object": "charge",
  ...
  "payment_method_details": {
    "card_present": {
      "brand": "visa",
      ...
      "network": "girocard"
    },
    "type": "card_present"
  }
}
```

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in DE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in DE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in DE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Jarrestrasse 80",
    city: "Hamburg",
    country: "DE",
    postal_code: "22303",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Germany must use the reader software version `4.01.03.00_DE_v31_511001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

Language regulations require that services, including point-of-sale services, be provided in German unless English has been agreed upon by the cardholder and their card issuer. Terminal is built to help you comply with these requirements if they apply to your business.

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in DE, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you’re required to provide services in or would like to translate text into German in addition to English, ensure that any of your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In DE, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Netherlands (NL)

> This is a Netherlands (NL) for when integration-country is NL. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=NL.

## Integrate Terminal in the Netherlands

Stripe supports Visa, Mastercard, American Express, and Discover payments in the Netherlands. All transactions must be made in euros (EUR). To accept Terminal charges in the Netherlands, either your platform account or connected account must be in the Netherlands.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in NL and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in NL. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in NL must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Frederik Roeskestraat 96",
    city: "Amsterdam",
    country: "NL",
    postal_code: "1076ED",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in the Netherlands must use the reader software version `4.01.03.00_Prod_EU_W1_on_v28_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in NL, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Dutch in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In NL, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Austria (AT)

> This is a Austria (AT) for when integration-country is AT. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=AT.

## Integrate Terminal in Austria

Stripe supports Visa, Mastercard, American Express, and Discover payments in Austria. All transactions must be made in euros (EUR). To accept Terminal charges in Austria, either your platform account or connected account must be in Austria.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in AT and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in AT. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in AT must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Hernalser Hauptstraße 11",
    city: "Vienna",
    country: "AT",
    postal_code: "1170",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Austria must use the reader software version `4.01.03.00_Prod_EU_W1_on_v28_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in AT, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into German in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In AT, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Belgium (BE)

> This is a Belgium (BE) for when integration-country is BE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=BE.

## Integrate Terminal in Belgium

Stripe supports Visa, Mastercard, American Express, and Discover payments in Belgium. All transactions must be made in euros (EUR). To accept Terminal charges in Belgium, either your platform account or connected account must be in Belgium.

### Bancontact payments

Bancontact is the interbank network that handles routing of debit payments in Belgium. Consumer debit cards in Bancontact are branded with a Bancontact logo and might also be co-branded with Visa or Mastercard. Stripe can support co-branded Bancontact over the co-brand rails.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in BE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in BE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in BE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Rue du Lombard 5-9",
    city: "Bruxelles",
    country: "BE",
    postal_code: "1000",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Belgium must use the reader software version `4.01.03.00_Prod_EU_W1_on_v28_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in BE, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Dutch, French, and German in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In BE, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Denmark (DK)

> This is a Denmark (DK) for when integration-country is DK. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=DK.

## Integrate Terminal in Denmark

Stripe supports Visa, Mastercard, American Express, and Discover payments in Denmark. All transactions must be made in Danish krone (DKK). To accept Terminal charges in Denmark, either your platform account or connected account must be in Denmark.

### Dankort payments

Dankort is the interbank network that handles routing of debit payments in Denmark. Consumer debit cards in Dankort are branded with a Dankort logo and might also be co-branded with Visa. Stripe can support co-branded Dankort over the co-brand rails.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in DK and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in DK. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in DK must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Baunegårdsvej 3A",
    city: "Gentofte",
    country: "DK",
    postal_code: "2820",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Denmark must use the reader software version `4.01.03.00_Prod_EU_W2_on_v21_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in DK, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Danish in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In DK, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Spain (ES)

> This is a Spain (ES) for when integration-country is ES. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=ES.

## Integrate Terminal in Spain

Stripe supports Visa, Mastercard, American Express, and Discover payments in Spain. All transactions must be made in euros (EUR). To accept Terminal charges in Spain, either your platform account or connected account must be in Spain.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in ES and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in ES. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in ES must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Calle Pedro Laborde 24",
    city: "Madrid",
    state: "Madrid",
    country: "ES",
    postal_code: "28018",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Spain must use the reader software version `4.01.03.00_Prod_EU_W3_on_v13_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in ES, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Spanish in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In ES, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Sweden (SE)

> This is a Sweden (SE) for when integration-country is SE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=SE.

## Integrate Terminal in Sweden

Stripe supports Visa, Mastercard, American Express, and Discover payments in Sweden. All transactions must be made in Swedish krona (SEK). To accept Terminal charges in Sweden, either your platform account or connected account must be in Sweden.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in SE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in SE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in SE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Hornsgatan 98",
    city: "Stockholm",
    country: "SE",
    postal_code: "118 21",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Sweden must use the reader software version `4.01.03.00_Prod_EU_W2_on_v21_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in SE, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Swedish in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In SE, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Hong Kong (HK)

> This is a Hong Kong (HK) for when integration-country is HK. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=HK.

## Integrate Terminal in Hong Kong

Stripe supports Visa, Mastercard, and American Express payments in Hong Kong. All transactions must be made in Hong Kong dollars (HKD). To accept Terminal charges in Hong Kong, either your platform account or connected account must be in Hong Kong.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in HK and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in HK. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in HK must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "8 Wang Hoi Road",
    city: "Kowloon Bay",
    state: "Kowloon",
    country: "HK",
    postal_code: "",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Hong Kong must use the reader software version `4.01.03.00_Prod_APAC1_off_v17_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

# Malaysia (MY)

> This is a Malaysia (MY) for when integration-country is MY. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=MY.

## Integrate Terminal in Malaysia

Stripe supports Visa and Mastercard payments in Malaysia. All transactions must be made in Malaysian ringgit (MYR). To accept Terminal charges in Malaysia, either your platform account or connected account must be in Malaysia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in MY and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in MY. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in MY must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "170, Jalan Maarof",
    city: "Bangsar",
    state: "Kuala Lumpur",
    country: "MY",
    postal_code: "59100",
  },
});
```

### Reader software version

BBPOS WisePad 3 readers operating in Malaysia must use the reader software version `4.01.03.00_Prod_APAC1_on_v28_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

# Czech Republic (CZ)

> This is a Czech Republic (CZ) for when integration-country is CZ. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=CZ.

## Integrate Terminal in the Czech Republic

Stripe supports Visa, Mastercard, American Express, and Discover payments in the Czech Republic. All transactions must be made in Czech Koruna (CZK). To accept Terminal charges in the Czech Republic, either your platform account or connected account must be in the Czech Republic.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in CZ and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in CZ. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in CZ must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Vodičkova 15",
    city: "Nové Město",
    country: "CZ",
    postal_code: "110 00",
  },
});
```

# Portugal (PT)

> This is a Portugal (PT) for when integration-country is PT. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=PT.

## Integrate Terminal in Portugal

Stripe supports Visa, Mastercard, American Express, and Discover payments in Portugal. All transactions must be made in euros (EUR). To accept Terminal charges in Portugal, either your platform account or connected account must be in Portugal.

### Multibanco payments

Multibanco is the interbank network that handles routing of debit payments in Portugal. Consumer debit cards in Portugal are branded with a Multibanco logo and might also be co-branded with Visa or Mastercard. Stripe can support co-branded Multibanco over the co-brand rails.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in PT and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in PT. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in PT must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "R. Sebastião José de Carvalho",
    city: "Cascais",
    country: "PT",
    postal_code: "2750-000",
  },
});
```

# Finland (FI)

> This is a Finland (FI) for when integration-country is FI. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=FI.

## Integrate Terminal in Finland

Stripe supports Visa, Mastercard, American Express, and Discover payments in Finland. All transactions must be made in euros (EUR). To accept Terminal charges in Finland, either your platform account or connected account must be in Finland.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in FI and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in FI. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in FI must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Kangasalantie 36",
    city: "Tampere",
    country: "FI",
    postal_code: "33710",
  },
});
```

# Luxembourg (LU)

> This is a Luxembourg (LU) for when integration-country is LU. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=LU.

## Integrate Terminal in Luxembourg

Stripe supports Visa, Mastercard, American Express, and Discover payments in Luxembourg. All transactions must be made in euros (EUR). To accept Terminal charges in Luxembourg, either your platform account or connected account must be in Luxembourg.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in LU and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in LU. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in LU must contain the properties.

#### Node.js

```javascript

// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require('stripe')('<<YOUR_SECRET_KEY>>');

const location = await stripe.terminal.locations.create({
  display_name: 'HQ',
  address: {
    line1: 'Rue de Grass 972, 2-6 Pl. d'Armes',
    city: 'Luxembourg',
    state: 'Luxembourg',
    country: 'LU',
    postal_code: '1368',
  }
})
```

# Italy (IT)

> This is a Italy (IT) for when integration-country is IT. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=IT.

## Integrate Terminal in Italy

Stripe supports Visa, Mastercard, American Express, and Discover payments in Italy. All transactions must be made in euros (EUR). To accept Terminal charges in Italy, either your platform account or connected account must be in Italy.

### Pago Bancomat payments

Pago Bancomat is the interbank network that handles routing of debit payments in Italy. Consumer debit cards in Italy are branded with a Pago Bancomat logo and might also be co-branded with Visa or Mastercard. Stripe can support co-branded Pago Bancomat over the co-brand rails.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in IT and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in IT. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in IT must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Piazza Regina Margherita, 15",
    city: "Roma",
    state: "RM",
    country: "IT",
    postal_code: "00198",
  },
});
```

# Switzerland (CH)

> This is a Switzerland (CH) for when integration-country is CH. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=CH.

## Integrate Terminal in Switzerland

Stripe supports Visa, Mastercard, American Express, and Discover payments in Switzerland. All transactions must be made in Swiss franc (CHF). To accept Terminal charges in Switzerland, either your platform account or connected account must be in Switzerland.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in CH and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in CH. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in CH must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Via Schliffras 87",
    city: "Galgenen",
    country: "CH",
    postal_code: "8854",
  },
});
```

### Reader software version

BBPOS WisePOS E readers operating in Switzerland must use the reader software version `1.5.0.0` or later. Read about [BBPOS WisePOS E software updates](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md#reader-software-version) for details.

Similarly, BBPOS WisePad 3 readers must use the reader software version `4.01.03.00_Prod_EU_W1_on_v28_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in CH, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into German in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

# Norway (NO)

> This is a Norway (NO) for when integration-country is NO. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=NO.

## Integrate Terminal in Norway

Stripe supports Visa, Mastercard, American Express, and Discover payments in Norway. All transactions must be made in Norwegian krone (NOK). To accept Terminal charges in Norway, either your platform account or connected account must be in Norway.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in NO and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in NO. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in NO must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Thomaskroken 205",
    city: "Alta",
    country: "NO",
    postal_code: "9513",
  },
});
```

### Reader software version

BBPOS WisePOS E readers operating in Norway must use the reader software version `1.5.0.0` or later. Read about [BBPOS WisePOS E software updates](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md#reader-software-version) for details.

Similarly, BBPOS WisePad 3 readers must use the reader software version `4.01.03.00_Prod_EU_W2_on_v21_510001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in NO, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Norwegian in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

# Poland (PL)

> This is a Poland (PL) for when integration-country is PL. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=PL.

## Integrate Terminal in Poland

Stripe supports Visa, Mastercard, American Express, and Discover payments in Poland. All transactions must be made in Polish złoty (PLN). To accept Terminal charges in Poland, either your platform account or connected account must be in Poland.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in PL and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in PL. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in PL must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "plac Grunwaldzki 21",
    city: "Warszawa",
    country: "PL",
    postal_code: "01-787",
  },
});
```

### Translation

#### Default reader language

The [BBPOS WisePOS E](https://docs.stripe.com/terminal/readers/bbpos-wisepos-e.md) and [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) support changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in PL, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Polish in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

# Japan (JP)

> This is a Japan (JP) for when integration-country is JP. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=JP.

## Integrate Terminal in Japan (Preview)

Stripe supports Visa, Mastercard, American Express, JCB, and Discover payments in Japan. All transactions must be made in Japanese yen (JPY). To accept Terminal charges in Japan, either your platform account or connected account must be in Japan.

> Saving payment details is only supported [after collecting a payment](https://docs.stripe.com/terminal/features/saving-payment-details/save-after-payment.md).

### Contactless payment support

Contactless cards and wallets in Japan use different payment networks that affect compatibility with Stripe Terminal:

- **International contactless**: Standard contactless technology supported globally. See our [list of supported networks](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md), which includes Visa, Mastercard and JCB.
- **Local contactless**: Japan-specific networks, such as iD and QUICPay.

Stripe Terminal only supports international contactless networks. Some cards in Japan, including physical cards and cards added to wallets like Apple Pay or Google Pay might only support local networks (iD or QUICPay) and won’t work with Terminal readers, even if the underlying card displays a supported card brand logo.

Cards that display the contactless “wave” symbol work with Terminal because they support the international contactless standard.

### Use locations

[Create Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in Japan and associate your readers to them. This ensures that they automatically download the configuration needed to properly process charges in Japan. The [Terminal Location](https://docs.stripe.com/api/terminal/locations.md) object for Japan requires different fields than other countries. You can’t set the [address](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) field for locations in Japan.

The new [address_kana](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address_kana) and [address_kanji](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address_kanji) fields contain the same fields as the existing [address](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) field, with the addition of an optional `town` field. A valid [Terminal Location](https://docs.stripe.com/api/terminal/locations.md) in Japan must contain:

One or both of:

- `address_kana`
- `address_kanji`

At least one of:

- `display_name`
- `display_name_kana`
- `display_name_kanji`

and can optionally contain the `phone` field.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  address: {},
  display_name: "My Shop",
  display_name_kana: "わたしの　みせ",
  display_name_kanji: "私の店",
  address_kana: {
    line1: "6-36-401",
    line2: "ニシコウエンハイツ",
    town: "ｱﾗﾄ 3-",
    city: "ﾌｸｵｶｼ ﾁﾕｳｵｳｸ",
    state: "ﾌｸｵｶｹﾝ",
    country: "JP",
    postal_code: "810-0062",
  },
  address_kanji: {
    line1: "6-36-401",
    line2: "西公園ハイツ",
    town: "荒戸　３丁目",
    city: "福岡市　中央区",
    state: "福岡県",
    country: "JP",
    postal_code: "８１０００６２",
  },
  phone: "+819012345678",
});
```

### Reader software version

Stripe S700/S710 readers operating in Japan must use the reader software version 2.34.3.0 or later. For details, see the [Stripe Reader S700/S710 software update](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md#reader-software-version). Similarly, BBPOS WisePad 3 readers operating in Japan must use the reader software version `4.01.03.00_JP_v14_491001` or later. Read about [BBPOS WisePad 3 software updates](https://docs.stripe.com/terminal/payments/connect-reader.md?reader-type=bluetooth#update-reader) for details.

### Translation

#### Default reader language

The [Stripe Reader S700/S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) supports changing reader language in the Settings panel. Swipe right across the screen to access the Settings panel, and select your language.

The [BBPOS WisePad 3](https://docs.stripe.com/terminal/readers/bbpos-wisepad3.md) supports changing reader language directly in the reader interface. After you have registered your reader to a [Location](https://docs.stripe.com/api/terminal/locations.md) with an address in JP, the reader installs a language pack relevant for your region if one isn’t already in place. To view available language options and to select a language, click the **Power / Settings** button and scroll down using the arrow keys until you reach the language selection menu. Highlight your desired language and press the green **Enter** key.

#### Other translations

If you would like to translate text into Japanese in addition to English, ensure that your [custom reader screens](https://docs.stripe.com/terminal/features/display.md) and [receipts](https://docs.stripe.com/terminal/features/receipts.md) display the appropriate translations.

# United Arab Emirates (AE)

> This is a United Arab Emirates (AE) for when integration-country is AE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=AE.

## Integrate Terminal in United Arab Emirates (Private preview)

Stripe supports Visa and Mastercard payments in United Arab Emirates. All transactions must be made in United Arab Emirates dirhams (AED). To accept Terminal charges in United Arab Emirates, either your platform account or connected account must be in United Arab Emirates.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in AE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in AE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in AE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "17B Street",
    city: "Dubai",
    state: "Dubai",
    country: "AE",
    postal_code: "",
  },
});
```

# Bulgaria (BG)

> This is a Bulgaria (BG) for when integration-country is BG. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=BG.

## Integrate Terminal in Bulgaria (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Bulgaria. All transactions must be made in EUR. To accept Terminal charges in Bulgaria, either your platform account or connected account must be in Bulgaria.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in BG and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in BG. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in BG must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "1-3, Trifon Kunev",
    city: "Sofia",
    state: "Sofia-City",
    country: "BG",
    postal_code: "1734",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In BG, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Cyprus (CY)

> This is a Cyprus (CY) for when integration-country is CY. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=CY.

## Integrate Terminal in Cyprus (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Cyprus. All transactions must be made in euros (EUR). To accept Terminal charges in Cyprus, either your platform account or connected account must be in Cyprus.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in CY and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in CY. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in CY must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Amathountos Avenue 67/69",
    city: "Agios Tychon",
    country: "CY",
    postal_code: "4532",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In CY, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Estonia (EE)

> This is a Estonia (EE) for when integration-country is EE. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=EE.

## Integrate Terminal in Estonia (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Estonia. All transactions must be made in euros (EUR). To accept Terminal charges in Estonia, either your platform account or connected account must be in Estonia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in EE and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in EE. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in EE must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Vana-Viru 7",
    city: "Tallinn",
    country: "EE",
    postal_code: "15097",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In EE, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Gibraltar (GI)

> This is a Gibraltar (GI) for when integration-country is GI. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=GI.

## Integrate Terminal in Gibraltar (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Gibraltar. All transactions must be made in British pounds (GBP). To accept Terminal charges in Gibraltar, either your platform account or connected account must be in Gibraltar.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in GI and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in GI. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in GI must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "55 Line Wall Rd",
    city: "Gibraltar",
    country: "GI",
    postal_code: "GX11 1AA",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In GI, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Greece (GR)

> This is a Greece (GR) for when integration-country is GR. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=GR.

## Integrate Terminal in Greece (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Greece. All transactions must be made in euros (EUR). To accept Terminal charges in Greece, either your platform account or connected account must be in Greece.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in GR and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in GR. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in GR must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Eleytherioy Venizeloy 21",
    city: "Athina",
    country: "GR",
    postal_code: "10250",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In GR, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Croatia (HR)

> This is a Croatia (HR) for when integration-country is HR. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=HR.

## Integrate Terminal in Croatia (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Croatia. All transactions must be made in euros (EUR). To accept Terminal charges in Croatia, either your platform account or connected account must be in Croatia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in HR and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in HR. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in HR must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Ul. Zrinsko Frankopanska 52",
    city: "Split",
    country: "HR",
    postal_code: "21000",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In HR, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Hungary (HU)

> This is a Hungary (HU) for when integration-country is HU. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=HU.

## Integrate Terminal in Hungary (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Hungary. All transactions must be made in Hungarian forint (HUF). To accept Terminal charges in Hungary, either your platform account or connected account must be in Hungary.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in HU and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in HU. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in HU must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Bem rakpart 27.",
    city: "Szamoskér",
    state: "Szabolcs-Szatmár-Bereg",
    country: "HU",
    postal_code: "4721",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In HU, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Liechtenstein (LI)

> This is a Liechtenstein (LI) for when integration-country is LI. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=LI.

## Integrate Terminal in Liechtenstein (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Liechtenstein. All transactions must be made in Swiss francs (CHF). To accept Terminal charges in Liechtenstein, either your platform account or connected account must be in Liechtenstein.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in LI and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in LI. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in LI must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "8, Kleinsteg",
    city: "Wisli",
    state: "Oberland",
    country: "LI",
    postal_code: "9497",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In LI, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Lithuania (LT)

> This is a Lithuania (LT) for when integration-country is LT. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=LT.

## Integrate Terminal in Lithuania (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Lithuania. All transactions must be made in euros (EUR). To accept Terminal charges in Lithuania, either your platform account or connected account must be in Lithuania.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in LT and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in LT. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in LT must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Contess, 21B, Metalo g.",
    city: "Vilnius",
    state: "Vilnius County",
    country: "LT",
    postal_code: "02190",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In LT, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Latvia (LV)

> This is a Latvia (LV) for when integration-country is LV. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=LV.

## Integrate Terminal in Latvia (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Latvia. All transactions must be made in euros (EUR). To accept Terminal charges in Latvia, either your platform account or connected account must be in Latvia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in LV and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in LV. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in LV must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Ezeru iela 22a",
    city: "Jurmala",
    country: "LV",
    postal_code: "2008",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In LV, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Malta (MT)

> This is a Malta (MT) for when integration-country is MT. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=MT.

## Integrate Terminal in Malta (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Malta. All transactions must be made in euros (EUR). To accept Terminal charges in Malta, either your platform account or connected account must be in Malta.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in MT and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in MT. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in MT must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "64, Triq il-Velleran",
    city: "Il-Fgura",
    state: "South Eastern Region",
    country: "MT",
    postal_code: "ZTN 3000",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In MT, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Romania (RO)

> This is a Romania (RO) for when integration-country is RO. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=RO.

## Integrate Terminal in Romania (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Romania. All transactions must be made in Romanian leu (RON). To accept Terminal charges in Romania, either your platform account or connected account must be in Romania.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in RO and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in RO. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in RO must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "74A, Strada Rudeni",
    city: "Chitila",
    state: "Ilfov",
    country: "RO",
    postal_code: "077046",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In RO, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Slovenia (SI)

> This is a Slovenia (SI) for when integration-country is SI. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=SI.

## Integrate Terminal in Slovenia (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Slovenia. All transactions must be made in euros (EUR). To accept Terminal charges in Slovenia, either your platform account or connected account must be in Slovenia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in SI and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in SI. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in SI must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "158, Slape",
    city: "Ljubljana",
    country: "SI",
    postal_code: "1260",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In SI, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).

# Slovakia (SK)

> This is a Slovakia (SK) for when integration-country is SK. View the full page at https://docs.stripe.com/terminal/payments/regional?integration-country=SK.

## Integrate Terminal in Slovakia (Private preview)

Stripe supports Visa, Mastercard, and American Express payments in Slovakia. All transactions must be made in euros (EUR). To accept Terminal charges in Slovakia, either your platform account or connected account must be in Slovakia.

### Use locations

Create [Locations](https://docs.stripe.com/api/terminal/locations/create.md) for your business with addresses in SK and [associate your readers to them](https://docs.stripe.com/terminal/fleet/locations-and-zones.md). This will ensure that they automatically download the configuration needed to properly process charges in SK. A valid [address for a Location](https://docs.stripe.com/api/terminal/locations/create.md#create_terminal_location-address) in SK must contain the properties.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const location = await stripe.terminal.locations.create({
  display_name: "HQ",
  address: {
    line1: "Landererova",
    city: "Bratislava I",
    country: "SK",
    postal_code: "811 09",
  },
});
```

### Strong Customer Authentication

_Strong Customer Authentication_ (Strong Customer Authentication (SCA) is a regulatory requirement in effect as of September 14, 2019, that impacts many European online payments. It requires customers to use two-factor authentication like 3D Secure to verify their purchase) (SCA) is a European regulatory requirement to reduce fraud and make payments more secure. SCA is or will be required for _customer-initiated_ electronic payments within the _European Economic Area_ (The European Economic Area is a regional single market with free movement of labor, goods, and capital. It encompasses the European Union member states and three additional states that are part of the European Free Trade Association) (EEA). For more information about this European regulation, you can read Stripe’s [PSD2: SCA guide](https://stripe.com/guides/strong-customer-authentication).

Transactions below 50 euros (or the local currency equivalent) are considered _low value_ and might be exempted from SCA. However, banks need to request authentication if the _low value_ exemption has been used five times since the cardholder’s last successful authentication or if the sum of previously exempted payments exceeds 150 euros (or the local currency equivalent).

In SK, all transactions authenticated with a PIN satisfy the SCA requirements. The card represents the first authentication element of the transaction (possession) and the PIN represents the second (knowledge). Some contactless cards might support PIN validation with a single tap; however, others might require initiating an authenticated Chip and PIN contact transaction to comply with the SCA requirements, which requires inserting the card into the reader.

When using Terminal hardware, the reader prompts the customer to enter their PIN or insert their card for a chip-and-PIN transaction. You see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required` or `offline_pin_required`, depending on the card’s capabilities. The second is the authorized or hard-declined charge.

When using Tap to Pay, the device prompts the customer to enter their PIN if contactless PIN validation is supported. If contactless PIN is supported, you see two charges associated with SCA-authenticated transactions. The first is a soft-declined charge with an error message `online_or_offline_pin_required`. The second is the authorized or hard-declined charge. If contactless PIN isn’t supported, the payment will be hard-declined before the PIN screen appears, with the reason `online_or_offline_pin_required` or `offline_pin_required`. If the card is hard-declined we recommend asking the customer to try a different card or collecting payment in a different way. For example, by sending a [Payment Link](https://docs.stripe.com/payment-links.md).
