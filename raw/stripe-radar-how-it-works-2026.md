<!-- Source URL: https://docs.stripe.com/radar/how-radar-works -->
<!-- Fetched: 2026-05-10 -->

# How Radar works

Learn about the Radar features that can help you protect your business against fraud.

[Stripe Radar](https://stripe.com/radar) provides real-time fraud protection and requires no additional development time. [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) adds customization capabilities and deeper insights and trend analysis for your business. [Radar for Platforms](https://docs.stripe.com/radar/radar-for-platforms.md) provides protection against both transaction and account risk.

Radar evaluates transactions in real-time, using AI algorithms to assess the risk of fraud. All Radar pricing tiers [charge a fee](https://stripe.com/radar/pricing) for each transaction they evaluate, including the first transaction and all subsequent transactions for recurring payments. The exception is Stripe Billing users, who we only bill for the first transaction—we don’t bill subsequent transactions. Radar for Platforms also charges a connected account fee.

Radar screens all payment attempt types (for example, successful, declined, blocked, and flagged for review) and the following payment method types:

- [Cards](https://docs.stripe.com/payments/cards.md)
- [Wallets](https://docs.stripe.com/payments/wallets.md) (when the underlying payment method is a card)
- [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md)
- [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md)
- (Preview) [Other popular payment methods](https://docs.stripe.com/radar/supported-payment-methods.md)

Radar doesn’t screen SetupIntents for non-card payment methods.

## Features

- [AI-based fraud detection](https://docs.stripe.com/radar/optimize-risk-factors.md): Enable [risk controls](https://docs.stripe.com/radar/risk-settings.md#risk-controls) on your account to automatically identify and block elevated or high-risk payments that are likely to result in fraudulent disputes or early fraud warnings.

- [Custom rules engine](https://docs.stripe.com/radar/rules.md): Create and implement your own fraud prevention rules based on your business needs, and [set up automatic responses](https://docs.stripe.com/radar/risk-settings.md) to specific risk levels.

- [Risk insights](https://docs.stripe.com/radar/reviews/risk-insights.md): Understand the factors driving risk on every payment, and detect suspicious patterns in customer behavior across transactions and location data.

- [Direct 3D Secure integration](https://docs.stripe.com/radar/rules.md#how-to-create-effective-rules): Incorporate additional authentication for high-risk card transactions.

- [Block lists and allow lists](https://docs.stripe.com/radar/lists.md): Manage lists of high-risk or trusted users, email addresses, IP addresses, metadata, and payment methods.

- [Real-time monitoring](https://docs.stripe.com/radar/analytics.md): View and respond to potentially fraudulent activity as it happens.

- (Preview) [Additional payment method fraud controls](https://docs.stripe.com/radar/supported-payment-methods.md), including customizable rules, block and allow lists, and consolidated fraud analytics across your entire payment volume
