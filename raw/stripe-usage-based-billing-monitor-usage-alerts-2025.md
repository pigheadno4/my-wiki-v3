<!-- Source URL: https://docs.stripe.com/billing/subscriptions/usage-based/monitor-usage -->
<!-- Fetched: 2026-05-05 -->

# Monitor usage with alerts

Set up alerts for when a customer exceeds a usage threshold.

Use alerts to notify you when customers exceed meter usage thresholds, or to trigger an invoice when customers reach a specific billing threshold. You can create alerts that apply to specific customers or all customers.

Are you interested in creating alerts for when customers exceed a specific spend amount or their available credits are low?

Create usage alerts in your business workflows, such as the following:

- **Email users**: Allow customers to configure usage limits, and send an email when they hit their limit.
- **Deprovision access**: Grant customers a free number of usage units to your service, and remove access when they exceed the limit.
- **Notify the sales team of an upsell**: Alert your sales team of an enterprise opportunity when a self-serve user exceeds a usage threshold.

## Before you begin

Consider the following limitations for usage alerts:

- We evaluate alerts when you report usage data after you create the alert. However, the evaluation includes usage data that you reported before you created the alert.
- You can create a maximum of 25 alerts for each combination of a specific meter and customer. However, you can create an alert for a specific meter for each of your customers.

Consider the following limitations for billing thresholds:

- Thresholds don’t apply to [trial subscriptions](https://docs.stripe.com/billing/subscriptions/trials.md).
- Billing thresholds aren’t evaluated in the 24 hours before a subscription ends. This helps limit confusion for a customer who receives multiple invoices on the same date.
- Monetary thresholds must be greater than the sum of any flat rates on usage-based subscription items.
- When determining if a monetary threshold has been reached, the value we use excludes taxes but includes discounts and billing credits.
- Subscriptions are only allowed a single monetary threshold.
- Subscription items are only allowed a single usage threshold.
- Invoiced amounts or usage might be slightly higher than the specified thresholds because invoices aren’t issued at the exact moment a specified threshold is reached.
- Per-package tiered pricing isn’t currently supported.

[Set up alerts](https://docs.stripe.com/billing/subscriptions/usage-based/alerts.md): Configure usage alerts with the Dashboard or API.

[Set up thresholds](https://docs.stripe.com/billing/subscriptions/usage-based/thresholds.md): Configure thresholds for usage.
