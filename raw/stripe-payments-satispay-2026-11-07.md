<!-- Source URL: https://docs.stripe.com/payments/satispay -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Satispay payments

Learn how to accept payments with Satispay, a digital wallet popular with Italian customers.

[Satispay](https://satispay.com/) is a stored value wallet payment method available to merchants on Stripe. When customers select Satispay as their payment method, Stripe redirects them to Satispay’s website to finish the transaction. You get immediate notification of whether the payment succeeded.
Payment method family: Wallets
Usability: Reusable
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/it-it/pricing/local-payment-methods#satispay
## Eligibility and availability 

### Account eligibility
Business location: AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HK, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✗ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for Satispay.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

| MCC | Description | Type |
| --- | --- | --- |
| 4761 | OTA and Travel Package | Prohibited |
| 4829 | Money Orders - Wire Transfers | Prohibited |
| 5701 | Software | Prohibited |
| 5913 | Software | Prohibited |
| 5933 | Pawn Shops | Prohibited |
| 5960 | Direct Marketing - Insurance Services | Prohibited |
| 5962 | Direct Marketing - Travel | Prohibited |
| 5963 | Door-To-Door Sales | Prohibited |
| 5964 | Direct Marketing - Catalog Merchant | Prohibited |
| 5965 | Direct Marketing - Combination Catalog and Retail Merchant | Prohibited |
| 5966 | Direct Marketing - Outbound Telemarketing | Prohibited |
| 5967 | Adult Content and Services | Prohibited |
| 5968 | Direct Marketing - Subscription | Prohibited |
| 5969 | Direct Marketing - Other | Prohibited |
| 6010 | Manual Cash Disburse | Prohibited |
| 6011 | Financial Service | Prohibited |
| 6012 | Financial Institutions | Prohibited |
| 6051 | Cryptocurrency exchanges and wallets | Prohibited |
| 6211 | Security Brokers and Dealers | Prohibited |
| 6540 | Non-FI, Stored Value Card Purchase and Load | Prohibited |
| 7273 | Dating and Escort Services | Prohibited |
| 7277 | Counseling Services | Prohibited |
| 7278 | Buying and Shopping Services | Prohibited |
| 7321 | Credit Reporting Agencies | Prohibited |
| 7322 | Financial Service | Prohibited |
| 7361 | Employment and Temp Agencies | Prohibited |
| 7393 | Detective Agencies | Prohibited |
| 7800 | Government-Owned Lotteries (US Region only) | Prohibited |
| 7801 | Government Licensed On-line Casinos (On-Line Gambling) | Prohibited |
| 7802 | Government-Licensed Horse and Dog Racing | Prohibited |
| 7995 | Betting and Casino Gambling | Prohibited |
| 9406 | Government-Owned Lotteries (Non-US region) | Prohibited |
| 9754 | Lodging - Hotels, Motels, and Resorts (Continued) | Prohibited |

Stripe accounts in the following countries can accept Satispay payments that settle in a supported currency.

AMER: CA, US

EMEA: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

APAC: AU, HK, JP, SG

Customers in the following countries can use Satispay.

EMEA: IT

### Payment support
Customer location: IT
Presentment currency: EUR
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 0.50 EUR

Maximum amount: 999,999.99 EUR
## Capabilities 
Recurring payments: ✓ Supported

Payment authorizations:
  ✗ Extended authorizations
  ✗ Flexible extended authorizations
  ✗ Incremental authorizations
  ✗ Decremental authorizations
  ✗ Re-authorizations

Payment captures:
  ✓ Manual capture
  ✓ Partial capture
  ✗ Multi-capture
  ✗ Over-capture

Refunds:
  ✓ Partial refunds
  ✓ Full refunds
  Submission window: 180 days
  Processing time: 5 minutes

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
  Submission window: 120 days
### Refunds 

Satispay requires that you submit a refund within 180 days from the original payment using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). This is the maximum the payment method allows. Your return policy determines what you offer customers.

Refunds for Satispay payments are asynchronous and take up to 5 minutes to complete. You can’t cancel Satispay refunds.

#### Refund process 

Satispay refunds are never processed as reversals. Satispay always returns the refunded amount to the customer’s Satispay wallet balance.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

Customers have up to 120 calendar days from the date of purchase to file Satispay disputes.

#### Dispute process 

1. **Dispute opened**: Satispay opens a dispute. Stripe immediately withholds the disputed amount from your balance. You have 15 calendar days to submit evidence.
2. **Decision**: Satispay reviews your evidence and issues a final decision within 25 calendar days of dispute creation.

#### Dispute notifications 

When Satispay disputes are opened, Stripe notifies you through:

- Email
- The [Stripe Dashboard](https://dashboard.stripe.com/disputes)
- A [charge.dispute.created](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) event

The dispute reason is available in the Dashboard and in the `reason` field of the [Dispute object](https://docs.stripe.com/api/disputes/object.md). The evidence submission deadline is available in the Dashboard and in the `evidence_details.due_by` field of the Dispute object.

#### Responding to disputes 

You have 15 calendar days from dispute creation to submit evidence.

We request that you upload compelling evidence proving that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include the:

- Tracking ID
- Shipping date
- Record of purchase for intangible goods, such as IP address or email receipt
- Record of purchase for services or physical goods, such as phone number or proof of receipt
- Record of refund (for purchases you’ve already refunded)

You can submit evidence and manage Satispay disputes in the [Dashboard](https://dashboard.stripe.com/disputes) or programmatically using the [Disputes API](https://docs.stripe.com/api/disputes/update.md). In the Dashboard, go to the **Needs response** tab, click the disputed payment, then click **Counter dispute** to submit your evidence, or **Accept dispute** to accept the loss. To submit evidence through the API, upload supporting files using the [Files API](https://docs.stripe.com/api/files/create.md) and include the returned file IDs when you update the [Dispute Evidence object](https://docs.stripe.com/api/disputes/update.md).

#### Dispute outcomes 

If Satispay resolves the dispute in your favor, Stripe returns the disputed amount to your Stripe balance.

If they rule in favor of the customer, the balance charge becomes permanent.

### Mandates 

Saving a Satispay payment method for future payments requires the customer’s authorization. The customer grants this authorization with Satispay when they set up the payment method, and Stripe stores it as a Mandate associated with the PaymentMethod.

#### What customers authorize 

When a customer saves Satispay for future use, they authorize your business to charge their Satispay account for future payments under the agreed terms. Stripe stores this authorization and associates it with the PaymentMethod.

#### Collect mandates 

When you use Checkout or the Payment Element, Stripe records the customer’s authorization automatically. The customer approves future payments with Satispay during setup. Satispay collects this authorization directly from the customer, so you don’t need to display additional mandate language in custom payment flows.

#### Manage mandates 

After saving Satispay with a SetupIntent, use its `mandate` ID to retrieve mandate details with the [Mandates API](https://docs.stripe.com/api/mandates.md). If you save Satispay with a PaymentIntent, use its `payment_method` ID for future payments instead of looking for a top-level `mandate` field.

#### Cancel mandates 

Customers can revoke their authorization with Satispay at any time. When this happens, Stripe sends a `mandate.updated` webhook event and you can no longer use the PaymentMethod for future payments. To stop future payments yourself, [detach the PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) from the customer.

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
  ✓ Off-session payments
## Customer experience 

#### 1. Select payment method

The customer selects Satispay at checkout.

#### 2. Redirect

The customer is redirected to a Satispay-hosted page.

#### 3. Identify

The customer enters their phone number to receive a payment request in the Satispay app, or scans the QR code on the page with the Satispay app.

#### 4. Authorize

The customer approves the payment in the Satispay app.

#### 5. Payment complete

The payment is confirmed immediately and the customer is automatically redirected back to your website.

### Statement descriptors 

Satispay payments appear in the customer’s Satispay app with your account’s [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md).

To override the default statement descriptor, set `statement_descriptor` when creating the `PaymentIntent`. For [Payment Links](https://docs.stripe.com/payment-links.md) or [Checkout](https://docs.stripe.com/payments/checkout.md), use `payment_intent_data.statement_descriptor`. Learn more about [overriding the default statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md#override-the-default-statement-descriptor).

The [charge type](https://docs.stripe.com/connect/charges.md) of Connect payments determines whether the platform’s or the connected account’s statement descriptor appears. See [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable Satispay 

If you use Stripe front-end products, enable Satispay in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration requires manually listing payment methods, you can [configure Satispay as an accepted payment method](https://docs.stripe.com/payments/satispay/accept-a-payment.md).
