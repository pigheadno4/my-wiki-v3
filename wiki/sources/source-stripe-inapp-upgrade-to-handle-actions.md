---
title: "Migrate Basic Card Integration to Handle Bank Authentication — Mobile"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-inapp-upgrade-to-handle-actions-2025.md"
tags: [stripe, mobile, ios, android, react-native, card-payments, requires-action, handle-next-action, confirmation-method-manual, migration]
---

## Summary

Upgrade guide from the legacy `error_on_requires_action` integration to one that handles 2FA bank requests. Triggered when seeing `requires_action_not_handled` errors or many `Failed` payments in Dashboard. Covers iOS, Android, and React Native.

> Pairs with [[source-stripe-inapp-without-card-auth]] (what you're upgrading from).

## 3 Server Changes

1. **Remove** `error_on_requires_action`
2. **Add** `confirmation_method: 'manual'` — enables explicit server re-confirmation
3. **Add** `use_stripe_sdk: true` — enables mobile client to handle additional auth steps

```javascript
stripe.paymentIntents.create({
    amount: 1099, currency: 'usd',
    confirm: true,
    payment_method: pmId,
    confirmation_method: 'manual',  // NEW
    use_stripe_sdk: true,            // NEW
    // NO error_on_requires_action
})
```

## New Server Response States

```javascript
function generateResponse(response, intent) {
    if (intent.status === 'succeeded') {
        return response.send({ success: true });
    } else if (intent.status === 'requires_action') {
        return response.send({ requiresAction: true, clientSecret: intent.client_secret });
    }
    // other = error
}
```

## Two-Round-Trip Pattern

1. Client POSTs `payment_method_id` → server creates+confirms PI
2. If `requiresAction`: client shows auth modal
3. Client POSTs `payment_intent_id` → server re-confirms: `paymentIntents.confirm(payment_intent_id)`
4. If `requires_action` again: loop

**Confirm window**: must re-confirm within **1 hour** or PI reverts to `requires_payment_method`.

## Platform Client Code

### iOS (Objective-C)
```objc
STPPaymentHandler *handler = [STPPaymentHandler sharedHandler];
[handler handleNextActionForPayment:clientSecret
         withAuthenticationContext:self
                         returnURL:nil
                        completion:^(status, paymentIntent, error) {
    // STPPaymentHandlerActionStatusSucceeded → send PI ID to server to re-confirm
}];
// Must implement STPAuthenticationContext
```

### Android (Java)
```java
stripe.handleNextActionForPayment(activity, clientSecret);
// Result via onActivityResult → stripe.onPaymentResult(requestCode, data, callback)
// callback.onSuccess(result) → result.getOutcome() == SUCCEEDED → re-confirm
```

### React Native
```javascript
const { handleCardAction } = useStripe();
const { error, paymentIntent } = await handleCardAction(clientSecret);
// success → POST { payment_intent_id: paymentIntent.id } to server
```

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[source-stripe-inapp-without-card-auth]] — the integration this guide upgrades from

## Raw Sources

- [[stripe-inapp-upgrade-to-handle-actions-2025]] — verbatim migration guide (~563 lines, iOS + Android + React Native, 1 image × 3)
