<!-- Source URL: https://docs.stripe.com/payments/bacs-debit -->
<!-- Fetched: 2026-05-02 -->

# Bacs Direct Debit payments in the UK

Learn how to accept payments with Bacs Direct Debit in the UK.

Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account.

To debit an account, businesses must collect a mandate from their customers. The mandate includes the customer’s sort code, account number, name, email, and full address. Stripe can generate this mandate for businesses to present to their customers.

BACS Direct Debit transactions have a limit of 100,000 GBP each. New users have an additional weekly limit of 10,000 GBP, which quickly increases as you process more BACS Direct Debit payments. If you need higher limits, [contact support](https://support.stripe.com/?contact=true).

Bacs Direct Debit is a [reusable, delayed notification payment method](https://docs.stripe.com/payments/payment-methods.md#payment-notification). This means it takes 4 business days to confirm the success or failure of a payment when a mandate is already in place, but when you must collect a new mandate, it can take 7 business days.

#### Payment method properties

- **Customer locations**

  UK

- **Presentment currency**

  GBP

- **Payment confirmation**

  Business-initiated

- **Payment method family**

  Bank debit

- **Recurring payments**

  Yes

- **Payout timing**

  4 business days

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/payment-methods/bacs-debit.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Bacs Direct Debit payments:

- GB

Platforms outside the UK can initiate Bacs Debit payments on behalf of UK connected accounts.

#### Product support

- Connect
- Checkout
- Payment Links
- Subscriptions1

- Invoicing
- Elements2

1You can’t use the Payment Element to create SetupIntents for Bacs Direct Debit. Use Checkout in setup mode instead.2Express Checkout Element doesn’t support Bacs Direct Debit.

## Verification Requirements

Using Bacs Direct Debit requires you to complete additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works) steps. We prompt you to complete these steps after you request access from the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you require further assistance, [contact support](https://support.stripe.com/contact).

## Get started

You don’t have to integrate Bacs Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Bacs Direct Debit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Bacs Direct Debit from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods or want to save Bacs Direct Debit details for future payments, see the following guides:

- [Manually configure Bacs Direct Debit as a payment](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md)
- [Save Bacs Direct Debit details for future payments](https://docs.stripe.com/payments/bacs-debit/save-bank-details.md)

## Timing

With Bacs Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for Bacs Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

It takes 4 business days to confirm the success or failure of a Bacs Direct Debit payment when a mandate is already in place and 7 business days when you must collect a new mandate.

In some cases, the bank might notify us of a payment failure after the payment has been marked as successful in your Stripe account. In this case the payment failure is identified as a dispute with the appropriate reason code.

The following table describes the settlement timings for Bacs Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type     | Payment Success  | Funds Available  | Cutoff time         |
| ------------------- | ---------------- | ---------------- | ------------------- |
| Standard Settlement | T+3 at 21:00 UTC | T+4 at 00:00 UTC | 20:00 Europe/London |

This table shows the Bacs timeline in business days from the time (T) that a payment is made when a new mandate must be collected:

| |
| |
| T+0 | Mandate submitted |
| T+3 | Mandate is active and the payment is submitted |
| T+5 | Funds leave the customer’s bank account |
| T+7 | Funds are available in Stripe |

## Debit notifications

Bacs Direct Debit requires that customers are notified of the following:

- When payment details are initially collected and confirmed
- Each time a debit will be made on their account

By default, Stripe automatically sends emails to the customer for the above cases. You can [customize the colors and logo](https://dashboard.stripe.com/account/branding) for these emails to fit the design and branding of your business.

If you require sending your own customer email notifications, [follow these steps](https://docs.stripe.com/payments/bacs-debit/email-customization.md) to customize your Business Display Name and contact us for approval of your email templates.

## Disputes

Bacs Direct Debit provides a [dispute process](https://stripe.com/legal/bacs-direct-debit-guarantee) for customers to dispute payments.

> *Customers* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) can dispute a payment through their bank for an unlimited period of time.

When a dispute is created, Stripe sends a `charge.dispute.created` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event and deducts the dispute amount from your Stripe balance.

Unlike [credit card disputes](https://docs.stripe.com/disputes.md), Bacs Direct Debit disputes are final and can’t be appealed. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation. If you’re able to come to an arrangement and your customer is willing to return the funds to you, they must make a new payment.

## Mandates

As part of the payment process, businesses must collect a mandate which gives them authorization to debit an account. For Bacs, this mandate is called a Direct Debit Instruction, or DDI. You can find information on how to collect a mandate with Stripe [Checkout](https://docs.stripe.com/payments/checkout.md) on the [Accept a payment](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md) page.

Customers can request the cancellation of a mandate at any time. To cancel a mandate, a customer can either reach out to the party they established the mandate with, or to their bank. Canceling a mandate invalidates any future debit requests that you issue using this mandate. If you want to accept additional payments from your customer, or continue using Bacs Direct Debit for a [Subscription](https://docs.stripe.com/subscriptions.md), you need to establish a new mandate by recollecting payment details.

### Mandate cancellation

Mandate cancellation ensures that no further debit requests can be made using the canceled mandate. When a customer requests cancellation through the party they established it with or directly through their bank, it renders any future debit requests associated with that mandate invalid. You can also cancel active mandates by detaching the payment methods and sources associated with them. You can detach a payment method by deleting it from the Customer view in the Stripe Dashboard or by using the [API](https://docs.stripe.com/api/payment_methods/detach.md).

Customers can also contact their bank to transfer existing mandates to a new bank or to report a name change. In these cases, Stripe automatically handles the update and reflect the updated mandate details.

### Mandate events

The mandate can change at any time after you’ve collected it. This might be the result of the customer instructing their bank to amend the mandate or because of a change in the bank itself (for example, the customer changes to a different one). Stripe sends the following events when the mandate changes:

| Event name                             | Description                                                                                                                                                                                                                            | Can accept payments?               |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `mandate.updated`                      | Occurs whenever a mandate is rejected, canceled, or reactivated by the Bacs network. Check [mandate.status](https://docs.stripe.com/api/mandates/object.md#mandate_object-status) to determine if the mandate can continue to be used. | Yes, if the new status is `active` |
| `payment_method.automatically_updated` | Occurs when a customer’s bank account details change.                                                                                                                                                                                  | Yes                                |

These events are available in the [Dashboard](https://dashboard.stripe.com/events), but you can set up a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to handle these programmatically.

## Refunds

Refunds for payments made with Bacs Direct Debit must be submitted within 180 days from the date of the original payment. Refunds require additional time to process (typically 3-4 business days). If you accidentally debit your customer, please contact them immediately to avoid a payment dispute.

> Refunds aren’t part of the Bacs Direct Debit scheme and are provided outside of Bacs Direct Debit by Stripe. Since Bacs Direct Debit has an indefinite indemnity period, if a customer creates a [dispute](https://docs.stripe.com/disputes.md) *any time after* a refund has been issued, you can lose both the disputed amount and the amount you refunded separately.

You can issue full or partial refunds for Direct Debit payments by using the API to [create a refund](https://docs.stripe.com/api.md#create_refund) with the [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md) object.

Refunds are processed only after the payment process is complete. If you create a full or partial refund on a payment that hasn’t completed yet, the refund process starts when the [Charge](https://docs.stripe.com/api/charges/object.md) object’s status transitions to `succeeded`. If the [Charge](https://docs.stripe.com/api/charges/object.md) object’s status transitions to `failed`, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

## Checkout

[Checkout](https://stripe.com/checkout) creates a secure, Stripe-hosted payment page that lets you collect payments quickly. You can use Checkout to collect Bacs Direct Debit payments, or collect payment details that you can use to initiate payments at a later date.

### Request the bacs_debit_payments capability

Platforms in the UK don’t need to request the `bacs_debit_payments` capability for their UK Connect accounts when performing [destination charges](https://docs.stripe.com/connect/destination-charges.md). Platforms outside the UK might still need to process Bacs Direct Debit payments for their UK Connect accounts, and they must have the `bacs_debit_payments` capability enabled.

In both scenarios, you must [request the `bacs_debit_payments` capability](https://docs.stripe.com/connect/account-capabilities.md) if you want to use the [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of) parameter.

Requesting the `bacs_debit_payments` capability with `settings.bacs_debit_payments.display_name` automatically enables custom branding. This allows you to collect mandates using the connected account’s chosen display name as the statement descriptor.

Each account that uses custom branding incurs a 50 GBP monthly fee.

If you don’t want to use custom branding, you can do either of the following:

- Request the capability without specifying `settings.bacs_debit_payments.display_name`
- Set the default value of `settings.bacs_debit_payments.display_name = Stripe` before requesting the capability

## Custom Branding

Upgrade to Custom Branding if you want to customize your customer’s bank statements, Stripe Checkout, and customer emails for direct debits to show your business name.

You can enable Custom Branding for your account in your [Bacs Direct Debit settings](https://dashboard.stripe.com/settings/payment_methods).

For your Express or Custom accounts, you can enable Custom Branding by selecting `settings.bacs_debit_payments.display_name` in the [API](https://docs.stripe.com/api/accounts/object.md#account_object-settings-bacs_debit_payments-display_name).

You can do this during account creation or when updating the account after setup.

If you request the `bacs_debit_payments` capability without specifying `settings.bacs_debit_payments.display_name`, the account defaults to Stripe branding.

Custom Branding is charged at 50 GBP per active month. Your business name is shown for new mandates created 5 business days after your request. To expedite Custom Branding or apply it to multiple connected accounts for a single fee, [contact us](https://support.stripe.com/contact).

If you don’t use your custom branding for a long period of time, your account automatically reverts to the default Stripe branding. Alternatively, if you have no active Bacs Debit mandates you can revert to the default Stripe branding in your [Bacs Direct Debit settings](https://dashboard.stripe.com/settings/payment_methods).

## Billing Retries (Private preview)

With [Direct Debit retries](https://dashboard.stripe.com/revenue_recovery/retries), Stripe can automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for recurring subscription invoices, one-off invoices, or both.
