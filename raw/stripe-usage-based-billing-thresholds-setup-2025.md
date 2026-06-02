<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/thresholds -->
<!-- Fetched: 2026-05-05 -->

# Set up thresholds

Set up usage thresholds to trigger alerts or invoices.

Set up billing thresholds to limit the amount owed or the products consumed between invoices or charges.

## Create billing thresholds

You can create [billing_thresholds](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-billing_thresholds) to issue an *invoice* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) when a customer’s accrued usage in a service period reaches a specific monetary threshold. You can also reset a subscription’s [billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_thresholds-reset_billing_cycle_anchor) when a customer reaches the monetary threshold.

Consider using billing thresholds to limit the amount owed or the products consumed between invoices or charges.

> Threshold invoices don’t include usage reported during the [invoice finalization grace period](https://docs.stripe.com/billing/subscriptions/usage-based/configure-grace-period.md). They reflect only the usage accrued within the billing period up to the point the invoice is created.

### Monetary thresholds

When you add a monetary threshold to a subscription, set the value as a multiple of the cost of one unit of the product. Setting a lower amount for the threshold results in your customers receiving an invoice for every unit of usage.

The value is a positive integer in the [smallest currency unit](https://docs.stripe.com/currencies.md#zero-decimal) (for example, 100 cents to charge 1 USD, or 100 to charge 100 JPY, a zero-decimal currency). Set the value to at least 50 currency units.

You can set monetary thresholds for a subscription using the Stripe [Dashboard](https://dashboard.stripe.com/test/subscriptions) or the API.

```curl
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "billing_thresholds[amount_gte]=10000" \
  -d "billing_thresholds[reset_billing_cycle_anchor]=false"
```

### Usage thresholds

When you add a usage threshold to a subscription item, set the value to exceed one unit of usage to prevent frequent invoicing. Stripe doesn’t support setting usage thresholds in the Dashboard.

```curl
curl https://api.stripe.com/v1/subscription_items/si_CFhSgkWb0MyTWg \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "billing_thresholds[usage_gte]=2000"
```

### Thresholds and the billing cycle anchor

By default, the [billing cycle anchor](https://docs.stripe.com/billing/subscriptions/billing-cycle.md) of a subscription remains unchanged after a customer reaches the usage threshold. If a customer reaches the threshold mid-month of a monthly subscription, the subscription resets at the end of the month, similar to a subscription without thresholds.

You can change the default behavior by configuring the subscription to reset the billing cycle anchor after it reaches the threshold. Stripe treats this configured behavior as if the subscription naturally arrived at its rollover point at the end of the month.

```curl
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "billing_thresholds[reset_billing_cycle_anchor]=true"
```

### Thresholds and tiered pricing

Stripe maintains tiers across threshold invoices. By default, tiers reset at the end of each billing period. You can change the default behavior by configuring the subscription to reset the billing cycle anchor after it reaches the threshold, similar to a subscription without thresholds.

For example, you run an ad platform with the following graduated tier structure for ad impressions:

| Tier                    | Amount (unit cost)          |
| ----------------------- | --------------------------- |
| 1-10000 (`up_to=10000`) | 0.50 USD (`unit_amount=50`) |
| 10000+ (`up_to=inf`)    | 0.40 USD (`unit_amount=40`) |

Because Stripe bills usage retrospectively, you can set a temporary threshold of 100 USD for new customers. Under this plan, you bill your customer every 200 impressions for the first 10,000 impressions (200 × 0.50 USD = 100 USD). When the customer exceeds 10,000 impressions, they’re billed every 250 impressions (250 × 0.40 USD = 100 USD). This continues until the end of the billing period, at which point you can invoice all usage that wasn’t previously invoiced, and the subscription and tiers reset.

To reset tiers after reaching a threshold, you must configure the subscription to reset the billing cycle anchor after the usage reaches the thresholds that you set.

### Volume tiers

Volume tiers define the pricing for all units of usage, as opposed to graduated tiers, which define pricing for a specific amount of usage. Some pricing models use volume tiers that decrease the unit cost at each successive tier. You can use these models to incentivize customers to use more of a product (for example, ad impressions, or GB of storage).

When combined with thresholds, these pricing models can lead to invoices with line items for negative amounts under the following conditions:

- A threshold invoice has already been issued.
- Subsequent usage gets billed to customers at a lower unit cost.

For example, consider the following tiered pricing structure:

| Tier                    | Amount (unit cost)          |
| ----------------------- | --------------------------- |
| 1-10000 (`up_to=10000`) | 0.50 USD (`unit_amount=50`) |
| 10000+ (`up_to=inf`)    | 0.40 USD (`unit_amount=40`) |

If a customer uses 10,000 units, the invoice total is 5,000 USD (10,000 × 0.50 USD = 5,000 USD). Any additional usage causes *all* usage to bill at the lower unit cost of 0.40 USD. If the customer uses one more unit, the invoice total *drops* to 4,000.40 USD (10,001 × 0.40 USD = 4,000.40 USD).

Without thresholds, Stripe would issue an invoice for 4,000.40 USD at the end of the billing period.

To demonstrate how negative invoicing can occur, assume you set a monetary threshold of 5,000 USD. In this scenario, Stripe issues an invoice when the customer reaches 10,000 units of usage.

If the customer uses one more unit, the invoice total drops to 4,000.40 USD (10,001 × 0.40 USD = 4,000.40 USD). However, if the customer doesn’t consume more units, they’re *owed* 999.60 USD (5,000 USD − 4,000.40 USD = 999.60 USD). At the end of the billing period, Stripe credits this amount to the customer’s balance, which we use to pay future invoices.

If the customer continues to accrue usage, the cost of the usage reaches 5,000 USD again when the customer uses 12,500 units (5,000 USD / 0.40 USD = 12,500). However, the previous payment of 5,000 USD covers all of this usage. As a result, we don’t issue an invoice.

Stripe won’t issue an invoice until either the total usage reaches 25,000 units (for a total cost of 10,000 USD), or the end of the billing period arrives—whichever occurs first. The tables below show the line items you see for the two invoices issued in the scenario where usage reaches 25,000 units.

Invoice 1:

| Line item                 | Quantity | Amount        |
| ------------------------- | -------- | ------------- |
| Usage (0.50 USD per unit) | 10,000   | 5,000 USD     |
| **Total**                 |          | **5,000 USD** |

Invoice 2:

| Line item                                       | Quantity | Amount        |
| ----------------------------------------------- | -------- | ------------- |
| Usage (0.40 USD per unit)                       | 25,000   | 10,000 USD    |
| Amount previously billed (at 0.50 USD per unit) |          | -5,000 USD    |
| **Total**                                       |          | **5,000 USD** |
