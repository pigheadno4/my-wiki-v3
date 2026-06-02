<!-- Source URL: https://docs.stripe.com/radar/fraud-alerts -->
<!-- Fetched: 2026-05-10 -->

# Fraud alerts

Get notified when Stripe detects unusual fraud patterns.

Stripe continuously monitors your payment activity for signs of fraud attacks. When we detect unusual patterns—such as a significant shift in the distribution of Radar risk scores—we send you an email and display an alert in the [Radar page](https://dashboard.stripe.com/radar) of your Dashboard.

Fraud attacks can result in lost revenue, increased dispute fees, and potential enrollment in card network [monitoring programs](https://docs.stripe.com/radar/analytics.md#card-monitoring-programs). By alerting you to potential attacks when we detect unusual patterns, Stripe gives you the tools to respond quickly and mitigate these risks.

## Receive fraud alerts

When Stripe detects a potential fraud attack on your account, we notify you with:

- **Email notification**: An email describing the detected attack with a link to view details in your Dashboard
- **Dashboard notification**: A bell notification in your Dashboard with a link to view details

The email and Dashboard notification direct you to a dedicated fraud alert investigation page where you can review the details and take action.

## Review fraud alerts

When you access a fraud alert in your Dashboard, you can:

- **View risk trends**: See charts showing the distribution of Radar risk scores or risk levels over the alert period compared to previous weeks.
- **Review suspicious transactions**: Access a list of payments with elevated risk that might warrant investigation.
- **Understand the impact**: See the volume and count of potentially fraudulent payments.

## Take action on fraud alerts

The actions you can take when you receive a fraud alert depend on whether you use Radar or Radar for Fraud Teams:

### Radar users

If you use _Radar_ (Stripe Radar helps detect and block fraud for any type of business using machine learning that trains on data across millions of global companies. It’s built into Stripe and requires no additional setup to get started), you can:

- **Review elevated risk payments**: See which recent transactions have elevated or high risk levels.
- **Verify the attack**: Confirm whether the shift in risk levels matches your expectations.
- **Upgrade to Radar for Fraud Teams**: Access additional fraud prevention tools to stop the current attack and prevent future ones.

### Radar for Fraud Teams users

If you use _Radar for Fraud Teams_ (Radar for Fraud Teams helps you fine-tune how Radar operates, get fraud insights on suspicious charges, and assess your fraud management performance from a unified dashboard), you can take additional action:

- **Review recommended refunds**: View [Stripe’s recommendations](https://docs.stripe.com/radar/reviews.md#smart-refunds) for payments to refund proactively to avoid disputes.
- **Enable fraud controls**: Use [fraud controls](https://docs.stripe.com/radar/risk-settings.md) to intelligently block or authenticate higher-risk payments and reduce fraud.
- **Adjust your strategy**: Create or modify [Radar rules](https://docs.stripe.com/radar/rules.md) to target the specific fraud patterns identified.

## Best practices

When you receive a fraud alert:

1. **Act quickly**: Fraud attacks can escalate rapidly. Review the alert as soon as possible to help minimize losses.
1. **Verify the pattern**: Check whether the detected risk shift aligns with expected changes in your business activity or represents actual fraudulent behavior.
1. **Review flagged transactions**: Examine the high-risk payments listed in the alert. Look for common patterns such as similar billing addresses, IP addresses, or card BINs.
1. **Take preventive action**: Use the tools available to you to mitigate the risk of further fraudulent transactions.
1. **Monitor results**: After taking action, continue monitoring your fraud metrics to make sure the attack has been mitigated.

## Related resources

- [Risk settings](https://docs.stripe.com/radar/risk-settings.md) — Configure how Radar handles different risk levels.
- [Radar rules](https://docs.stripe.com/radar/rules.md) — Create custom rules to block specific fraud patterns.
- [Dispute prevention](https://docs.stripe.com/disputes/prevention.md) — Review strategies to reduce disputes.
- [Card monitoring programs](https://docs.stripe.com/radar/analytics.md#card-monitoring-programs) — Understand card network fraud thresholds.
