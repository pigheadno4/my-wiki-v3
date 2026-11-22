<!-- Source URL: https://docs.stripe.com/payments/link/stablecoins -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Stablecoins on Link

Learn about Stablecoins, now offered on Link.
Available in: US
Stablecoin payments on Link allow you to accept *stablecoins* (A cryptocurrency pegged to a fiat currency or other asset to limit volatility. Stripe supports OUSD and USDC for stablecoin balances, although transfers on the Tempo network use USDC.e) from customers in supported countries. Customers can pay with their preferred crypto wallet, token and payment network, while completed stablecoin payments settle in your Stripe balance in USD.

Link guarantees the funds, meaning no changes are required to your existing integration.

### Interested in learning more about stablecoins on Link?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/link/stablecoins" \
  -d '{"email": "EMAIL", "preview": "link_lpm_interest_preview"}'
```

## Get started

Stripe automatically enables stablecoin payments when you activate [Link](https://docs.stripe.com/payments/link.md).

> Only [Payment Links](https://docs.stripe.com/payment-links.md), [Stripe Checkout](https://docs.stripe.com/checkout/quickstart.md) and [Elements](https://docs.stripe.com/payments/advanced.md) support stablecoins on Link. Link doesn’t offer stablecoins in other payment flows.

Stablecoins in Link are currently supported for:

- One-time and on-session payments
- Payments presented in USD
- Transaction amounts from 1 USD to 10,000 USD
- Eligible US businesses, subject to onboarding and restricted-business exclusions

### Testing

Stablecoin payments use blockchain testnets to execute transactions. You need a wallet with testnet funds to test the stablecoins flow on Link. Learn how to [test your integration](https://docs.stripe.com/payments/accept-stablecoin-payments.md?#test-your-integration).

### New Link customers

The following describes how a new customer checks out with Stablecoins on Link:

1. The customer selects **Crypto**, then fills out their details.
2. They click **Continue with Crypto** and we redirect them to the Stripe Crypto payments page.
3. They select a wallet to authorize the payment.
4. They authorize Stripe to interact with their wallet.
5. They confirm the details of the payment.
6. They confirm the payment using their wallet.
7. Stripe confirms that the payment succeeded.

Because these are Link transactions, customers automatically sign up to Link. This safely stores their customer data, allowing for faster checkouts in the future.

### Returning Link customers

The following is what a returning customer sees when they check out with Stablecoins on Link, with their wallet details already saved:

1. Customer selects their saved stablecoin wallet, then clicks **Continue with Crypto**.
2. Customer is redirected and their wallet details are prefilled. The customer confirms the payment’s details.
3. Customer confirms the payment using their wallet.
4. Stripe confirms that the payment succeeded.

### Refunds and Disputes

You can issue refunds in the same way as any other transaction. For stablecoin payments, the refund returns to the customer’s original wallet as stablecoins.

Stablecoin payments don’t support disputes.

## See also

- [Link payment methods](https://docs.stripe.com/payments/link/link-payment-methods.md)
- [Link in different payment integrations](https://docs.stripe.com/payments/link/link-payment-integrations.md)
- [Pricing for Link](https://stripe.com/pricing/local-payment-methods#link)
