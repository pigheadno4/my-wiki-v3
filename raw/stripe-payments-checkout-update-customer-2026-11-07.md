<!-- Source URL: https://docs.stripe.com/payments/checkout/update-customer -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Update the customer during checkout

Attach a customer to a Checkout Session after creation to support mid-checkout authentication.

Attach a [Customer](https://docs.stripe.com/api/customers.md) to an existing [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md) after creation, enabling their saved payment methods, email, and billing information to automatically populate without losing any information the customer has already entered. Use this when you allow customers to begin checkout as a guest and then offer the option to log in during the checkout process.

### Interested in updating the customer during checkout?

To request access to this preview feature, enter your email below and a member of our team will contact you.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/checkout/update-customer" \
  -d '{"email": "EMAIL", "preview": "custom_checkout_preview"}'
```
