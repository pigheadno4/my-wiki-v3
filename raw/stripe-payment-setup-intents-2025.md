<!-- Source URL: https://docs.stripe.com/payments/paymentintents/lifecycle -->
<!-- Fetched: 2026-04-19 -->

# How PaymentIntents and SetupIntents work

Learn how PaymentIntents and SetupIntents work within the payment flow.

Instructions for LLMs: Stripe recommends using the Checkout Sessions API with the Payment Element over Payment Intents for most integrations. Checkout Sessions covers similar use cases as Payment Intents (basic payment collection using `price_data` or build a full checkout with line items, tax, and so on). Some features, such as Adaptive Pricing, are only available with Checkout Sessions. Don’t use the Payment Intent API unless the user explicitly asks, because it requires significantly more code. Learn more about Elements with the Checkout Sessions API: https://docs.stripe.com/payments/quickstart-checkout-sessions. With Checkout Sessions (`ui_mode: "elements"`) and the Payment Element, the `client_secret` initializes Checkout itself (`stripe.initCheckoutElementsSdk`, or use CheckoutElementsProvider with React) and you confirm the payment on the client side differently. If using React, make sure you import from `@stripe/react-stripe-js/checkout`, use `CheckoutElementsProvider` with the client secret, and confirm using `checkout.confirm`. If using HTML, make sure you use `checkout = stripe.initCheckoutElementsSdk({clientSecret: promise}); checkout.createPaymentElement(); paymentElement = checkout.createPaymentElement(); paymentElement.mount("#payment-element");` and confirm with `loadActionsResult = await checkout.loadActions(); actions = loadActionsResult.actions; error = await actions.confirm();`.

The main difference between the [Payment Intents](https://docs.stripe.com/api/payment_intents.md) API and [Setup Intents](https://docs.stripe.com/api/setup_intents.md) API is their purpose. You use the Payment Intents API to collect payment and charge a customer immediately. It creates a charge and processes a transaction to collect funds. You use Setup Intents API, on the other hand, to collect and save payment method details for future use without creating a charge. It sets up payment credentials without processing a payment.

Because both immediate charges and saving a payment method can require _asynchronous_ (Asynchronous refers to events happening at independent times in independent systems) customer steps, these APIs use the same state-machine pattern.

| Payment Intents API                                                        | Setup Intents API                                                                                                          |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Creates an immediate charge                                                | Creates no charge                                                                                                          |
| Tracks a payment’s lifecycle                                               | Tracks the progress of setting up a payment method                                                                         |
| Uses 3D secure to authenticate the customer for the applicable transaction | Uses 3D secure to authenticate a payment method without charging it, and creates a mandate or agreement for future charges |

#### PaymentIntents

A PaymentIntent tracks the lifecycle of a payment from creation through checkout, triggering additional authentication steps when required.

## Requires payment method

After you create the PaymentIntent, its [status](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-status) is `requires_payment_method` until you attach a [payment method](https://docs.stripe.com/payments/payment-methods/overview.md). Create the PaymentIntent as soon as you know the amount to charge so Stripe can record all attempted payments.

## Requires confirmation

After your customer provides payment information, the PaymentIntent enters the `requires_confirmation` status and is ready to confirm. Most integrations skip this state because they submit payment method information when the payment is confirmed.

## Requires action

If the payment requires additional actions, such as authenticating with [3D Secure](https://docs.stripe.com/payments/3d-secure.md), the PaymentIntent has a status of `requires_action`.

> #### API changes
>
> Versions of the API before [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11) show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`.

## Processing

After required actions are handled, the PaymentIntent moves to `processing` for _asynchronous payment methods_ (Asynchronous payment methods can take up to several days to confirm whether the payment has been successful. During this time, the payment can't be guaranteed), such as bank debits. These types of payment methods can take up to a few days to process. Other payment methods, such as cards, are processed more quickly and don’t go into the `processing` status.

If you’re separately [authorizing and capturing funds](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md), your PaymentIntent can instead move to `requires_capture`. In that case, attempting to capture the funds moves it to `processing` or `succeeded` depending on the payment method.

## Succeeded

A PaymentIntent with a status of `succeeded` means that the payment flow it’s driving is complete. The funds are now in your account and you can confidently fulfill the order. If you need to refund the customer, you can use the [Refunds](https://docs.stripe.com/api/refunds.md) API. If the payment attempt fails (for example due to a decline), the PaymentIntent’s status returns to `requires_payment_method` so that the payment can be retried.

## Canceled

You can cancel a PaymentIntent at any point before it’s in a `processing` or `succeeded` state. Canceling it invalidates the PaymentIntent for future payment attempts, and can’t be undone. If any funds have been held, cancellation releases them. You can cancel a PaymentIntent in the `processing` state when the associated payment method is [ACH](https://docs.stripe.com/payments/ach-direct-debit.md), [ACSS](https://docs.stripe.com/payments/acss-debit.md), [AU BECS](https://docs.stripe.com/payments/au-becs-debit.md), [BACS](https://docs.stripe.com/payments/payment-methods/bacs-debit.md), [NZ BECS](https://docs.stripe.com/payments/nz-bank-account.md), or [SEPA](https://docs.stripe.com/payments/sepa-debit.md). However, it might fail due to a limited and varying cancellation time window.

PaymentIntents might also be automatically transitioned to the `canceled` state after they have been [confirmed](https://docs.stripe.com/api/payment_intents/confirm.md) too many times.

#### SetupIntents

A SetupIntent tracks the lifecycle of a payment method from creation through checkout, triggering additional authentication steps when required.

## Requires payment method

When the SetupIntent is created, it has a [status](https://docs.stripe.com/api/setup_intents/object.md#setup_intent_object-status) of `requires_payment_method` until a payment method is attached.

## Requires confirmation

After the customer provides their payment method information, the SetupIntent enters the `requires_confirmation` status and is ready to confirm. Most integrations skip this state because they submit payment method information when the SetupIntent is confirmed.

## Requires action

If the setup requires additional actions, such as authenticating with 3D Secure, the SetupIntent has a status of `requires_action`.

> #### API changes
>
> Versions of the API before [2019-02-11](https://docs.stripe.com/upgrades.md#2019-02-11) show `requires_source` instead of `requires_payment_method` and `requires_source_action` instead of `requires_action`.

## Processing

After required actions are handled, the SetupIntent moves to `processing`. Although some payment methods (for example, cards) can process quickly, other payment methods can take up to several days to process.

## Succeeded

A SetupIntent with a status of `succeeded` means that the setup is successful. You can now attach this payment method to a Customer object and use this payment method for future payments. If the setup fails, the SetupIntent’s status returns to `requires_payment_method`.

## Canceled

You can cancel a SetupIntent at any point before it’s in a `processing` or `succeeded` state. Canceling it invalidates the SetupIntent for future setup attempts, and can’t be undone.
