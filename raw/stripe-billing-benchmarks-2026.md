<!-- Source URL: https://docs.stripe.com/billing/subscriptions/benchmarking -->
<!-- Fetched: 2026-05-13 -->

# Benchmarking

Compare metric performance to that of similar businesses.

Use the **Compare to Benchmarks** dropdown on the Billing overview page to see how your business compares to similar companies using Stripe. Benchmarks can help you assess business health, uncover seasonal patterns, communicate performance to stakeholders, and set realistic growth targets.

## Access benchmarks

To access benchmarks, a business must meet both of the following requirements:

- Have at least five active subscriptions
- Have had at least one paid subscription within the past year

## Peer groups

Stripe uses a k-nearest neighbors (k-NN) algorithm to identify businesses that are most similar to yours based on several factors:

- Publicly available information about your business
- Merchant category code (MCC)
- An [AI-generated](<https://support.stripe.com/questions/use-of-artificial-intelligence-(ai)-in-stripe-services>) industry we’ve identified for your business
- Annual recurring revenue (ARR)
- Average revenue per user (ARPU)

When available, we use website information to better understand your business, such as the industry you’re in and the products or services you offer. This information helps us map businesses into a shared vector space, where we can measure similarity and identify relevant peers.

A business must meet all of the following criteria to be included in another user’s peer group:

- Have at least 100 active subscriptions
- Have maintained more than five active subscriptions for at least 1 year
- Show positive annual recurring revenue (ARR)

These requirements help make sure that the data used for comparisons is complete and reliable.

## How to interpret benchmarks

Some tabs on the Billing overview page have the option to compare to benchmarks (in addition to comparing against previous periods). Select **Benchmarks** from the comparison dropdown to show the top, median, and bottom trends from a group of at least 100 similar businesses, and show your position relative to peers by percentile.

Click the chart to open a detailed view where you can hover over the chart to see your percentile standing, along with the top, median, and bottom trends from your peer group for that time period.

Benchmarks are available for the following metrics, over the past 12 months:

- [Gross and net MRR churn rate](https://docs.stripe.com/billing/subscriptions/analytics.md#churned-revenue)
- [Subscriber churn rate](https://docs.stripe.com/billing/subscriptions/analytics.md#subscriber-churn-rate)
- [Subscriber and revenue retention](https://docs.stripe.com/billing/subscriptions/analytics.md#retention-by-cohort)
- [MRR Growth Rate](https://docs.stripe.com/billing/subscriptions/analytics.md#mrr-growth)
- [Subscriber Lifetime Value (LTV)](https://docs.stripe.com/billing/subscriptions/analytics.md#ltv)
- [Average Revenue Per User (ARPU)](https://docs.stripe.com/billing/subscriptions/analytics.md#arpu)
- [Trial Conversion Rate](https://docs.stripe.com/billing/subscriptions/analytics.md#trial-conversion-rate)
