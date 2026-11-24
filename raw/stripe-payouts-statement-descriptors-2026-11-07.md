<!-- Source URL: https://docs.stripe.com/payouts/statement-descriptors -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Payout statement descriptors

Understand and manage how Stripe payouts appear on a connected account's bank statements.

Stripe allows you to configure payout statement descriptors at an account or payout level. We apply a [precedence order](https://docs.stripe.com/payouts/statement-descriptors.md#precedence-order) across the payout statement descriptor configurations. Beneficiary banks don’t guarantee that they’ll display statement descriptors. Stripe shares this information with the beneficiary’s bank, but it’s up to the beneficiary bank to decide what they actually display on the bank statement.

> #### ACH payout descriptor limit
> 
> For standard US ACH payouts, the statement descriptor maps to the ACH **Company Entry Description** field, which the NACHA standard limits to 10 characters. Stripe silently truncates any descriptor longer than 10 characters before submitting to the banking partner. To ensure your descriptor appears as intended on US ACH payouts, use 10 characters or fewer.

## Account-level statement descriptors

Account-level statement descriptors allow you to configure a custom descriptor across all your auto and manual payouts. We recommend that you use this setting if you want a single statement descriptor. For example, you could display `Cactus payout` on your bank statement across all your Stripe payouts.
![Account-level Statement Descriptors](https://b.stripecdn.com/docs-statics-srv/assets/account-level-statement-descriptor.5ecb0337d82a64ea6029340302ad3366.svg)

### Dashboard 

Account-level statement descriptors are customized on your [payout settings page](https://dashboard.stripe.com/settings/payouts#payout-statement-descriptor-settings) in the Dashboard.

## Payout-level statement descriptors

Payout-level statement descriptors allow you to configure a unique descriptor for each manual payout. We recommend that you use this setting if you want a unique statement descriptor. For example, you could display `Cactus payout 001` on your bank statement across a single Stripe manual payout.
![Payout-level Statement Descriptor](https://b.stripecdn.com/docs-statics-srv/assets/payout-level-statement-descriptor.684617d20052b8834e240ada78c16c82.svg)

### Dashboard 

Payout-level statement descriptors are customized on the [balances overview page](https://dashboard.stripe.com/balance/overview) in the Dashboard when creating a manual payout.

### API 

```curl
curl https://api.stripe.com/v1/payouts \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d amount=100 \
  -d currency=usd \
  -d "statement_descriptor=Cactus Payouts 001"
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
![Payout Statement Descriptor precedence order](https://b.stripecdn.com/docs-statics-srv/assets/statement-descriptor-precedence.8530aa5db34fea4e42383aef8c9bbca1.svg)
