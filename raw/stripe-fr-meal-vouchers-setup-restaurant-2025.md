<!-- Source URL: https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/set-up-restaurant -->
<!-- Fetched: 2026-05-05 -->

# Set up a restaurant for titres-restaurant payments

Learn how to onboard a restaurant or store to accept Bimpli, Pluxee, and Up Déjeuner French meal vouchers payments.

> #### Want to accept France titres-restaurant payments?
>
> France titres-restaurant is in private preview. >

Meal vouchers in France require a restaurant to complete an onboarding process before it can [accept French meal vouchers payments](https://docs.stripe.com/payments/meal-vouchers/fr-meal-vouchers/accept-a-payment.md). This guide shows how to onboard a restaurant using the Stripe Dashboard.

Before you set up a restaurant on Stripe, you must obtain a license from [Commission Nationale des Titres-Restaurant](https://www.cntr.fr/) (CNTR) and contract with each of the French meal vouchers issuers you want to support.

> Stripe currently only supports Bimpli, Pluxee, and Up Déjeuner French meal vouchers.

> The Stripe API for onboarding restaurants to accept French meal vouchers payments is in preview and is only available for select preview users. Contact us at fr-meal-voucher-beta@stripe.com to join the preview and use the API.

## Onboard the restaurant

#### Dashboard

1. Go to the [French meal vouchers SIRETs page](https://dashboard.stripe.com/settings/payment_methods/fr_meal_vouchers_sirets).
1. Click **Add SIRET**.
1. Enter a SIRET, postal code, and store name. The SIRET and postal code you provide must match for the restaurant to be onboarded successfully.
1. Click **Confirm**.

The SIRET is a French tax identifier used with the postal code to find the restaurant’s license.

After you submit your onboarding request, it takes 1–2 business days to validate your details and confirm the issuers you can accept payments from.

You can’t modify the restaurant’s name and SIRET after creation.

## Confirm the restaurant is onboarded

Before you begin processing French meal vouchers payments, confirm the restaurant has been successfully onboarded.

#### Dashboard

1. Go to the [French meal vouchers SIRETs page](https://dashboard.stripe.com/settings/payment_methods/fr_meal_vouchers_sirets).
1. Click the restaurant.

You can see the restaurant’s status and the supported card issuers.

## Check supported issuers

#### Dashboard

1. Go to the [French meal vouchers SIRETs page](https://dashboard.stripe.com/settings/payment_methods/fr_meal_vouchers_sirets).
1. Click the restaurant. The open drawer shows the status for each issuer.

## Optional: Handle errors and changes to onboarding status

In some cases a restaurant’s onboarding attempt might not be successful, or a previously onboarded restaurant’s status changes.

## Invalid postal code

The restaurant’s postal code must match the SIRET licensed with CNTR. The onboarding process for a restaurant might fail if you provide an incorrect postal code.

#### Dashboard

1. Go to the [French meal vouchers SIRETs page](https://dashboard.stripe.com/settings/payment_methods/fr_meal_vouchers_sirets).
1. Click the restaurant marked `Requires Action`.
1. Click **Update Details**.
1. Enter the correct postal code.
1. Click **Confirm**.

After you update the postal code, the restaurant’s status updates within 1–2 business days.

## Set up a restaurant with Connect

#### Dashboard

1. Go to the [Connected Accounts page](https://dashboard.stripe.com/connect/accounts).
1. Click the account to set up a restaurant for.
1. Click **Payment methods**.
1. Click **French Meal Voucher Conecs**.
1. Click **Configure SIRETs** in the open drawer.

You can use the open French meal vouchers SIRETs page for the current connected account to set up and manage restaurants for this connected account.

## Test your integration

You can use the following SIRETs and associated postal codes to test your integration:

| SIRET            | Postal code                        | Scenario                                         |
| ---------------- | ---------------------------------- | ------------------------------------------------ |
| `42424242424242` | `42424`                            | A valid onboarded restaurant                     |
| `11111111111111` | `11111`                            | Awaiting an onboarding outcome                   |
| `42424242424242` | Any postal code other than `42424` | Postal code doesn’t match the restaurant’s SIRET |
