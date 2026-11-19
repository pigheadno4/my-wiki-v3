<!-- Source URL: https://docs.stripe.com/payments/grabpay -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# GrabPay payments

A digital wallet and common payment method in Southeast Asia.

GrabPay is a digital wallet developed by Grab. Customers maintain a balance in their GrabPay wallet. To pay, customers are redirected to GrabPay, authenticate the transaction using a one-time password, and are then redirected back to your website.
Payment method family: Wallets
Usability: Single-use
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/undefined/pricing/local-payment-methods#grabpay
## Eligibility and availability 

### Account eligibility
Business location: MY, SG
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Stripe accounts in the following countries can accept GrabPay payments that settle in a supported currency.

APAC: MY, SG

Customers in the following countries can use GrabPay.

APAC: MY, SG

### Payment support
Customer location: MY, SG
Presentment currency: MYR, SGD
Geographic coverage: ✓ Domestic, ✗ Crossborder
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
  Submission window: 90 days
  Processing time: 5 minutes

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Refunds 

You have up to 90 days from the original payment to submit a refund using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). This is the maximum the payment method allows—your return policy determines what you offer customers.

Refunds for GrabPay payments are asynchronous and take up to 5 minutes to complete. You can’t cancel GrabPay refunds.

#### Refund process 

GrabPay refunds are never processed as reversals. GrabPay handles the refund directly and returns the funds to the customer’s original payment source, which is either their GrabPay balance or linked payment method. The customer sees the refund reflected in their GrabPay account or funding source.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

GrabPay requires customers to authenticate payments directly with the GrabPay app, which reduces the risk of fraud and unrecognized transactions. As a result, GrabPay doesn’t support the standard dispute process—customers can’t file a chargeback, and funds are never withdrawn from your Stripe balance because of a dispute.

If a customer contacts GrabPay about a payment, they might be directed back to you. You can then issue a full or partial refund.

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
  ✓ Invoicing
  ✗ Customer Portal
  ✗ Radar
  ✗ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✗ Payment Intents with setup_future_usage
  ✗ Setup Intents
  ✗ Off-session payments
## Branding guidelines 

Use the [branding guidelines](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay_Online_Partners_Brand_Guidelines.pdf) provided by GrabPay when building your checkout page. Assets such as logos and buttons are available for download [as a ZIP file](https://d37ugbyn3rpeym.cloudfront.net/docs/files/GrabPay-Branding-Guidelines-with-Logos-and-Artworks.zip).

## Customer experience 

#### 1. Select GrabPay

The customer selects GrabPay at checkout.

#### 2. Authenticate the payment

The customer is redirected in their browser or webview to GrabPay and authenticates with a one-time password. They must complete authentication within 15 minutes of inactivity; three incorrect one-time password attempts fail authentication.

#### 3. Complete the payment

The customer returns to the website or app through the configured return URL, URL scheme, or universal link, where the integration displays the PaymentIntent success or failure result.

### Transaction identifiers 

Stripe sends GrabPay a descriptor constructed from the merchant descriptor and payment descriptor. When both are present, Stripe sends `<merchant descriptor> - <payment descriptor>`. When neither is present, Stripe sends `STRIPE`. GrabPay doesn’t guarantee how this descriptor appears to the customer.

For [direct charges](https://docs.stripe.com/connect/direct-charges.md), the descriptor comes from the connected account. For [destination charges](https://docs.stripe.com/connect/destination-charges.md), it comes from the platform by default. Charge and PaymentIntent IDs are separate Stripe identifiers and aren’t the GrabPay transaction identifier.

To retrieve the GrabPay transaction identifier from a PaymentIntent, expand or retrieve its latest Charge and read `latest_charge.payment_method_details.grabpay.transaction_id`.

## Enable GrabPay 

If you use Stripe front-end products, enable GrabPay in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure GrabPay as a payment method](https://docs.stripe.com/payments/grabpay/accept-a-payment.md).

Check out the GrabPay [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).
