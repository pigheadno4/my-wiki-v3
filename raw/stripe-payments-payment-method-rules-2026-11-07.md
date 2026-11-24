<!-- Source URL: https://docs.stripe.com/payments/payment-method-rules -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Payment method rules

Control when payment methods are available to your customers.

Payment method rules allow you to set conditions on non-card payment methods directly from the Dashboard without any custom logic or code. Rules allow you to:

- Hide or show a payment method if the order amount is over or under a certain amount.
  - **Example**: Show only Affirm transactions over 1,000 USD to encourage higher-value purchases.
- Hide or show a payment method for customers in certain countries or using certain currencies.
  - **Example**: Hide iDEAL for customers outside the Netherlands, where it’s not commonly used.

> Payment method rules only apply to non-card payment methods. Card payments and wallet payment methods, such as Apple Pay and Google Pay, aren’t currently supported.

## Payment method rules considerations

Non-card payment methods can help offer improved unit economics compared to cards and they often drive higher AOV and conversion rates.

When you turn on these payment methods, you might want to apply specific business logic to control when payment methods are available to your customers. With payment method rules, you can apply these insights directly in Dashboard—no code required.

Payment method rules are compatible with Stripe [A/B Testing](https://docs.stripe.com/payments/a-b-testing.md). This allows you to run A/B tests using the targeting criteria you select or test additional criteria. For example, you can test the impact of only showing a specific payment method when the price is greater than a certain dollar amount.

> Payment method rules don’t apply to the [hosted invoice page](https://docs.stripe.com/invoicing/hosted-invoice-page.md) or when a Payment Element, Express Checkout Element, Checkout, or Payment Links integration creates a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis). For more information about subscriptions and invoices, see [How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview.md).

## Before you begin

- You must use either the Stripe [Payment Element](https://docs.stripe.com/payments/payment-element.md), [Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Payment Links](https://docs.stripe.com/payment-links.md).
- You must use [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) to enable additional payment methods from the Stripe Dashboard, which won’t require any code changes.
  - To set up dynamic payment methods for direct users, see the [payment method integration](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) guide.
  - (Connect) To set up dynamic payment methods for Connect platforms, see [Manage payment methods for connected accounts](https://docs.stripe.com/connect/manage-payment-methods.md).

## Set rule conditions

1. In the Dashboard, go to [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods/default).

2. (Connect) If you’re a Connect platform, configure payment method rules in your [template config](https://dashboard.stripe.com/test/settings/payment_methods/connected_accounts), not in your direct payment methods settings.

   **Direct charges**: Rules you set in your template config are inherited by all connected accounts. Connected accounts can’t override these rules.

   **Destination charges**: Rules you set in your direct payment methods settings apply to destination charges. Your connected accounts’ rules don’t affect destination charges.

   For more information about charge types, see [Direct charges](https://docs.stripe.com/connect/charges.md) and [Destination charges](https://docs.stripe.com/connect/destination-charges.md).

3. For a supported payment method (such as Klarna), click the overflow menu (⋯) and select **Customize availability**.

4. Set custom rules (for example, a new minimum of 100 USD for Klarna), then select **Apply Overrides**.

> In your Dashboard, you configure transaction limits in a single currency. When evaluating these limits in a transaction that uses a different currency, Stripe automatically calculates the equivalent limits using the current exchange rate.
![A checkout page showing Klarna.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-present.fab9fed6ec4dfc1e187b38beb944fc65.png)

Before
![A checkout page with Klarna hidden.](https://b.stripecdn.com/docs-statics-srv/assets/pmt-checkout-klarna-hidden.e1d585ab6318861be8aa813cdde91fb4.png)

After

## Testing

To test location-based payment method rules for Checkout and Payment Links, pass in a location-formatted customer email that includes a suffix in a `+location_XX` format in the local part of the email. `XX` must be a valid [two-letter ISO country code](https://www.nationsonline.org/oneworld/country_code_list.htm).

For example, to test location-based rules for a customer in France, pass in an email like `test+location_FR@example.com`.

When you visit the URL for a Checkout Session or Payment Link created with a location-formatted email, you see the same available payment methods as a customer does in the specified country.

### Testing Checkout

When you create a Checkout Session, pass the location-formatted email as [customer_email](https://docs.stripe.com/api/checkout/sessions/object.md#checkout_session_object-customer_email) to simulate Checkout from a particular country.

```curl
curl https://api.stripe.com/v1/checkout/sessions \
  -u <<YOUR_SECRET_KEY>>: \
  -d "line_items[0][price]"="{{PRICE_ID}}" \
  -d "line_items[0][quantity]"=1 \
  -d mode=payment \
  -d success_url="https://example.com/success" \
  --data-urlencode customer_email="test+location_FR@example.com"
```

You can also create a [Customer](https://docs.stripe.com/api/customers/create.md) and specify their email that contains the `+location_XX` suffix. Stripe [test cards](https://docs.stripe.com/testing.md#cards) work as usual.

### Testing Payment Links

For Payment Links, pass the location-formatted email as either the `prefilled_email` or `locked_prefilled_email` [URL parameter](https://docs.stripe.com/payment-links/customize.md#customize-checkout-with-url-parameters) to test payment method rules for customers in different countries.
