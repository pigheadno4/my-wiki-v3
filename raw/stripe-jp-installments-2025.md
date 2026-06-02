<!-- Source URL: https://docs.stripe.com/payments/jp-installments -->
<!-- Fetched: 2026-05-01 -->

# Accept installment card payments in Japan

Learn about credit card payments using installments.

Installments (分割払い) are a type of credit card payment in Japan that allows customers to split purchases over multiple billing statements. You receive the full amount as with standard card payments, and the customer’s card company provides credit and collects the funds over time.

Stripe supports installment payments for Stripe Japan accounts using the Payment Intents and Payment Methods APIs.

Get started with accepting [installments](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md).

#### Payment method properties

- **Customer locations**

  Japan

- **Presentment currency**

  JPY

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Cards

- **Recurring payments**

  No

- **Payout timing**

  Standard

- **Connect support**

  Yes

- **Dispute support**

  Yes

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  Yes / yes

#### Business locations

Stripe accounts in Japan can accept card installment payments:

- JP

## Fees

Accepting installments doesn’t result in any additional fees for you. However, your customer might pay interest to their credit card company. Interest typically doesn’t apply when paying in two installments or with bonus installment plans, but does for others. Cardholders can check with their card company to learn about their fees.

## Transaction availability timing

Payments using installments become available on the same schedule as other card payments.

## User experience

In a [Stripe-hosted payment UI](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md?platform=web&ui=stripe-hosted), the option to pay in installments only displays after a user enters a supported card number. Use a [test card number](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md#testing) to test the functionality in the [Checkout Demo](https://checkout.stripe.dev/checkout). If you’ve built a custom payment UI using the [direct API](https://docs.stripe.com/payments/jp-installments/accept-a-payment.md?platform=web&ui=direct-api), we recommend you similarly collect the card number first, then display any available installment plans.

## Requirements

There are restrictions on which transactions and cards can use installments. Stripe automatically determines installments eligibility after you set up the payment method.

- Stripe only supports installments for Japanese Stripe accounts.
- The payment method must be a credit card issued in Japan. Debit and prepaid cards aren’t supported.
- The currency must be JPY.
- Don’t use installments for recurring payments or other off-session payments where your customer doesn’t select the installment plan when making the payment.

In addition, different brands offer different combinations of plans.

| Brand            | Installments   | Revolving      | Bonus          |
| ---------------- | -------------- | -------------- | -------------- |
| Visa/Mastercard  | Up to 60       | ✓ Supported    | ✓ Supported    |
| JCB              | Up to 24       | ✓ Supported    | ✓ Supported    |
| American Express | ❌ Unsupported | ❌ Unsupported | ❌ Unsupported |
| Diners Club      | ❌ Unsupported | ✓ Supported    | ✓ Supported    |
| Discover         | ❌ Unsupported | ❌ Unsupported | ❌ Unsupported |

American Express stopped supporting installments on all their self-issued cards as of December 2022. American Express prefers their cardholders to use their あと分割 product, where cardholders can apply installment plans post-checkout.

### Bonus payments

Stripe continues to return bonus payment plans in test environments even during periods when bonus payments are unavailable in live mode.

Bonus payments are available during two annual cycles:

- **Summer:** Dec 16 to Jun 15
- **Winter:** Jul 16 to Nov 15

On days between these cycles, bonus payments are unavailable:

- Jun 16 to Jul 15
- Nov 16 to Dec 15

When bonus payments are unavailable:

- Stripe doesn’t include bonus payments as an available [plan](https://docs.stripe.com/api/payment_intents/update.md#update_payment_intent-payment_method_options-card-installments-plan).
- You can’t create payments with bonus plans. If you try to do so, the Payment Intent confirmation fails with a `payment_intent_invalid_parameter` error.

If your customer is in your checkout while bonus payments are still available (for example, 11.59pm on Jun 15), but attempts to complete the payment when they’re no longer available (for example, 12:01am on Jun 16), their payment fails.

If you use [separate authorization and capture](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md) to create a bonus payment and capture it at a later date when bonus payments are unavailable, your customers might see their bonus payment as a normal card payment, or in their next bonus cycle.
