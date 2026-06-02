<!-- Source URL: https://docs.stripe.com/payouts/statement-descriptors -->
<!-- Fetched: 2026-05-11 -->

# Payout statement descriptors

Understand and manage how Stripe payouts appear on a connected account's bank statements.

Stripe allows you to configure payout statement descriptors at an account or payout level. We apply a [precedence order](https://docs.stripe.com/payouts/statement-descriptors.md#precedence-order) across the payout statement descriptor configurations.

> #### Banks don't always display statement descriptors
>
> Beneficiary banks don’t guarantee that they’ll display statement descriptors. While Stripe shares this information with the beneficiary’s bank, it’s up to the beneficiary bank to decide what they actually display on the bank statement.

## Account-level statement descriptors

Account-level statement descriptors allow you to configure a custom descriptor across all your auto and manual payouts. We recommend that you use this setting if you want a single statement descriptor. For example, you could display `Cactus payout` on your bank statement across all your Stripe payouts.
![Account-level Statement Descriptors](assets/stripe-payouts-account-level-descriptor.svg)

### Dashboard

Account-level statement descriptors are customized on your [payout settings page](https://dashboard.stripe.com/settings/payouts#payout-statement-descriptor-settings) in the Dashboard.

## Payout-level statement descriptors

Payout-level statement descriptors allow you to configure a unique descriptor for each manual payout. We recommend that you use this setting if you want a unique statement descriptor. For example, you could display `Cactus payout 001` on your bank statement across a single Stripe manual payout.
![Payout-level Statement Descriptor](assets/stripe-payouts-payout-level-descriptor.svg)

### Dashboard

Payout-level statement descriptors are customized on the [balances overview page](https://dashboard.stripe.com/balance/overview) in the Dashboard when creating a manual payout.

### API

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const payout = await stripe.payouts.create({
  amount: 100,
  currency: "usd",
  statement_descriptor: "Cactus Payouts 001",
});
```

#### Json

```json
{
  "id": "po_1OaFDbEcg9tTZuTgNYmX0PKB",
  "object": "payout",
  "amount": 1100,
  "currency": "usd",
  ...
  "statement_descriptor": "Cactus Payouts 001",
  "status": "pending",
  "type": "bank_account"
}
```

## Precedence Order

If you don’t define an account-level or payout-level statement descriptor, we default to ‘STRIPE’ as the descriptor shown on your bank statement.
![Payout Statement Descriptor precedence order](assets/stripe-payouts-descriptor-precedence.svg)
