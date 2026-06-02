<!-- Source URL: https://docs.stripe.com/secure-remote-commerce -->
<!-- Fetched: 2026-05-08 -->

# Secure Remote Commerce program guide

Accept payments using Secure Remote Commerce in your existing Stripe integration.

Use [Secure Remote Commerce (SRC)](https://www.mastercard.us/en-us/merchants/grow-your-business/find-solutions-by-need/improve-checkout/secure-digital-checkout.html) to securely pay online, and use the global payments industry to protect your payment information. Users can add cards from Visa, Mastercard, American Express, and Discover to enable Click to Pay. SRC supports all participating network brands.

> Secure Remote Commerce is only available in the US at this time.

## Integrate the Secure Remote Commerce button

> Mastercard has deprecated Masterpass. As a result, new Masterpass Checkout IDs can’t be generated in the Dashboard. We’re working to re-enable Secure Remote Commerce onboarding.

If you’re using [Visa Checkout](https://docs.stripe.com/visa-checkout.md) or [Masterpass](https://docs.stripe.com/masterpass.md) to accept payments, we recommend migrating these integrations to SRC, which provides a unified checkout process that supports a number of card brands.

To get started, generate your Masterpass **Checkout ID** in the [Dashboard](https://dashboard.stripe.com/account/payments/settings) and configure your sandbox and production callback URLs. Mastercard offers SRC as an update to their Masterpass service.

To use SRC on your website, add the following script tag to your HTML document:

#### Sandbox

```html
<script
  type="text/javascript"
  src="https://sandbox.src.mastercard.com/srci/integration/merchant.js?locale=en_us&checkoutid={checkoutId}"
></script>
```

#### Production

```html
<script
  type="text/javascript"
  src="https://src.mastercard.com/srci/integration/merchant.js?locale=en_us&checkoutid={checkoutId}"
></script>
```

| Parameter    | Description                                                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`     | The country (and language) of the business. `en_US` is the only valid value because SRC is only available to US businesses.                     |
| `checkoutid` | The Checkout ID from Mastercard, copied from the Masterpass section of the [Dashboard](https://dashboard.stripe.com/account/payments/settings). |

To display the Masterpass button with black text, use the following image:

```html
<img
  id="mpbutton"
  src="https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}"
/>
```

To display the Masterpass button with white text, use the following image:

```html
<img
  id="mpbutton"
  src="https://src.mastercard.com/assets/img/acc/global/src_mark_hor_blk.svg?locale=en_us&paymentmethod={acceptedCardBrands}&checkoutid={checkoutId}"
/>
```

| Parameter       | Description                                                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `locale`        | The country (and language) of the business. `en_US` is the only valid value because SRC is only available to US businesses.                     |
| `paymentmethod` | The list of accepted card brands, comma separated (for example: “master,amex,visa,diners,discover,jcb,maestro”).                                |
| `checkoutid`    | The Checkout ID from Mastercard, copied from the Masterpass section of the [Dashboard](https://dashboard.stripe.com/account/payments/settings). |

Attach a click handler to the image and use it to invoke the `masterpass.checkout` function with the desired parameters:

```javascript
const button = document.getElementById("mpbutton");

button.addEventListener("click", (ev) =>
  masterpass.checkout({
    checkoutId: "{{MASTERPASS_CHECKOUT_ID}}",
    allowedCardTypes: ["master", "amex", "visa"],
    amount: "10.00",
    currency: "USD",
    cartId: "{{UNIQUE_ID}}",
    callbackUrl: "{{CALLBACK_URL}}",
  }),
);
```

The `masterpass.checkout` function requires the following parameters:

| Parameter          | Description                                                                                                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `checkoutId`       | The Checkout ID for your Masterpass project, copied from the [Dashboard](https://dashboard.stripe.com/account/payments/settings). |
| `allowedCardTypes` | A list of the Masterpass-compatible payment providers that you want to support.                                                   |
| `amount`           | The amount of the transaction, expressed in decimal format.                                                                       |
| `currency`         | The currency to use for the transaction.                                                                                          |
| `cartId`           | A unique string that you generate to identify the purchase.                                                                       |
| `callbackUrl`      | Use this optional parameter to override the default `callbackUrl` configured when activating Masterpass.                          |

For more details about the `masterpass.checkout` function and the parameters that it accepts, refer to [Mastercard’s documentation](https://developer.mastercard.com/documentation/masterpass-merchant-integration-v7/7#standard-checkout1).

## Complete the payment

When the user clicks the Masterpass button on your checkout page, it takes them to the Masterpass website where they can select an existing payment method from their account or input a new one. When the user completes the process, Masterpass redirects them to the callback URL that you configured when activating Masterpass, or to the specified callback URL when invoking `masterpass.checkout` function. It appends an `oauth_verifier` URL query parameter that your application can use to complete the transaction.

In the route handler for the redirect destination, extract the URL query parameter and use it to [confirm](https://docs.stripe.com/api/payment_intents/confirm.md) the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) that you’ve created at the beginning of the checkout flow. See [accept a payment](https://docs.stripe.com/payments/accept-a-payment.md) to learn how to manage your checkout flow using Payment Intents.

The following code example demonstrates how to _confirm_ (Confirming an intent indicates that the customer intends to use the current or provided payment method. Upon confirmation, the intent attempts to initiate the portions of the flow that have real-world side effects) a PaymentIntent with SRC in Node.js with the Express framework:

```javascript
app.get("/callback", async (req, res) => {
  // retrieve the PaymentIntent ID created at the beginning of the checkout flow.
  const payment_intent_id = "{{PAYMENT_INTENT_ID}}";

  const payment_intent = await stripe.paymentIntents.confirm(
    payment_intent_id,
    {
      amount: 1000,
      currency: "usd",
      payment_method_data: {
        type: "card",
        card: {
          masterpass: {
            cart_id: "{{UNIQUE_ID}}",
            transaction_id: req.query.oauth_verifier,
          },
        },
      },
    },
  );

  res.send("<h1>Charge succeeded</h1>");
});
```

## Test Secure Remote Commerce

To test your SRC integration against Mastercard’s sandbox, create a new SRC user account during the checkout process on your website. Configure the account to use one of the [test cards](https://developer.mastercard.com/masterpass/documentation/migration/masterpass_to_src_migration/#mastercard-test-cards) from the Masterpass documentation. Complete the checkout process as normal, selecting the test card as your payment method. If everything works correctly, Mastercard redirects you back to your application, which creates the charge as expected.

The SRC integration only works correctly when included on an `http` or `https` page. Stripe doesn’t support serving from the filesystem, even during testing.
