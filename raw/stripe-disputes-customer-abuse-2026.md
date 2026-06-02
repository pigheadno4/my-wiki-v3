<!-- Source URL: https://docs.stripe.com/disputes/prevention/customer-abuse -->
<!-- Fetched: 2026-05-11 -->

# Customer abuse

Learn how to protect yourself against refund, reseller, and trial abuse.

Customer abuse is behavior that exploits your policies. These are the three common scenarios you might encounter:

- Refund abuse
- Resale abuse
- Trial abuse

Use this guide to learn how to prevent, detect, and mitigate these types of abuse. Every business is different, you can adapt these suggestions to fit your needs.

## Refund abuse

Refund abuse occurs when a customer takes advantage of your refund policy and causes disproportionate operational cost. For example, a customer might frequently return all purchased orders over a sustained period of time or request a refund for a shipment claiming they never received it despite having received their order.

### Customers with a history of repeatedly refunding orders

To assess whether refunds are concentrated among high-refunding customers, split order volume by customer refund frequency. Use the following [Stripe Sigma](https://docs.stripe.com/stripe-data/sigma.md) query to assess refund concentration.

For example, if the output shows that customers with 10 or more refunds per year account for most refunds but a small share of total orders, this might indicate abuse on a high level. However, we recommend you interpret these results in addition to your business context (such as the customer lifetime value).

```sql
-- Order counts by customer refund frequency
WITH order_counts AS (
  SELECT
    customer_id, -- This can be changed to another customer identifying attribute such as card, email, or shipping address
    COUNT(*) AS order_count,
    COUNT_IF(refunded) AS full_refund_count
  FROM charges
  WHERE captured
    AND created >= DATE_ADD('day', -365, CURRENT_DATE)
    AND dispute_id IS NULL -- Excludes disputes
  GROUP BY customer_id
),
order_count_frequency AS (
  SELECT
    CASE
      WHEN full_refund_count >= 10 THEN 10
      WHEN customer_id IS NULL THEN 0
      ELSE full_refund_count
    END AS customer_refunded_x_or_more_orders,
    SUM(order_count) AS total_orders,
    SUM(full_refund_count) AS full_refund_orders
  FROM order_counts
  GROUP BY CASE
    WHEN full_refund_count >= 10 THEN 10
    WHEN customer_id IS NULL THEN 0
    ELSE full_refund_count
  END
),
order_count_frequency_aggregate_v1 AS (
  SELECT
    *,
    SUM(total_orders) OVER (ORDER BY customer_refunded_x_or_more_orders DESC) AS total_orders_count,
    SUM(full_refund_orders) OVER (ORDER BY customer_refunded_x_or_more_orders DESC) AS total_full_refunds_count
  FROM order_count_frequency
  ORDER BY customer_refunded_x_or_more_orders
),
order_count_frequency_aggregate_v2 AS (
  SELECT
    *,
    total_full_refunds_count / CAST(total_orders_count AS DOUBLE) AS refund_rate,
    total_full_refunds_count / CAST(SUM(full_refund_orders) OVER () AS DOUBLE) AS refunded_orders_recall,
    total_orders_count / CAST(SUM(total_orders) OVER () AS DOUBLE) AS total_orders_recall
  FROM order_count_frequency_aggregate_v1
)
SELECT
  customer_refunded_x_or_more_orders,
  refund_rate, -- The rate of full refund orders divided by captured orders at each customer refund frequency and above
  refunded_orders_recall, -- Percentage of fully refunded orders out of all refunds
  total_orders_recall, -- Percentage of total orders out of all total orders
  total_orders_count, -- Number of all captured orders
  total_full_refunds_count -- Number of orders fully refunded
FROM order_count_frequency_aggregate_v2
ORDER BY customer_refunded_x_or_more_orders DESC
```

To address frequent high-refunding customers, you can:

- Notify identified customers about their refund history and its business impact
- Restrict future order attempts (temporary or permanent)
- Introduce a fee to deter repeat refunds

## Resale abuse

Resale abuse is a customer who intends to resell the product to another person or business elsewhere, such as a marketplace. For example, resellers might purchase limited-release goods in large quantities or create subscription accounts with discount codes in an effort to monetize them from another buyer.

### Account sharing

Account sharing, often referred to as “password sharing,” is when login credentials are shared to allow others to benefit from a single purchase. Look for activity such as:

- Simultaneous login sessions
- Logins from geographically dispersed IP addresses within a short time window

When detected, you can implement additional authentication such as an email or SMS one-time passcode to add friction and verify the account owner.

### Account transfers

Reseller transfers an account to another person typically for a fee. Look for activity such as:

- Accounts listed for sale on marketplaces you don’t manage
- Many accounts created using the same card or device and browser fingerprint, often using the same promotion code when applicable
- Login from a different geographic IP address shortly after account creation
- Screenshots shortly after account creation

Create [velocity rules](https://docs.stripe.com/radar/rules/reference.md#velocity-rules) to block, detect, or create friction on multiple accounts which might be created by potential resellers. A few rule examples using [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) include:

| Rule example                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Review if :card_funding: = 'prepaid' and :total_customers_for_card_weekly: > 3 and not :is_off_session: and :charge_description: = “Individual Plan New Customer Discount"` | This rule marks prepaid card payments triggered by direct customer action where the total number of customers per card in the last week exceeds 3 and matches a specific charge description. You can modify attributes as needed for your business. See the full list of [supported attributes](https://docs.stripe.com/radar/rules/supported-attributes.md). |
| `Block if ::customer_count_for_card_and_coupon_yearly:: > 3`                                                                                                                 | Blocks any attempt where customer count exceeds three per combination of card and coupon. This attribute is derived by you. To learn more, see [metadata attributes](https://docs.stripe.com/radar/rules/reference.md#metadata-attributes).                                                                                                                   |

Additionally, use [Stripe Sigma](https://docs.stripe.com/stripe-data/sigma.md) to investigate suspected resold accounts and reconcile with your internal data to check for any policy abuse.

## Trial abuse

Trial abuse occurs when customers cycle through free trials with no intent of converting to a paid account. For example, these customers create multiple accounts to repeatedly gain access or intentionally omit canceling trials, resulting in a breach of trial terms.

#### End of trial payment failure

Bad actors might repeatedly leverage stolen or virtual cards with no intention of canceling the trial at the end, resulting in high cost to the businesses.

Stripe Radar offers a [trial abuse control](https://docs.stripe.com/radar/risk-settings.md#prevent-free-trial-abuse) to detect repeated trial signup and failure to cancel trials. You can use this information to block or pre-authorize signups, limit product access, or take other actions for high-risk trials.

## Request access (Private preview)
