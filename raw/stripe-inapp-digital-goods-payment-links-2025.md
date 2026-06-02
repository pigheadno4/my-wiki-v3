<!-- Source URL: https://docs.stripe.com/mobile/digital-goods/payment-links -->
<!-- Fetched: 2026-04-22 -->

# Accept payments for digital goods on iOS using Payment Links

Link out to a Stripe-hosted payment page from your app to sell digital goods or subscriptions.

For digital products, content, and subscriptions sold in the United States or European Economic Area (EEA), your iOS app can accept Apple Pay using [Payment Links](https://docs.stripe.com/payment-links.md).

In other regions, your app can’t accept Apple Pay for digital products, content, or subscriptions.

This guide describes how to sell digital goods and services in your app using Payment Links to redirect your customers to a Stripe-hosted payment page.

Use Payment Links when you have a limited number of products and prices and don’t want to run a server. Use [Stripe Checkout](https://docs.stripe.com/mobile/digital-goods/checkout.md) or [Elements](https://docs.stripe.com/mobile/digital-goods/custom-checkout.md) for a more dynamic cart or to attach a `Customer` to the `Checkout Session`.

This guide only describes the process for selling in-app digital goods. If you sell any of the following, use the [native iOS payment guide](https://docs.stripe.com/payments/mobile.md) instead:

- Physical items
- Goods and services intended for consumption outside your app
- Real-time person-to-person services

## What you’ll build

This guide shows you how to:

- Model your digital goods or subscriptions with _Products_ (Products represent what your business sells—whether that's a good or a service) and _Prices_ (Prices define how much and how often to charge for products. This includes how much the product costs, what currency to use, and the interval if the price is for subscriptions).
- Create a payment link from the Dashboard.
- Use _universal links_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) to redirect directly to your app from the payment link.
- Monitor _webhooks_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to update your customer’s in-app subscriptions.

## What isn’t covered

This guide demonstrates how to add payment links alongside your existing in-app purchase system. It doesn’t cover:

- User authentication. If you don’t have an existing authentication provider, you can use a third-party provider, such as [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) or [Firebase Authentication](https://firebase.google.com/docs/auth).
- Native in-app purchases. To implement in-app purchases using StoreKit, visit [Apple’s in-app purchase guide](https://developer.apple.com/in-app-purchase/).

## Set up universal links [Client-side] [Server-side]

_Universal links_ (Use Universal links on iOS and macOS to link directly to in-app content. They're standard HTTPS links, so the same URL works for your website and your app) allow payment links to deep link into your app after a successful payment. To configure a universal link:

1. Add an `apple-app-site-association` file to your domain.
1. Add an Associated Domains entitlement to your app.
1. Add a fallback page for your Checkout redirect URLs.

#### Define the associated domains

Add a file to your domain at `.well-known/apple-app-site-association` to define the URLs your app handles. Prepend your App ID with your Team ID, which you can find on the [Membership page of the Apple Developer Portal](https://developer.apple.com/account).

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appIDs": [
          "A28BC3DEF9.com.example.MyApp1",
          "A28BC3DEF9.com.example.MyApp1-Debug"
        ],
        "components": [
          {
            "/": "/checkout_redirect*",
            "comment": "Matches any URL whose path starts with /checkout_redirect"
          }
        ]
      }
    ]
  }
}
```

> You must serve the file with MIME type `application/json`. Use `curl -I` to confirm the content type.
>
> ```bash
> curl -I https://example.com/.well-known/apple-app-site-association
> ```

```

See Apple’s page on [supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) for more details.

#### Add an Associated Domains entitlement to your app

1. Open the **Signing & Capabilities** pane of your app’s target.
1. Click **+ Capability**, then select **Associated Domains**.
1. Add an entry for `applinks:example.com` to the Associated Domains list.

For more information on universal links, see Apple’s [universal links](https://developer.apple.com/ios/universal-links/) documentation.

Although iOS intercepts links to the URLs defined in your `apple-app-site-association` file, you might encounter situations where the redirect fails to open your app.

## Create a payment link for your product or subscription

#### One-time product

1. In the Dashboard, open the [Payment Links](https://dashboard.stripe.com/payment-links) page and click **+New** (or click the plus sign (+) and select **Payment link**).
1. (Optional) Let your customer pay what they want (for example, to decide how many credits to buy), by selecting **Customers choose what to pay**.
1. Select an existing product or click **+Add a new product**.
1. If you’re adding a new product, fill out the product details and click **Add product**.
1. Navigate **After payment** and select **Don’t show confirmation page**.
1. Set a [universal link](https://developer.apple.com/ios/universal-links/) as your success URL to direct your customer to your app after they complete the payment.
1. Click **Create Link**

#### Subscription

1. In the Dashboard, open the [Payment Links](https://docs.stripe.com/payment-links/create.md) page and click **+New** (or click the plus sign (+) and select **Payment link**).
1. Select an existing product or click **+Add a new product**.
1. If you’re adding a new product, fill out the product details and click **Add product**.
1. Navigate to the **After payment** tab and select **Don’t show confirmation page**.
1. Set a [universal link](https://developer.apple.com/ios/universal-links/) as your success URL to direct your customer to your app after they complete the payment.
1. Click **Create Link**

Payment Links support card payments and Apple Pay by default. You can enable additional payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

## Use URL parameters to attach relevant information

[URL parameters](https://docs.stripe.com/payment-links/customize.md#customize-checkout-with-url-parameters) allow you to add additional context to your payment page and streamline checkout. You can use URL parameters to adjust the language of the payment page, prefill an email or promotion code, or attach relevant metadata to help with reconciliation.

We recommend using `prefilled_email` (or `locked_prefilled_email`) and `client_reference_id` to help streamline checkout and help with your reconciliation.

| Parameter                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Syntax                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `prefilled_email`        | Use `prefilled_email` to enter an email address on the payment page automatically. Your customer can still edit this field, so the email you pass in for checkout might not be the same email that your customer uses to complete the payment.                                                                                                                                                                                                                                            | `prefilled_email` must be a valid email address. Invalid values are disregarded and your payment page continues to work as expected.

  We recommend [encoding](https://en.wikipedia.org/wiki/Percent-encoding) email addresses that you attach as URL parameters to reduce the risk of them not being passed through to your payment page.                                                                                                                      |
| `locked_prefilled_email` | Use `locked_prefilled_email` to enter an uneditable email address on the payment page automatically.                                                                                                                                                                                                                                                                                                                                                                                      | `locked_prefilled_email` must be a valid email address. Invalid values are disregarded and your payment page continues to work as expected. If both `prefilled_email` and `locked_prefilled_email` are passed, `locked_prefilled_email` takes precedence.

  We recommend [encoding](https://en.wikipedia.org/wiki/Percent-encoding) email addresses that you attach as URL parameters to reduce the risk of them not being passed through to your payment page. |
| `client_reference_id`    | Use `client_reference_id` to attach a unique string of your choice to the Checkout Session. This can be an App ID or a cart ID (or similar), and you can use it to reconcile the Session with your internal systems. This value isn’t shown to the customer during checkout, but is sent in the [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) [webhook](https://docs.stripe.com/webhooks.md) after payment completion. | `client_reference_id` can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are disregarded and your payment page continues to work as expected.                                                                                                                                                                                                                                             |

The following is an example link with `prefilled_email` and `client_reference_id`:

`https://buy.stripe.com/test_eVa3do41l4Ye6KkcMN?prefilled_email=jenny%40example.com&client_reference_id=id_123`

## Add the link to your app

Add a checkout button to your app. This button:

- Prefills your payment link with `prefilled_email` and `client_reference_id`.
- Opens the Stripe-hosted payment page in Safari.

## Handle order fulfillment [Server-side]

After the purchase succeeds, Stripe sends you a `checkout.session.completed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). In the payload of the webhook event, you’ll find the `client_reference_id` under the `checkout.session object`, which you can use for your business logic, such as associating the payment with a specific order or user in your system.

To test your integration, you can monitor events in the [Dashboard](https://dashboard.stripe.com/events) or using the [Stripe CLI](https://docs.stripe.com/webhooks.md#test-webhook). For production, set up a webhook endpoint and subscribe to appropriate event types. If you don’t know your `STRIPE_WEBHOOK_SECRET` key, click the [webhook](https://dashboard.stripe.com/webhooks) in the Dashboard to view it.

### Testing

To test your that your checkout button works, do the following:

1. Click the checkout button, which redirects you to the Stripe Checkout payment form.
1. Enter the test number 4242 4242 4242 4242, a three-digit CVC, a future expiration date, and any valid postal code.
1. Tap **Pay**.
1. The `checkout.session.completed` webhook fires, and Stripe notifies your server about the transaction. You’re redirected back to your app.

## Optional: In-app purchases with Lemon Squeezy

Accept payments with Lemon Squeezy, which can handle many business functions (for example, tax and disputes) on your behalf. Learn more about [how to use Lemon Squeezy](https://docs.lemonsqueezy.com/guides/tutorials/in-app-purchases) as your merchant of record for in-app purchases.

## See also

- [Add discounts](https://docs.stripe.com/payments/checkout/discounts.md)
- [Collect taxes](https://docs.stripe.com/payments/checkout/taxes.md)
```
