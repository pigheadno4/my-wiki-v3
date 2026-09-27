---
title: "PayPal v5 to v6: Returning-Buyer Frontend Evidence Gap"
type: analysis
date_created: 2026-09-27
tags: [paypal, javascript-sdk, vault, returning-buyer, migration]
---

## Conclusion

Direct PayPal JS SDK v5 documents a customer-aware saved-PayPal frontend experience. An equivalent direct-PayPal v6 frontend integration was not confirmed in the documentation and package evidence checked on 2026-09-27. Backend payment-token reuse is not evidence of frontend parity.

> [!info] Evolving
> This is a bounded documentation/type-surface gap, not proof that the hosted v6 runtime cannot support the experience. No merchant sandbox or production end-to-end test was performed. Package versions below identify the checked snapshots, not a permanent latest-version claim.

## Capability Boundaries

| Capability | Direct PayPal v5 | Direct PayPal v6 |
| --- | --- | --- |
| Render a recognized buyer's saved PayPal payment option | Documented customer ID to ID-token flow and PayPal button test | Equivalent customer-aware frontend flow not confirmed |
| Save PayPal for future payments | Documented | Save-payment session documented and typed |
| Charge a saved PayPal token through Orders API | Server-side capability | Server-side capability; does not establish SDK-rendered returning-buyer UI |
| Dedicated View/Edit saved funding method flow | Not established by this comparison | Do not substitute Braintree's separately evidenced integration for direct-PayPal support |

## v5: Customer-Aware PayPal Button

The PayPal-wallet-specific guide describes storing the PayPal-generated customer ID, generating an `id_token` server-side with `target_customer_id`, passing it through `data-user-id-token`, and rendering `paypal.Buttons()`. The identifier is not the merchant's own customer ID and is not passed directly as the script attribute.

Its returning-payer test explicitly checks that the PayPal button displays the payer's preferred payment method and can be selected again. This is PayPal-wallet evidence, not an inference from card or Venmo guides. Sources: [[source-paypal-save-payment-methods]] and [retained raw guide](../../raw/paypal-save-paypal-js-sdk.md).

The [current v5 PayPal guide](https://developer.paypal.com/sdk/js/v5/save-with-purchase/paypal), checked on 2026-09-27, corroborates the frontend behavior. It also contains a warning against saving during purchase despite describing that integration; treat this as a documentation inconsistency requiring clarification before selecting a new save-during-purchase design. This note records returning-buyer behavior, not a blanket implementation recommendation.

## v6: Saving Is Not Returning-Buyer Rendering

The checked `@paypal/paypal-js@11.1.1` and `@paypal/react-paypal-js@10.5.1` snapshots at `dfd184b6abc9384d07a95f92db4be517d8c22c86` expose `createPayPalSavePaymentSession`, `PayPalSavePaymentButton`, and `usePayPalSavePaymentSession`. These establish initial saving, not an equivalent customer-aware saved-wallet button or dedicated edit-existing-funding-method wrapper. Package evidence: [[source-github-paypal-js]] and [[changelog-github-paypal-js]].

The [v6 reference](https://developer.paypal.com/sdk/js/reference/) and [v6 save guide](https://developer.paypal.com/sdk/save-without-purchase/paypal/) were checked separately from the [server-side saved-token payment guide](https://developer.paypal.com/checkout/save-customer-info/). The latter uses `payment_source.paypal.vault_id`; it does not establish an SDK-rendered returning-buyer experience. Live documentation checks are external corroboration, not newly collected immutable raw snapshots.

## Braintree Is a Separate Integration

[[source-github-braintree-web]] records Braintree Web `3.146.0` v6 saved-payment editing. Its Braintree client-token/payment-method context and nonce-based processing do not establish an equivalent API for a direct PayPal merchant. Keep that evidence and integration path separate; see [[paypal-braintree-integration]].

## Migration Decision

- Do not mark customer-aware returning-buyer UI as v5/v6 parity solely because v6 can save a wallet or the backend can charge a token.
- For an existing v5 experience, require a documented v6 equivalent and a merchant-specific sandbox test before claiming frontend parity.
- Keep authentication, customer-to-token ownership, merchant eligibility, consent, risk-data collection, and payment finalization separate from UI rendering.
- Revisit this gap when PayPal publishes a direct v6 customer-aware example or corresponding typed/React API. Retain the dated finding rather than rewriting historical evidence.
