---
title: "Stripe Billing — Analytics"
type: source
date_ingested: 2026-11-08
original_format: webpage
canonical_url: "https://docs.stripe.com/billing/subscriptions/analytics"
raw_files:
  - "stripe-billing-subscriptions-analytics-2026-11-07.md"
  - "stripe-billing-analytics-2026.md"
tags: [stripe, billing, analytics, mrr, churn, subscribers, ltv, arpu, cohort, reports]
---

## Summary

Stripe Billing's Dashboard analytics guide defines recurring-revenue, subscriber, trial, churn, retention, and usage metrics. The 2026-11-07 capture distinguishes item-level trial offers from legacy subscription-level trials, adds AR aging and two CSV export routes, and keeps Usage MRR in preview-request status. These are documented analytics definitions, not observed merchant totals or settled revenue.

## Usage MRR preview

Both captures list Usage MRR and reporting as a preview feature. The November page provides a signup link and registration example to **request** access (new lines 16–34); it does not establish account eligibility, accepted registration, or inclusion of metered products in ordinary MRR. Ordinary MRR still excludes metered products (new line 113).

## Accounts receivable aging (2026-11-07)

**Billing overview > Collections** shows current unpaid invoice balances grouped by age **as of today**. AR aging for a supported past reporting date requires Revenue Recognition; the captured page does not enumerate supported historical dates. See new lines 36–38.

## CSV export routes (2026-11-07)

- **Individual metric details:** on Revenue, Subscribers, Trials, Churn, or Usage, open a metric and choose **Export**. The **Summary table** downloads aggregated time-series data reflecting the current date range, filters, grouping, and comparison where applicable. **Data results** downloads underlying rows for the selected period and filters only where the metric supports that option (new lines 40–51).
- **Prebuilt reports:** in live mode, use **Report downloads** on Billing overview. These reports have fixed schemas independent of an individual metric's detail-page filters or grouping (new lines 53–61).

| November 2026 prebuilt report | Listed contents |
|---|---|
| MRR per subscriber per month | Each subscriber's MRR at each month end |
| Subscription metrics per month | MRR and subscriber roll-forwards, retention, and customer value by month |
| Customer MRR changes | Customer MRR change log for new subscribers, upgrades, downgrades, reactivations, and churn |

Prebuilt report date columns use **UTC**, while Billing Analytics charts use the account time zone; monthly totals can therefore differ (new lines 63–65). The May capture instead lists **Subscription metrics summary**, with MRR and active-subscriber roll-forwards, trial conversion, and lifetime value (old lines 23–31). The newer row does not prove that the older label is unavailable on every Stripe surface.

## Configurable metrics

From Billing overview, **Configure** changes calculation choices for MRR, Churn, and Active Subscribers. Changes take **24–48 hours to appear in the configuration** (old line 35; new line 69), not a proven payment or cash-collection effect.

**Discounts in MRR:**
- Subtract recurring discounts: optional.
- Subtract one-time discounts: optional.
- Permanent recurring discounts: always subtracted (old lines 37–46; new lines 71–80).

**Active subscriber timing:**
- At subscription start, when the first billing period begins: the **most common** option, not an established product default.
- When first payment is received (old lines 48–53; new lines 82–87).

## Metric definitions

### MRR

MRR sums the monthly-normalized value of `active` and `past_due` subscriptions. Taxes, free plans, and metered products are excluded; a `canceled` or `unpaid` subscription ceases to count (new lines 111–115). The May capture described subscription-level trial exclusion (old line 79). The November capture makes this variant boundary explicit:

- For **item-level trial offers**, only the items currently trialing are excluded. Non-trial items in the same subscription still contribute.
- For a **legacy `trial_end` free trial**, the entire subscription is excluded during its trial (new line 115).

Example: 100 subscribers at $100/month plus 50 at $600/year gives $12,500 MRR in the page's simplified example (old line 81; new line 117). This is illustrative arithmetic, not a merchant result.

### MRR growth

Beginning MRR plus new, reactivation, and expansion MRR, less contraction and churn MRR, with FX adjustment (old lines 85–97; new lines 121–133).

### Active subscribers

Customers with positive MRR on at least one `active` or `past_due` subscription; multiple active subscriptions count once per customer. Free plans and trials without positive MRR do not count. If discounts are subtracted and a 100% coupon reduces MRR to zero, the subscriber is counted as churned and can reactivate when the coupon is removed (old lines 131–139; new lines 167–175).

### ARPU and LTV

ARPU = MRR ÷ active subscribers. Estimated subscriber LTV = ARPU ÷ subscriber churn rate, based on values at a point in time (old lines 149–159; new lines 185–195).

### Trials and trial conversion

**New trials** count trial periods started in the selected period. Under item-level trial offers, each trialing subscription item counts separately; under legacy `trial_end`, each subscription trial counts separately, so one customer may count more than once (new lines 199–205). The May capture's subscription-level language describes the older variant (old lines 163–168).

**Trial conversion rate** = trials converted to paid in the last 30 days ÷ trials ended in the last 30 days. Item-level offers track conversion for each trialing item; legacy `trial_end` tracks at subscription level. It may exceed 100% if some convert after their trial ended (old lines 170–174; new lines 207–211).

### Churn

Subscriber churn rate = churned subscribers in the past 30 days ÷ (active subscribers 30 days ago + new subscribers in those 30 days). Churned revenue = churned MRR + contraction MRR (old lines 176–188; new lines 213–225).

### Retention by cohort

Cohorts start when subscribers first generate positive MRR. Subscriber retention tracks remaining active subscribers; revenue retention tracks remaining MRR, which can exceed 100% after expansion (old lines 190–212; new lines 227–249).

### Usage metrics

**Aggregate usage** follows the meter's SUM or COUNT aggregation; the Dashboard does not display meters with other aggregation formulas. **Usage revenue** is the amount generated from usage events across meters in a period, excluding taxes and discounts; the documented example multiplies a metered product price by usage within an active subscription's billing period (old lines 99–129; new lines 135–165). These metrics do not imply ordinary MRR includes metered products.

## Dashboard features

- **Explore:** drill down into data points and, where cells are clickable, underlying events. Available for a subset of billing metrics (old lines 55–61; new lines 89–95).
- **Product/Price filtering and grouping:** available for a subset and unavailable with subscription volume in multiple currencies (old lines 63–69; new lines 97–103).
- **Benchmarking:** the guide lists comparison with similar Stripe businesses (old lines 8–13; new lines 9–14). See [[source-stripe-billing-benchmarks]] for separate benchmark detail.

## Related pages

- [[stripe-billing-analytics]] — concept route
- [[stripe-subscriptions]] — subscription concept
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-billing-subscriptions-analytics-2026-11-07|2026-11-07 Stripe Billing analytics capture]]
- [[raw/stripe-billing-analytics-2026|2026-05-13 Stripe Billing analytics capture]]
