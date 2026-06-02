<!-- Source URL: https://docs.stripe.com/payments/upi/upi-autopay -->
<!-- Fetched: 2026-05-06 -->

# Recurring payments (UPI AutoPay)

Learn about e-mandates, regulatory requirements, and payment flows.

UPI supports recurring payments through e-mandates (also known as UPI AutoPay). This lets customers authorize automatic charges for subscriptions and recurring services.

## How e-mandates work

When setting up a mandate, customers authorize it in their UPI app during the initial payment flow. After the mandate is created, you can charge customers automatically for future payments within the mandate terms.

The Reserve Bank of India has established several security measures for recurring payments:

- **Additional factor authentication (AFA)**: Customers must enter their PIN to authorize the mandate during setup.
- **Pre-debit notifications**: At least 24 hours before each recurring charge, the customer must receive an SMS or app notification with the exact debit amount and an option to cancel the mandate.
  - If you integrate with Stripe, we send this notification automatically as part of the payment flow, without the need for you to take additional action.

## Initial payments

You can charge customers up to 5 minutes after the mandate is set up. Stripe handles this automatically. If you’re using Setup Intents, your customer is still debited and instantly refunded to prevent requiring AFA when you intend to charge them later.

## Subsequent payments

When you confirm a PaymentIntent for a recurring payment, Stripe automatically:

1. Sends the pre-debit notification to the customer
1. Waits the required 24 hours
1. Charges the customer

No additional action is required from you.

## Customize an e-mandate

Stripe offers multiple options for you to customize the mandate that you set up for your customer.

You can specify these options using the `payment_method_options[upi][mandate_options]` hash in the Stripe APIs. The options that you can customize are:

| Field name    | Description                                                                                                                                   | Default value                                                                                          |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `description` | The description that your customers see in their UPI app when approving the e-mandate.                                                        | `Subscription`                                                                                         |
| `amount`      | The amount that you want to associate with the mandate.                                                                                       | `1500000` (15,000 INR). This is the maximum amount that can be charged automatically with UPI AutoPay. |
| `amount_type` | Set to `maximum` to authorize payments under the mandate up to the `amount`. Set it to `fixed` to charge that exact amount under the mandate. | `maximum`                                                                                              |
| `end_date`    | Expiration date for the mandate. The maximum allowed value is 40 years from now, which reflects the UPI scheme maximum.                       | 10 years from when the mandate is created                                                              |

If your customer initiates a subscription with [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md), and [mandates support the selected currency](https://docs.stripe.com/india-recurring-payments.md?integration=subscriptions#mandate-creation), Stripe automatically creates an e-mandate in that currency.

To make sure that the mandate is created in the local currency with the correct exchange rate, don’t pass any mandate-specific parameters to the [Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md) when using Adaptive Pricing. If you pass mandate-specific parameters, then mandates use those values instead of the automatic ones.
