<!-- Source URL: https://docs.stripe.com/payments/orchestration/wallet-payments -->
<!-- Fetched: 2026-05-11 -->

# Wallet payments with Orchestration

Orchestration supports wallet payments including Apple Pay and Google Pay. You can route wallet payment methods to different processors based on your business needs, providing flexibility in how you handle digital wallet transactions.

> #### Using saved payment methods with mobile wallets
>
> When you attempt to charge a mobile wallet with a saved payment method, make sure to pass `off_session=true` during PaymentIntent confirmation. If the customer is present in your checkout flow, you can’t reuse a saved payment method. You need to instead use the [Apple Pay](https://docs.stripe.com/apple-pay.md) and [Google Pay](https://docs.stripe.com/google-pay.md) integrations to re-prompt for payment method presentment.

## Set up wallet payments

To accept Apple Pay and Google Pay with Orchestration:

1. Enable Apple Pay or Google Pay payment methods on your third-party processor. Check with your processor’s documentation for specific configuration requirements.
1. Configure Stripe to accept wallet payments:
   - Follow [Accept a payment with Google Pay](https://docs.stripe.com/google-pay.md) to set up Google Pay.
   - Follow [Accept a payment with Apple Pay](https://docs.stripe.com/apple-pay.md) to set up Apple Pay.
1. Set up test routing in Payments > Orchestration > [Rules](https://dashboard.stripe.com/orchestration/rules) to test orchestration for wallet payments.
1. Test your wallet payment routing. You can use [Payment Links](https://docs.stripe.com/payment-links.md) to quickly test your Google Pay or Apple Pay payments.
