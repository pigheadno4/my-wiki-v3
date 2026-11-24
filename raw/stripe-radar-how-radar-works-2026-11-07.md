<!-- Source URL: https://docs.stripe.com/radar/how-radar-works -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# How Radar works

Learn about the Radar features that can help you protect your business against fraud.

[Stripe Radar](https://stripe.com/radar) provides real-time fraud protection, customization capabilities, and deeper insights and trend analysis for your business. Radar protects against transaction fraud, account risk, and customer abuse.

Radar screens all payment attempt types (for example, successful, declined, blocked, and flagged for review) and all [supported payment methods](https://docs.stripe.com/radar/supported-payment-methods.md).

Radar doesn’t screen SetupIntents for non-card payment methods.

## Compare Radar plans 

Radar provides several plans for you to choose from, based on your business needs for real-time fraud protection:

- **Radar Lite**: AI-based fraud prevention for payments and card testing, plus fraud alerts.
- **Radar Standard**: Out-of-the-box fraud protection for all [supported payment methods](https://docs.stripe.com/radar/supported-payment-methods.md) to detect and prevent transaction fraud, and identify fraudulent accounts. On average, businesses block 42% more fraud on Standard compared to Lite.
- **Radar Plus**: Configurable fraud protection that lets you write and backtest custom rules, set risk tolerance, and get advanced analytics.
- **Radar Pro**: Advanced protection against emerging fraud threats and customer abuse. Detect multi-account, free trial, and pay-as-you-go abuse.

### Transaction risk prevention 

|  | Radar Lite | Radar Standard | Radar Plus | Radar Pro |
| --- | --- | --- | --- | --- |
| [Essential fraud prevention for card payments](https://docs.stripe.com/radar/risk-settings.md#fraudulent-dispute-score) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Card testing prevention](https://docs.stripe.com/disputes/prevention/card-testing.md#prevent-card-testing) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Fraud alerts](https://docs.stripe.com/radar/analytics/transaction-fraud-alerts.md) | ✓ Supported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Expanded fraud prevention](https://docs.stripe.com/radar/risk-settings.md#fraudulent-payment-score) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Fraud prevention for all payment methods](https://docs.stripe.com/radar/supported-payment-methods.md) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Fraud analytics](https://docs.stripe.com/radar/analytics.md) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Default rules](https://docs.stripe.com/radar/rules.md#built-in-rules) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Default allowlists and blocklists](https://docs.stripe.com/radar/lists.md#default-lists) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Risk level](https://docs.stripe.com/radar/transaction-risk-prevention.md#risk-outcomes) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Risk scores](https://docs.stripe.com/radar/risk-settings.md#radar-scores) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Custom rules, backtesting, allowlists, and blocklists](https://docs.stripe.com/radar/rules.md#create-rules) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Manual reviews](https://docs.stripe.com/radar/transaction-reviews.md) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Risk preferences](https://docs.stripe.com/radar/risk-settings.md) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Adaptive 3D Secure](https://docs.stripe.com/radar/risk-settings.md#adaptive-3ds) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Smart Refunds](https://docs.stripe.com/radar/transaction-reviews.md#smart-refunds) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Radar Assistant](https://docs.stripe.com/radar/rules.md#radar-assistant) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Advanced fraud analytics](https://docs.stripe.com/radar/analytics.md) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| Agentic insights | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Dynamic risk thresholds](https://docs.stripe.com/radar/risk-settings.md#dynamic-risk-thresholds) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |

### Customer abuse prevention 

|  | Radar Lite | Radar Standard | Radar Plus | Radar Pro |
| --- | --- | --- | --- | --- |
| [Free trial](https://docs.stripe.com/radar/free-trial-abuse.md) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| [Bot abuse](https://docs.stripe.com/radar/bot-abuse.md) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| [Multi-account signal](https://docs.stripe.com/radar/customer-account-evaluations.md) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| [Account sharing signal](https://docs.stripe.com/radar/customer-account-evaluations.md) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |
| [Pay-as-you-go signal](https://docs.stripe.com/radar/pay-as-you-go-abuse.md) | - Unsupported | - Unsupported | - Unsupported | ✓ Supported |

### Account risk prevention 

|  | Radar Lite | Radar Standard | Radar Plus | Radar Pro |
| --- | --- | --- | --- | --- |
| [AI-based fraud prevention for accounts](https://docs.stripe.com/radar/account-fraud-prevention.md#identify-potential-financial-risk) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Fraud analytics](https://docs.stripe.com/radar/account-fraud-prevention.md#risk-metrics) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Default rules](https://docs.stripe.com/radar/rules.md#built-in-rules) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Default allowlists and blocklists](https://docs.stripe.com/radar/lists.md) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Manual reviews](https://docs.stripe.com/radar/account-fraud-prevention.md#connected-account-reviews) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Account risk recommendations](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Fraudulent merchant signal](https://docs.stripe.com/radar/fraudulent-merchant.md) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Account risk history](https://docs.stripe.com/radar/account-fraud-prevention.md#risk-history) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Account risk levels](https://docs.stripe.com/radar/account-fraud-prevention.md#risk-scores-and-levels) | - Unsupported | ✓ Supported | ✓ Supported | ✓ Supported |
| [Account risk scores](https://docs.stripe.com/radar/account-fraud-prevention.md#identify-potential-financial-risk) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Custom rules, backtesting, allowlists, and blocklists](https://docs.stripe.com/radar/account-fraud-prevention.md#custom-rule-creation) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Dynamic reserves](https://docs.stripe.com/radar/account-fraud-prevention.md#set-reserves) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Fraudulent website signal](https://docs.stripe.com/radar/fraudulent-website.md) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Radar Assistant](https://docs.stripe.com/radar/rules.md#radar-assistant) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |
| [Agentic insights](https://docs.stripe.com/radar/account-fraud-prevention.md#agentic-account-risk-insights) | - Unsupported | - Unsupported | ✓ Supported | ✓ Supported |

## Radar fees 

Radar Standard, Plus, and Pro plans [charge a fee](https://stripe.com/radar/pricing) for each screened transaction. This applies to any authorization or charge evaluated by Radar, including one-off payments, recurring transactions, invoice transactions, and subscription lifecycle events. Fees are charged only when Radar screens a transaction.

For subscriptions created through Stripe Billing, Radar always screens and charges for the first payment on a subscription and the first payment after any payment method change. Beyond these, you can use the Dashboard to configure the number of successful renewal cycles Radar screens before stopping. For example, you might screen the first five renewals after the first payment on the subscription and then stop. You aren’t charged for skipped renewals. If the payment method on a subscription changes, Radar resumes screening on the next payment, and your configured skip behavior resumes from that point. For subscriptions with a free trial, the first screened payment occurs when the customer is charged.

For Connect users, Stripe charges Radar account fees to the platform, and Radar transaction fees based on the rate for the account that collected the payment. For payments collected by the platform account and transferred to a connected account, you can pass Radar fees to the connected account by reducing the transferred amount.
