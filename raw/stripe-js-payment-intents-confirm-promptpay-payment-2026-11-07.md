<!-- Source URL: https://docs.stripe.com/js/payment_intents/confirm_promptpay_payment -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

## Confirm a PromptPay payment

`stripe.confirmPromptPayPayment(clientSecret: string, data?: object, options?: object)`

Use `stripe.confirmPromptPayPayment` in the PromptPay payment method creation flow when the customer submits your payment form.
When called, it will confirm the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with `data` you provide and handle the [NextAction](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-next_action) for the customer to authorize the payment.
When you confirm a `PaymentIntent`, it needs to have an attached [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
In addition to confirming the `PaymentIntent`, this method can automatically create and attach a new `PaymentMethod` for you.
If you have already attached a `PaymentMethod` you can call this method without needing to provide any additional data.
These use cases are detailed in the sections that follow.

> Note that `stripe.confirmPromptPayPayment` may take several seconds to complete and display the QR code.
> During that time, you should disable your form from being resubmitted and show a waiting indicator like a spinner.
> If you receive an error result, you should be sure to show that error to the customer, re-enable the form, and hide the waiting indicator.

- `clientSecret`
  The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent`.

- `data`
  Data to be sent with the request.
Refer to the [Payment Intents API](https://docs.stripe.com/api/payment_intents/confirm.md) for a full list of parameters.
    - `payment_method`
      Either the `id` of an existing [PaymentMethod](https://docs.stripe.com/api/payment_methods.md), or an object containing data to create a `PaymentMethod` with.
See the use case sections below for details.

- `options`
  An options object to control the behavior of this method.
    - `handleActions`
      Default to be `true`. Set this to `false` if you would like to [handle displaying the PromptPay QR code yourself](https://docs.stripe.com/payments/promptpay/accept-a-payment.md#confirm-payment-intent).

### Without an existing payment method

### Data argument properties

- `payment_method`
  Pass payment method billing details.
    - `billing_details`
      The [billing_details](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-billing_details) associated with the payment method.

### Example

```title
Confirm without existing payment method
```

### With an existing payment method

### Data argument properties

- `payment_method`
  The `id` of an existing `PaymentMethod`.

### Example

```title
Confirm with existing payment method
```

### With an attached PaymentMethod

### Example

```title
Confirm with an attached PaymentMethod
```

### Example

```title
Confirm a PromptPay payment
```
