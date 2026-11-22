<!-- Source URL: https://docs.stripe.com/payments/nz-bank-account -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# New Zealand BECS Direct Debit payments

Learn how to accept New Zealand BECS Direct Debit payments.

Stripe users in New Zealand can accept New Zealand BECS Direct Debit payments directly from customers with a New Zealand bank account.

You must collect the customer’s bank account information and a mandate authorizing them to debit the account. Stripe can collect this information and mandate on behalf of your business.
Payment method family: Bank debits
Usability: Reusable
Access type: Approval required
Payment confirmation timing: Delayed
Settlement timing: Up to 2 business days (T+2)
Pricing: https://stripe.com/nz/pricing/local-payment-methods#new-zealand-becs-direct-debit
## Eligibility and availability 

### Account eligibility
Business location: NZ
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
### Verification requirements 

Using New Zealand BECS Direct Debit requires you to complete additional [identity verification](https://support.stripe.com/questions/common-questions-about-stripe-identity#how-verification-works) steps. We prompt you to complete these steps after you request access from the [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods). If you require further assistance, [contact Stripe support](https://support.stripe.com/contact).

Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for New Zealand BECS Direct Debit.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

| MCC | Description | Type |
| --- | --- | --- |
| 5094 | Precious Stones and Metals, Watches and Jewelry | Prohibited |
| 5816 | Digital Goods – Games | Prohibited |
| 5932 | Antique Shops | Prohibited |
| 5933 | Pawn Shops | Prohibited |
| 5944 | Jewelry Stores, Watches, Clocks, and Silverware Stores | Prohibited |
| 5967 | Adult Content and Services | Prohibited |
| 5972 | Stamp and Coin Stores | Prohibited |
| 7801 | Government Licensed On-line Casinos (On-Line Gambling) | Prohibited |
| 7994 | Video Game Arcades | Prohibited |
| 7995 | Betting and Casino Gambling | Prohibited |

Stripe accounts in the following countries can accept New Zealand BECS Direct Debit payments that settle in a supported currency.

APAC: NZ

Customers in the following countries can use New Zealand BECS Direct Debit.

APAC: NZ

### Payment support
Customer location: NZ
Presentment currency: NZD
Geographic coverage: ✓ Domestic, ✗ Crossborder
Transaction limits: Minimum amount: 0.50 NZD

Scheme maximum: 999,999,999.99 NZD; account limits also apply
### Transaction limits 

The maximum transaction amount in the Payment support table is the scheme maximum, not your account’s processing limit. Stripe applies separate per-transaction and weekly volume limits to your account.

- The default per-transaction limit is 10,000 NZD.
- The initial weekly volume limit is 10,000 NZD across your New Zealand BECS Direct Debit payments. This limit increases as you build a history of successful payments.

Your account’s limits can differ based on approval status and any limit increases. Payments must stay within both your applicable per-transaction and weekly volume limits, even when the payment amount is below the scheme maximum. If you need higher limits, [contact Stripe support](https://support.stripe.com/contact).

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
  Processing time: Typically 3–5 business days

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
### Refunds 

Issue New Zealand BECS Direct Debit refunds within 90 days of the original payment. Refunds typically take 3–5 business days to process. If you accidentally debit a customer, contact them immediately to avoid a payment dispute.

#### Refund process 

If you request a refund before Stripe submits the debit, Stripe cancels the payment instead of debiting your customer. To refund a successful payment, wait until the debit succeeds, then issue the refund. If you request a refund after Stripe has submitted the debit, the refund remains pending until the payment succeeds. If the payment fails, Stripe marks the pending refund as failed. When funds have been debited, the refund appears as a separate credit referencing the original payment’s statement descriptor.

#### Tracking refunds 

Retrieve the Refund and check its status to track whether the refund is pending, succeeded, or failed.

#### Bank statement appearance 

New Zealand BECS Direct Debit refunds aren’t explicitly labelled as refunds when they’re deposited into a bank account. Instead, they appear as a credit that references the original payment’s statement descriptor. Notify your customer when you issue a refund for them to identify the incoming credit.

#### Prevent double credits 

Due to longer settlement times and extended dispute windows for direct debit transactions, your customer might contact both you and their bank about the same payment. If you issue a refund while the customer’s bank also initiates a dispute, the customer might receive two credits for the same transaction.

To reduce the risk of a double credit:

- Confirm with your customer that you’re processing the refund, so they don’t independently file a dispute with their bank.
- Inform your customer of the expected processing time so they don’t assume the refund failed and escalate to their bank.
- Use Stripe to issue the refund after the original payment has fully settled.

> Issuing a refund does not prevent a dispute from being processed. A malicious customer can still file a dispute with their bank after receiving a refund, resulting in a double credit against you.

### Disputes 

#### Dispute process 

A customer can dispute a New Zealand BECS Direct Debit payment for up to 9 months from the date of the first payment if they aren’t reasonably satisfied that the Direct Debit Authority authorizes the debit. A customer can also dispute an individual payment for up to 120 days after that payment if you didn’t send the pre-debit notification, or if the notification’s amount or date differs from the debit. New Zealand BECS Direct Debit disputes are for the full payment amount.

#### Dispute notifications 

When a dispute is created, Stripe sends the `charge.dispute.created` webhook event.

#### Dispute outcomes 

If the customer’s bank rules in the customer’s favor and requests a return of funds, Stripe immediately removes the funds from your Stripe account.

> If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer might receive two credits for the same transaction. To avoid this, see the [refund guidelines](https://docs.stripe.com/payments/nz-bank-account.md#refunds).

### Mandates 

During the payment process, you must collect authorization for Stripe to debit the customer’s account on their behalf. New Zealand BECS Direct Debit calls this authorization a Direct Debit Authority, or DDA.

#### What customers authorize 

The customer authorizes Stripe to debit their bank account under a Direct Debit Authority.

#### Collect mandates 

Checkout and the Payment Element display the New Zealand BECS Direct Debit Service Terms and Conditions and collect the customer’s acceptance. If your integration doesn’t use Stripe-hosted mandate collection, you must separately display these terms and confirm the customer’s acceptance.

#### Manage mandates 

For a mandate created by a SetupIntent, read the mandate ID from `SetupIntent.mandate`, then retrieve it with `GET /v1/mandates/{id}`. You can view the mandate on the transaction’s details page in the Dashboard.

#### Cancel mandates 

Customers can cancel a Direct Debit Authority by contacting their bank or your business. To inactivate the associated mandate in Stripe, detach the PaymentMethod. Establish a new mandate before accepting further payments under a new authorization.

#### Direct Debit Authority terms 

Follow the [mandate collection instructions](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md#web-collect-details) for the required authorization language and acceptance requirements. The authority is subject to the [New Zealand BECS Direct Debit Service Terms and Conditions](https://stripe.com/nz/legal/nzbecs-customer-dd-service-terms).

#### Mandate events 

| Event name | Description |
| --- | --- |
| `mandate.updated` | Occurs whenever the customer cancels a mandate or because of a permanent debit failure. The `status` property changes to `inactive`. |

You can see the events in your Dashboard, but you should still set up a [webhook endpoint](https://docs.stripe.com/webhooks.md).

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
  ✓ Setup Intents
  ✗ Off-session payments
### Integration guides 

Follow the guide for the integration or Stripe product you use:

- [Checkout quickstart](https://docs.stripe.com/checkout/quickstart.md)
- [Elements quickstart](https://docs.stripe.com/payments/quickstart.md)
- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)
- [Manually configure New Zealand BECS Direct Debit as a payment](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md)
- [Save New Zealand BECS Direct Debit details for future payments](https://docs.stripe.com/payments/nz-bank-account/set-up-payment.md)
- [Migrate from another processor](https://docs.stripe.com/payments/nz-bank-account/migrate-from-another-processor.md)

## Timing 

The following timing applies to New Zealand BECS Direct Debit payments.

With New Zealand BECS Direct Debit, it can take several business days for funds to become available in your Stripe balance. The number of business days it takes for funds to become available is called the settlement timing. Payments are generally submitted on the same day that they’re created, but are processed on the following business day if they’re created on a non-business day or after the cutoff time.

You can access the `expected_debit_date` for New Zealand BECS Direct Debit under [payment_method_details](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details) for [Charges](https://docs.stripe.com/api/charges/object.md). This is an estimated date of when the funds might be debited. This estimate isn’t guaranteed and the actual date might vary. This information is available in API responses and in [charge.updated](https://docs.stripe.com/api/events/types.md#event_types-charge.updated), [charge.succeeded](https://docs.stripe.com/api/events/types.md#event_types-charge.succeeded), and [charge.failed](https://docs.stripe.com/api/events/types.md#event_types-charge.failed) webhook events when the debit date can be determined.

The following table describes the settlement timings for New Zealand BECS Direct Debit payments that Stripe offers. `T+x` refers to `x` business days after submission, which might differ from the payment creation date.

| Settlement type | Payment Success | Funds Available | Cutoff time |
| --- | --- | --- | --- |
| Standard Settlement | T+2 at 00:00 UTC | T+2 at 00:00 UTC | 18:20 Pacific/Auckland |

## Mandate confirmation and debit notification emails 

You must notify your customer by email within 5 days after collecting a mandate, and notify your customer of each debit no later than the day it occurs. By default, Stripe sends the mandate confirmation immediately and automatically sends the debit notifications.

If you want to turn off Stripe emails for New Zealand bank account payments and send your own emails to your customers, contact [Stripe support](https://support.stripe.com/contact) for assistance.

### Mandate confirmation emails 

Stripe sends this email immediately after collecting a mandate, which is within the required 5 days. It contains all relevant details of the mandate, including:

- The date of the mandate confirmation
- A statement that Stripe New Zealand Limited (authorization code 3143978) acts on your behalf to arrange for the funds to be debited
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
- A statement that the debit from the customer’s account will be made by Stripe New Zealand Limited (authorization code 3143978)
- The date we debit their account
- A statement that the transaction may appear on the customer’s bank statement as “Stripe New Zealand Limited”
- Your contact information, including address, email, and a phone number

## Billing retries 

Enable [Direct Debit retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries.md#direct-debit-retries) to have Stripe automatically retry failed Direct Debit payments caused by insufficient funds. You can turn on retries for [recurring subscription invoices](https://dashboard.stripe.com/revenue_recovery/retries), [one-off invoices](https://dashboard.stripe.com/settings/billing/invoices/general), or both.

Stripe can automatically retry each failed NZ BECS Direct Debit payment a maximum of 1 time, no more than 30 days after the original payment attempt. These limits differ from card retries because NZ BECS Direct Debit payments are asynchronous and can take several business days to complete.

Debit failure fees aren’t charged for retry attempts that we initiate automatically.

## Customer experience 

#### 1. Choose New Zealand BECS Direct Debit

The customer selects New Zealand BECS Direct Debit at checkout.

#### 2. Enter bank details and authorize the debit

The customer provides their name, email address, and New Zealand bank account details, then accepts the Direct Debit Authority.

#### 3. Receive submission confirmation

Checkout confirms that the debit has been submitted for processing. The payment is not yet confirmed successful.

#### 4. Receive the payment result

The business confirms the final result after Stripe reports that the payment succeeded or failed.

### Statement descriptors 

New Zealand BECS Direct Debit payments may appear on your customer’s bank statement using the payment’s statement descriptor or as “Stripe New Zealand Limited.”

You can specify a statement descriptor for an individual payment or configure an account-level statement descriptor. Stripe uses the first 12 characters. If neither is provided, Stripe falls back to your business name, then “Stripe.” A descriptor specified for an individual payment takes precedence.

For Connect, the charge type determines which account supplies the business name and default descriptor:

| Charge type | Account |
| --- | --- |
| Direct charge | Connected account |
| Destination charge | Platform |
| Separate charge and transfer | Platform |
| Destination charge with `on_behalf_of` | Platform |
| Separate charge and transfer with `on_behalf_of` | Platform |

Unlike other charge types, a destination charge or separate charge and transfer uses the platform’s default statement descriptor or business-name fallback even when you set `on_behalf_of`.

[Learn more about statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable New Zealand BECS Direct Debit 

If you use Stripe front-end products, enable New Zealand BECS Direct Debit in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure New Zealand BECS Direct Debit as a payment method](https://docs.stripe.com/payments/nz-bank-account/accept-a-payment.md).

## Prohibited business categories 

In addition to the industry and business categories listed in [Prohibited and restricted businesses](https://stripe.com/restricted-businesses), the following categories are prohibited or restricted from using New Zealand BECS Direct Debit:

- Adult content, entertainment, and sex-related products and services
- Cannabis businesses, excluding cannabidiol (CBD)
- Non-fungible tokens (NFTs)
- Payment facilitators that process payments for sub-merchants
- Peer-to-peer money transfers
- Contracts for difference (CFDs)
- Weapons and firearms
- Donation-based crowdfunding
- Creator economy and live-streaming businesses
- Open-loop gaming
- Traders in precious metals or minerals
- Any business whose activities are prohibited by applicable law or regulation, including terrorist financing, human trafficking, illegal narcotics dealing, and shell banks
