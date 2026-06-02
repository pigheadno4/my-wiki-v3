<!-- Source URL: https://docs.stripe.com/payments/analytics/authorization-boost -->
<!-- Fetched: 2026-05-08 -->

# Set up an A/B test for Authorization Boost

See how Authorization Boost compares with your current optimization settings.

Authorization Boost combines features such as [Adaptive Acceptance](https://docs.stripe.com/payments/analytics/optimization.md#adaptive-acceptance), [Network tokens](https://docs.stripe.com/payments/analytics/optimization.md#network-tokens), and [Card account updater (CAU)](https://docs.stripe.com/payments/analytics/optimization.md#card-account-updater) to improve your payment success rate for card-not-present transactions, and decrease processing costs for businesses on [IC+ pricing](https://support.stripe.com/questions/understanding-blended-interchange-pricing).

Run a 30-day A/B test to measure the impact before you decide whether to enable Authorization Boost. The test runs at no additional cost—you’re only billed for optimization features you already have enabled on your Stripe account, in line with your Stripe Services Agreement.

## How Stripe configures the test

For the A/B test, Stripe randomizes your eligible payment volume between two equal groups:

- **Control group (called Current features)**: Uses your existing optimization configuration, plus Card account updater if that feature isn’t currently enabled.
- **Experiment treatment group (called Authorization Boost)**: Uses your existing optimization configuration plus any Authorization Boost features you don’t already use.

Each feature works as follows:

- **Adaptive Acceptance and Network tokens**: If you currently don’t use either of these features, they only run in the Authorization Boost group—meaning they apply to 50% of your eligible payment volume.
- **Card account updater (CAU)**: Always runs on both the Current features and Authorization Boost groups regardless of whether you currently use it—meaning it applies to 100% of your card-not-present payment volume. This is because Stripe can’t apply card credential updates selectively across the control or treatment groups. If you don’t have this feature enabled, Stripe enables it for both groups to keep testing conditions equal.

## Start your test

1. Go to the [Optimization](https://dashboard.stripe.com/optimization) page in the Dashboard.
1. Find the Test Authorization Boost recommendation and click **Test for 30 days**.
1. Click **Test Authorization Boost**.
1. Confirm your selection and click **Start test**.

### Cancel your test

[Admin and Developer roles](https://docs.stripe.com/get-started/account/teams/roles.md) can cancel the test at any time during the 30-day period.

1. Go to the [Optimization](https://dashboard.stripe.com/optimization) page in the Dashboard.
1. Click the overflow menu (⋯) and click **End Test**.

After canceling, you revert to your prior optimization features. You can’t run another Authorization Boost test for 12 months.

## Monitor your test

During the 30-day test period, go to the [Optimization](https://dashboard.stripe.com/optimization) page in the Dashboard to track progress. The page displays the following metrics for both the current features and Authorization Boost groups:

| Metric               | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Payments             | The total number of attempted payments in your A/B test.                 |
| Accepted payments    | The number of attempted payments authorized by the card networks.        |
| Payment success rate | The number of accepted payments divided by the total number of payments. |

All metrics are [deduplicated](https://docs.stripe.com/payments/analytics/acceptance.md?payment-attempt=deduplicated-rate) and might take up to 12 hours to update throughout the test. Because the metrics are deduplicated, data in the first week might fluctuate as retries occur. When the A/B test begins, you might see a pronounced difference between the A/B test payment success rate and the payment success rates on the [Acceptance](https://dashboard.stripe.com/acceptance) page of the Dashboard. After a few days, as associated payment retries occur, these two rates match more closely.

## Interpret your results

Final results are available 37 days after test initiation. Stripe waits 7 days to account for payments that initially failed during the 30-day test period but were successfully retried and authorized afterward.

Stripe notifies you about the final results through email. You can see a results summary that includes the estimated impact of the test on the [Optimization](https://dashboard.stripe.com/optimization) page in the Dashboard. After 37 days, Stripe compares the payment success rate between the two groups and calculates the estimated impact of enabling Authorization Boost on your total eligible volume during the test period. This impact is incremental, only considering the Authorization Boost features you don’t already use.

Statistically significant changes in payment success rate appear highlighted in green with the associated percentage change. Non-statistically significant changes in payment success rate appear in grey. Stripe considers results statistically significant when the probability of observing them by chance alone is less than 5%.

### How Stripe calculates results

Stripe calculates the A/B test results using [deduplicated](https://docs.stripe.com/payments/analytics/acceptance.md?payment-attempt=deduplicated-rate#specify-raw-rate-deduplicated-rate) payment success rates, grouping retried attempted payments together and calculating the payment success rate based on the final outcome.

Stripe calculates the estimated impact of the Authorization Boost features in the following manner:

- **Adaptive Acceptance and Network tokens**: Stripe measures the difference in payment success rate between the control and treatment groups. Then Stripe multiplies that difference by your total attempted payment volume during the 30-day test period to scale the estimated effect from the A/B test across your total eligible volume.
- **Card account updater (CAU)**: Because card credential updates are applied to 100% of your payment volume, Stripe estimates recovered revenue from updated card credentials during the test period. To learn more about how Stripe estimates whether a feature led to a payment succeeding, see [How Stripe calculates recovered revenue from optimizations](https://docs.stripe.com/payments/analytics/optimization.md#recovered-revenue-from-optimizations). Total Authorization Boost estimated impact combines the A/B test impact with your estimated Card account updater recovered revenue, if your existing configuration doesn’t include Card account updater.

#### Example

#### Estimated impact (with CAU)

| Calculation component              | Value                          |
| ---------------------------------- | ------------------------------ |
| Treatment payment success rate     | 93.5%                          |
| Control payment success rate       | 91%                            |
| Difference in payment success rate | 2.5%                           |
| Attempted payment volume           | 100,000 USD                    |
| Estimated impact                   | 100,000 USD × 2.5% = 2,500 USD |

#### Estimated impact (without CAU)

| Calculation component                       | Value                                                  |
| ------------------------------------------- | ------------------------------------------------------ |
| Treatment payment success rate              | 93.5%                                                  |
| Control payment success rate                | 91%                                                    |
| Difference in payment success rate          | 2.5%                                                   |
| Attempted payment volume                    | 100,000 USD                                            |
| Recovered revenue from Card account updater | 1,000 USD                                              |
| Estimated impact                            | 100,000 USD × 2.5% = 2,500 USD + 1,000 USD = 3,500 USD |

> Stripe doesn’t guarantee outcomes from Authorization Boost features. The calculations we provide are estimates to help with your decision. For the most current data, see the [Optimization](https://dashboard.stripe.com/optimization) page in the Dashboard.

## Next steps

Any optimizations that were enabled for your Stripe account before the test remain enabled after the test ends. You can purchase Authorization Boost by clicking **Enable Authorization Boost** on the results summary. Learn more about [pricing](https://stripe.com/authorization-boost#pricing). For custom pricing, contact your Stripe account team.

## Request early access
