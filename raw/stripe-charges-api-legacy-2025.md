<!-- Source URL: https://docs.stripe.com/payments/charges-api -->
<!-- Fetched: 2026-04-20 -->

# Card payments on the Charges API

Learn how to charge, save, and authenticate cards with Stripe's legacy APIs.

> #### Legacy API
>
> The content of this section refers to a _Legacy_ (Technology that's no longer recommended) feature. Use the [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment.md) instead.
>
> The Charges API doesn’t support the following features, many of which are required for credit card compliance:
>
> - Businesses in India

- [Bank requests for card authentication](https://docs.stripe.com/payments/cards/overview.md)
- [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication.md)

The [Charges](https://docs.stripe.com/api/charges.md) and [Tokens](https://docs.stripe.com/api/tokens.md) APIs are legacy APIs used in older Stripe integrations to accept debit and credit card payments. Use [PaymentIntents](https://docs.stripe.com/payments/accept-a-payment.md) for new integrations.

The Charges API limits your ability to take advantage of Stripe features. To get the latest features, use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) or [migrate to the Payment Intents API](https://docs.stripe.com/payments/payment-intents/migration.md).

## Payment flow

In most cases, the PaymentIntents API offers more flexibility and integration options.

| Charges API | Payment Intents API |
| ----------- | ------------------- |

| 1. Collect the customer’s payment information in the browser with Elements.

1. Tokenize the payment information with Stripe.js.
1. Perform a request to send the token to your server.
1. Use the token to create a charge on your server with the desired amount and currency.
1. Fulfill the customer’s order if payment is successful. | 1. Create a PaymentIntent on your server with the desired amount and currency.
1. Send the PaymentIntent’s client secret to the client side.
1. Collect the customer’s payment information in the browser with Elements.
1. Use Stripe.js or the mobile SDKs to handle [3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#three-ds-radar) and complete the payment on the client.
1. Use webhooks to fulfill the customer’s order if the payment is successful. |

## Refunds

To refund a payment through the API, create a [Refund](https://docs.stripe.com/api.md#create_refund) and provide the ID of the charge to be refunded.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const refund = await stripe.refunds.create({
  charge: "{{CHARGE_ID}}",
});
```

To refund part of a payment, provide an `amount` parameter, as an integer in cents (or the charge currency’s smallest currency unit).

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const refund = await stripe.refunds.create({
  charge: "{{CHARGE_ID}}",
  amount: 1000,
});
```

## Apple Pay

When your customer approves the payment, your app receives a [PKPayment](https://developer.apple.com/documentation/passkit/pkpayment) instance containing their encrypted card details by implementing the [PKPaymentAuthorizationViewControllerDelegate](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate) methods.

1. Use the [createTokenWithPayment](<https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createTokenWithPayment:completion:>) SDK method to turn the `PKPayment` into a Stripe `Token`
1. Use this `Token` to create a charge.

#### Swift

```swift
extension CheckoutViewController: PKPaymentAuthorizationViewControllerDelegate {

    func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, handler: @escaping (PKPaymentAuthorizationResult) -> Void) {
        // Convert the PKPayment into a Token
        STPAPIClient.shared.createToken(withPayment: payment) { token, error in
              guard let token = token else {
                  // Handle the error
                  return
              }
            let tokenID = token.tokenId
            // Send the token identifier to your server to create a Charge...
            // If the server responds successfully, set self.paymentSucceeded to YES
        }
    }

    func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController) {
        // Dismiss payment authorization view controller
        dismiss(animated: true, completion: {
            if (self.paymentSucceeded) {
                // Show a receipt page...
            } else {
                // Present error to customer...
            }
        })
    }
}
```

## Dynamic statement descriptor

By default, your Stripe account’s [statement descriptor](https://docs.stripe.com/get-started/account/set-up.md#public-business-information) appears on customer statements whenever you charge their card. Additionally, you can set the statement descriptor dynamically on every charge request with the `statement_descriptor` argument on the Charge object.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Token is created using Checkout or Elements!
// Get the payment token ID submitted by the form:
const token = request.body.stripeToken; // Using Express

const charge = await stripe.charges.create({
  amount: 999,
  currency: "usd",
  description: "Example charge",
  source: token,
  statement_descriptor: "Custom descriptor",
});
```

Statement descriptors are limited to 22 characters, can’t use the special characters `<`, `>`, `'`, `"`, or `*`, and must not consist solely of numbers.

When setting the statement descriptor dynamically on credit and debit card charges, the dynamic portion is appended to the settlement merchant’s statement descriptor (separated by an `*` and an empty space). For example, a statement descriptor for a business, named FreeCookies, that includes the kind of cookie purchased might look like `FREECOOKIES* SUGAR`.

The `*` and empty space count towards the 22 character limit and Stripe automatically allots 10 characters for the dynamic statement descriptor. This means that the settlement merchant’s descriptor might be truncated if it’s longer than 10 characters (assuming the dynamic statement descriptor is also greater than 10 characters). If the dynamic statement descriptor is also greater than 10 characters, both descriptors are truncated at 10 characters.

If you’re having issues with the character limits, you can set a [shortened descriptor](https://dashboard.stripe.com/settings/public) in the Stripe Dashboard to shorten the settlement merchant’s descriptor. This allows more room for the dynamic statement descriptor. The shortened descriptor:

- Replaces the settlement merchant’s statement descriptor when using dynamic descriptors.
- Can be between 2 and 10 characters.

> If your account’s statement descriptor is longer than 10 characters, set a [shortened descriptor](https://dashboard.stripe.com/settings/public) in the Dashboard or use `statement_descriptor_prefix`. This prevents your statement descriptor from being truncated in unpredictable ways.

If you’re not sure what the statement descriptors look like when they’re combined, you can check them in the [Stripe Dashboard](https://dashboard.stripe.com/settings/public).

## Storing information in metadata

If using the [Payment Intents API](https://docs.stripe.com/payments/accept-a-payment.md), only retrieve and update the `metadata` and `description` fields on the Payment Intent object. If using both the Payment Intent and Charge objects, you’re not guaranteed to see consistent values for these fields.

Stripe supports adding [metadata](https://docs.stripe.com/api.md#metadata) to the most common requests you make, such as processing charges. Metadata isn’t shown to customers or factored into whether or not a charge is declined or blocked by our fraud prevention system.

Through metadata, you can associate other information—meaningful to you—with Stripe activity. Any metadata you include is viewable in the Dashboard (for example, when looking at the page for an individual charge), and is also available in common reports and exports. As an example, your store’s order ID can be attached to the charge used to pay for that order. Doing so allows you, your accountant, or your finance team to easily reconcile charges in Stripe to orders in your system.

If you’re using _Radar_ (Stripe Radar helps detect and block fraud for any type of business using machine learning that trains on data across millions of global companies. It’s built into Stripe and requires no additional setup to get started), consider passing any additional customer information and order information as metadata. By doing so, you can write [Radar rules using metadata attributes](https://docs.stripe.com/radar/rules/reference.md#metadata-attributes) and have more information about the payment available within the Dashboard which can expedite your review process.

#### Node.js

```javascript
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

// Token is created using Checkout or Elements!
// Get the payment token ID submitted by the form:
const token = request.body.stripeToken; // Using Express

const charge = await stripe.charges.create({
  amount: 999,
  currency: "usd",
  description: "Example charge",
  source: token,
  metadata: { order_id: "6735" },
});
```

> Don’t store any sensitive information (personally identifiable information, card details, and so on) as metadata or in the charge’s `description` parameter.

## Declines

If you want your integration to respond to payment failures automatically, you can access a charge’s `outcome` in two ways.

- [Handle the API error](https://docs.stripe.com/api.md#error_handling) that’s returned when a payment fails. For blocked and card issuer-declined payments, the error includes the charge’s ID, which you can then use to [retrieve](https://docs.stripe.com/api.md#retrieve_charge) the charge.
- Use [webhooks](https://docs.stripe.com/webhooks.md) to monitor status updates. For example, the `charge.failed` event triggers when a payment is unsuccessful.
