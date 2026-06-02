<!-- Source URL: https://docs.stripe.com/radar/fraudulent-merchant -->
<!-- Fetched: 2026-05-10 -->

# Fraudulent merchant signal

Detect connected accounts engaging in fraudulent activity.

The fraudulent merchant signal identifies whether a new or existing account poses a fraud risk. The Stripe machine learning models analyze patterns across the network, including bank account information, business details, transaction activity, disputes, and relationships with other accounts.

## Risk levels

Each signal returns a `risk_level` and a `probability` score with a value between 0 to 100.

| Risk level     | Description                                                     |
| -------------- | --------------------------------------------------------------- |
| `highest`      | Approximately a 90% probability that the account is fraudulent. |
| `elevated`     | Approximately a 50% probability that the account is fraudulent. |
| `normal`       | A low probability of fraud.                                     |
| `low`          | A very low probability of fraud.                                |
| `not_assessed` | The signal hasn’t been assessed for this account.               |

## Indicators

The following indicators explain the factors that contributed to the risk assessment.

| Indicator                                   | Description                                                                                                    |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `bank_account`                              | The bank account matches a previously detected fraudulent account.                                             |
| `business_information_and_account_activity` | There’s a spike in the average order value or payment volume, or suspicious business details.                  |
| `disputes`                                  | There’s a spike in disputes.                                                                                   |
| `failures`                                  | There’s a spike in payment failures.                                                                           |
| `geo_location`                              | There’s account activity in a country that differs from the business location or that’s in a high-risk region. |
| `other_related_accounts`                    | The account is connected to a previously detected fraudulent account.                                          |
| `other_transaction_activity`                | There are unusual transaction patterns, such as spikes in volume or order value.                               |
| `owner_email`                               | The email address uses a suspicious domain or doesn’t match the business URL.                                  |
| `web_presence`                              | There’s a suspicious web presence, such as a domain that doesn’t match the business.                           |

## Webhook event

Listen for `v2.signals.account_signal.fraudulent_merchant_ready` event notifications when a fraud signal is evaluated. The event payload includes the `risk_level`, `probability`, and `indicators` for the connected account.

## Take action on connected accounts

You can respond to the fraudulent merchant signals that you receive for a connected account using the [Radar for Platforms](https://docs.stripe.com/radar/radar-for-platforms.md) tools. See the list of [available actions](https://docs.stripe.com/radar/account-risk-signals.md).
