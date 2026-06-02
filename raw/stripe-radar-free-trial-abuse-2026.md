<!-- Source URL: https://docs.stripe.com/radar/free-trial-abuse-prevention -->
<!-- Fetched: 2026-05-10 -->

# Free trial abuse prevention

Detect and block customers likely to abuse free trials.

Free trial abuse can occur when customers exploit free trials to access your product without intending to pay. Common patterns include using prepaid or virtual cards, or repeatedly signing up with the same card across multiple accounts.

Radar provides a free trial abuse control that automatically detects and blocks high-risk trial starts before they convert to subscriptions. You can enable it on the [Risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page in the Dashboard.

## How it works

When a customer starts a free trial, Radar evaluates the payment method they provide and predicts whether their subscription payment will fail when the trial ends. If the risk is high, Radar blocks the trial from starting before the customer can gain access to your product.

To evaluate trial starts, Radar must know which payment method collections represent a free trial. We recommend integrating with [Checkout Sessions](https://docs.stripe.com/payments/checkout.md), which automatically evaluates trial starts with no code changes.

Follow the steps below to set up your integration.

## Enable Radar to detect trial starts

We recommend integrating with [Checkout Sessions](https://docs.stripe.com/payments/checkout.md) in `subscription` mode, which automatically detects trial starts with no code changes required.

If you don’t use Checkout Sessions, Radar can still automatically detect trial starts if you do any of the following to create free trials:

- Set [`subscription_data.trial_period_days`](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_period_days)
- Set [`subscription_data.trial_end`](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-subscription_data-trial_end)
- Use [coupons](https://docs.stripe.com/billing/subscriptions/coupons.md) to create 100% off trials

If you use a different integration path (for example, the [Setup Intents API](https://docs.stripe.com/api/setup_intents.md), [Payment Intents API](https://docs.stripe.com/api/payment_intents.md), or [Subscriptions API](https://docs.stripe.com/api/subscriptions.md)), contact us using the form above. We’ll help you add the metadata you need to enable Radar to detect trial starts.

## Enable the control in the Dashboard

After updating your integration, go to the [Risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page and enable **Free trial abuse**. Before selecting this control, you can review backtesting data to see how the control would have performed on your recent trial starts.

## Monitor trial starts

You can review blocked trial starts on the [Risk controls](https://dashboard.stripe.com/settings/radar/risk-controls) page in the Dashboard.

To query blocked trial starts in [Sigma](https://docs.stripe.com/stripe-data/sigma.md), use the `rule_decisions` table with the `block_if_high_free_trial_abuse_risk` rule ID:

```sql
-- Setup attempts blocked by the free trial abuse control
SELECT *
FROM rule_decisions
WHERE rule_id = 'block_if_high_free_trial_abuse_risk'
```

To view the number of blocked SetupIntents and customers:

```sql
SELECT
  COUNT(DISTINCT setup_intent_id) AS blocked_setup_intents,
  COUNT(DISTINCT customer_id) AS blocked_customers
FROM rule_decisions r
JOIN setup_intents s ON r.setup_intent_id = s.id
WHERE rule_id = 'block_if_high_free_trial_abuse_risk'
```
