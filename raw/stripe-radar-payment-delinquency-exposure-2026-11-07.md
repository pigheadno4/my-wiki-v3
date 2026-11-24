<!-- Source URL: https://docs.stripe.com/radar/payment-delinquency-exposure -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Payment delinquency exposure

Estimate the dollar amount at risk if a connected account becomes delinquent.

The payment delinquency exposure signal estimates the financial exposure if a connected account becomes delinquent. It quantifies the dollar amount at risk from disputes and refunds in the event of a business credit delinquency.

### Get early access to the payment delinquency exposure signal.

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/radar/payment-delinquency-exposure" \
  -d '{"email": "EMAIL", "preview": "merchant_risk_tooling_beta_preview"}'
```

## Retrieve exposure signals

Use the [Account Signals API](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=2026-07-29.preview) to retrieve the exposure signal for a connected account. The response includes the estimated exposure amount and additional details about how it was calculated.

## How Stripe calculates exposure 

The Stripe exposure model estimates the dollar-at-risk using concepts borrowed from financial credit models. The formula is:

`Payment delinquency exposure = Gross exposure × Loss given default`

The signal returns the final estimate in the `exposure_amount` field. The components that feed into it are available in `additional_details`.

### Gross exposure

Gross exposure (`additional_details.gross_exposure_amount`) is the total trailing payment volume still at risk of a dispute or refund. It’s calculated as:

`Gross exposure = Trailing payment volume × Predicted dispute window distribution`

### Predicted dispute window

The predicted dispute window (`additional_details.predicted_dispute_window_in_days`) is the estimated number of days between a charge and a potential dispute:

`Predicted dispute window = Dispute date − Charge date`

Stripe uses historical dispute data to calculate the predicted dispute window distribution for each business and applies that distribution as weights to trailing processing volume when aggregating to gross exposure.

### Loss given default

Loss given default (`additional_details.loss_given_default_in_percentages`) is the percentage of gross exposure that’s expected to actually be disputed or refunded and materialize as a loss in the event of delinquency, given as a value between 0% and 100%:

`Loss given default = % of Gross exposure that turns into a loss`

## Webhook event 

Listen for `v2.signals.account_signal.payment_delinquency_exposure_ready` event notifications when an exposure signal is evaluated.

## Take action on connected accounts

After you receive an exposure signal, use the available [Radar](https://docs.stripe.com/radar.md) tools to take action on your connected accounts. See the list of [available actions](https://docs.stripe.com/radar/account-fraud-prevention.md#take-action).
