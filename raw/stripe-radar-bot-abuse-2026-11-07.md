<!-- Source URL: https://docs.stripe.com/radar/bot-abuse -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Bot abuse prevention

Use bot score to detect and prevent bot-driven payments.

Bot abuse occurs when bots attempt payments on your platform, violating your terms of service or bypassing your anti-bot policies. Radar evaluates whether a payment was likely made by a bot.

> Radar Pro includes the bot risk control and the bot score. Use the bot risk control to automatically block bot-driven payments. For more flexibility, use the bot score to write your own rules.

## How bot score works

Stripe Radar assigns a numerical bot score to payments made through [Stripe Checkout](https://docs.stripe.com/payments/checkout.md), [Custom Checkout](https://docs.stripe.com/payments/quickstart.md), [Radar Sessions](https://docs.stripe.com/radar/radar-session.md), or [Web Elements](https://docs.stripe.com/payments/elements.md). The score ranges between 0 and 99, where 0 is the lowest likelihood and 99 is the highest likelihood that a bot made the payment.

A high score indicates that a bot likely made the payment, not that the payment is fraudulent or the bot is malicious. Use the bot score to enforce your anti-scripting or anti-bot policies, instead of as a standalone fraud signal.

## Block payments using bot score

Use the bot score with your policies against scripted or automated payments, such as preventing bots from buying limited-availability inventory.

You can:

- View the bot score in the **Risk scores** section on each payment details page
- Write custom rules on `:bot_score:` to block payments that exceed a threshold you define

## Block payments using bot risk control

Use the bot risk control to automatically block payments made through Stripe Checkout, Custom Checkout, Radar Sessions, or Web Elements that exceed a bot score threshold, without requiring custom rules.

### How bot risk control works

1. Stripe Radar assigns a bot score to payments made through Stripe Checkout, Custom Checkout, Radar Sessions, or Web Elements.
2. Radar blocks payments with a bot score that exceeds the configured threshold.

You can also write your own threshold logic to [block payments using the bot score](https://docs.stripe.com/radar/bot-abuse.md#block-payments-using-bot-score).
