<!-- Source URL: https://docs.stripe.com/payments/nz-bank-account -->
<!-- Fetched: 2026-05-03 -->

# New Zealand BECS Direct Debit payments

Learn how to accept New Zealand BECS Direct Debit payments.

Stripe users in New Zealand can accept New Zealand BECS Direct Debit payments directly from customers with a New Zealand bank account.

As part of the payment process, businesses must collect a mandate that includes the customer’s bank account details (account holder’s name, email address, and bank account number) and agreement to the New Zealand BECS Direct Debit Service terms and conditions. This grants the business an authorization to debit the account. Stripe can handle collection of this account information and mandate on behalf of businesses.

New Zealand BECS Direct Debit is a [reusable](https://docs.stripe.com/payments/payment-methods.md#usage), [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. This means that it can take up to two business days to receive notification on the success or failure of a payment after you initiate a debit from the customer’s account.

#### Payment method properties

- **Customer locations**

  New Zealand

- **Presentment currency**

  NZD

- **Payment confirmation**

  Business-initiated

- **Payment method family**

  Bank debits

- **Recurring payments**

  Yes

- **Payout timing**

  2 business days

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/nz-bank-account.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes](https://docs.stripe.com/payments/nz-bank-account.md#refunds) / Yes

#### Business locations

Stripe accounts in the following countries can accept New Zealand BECS Direct Debit payments:

- NZ

#### Product support

- Connect
- Checkout
- Payment Links
- Subscriptions
- Invoicing
- Elements

## Verification Requirements

Using New Zealand BECS Direct Debit requires you to complete additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works) steps. We prompt you to complete these steps after you request access from the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you require further assistance, [contact Stripe support](https://support.stripe.com/contact).

## Payment flow

![](assets/stripe-acss-debit-checkout-flow.svg)

Customer selects New Zealand bank account debit at checkout
![](assets/stripe-acss-debit-account-info.svg)

Customer provides bank account information and accepts mandate
![](assets/stripe-acss-debit-success.svg)

Customer gets notification that the payment is complete

## Get started

You don’t have to integrate New Zealand BECS Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable New Zealand BECS Direct Debit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add New Zealand BECS Direct Debit from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods or want to save New Zealand BECS Direct Debit details for future payments, see the following guides:

- [Manually configure New Zealand BECS Direct Debit as a payment](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md)
- [Save New Zealand BECS Direct Debit details for future payments](https://docs.stripe.com/payments/nz-bank-account/set-up-payment.md)

If you prefer to migrate your New Zealand BECS Direct Debit from another processor, see how to [migrate from another processor](https://docs.stripe.com/payments/nz-bank-account/migrate-from-another-processor.md).

## Timing

With New Zealand BECS Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for New Zealand BECS Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

The following table describes the settlement timings for New Zealand BECS Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type     | Payment Success  | Funds Available  | Cutoff time            |
| ------------------- | ---------------- | ---------------- | ---------------------- |
| Standard Settlement | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:20 Pacific/Auckland |

## Mandates

During the payment process, businesses must collect a mandate that authorizes Stripe to debit the account on their behalf. New Zealand BECS Direct Debit calls these mandates Direct Debit Authorities, or DDAs.

Bank account holders can request the cancellation of active mandates at any time. To cancel a mandate, a bank account holder must either contact their bank or the party they established the mandate with. Canceling a mandate invalidates any future debit requests that you issue using it. If you want to accept additional payments from your customer, establish a new mandate with them.

### Mandate events

| Event name        | Description                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `mandate.updated` | Occurs whenever the customer cancels a mandate or because of a permanent debit failure. The `status` property changes to `inactive`. |

You can see the events in your Dashboard, but you should still set up a [webhook endpoint](https://docs.stripe.com/webhooks.md).

## Mandate confirmation and debit notification emails

The New Zealand BECS Direct Debit scheme requires that you notify your customer by email within 5 days after establishing a mandate, and on the day of the debit each time you debit their account. By default, Stripe automatically sends these emails to the customer.

If you want to turn off Stripe emails for New Zealand bank account payments and send your own emails to your customers, contact [Stripe support](https://support.stripe.com/contact) for assistance.

### Mandate confirmation emails

Stripe sends this email within 5 days of establishing a mandate. It contains all relevant details of the mandate, including:

- The date of the mandate confirmation
- A statement that Stripe New Zealand Limited (authorization code 3143978) acts on your behalf to arrange for the funds to be debited
- A link to the [New Zealand Direct Debit Service Terms and Conditions](https://stripe.com/nz/legal/nzbecs-customer-dd-service-terms)
- A statement that the direct debit is subject to the [New Zealand BECS Direct Debit Service Terms and Conditions](https://stripe.com/nz/legal/nzbecs-customer-dd-service-terms), and the terms and conditions of the customer’s own bank for accepting direct debits
- The name of the customer’s bank
- The customer’s bank account number
- The name of the customer’s bank account
- The name of the authorised signatory for the customer’s bank account (if different from the customer’s bank account name)
- Your contact information, including address, email, and a phone number

If creating the PaymentMethod and collecting the mandate using a PaymentIntent, this happens immediately after successful confirmation.

If collecting the mandate using a SetupIntent, this happens immediately after the SetupIntent succeeds.

### Pre-debit notification emails

Stripe sends this email immediately after every successful PaymentIntent confirmation. It contains all relevant details of the payment, including:

- The amount of the payment
- A statement that the debit from the customer’s account will be made by Stripe New Zealand Limited (authorization code: 3143978)
- The date we debit their account
- A statement that the transaction may appear on the customer’s bank statement as “Stripe New Zealand Limited”
- Your contact information, including address, email, and a phone number

## Disputes

New Zealand bank account debits provide a dispute process for bank account holders to dispute payments.

For up to 9 months from the date of the first payment, a customer can dispute a payment if the customer isn’t reasonably satisfied that the DDA authorizes that direct debit.

For up to 120 days after the date of a payment, a customer can dispute that payment if you didn’t send the pre-debit notification, or if you sent the pre-debit notification, but the amount or date of the direct debit is different from the amount or date on the notification.

If the customer’s bank rules in favor of the customer and requests a return of funds, Stripe immediately removes the funds from your Stripe account.

If a dispute gets created, Stripe sends the `charge.dispute.created` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

> If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. Follow the [refund guidelines](https://docs.stripe.com/payments/nz-bank-account.md#refunds) to avoid this.

## Refunds

Refunds for New Zealand bank account debits must be issued within 90 days from the date of the original payment. Refunds require additional time to process (typically 3-5 business days). If you accidentally debit your customer, contact them immediately to avoid a payment dispute.

Refunds are processed only after the payment process completes. If you create a full or partial refund on a payment that hasn’t completed yet, the refund process starts when the `PaymentIntent` object’s status transitions to `succeeded`. If the payment fails and the `PaymentIntent` object’s status transitions to `requires_payment_method`, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

New Zealand BECS Direct Debits don’t explicitly label refunds when they’re deposited back into a bank account. Instead, refunds are processed as a credit and include a visible reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process New Zealand bank account transactions, there might be confusion between you, your customer, your customer’s bank, and Stripe. For example, your customer might contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction.

When issuing a refund, inform your customer immediately that the refund can take up to 5 business days to arrive in their bank account. Stripe won’t automatically send the customer an email to inform them about this.

## Billing Retries (Private preview)

With Direct Debit retries, Stripe can automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for recurring subscription invoices, one-off invoices, or both.
