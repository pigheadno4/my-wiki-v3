<!-- Source URL: https://docs.stripe.com/payments/checkout/update-customer -->
<!-- Fetched: 2026-04-21 -->

# Update the customer during checkout

Attach a customer to a Checkout Session after creation to support mid-checkout authentication.

Attach a [Customer](https://docs.stripe.com/api/customers.md) to an existing [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) after creation, enabling their saved payment methods, email, and billing information to automatically populate without losing any information the customer has already entered. This is useful when you allow customers to begin checkout as a guest and offer the option to log in during the checkout process.
