---
title: "Stripe Terminal: Saving Payment Details"
type: concept
category: technology
tags: [stripe, stripe-terminal, saved-payment-methods, generated-card, off-session, card-fingerprint, compliance]
---

## Definition

Stripe Terminal can collect payment details in person for future online reuse. Stripe can generate a separate reusable `generated_card` PaymentMethod representing the same card when the payment method and flow support it. Its use for online charges, subscriptions, or off-session payments depends on the saved method’s usage restrictions and the customer’s consent.

## How generated_card Works

1. Complete a Terminal PaymentIntent or SetupIntent with a card-present payment method
2. Stripe can create a `generated_card` PaymentMethod linked to the same underlying card where supported. Check that the generated method exists before reuse.
3. Attach `generated_card` to a `Customer` (v1) or customer-configured `Account` (v2) — **required for reuse**
4. Charge the saved method via the standard PaymentIntents API (online, not Terminal SDK)

**If you attach `generated_card` only to a PaymentIntent without a Customer/Account, it cannot be reused.**

## Two Save Flows

- **Save directly** (without charging): use a SetupIntent to collect and vault card details without an initial payment
- **Save after payment** — Request a reusable `generated_card` as part of a Terminal PaymentIntent that charges the card.

### Save Directly: SetupIntent Flow

**Card networks in the 2026-05-01 SetupIntent guide**. Visa, Mastercard, Amex, Discover, and co-branded Interac, eftpos, and girocard are supported. Co-branded Interac must be inserted into a reader and is unsupported by Tap to Pay. Single-branded Interac, eftpos, and girocard are unsupported.

**`generated_card` is CNP** — Charges via `generated_card` are card-not-present. Card-present liability-shift and pricing benefits do not apply.

**SetupIntent flow in the 2026-05-01 guide**

1. Create or retrieve a `Customer`. The guide separately recommends customer-configured Accounts for most uses of Accounts v2.
2. For server-driven and JavaScript integrations, create the SetupIntent on the server with `card_present` in `payment_method_types`. JavaScript passes the client secret to the client. iOS, Android, and React Native can create through the SDK or retrieve a server-created SetupIntent using its client secret. Use `usage=on_session` for checkout-only reuse.
3. Obtain the customer’s explicit consent before collecting the payment method and confirming the SetupIntent. The collection and confirmation calls depend on the integration and SDK version.

**`allow_redisplay` required** (replaced legacy `customer_consent_collected`):

- `always` — payment method can be shown in any future checkout flow
- `limited` — restricted display (used automatically for saved mobile wallets)
- Mandatory since March 31, 2025 for non-React Native; Sept 30, 2025 for React Native

**Collection and confirmation in the 2026-05-01 guide**

| Integration | Reader models named for this variant | SDK/API path |
| --- | --- | --- |
| Server-driven | BBPOS WisePOS E, Stripe Reader S700/S710 | The `process_setup_intent` endpoint handles both steps |
| JavaScript | Unspecified | Separate `collectSetupIntentPaymentMethod` and `confirmSetupIntent` calls |
| iOS | Unspecified | SDK 5.0.0 combines both steps in `processSetupIntent` |
| Android | Unspecified | SDK 5.0.0 combines both steps in `processSetupIntent` |
| React Native | Unspecified | SDK 0.0.1-beta.29 offers combined `processSetupIntent`. The guide also documents separate collection and confirmation |

See the separate iOS and Android 6.0.0 sections below for the consent and model migrations.

**Retrieving `generated_card`**. Check for the reusable `card` PaymentMethod on the latest SetupAttempt or list the Customer’s attached `card` PaymentMethods. `SetupIntent.payment_method` is a `card_present` PaymentMethod and cannot be charged online. An available `generated_card` automatically attaches to the Customer supplied at SetupIntent creation upon successful setup. Otherwise, attach it to the Customer separately before reuse.

**Mobile wallets**: saved wallets get `allow_redisplay=limited`; must use `off_session=true` when charging; if customer is present in checkout flow, use Apple Pay / Google Pay integrations directly instead.

### Save After Payment: PaymentIntent Flow

The in-person transaction charges the card and requests a reusable payment method. Follow-up `generated_card` charges are card-not-present and do not receive card-present liability-shift or pricing benefits.

**How it works**:

1. Create Customer or Accounts v2 customer-configured Account
2. Create PaymentIntent with `setup_future_usage: 'off_session'` (or `'on_session'`) to request a `generated_card`
3. Collect payment with `allow_redisplay: 'always'` or `'limited'` passed at collect time
4. Retrieve `generated_card` by expanding `latest_charge` → `payment_method_details.card_present.generated_card`; auto-attaches to Customer if Customer ID was provided at PaymentIntent creation

**Server-driven options in the 2026-05-01 guide** — The feature requires `Stripe-Version: 2024-09-30.acacia`. Use `process_payment_intent`, or use Preview `collect_payment_method` to access card brand or funding before separately calling `confirm_payment_intent`.

**SDK minimums**: iOS SDK v4.3.0+, Android SDK v4.0.0+.

**Verify `generated_card`** — Some digital-wallet and single-branded Interac, eftpos or girocard payments might produce none. If a reusable method is needed, ask the customer to use the save-directly flow with a different method, or refund and retry with a different method. The May 2026 guide scopes saved mobile wallet reuse to off-session confirmation with `off_session=true` and `allow_redisplay=limited` on the generated card. Re-prompt through Apple Pay or Google Pay when the customer is present.

## iOS SDK 6.0.0 Consent and Model Migration

`StripeTerminal@6.0.0` makes `allowRedisplay` a required initializer argument to `CollectSetupIntentConfigurationBuilder`, rather than a separate argument to the collection/processing method. Build with a consent-appropriate `.always` or `.limited`, then pass the configuration as `setupConfig` to `collectSetupIntentPaymentMethod` or `collectConfig` to `processSetupIntent`. The example's default `.always` is not evidence of merchant consent; the header requires consent and documents those two permitted values.

In v6, `SetupIntent.paymentMethod` is the expanded PaymentMethod object (formerly `paymentMethodExpanded`), while `paymentMethodId` supplies the ID formerly returned by `paymentMethod`. For save-after-payment retrieval, `PaymentIntent.latestCharge`/`latestChargeId` replace `charges`. PaymentMethod card-present instrument details are now distinct from transaction details on a Charge; do not assume instrument details contain `generatedCard` or receipt fields. These SDK migrations do not remove the existing generated-card, customer-attachment or CNP reuse boundaries. Earlier v5 guidance remains historical. See [[source-github-stripe-terminal-ios]] and [[changelog-github-stripe-terminal-ios]].

## Android SDK 6.0.0 Consent and Models

`stripeterminal@6.0.0` moves `allowRedisplay` into the required `CollectSetupIntentConfiguration`: construct the builder with a consent-appropriate value, then pass `config` to collection or `collectConfig` to processing. The Java/Kotlin demos use `AllowRedisplay.ALWAYS`; they do not collect or prove customer consent. `PaymentIntent.latestCharge`/`latestChargeId` replace `getCharges()`. The release separates `PaymentMethod.CardPresent` instrument data from `Charge.CardPresent` transaction data, makes instrument expiry nullable, and renames SetupAttempt detail types. Do not substitute iOS property names for Android model contracts.

The v6 cumulative changelog also clarifies an older Tap to Pay `generated_card` bug affecting 5.4.0–5.6.0, fixed in 5.7.0. These retrospective notes are not a new v6 fix and do not change the existing CNP/customer-attachment boundaries. See [[source-github-stripe-terminal-android]] and [[changelog-github-stripe-terminal-android]].

## Charging a Saved PaymentMethod

- Set `off_session: true` when charging outside the checkout flow — causes PaymentIntent to error if customer authentication is required
- **Terminal SDK methods cannot process `generated_card` payments** — these are online payments processed via the Stripe API directly

```javascript
// Accounts v2
const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['card'],
  amount: 1099,
  currency: 'sgd',
  customer_account: '{{CUSTOMER_ACCOUNT_ID}}',
  payment_method: '{{PAYMENT_METHOD_ID}}',
});

// Customers v1
const paymentIntent = await stripe.paymentIntents.create({
  payment_method_types: ['card'],
  amount: 1099,
  currency: 'sgd',
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{PAYMENT_METHOD_ID}}',
});
```

## Card Fingerprints

`card_present` PaymentMethods have a `fingerprint` attribute — same as `card` PaymentMethods — uniquely identifying the card number. Use to correlate in-person and online transactions by the same customer.

- **Mobile wallets** (Apple Pay, Google Pay): fingerprint differs from the underlying card's online fingerprint
- **Connect**: since API v2018-01-23, fingerprints are uniform across all connected accounts — usable for cross-account card lookups

## Compliance

When saving card details in-person, merchants must:

- State in checkout terms how payment details will be saved and allow customer opt-in
- For off-session charging, terms must cover: payment initiation authority, timing/frequency, amount determination, and cancellation policy (for subscriptions)
- Keep written records of customer agreement
- Only use saved methods for the purpose stated in terms
- If combining off-session charging with saving for future checkout display: collect explicit consent (e.g., checkbox)

## Sources

- [[source-stripe-terminal-save-payment-details]] — overview: generated_card mechanism, off-session, fingerprints, compliance
- [[source-stripe-terminal-save-directly]] — SetupIntent guide captured 2026-05-01, with the 2026-11-07 platform variant index linked for navigation.
- [[source-stripe-terminal-js-sdk-reference]] — JavaScript SDK SetupIntent methods and the separate `readReusableCard()` warning
- [[source-stripe-terminal-save-after-payment]] — Save after payment: setup_future_usage, allow_redisplay at collect time, generated_card retrieval, fallback when absent, SDK notes
