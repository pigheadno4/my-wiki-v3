<!-- Source URL: https://docs.stripe.com/payments/advanced/credits -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Redeem credits

Learn how to integrate a credits system into checkout sessions.

Credits reduce the total amount due on a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md) after tax or shipping has been applied. Use credits to apply a store credit or prepaid gift card during checkout.

Stripe doesn’t manage or keep track of credits. Pass an available credit amount into the Checkout Session to reduce the payment total during checkout.

After completion, you must retrieve session details to determine the credit amount used for reconciliation.

### Checkout session credits

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/advanced/credits" \
  -d '{"email": "EMAIL", "preview": "checkout_credits_preview"}'
```
