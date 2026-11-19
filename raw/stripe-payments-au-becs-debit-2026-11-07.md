<!-- Source URL: https://docs.stripe.com/payments/au-becs-debit -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Australia BECS Direct Debit payments

Learn how to accept Australia BECS Direct Debit payments.

If your business is in Australia, you can accept Australia BECS Direct Debit payments from customers with an Australian bank account.

To debit an account, you must collect the account holder’s name, Bank-State-Branch (BSB) number, and account number, and the customer’s acceptance of a Direct Debit Request (DDR) and its Service Agreement. Checkout and the Payment Element collect these details and the mandate acceptance for you.

Australia BECS Direct Debit is a [reusable](https://docs.stripe.com/payments/payment-methods.md#usage), [delayed notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) payment method. It takes up to 2 business days to receive the final success or failure notification after initiating a debit.
Payment method family: Bank debits
Usability: Reusable
Access type: Approval required
Payment confirmation timing: Delayed
Settlement timing: Up to 2 business days (T+2)
Pricing: https://stripe.com/au/pricing/local-payment-methods#australia-becs-direct-debit
## Eligibility and availability 

### Account eligibility
Business location: AU
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
### Verification requirements 

Australia BECS Direct Debit requires additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works). Stripe prompts you to complete these steps after you request access in [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you need help, [contact support](https://support.stripe.com/contact).

Stripe accounts in the following countries can accept Australia BECS Direct Debit payments that settle in a supported currency.

APAC: AU

Customers in the following countries can use Australia BECS Direct Debit.

APAC: AU

### Payment support
Customer location: AU
Presentment currency: AUD
Geographic coverage: ✓ Domestic, ✗ Crossborder
Transaction limits: Scheme minimum: 0.50 AUD

Scheme maximum: 99,000,000 AUD; account limits also apply
### Transaction limits 

The maximum transaction amount in the Payment support table is the scheme maximum, not your account’s processing limit. Stripe applies separate per-transaction and weekly volume limits to your account.

- The default per-transaction limit is 10,000 AUD.
- The default weekly volume limit is 10,000 AUD across your Australia BECS Direct Debit payments.

Your account’s limits can differ based on approval status and any limit increases. Payments must stay within both your applicable per-transaction and weekly volume limits, even when the payment amount is below the scheme maximum. If you need higher limits, [contact support](https://support.stripe.com/contact).

## Capabilities 
Recurring payments: ✓ Supported

Payment authorizations:
  ✗ Extended authorizations
  ✗ Flexible extended authorizations
  ✗ Incremental authorizations
  ✗ Decremental authorizations
  ✗ Re-authorizations

Payment captures:
  ✗ Manual capture
  ✗ Partial capture
  ✗ Multi-capture
  ✗ Over-capture

Refunds:
  ✓ Partial refunds
  ✓ Full refunds
  Submission window: 90 days
  Processing time: 5 business days

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
### Refunds 

Submit Australia BECS Direct Debit refunds within 90 days of the original payment. Refunds typically take 5 business days to process. You can issue full or partial refunds using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). If you accidentally debit a customer, contact them immediately to avoid a payment dispute.

#### Refund process 

If you create a full or partial refund while the payment is still processing, the refund begins only after the [Charge](https://docs.stripe.com/api/charges/object.md) status changes to `succeeded`. If the `Charge` status changes to `failed`, Stripe cancels the pending refund because the customer’s bank account was never debited.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

#### Bank statement appearance 

Australia BECS Direct Debit refunds are always processed as a separate credit to the customer’s bank account. Unlike card payments, they’re never issued as a reversal. The refund won’t be explicitly labeled as a refund on the customer’s bank statement. Instead, it appears as a credit referencing the original payment’s statement descriptor. Notify your customer when you issue a refund so they can identify the incoming credit.

#### Avoid duplicate credits 

Longer settlement times and extended dispute windows can lead a customer to contact both you and their bank about the same payment. If you issue a refund while the bank also initiates a dispute, the customer might receive two credits for the same transaction.

To reduce this risk:

- Confirm with your customer that you’re processing the refund so they don’t independently file a dispute with their bank.
- Explain the expected 5-business-day processing time so they don’t assume the refund failed.
- Wait until the original payment succeeds before issuing the refund, instead of refunding the customer directly outside Stripe.

> Issuing a refund doesn’t prevent the customer’s bank from processing a dispute. A customer can still file a dispute with their bank after receiving a refund, resulting in a double credit against you.

### Disputes 

#### Dispute process 

For up to 7 years, a customer can dispute an Australia BECS Direct Debit payment through their bank on a “no questions asked” basis. The bank honors disputes within this period. When a dispute is created, Stripe deducts the disputed amount and the applicable dispute fee from your Stripe balance.

#### Dispute notifications 

Stripe sends both [`charge.dispute.created`](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) and [`charge.dispute.closed`](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.closed) webhook events. You can also review the dispute in the [Dashboard](https://dashboard.stripe.com/disputes). [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) before acting on events.

#### Responding to disputes 

Contact your customer directly to resolve the dispute. Australia BECS Direct Debit disputes have no inquiry phase, and you can’t submit evidence or counter the dispute through the Dashboard or [Disputes API](https://docs.stripe.com/api/disputes.md).

#### Dispute outcomes 

All Australia BECS Direct Debit disputes are final and non-appealable. The dispute fee isn’t refunded. If you reach an agreement and your customer is willing to return the funds, they must make a new payment.

> If you proactively issue a refund while the customer’s bank also initiates the dispute process, the customer might receive two credits for the same transaction. Follow the [refund guidelines](https://docs.stripe.com/payments/au-becs-debit.md#avoid-duplicate-credits) to avoid this.

### Mandates 

Before debiting a customer’s bank account, you must collect a mandate authorizing the debit. Australia BECS Direct Debit calls this authorization a Direct Debit Request, or DDR.

#### What customers authorize 

The customer accepts the DDR and its Service Agreement to authorize your business to debit their bank account for one-time and recurring payments under the agreed terms.

#### Collect mandates 

Checkout and the Payment Element display the DDR and Service Agreement and collect the customer’s acceptance by default.

If you build a custom form with the `auBankAccount` Element, you must display Stripe’s DDR Service Agreement and standard authorization text and collect the customer’s acceptance. Follow the [payment integration guide](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md) or [save bank details guide](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md?payment-ui=direct-api) for the required text and form examples. Don’t substitute your own mandate language.

#### Manage mandates 

[Retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) with `latest_charge` expanded, then read `latest_charge.payment_method_details.au_becs_debit.mandate`. Use that mandate ID to [retrieve the Mandate](https://docs.stripe.com/api/mandates/retrieve.md). For Connect, make these requests in the account context that owns the payment and mandate.

A mandate collected for a `PaymentIntent` `on_behalf_of` a connected account can’t be reused for a different connected account.

#### Cancel mandates 

Customers can revoke a DDR at any time through your business or their bank. To cancel it from your business, detach the associated payment method from the `Customer` in the Dashboard or with the [Payment Methods API](https://docs.stripe.com/api/payment_methods/detach.md).

Canceling a mandate invalidates future debit requests under that authorization. Collect a new mandate before accepting later payments or continuing recurring payments.

#### Mandate events 

Stripe sends `mandate.updated` when a customer cancels a mandate or a permanent debit failure makes it inactive. Check the `Mandate` object’s `status`, which changes to `inactive`. Review these events in [Dashboard Events](https://dashboard.stripe.com/events), or handle them with a [webhook endpoint](https://docs.stripe.com/webhooks.md). [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) before acting on events.

## Stripe product support 
Checkout UIs:
  ✓ Full page (Recommended)
  ✓ Payment Links
  ✓ Embedded form
  ✓ Payment Element
  ✗ Express Checkout Element
  ✗ Payment Method Messaging Element
  ✓ In-app payments

Products:
  ✗ Managed Payments
  ✓ Billing
  ✓ Invoicing
  ✓ Customer Portal
  ✓ Radar
  ✗ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✓ Payment Intents with setup_future_usage
  ✓ Setup Intents
  ✗ Off-session payments
### Integration guides 

Follow the guide for your integration:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md)
- [Elements](https://docs.stripe.com/payments/quickstart.md)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)
- [Manually configure Australia BECS Direct Debit payments](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md)
- [Save Australia BECS Direct Debit details for future payments](https://docs.stripe.com/payments/au-becs-debit/set-up-payment.md)

## Timing 

With Australia BECS Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for Australia BECS Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

The following table describes the settlement timings for Australia BECS Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type | Payment Success | Funds Available | Cutoff time |
| --- | --- | --- | --- |
| Standard Settlement | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:30 Australia/Melbourne |

You can also read the estimated debit date from `latest_charge.payment_method_details.au_becs_debit.expected_debit_date` on the `PaymentIntent` with `latest_charge` expanded.

## Debit notification emails 

The Australia BECS Direct Debit scheme recommends notifying customers when a mandate is established and each time you debit their account. Stripe automatically sends these emails by default.

To send your own notifications:

1. Turn off Stripe emails in your [Dashboard email settings](https://dashboard.stripe.com/account/emails).
2. Include a link to the mandate in the mandate notification.
3. Use the `payment_intent.processing` [event](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) to trigger pre-debit notifications. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) before acting on events.

Include the following details in pre-debit notifications:

- The last 4 digits of the customer’s bank account
- The amount to be debited
- Your contact information
- The planned debit date

Scheme guidelines recommend sending notifications at least 14 calendar days before creating a payment, but this isn’t mandatory. Stripe’s default pre-debit email is sent the day before the account is debited. Notifications help avoid unnecessary debit failures and disputes.

For recurring payments of the same amount, such as a fixed-price subscription, you can group multiple upcoming debits and their dates in a single notice.

## Billing retries 

Enable [Direct Debit retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#direct-debit-retries) to have Stripe automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for [recurring subscription invoices](https://dashboard.stripe.com/revenue_recovery/retries), [one-off invoices](https://dashboard.stripe.com/settings/billing/invoices/general), or both.

Stripe can automatically retry each failed AU BECS Direct Debit payment a maximum of 4 times, no more than 30 days after the original payment attempt. These limits differ from card retries because AU BECS Direct Debit payments are asynchronous and can take several business days to complete.

Debit failure fees aren’t charged for retry attempts that we initiate automatically.

## Customer experience 

#### 1. Select Australia BECS Direct Debit

The customer selects Australia BECS Direct Debit at checkout.

#### 2. Enter bank details

The customer enters the account holder's name, email address, BSB number, and bank account number.

#### 3. Accept the Direct Debit Request

The customer accepts the DDR and its Service Agreement in the payment form, without a bank redirect or app switch.

#### 4. Payment submitted

The customer sees that the payment is submitted or processing, not that it has succeeded. Stripe reports the final success or failure asynchronously within 2 business days.

### Statement descriptors 

Each Australia BECS Direct Debit payment shows the business name and a transaction-specific lodgement reference on the customer’s bank statement. The business name comes from your account’s [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md). The lodgement reference uses the first 9 alphanumeric characters of the payment’s descriptor followed by a unique suffix.

Set `statement_descriptor` when creating the `PaymentIntent` to use a [dynamic statement descriptor](https://docs.stripe.com/payments/payment-intents.md#dynamic-statement-descriptor) for that payment. This changes the descriptor used in the lodgement reference, not the business name. Banks format these fields differently, including differences in capitalization.

For Connect, the charge type determines which account supplies the business name and default descriptor:

| Charge type | Account |
| --- | --- |
| Direct charge | Connected account |
| Destination charge | Platform |
| Separate charge and transfer | Platform |
| Destination charge with `on_behalf_of` | Connected account |
| Separate charge and transfer with `on_behalf_of` | Connected account |

Stripe doesn’t expose the lodgement reference through the API. Use `PaymentIntent` and `Charge` IDs to reconcile payments in the account context that owns those objects.

## Enable Australia BECS Direct Debit 

If you use Stripe front-end products, enable Australia BECS Direct Debit in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure Australia BECS Direct Debit as a payment method](https://docs.stripe.com/payments/au-becs-debit/accept-a-payment.md).
