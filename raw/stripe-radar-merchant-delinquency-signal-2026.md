<!-- Source URL: https://docs.stripe.com/radar/merchant-delinquency-risk -->
<!-- Fetched: 2026-05-10 -->

# Merchant delinquency risk

Identify connected accounts at risk of financial distress that might lead to negative balances.

The merchant delinquency risk signal identifies connected accounts at risk of financial distress. This includes accounts that are likely to accumulate unrecoverable negative balances from disputes, refunds, or failed payouts.

## Retrieve delinquency signals

Use the [Account Signals API](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2026-03-25.preview) to retrieve the delinquency signal for a connected account. The response includes the latest evaluation with a risk level and indicators to explain the risk assessment.

## Risk levels

Each signal returns a `risk_level` with one of the following values.

| Risk level     | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `highest`      | The highest predicted risk of delinquency.                 |
| `elevated`     | An elevated predicted risk of delinquency.                 |
| `normal`       | A predicted risk that’s at or near the baseline.           |
| `low`          | A predicted risk of delinquency that’s below the baseline. |
| `not_assessed` | The signal hasn’t been assessed for this account.          |

## Indicators

The following delinquency indicators explain which financial and behavioral factors contributed to the risk assessment.

| Indicator              | Description                                                                                           |
| ---------------------- | ----------------------------------------------------------------------------------------------------- |
| `account_balance`      | The average, minimum, or maximum balances and negative balance duration.                              |
| `aov`                  | The average order value relative to the industry or account’s past history.                           |
| `charge_concentration` | The concentration of charge amounts, counts, and number of distinct payers.                           |
| `dispute_window`       | The dispute window estimates and a comparison to the industry average.                                |
| `disputes`             | The recent dispute rate and amount relative to history.                                               |
| `duplicates`           | The accounts sharing identifiers (for example, email, bank, name) associated with past delinquencies. |
| `exposure`             | The account and industry exposure.                                                                    |
| `firmographic`         | The account attributes, such as country, region, or industry.                                         |
| `lifetime_metrics`     | The lifetime totals for transactions, disputes, and dispute rate.                                     |
| `payment_processing`   | The charge concentration, time between charges, and payment methods.                                  |
| `payment_volume`       | The trends for total payment volume and average payment volume.                                       |
| `payouts`              | The payout totals, comparison of instant versus regular activity, and relative trends.                |
| `refunds`              | The refund totals, rate, and averages.                                                                |
| `related_accounts`     | The accounts sharing identifiers associated with delinquencies in the Stripe network.                 |
| `tenure`               | The age of the account since creation.                                                                |
| `transfers`            | The failed transfer counts by reason, including insufficient funds failures.                          |

## Webhook event

Listen for `v1.account_signals[delinquency].created` event notifications when a delinquency signal is evaluated.

## Take action on connected accounts

After you receive a delinquency signal, use the available [Radar for Platforms](https://docs.stripe.com/radar/radar-for-platforms.md) tools to take action on your connected accounts. See the list of [available actions](https://docs.stripe.com/radar/account-risk-signals.md).
