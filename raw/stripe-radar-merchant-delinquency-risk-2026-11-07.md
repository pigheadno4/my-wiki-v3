<!-- Source URL: https://docs.stripe.com/radar/merchant-delinquency-risk -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Merchant delinquency risk

Identify connected accounts at risk of delinquency that might lead to negative balances.

The merchant delinquency risk signal identifies connected accounts at risk of carrying a negative balance for more than 90 days. This includes accounts that are likely to accumulate unrecoverable negative balances from disputes, refunds, or failed payouts.

### Get early access to the merchant delinquency risk signal.

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/radar/merchant-delinquency-risk" \
  -d '{"email": "EMAIL", "preview": "merchant_risk_tooling_beta_preview"}'
```

## Retrieve delinquency signals

Use the [Account Signals API](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=2026-07-29.preview) to retrieve the delinquency signal for a connected account. The response includes the latest evaluation with a risk level and indicators to explain the risk assessment.

## Risk levels 

Each signal returns a `risk_level` with one of the following values. On Radar Plus and Radar Pro, the signal also includes a `probability` score with a value between 0 and 100.

| Risk level | Description |
| --- | --- |
| `highest` | The highest predicted risk of delinquency. |
| `elevated` | An elevated predicted risk of delinquency. |
| `normal` | A predicted risk that’s at or near the baseline. |
| `low` | A predicted risk of delinquency that’s below the baseline. |

## Indicators 

The following delinquency indicators explain which financial and behavioral factors contributed to the risk assessment.

| Indicator | Description |
| --- | --- |
| `account_balance` | The average, minimum, or maximum balances and negative balance duration. |
| `aov` | The average order value relative to the industry or account’s past history. |
| `charge_concentration` | The concentration of charge amounts, counts, and number of distinct payers. |
| `dispute_window` | The dispute window estimates and a comparison to the industry average. |
| `disputes` | The recent dispute rate and amount relative to history. |
| `exposure` | The account and industry exposure. |
| `firmographic` | The account attributes, such as country, region, or industry. |
| `lifetime_metrics` | The lifetime totals for transactions, disputes, and dispute rate. |
| `payment_processing` | The charge concentration, time between charges, and payment methods. |
| `payment_volume` | The trends for total payment volume and average payment volume. |
| `payouts` | The payout totals, comparison of instant versus regular activity, and relative trends. |
| `refunds` | The refund totals, rate, and averages. |
| `related_accounts` | The accounts sharing identifiers associated with delinquencies in the Stripe network. |
| `tenure` | The age of the account since creation. |
| `transfers` | The failed transfer counts by reason, including insufficient funds failures. |

## Webhook event 

Listen for `v2.signals.account_signal.merchant_delinquency_ready` event notifications when a delinquency signal is evaluated.

## Take action on connected accounts

After you receive a delinquency signal, use the available [Radar](https://docs.stripe.com/radar.md) tools to take action on your connected accounts. See the list of [available actions](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action).
