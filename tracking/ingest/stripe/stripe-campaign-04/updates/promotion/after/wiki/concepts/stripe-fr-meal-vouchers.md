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
3. **SIRET provisioning.** The May and November overviews estimate 1–3 business days. In the November Dashboard guide, add the branch’s SIRET, postal code matching its CNTR record, and store name. The Dashboard validation estimate is 1–2 business days. Name and SIRET are immutable in the Dashboard after creation. For a postal mismatch, open the restaurant marked `Requires Action`, select **Update Details**, enter the corrected postal code, and confirm. The Dashboard guide describes another 1–2 business days. For Connect, open **Configure SIRETs** under the connected account’s **Payment methods**. The November Dashboard drawer shows the Payment Location ID after successful onboarding. The separate November preview API guide estimates 1–2 business days for pending onboarding. Create the location and request its capability on behalf of the merchant of record. The API blocks onboarding-sensitive edits by default. Acknowledging a SIRET or address edit with `onboarding_data_update_acknowledged=true` returns the capability to `pending` and pauses voucher acceptance until it becomes active again. See [[source-stripe-fr-meal-vouchers-setup-restaurant]] and [[source-stripe-fr-meal-vouchers-connect]].

Eligible businesses generally include restaurants, grocers, canteens and other businesses serving prepared food.

In the November Dashboard guide, enter SIRET, postal code and store name. The SIRET and postal code must match. The name and SIRET cannot be changed after creation in this UI. A postal-code mismatch can use the `Requires Action` and Update Details flow. Conecs rejection can show `Ineligible` for a nonexistent SIRET, missing CNTR approval or revoked approval. A wrong SIRET requires a new Dashboard request, while a correct SIRET awaiting CNTR registration automatically resumes after Conecs processes it. The November API's specific nonexistent or unapproved SIRET example shows a pending capability with `business_registration.siret` currently due. There, correct a wrong SIRET on the existing location. After activation, onboarding-sensitive changes require `onboarding_data_update_acknowledged=true` and pause voucher acceptance during re-onboarding. See [[source-stripe-fr-meal-vouchers-setup-restaurant]].

## Settlement

Issuers pay acceptors directly per French law — **off-Stripe**. Stripe deducts a processing fee as a **negative BalanceTransaction**. Settlement bank account setup handled directly with each issuer.

## No Refunds or Disputes

Captured vouchers cannot be refunded. Bimpli, Pluxee and Up Déjeuner have no dispute system. Separate authorization from capture for orders that may be unfulfillable, so the uncaptured voucher authorization can be released. See the [[source-stripe-fr-meal-vouchers-check-balance#November 7, 2026 diagram|split-tender diagram warning]] for the unresolved voucher state behind its revert arrow.

## Integration

**PaymentIntent.** The May acceptance and Connect guides and the May and November product overviews describe a pre-provisioned literal `payment_details.benefit.fr_meal_voucher.siret`. The separate November acceptance and Connect preview guides use a Payment Location with an active voucher capability, `payment_details[location]` and `payment_details[benefit][fr_meal_voucher][enabled]=if_payment_method_is_eligible` in their `2026-05-27.preview` examples. Stripe resolves the location’s stored SIRET at confirmation. Changes before confirmation can apply, and already-confirmed payments retain the SIRET used. Both overviews say Stripe does not retry failures between voucher and ordinary card routes. See [[source-stripe-fr-meal-vouchers-accept-payment]] for the separate preview request and optional Charge lookup.

**Identification.** The May Connect and the two product-overview examples show scalar `PaymentMethod.card.benefits.programs` and use the corresponding issuer field. The November Connect example shows an array in the PaymentMethod and a scalar at `ConfirmationToken.payment_method_preview.card.benefits.programs`. These dated object examples leave general response shape and actual payment eligibility undetermined. See [[source-stripe-fr-meal-vouchers-connect]].

**Daily balance cap**: 25 EUR, resets at midnight French local time.

**Check balance**: The [[source-stripe-fr-meal-vouchers-check-balance|dedicated guide]] documents optional server-side `POST /v1/payment_methods/:id/check_balance` on a saved PaymentMethod. The response contains `balance.fr_meal_voucher.available` amounts by currency and an `as_of` retrieval timestamp. The check places no hold. The `pm_card_conecs_fr_frMealVoucher` fixture returns 10.00 EUR in a sandbox.

**Split tender order.** The May and November 2026 written guidance puts the secondary method first or defers manual voucher capture until the secondary leg succeeds. The [[source-stripe-fr-meal-vouchers-check-balance#November 7, 2026 diagram|November diagram]] instead confirms the voucher first and shows a revert arrow on secondary failure. It leaves voucher capture mode and reversible state unspecified. The overview allows release of an uncaptured voucher authorization. Captured vouchers cannot be refunded. A prior balance lookup does not reserve funds against concurrent spending.

**Split tender.** The merchant orchestrates separate PaymentIntents for the voucher and secondary payment method. The secondary method covers ineligible fees or an eligible amount above the voucher's available balance.

**Saving without a purchase.** The May SetupIntent example uses the provisioned SIRET in `setup_details.benefit.fr_meal_voucher.siret`. The [[source-stripe-fr-meal-vouchers-save-payment|November save guide]] uses `2026-05-27.preview` or later, an active location capability, `setup_details[location]` and `setup_details[benefit][fr_meal_voucher][enabled]=if_payment_method_is_eligible`. Call `stripe.confirmSetup` with Payment Element and verify the SetupIntent succeeded. A later on-session PaymentIntent uses the Customer and saved PaymentMethod IDs and its separate `payment_details`. Both save guides describe a temporary €0.30 verification authorization that may appear on the customer’s statement. Stripe reverses it almost immediately and restores the daily balance.

The May [[source-stripe-fr-meal-vouchers-accept-payment|acceptance guide]] describes first-payment CVC and later reuse without CVC when saving during payment.

**Test data.** Both acceptance captures use the Bimpli with Conecs sandbox card `4000002501000002`. The May direct-SIRET examples use `42424242424242` as provisioned and `00000000000000` as invalid. The November acceptance and save guides use the onboarded `loc_` Payment Location ID from the same sandbox as the payment or setup. The preview location API supplies separate SIRET and postal-code fixtures for simulated onboarding. See [[source-stripe-fr-meal-vouchers-accept-payment]] and [[source-stripe-fr-meal-vouchers-save-payment]].

## Connect

Supported charge types: **platform charges** and **direct charges** only. Destination charges and separate charges + transfers are unsupported because funds settle outside Stripe.

- **Direct charges**: Use the connected account's `Stripe-Account` header. The November preview uses `payment_details.location` and `if_payment_method_is_eligible`.
- **Platform charges**: Create the PaymentIntent on the platform. Omit `transfer_data`, `application_fee_amount` and `transfer_group`. The May 5 Connect example passes the branch’s literal `payment_details.benefit.fr_meal_voucher.siret`. November’s `2026-05-27.preview` path uses a Payment Location and conditional benefit and retains `on_behalf_of` in its examples. The separate setup API discusses destination-charge merchant-of-record onboarding. The Connect payment matrix excludes voucher destination charges.
- **Fees and settlement**: The issuer settles with the connected account outside Stripe. Stripe debits platform processing fees separately. After capture, the platform can collect its application fee through the documented connected-account balance debit, subject to Account Debits requirements. A transfer reversal returns that application fee only.
- **Merchant of record**: May provisions the literal SIRET. The November preview provisions the Payment Location and requests its capability on behalf of the merchant of record. Accept vouchers after the capability becomes active. See [[source-stripe-fr-meal-vouchers-connect]].

## Sources

- [[source-stripe-fr-meal-vouchers]] — overview: issuers, CNTR requirements, SIRET provisioning, settlement model, no refunds, balance cap, split tender
- [[source-stripe-fr-meal-vouchers-accept-payment]] — May and November 2026 Payment Element acceptance guides covering the dated SIRET and preview PaymentLocation paths, confirmation-time lookup and same-sandbox testing.
- [[source-stripe-fr-meal-vouchers-connect]] — May 2026 literal SIRET and November 2026 Payment Location preview (`2026-05-27.preview` or later). Dated classifier shapes, direct and platform charge scope, per-location activation, and application-fee transfer separate from issuer settlement.
- [[source-stripe-fr-meal-vouchers-check-balance]] — optional POST on a saved voucher, balance snapshot and sandbox fixture, and the November conflict between split-tender prose and diagram
- [[source-stripe-fr-meal-vouchers-save-payment]] — dated SetupIntent request shapes, November preview Payment Location and capability, setup status check, temporary verification, and later on-session reuse
- [[source-stripe-fr-meal-vouchers-setup-restaurant]] — dated Dashboard onboarding, postal and SIRET remediation, distinct preview API capability states, and handoff from branch SIRET to the November Payment Location ID. Verify the location capability is active before the location-based acceptance flow.
