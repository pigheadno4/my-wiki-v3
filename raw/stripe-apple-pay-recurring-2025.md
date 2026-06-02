<!-- Source URL: https://docs.stripe.com/apple-pay/apple-pay-recurring -->
<!-- Fetched: 2026-05-07 -->

# Manage recurring payments on Apple Pay

Improve authorization rates for recurring Apple Pay transactions.

## Checkout and Elements best practices

[Checkout](https://docs.stripe.com/payments/checkout.md) and [Elements](https://docs.stripe.com/payments/elements.md) automatically apply the best practices recommended in this guide.

## How recurring Apple Pay payments work

To make recurring payments, some businesses need to save the Apple Pay payment method on file when a user is on-session then make the recurring payments later when the user is off-session. The first on-session payment is often called a customer initiated transaction (CIT), and the later recurring payments are often called merchant initiated transactions (MIT). Two examples of recurring payments (or MIT) are:

- Subscriptions where users get billed on a fixed frequency.
- Recurring off-session payments where the billing frequency is inconsistent, or where customers can vary the frequency.

When users interact with the Apple Pay payment sheet, to keep the PAN (the original card number) private, Apple Pay processes a card PAN and generates a Device Primary Account Number (DPAN) or [Merchant Token](https://developer.apple.com/apple-pay/merchant-tokens/) (MPAN) depending on the device OS version and integration. DPANs are tied to the specific Apple device, and can be unintentionally deactivated if a user switches to a new device (for example, an iPhone or an iPad) and adds the same card on it. MPAN is the newly introduced more reliable option for recurring payments. MPANs aren’t deactivated when users switch their devices, and comes with better visibility and lifecycle management features.

Beyond these differences, MPAN and DPAN behave similarly.

## Expired cryptogram can cause authorization failures

When a DPAN (or an MPAN) generates, it also comes with an expiring one-time use cryptogram. Stripe needs to conduct the CIT and send both the DPAN (or MPAN) and cryptogram to the authorization network as soon as possible before the cryptogram expires. This expiration mechanism adds a layer of security to Apple Pay Wallets, but failing to trigger the CIT in time is often the root cause of authorization failures.

When the first CIT using the cryptogram fails, subsequent MITs using the same [Card](https://docs.stripe.com/api/cards/object.md) will likely also fail because they’re internally linked to the CIT. These recurring payment failures lead to the low authorization success rate.

## Improve authorization for your API integration

To implement recurring Apple Pay transactions using the API:

1. Save the DPAN (or MPAN) and cryptogram in a `Card`.
1. Initiate a CIT to consume the cryptogram before its expiration. [Use a SetupIntent](https://docs.stripe.com/apple-pay/apple-pay-recurring.md#create-setup-intent) to send a 0 USD validation or a charge transaction to the authorization network, and keep a record of the returned network transaction.
1. Reuse the payment method for future off-session MITs. Stripe sends the DPAN (or MPAN) and the network transaction ID of the original CIT to the authorization network to improve authorization rate.

Consume cryptograms as soon as they’re created using the following recommendations.

### Use subscriptions for free trials

When a customer signs up for a free trial, they’re not charged until the free trial period ends. To make sure you consume the DPAN (or MPAN) cryptogram before it expires, use [Stripe Subscriptions](https://docs.stripe.com/subscriptions.md). The Subscription creates a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) that generates a 0 USD validation with the authorization network. This acts as the CIT, consuming the cryptogram immediately, rather than delaying the first transaction until after the free trial, when the cryptogram has expired.

You can also [create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md) directly to save the [Apple Pay PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-wallet-apple_pay) for future usage. SetupIntent confirmation initiates the same CIT 0 USD validation to consume the cryptogram. Then you can use the authorized [Apple Pay PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md#payment_method_object-card-wallet-apple_pay) to create a Subscription later.

### Create a SetupIntent for Tokens API integrations (Legacy)

We discourage using the legacy Tokens and Charges APIs for recurring Apple Pay payments. It causes the cryptogram expiration authorization failure described in this document. The Tokens API doesn’t trigger the authorization request in time to consume the cryptogram. Additionally, the Charges API doesn’t support the following features, many of which are required for credit card compliance:

- Businesses in India
- Bank requests for card authentication
- Strong Customer Authentication

**For these reasons, we recommend migrating to the PaymentIntents and the SetupIntents APIs.**

If you’re using the legacy [Tokens](https://docs.stripe.com/api/tokens.md) to create an Apple Pay payment token and then calling [Charges](https://docs.stripe.com/api/charges.md) later to charge the user when the trial ends, you can improve your authorization rate following these steps.

1. Create a Payment Method immediately after you create the token.

   #### curl

   ```bash
   curl https://api.stripe.com/v1/payment_method \
     -u <<YOUR_SECRET_KEY>>: \
     -d "type"="card" \
     -d "card[token]"="tok_123"
   ```

1. Immediately create a [SetupIntent](https://docs.stripe.com/api/setup_intents.md) with the new PaymentMethod to perform a 0 USD validation transaction.

Completing these two steps performs the CIT and sends the cryptogram to the network for authorization before it expires. If you’re using Stripe.js, you can combine these steps by calling [stripe.confirmCardSetup with token](https://docs.stripe.com/js/setup_intents/confirm_card_setup#stripe_confirm_card_setup-token).

You can now make off-session MIT payments using the saved Apple Pay payment method. If you’re using PaymentIntents, set [off_session=true](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to indicate that the customer isn’t in your checkout flow.

### Set up off-session payments

If you’re setting up deferred off-session Apple Pay payments and aiming to collect payment information for future off-session uses, such as a hotel reservation, see Apple Pay’s [list of supported payment types](https://developer.apple.com/apple-pay/planning/).

Apple Pay supports [usage=off_session](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) payments using DPANs (or MPANs) when the customer is outside of the checkout flow. However, they have a slightly higher risk because they don’t get a liability shift from the network and might get lower authorization rates than average.

> #### Saved payments restriction
>
> Apple Pay terms forbid using a saved payment method for [usage=on_session](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-usage) payments. If the customer is in the flow, you’re required to have them authorize and generate a new cryptogram for that transaction.

Apple Pay supports incremental authorizations only when you increase the amount of an authorized charge before capturing it.

You can initiate a CIT for your Tokens API integration in either of the following ways:

- [Create a SetupIntent](https://docs.stripe.com/api/setup_intents/create.md) as described in the free trial scenario to initiate a 0 USD validation that creates a reusable DPAN (or MPAN) based payment method for off-session payments.
- Create a PaymentIntent with [setup_future_usage=off_session](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-setup_future_usage).

You can now make off-session MIT payments using the saved payment method. If you’re using PaymentIntents, set [off_session=true](https://docs.stripe.com/api/payment_intents/confirm.md#confirm_payment_intent-off_session) to indicate that the customer isn’t in your checkout flow.
