<!-- Source URL: https://docs.stripe.com/radar/account-risk-signals -->
<!-- Fetched: 2026-05-10 -->

# Account risk signals

Get risk signals for connected account fraud, delinquency, and website legitimacy.

The [Account Signals API](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2026-03-25.preview) provides risk intelligence for your connected accounts, to help you detect and respond to the following risk categories:

- [Fraudulent merchant](https://docs.stripe.com/radar/fraudulent-merchant.md): Detect connected accounts engaging in fraudulent activity, such as misrepresenting goods or services, processing unauthorized transactions, or committing first-party fraud.
- [Merchant delinquency risk](https://docs.stripe.com/radar/merchant-delinquency-risk.md): Identify connected accounts showing financial distress indicators that might lead to unfulfilled orders, increased disputes, or the inability to cover refunds.
- [Fraudulent website](https://docs.stripe.com/radar/fraudulent-website.md): Flag connected accounts operating deceptive or policy-violating websites, including sites with misleading product claims, fake storefronts, or content that doesn’t match the stated business model.

## How it works

Stripe continuously evaluates your connected accounts using machine learning models trained on millions of payments across the Stripe network. When a risk signal changes, Stripe sends a webhook event to your endpoint so you can take action.
A diagram showing the account signals flow between a connected account, Stripe, and a platform. (See full diagram at https://docs.stripe.com/radar/account-risk-signals)

## Signal types

Learn how to use each signal type:

- [Fraudulent merchant signal](https://docs.stripe.com/radar/fraudulent-merchant.md): Detects connected accounts engaging in fraudulent activity using ML models trained on Stripe network data.
- [Merchant delinquency risk signal](https://docs.stripe.com/radar/merchant-delinquency-risk.md): Identifies connected accounts at risk of financial distress that might lead to negative balances.
- [Fraudulent website signal](https://docs.stripe.com/radar/fraudulent-website.md): Evaluates whether a connected account’s website is deceptive or policy-violating using on-demand analysis.

## Take action on connected accounts

You can respond to the risk signals that you receive for a connected account using the following [Radar for Platforms](https://docs.stripe.com/radar/radar-for-platforms.md) tools:

| Action                            | Description                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Raise a review**                | Flag the account for manual investigation by your risk team.                                     |
| **Pause payouts**                 | Hold funds while you investigate to reduce potential losses.                                     |
| **Pause payments**                | Stop the account from processing new transactions.                                               |
| **Reject the account**            | Permanently disable the account if you confirm it’s fraudulent.                                  |
| **Set reserves**                  | Require holding a percentage of each transaction as a buffer against future losses.              |
| **Request identity verification** | Ask the connected account to verify their identity with a government-issued document and selfie. |

Learn more about the [investigation and enforcement workflows](https://docs.stripe.com/radar/radar-for-platforms.md) from Radar for Platforms.
