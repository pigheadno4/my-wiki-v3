<!-- Source URL: https://docs.stripe.com/radar/bot-abuse-prevention -->
<!-- Fetched: 2026-05-10 -->

# Bot abuse prevention

Use bot score to detect and prevent bot-driven payments.

Bot abuse occurs when bots attempt payments on your platform, violating your terms of service or bypassing your anti-bot policies. Radar evaluates whether a payment was likely made by a bot.

## How bot score works

Stripe Radar assigns payments made on [Stripe Checkout](https://stripe.com/payments/checkout) a numerical bot score between 0 and 99, where 0 is the lowest likelihood and 99 is the highest likelihood that a bot made the payment.

A high score indicates that a bot likely made the payment, not that the payment is fraudulent or the bot is malicious. Use the bot score to enforce your anti-scripting or anti-bot policies, instead of as a standalone fraud signal.

## Block payments using bot score

Use the bot score with your policies against scripted or automated payments, such as preventing bots from buying limited-availability inventory.

You can:

- View the bot score in the **Risk scores** section on each payment details page
- Query for `bot_score` under the `radar_abuse_prevention_attributes` table in [Sigma](https://stripe.com/sigma)
- Write custom rules on `:bot_score:` to block payments that exceed a threshold you define
