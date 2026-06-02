<!-- Source URL: https://docs.stripe.com/payouts/instant-payouts-advance-funding -->
<!-- Fetched: 2026-05-11 -->

# Instant Payouts with advance funding

Let Instant Payouts access pending balances with trackable balance activities.

Instant payout users benefit from quick access to their pending balances. To use these funds safely, explicit actions like advance funding are necessary for accurate bookkeeping when fund availability changes.

## How Instant Payouts with advance funding works

Stripe enables Instant Payouts users to access pending balances through the `advance` and `advance_funding` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transactions. When you create an instant payout that exceeds your available balance, funds are added to your available balance and subtracted from your pending balance to cover the difference.

### Advance funding alignment

To align advance funding with the original availability of payments, Stripe creates multiple `advance_funding` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transactions when it pulls funds from multiple days worth of payments balances.

For example, if you have the following:

- 0 USD in your available balance today
- 25 USD available on tomorrow (T+1)
- 15 USD available on the day after (T+2)

When you request a 40 USD instant payout, you’ll see two separate `advance_funding` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transactions:

- One that deducts 25 USD from your T+1 balance
- One that deducts 15 USD from your T+2 balance
- And one `advance` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transaction that credits 40 USD to your available balance

### Reversal of failed or canceled Instant Payouts

When an instant payout fails or gets canceled, the corresponding `advance` and `advance_funding` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transactions are reversed by offsetting balance transactions. In the example above, if the 40 USD instant payout fails, we:

- Credits 25 USD to your T+1 balance
- Credits 15 USD to your T+2 balance
- Deducts 40 USD from your available balance

### Negative available balance recovery

When your available balance is negative, advance funding doesn’t restore it. Instead, it only provides funding for the requested instant payout amount, leaving your negative available balance unchanged. We’ll choose the appropriate pending balances to allow your negative available balance to phase out gradually. This funding is drawn from future days where the cumulative balance is positive. For example:

- -25 USD in your available balance today (available balance)
- 20 USD available tomorrow (T+1)
- 30 USD available the day after (T+2)

In this scenario, the cumulative balance on T+1 is -5 USD, while T+2 shows a cumulative balance of 25 USD. If you request a 10 USD instant payout, we:

- Deduct 10 USD from your T+2 balance
- Credit 10 USD to your available balances for the Instant Payouts

This method retains more recent pending balances, aiding recovery from a negative balance. The cumulative balance recovers on T+2.

## Filter balance transactions by source

Use the `source` field to find the `advance` and `advance_funding` [type](https://docs.stripe.com/reports/balance-transaction-types.md) balance transactions for the Instant Payout. You can access the `source` field in the Dashboard when you filter transactions or through the [Balance Transactions API](https://docs.stripe.com/api/balance_transactions.md).

#### Dashboard

1. Go to the **Balances > All activity** page.
1. Click the **Export** button and select a time range.
1. Open the downloaded balance history CSV file.
1. Locate the **source** column in the export file.
1. The related `advance` and `advance_funding` balance transactions will have a `source` field that matches the instant payout token.

#### API

In this example, you created an instant payout at May 8, 2024 at 10:02 PM UTC and call the Balance Transaction API to list the linked balance transactions.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const balanceTransactions = await stripe.balanceTransactions.list({
  source: "po_123",
});
```

```json
{
  "object": "list",
  "data": [
    {
      "id": "txn_123",
      "object": "balance_transaction",
      "amount": -1500,
      "available_on": 1715299200, // 2024-05-10 00:00:00 UTC
      "created": 1715205760, // 2024-05-08 22:02:40 UTC
      "currency": "usd",
      "description": "Deducting pending funds for po_123",
      "exchange_rate": null,
      "fee": 0,
      "fee_details": [],
      "net": -1500,
      "reporting_category": "advance_funding",
      "source": "po_123",
      "status": "pending",
      "type": "advance_funding"
    }
    {
      "id": "txn_234",
      "object": "balance_transaction",
      "amount": -2500,
      "available_on": 1715212800, // 2024-05-09 00:00:00 UTC
      "created": 1715205760, // 2024-05-08 22:02:40 UTC
      "currency": "usd",
      "description": "Deducting pending funds for po_123",
      "exchange_rate": null,
      "fee": 0,
      "fee_details": [],
      "net": -2500,
      "reporting_category": "advance_funding",
      "source": "po_123",
      "status": "pending",
      "type": "advance_funding"
    },
    {
      "id": "txn_456",
      "object": "balance_transaction",
      "amount": 4000,
      "available_on": 1715205759, // 2024-05-08 22:02:39 UTC
      "created": 1715205760, // 2024-05-08 22:02:40 UTC
      "currency": "usd",
      "description": "Adding available funds for po_123",
      "exchange_rate": null,
      "fee": 0,
      "fee_details": [],
      "net": 4000,
      "reporting_category": "advance",
      "source": "po_123",
      "status": "available",
      "type": "advance"
    },
    {
      "id": "txn_567",
      "object": "balance_transaction",
      "amount": -4000,
      "available_on": 1715205759, // 2024-05-08 22:02:39 UTC
      "created": 1715205760, // 2024-05-08 22:02:40 UTC
      "currency": "usd",
      "description": "",
      "exchange_rate": null,
      "fee": 0,
      "fee_details": [],
      "net": -4000,
      "reporting_category": "payout",
      "source": "po_123",
      "status": "available",
      "type": "payout"
    }
}
```
