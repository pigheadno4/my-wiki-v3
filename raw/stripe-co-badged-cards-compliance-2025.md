<!-- Source URL: https://docs.stripe.com/co-badged-cards-compliance -->
<!-- Fetched: 2026-05-01 -->

# Co-badged cards compliance

Learn about EU regulations requiring customer choice for co-badged cards.

[Regulation (EU) 2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751) requires businesses in the European Economic Area (EEA) to honor customers’ card brand choice for co-badged cards (for example, [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires.md) cards co-badged with Visa). This means you must allow cardholders to select a preferred card brand on your payment page in accordance with these guidelines:

- **Display the available card networks on your online payment page or in-person checkout flow:** All available card networks must be clearly identified during the checkout process. The visual quality, clarity, and size of the brand logos must be consistent, and it should be clear to cardholders how to select a card network.
- **Abide by the cardholder’s preferred card network:** Where the cardholder chooses their preferred card network, you must use it when confirming a payment or storing card details for future use. If the cardholder doesn’t make a choice, you can choose your card network for the transaction.
- **Allow updates to the preferred card network:** You must present cardholders updating their payment methods that are saved for future use with the option to change their preferred card network when they’re updating their payment details. For example, you can provide a customer portal for managing saved payment methods.

> #### Does this regulation apply to me?
>
> [Regulation (EU) 2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751) applies to all businesses in the EEA that can process Cartes Bancaires. [Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fco-badged-cards-compliance) and return to this section to view if co-badged card regulation applies to you.

## When regulation applies

[Regulation (EU) 2015/751](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015R0751) applies to the following businesses and Stripe-supported transaction types:

| Payment channel | Subject to card brand choice regulation                                                                                                                        | Transaction types                                                                 |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Online          | Businesses in the EEA that can process Cartes Bancaires                                                                                                        | The payment method is a co-badged Cartes Bancaires card, and the currency is EUR. |
| In-person       | Businesses in France that can process [Cartes Bancaires](https://docs.stripe.com/terminal/payments/regional.md?integration-country=FR#enable-cartes-bancaires) | The payment method is a co-badged Cartes Bancaires card.                          |
| In-person       | Businesses in Germany that can process [Girocard](https://docs.stripe.com/terminal/payments/regional.md?integration-country=DE#girocard-payments)              | The payment method is a co-badged Girocard.                                       |

**Applicable in:**

- AT
- BE
- BG
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GR
- HR
- HU
- IE
- IS
- IT
- LI
- LT
- LU
- LV
- MT
- NL
- NO
- PL
- PT
- RO
- SE
- SI
- SK

## Integration guides

Stripe-hosted UIs, such as [Checkout](https://docs.stripe.com/payments/checkout.md), [Payment Links](https://docs.stripe.com/payment-links.md), [Elements](https://docs.stripe.com/payments/elements.md), and [Stripe Terminal](https://docs.stripe.com/terminal.md), automatically display a network selector when you meet the [applicability criteria](https://docs.stripe.com/co-badged-cards-compliance.md#when-regulation-applies). You must configure these UIs according to the guides below.

For other integrations, you’re fully responsible for making sure your integration complies with the regulation requirements.

> #### Sandbox environments
>
> When using sandboxes, Cartes Bancaires is always enabled for online payments, which means you might see the network selector on Stripe-hosted UIs in a sandbox, even if you don’t enable Cartes Bancaires. This allows you to preview how Stripe-hosted UIs handle co-badged cards if Cartes Bancaires were enabled.

# Checkout and Payment Links

> This is a Checkout and Payment Links for when type is checkout-payment-links. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=checkout-payment-links.

[Stripe Checkout](https://stripe.com/checkout) supports customer card brand choice, by default. Customers who enter a co-badged card in Checkout can select their option for card brand choice.
![The card input with a co-badged card in Stripe Checkout](assets/stripe-co-badged-checkout.png)

Card input with a co-badged card

# Web Payment Element

> This is a Web Payment Element for when type is web-elements and ui is payment-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=web-elements&ui=payment-element.

The [Payment Element](https://docs.stripe.com/payments/payment-element.md) supports customer card brand choice, by default. Customers who enter a co-badged card in the Payment Element can select their option for card brand choice.
![The card input with a co-badged card in Payment Element](assets/stripe-co-badged-payment-element.png)

Card input with a co-badged card

### Connect platforms

Connect platforms that use the `on_behalf_of` property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) in a [Payment Element created without an Intent](https://docs.stripe.com/payments/accept-a-payment-deferred.md) must also specify [onBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf) on the Elements group of the Payment Element. This allows the Payment Element to determine when to display the card brand choice dropdown.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

```javascript
const elements = stripe.elements({
  mode: 'payment',
  amount: 1099,
  currency: 'usd',
  onBehalfOf: 'CONNECTED_STRIPE_ACCOUNT_ID',
});

const paymentElementOptions = {
  layout: 'accordion',
};

const paymentElement = elements.create('payment', paymentElementOptions);
```

### Select a default network

By default, the dropdown appears without an option selected. To set a default network, specify an array of networks from most to least preferred in your [default values](https://docs.stripe.com/js/elements_object/create_payment_element#payment_element_create-options-defaultValues-card-network) when creating the Payment Element. The first network in the array that matches a network on the entered co-badged card is selected as the default. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

```javascript
const paymentElement = elements.create('payment', {
  layout: 'accordion',
  defaultValues: {
    card: {
      network: [preferredNetwork],
    },
  },
});
```

# Web Card Element

> This is a Web Card Element for when type is web-elements and ui is card-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=web-elements&ui=card-element.

The Card Element supports customer card brand choice automatically for eligible businesses whose integrations display the card icon.

- To enable card brand choice in the Combined Card Element, set [hideIcon](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options-hideIcon) to `false` or `undefined`.
- To enable card brand choice in the Split Card Element, set [showIcon](https://docs.stripe.com/js/elements_object/create_element?type=cardNumber#elements_create-options-showIcon) to `true`.
  ![The card input with a co-badged card in Card Element](assets/stripe-co-badged-card-element.png)

Card input with a co-badged card

### Card brand choice dropdown

The Card Element can’t detect the transaction currency. This means the card brand choice dropdown might display, even if the currency isn’t EUR. If the selected network can’t process the transaction because of the currency, the other card network processes the transaction instead.

### Connect platforms

Connect platforms that use the `on_behalf_of` property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify [onBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf) on the Elements group of the Card Element. This allows the Card Element to determine when to display the card brand choice dropdown.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

```javascript
const elements = stripe.elements({
  onBehalfOf: 'CONNECTED_STRIPE_ACCOUNT_ID',
});

const cardElement = elements.create('card');
```

### Card brand choice and Sources

Customer card brand choice in the Card Element is incompatible with [Sources](https://docs.stripe.com/js/deprecated/sources). The customer card brand choice dropdown might still appear if the payment is made using Sources, but we won’t honor the selected network.

### Select a default network

The card brand choice dropdown typically appears without a default option selected. To select a default network, specify an array of networks from most to least preferred using the [preferredNetwork](https://docs.stripe.com/js/elements_object/create_element?type=card#elements_create-options-preferredNetwork) option when creating the Card Element. The first network in the array that matches a network on the entered co-badged card is selected as the default. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

If you specify a value for `preferredNetwork` when creating the Card Element, you must enable icons for the card brand choice dropdown to appear. You also can’t specify [payment_method_options.card.network](https://docs.stripe.com/js/payment_intents/confirm_card_payment#stripe_confirm_card_payment-data-payment_method_options-card-network) at confirmation time.

```javascript
const cardElement = elements.create('card', {
  hideIcon: false,
  preferredNetwork: ['cartes_bancaires', 'visa', 'mastercard'],
});
```

### Interaction with the networkschange event

Previously, customer card brand choice was supported by listening to the [networkschange](https://docs.stripe.com/js/element/events/on_networkschange) event, and presenting the customer with a choice of card networks outside of the Card Element. That integration is deprecated, in favor of the Card Element card brand choice dropdown.

The `networkschange` event truncates the returned [networks](https://docs.stripe.com/js/element/events/on_networkschange?#element_on_networkschange-handler-networks) array to a single network when the Card Element is eligible for the card brand choice dropdown. Co-badged cards appear as single-network cards, preventing legacy custom integrations from presenting a redundant network selection when the Card Element handles card brand choice.

# Payment Request Button Element

> This is a Payment Request Button Element for when type is web-elements and ui is payment-request-button-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=web-elements&ui=payment-request-button-element.

The Payment Request Button supports customer card brand choice, by default, with the exception of certain Connect integration types that must pass an additional parameter.
![The Link popup with a co-badged card in the Payment Request Button](assets/stripe-co-badged-popup.png)

Payment Request Button Link popup with a co-badged card

### Connect platforms

Connect platforms that use the `on_behalf_of` property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify [onBehalfOf](https://docs.stripe.com/js/payment_request/create#stripe_payment_request-options-onBehalfOf) on the `paymentRequest`. This allows the Payment Request Button Element to determine when to display the card brand choice dropdown.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

```javascript
const paymentRequest = stripe.paymentRequest({
  country: 'US',
  currency: 'usd',
  total: {label: 'Demo total', amount: 1099},
  onBehalfOf: 'CONNECTED_STRIPE_ACCOUNT_ID',
});

const paymentRequestButtonElement = elements.create(
  'paymentRequestButton',
  {
    paymentRequest: paymentRequest,
  }
);
```

# Express Checkout Element

> This is a Express Checkout Element for when type is web-elements and ui is express-checkout-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=web-elements&ui=express-checkout-element.

The Express Checkout Element supports customer card brand choice, by default, with the exception of certain Connect integration types that must pass an additional parameter.
![The Link popup with a co-badged card in the Express Checkout Element](assets/stripe-co-badged-popup.png)

Express Checkout Element Link popup with a co-badged card

### Connect platforms

Connect platforms that use the `on_behalf_of` property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify [onBehalfOf](https://docs.stripe.com/js/elements_object/create_without_intent#stripe_elements_no_intent-options-onBehalfOf) on the Elements group of the Express Checkout Element. This allows the Express Checkout Element to determine when to display the card brand choice dropdown.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

```javascript
const elements = stripe.elements({
  onBehalfOf: 'CONNECTED_STRIPE_ACCOUNT_ID',
});

const expressCheckoutElement = elements.create('expressCheckout');
```

# Payment Sheet

> This is a Payment Sheet for when type is mobile-elements and mobile-ui is payment-sheet. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=mobile-elements&mobile-ui=payment-sheet.

The Payment Sheet supports customer card brand choice automatically. You can provide a sorted list of preferred networks in `PaymentSheet.Configuration.preferredNetworks(…)` to use if your customer doesn’t make a selection. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

> To enable card brand choice, you must use iOS SDK 23.22.1 or later on iOS, or Android SDK 20.37.4 or later on Android.

#### iOS

```swift
var configuration = PaymentSheet.Configuration()

configuration.merchantDisplayName = "Merchant Inc."
configuration.preferredNetworks = [.cartesBancaires, .visa, .mastercard]
```

#### Android

```kotlin
val configuration = PaymentSheet.Configuration.Builder(merchantDisplayName = "Merchant Inc.")
    .preferredNetworks(listOf(CardBrand.CartesBancaires, CardBrand.Visa, CardBrand.MasterCard))
    .build()
```

### Connect platforms

Connect platforms that use the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify that same value as `onBehalfOf` in the `IntentConfiguration`.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

#### iOS

```swift
var configuration = PaymentSheet.IntentConfiguration(
  mode: .payment(amount: 1099, currency: "usd"),
  onBehalfOf: "CONNECTED_STRIPE_ACCOUNT_ID"
) { [weak self] _, _ in
  // Handle intent creation....
}
```

#### Android

```kotlin
val intentConfiguration = PaymentSheet.IntentConfiguration(
    mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = 1099,
        currency = "usd",
    ),
    onBehalfOf = "CONNECTED_STRIPE_ACCOUNT_ID",
)
```

This allows the Payment Sheet to determine when to display the card brand choice dropdown.
![The card input with a co-badged card in the  Payment Sheet](assets/stripe-co-badged-mobile.png)

Card input with a co-badged card

# Payment Element

> This is a Payment Element for when type is mobile-elements and mobile-ui is payment-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=mobile-elements&mobile-ui=payment-element.

The [Payment Element](https://docs.stripe.com/payments/mobile/embedded.md) supports customer card brand choice automatically. Customers who enter a co-badged card are presented with a network selector without any additional configuration. You can provide a sorted list of preferred networks in `EmbeddedPaymentElement.Configuration.preferredNetworks` to use if your customer doesn’t make a selection. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

> To enable card brand choice, you must use iOS SDK 23.22.1 or later on iOS, or Android SDK 20.37.4 or later on Android.

#### iOS

```swift
var configuration = EmbeddedPaymentElement.Configuration()

configuration.merchantDisplayName = "Merchant Inc."
configuration.preferredNetworks = [.cartesBancaires, .visa, .mastercard]
```

#### Android

```kotlin
val configuration = EmbeddedPaymentElement.Configuration.Builder(merchantDisplayName = "Merchant Inc.")
    .preferredNetworks(listOf(CardBrand.CartesBancaires, CardBrand.Visa, CardBrand.MasterCard))
    .build()
```

### Connect platforms

Connect platforms that use the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify that same value as `onBehalfOf` in the `IntentConfiguration`.

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

#### iOS

```swift
let intentConfiguration = PaymentSheet.IntentConfiguration(
  mode: .payment(amount: 1099, currency: "usd"),
  onBehalfOf: "CONNECTED_STRIPE_ACCOUNT_ID"
) { [weak self] _, _ in
  // Handle intent creation....
}
```

#### Android

```kotlin
val intentConfiguration = PaymentSheet.IntentConfiguration(
    mode = PaymentSheet.IntentConfiguration.Mode.Payment(
        amount = 1099,
        currency = "usd",
    ),
    onBehalfOf = "CONNECTED_STRIPE_ACCOUNT_ID",
)
```

This allows the Payment Element to determine when to display the card brand choice dropdown.
![The card input with a co-badged card in the Payment Element](assets/stripe-co-badged-mobile.png)

Card input with a co-badged card

# Mobile Customer Sheet

> This is a Mobile Customer Sheet for when type is mobile-elements and mobile-ui is customer-sheet. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=mobile-elements&mobile-ui=customer-sheet.

The Customer Sheet supports customer card brand choice automatically. You can provide a sorted list of preferred networks in `CustomerSheet.Configuration.preferredNetworks(…)` to use if your customer doesn’t make a selection. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

> To enable card brand choice, you must use iOS SDK 23.22.1 or later on iOS, or Android SDK 20.37.4 or later on Android.

#### iOS

```swift
var configuration = CustomerSheet.Configuration()

configuration.merchantDisplayName = "Merchant Inc."
configuration.preferredNetworks = [.cartesBancaires, .visa, .mastercard]
```

#### Android

```kotlin
val configuration = CustomerSheet.Configuration.builder(merchantDisplayName = "Merchant Inc.")
    .preferredNetworks(listOf(CardBrand.CartesBancaires, CardBrand.Visa, CardBrand.MasterCard))
    .build()
```

This allows the Customer Sheet to determine when to display the card brand choice dropdown.
![The card input with a co-badged card in the Mobile Customer Sheet](assets/stripe-co-badged-mobile.png)

Card input with a co-badged card

# Mobile Card Element

> This is a Mobile Card Element for when type is mobile-elements and mobile-ui is card-element. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=mobile-elements&mobile-ui=card-element.

All Card Element variants support customer card brand choice automatically:

- iOS: `STPaymentCardTextField` and `STPCardFormView`
- Android: `CardInputWidget`, `CardMultilineWidget`, and `CardFormView`

The resulting `STPPaymentMethod` on iOS and `PaymentMethodCreateParams` on Android contain the customer’s selected network. You can pass these objects to your Stripe integration without any extra work on your part.

You can provide a sorted list of preferred networks in `preferredNetworks` (iOS) or `setPreferredNetworks(…)` (Android) to use if your customer doesn’t make a selection. See the [supported networks](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-card-networks-preferred) for valid values.

> To enable card brand choice, you must use iOS SDK 23.22.1 or later on iOS, or Android SDK 20.37.4 or later on Android.

### Connect platforms

Connect platforms that use the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) property with [separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) or [destination charges](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant) must also specify that same value as `onBehalfOf` on the Card Element variant.

> To enable card brand choice with `on_behalf_of`, you must use iOS SDK 23.27.1 or later on iOS, or Android SDK 20.42.0 or later on Android.

This allows the Card Element to determine when to display the card brand choice dropdown.
![The card input with a co-badged card in the Mobile Card Element](assets/stripe-co-badged-mobile.png)

Card input with a co-badged card

> In Connect integrations, the _merchant of record_ (The legal entity responsible for facilitating the sale of products to a customer that handles any applicable regulations and liabilities, including sales taxes. In a Connect integration, it can be the platform or a connected account) on a transaction is the business we use to determine if co-badged regulation applies. Depending on the Connect integration, this can either be the platform or the connected account.

## Optional: Multiprocessor

If you process payments outside of Stripe, you must pass the selected network to your payment processor:

- iOS: `STPPayment.card.networks.preferred`
- Android: `PaymentMethodCreateParams.card.networks.preferred`

# Terminal

> This is a Terminal for when type is terminal. View the full page at https://docs.stripe.com/co-badged-cards-compliance?type=terminal.

By default, [Stripe Terminal](https://stripe.com/terminal) supports customer card brand choice on the [BBPOS WisePad 3](https://stripe.com/fr/terminal/wisepad3), [Stripe Reader S700](https://stripe.com/fr/terminal/s700), and [Stripe Reader S710](https://stripe.com/fr/terminal/s710) readers. Customers who present a co-badged card on the Terminal, when applicable, can choose their option for the card brand to select.

If you use [Tap to Pay on iPhone](https://docs.stripe.com/terminal/payments/setup-reader/tap-to-pay.md?platform=ios) to accept payments on co-badged cards, your integration must facilitate [card brand choice](https://docs.stripe.com/co-badged-cards-compliance.md#integration-guides) by allowing customers to select their preferred network at any point before initiating the tap. You must also pass the relevant [requested_priority](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-card_present-routing-requested_priority) to Stripe before the customer initiates the tap.
![An application selection screen showing two card brands, one with Cartes Bancaires (CB) and the other Visa, on the WisePad 3 device.](assets/stripe-co-badged-wisepad.png)

BBPOS WisePad 3
![An application selection screen showing two card brands, one with Cartes Bancaires (CB) and the other Visa, on the Stripe Reader S700/S710 device.](assets/stripe-co-badged-s700.png)

Stripe Reader S700/S710

## Identify the processing network

The `charge` object associated with a successful payment contains a `network` field that indicates which card network processed the payment. For example, you can identify the network for a transaction using a `card` as follows:

```json
{
  "id": "ch_1Ff52K2eZvKYlo2CWe10i0s7",
  "object": "charge",
  ...
  "payment_method_details": {
    "card": {
      "brand": "visa",
      ..."network": "cartes_bancaires",
    },
    "type": "card"
  }
}
```

If you use a [Terminal](https://docs.stripe.com/terminal.md) integration, review the [specific regional requirements](https://docs.stripe.com/terminal/payments/regional.md?integration-country=FR#identify-the-network) to identify the network used.

## Testing

You can use the following co-badged cards to test your integration.

#### Card numbers

| Number              | Brand                          | CVC          | Date            |
| ------------------- | ------------------------------ | ------------ | --------------- |
| 4000 0025 0000 1001 | Cartes Bancaires or Visa       | Any 3 digits | Any future date |
| 5555 5525 0000 1001 | Cartes Bancaires or Mastercard | Any 3 digits | Any future date |

#### Tokens

| Token                            | Brand                          |
| -------------------------------- | ------------------------------ |
| `tok_visa_cartesBancaires`       | Cartes Bancaires or Visa       |
| `tok_mastercard_cartesBancaires` | Cartes Bancaires or Mastercard |

#### PaymentMethods

| Payment Method                                 | Brand                          |
| ---------------------------------------------- | ------------------------------ |
| `pm_card_visa_credit_fr_cartesBancaires`       | Cartes Bancaires or Visa       |
| `pm_card_mastercard_credit_fr_cartesBancaires` | Cartes Bancaires or Mastercard |

If you use a [Terminal](https://docs.stripe.com/terminal.md) integration, see the [simulated test cards](https://docs.stripe.com/terminal/references/testing.md#standard-test-cards) that you can use with a [simulated reader](https://docs.stripe.com/terminal/references/testing.md#simulated-reader) to verify network routing.
