<!-- Source URL: https://docs.stripe.com/payments/acss-debit -->
<!-- Fetched: 2026-05-02 -->

# Pre-authorized debit payments in Canada

Learn how to accept pre-authorized debit payments in Canada.

Stripe users in Canada and the United States can accept pre-authorized debit payments (PADs) from customers with a Canadian bank account using the Automated Clearing Settlement System (ACSS) provided by [Payments Canada](https://www.payments.ca).

Before debiting a customer’s bank account, businesses must first collect a [mandate](https://docs.stripe.com/payments/acss-debit.md#mandates) from the customer defining a specific payment schedule or terms. The mandate includes the customer’s institution number, transit number, account number, name, and email.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#pre-authorized-debits-in-canada).

When you use Stripe.js, our foundational JavaScript library for building payment flows, Stripe provides a hosted solution for collecting mandates from customers using your preferred terms, as well as fully-hosted collection of bank account details and instant bank verification (and delayed verification using micro-deposits in rare cases). This verification process is a requirement to accept PADs, and can also help to reduce payment failures and fraudulent activities.

Canadian pre-authorized debits are a [reusable](https://docs.stripe.com/payments/payment-methods.md#usage), [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. It can take up to 5 business days after initiating a payment to receive notification of success or failure. PADs aren’t a guaranteed payment method. There is a risk of failed payments and [disputes](https://docs.stripe.com/payments/acss-debit.md#disputed-payments).

#### Payment method properties

- **Customer locations**

  CA

- **Presentment currency**

  CAD, USD (in [rare cases](https://docs.stripe.com/payments/acss-debit.md#presentment-currency))

- **Payment confirmation**

  Business-initiated

- **Payment method family**

  Bank debit

- **Recurring payments**

  Yes

- **Payout timing**

  5 business days

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/acss-debit.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/acss-debit.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept pre-authorized debit payments:

- CA
- US

#### Product support

- Connect
- Checkout1, 4

- Subscriptions
- Invoicing
- Elements2, 3, 4

1 Not supported when using Checkout in subscription mode.2 Payment Element supports ACSS debit if you [create a PaymentIntent before rendering the Payment Element](https://docs.stripe.com/payments/accept-a-payment-deferred.md).3 Express Checkout Element and Mobile Payment Element don’t support ACSS debit.4 Not supported when using [Elements with the Checkout Sessions API](https://docs.stripe.com/payments/quickstart-checkout-sessions.md).

## Payment flow

![](assets/stripe-acss-debit-checkout-flow.svg)

*Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) selects pre-authorized debit at checkout
![](assets/stripe-acss-debit-account-info.svg)

Customer provides bank information and accepts mandate
![](assets/stripe-acss-debit-success.svg)

Customer gets notification that the payment is complete

## Get started

> Subscription mode in [Checkout](https://docs.stripe.com/payments/checkout.md) isn’t yet supported. To learn about early access when this feature is available, [contact us](mailto:payment-methods-feedback@stripe.com?subject=PADs%20Subscription%20Mode%20User%20Interest) to join the waitlist.

You don’t have to integrate Canadian pre-authorized debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Canadian pre-authorized debit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Canadian pre-authorized debit from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods or want to save Canadian pre-authorized debit details for future payments, see the following guides:

- [Manually configure Canadian pre-authorized debit as a payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md)
- [Save Canadian pre-authorized debit details for future payments](https://docs.stripe.com/payments/acss-debit/set-up-payment.md)

## Timing

With Canadian pre-authorized debits, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for Canadian pre-authorized debits under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

The following table describes the settlement timings for Canadian pre-authorized debits payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type     | Payment Success  | Funds Available  | Cutoff time      |
| ------------------- | ---------------- | ---------------- | ---------------- |
| Standard Settlement | T+4 at 21:00 UTC | T+5 at 00:00 UTC | 17:00 US/Eastern |

## Mandates

During the payment flow, Stripe helps you collect a mandate which gives your business authorization to debit the customer’s account. In Canada, these are called pre-authorized debit agreements or PAD agreements. The mandate collection, confirmation and pre-debit notification requirements for pre-authorized debits are governed by Payments Canada’s [Rule H1 for pre-authorized debits (PADs)](https://www.payments.ca/sites/default/files/h1eng.pdf).

Instructions for collecting mandate acceptance can be found on the [Accept a payment](https://docs.stripe.com/payments/acss-debit/accept-a-payment.md) page. In the unlikely event that your business requires a custom agreement, information on how to create a mandate that meets Payments Canada requirements can be found on the [Custom PAD mandate agreements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement.md) page.

Stripe will initiate the first debit immediately after mandate acceptance. Your customers must receive confirmation of a new mandate within 5 days after they have accepted the mandate (see [Mandate and debit notification emails](https://docs.stripe.com/payments/acss-debit.md#mandate-and-debit-notification-emails)).

Customers can at any time request the cancellation of a mandate, including by properly giving oral notice of cancellation. To cancel a mandate, a customer must either reach out to the business they established the mandate with, or to their bank. Canceling a mandate invalidates any further debit requests that you issue using this mandate. If you wish to accept additional payments from the customer, a new mandate must be established with them.

### Payment schedule

Each PAD mandate must specify a [payment schedule](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-mandate_options-payment_schedule) that defines when and how debits can be automatically charged to a customer.

| Schedule   | Use Case                                                                                                                                                                                                                                                                                                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `interval` | Subsequent payments for set interval PADs can be charged to customers outside of your checkout flow on a specified schedule or based on triggering events clearly described in the mandate with an [interval description](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-mandate_options-interval_description). |

One or more debits that occur with predictability, such as:

- a one-time payment on a specific date
- on a set of dates
- on a regular basis (for example, weekly, monthly)
- on the occurrence of certain criteria or events

Some example `interval_description` values for which you could debit:

- on the 5th of every month
- on completion of checkout
- on acceptance of a contract
- when a customer balance owing reaches 100 USD
- when any invoice becomes due |
  | `sporadic` | Debits that are infrequent or irregular and not at specified or predictable periods or time. Sporadic PADs can be charged to customers at arbitrary times, but only with the express authorization of the customer at the time of payment (such as logging into your website).

An example of a sporadic payment could be a balance owed by the customer where payment is triggered by the customer rather than automatically by you at a certain time. Collecting bank account details and a `sporadic` mandate ahead of time would allow your customer to trigger payment with a single step. |
| `combined` | A mandate that would allow both `interval` and `sporadic` debits. |

### Transaction type

Each PAD mandate must specify a [transaction type](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method_options-acss_debit-mandate_options-transaction_type) that defines whether transactions are for `personal` or `business` reasons.

### Default for

If you plan to use the payment method with [Invoicing](https://docs.stripe.com/invoicing.md) or [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md), set [default_for](https://docs.stripe.com/api/setup_intents/create.md#create_setup_intent-payment_method_options-acss_debit-mandate_options-default_for) to `['invoice', 'subscription']`. This lets you reuse the payment method for invoice and subscription payments without creating a new mandate.

## Mandate and debit notification emails

The [Payments Canada network rules](https://www.payments.ca/sites/default/files/h1eng.pdf) require that you notify your customer:

- When a mandate is established
- Each time a debit is made on their account

In addition, should your customer’s bank account need to be verified using micro-deposits, Stripe will send reminder emails linking to a hosted verification page.

By default, Stripe automatically sends emails to the customer for these cases. You can [customize the colors and logo](https://dashboard.stripe.com/account/branding) for these emails to fit the design and branding of your business.

> If you prefer to send custom notifications, all of these emails must be supported. It isn’t possible to send custom notifications for only one of them.

To send custom notifications:

- Turn off Stripe emails in the [Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails)
- Send a **mandate confirmation** email when you’ve collected your customer’s bank account and mandate authorization.
  - Mandate confirmation emails must be sent no later than 5 calendar days after your customer has accepted the mandate. Stripe will initiate the first debit immediately after mandate acceptance.
  - The email must include the mandate you created for the debit (see [Custom PAD mandate agreements](https://docs.stripe.com/payments/acss-debit/custom-pad-agreement.md)) and the bank account information collected from your customer, including the institution number, transit number and last four digits of the account number.
- Use the [charge.pending](https://docs.stripe.com/api/events/types.md#event_types-charge.pending) event to trigger **debit notification** emails.
  - Debit notification emails must include: your contact information, the last 4 digits of your customer’s bank account, and the amount to be debited.

## Disputes

Canadian pre-authorized debits provide a dispute process for bank account holders to dispute payments. Customers can dispute a debit payment through their bank on a “no questions asked” basis for up to 90 calendar days after a debit on a personal account or up to 10 business days for a business account. The customer’s bank can honor any dispute within this period.

When a dispute is created, Stripe sends both the [charge.dispute.created](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) and [charge.dispute.closed](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) events, and deducts the amount of the dispute and associated dispute fee from your Stripe balance.

Unlike [credit card disputes](https://docs.stripe.com/disputes.md), all PAD disputes are final and there is no process for appeal. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation. If you’re able to come to an arrangement and your customer is willing to return the funds to you, they must make a new payment.

> If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. You should follow the guidelines in the following section on refunds to avoid this happening.

## PADs transaction failures

PADs transactions can fail any time after the payment is initiated through payment confirmation. These failures can occur for a number of reasons, such as:

- Insufficient funds
- An invalid account number
- A customer disabling debits from their bank account

If a payment fails after funds have been made available in your Stripe balance, Stripe immediately removes funds from your Stripe account.

In rare situations, Stripe might receive a PADs failure from the bank after a PaymentIntent has transitioned to `succeeded`. If this happens, Stripe creates a dispute with a `reason` of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Presentment currency (Optional)

Most bank accounts in Canada hold Canadian dollars (CAD), with a small number of accounts in other currencies, including US dollars (USD). It’s possible to accept PAD payments in either CAD or USD, but choosing the correct currency for your customer is important to avoid payment failures.

Unlike many card-based payment methods, you might not be able to successfully debit a CAD account in USD or debit a USD account in CAD. Most often, attempting to do so will result in a delayed payment failure that will take up to 5 business days.

To avoid these failures, it’s safest to take PAD payments in CAD unless you’re confident your customer’s account will accept USD debits.

## Refunds

Refunds for PADs must be submitted within 180 days from the date of the original payment. Refunds require additional time to process (typically 3 business days). If you accidentally debit your customer, please contact them immediately to avoid a payment dispute.

Refunds are processed only after the payment process is complete. If you create a full or partial refund on a payment that hasn’t yet completed, the refund is actioned when the `Charge` object’s status transitions to `succeeded`. If the `Charge` object’s status transitions to `failed`, the full or partial refund is marked as canceled because the money was never debited from the customer’s bank account.

PAD refunds aren’t explicitly labeled as refunds when the funds are deposited back to a customer’s bank account. Instead, refunds are processed as a credit and include a reference to the original payment’s statement descriptor.

Due to longer settlement time periods and how banks process PAD transactions, there is potential for confusion between you, your customer, your customer’s bank, and Stripe. For example, your customer might contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction.

When issuing a refund, you should inform your customer immediately that the refund typically takes 3 business days to arrive in their bank account.

## Statement descriptors

Every PAD payment shows up on customers’ bank statements with the *name of the merchant*. For PAD payments created with Stripe, the name of the merchant is your Stripe account’s [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md). You can override this default behavior for every transaction independently by using a [dynamic statement descriptor](https://docs.stripe.com/payments/payment-intents.md#dynamic-statement-descriptor). To do so, you can specify the [statement_descriptor](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor) parameter when creating the `PaymentIntent`.

> Your statement descriptor will be truncated to the first 15 alphanumeric characters on the bank statement. For example, if your statement descriptor is `ROCKETRIDESLIMITED`, the customer will see `ROCKETRIDESLIMI`.
>
> Additionally, statement descriptors can’t use the special characters `<`, `>`, `'`, or `"`.

The table below illustrates the *merchant name* behavior you can expect on the customer’s bank statement:

| Default statement descriptor | Dynamic statement descriptor | Merchant name  | Bank statement descriptor |
| ---------------------------- | ---------------------------- | -------------- | ------------------------- |
| Rocket Rides                 | Unspecified                  | `Rocket Rides` | `Rocket Rides`            |
| Rocket Rides                 | `Sunday Ride`                | `Rocket Rides` | `Sunday Ride`             |

Each bank in Canada formats these fields differently. Depending on your customer’s bank, some fields might appear in all lowercase or uppercase.

### Statement descriptors and Connect

The charge type of Connect payments changes the statement descriptor and the merchant name, which appears on the customer’s bank statement.

| Charge type                                        | Descriptor taken from |
| -------------------------------------------------- | --------------------- |
| Direct                                             | Connected account     |
| Destination                                        | Platform              |
| Separate charge and transfer                       | Platform              |
| Destination (with `on_behalf_of`)                  | Connected Account     |
| Separate charge and transfer (with `on_behalf_of`) | Connected Account     |

A mandate collected for a `PaymentIntent` `on_behalf_of` a connected account can’t be used with a different connected account.

## Billing Retries (Private preview)

With Direct Debit retries, Stripe can automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for recurring subscription invoices, one-off invoices, or both.
