---
title: "Place a Hold on a Payment Method"
type: source
date_ingested: 2026-04-22
date_updated: 2026-11-22
original_format: webpage
canonical_url: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method
raw_files:
  - "stripe-payments-place-a-hold-on-a-payment-method-2026-11-07.md"
  - "stripe-auth-and-capture-2025.md"
tags: [stripe, auth-capture, capture-method, manual-capture, payment-intents, checkout-sessions, authorization-window, automatic-delayed]
---

## Summary

The April 22 and November 7, 2026 [[stripe|Stripe]] guides describe authorizing an eligible payment method to reserve funds and capturing them later. The Charge field `payment_method_details.card.capture_before` identifies when that card authorization expires. If a wholly uncaptured authorization expires, the funds are released and the payment changes to `canceled`.

## Authorization Validity Windows

Both captures give these standard card windows.

| Card brand | Card-not-present CIT | Card-not-present MIT | Card-present |
| --- | --- | --- | --- |
| Visa | 7 days | 5 days (exactly 4 days 18 hours) | 5 days (exactly 4 days 18 hours) |
| Mastercard | 7 days | 7 days | 2 days |
| American Express | 7 days | 7 days | 2 days |
| Discover | 7 days | 7 days | 2 days |

Stripe and the network use cardholder participation signals to classify a transaction as customer-initiated (CIT) or merchant-initiated (MIT). For example, a supplied CVC can still result in CIT classification when `off_session=true`. The April guide records that on April 14, 2024, Visa shortened its online MIT window from seven days to five and lengthened its in-person window from two days to five. The November table retains the durations and omits the history note. Eligible online and Terminal authorizations may have extended windows.

### Japan

For accounts based in Japan, both guides document up to 30 days for JPY transactions from Visa, Mastercard, JCB, Diners Club, and Discover. The April text gave a standard seven-day window for non-JPY and American Express transactions. The November guide refers those transactions to the applicable standard window by brand and transaction type. See April lines 18–46 and November lines 19–45.

## Payment method capture windows

| Payment method | Documented window and conditions |
| --- | --- |
| Affirm | Affirm may require a down payment for very large orders. If required, Affirm collects it at authorization and refunds it if the payment is uncaptured. Capture the remaining balance within 30 days. |
| Afterpay / Clearpay | The customer pays the first installment at authorization, and Afterpay refunds it if the payment is never captured. Capture the remaining balance within 13 days. |
| Cash App Pay | Capture within 7 days. |
| Klarna | Capture by midnight of the 28th calendar day after the charge request. |
| PayPal | The hold is 10 days. Stripe automatically attempts to extend it by a further 10 days, and the chosen settlement preference may affect the window. |

ACH Direct Debit and iDEAL do not support separate authorization and capture. See April lines 48–60 and November lines 47–60. The Affirm link moves to the direct API variant in November while the down-payment conditions remain.

## Authorize and capture

- **Dashboard.** Create a one-time payment and select **More options** then **Capture funds later**. The Dashboard shows the payment as **Uncaptured**. Capture from the payment details page.
- **Checkout Sessions.** Create the Session with `payment_intent_data.capture_method=manual` for eligible methods. Use the PaymentIntent ID returned on the Checkout Session when capturing.
- **Payment Intents.** Set `capture_method=manual` on the PaymentIntent to use only eligible methods. To offer methods with differing capture support, set `payment_method_options[card][capture_method]=manual` to place only card payments on hold. Both guides show an automatic payment methods path. The explicit mixed card and SEPA Direct Debit create example uses `payment_method_types` in April and `allowed_payment_method_types` in November. These are guide examples. The [[stripe-payment-intents#Server SDK 23.0.0 Endive Boundary|separate versioned API and SDK evidence]] defines the scoped request-field boundary.
- **Verify authorization.** Attach the method and confirm the direct PaymentIntent to authorize. Successful manual authorization leaves it in `requires_capture`. The customer completing the manual-capture payment flow triggers `payment_intent.amount_capturable_updated`. Inspect `amount_capturable` and the card Charge's `capture_before` for the available amount and deadline.
- **Capture.** The PaymentIntent capture request captures the total authorized amount by default. Use `amount_to_capture` for a partial capture or eligible [[source-stripe-overcapture|online card overcapture]]. Most payments support one capture, and an ordinary partial capture releases the rest. For eligible multicapture, the [[stripe-multicapture|dedicated guide]] describes `final_capture=false` retaining the remainder and the distinct finalization rules.
- **Cancel.** The hold guides route cancellation of an authorization through its PaymentIntent. The separate [[raw/stripe-api-payment-intents-cancel-2026-11-07|November 7 PaymentIntent Cancel API reference]] (lines 5–11) says to directly cancel a Checkout Session-linked PaymentIntent only in `requires_capture`. It directs other cases to Checkout Session expiration.

For API setup, see April lines 73–158 and November lines 73–127. For capture and cancellation, see April lines 160–194 and November lines 129–159.

## Automatic delayed card capture (private preview)

Both guides set the PaymentIntent card option `payment_method_options[card][capture_method]=automatic_delayed`. Stripe describes the default as capture before authorization expires, with a backup trigger about six hours before expiry. Manual capture or cancellation can occur first.

- **April 22, 2026.** The example sets `payment_method_options[card][capture_delay_days]=3` to target three days after a successful authorization.
- **November 7, 2026.** The guide documents `payment_method_options[card][capture_by]`. Its default `auth_expiry` captures before expiration, `end_of_day` uses UTC, and `target_delay` takes a nested `capture_delay` with `days`, `hours`, or both, up to 30 days total. The sample sets `capture_by=target_delay` and `capture_delay[days]=3`.

Both guides prioritize capture before expiry when the authorization window is shorter than the target delay. The November form requests early-access follow-up. The captures establish the options independently as dated preview documentation, with compatibility and account access unverified. See April lines 196–243 and November lines 161–213.

## Related Pages

- [[stripe]] — provider overview
- [[stripe-payment-intents]] and [[source-stripe-payment-intents]] — PaymentIntent states and capture
- [[stripe-checkout]] — Checkout Sessions
- [[stripe-multicapture]] — partial and final capture on eligible payments
- [[source-stripe-extended-authorization]] — eligible online card holds

## Raw Sources

- [[raw/stripe-payments-place-a-hold-on-a-payment-method-2026-11-07]] — November 7, 2026 full hold and capture guide
- [[raw/stripe-auth-and-capture-2025]] — April 22, 2026 full guide, with Visa history and the earlier private preview example
