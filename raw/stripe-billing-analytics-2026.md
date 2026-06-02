<!-- Source URL: https://docs.stripe.com/billing/subscriptions/analytics -->
<!-- Fetched: 2026-05-13 -->

# Analytics

Use the Stripe Dashboard to monitor and analyze your recurring revenue.

[Stripe Billing](https://dashboard.stripe.com/billing) analytics and [downloadable reports](https://docs.stripe.com/billing/subscriptions/analytics.md#downloadable-reports) let you:

- Monitor overall performance at a glance
- Drill down into data to audit changes over time
- Filter and group data to compare segment performance
- Benchmark your metrics against similar businesses on Stripe

## Preview features

To get early access to a [preview](https://docs.stripe.com/release-phases.md) feature, enter your email.

| Preview program | Description                                   | Sign up                     |
| --------------- | --------------------------------------------- | --------------------------- |
| Usage MRR       | Access usage-based MRR and reporting features | to sign up for our preview. |

## Downloadable reports

To build financial models and begin downstream reporting, download your billing metrics data. The export is in CSV format and includes the following reports:

| Report                       | Description                                                                                                                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MRR per subscriber per month | Includes the Monthly Recurring Revenue (MRR) for each subscriber at the end of each month.                                                                                                     |
| Subscription metrics summary | A summary of your monthly subscription metrics. The report includes your MRR roll-forward report, active subscriber roll-forward report, trial conversion metrics, and lifetime value metrics. |
| Customer MRR changes         | Includes a log of every MRR change for each customer, including new subscribers, upgrades, downgrades, reactivations, and churn.                                                               |

## Configure your metrics definitions

You can configure metrics from the [Billing overview](https://dashboard.stripe.com/billing) page. Click **Configure** to change how Stripe calculates Monthly Recurring Revenue (MRR), Churn, and Active Subscribers. Changes take 24-48 hours to appear in your configuration.

### Discounts

You can configure whether to include or exclude discounts in your MRR calculation. Subtracting discounts from MRR is considered a more conservative approach to reporting MRR because it more closely reflects the present value of these customers.

You can adjust two settings to exclude discounts:

- **Subtract recurring discounts from MRR**: Turn this on for your MRR to reflect any recurring discounts applied.
- **Subtract one-time discounts from MRR**: Turn this on for your MRR to reflect any one-time discounts applied.

These settings apply the same way to all coupons you use on Stripe, including subscription-level coupons, line-item level coupons, and stacked coupons. Permanent recurring discounts, are always subtracted from MRR.

### Active subscribers

You can configure when Stripe considers a subscriber to be active:

- **At the start of the subscription**: If you select this option, a subscription is considered active when the first billing period begins. This is the most common option.
- **When the first payment is received**: If you select this, the subscription is considered active when the first payment is received. Use this if you don’t want to consider subscribers active until they’ve paid their first invoice.

## Audit your metrics with drill-downs

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to drill down into data points to see the underlying data. To do this, click **Explore** on a chart to see the chart and a table of related data points. If a cell in the table is clickable, you can click into it to reveal the underlying events for that data point. This is particularly helpful to understand things like which customers churned or expanded their subscription in a given period.

> This feature is currently available for a subset of billing metrics.

## Analyze your metrics with filtering and grouping

You can interact with billing charts using the **Explore** functionality.

Some charts, like **MRR growth** and **Churned revenue**, allow you to filter and group by **Product** or **Price**. To do this, click **Explore** on a chart to see the chart and a table of related data points below and options for filtering and grouping above.

> This feature is available for a subset of billing metrics. This feature isn’t available if you’re processing subscription volume in multiple currencies.

## Billing metric definitions

Expand the report names in this section to see descriptions of the analytics and downloadable reports from the Dashboard’s [Billing overview](https://dashboard.stripe.com/billing).

### Revenue

### Monthly Recurring Revenue (MRR)

**MRR** is the sum of the monthly-normalized value of all your `active` and `past_due` subscriptions. MRR calculations exclude subscriptions in trial periods, any taxes applied to the subscription, any subscribers on free plans, and any metered (usage based) products. When a subscriber’s subscription is canceled or marked as `unpaid`, then the subscription is considered [churn](https://docs.stripe.com/billing/subscriptions/analytics.md#churn) and no longer counts towards MRR.

For example, in a given period, 100 subscribers are on Plan A (100 USD per month) and 50 subscribers are on Plan B (600 USD per year). In this example, MMR is calculated as: (100 subscribers x 100 USD) + (50 subscribers x (600 USD / 12)) = 12,500 USD.

Learn more about how your [MRR is impacted by taxes, trials, delinquency, and refunds](<https://support.stripe.com/questions/understanding-monthly-recurring-revenue-(mrr)>).

### MRR growth

**MRR growth** is the net change in your MRR over a period of time starting with the MRR at the beginning of the period, adding any new MRR, reactivation MMR, and expansion MRR, subtracting any contraction MRR and any churn MRR, and adjusting for any foreign currency (FX) impact.

For example, at the start of the period, your MRR is 1,000 USD.

- **New MRR**: During the period, you have one subscriber convert from a free trial to Plan A (100 USD per month). This results in an increase of 100 USD to your MRR.
- **Expansion MMR**: During the period, you have one subscriber upgrade from Plan A (100 USD month) to Plan C (150 USD per month). This results in an increase of 50 USD to your MRR.
- **Contraction MMR**: During the period, you have one subscriber downgrade from Plan A (100 USD per month) to Plan B (60 USD per month). This results in a decrease of 40 USD to your MRR.
- **Churn**: During the period, you have one subscriber downgrade from Plan B (60 USD per month). This results in a decrease of 60 USD to your MRR.
- **FX Adjustment**: You have a single customer paying in a foreign currency. They subscribed to Plan A in a foreign currency last period. During that period it was worth (100 USD per month) but the currency lost value in the current period and it’s now worth 95 USD per month. This results in a decrease of 5 USD to your MRR.

At the end of the reporting period, your MRR is 1,045 USD.

### Usage

### Aggregate usage

**Aggregate usage** is the sum of all usage events over a given time, based on the [meter’s aggregation type](https://docs.stripe.com/api/billing/meter/object.md#billing_meter_object-default_aggregation). Use it to analyze consumption patterns and trends. Stripe doesn’t display meters with aggregation formulas that are neither sum nor count.

For example, consider the following meter:

- Meter Name: Data Transfer Meter
- Aggregation Type: SUM (total the amount of data used)

Customer A subscribes to a usage-based billing subscription with the above meter. The following usage events occur for Customer A in the month of January:

- Event 1: 100 GB used on January 1
- Event 2: 200 GB used on January 15
- Event 3: 50 GB used on January 30

The aggregate usage for the month is 350 GB (100 GB + 200 GB + 50 GB).

This aggregate usage figure can help you anticipate service demands and adjust your infrastructure accordingly.

### Usage revenue

**Usage revenue** is the total monetary amount generated from usage events across all meters during a given time period, excluding taxes and discounts. Stripe doesn’t display meters with aggregation formulas that are neither sum nor count. It equals the subscription price of a metered product multiplied by the customer’s total number of usage events within the billing period of an active subscription. It provides insight into the revenue expected from consumption-based billing.

For example, given the following meter:

- Meter Name: Data Transfer Meter
- Aggregation Type: SUM (total the amount of data used)

Customer A subscribes to a usage-based billing subscription with the above meter at a price of 0.10 USD per event. If customer A uses 150 GB of data in a billing period, their total usage revenue is 15.00 USD (150 GB multiplied by 0.10 USD).

### Subscribers

### Active subscribers

In Stripe, you create _Customer_ (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) and _Subscription_ (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) objects. If a customer has one or more subscriptions attached, Stripe considers that customer to be a subscriber.

**Active subscribers** only includes subscribers with positive MRR that are in an `active` or `past_due` status. It doesn’t include subscribers on free plans or trials. A customer with multiple active subscriptions is counted as a single active subscriber. See [How subscriptions work](https://docs.stripe.com/billing/subscriptions/overview.md#subscription-lifecycle) for information about subscription statuses.

If a subscriber drops to 0 USD in MRR, we consider them churned in the period. This most commonly happens when a subscriber cancels their subscription. It can also occur if you’re choosing to subtract discounts from your MRR. In this case, we consider a subscriber churned if they have a 100% coupon applied and they become active again if you remove the coupon.

### Active subscriber growth

**Active subscriber growth** is the net change in your number of active subscribers over a period of time. Start with the number of active subscribers at the beginning of the period, add any new active subscribers and any reactivated subscribers, and subtract any churned subscribers.

### New subscribers

**New subscribers** is the number of paid subscribers who became active for the first time during the period. This doesn’t include subscribers on free plans or trials. We don’t count existing paid subscribers who add additional subscriptions multiple times. We also don’t include reactivated customers.

### Average revenue per user (ARPU)

**ARPU** is your average MRR per paid subscriber. ARPU is calculated as the total MRR divided by total active subscribers.

For example, you have 100 active subscribers at the end of January. The total MRR at the end of January is 50,000 USD. Your ARPU at the end of January is 50,000 USD divided by 100, or 500 USD.

### Subscriber lifetime value (LTV)

**Subscriber lifetime value** is calculated by dividing the average revenue per user (ARPU) by the subscriber churn rate. This is an estimate of LTV based on the values at various points in time.

For example, in January the business started with 110 subscribers and finished with 100 after 10 subscribers churned. The total MRR at the end of January is 50,000 USD. The ARPU at the end of January is 500 USD and the January subscriber churn rate was 9%. Subscriber lifetime value at the end of January is calculated as 500 USD divided by 9%, which equals 5,555 USD.

### Trials

### New trials

**New trials** shows the sum of subscriptions that started a trial during the period. We count the number of trials at the subscription level rather than at the customer level, so a single customer can count as multiple trials. For example, each of the following scenarios counts as two new trials in January:

- Customer A creates two subscriptions in January. Each subscription starts with a 7-day free trial period on January 1.
- Customer B enters a 7-day free trial period on January 1. They start another 7-day free trial period on January 21.

### Trial conversion rate

**Trial conversion rate** is the number of subscriptions that converted from a trial to a paid plan in the last 30 days, divided by the number of trials that ended in the last 30 days. The number reflects the trial conversion rate at the end of the selected time period, and might exceed 100% if some subscriptions convert to a paid plan after the end of their trial period.

For example, during a 30-day period, 100 trials ended and 15 trials converted. The trial conversion rate equals 15 divided by 100, or 15%.

### Churn

### Subscriber churn rate

When all of a subscriber’s subscriptions are canceled or marked as `unpaid`, the subscriber is considered to have churned and no longer counts as an active subscriber. **Subscriber churn rate** is the number of total churned subscribers in the past 30 days, divided by the number of active subscribers 30 days ago, plus the total new subscribers in the past 30 days.

For example, at the start of the month, the business had 1000 subscribers. During the month, the business added 100 subscribers and churned 100 subscribers. The subscriber churn rate equals the number of churned subscribers (100) divided by the sum of the subscribers at the beginning of the month and the new subscribers added during the month (1000 + 100), resulting in 100 / 1100 = 9.1%.

### Churned revenue

**Churned revenue** is the sum of churned MRR plus total contraction MRR in the period.

For example, during the period, Customer A cancels their 120 USD per year plan and Customer B downgrades from a 50 USD per month plan to a 25 USD per month plan. The churned revenue during the period is calculated as 10 USD (Customer A) + 25 USD (Customer B) = 35 USD.

### Retention by cohort

Stripe assigns cohorts to subscribers based off of when they first started generating positive Monthly Recurring Revenue (MRR) by starting active paying subscriptions. Revenue retention considers expansion and can increase above 100%.

For **Subscriber retention**:

- The start value is the initial number of active subscribers in the cohort.
- The month column shows the remaining number of active subscribers at the end of each subsequent month.

For **Revenue retention**:

- The start MRR is the MRR of all active subscribers in the cohort.
- The month column shows the amount of MRR remaining from subscribers in the cohort at the end of each subsequent month. The MRR for a cohort can change due to upgrades, downgrades, and cancellations and thus can exceed 100%.

For example, if each month’s subscriber churn rate is 10%, you can expect the following retention rates in each following month:

- Month 1: 90%
- Month 2: 81%
- Month 3: 73%
- Month 4: 66%
- Month 5: 59%

In January, 100 subscribers became active on 10 USD per month plans. The starting MRR is 1,000 USD. At the end of the first month, 10 subscribers have churned and 5 subscribers have upgraded to 25 USD per month plans. The net MRR impact is calculated as follows: 125 USD of expansion MRR minus 100 USD of churn MRR equals an increase of 25 USD. Therefore, at the end of the first month, you see 102.5% revenue retention.
