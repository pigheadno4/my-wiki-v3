---
title: "France Titres-Restaurant / Meal Vouchers (Stripe)"
type: concept
category: technology
tags: [stripe, meal-vouchers, france, titres-restaurant, benefits, siret, split-tender]
---

## Definition

France titres-restaurant (meal vouchers) is a Stripe payment method in **private preview** for French businesses serving prepared food. Employers provide these as prepaid cards with a daily refreshed balance used to purchase food and beverages on working days.

## Key Properties

| Property | Value |
| --- | --- |
| Customer locations | France only |
| Presentment currency | EUR |
| Payment method family | Cards |
| Recurring payments | No |
| Manual capture | Yes |
| Refunds | No |
| Disputes | No (Bimpli, Pluxee, Up Déjeuner) |
| Payout timing | Controlled by issuer (off-Stripe) |
| Connect | Yes (partial — contact Stripe) |

## Issuers

- **Bimpli** (formerly Apetiz)
- **Pluxee** (formerly Sodexo)
- **Up Déjeuner**
- **Swile** — processed via Mastercard network; different rules apply; integration changes in this doc don't apply to Swile

## Requirements

1. **CNTR approval**: obtain approval from the [Commission Nationale des Titres-Restaurant](https://www.cntr.fr/) — per branch, not per company.
2. **Issuer agreements**: commercial acceptance agreement with at least one Stripe-supported issuer.
3. **SIRET provisioning**: Dashboard → French meal vouchers SIRETs → Add SIRET (SIRET + postal code + store name — all must match CNTR record). Takes **1–2 business days**. SIRET and name are **immutable** after creation. Postal code mismatch → `Requires Action`; fix via Update Details (another 1–2 days). Connect: go to connected account → Configure SIRETs.

Eligible businesses: restaurants, grocers, canteens, food-serving businesses.

## Settlement

Issuers pay acceptors directly per French law — **off-Stripe**. Stripe deducts a processing fee as a **negative BalanceTransaction**. Settlement bank account setup handled directly with each issuer.

## No Refunds or Disputes

No refunds after capture. No dispute system for Bimpli, Pluxee, Up Déjeuner. Use **auth+capture with release** for unfulfillable orders (e.g., order-and-pickup, orders past closure).

## Integration

Opt in per PaymentIntent by passing a pre-provisioned `siret`:

```text
payment_details.benefit.fr_meal_voucher.siret = SIRET_VALUE
```

**Identify via** `paymentMethod.card.benefits` hash:

- `benefits.programs = 'fr_meal_voucher'`
- `benefits.issuer` = issuer name (e.g., `pluxee`)

**Daily balance cap**: 25 EUR, resets at midnight French local time.

**Check balance**: `POST /v1/payment_methods/:id/check_balance` — non-binding (doesn't hold funds). Response: `balance.fr_meal_voucher.available[0].amount` + `as_of` timestamp. Test card: `pm_card_conecs_fr_frMealVoucher` (returns 10.00 EUR in sandbox).

**Split tender order**: charge secondary payment method first (no refunds on meal vouchers); or use auth+capture for the meal voucher after secondary succeeds.

**Split tender**: Stripe doesn't natively support split tender. Orchestrate manually: create separate PaymentIntents for the meal-voucher portion and for ancillary/overage amounts charged to another payment method.

**Save for future use**: CVC required on first payment; reusable without CVC after that. To save without charging: `stripe.setupIntents.create({ customer, setup_details: { benefit: { fr_meal_voucher: { siret } } } })`. Temporary **0.30 EUR auth charge** may appear when saving — reversed almost immediately (restored to daily balance).

**Test data**: card `4000002501000002` (Bimpli with Conecs). Test SIRETs: `42424242424242` (valid), `00000000000000` (invalid).

## Connect

Supported charge types: **platform charges** and **direct charges** only. Destination charges and separate charges + transfers are unsupported because funds settle outside Stripe.

- **Direct charges**: add `Stripe-Account` header; rest of integration unchanged.
- **Platform charges**: create PaymentIntent on platform account; omit `transfer_data`, `application_fee_amount`, `transfer_group`; pass `siret`.
- **Fee collection**: after capture, create `v1/transfers` from connected account to platform. Refund via transfer reversal.
- **SIRET provisioned on**: the merchant of record.

## Sources

- [[source-stripe-fr-meal-vouchers]] — overview: issuers, CNTR requirements, SIRET provisioning, settlement model, no refunds, balance cap, split tender
- [[source-stripe-fr-meal-vouchers-accept-payment]] — integration: PaymentIntent + SIRET API, CVC save requirement, test card + test SIRETs
- [[source-stripe-fr-meal-vouchers-connect]] — Connect: supported charge types (platform/direct only), fee collection via transfers, ConfirmationToken identification
- [[source-stripe-fr-meal-vouchers-check-balance]] — balance check API, response structure, non-binding nature, test card, split tender ordering
- [[source-stripe-fr-meal-vouchers-save-payment]] — SetupIntent save API, 0.30 EUR temp auth charge, on-session reuse with saved card
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — SIRET provisioning flow, postal code matching, immutability, Connect path, test SIRET table
