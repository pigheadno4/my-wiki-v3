<!-- Source URL: https://docs.stripe.com/payments/amazon-pay -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Amazon Pay payments

Learn how to accept payments with Amazon Pay.

[Amazon Pay](https://pay.amazon.com/) is a wallet payment method that lets your customers check out the same way as on Amazon.com.
Payment method family: Wallets
Usability: Reusable
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-us/pricing/local-payment-methods#amazon-pay
## Eligibility and availability 

### Account eligibility
Business location: AT, BE, CH, CY, DE, DK, ES, FR, GB, HU, IE, IT, LU, NL, PT, SE, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for Amazon Pay.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

| MCC | Description | Type |
| --- | --- | --- |
| 6051 | Cryptocurrency exchanges and wallets | Prohibited |

Stripe accounts in the following countries can accept Amazon Pay payments that settle in a supported currency.

AMER: US

EMEA: AT, BE, CH, CY, DE, DK, ES, FR, GB, HU, IE, IT, LU, NL, PT, SE

Customers worldwide can use Amazon Pay.

### Payment support
Customer location: Worldwide
Presentment currency: AUD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, USD, ZAR
Geographic coverage: ✓ Domestic, ✓ Crossborder
### Currency availability 

| Business location | Supported currencies |
| --- | --- |
| Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, Switzerland, United Kingdom | AUD, CHF, DKK, EUR, GBP, HKD, JPY, NOK, NZD, SEK, USD, ZAR |
| United States | USD |

The minimum amount is 0.50 USD, 0.50 GBP, or 0.50 EUR. For other currencies, see [minimum charge amounts](https://docs.stripe.com/currencies.md#minimum-and-maximum-charge-amounts).

### Available payment methods 

Use Amazon Pay to store card credentials. Amazon Pay also supports the following alternative payment methods:

| Country | Payment methods |
| --- | --- |
| United States | Amazon Store Card, Amazon Store Card Installments, Amazon Visa Card Installments, Citi Flex Pay, Affirm, and Shop with Points |
| Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, Switzerland | SEPA Direct Debit |

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
  Submission window: 90 days
  Processing time: 14 days

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
  Submission window: 240 days
### Refunds 

You have up to 90 days from the original payment to submit a refund using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). For some Amazon Pay transactions that use non-card payment methods, refunds can take up to 14 calendar days to return a final status.

#### Refund process 

After Stripe initiates a refund, Amazon Pay returns the funds to the customer’s original form of payment.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

Customers have up to 240 calendar days from the date of purchase to file Amazon Pay disputes.

#### Dispute process 

1. **Dispute opened**: Amazon Pay opens a dispute. Stripe immediately withholds the disputed amount and the applicable dispute fee from your balance. Chargebacks and A-to-z Guarantee claims have different evidence deadlines. See [Responding to disputes](https://docs.stripe.com/payments/amazon-pay.md#responding-to-disputes).
2. **Decision**: Amazon Pay reviews your evidence and issues a final decision within 90 calendar days after evidence submission.

#### Dispute notifications 

When an Amazon Pay dispute is opened, Stripe notifies you through:

- Email
- The [Stripe Dashboard](https://dashboard.stripe.com/disputes)
- A [charge.dispute.created](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) webhook event

The dispute reason is available in the Dashboard and in the `reason` field of the [Dispute object](https://docs.stripe.com/api/disputes/object.md). The evidence submission deadline is available in the Dashboard and in the [evidence_details.due_by](https://docs.stripe.com/api/disputes/object.md#dispute_object-evidence_details-due_by) field of the Dispute object.

#### Responding to disputes 

You typically have 10 calendar days from dispute creation to respond to a chargeback, and 6 calendar days to respond to an A-to-z Guarantee claim. Always use the deadline shown in the Dashboard or in the [evidence_details.due_by](https://docs.stripe.com/api/disputes/object.md#dispute_object-evidence_details-due_by) field of the Dispute object.

Upload compelling evidence that you fulfilled the purchase order. This evidence can include a received return confirmation for shipped goods returned by the customer, the tracking ID, the shipping date, a record of purchase for intangible goods such as an IP address or email receipt, or a record of purchase for services or physical goods such as a phone number or proof of receipt. Include as much detail as possible from the information the customer provided at checkout.

You can submit evidence and manage Amazon Pay disputes in the [Dashboard](https://dashboard.stripe.com/disputes) or programmatically using the [Disputes API](https://docs.stripe.com/api/disputes/update.md). In the Dashboard, go to the **Needs Response** tab, click the disputed payment, then click **Counter dispute** to submit your evidence, or **Accept dispute** to accept the loss. To submit evidence through the API, upload supporting files using the [Files API](https://docs.stripe.com/api/files/create.md) and include the returned file IDs when you update the [Dispute Evidence object](https://docs.stripe.com/api/disputes/update.md).

#### Dispute outcomes 

If Amazon Pay resolves the dispute in your favor, Stripe returns the disputed amount and the dispute fee to your Stripe balance.

If they rule in favor of the customer, the balance charge becomes permanent.

#### Authentication and fraud 

Customers must authenticate Amazon Pay payments by signing in to their Amazon account. This requirement helps reduce the risk of fraud and unrecognized payments.

#### A-to-z Guarantee claims 

Amazon Pay offers an [A-to-z Guarantee](https://www.amazon.com/gp/help/customer/display.html?nodeId=GQ37ZCNECJKTFYQV) that protects customers from issues related to timely delivery and the condition of their items. Customers have up to 90 calendar days from the date of purchase to file a claim against this guarantee. A claim follows the same dispute process described above, but has a shorter evidence deadline and doesn’t incur a dispute fee. In the Dispute object, `payment_method_details.amazon_pay.dispute_type` is `claim` for an A-to-z Guarantee claim.

You can also [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

## Stripe product support 
Checkout UIs:
  ✓ Full page (Recommended)
  ✓ Payment Links
  ✓ Embedded form
  ✓ Payment Element
  ✓ Express Checkout Element
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

#### 1. Select Amazon Pay

The customer selects Amazon Pay at checkout.

#### 2. Authorize with Amazon

Stripe redirects the customer to Amazon's hosted checkout page. The customer signs in and completes the payment using the shipping and payment information stored in their Amazon account. Amazon controls how long the customer has to complete this step; Stripe doesn't configure an authorization-session timeout.

#### 3. Complete payment

After Amazon authorizes the payment, Stripe confirms it immediately and Amazon redirects the customer to the merchant's success or confirmation page.

### Transaction identifiers 

Stripe passes your payment’s statement descriptor to Amazon Pay. Amazon Pay and the customer’s funding source control how it appears on the customer’s statement.

To retrieve the Amazon Pay transaction ID for a payment, [retrieve the PaymentIntent](https://docs.stripe.com/api/payment_intents/retrieve.md) with `expand[]=latest_charge`, then read `latest_charge.payment_method_details.amazon_pay.transaction_id`. Without expansion, `latest_charge` is a Charge ID. You can also [retrieve the referenced Charge](https://docs.stripe.com/api/charges/retrieve.md) and read `payment_method_details.amazon_pay.transaction_id` on the Charge object. The field might be absent when Amazon doesn’t provide a transaction ID.

## Enable Amazon Pay 

If you use Stripe front-end products, enable Amazon Pay in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration requires manually listing payment methods, you can [configure Amazon Pay as an accepted payment method](https://docs.stripe.com/payments/amazon-pay/accept-a-payment.md).
