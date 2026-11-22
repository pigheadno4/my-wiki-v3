<!-- Source URL: https://docs.stripe.com/js/payment_intents/confirm_oxxo_payment -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

## Confirm an Oxxo payment

`stripe.confirmOxxoPayment(clientSecret: string, data?: object, options?: object)`

Use `stripe.confirmOxxoPayment` in the [OXXO Payment](https://docs.stripe.com/payments/oxxo.md) with Payment Methods flow when the customer submits your payment form.
When called, it will confirm the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md) with `data` you provide.
Note that there are some additional requirements to this flow that are not covered in this reference.
Refer to our [integration guide](https://docs.stripe.com/payments/oxxo.md) for more details.

When you confirm a `PaymentIntent`, it needs to have an attached [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).
In addition to confirming the `PaymentIntent`, this method can automatically create and attach a new PaymentMethod for you.
If you have already attached a `PaymentMethod` you can call this method without needing to provide any additional data.
These use cases are detailed in the sections that follow.

> Note that `stripe.confirmOxxoPayment` may take several seconds to complete.
> During that time, you should disable your form from being resubmitted and show a waiting indicator like a spinner.
> If you receive an error result, you should be sure to show that error to the customer, re-enable the form, and hide the waiting indicator.
> 
> Additionally, `stripe.confirmOxxoPayment` will pop up a modal with the voucher. This modal contains all the information required
> to pay the voucher at OXXO stores, such as the amount, a reference number and corresponding barcode.

- `clientSecret`
  The [client secret](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-client_secret) of the `PaymentIntent`.

- `data`
  Data to be sent with the request.
Refer to the [Payment Intents API](https://docs.stripe.com/api/payment_intents/confirm.md) for a full list of parameters.
    - `payment_method`
      The `id` of an existing PaymentMethod or an object of collected data.
See use cases below for details.

- `options`
  An options object to control the behavior of this method.
    - `handleActions`
      Set this to `false` if you want to handle next actions yourself. Please refer to our [Stripe OXXO integration guide](https://docs.stripe.com/payments/oxxo.md) for more info. Default is `true`.

### with collected data

### Data argument properties

- `payment_method`
  Pass an object to confirm using data collected.
    - `billing_details`
      The customer's [billing_details](https://docs.stripe.com/api/payment_methods/create.md#create_payment_method-billing_details).
`name` and `email` are required.
      - `name`
        The customer's name. The first and last name must be at minimum 2 characters each.
      - `email`
        The customer's email.

### Example

```title
Confirm with collected data
```

### with an existing payment method

### Data argument properties

- `payment_method`
  The `id` of an existing [PaymentMethod](https://docs.stripe.com/api/payment_methods.md).

### Example

```title
Confirm with existing payment method
```

### with an attached PaymentMethod

### Example

```title
Confirm with an attached PaymentMethod
```

### Example

```title
Confirm an Oxxo payment
```
