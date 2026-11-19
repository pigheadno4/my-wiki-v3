<!-- Source URL: https://docs.stripe.com/payments/bacs-debit -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Bacs Direct Debit payments

Learn how to accept Bacs Direct Debit payments in the UK.

Stripe users in [supported business locations](https://docs.stripe.com/payments/bacs-debit.md#bacs_debit-business-locations) can accept Bacs Direct Debit payments from customers with a UK bank account.

To debit an account, businesses must collect a mandate from their customers. The mandate includes the customer’s sort code, account number, name, email, and full address. Stripe can generate this mandate for businesses to present to their customers.

Bacs Direct Debit is a [reusable, delayed notification payment method](https://docs.stripe.com/payments/payment-methods.md#payment-notification). It typically takes 4 business days to confirm the success or failure of a payment when a mandate is already in place, or up to 7 business days when collecting a new mandate.
Payment method family: Bank debits
Usability: Reusable
Access type: Approval required
Payment confirmation timing: Delayed
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-gb/pricing/local-payment-methods#bacs-direct-debit
## Eligibility and availability 

### Account eligibility
Business location: AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
We might review your account after activation to confirm eligibility. Make sure your website meets [Stripe’s account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq).

### Verification requirements 

Using Bacs Direct Debit requires additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works). Stripe prompts you to complete these steps after you request access in [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you need help, [contact support](https://support.stripe.com/contact).

Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for Bacs Direct Debit.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

| MCC | Description | Type |
| --- | --- | --- |
| 4829 | Money Orders - Wire Transfers | Restricted |
| 5122 | Drugs, Drug Proprietaries, and Druggist Sundries | Restricted |
| 5499 | Miscellaneous Food Stores | Restricted |
| 5912 | Drug Stores and Pharmacies | Restricted |
| 5941 | Sporting Goods Stores | Restricted |
| 6012 | Financial Institutions | Restricted |
| 6050 | Software | Restricted |
| 6051 | Cryptocurrency exchanges and wallets | Restricted |
| 6211 | Security Brokers and Dealers | Restricted |
| 6536 | Software | Restricted |
| 6537 | Software | Restricted |
| 6538 | Software | Restricted |
| 6539 | Software | Restricted |
| 6540 | Non-FI, Stored Value Card Purchase and Load | Restricted |
| 7800 | Government-Owned Lotteries (US Region only) | Restricted |
| 7801 | Government Licensed On-line Casinos (On-Line Gambling) | Restricted |
| 7802 | Government-Licensed Horse and Dog Racing | Restricted |
| 7995 | Betting and Casino Gambling | Restricted |
| 9223 | Bail and Bond Payments | Restricted |
| 9311 | Tax Payments - Government Agencies | Restricted |
| 9754 | Lodging - Hotels, Motels, and Resorts (Continued) | Restricted |
| 6010 | Manual Cash Disburse | Prohibited |
| 6011 | Financial Service | Prohibited |
| 7273 | Dating and Escort Services | Prohibited |

Stripe accounts in the following countries can accept Bacs Direct Debit payments that settle in a supported currency.

AMER: CA, US

EMEA: AT, BE, BG, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

APAC: AU, SG

Customers in the following countries can use Bacs Direct Debit.

EMEA: GB

### Payment support
Customer location: GB
Presentment currency: GBP
Geographic coverage: ✓ Domestic, ✓ Crossborder
### Transaction limits 

Bacs Direct Debit transactions have a default limit of 10,000 GBP each.

New users also have a weekly limit of 10,000 GBP that increases as they process more Bacs Direct Debit payments. If you need higher limits, [contact support](https://support.stripe.com/?contact=true).

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
  Submission window: 180 days
  Processing time: 4 business days

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
### Refunds 

Refunds for Bacs Direct Debit payments must be submitted within 180 days of the original payment. Refunds typically take 3–4 business days to process. If you accidentally debit your customer, contact them immediately to avoid a payment dispute.

#### Refund process 

Refunds aren’t part of the Bacs Direct Debit scheme and are provided outside of Bacs by Stripe. When the original debit has completed, Stripe processes the refund as a separate credit to the customer’s bank account, not as a reversal of the original debit. If Stripe has submitted the debit and the payment is still processing, the refund waits until the Charge succeeds. If the Charge fails, Stripe cancels the pending refund because the customer wasn’t debited, so no separate credit is sent. Because Bacs has an indefinite indemnity period, a customer can create a dispute at any time after a refund has been issued. This means you can lose both the disputed amount and the refunded amount.

If your customer contacts both you and their bank about a payment, issuing a refund while the bank also initiates a dispute might result in two credits.

To reduce the risk of a double credit:

- Confirm with your customer that you’re processing the refund so they don’t independently file a dispute with their bank.
- Tell your customer the expected 3–4-business-day processing time.
- Issue the refund through Stripe only after the original payment has fully settled.

You can issue full or partial refunds using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md).

#### Tracking refunds 

To receive refund-failure notifications, configure your event destination to receive [refund.failed](https://docs.stripe.com/api/events/types.md#event_types-refund.failed). Inspect the Refund object’s [status](https://docs.stripe.com/api/refunds/object.md#refund_object-status) and [failure_reason](https://docs.stripe.com/api/refunds/object.md#refund_object-failure_reason). If the refund fails, arrange an alternative way to refund your customer. This is a webhook notification, not a guaranteed email.

Stripe doesn’t send a `refund.succeeded` event. To monitor successful refunds, configure your event destination to receive [refund.updated](https://docs.stripe.com/api/events/types.md#event_types-refund.updated) and check for `status` set to `succeeded`. You can also check the Refund status in the [Dashboard](https://dashboard.stripe.com/payments) or retrieve the [Refund object](https://docs.stripe.com/api/refunds/retrieve.md) through the API. A `refund.created` or `charge.refunded` event alone doesn’t confirm that the refund succeeded or that the customer’s bank has posted the credit.

### Disputes 

There’s no set time limit for customers to file Bacs Direct Debit disputes. Bacs Direct Debit payments can only be disputed once.

#### Dispute process 

Stripe doesn’t publish a fixed timeframe between a customer contacting their bank and Stripe receiving or creating the dispute. When we create a dispute, we send a [charge.dispute.created](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) event and deduct the disputed amount and applicable fee from your Stripe balance.

#### Dispute notifications 

Review the dispute in the [Dashboard](https://dashboard.stripe.com/disputes). Open the disputed payment to view its **Dispute details**. The reported reason is also available in the [Dispute object’s `reason` property](https://docs.stripe.com/api/disputes/object.md#dispute_object-reason), including the object in `charge.dispute.created`. This is a reported reason category, not necessarily a detailed explanation from the customer. The public Bacs documentation doesn’t specify additional Bacs-specific network reason details.

#### Responding to disputes 

You can’t submit evidence or counter a Bacs Direct Debit dispute. There isn’t a merchant appeal stage for these payment disputes. Contact your customer directly if you want to resolve the situation.

#### Dispute outcomes 

The bank’s dispute decision is final and non-appealable. If you reach an arrangement with your customer and they agree to return the funds, they must make a new payment. The dispute fee isn’t refunded.

### Mandates 

To debit a customer’s account, you must collect a Bacs Direct Debit Instruction (DDI), also called a mandate. The mandate authorizes you to debit the account for one-time and recurring payments.

#### What customers authorize 

By accepting the Bacs Direct Debit mandate, the customer authorizes you to debit their bank account under the Direct Debit Instruction. Stripe records the business name, acceptance details, and Bacs mandate reference on the Mandate object.

#### Collect mandates 

[Checkout](https://docs.stripe.com/payments/checkout.md) collects the customer’s Bacs bank details and mandate acceptance. The Payment Element can’t create Bacs Direct Debit SetupIntents; use Checkout in setup mode instead.

Custom API mandate collection requires Stripe approval. Your form must follow the [Bacs mandate collection requirements](https://docs.stripe.com/payments/bacs-debit/mandate-collection-requirements.md), including collecting the payer’s agreement with this exact checkbox text:

`I understand that [Merchant Name] has partnered with Stripe, who collects Direct Debits on behalf of [Merchant Name] and confirm that I am the account holder and the only person required to authorize debits from this account.`

#### Manage mandates 

A mandate can change after collection because the customer asks their bank to amend it or their bank details change. Stripe updates the mandate automatically and sends mandate events that you can monitor.

#### Cancel mandates 

Customers can request cancellation at any time from you or their bank. Canceling a mandate invalidates future debit requests. To accept more payments or continue a Subscription, collect a new mandate and payment details.

You can also cancel an active mandate by detaching its payment method from the Customer in the Dashboard or with the [PaymentMethods API](https://docs.stripe.com/api/payment_methods/detach.md). Customers can ask their bank to transfer a mandate to a new bank or report a name change; Stripe automatically applies those updates.

#### Bacs mandate requirements 

If you use a custom mandate form, it must include your postal address or customer support email, a phone number for general inquiries or customer service, the 2-working-day advance notice period, the name that appears on the customer’s bank statement, and a link to or unedited copy of the [Direct Debit Guarantee](https://stripe.com/legal/bacs-direct-debit-guarantee). Show the bank details the customer entered so they can confirm them. Your final setup screen must confirm that setup is complete and that an email confirmation will follow within 3 working days. See the [full mandate collection requirements](https://docs.stripe.com/payments/bacs-debit/mandate-collection-requirements.md).

#### Mandate events 

The mandate can change at any time after you’ve collected it. This might result from the customer instructing their bank to amend the mandate or from a change at the bank. Stripe sends the following events when the mandate changes:

| Event name | Description | Can accept payments? |
| --- | --- | --- |
| `mandate.updated` | Occurs whenever a mandate is rejected, canceled, or reactivated by the Bacs network. Check [mandate.status](https://docs.stripe.com/api/mandates/object.md#mandate_object-status) to determine whether the mandate can continue to be used. | Yes, if the new status is `active` |
| `payment_method.automatically_updated` | Occurs when a customer’s bank account details change. | Yes |

These events are available in the [Dashboard](https://dashboard.stripe.com/events), and you can configure a *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) to handle them programmatically.

## Pay by Bank Recurring (Private preview) 

Pay by Bank Recurring is now available in private preview for users of Stripe Elements and the PaymentIntents API. It combines an initial [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank.md) payment with a Bacs Direct Debit mandate for recurring payments.

**Benefits**

- **Instant first payment**: Confirm the initial payment immediately, saving 7 business days compared to Bacs Direct Debit.
- **Faster payouts**: Receive the initial payout within 3 business days, saving 4 business days.
- **Fewer disputes**: The initial payment is strongly authenticated and can’t be disputed.
- **Instant bank verification**: Verify account ownership and the account holder’s name immediately.

Sign in to Stripe to request access to the Pay by Bank Recurring private preview.

## Stripe product support 
Checkout UIs:
  ✓ Full page (Recommended)
  ✓ Payment Links
  ✓ Embedded form
  ✓ Payment Element
  ✗ Express Checkout Element
  ✗ Payment Method Messaging Element
  ✗ In-app payments

Products:
  ✗ Managed Payments
  ✓ Billing
  ✓ Invoicing
  ✓ Customer Portal
  ✗ Radar
  ✗ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✓ Payment Intents with setup_future_usage
  ✗ Setup Intents
  ✗ Off-session payments
### Integration guides 

Use one of these guides to integrate Bacs Direct Debit:

- [Accept a Bacs Direct Debit payment](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md)
- [Save Bacs Direct Debit details for future payments](https://docs.stripe.com/payments/bacs-debit/save-bank-details.md)
- [Use Bacs Direct Debit with Checkout](https://docs.stripe.com/checkout/quickstart.md)
- [Use Bacs Direct Debit with Elements](https://docs.stripe.com/payments/quickstart.md)
- [Use Bacs Direct Debit with Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Use Bacs Direct Debit with Payment Links](https://docs.stripe.com/payment-links.md)
- [Use Bacs Direct Debit with Subscriptions](https://docs.stripe.com/billing/subscriptions/bacs-debit.md)

The Payment Element can’t create Bacs Direct Debit SetupIntents; use Checkout in setup mode instead. Express Checkout Element doesn’t support Bacs Direct Debit.

### Connect requirements 

Platforms in [supported business locations](https://docs.stripe.com/payments/bacs-debit.md#bacs_debit-business-locations) can accept Bacs Direct Debit payments using [destination charges](https://docs.stripe.com/connect/destination-charges.md) with or without [on_behalf_of](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-on_behalf_of).

When you omit `on_behalf_of`, the platform is the [settlement merchant](https://docs.stripe.com/connect/destination-charges.md#settlement-merchant).

[Enable Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit.md#enablement) on the platform before accepting payments. When using `on_behalf_of`, [request the bacs_debit_payments capability](https://docs.stripe.com/connect/account-capabilities.md) for the connected account, which must be in a supported business location.

Requesting the capability with `settings.bacs_debit_payments.display_name` enables Custom Branding for that connected account. To retain Stripe branding, omit the display name or set it to `Stripe`. Each account using Custom Branding incurs a 50 GBP monthly fee.

## Timing 

With Bacs Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for Bacs Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

It takes 4 business days to confirm the success or failure of a Bacs Direct Debit payment when a mandate is already in place and 7 business days when you must collect a new mandate.

In some cases, the bank might notify us of a payment failure after the payment has been marked as successful in your Stripe account. In this case the payment failure is identified as a dispute with the appropriate reason code.

The following table describes the settlement timings for Bacs Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

For a successful Bacs Direct Debit payment submitted with an existing mandate, funds typically leave the customer’s bank account at T+2. The T+3 **Payment Success** timing in the table refers to when the associated PaymentIntent succeeds, not when the customer’s account is debited.

| Settlement type | Payment Success | Funds Available | Cutoff time |
| --- | --- | --- | --- |
| Standard Settlement | T+3 at 21:00 UTC | T+4 at 00:00 UTC | 20:00 London time (GMT or BST, depending on the time of year) |

When you collect a new mandate, the typical timeline in business days is:

| Timing | Event |
| --- | --- |
| T+0 | Mandate submitted |
| T+3 | Mandate is active and the payment is submitted |
| T+5 | Funds leave the customer’s bank account |
| T+7 | Funds are available in Stripe |

### Payment status notifications

Payment status events differ by integration. Configure your event destination to receive the events for your integration. You won’t receive every event in the table for every integration.

| Payment stage | PaymentIntents | Checkout |
| --- | --- | --- |
| Submitted and awaiting outcome | [payment_intent.processing](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.processing) | [checkout.session.completed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.completed) |
| Payment succeeded | [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.succeeded) | [checkout.session.async_payment_succeeded](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_succeeded) |
| Payment failed | [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md#event_types-payment_intent.payment_failed) | [checkout.session.async_payment_failed](https://docs.stripe.com/api/events/types.md#event_types-checkout.session.async_payment_failed) |

The `checkout.session.completed` event confirms that the customer submitted and authorized the Checkout form. It doesn’t mean the asynchronous Bacs payment succeeded. Wait for `checkout.session.async_payment_succeeded` or `checkout.session.async_payment_failed` to determine the outcome.

## Debit notifications 

Bacs requires notifying customers when their payment details are collected and confirmed, and before you debit their account. Stripe sends these emails by default, except for enterprise accounts with a custom service user number (SUN). You can [customize their colors and logo](https://dashboard.stripe.com/account/branding).

To send your own notifications, follow the [eligibility requirements and approval process](https://docs.stripe.com/payments/bacs-debit/email-customization.md#approval-process).

## Custom Branding 

Custom Branding displays your business name on customer bank statements, Stripe Checkout, and customer emails. Enable it in [Bacs Direct Debit settings](https://dashboard.stripe.com/settings/payment_methods). For Express or Custom connected accounts, set [settings.bacs_debit_payments.display_name](https://docs.stripe.com/api/accounts/object.md#account_object-settings-bacs_debit_payments-display_name) during account creation or in an account update.

If you request the capability without a display name, the account uses Stripe branding. Custom Branding costs 50 GBP per active month. Custom branding typically takes 10 business days to become active. New mandates created after activation show your business name. To expedite activation or apply branding to multiple connected accounts for one fee, [contact support](https://support.stripe.com/contact). Inactive branding eventually reverts to Stripe branding; if you have no active mandates, you can also revert it in Bacs Direct Debit settings.

## Billing retries 

Enable [Direct Debit retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#direct-debit-retries) to have Stripe automatically retry failed Direct Debit payments caused by insufficient funds. You can enable retries for [recurring subscription invoices](https://dashboard.stripe.com/revenue_recovery/retries), [one-off invoices](https://dashboard.stripe.com/settings/billing/invoices/general), or both.

Stripe can automatically retry each failed Bacs Direct Debit payment up to 2 times, no more than 30 days after the original payment attempt.

Debit failure fees aren’t charged for retry attempts that we initiate automatically.

## Customer experience 

#### 1. Select Bacs Direct Debit

On desktop and mobile web, the customer selects Bacs Direct Debit as the payment method.

#### 2. Enter bank details

The customer enters their bank account details.

#### 3. Authorize the mandate

The customer reviews and accepts the Bacs Direct Debit mandate.

#### 4. Payment submitted

The customer submits the payment and returns to your site. The payment remains processing while Stripe submits the mandate and debit. Final confirmation typically takes 4 business days with an existing mandate, or up to 7 business days when collecting a new mandate. This web flow doesn't imply support for native mobile SDKs.

### Transaction identifiers 

By default, a customer’s bank statement identifies Stripe as the service user and includes the mandate reference. [Custom Branding](https://docs.stripe.com/payments/bacs-debit.md#custom-branding) changes the displayed service-user name for new mandates.

Retrieve the mandate-level reference from [Mandate.payment_method_details.bacs_debit.reference](https://docs.stripe.com/api/mandates/object.md#mandate_object-payment_method_details-bacs_debit-reference). For Connect payments, retrieve the Mandate in the account context that owns the payment and mandate.

If a customer asks about a debit, request the debit date and amount, the bank account’s last 4 digits, the service-user name shown on the statement, and the mandate reference. Bacs Direct Debit doesn’t support transaction-level statement descriptors.

### What customers see after submission 

Payment confirmation happens asynchronously after customers submit the payment.

With Checkout, customers return to your confirmation page after they submit the payment. Tell them that you collected their payment details and that the payment is processing. Don’t tell them the payment succeeded until you receive the success event.

Stripe sends mandate confirmation and advance debit notifications by default. These confirm the mandate and notify the customer about a debit. They aren’t payment-success receipts. When the payment succeeds, handle the appropriate [post-payment event](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md#async) to update the order and send your own payment or order confirmation if needed.

The custom mandate setup confirmation isn’t a payment-success confirmation. See the [custom mandate requirements](https://docs.stripe.com/payments/bacs-debit/mandate-collection-requirements.md).

### Checkout authorization deadline 

With Checkout, customers must complete authorization before the Checkout Session expires. Sessions expire after 24 hours by default. You can configure an expiration between 30 minutes and 24 hours after creation. This deadline is separate from Bacs payment processing time. See [Checkout Session expiration](https://docs.stripe.com/payments/checkout/how-checkout-works.md#expiration).

The Bacs documentation doesn’t specify a separate authorization timeout for custom integrations. Don’t treat the 4–7-business-day processing period as an authorization deadline.

## Enable Bacs Direct Debit 

If you use Stripe front-end products, enable Bacs Direct Debit in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration requires manually listing payment methods, you can [configure Bacs Direct Debit as an accepted payment method](https://docs.stripe.com/payments/bacs-debit/accept-a-payment.md).
