<!-- Source URL: https://docs.stripe.com/payments/paypay -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# PayPay payments

Learn about PayPay, a digital wallet payment method in Japan.

PayPay is a popular digital payment platform and mobile wallet service in Japan.
Payment method family: Wallets
Usability: Single-use
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/jp/pricing/local-payment-methods#paypay
## Eligibility and availability 

### Account eligibility
Business location: JP
Account type: ✓ Merchant, ✗ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
Your account might be reviewed after activation to confirm eligibility. In addition to meeting the criteria above, you must also provide a website that meets the following requirements in addition to the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq):

- Business information must match what was provided during onboarding.
- Must clearly indicate the products or services for sale.
- Must clearly indicate the payment flow.
- Must specify if selling digital goods or services.
- Must have a complete SCTA (Specific Conditions of Transaction Acceptance) page.

You can contact [Stripe support](https://support.stripe.com/) to appeal any PayPay capability restrictions.

Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for PayPay.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

| MCC | Description | Type |
| --- | --- | --- |
| 6051 | Cryptocurrency exchanges and wallets | Prohibited |

Stripe accounts in the following countries can accept PayPay payments that settle in a supported currency.

APAC: JP

Customers in the following countries can use PayPay.

APAC: JP

### Payment support
Customer location: JP
Presentment currency: JPY
Geographic coverage: ✓ Domestic, ✗ Crossborder
Transaction limits: Minimum amount: 50 JPY

Maximum amount: 1,000,000 JPY
### Payment expiration 

PayPay-side authorization expires 5 minutes after redirect. Separately, Stripe expires the payment attempt 1 hour after payment-attempt creation and reports `payment_intent_payment_attempt_expired`.

## Capabilities 
Recurring payments: ✗ Not supported

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
  Submission window: 1 year
  Processing time: 0 minutes

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Refunds 

PayPay requires that you submit a refund within 365 days from the original payment using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). This is the maximum the payment method allows. Your return policy determines what you offer customers.

Refunds for PayPay payments complete instantly. You can’t cancel PayPay refunds.

#### Refund process 

PayPay refunds are never processed as reversals. PayPay handles the refund directly and returns the funds to the customer’s original payment source, which is either their PayPay balance or linked payment method. The customer sees the refund reflected in their PayPay account or funding source.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

PayPay requires customers to authenticate payments directly with the PayPay app, which reduces the risk of fraud and unrecognized transactions. As a result, PayPay doesn’t support the standard dispute process—customers can’t file a chargeback, and funds are never withdrawn from your Stripe balance because of a dispute.

If a customer contacts PayPay about a payment, they might be directed back to you. You can then issue a full or partial refund.

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
  ✗ Billing
  ✗ Invoicing
  ✗ Customer Portal
  ✓ Radar
  ✗ Terminal
  ✗ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✗ Payment Intents with setup_future_usage
  ✗ Setup Intents
  ✗ Off-session payments
Radar support for PayPay is in private preview. Contact Stripe to request access.

## Customer experience 

#### 1. Choose PayPay

The customer chooses PayPay at checkout.

#### 2. Open PayPay

On desktop, the customer opens PayPay using a QR code or the web. On mobile, the customer opens the PayPay app or uses their browser.

#### 3. Authorize payment

The customer authorizes the payment with PayPay.

#### 4. Return and receive confirmation

PayPay returns the customer automatically after a short delay, or the customer chooses to return. Stripe immediately confirms whether the payment succeeded or failed.

In the standard redirect flow, customers leave your website or app to authorize each payment with PayPay. PayPay returns the customer automatically after a short delay, or the customer chooses to return. An eligible custom integration can instead present a separate custom QR variant while keeping its page open. Stripe immediately confirms whether the payment succeeded or failed.

### Statement descriptors 

Stripe sends a computed statement descriptor to its PayPay partner integration, using the payment’s descriptor and applicable account configuration. PayPay controls whether and how that descriptor is displayed.

See the PaymentIntent [statement_descriptor parameter](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-statement_descriptor), [statement descriptor guidance](https://docs.stripe.com/get-started/account/statement-descriptors.md), and [Connect statement descriptor guidance](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable PayPay 

If you use Stripe front-end products, enable PayPay in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure PayPay as a payment method](https://docs.stripe.com/payments/paypay/accept-a-payment.md).
