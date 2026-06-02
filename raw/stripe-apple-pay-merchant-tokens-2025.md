<!-- Source URL: https://docs.stripe.com/apple-pay/merchant-tokens -->
<!-- Fetched: 2026-05-07 -->

# Apple Pay merchant tokens

Learn how to use Apple Pay merchant tokens for recurring, deferred, and automatic reload payments.

An [Apple Pay merchant token (MPAN)](https://developer.apple.com/apple-pay/merchant-tokens/) ties together a payment card, a business, and a customer, and enables the wallet holder to manage access to a card stored in their Apple wallet. Apple Pay’s latest guidelines recommend merchant tokens over device tokens (DPANs) because merchant tokens:

- Allow for continuity across multiple devices
- Enable recurring payments independent of a device
- Keep payment information active in a new device even when its removed from a lost or stolen device

## Merchant token types

You can use Apple Pay to request an MPAN in three ways. Each type of request has different parameters that affect how the user is presented with Apple Wallet. Almost all request types provide the option to supply a `managementURL`, which routes customers to a webpage to manage their payment methods. If you request an MPAN and the issuer supports MPAN generation, you receive an MPAN. Otherwise, you receive a DPAN.

| MPAN request type                                                                                                                     | Use case                                                                                 | Support                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Recurring [PKRecurringPaymentRequest](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest)                    | Issues an MPAN for use in a recurring payment such as a subscription.                    | - [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web) |
| - iOS > v16.0                                                                                                                         |
| Automatic reload [PKAutomaticReloadPaymentRequest](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest) | Issues an MPAN for use in a store card top-up or prepaid account. Supported parameters:  |
| - `automaticReloadBilling` shows billing details when you present Apple Pay.                                                          | - [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web) |
| - iOS > v16.0                                                                                                                         |
| Deferred payment [PKDeferredPaymentRequest](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest)               | Issues an MPAN for use in reservations such as hotels. Supported parameters:             |

- `freeCancellationDate` shows the cancellation deadline when you present Apple Pay.
- `billingAgreement` shows the terms of service when you present Apple Pay. | - [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
- Xcode 14.3
- iOS > v16.4 |

## Add Apple Pay merchant tokens

You can add a [merchant token](https://developer.apple.com/apple-pay/merchant-tokens/) when presenting Apple Pay in the Express Checkout Element, web Payment Element, and mobile Payment Element. Stripe automatically handles merchant token requests in Stripe Checkout integrations.

#### Express Checkout Element

If you’re using the [Payment Request Button](https://docs.stripe.com/stripe-js/elements/payment-request-button.md) for recurring payments, we recommend [migrating to the Express Checkout Element](https://docs.stripe.com/elements/express-checkout-element/migration.md) for improved functionality and payment method support.

1. Set up [Express Checkout Element integration](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment.md).
1. Pass the `applePay` object relevant to your MPAN use case (choose from the drop-down to see use case code samples).
1. Include relevant parameters for your use case.

#### MPAN use case - Recurring payments

```javascript
elements.create("expressCheckout", {
  applePay: {
    recurringPaymentRequest: {
      paymentDescription: "Standard Subscription",
      regularBilling: {
        amount: 1000,
        label: "Standard Package",
        recurringPaymentStartDate: new Date("2023-03-31"),
        recurringPaymentEndDate: new Date("2024-03-31"),
        recurringPaymentIntervalUnit: "year",
        recurringPaymentIntervalCount: 1,
      },
      billingAgreement: "billing agreement",
      managementURL: "https://stripe.com",
    },
  },
});
```

#### MPAN use case - Automatic reload

```javascript
elements.create("expressCheckout", {
  applePay: {
    automaticReloadPaymentRequest: {
      paymentDescription: "My automatic reload payment",
      managementURL: "https://example.com/billing",
      automaticReloadBilling: {
        amount: 2500,
        label: "Automatic Reload",
        automaticReloadPaymentThresholdAmount: 500,
      },
    },
  },
  // Other options
});
```

#### MPAN use case - Deferred payment

```javascript
const stripe = Stripe("pk_test_TYooMQauvdEDq54NiTphI7jx");
elements.create("expressCheckout", {
  applePay: {
    deferredPaymentRequest: {
      paymentDescription: "My deferred payment",
      managementURL: "https://example.com/billing",
      deferredBilling: {
        amount: 2500,
        label: "Deferred Fee",
        deferredPaymentDate: new Date("2024-01-05"),
      },
    },
  },
});
```

#### Web Payment Element

1. Create an instance of the [Payment Element](https://docs.stripe.com/payments/payment-element.md).
1. Pass the `applePay` object relevant to your MPAN use case (choose from the drop-down to see use case code samples).
1. Include relevant parameters for your use case.

#### MPAN use case - Recurring payments

```javascript
const paymentElement = elements.create("payment", {
  applePay: {
    recurringPaymentRequest: {
      paymentDescription: "My subscription",
      managementURL: "https://example.com/billing",
      regularBilling: {
        amount: 2500,
        label: "Monthly subscription fee",
        recurringPaymentIntervalUnit: "month",
        recurringPaymentIntervalCount: 1,
      },
    },
  },
  // Other options
});
```

#### MPAN use case - Automatic reload

```javascript
const paymentElement = elements.create("payment", {
  applePay: {
    automaticReloadPaymentRequest: {
      paymentDescription: "My subscription",
      managementURL: "https://example.com/billing",
      regularBilling: {
        amount: 2500,
        label: "Automatic Reload",
        automaticReloadPaymentThresholdAmount: 500,
      },
    },
  },
  // Other options
});
```

#### MPAN use case - Deferred payment

```javascript
const paymentElement = elements.create("payment", {
  applePay: {
    deferredPaymentRequest: {
      paymentDescription: "My deferred payment",
      managementURL: "https://example.com/billing",
      deferredBilling: {
        amount: 2500,
        label: "Deferred Fee",
        deferredPaymentDate: new Date("2024-01-05"),
      },
    },
  },
  // Other options
});
```

## Merchant token auth rate monitoring

For Sigma users, the `charges` table contains a `card_token_type` enum field to indicate the charge is using an `mpan` or `dpan` card. The following Sigma query example calculates the MPAN auth rate:

```sql
-- deduplicated MPAN auth rate
select
  100.0 * count(
    case
      when charge_outcome in ('authorized', 'manual_review') then 1
    end
  ) / count(*) as deduplicated_auth_rate_pct,
  count(*) as n_attempts
from
  authentication_report_attempts a
  join charges c on c.id = a.charge_id
where
  c.created >= date('2021-01-01')
  and c.card_tokenization_method = 'apple_pay'
  -- The new field added to charges table.
  and c.card_token_type = 'mpan'
  -- deduplicate multiple manual retries to a single representative charge
  and is_final_attempt
```
