<!-- Source URL: https://docs.stripe.com/payments/sepa-debit -->
<!-- Fetched: 2026-05-03 -->

# SEPA Direct Debit payments

Learn about Single Euro Payments Area (SEPA) Direct Debit, a common payment method in the European Union.

The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. They established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region. Stripe currently supports the [SEPA Direct Debit Core scheme](https://www.europeanpaymentscouncil.eu/what-we-do/epc-payment-schemes/sepa-direct-debit/sepa-direct-debit-core-rulebook-and-implementation) and not the SEPA Direct Debit B2B scheme. The Core scheme supports both business and personal bank accounts.

To debit an account, businesses must collect their customer’s name and bank account number in IBAN format. During the payment flow, customers must accept a mandate that gives the business an authorization to debit the account. Stripe is able to generate this mandate for businesses to present to their customers. Locate the ID of the mandate used for this payment on the Charge under the [payment_method_details.sepa_debit.mandate](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-sepa_debit-mandate) property. Then, use the mandate ID to [retrieve the Mandate](https://docs.stripe.com/api/mandates/retrieve.md).

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#sepa-direct-debit).

SEPA Direct Debit is a [reusable](https://docs.stripe.com/payments/payment-methods.md#usage), [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method.

SEPA Direct Debit transactions have a limit of 10,000 EUR each. For new users, there’s an additional weekly limit of 10,000 EUR, which quickly increases as you process more SEPA direct debit payments. If you need higher limits, [contact support.](https://support.stripe.com/contact)

#### Payment method properties

- **Customer locations**

  EU

- **Payment method family**

  Bank debit

- **Connect support**

  [Yes](https://docs.stripe.com/payments/sepa-debit.md#connect)

- **Presentment currency**

  EUR

- **Recurring Payments**

  Yes

- **Payout timing**

  6 business days

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/sepa-debit.md#disputed-payments)

- **Manual capture support**

  No

- **Payment confirmation**

  Business-initiated

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/sepa-debit.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept SEPA Direct Debit payments:

- AT
- AU
- BE
- BG
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GI
- GR
- HK
- HR
- HU
- IE
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MX
- NL
- NO
- NZ
- PL
- PT
- RO
- SE
- SG
- SI
- SK
- US

#### Product support

- Connect
- Checkout
- Payment Links
- Subscriptions
- Invoicing
- Elements1

1Express Checkout Element doesn’t support SEPA Direct Debit.

## Verification Requirements

Using SEPA Direct Debit requires you to complete additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works) steps. We prompt you to complete these steps after you request access from the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you require further assistance, please [contact support](https://support.stripe.com/contact).

## Payment flow

![](assets/stripe-acss-debit-checkout-flow.svg)

*Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) selects SEPA Direct Debit at checkout
![](assets/stripe-acss-debit-account-info.svg)

Customer provides full name, IBAN, and authorizes mandate
![](assets/stripe-acss-debit-success.svg)

Customer gets notification that the payment is complete

## Get started

You don’t have to integrate SEPA Direct Debit and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable SEPA Direct Debit. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add SEPA Direct Debit from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If you prefer to manually list payment methods or want to save SEPA Direct Debit details for future payments, see the following guides:

- [Manually configure SEPA Direct Debit as a payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md)
- [Save SEPA Direct Debit details for future payments](https://docs.stripe.com/payments/sepa-debit/set-up-payment.md)

## Timing

With SEPA Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for SEPA Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

The following table describes the settlement timings for SEPA Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type     | Payment Success  | Funds Available  | Cutoff time |
| ------------------- | ---------------- | ---------------- | ----------- |
| Standard Settlement | T+6 at 00:00 UTC | T+6 at 00:00 UTC | 10:30 CET   |

## Debit notification emails

The [SEPA Direct Debit rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core) requires that you notify your customer each time you debit their account. For this case, by default, Stripe automatically sends the customer an email.

> When processing SEPA Direct Debit payments using the Stripe [Creditor ID](https://docs.stripe.com/payments/sepa-debit.md#creditor-identifiers-creditor-id), debit notification emails are always sent automatically by Stripe.

If you decide to send your customer a custom notification:

- Turn off Stripe emails in the [Stripe Dashboard email settings](https://dashboard.stripe.com/account/emails). However, if you use the Sources API, you can only control emails using [mandate.notification_method](https://docs.stripe.com/api/sources/update.md#update_source-mandate-notification_method) (for more information, see [notifying customers of recurring payments](https://docs.stripe.com/sources/sepa-debit.md#notifying-customers-of-recurring-payments)).
- Use the [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) event to trigger debit initiation emails.
- The email must include:
  - The last 4 digits of the debtor’s bank account
  - The mandate reference (`sepa_debit[reference]` on the Mandate)
  - The amount to be debited
  - Your SEPA creditor identifier
  - Your contact information
- It’s standard to send notifications at least 14 calendar days before you create a payment. However, SEPA rules let you send notifications closer to the payment date—just make sure your mandate clearly states when customers can expect to receive a notification. The mandate provided by Stripe specifies this can happen up to two calendar days in advance of future payments, allowing you to send notifications at payment creation. For recurring payments of the same amount (for example, a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) of a fixed amount), you can indicate multiple upcoming debits with corresponding dates in a single notice.

## Connect

To use SEPA Direct Debits in a *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) integration, you must enable SEPA Direct Debit on your platform and request the `sepa_debit_payments` capability for your connected accounts.

## Creditor Identifiers (Creditor ID)

A SEPA Creditor Identifier (Creditor ID) is an ID associated with each SEPA Direct Debit payment that identifies the company requesting the payment. While companies might have multiple creditor identifiers, each creditor identifier is unique and allows your customers to easily identify the debits on their account.

By default, your Stripe account is configured to use a Stripe Creditor ID when collecting SEPA Direct Debit Payments. The Creditor Name that appears on bank statements is determined by the following order of priority:

1. Your business name or legal entity name. For Connect, Stripe defaults to using the connected account’s business name if available. If not, Stripe uses the platform account’s business name.
1. Your Stripe account’s custom [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md). For Connect accounts, Stripe defaults to the connected account’s statement descriptor if available. If not, Stripe uses the platform account’s descriptor.
1. A default Stripe name (for example, “Stripe Technologies Europe Ltd”)

We recommend:

- Configuring a recognizable statement descriptor to help customers identify payments and reduce the risk of disputes.
- If you’re based in the EU, use your own Creditor ID to both reduce dispute rates and improve your customer experience. You can configure your own Creditor ID on the [Payment Method Settings](https://dashboard.stripe.com/settings/payment_methods) page in the Dashboard.
- If you’re using the Stripe Creditor ID, use [Stripe Checkout](https://docs.stripe.com/payments/checkout.md) to collect mandates from your customers for SEPA Direct Debits.

> After you’ve collected live SEPA Direct Debit payments on your account, you can’t change your Creditor ID in the Dashboard. If you need help with this issue, contact [Stripe support](https://support.stripe.com/contact) for information about migrating to a new Creditor ID.

### Creditor identifiers and Connect

The charge type of Connect payments changes the creditor identifier and name which appear on the customer’s bank statement.

| Charge type                                                                                                                            | Creditor ID taken from |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [Direct](https://docs.stripe.com/connect/direct-charges.md)                                                                            | Connected Account      |
| [Destination](https://docs.stripe.com/connect/destination-charges.md)                                                                  | Platform               |
| [Separate charges and transfers](https://docs.stripe.com/connect/separate-charges-and-transfers.md)                                    | Platform               |
| [Destination (`on_behalf_of`)](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant)                             | Connected Account      |
| [Separate charge and transfer (`on_behalf_of`)](https://docs.stripe.com/connect/separate-charges-and-transfers.md#settlement-merchant) | Connected Account      |

## Mandates

Before you can create a SEPA Direct Debit payment, businesses must collect a mandate that authorizes Stripe to debit the account on their behalf. Instructions for collecting mandate acceptance can be found on the [Accept a payment](https://docs.stripe.com/payments/sepa-debit/accept-a-payment.md) page.

Customers can request the cancellation of a mandate at any time. To cancel a mandate, a customer must either reach out to the party they established the mandate with, or to their bank. Canceling a mandate invalidates any future debit requests that you issue using this mandate. If you want to accept additional payments from your customer, you need to establish a new mandate with them. Stripe only learns about a canceled SEPA mandate when a payment attempt fails, after which Stripe sets the mandate as inactive and sends a `mandate.updated` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event.

### Mandate cancellation

Mandate cancellation makes sure that no further debit requests can be made using the canceled mandate. When a customer requests cancellation through the party they established it with or directly through their bank, it renders any future debit requests associated with that mandate invalid. You can also cancel active mandates by detaching the payment methods and sources associated with them. You can detach a payment method by deleting it from the Customer view in the Stripe Dashboard or by using the [API](https://docs.stripe.com/api/payment_methods/detach.md).

## Failed payments

SEPA Direct Debit payments can fail for various reasons, such as insufficient funds, closed accounts, or missing authorization.

### Payment timing and failures

Most SEPA Direct Debit payment failures occur within 6 business days of initiation. The following timeline describes how payments are processed:

**Submission phase (1-2 business days)**

- Your payment is submitted to the customer’s bank.
- Payments created before the daily cutoff time (10:30 CET) are submitted the same day.
- Payments made after the cutoff are submitted the following business day.

**Refusal window (5 business days)**

- After submission, there is a 5-business-day period (the “refusal window”) during which the customer’s bank can reject the payment. This is when most failures occur.
- The bank can return the payment during this period.

**Final settlement**

- After the refusal window, the payment appears as successful.
- In rare cases, payments can still fail after this point and appear as [disputes](https://docs.stripe.com/payments/sepa-debit.md#disputed-payments).

> Wait at least 6 business days before considering a SEPA Direct Debit payment as successful.

### Understand failure information

When a payment fails, Stripe provides detailed information to help you understand the issue. The `failure_code` field on the `Charge` indicates the specific reason for the failure, and the `failure_message` field provides a more detailed description of why the payment failed. Stripe immediately removes funds from your Stripe balance after failures.

The following table lists the possible SEPA Direct Debit failure codes with recommended next steps.

| Failure code                  | Explanation                                                                                                                                 | Next steps                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| refer_to_customer             | We don’t have detailed information about the payment failure because your customer’s bank didn’t provide a reason code.                     | Reach out to your customer for additional information.                                                                                                  |
| insufficient_funds            | The payment process can’t be completed because your customer’s bank account lacks the necessary funds.                                      | Reach out to your customer to verify that they have the required funds, then retry the transaction.                                                     |
| debit_disputed                | Your customer requested that their bank refund this payment.                                                                                | Reach out to your customer to resolve any dispute, then retry the transaction.                                                                          |
| authorization_revoked         | Your customer revoked their authorization and refused this payment.                                                                         | Reach out to your customer to understand the reasons for this revocation, then collect a new mandate and retry the transaction.                         |
| debit_not_authorized          | The payment lacks an authorized mandate.                                                                                                    | Collect a new mandate and retry the transaction.                                                                                                        |
| account_closed                | The payment can’t be processed because your customer’s bank account is closed.                                                              | Reach out to your customer for new account details, then try the transaction again.                                                                     |
| bank_account_restricted       | The payment can’t be processed because your customer’s bank has blocked Direct Debits, due to either the bank’s actions or your customer’s. | Reach out to your customer to understand the reason for the block. If the bank unblocks the account, attempt the transaction again.                     |
| debit_authorization_not_match | The transaction can’t be processed due to missing or incorrect mandate information.                                                         | Collect a new mandate from your customer, then attempt the transaction again.                                                                           |
| recipient_deceased            | The mandate was set up on the account of a possibly deceased individual.                                                                    | Verify your customer’s status before proceeding further.                                                                                                |
| branch_does_not_exist         | The payment can’t be processed because the bank branch associated with your customer’s IBAN doesn’t exist.                                  | Reach out to your customer to provide new bank details, then attempt the transaction again.                                                             |
| incorrect_account_holder_name | The transaction can’t be processed because your customer’s account information is missing or incorrect.                                     | Collect a new mandate and ask your customer to provide their name and address exactly as it appears on their bank account. Then, retry the transaction. |
| invalid_account_number        | The transaction can’t be processed because the IBAN provided by your customer is incorrect.                                                 | Reach out to your customer for correct bank details, then attempt the transaction again.                                                                |
| generic_could_not_process     | Stripe can’t identify a particular reason for the payment failure.                                                                          | Contact [Support](https://stripe.com/support) for more information.                                                                                     |

## Disputes

SEPA Direct Debit provides a dispute process for customers to dispute payments.

Customers can dispute a payment through their bank on a “no questions asked” basis up to eight weeks after their account is debited. Any disputes within this period are automatically honored.

After eight weeks and up to 13 months, a customer can only dispute a payment with their bank if the debit is considered unauthorized. If this occurs, we provide the bank with the mandate that the customer approved upon request. This doesn’t guarantee cancellation of the dispute. The bank can still decide that the debit was unauthorized and the customer is entitled to a refund.

When a dispute is created, Stripe sends a `charge.dispute.created` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event, and deducts the dispute amount and fee from your Stripe balance. The dispute fee varies based on your account’s default *settlement currency* (The settlement currency is the currency your bank account uses).

Unlike [credit card disputes](https://docs.stripe.com/disputes.md), SEPA Direct Debit disputes are final and there is no process for appeal. If a customer successfully disputes a payment, you must contact them if you want to resolve the situation. If you come to an arrangement and your customer is willing to return the funds to you, they must make a new payment.

In general, each dispute includes the reason for its creation, but this varies from country to country. For example, disputed payments in Germany don’t provide additional information for privacy reasons.

If a payment is disputed, and that payment is associated with a multi-use mandate, that mandate could be deactivated. Make sure to check the status of such mandates after a dispute. You have to re-collect mandate acceptance from your customers if their previous mandate is deactivated.

## Refunds

You can refund SEPA Direct Debit payments for up to 180 days after the original payment. You can refund part of the original payment or the entire amount of the original payment. Refunds are free of charge but the processing fees for the original payment are non-refundable.

### Refund timing and processing

- Refunds typically take 3-4 business days to process, and funds arrive in the customer’s account within 5 business days.
- Refunds must be submitted within 180 days of the original payment.
- SEPA refunds appear as credits in the customer’s bank account with a reference to the original payment’s statement descriptor, rather than being explicitly labeled as refunds.

### Important considerations

Customers can dispute a payment with their bank even after you’ve issued a refund, potentially resulting in two credits for the same payment. This happens because SEPA’s longer processing times can create confusion between you, your customer, their bank, and Stripe.

New accounts attempting refunds might have refunds temporarily disabled while Stripe reviews the account for fraud prevention. This review typically takes up to 2 business days.

### When to issue refunds

Stripe recommends issuing SEPA Direct Debit refunds only when:

- The customer is trusted and verified
- You’ve confirmed with the customer that you’re processing the refund
- At least 7 business days have passed since the original payment

> SEPA Direct Debit payments can fail up to 6 business days after creation (during the refusal window). Waiting 7 business days ensures the payment has fully settled before issuing a refund, preventing the double credit risk mentioned above.

### Customer communication

Always inform customers immediately when issuing a refund, explaining that it might take up to 5 business days to appear in their account.

If you accidentally debit a customer, contact them immediately to prevent disputes.

If you need assistance processing a refund, contact [Stripe support](https://support.stripe.com/contact/).

## Fraud Protection for SEPA with Radar

[Stripe Radar](https://stripe.com/radar) provides fraud protection capabilities for SEPA Direct Debits without any additional development time, performing real-time evaluation using machine learning algorithms to help identify and block high-risk transactions. Our machine learning trains specifically for SEPA, so it’s effective at detecting fraud that might be unique to SEPA Direct Debit payments.

For Radar users, Radar might default to on for all supported payment methods.

## Billing Retries (Private preview)

With Direct Debit retries, Stripe can automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for recurring subscription invoices, one-off invoices, or both.
