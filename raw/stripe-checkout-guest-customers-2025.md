<!-- Source: Stripe Checkout — Guest customers -->
<!-- Fetched: 2026-04-20 -->

# Guest customers

Learn how to track the activity of guest customers.

The [Customer object](https://docs.stripe.com/api/customers.md) represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with guest customers instead. Stripe automatically groups [guest customers in the Dashboard](https://dashboard.stripe.com/customers?type=guest) based on them having used the same card, email, or phone to make payments. This unified view helps you review purchasing behavior, refunds, chargebacks, or fraud.

Guest customers are a read-only grouping for completed transactions. Stripe doesn’t save payment methods for guest customers, so you can’t initiate new charges against them. To save payment details for future use, create a [Customer](https://docs.stripe.com/api/customers.md) and [save their payment method](https://docs.stripe.com/payments/save-customer-payment-methods.md).

Checkout supports passing in a [customer](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer) to enable you to [prefill customer information](https://docs.stripe.com/payments/existing-customers.md?platform=web&ui=stripe-hosted) on the Checkout page and to associate the payment or subscription with a specific customer.

If you don’t pass in a `customer`, you can set [customer_creation](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-customer_creation) to configure whether or not Checkout automatically creates a Customer object when the session is confirmed.

## Managing and monitoring guest customers

Even though you can’t manage or monitor guest customers in the same way as with Checkout Sessions that create Customers, you can still manage them and monitor their activity.

### Grouping payments under guest customers

We use credit card number as the unique identifier to group credit card payments of your guest customers under the same guest identity. See the [guest customer support page](https://support.stripe.com/questions/guest-customer-faq) for additional details on the matching logic. If the same credit card was used by different guest customers (for example, two spouses using the same credit card to checkout at different times), all guest payments for that credit card show up together under one guest customer. Because we group by credit card, we consider it the same guest customer.

### Updating your privacy policy or other privacy notices

You’re in the best position to know whether this feature is consistent with your privacy policy or other privacy notices. It’s a good practice to review your privacy notices and privacy policy when considering any new feature. Guest customers give you a view of your existing guest data, which can help you better detect fraud and help you manage customer service inquiries.

### Exporting guest customer data from the Dashboard

You can export guest customer data from the [Customers](https://dashboard.stripe.com/customers) tab in the Dashboard. Guest customer information isn’t included in exports from the [Payments](https://dashboard.stripe.com/payments) tab.

### Not seeing any guest customers in the Guests tab

If you don’t see any guest customers under the **Guests** tab, this is because your Stripe integration is passing a Customer ID when creating Checkout Sessions. We only create guest customers for payments without a specific Customer object associated with them.
