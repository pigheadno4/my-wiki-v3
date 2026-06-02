<!-- Source URL: https://docs.stripe.com/payments/advanced/credits -->
<!-- Fetched: 2026-04-21 -->

# Redeem credits

Learn how to integrate a credits system into checkout sessions.

Credits reduce the total amount due on a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md) after tax or shipping has been applied. Use credits to apply a store credit or prepaid gift card during checkout.

Stripe doesn’t manage or keep track of credits. Pass an available credit amount into the Checkout Session to reduce the payment total during checkout.

After completion, you must retrieve session details to determine the credit amount used for reconciliation.

Allow your customers to claim credits during checkout when you integrate with [Elements and the Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md). To request access to Checkout Session Credits, enter your email address below.
