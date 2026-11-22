---
title: "Stripe: Check French Meal Vouchers Balances"
type: source
date_ingested: 2026-05-05
date_updated: 2026-11-22
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/checking-a-card-balance"
raw_files:
  - "stripe-payments-meal-vouchers-fr-meal-vouchers-checking-a-card-balance-2026-11-07.md"
  - "stripe-fr-meal-vouchers-check-balance-2025.md"
tags: [stripe, meal-vouchers, france, titres-restaurant, balance-check, split-tender]
---

## Summary

Stripe's May 5 and November 7, 2026 captures describe a pre-payment balance check for Bimpli, Pluxee and Up Déjeuner. Both describe private preview. The November capture adds an email waitlist and a request example. A waitlist submission requests access, with Stripe contacting applicants when it can onboard more users.

## Check the available balance

- **Prerequisites.** Provision the restaurant or store SIRET for French meal voucher acceptance and save the voucher as a PaymentMethod. A voucher saved during an earlier payment is eligible for the documented check.
- **Request.** Both captures show server-side `POST /v1/payment_methods/:id/check_balance` with secret-key authentication. Use the saved PaymentMethod ID, which is distinct from the SIRET and the PaymentIntent IDs. The [[source-stripe-fr-meal-vouchers|overview]] names the endpoint without a verb. The prior overview summary's GET has no support in these captures.
- **Use.** The optional balance lookup can inform checkout display, payment allocation, or a check for sufficient funds before creating a PaymentIntent. It does not place a hold. A concurrent purchase can use the balance and cause authorization to decline.
- **Response.** `payment_method_balance` returns available amounts by benefit and currency under `balance.fr_meal_voucher.available`. `as_of` is when the balance was retrieved. The amount can change immediately thereafter.

```json
{
  "object": "payment_method_balance",
  "as_of": 1750768577,
  "balance": {
    "fr_meal_voucher": {
      "available": [{ "amount": 2500, "currency": "eur" }]
    }
  },
  "livemode": true
}
```

- **Sandbox.** `pm_card_conecs_fr_frMealVoucher` always returns 10.00 EUR in a sandbox. The response above is a separate illustrative live-mode example. Both examples describe the balance check alone.
- **Version and request boundary.** The balance examples show no Stripe version header or PaymentLocation field. The separate [[source-stripe-fr-meal-vouchers-accept-payment|November acceptance guide]] requires `2026-05-27.preview` or later and an active `fr_meal_vouchers_conecs_payments` capability on the PaymentLocation for payment acceptance. Those are documented acceptance prerequisites.

## Split tender considerations

Food eligibility and daily allowances still apply. Ineligible service or delivery fees go to a separate payment method even if voucher funds could cover the whole order. An eligible purchase exceeding the available balance is a separate reason to split payment. The [[source-stripe-fr-meal-vouchers|overview]] describes merchant orchestration through separate payments.

### Written guidance in both captures

Check availability, then use two PaymentIntents when the balance is insufficient, one per payment method. The guides give the following written order:

> Because you can’t refund French meal vouchers, always process the secondary payment method first. Alternatively, use manual capture for French meal vouchers after confirming the secondary payment succeeded.
>
> If any of the payments fail, revert the other payment.

### November 7, 2026 diagram

May points to the diagram. November also captures its text, including these arrows:

```text
[Display the Checkout page] -- User confirmation --> [Create and confirm the Payment Intent for the French meal voucher]
[Create and confirm the Payment Intent for the French meal voucher] -- Payment succeeded --> [Create and confirm the Payment Intent for the secondary payment method]
[Create and confirm the Payment Intent for the secondary payment method] -- Payment failed --> [Revert the French meal vouchers Payment Intent]
```

This is a voucher-first confirmation sequence, while the written guidance puts the secondary payment first or delays voucher capture. The diagram leaves the capture mode, actual payment state and reversal operation unspecified. The overview documents release of an uncaptured voucher authorization and excludes a refund after capture. Treat the voucher-first arrows as a documentation conflict. Separate PaymentIntents require merchant handling of failure and do not establish atomic rollback.

## Related Pages

- [[stripe-fr-meal-vouchers]] — Voucher acceptance, balance checks and split tender
- [[source-stripe-fr-meal-vouchers]] — Issuer scope, eligibility, split tender and the authorization-versus-capture boundary
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — Restaurant or store provisioning
- [[source-stripe-fr-meal-vouchers-save-payment]] — Saving a voucher
- [[source-stripe-fr-meal-vouchers-accept-payment]] — Payment acceptance and the separate preview version and PaymentLocation requirements
- [[stripe]] — Stripe company page

## Raw Sources

- [[raw/stripe-payments-meal-vouchers-fr-meal-vouchers-checking-a-card-balance-2026-11-07]] — 2026-11-07 full webpage capture (118 lines)
- [[raw/stripe-fr-meal-vouchers-check-balance-2025]] — 2026-05-05 full webpage capture (89 lines)
