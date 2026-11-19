<!-- Source URL: https://docs.stripe.com/payments/bancontact -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Bancontact payments

Learn about Bancontact, a common payment method in Belgium.

Bancontact is a common online payment method in Belgium. Customers use a Bancontact card or mobile app linked to a Belgian bank account to make online payments.
Payment method family: Bank redirects
Usability: Single-use
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-us/pricing/local-payment-methods#bancontact
## Eligibility and availability 

### Account eligibility
Business location: AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HK, HR, HU, IE, IT, JP, LI, LT, LU, LV, MT, MX, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Your account might be reviewed after activation to confirm eligibility. While Bancontact doesn’t enforce any additional website requirements, make sure that you provide a website that meets the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq). You can contact [Stripe support](https://support.stripe.com/) to appeal any Bancontact capability restrictions.

Stripe accounts in the following countries can accept Bancontact payments that settle in a supported currency.

AMER: CA, MX, US

EMEA: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

APAC: AU, HK, JP, NZ, SG

Customers in the following countries can use Bancontact.

EMEA: BE

### Payment support
Customer location: BE
Presentment currency: EUR
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 0.50 EUR
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
  Submission window: 2 years
  Processing time: Typically 2–5 days, with timing varying by bank

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Refunds 

You can issue a full or partial refund for a Bancontact payment within 730 days of the original payment through the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). Funds typically reach the customer’s bank account within 2–5 days. You can’t cancel a Bancontact refund after submitting it.

#### Refund process 

Bancontact refunds are always processed as a separate credit to the customer’s bank account. Unlike card payments, they’re never issued as a reversal. The refund won’t be explicitly labeled as a refund on the customer’s bank statement. We recommend notifying your customer when you issue a refund so they can identify the incoming credit.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

#### Refund reference 

When a Bancontact refund’s status changes to `succeeded`, you can share the refund reference in [destination_details.eu_bank_transfer.reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-eu_bank_transfer-reference) with the customer, if available.

### Disputes 

Bancontact requires customers to authenticate payments directly with their bank, which reduces the risk of fraud and unrecognized transactions. As a result, Bancontact doesn’t support the standard dispute process—customers can’t file a chargeback through their bank, and funds are never withdrawn from your Stripe balance because of a dispute.

If a customer contacts their bank about a payment made with Bancontact, the bank directs them back to you. You can then issue a full or partial refund.

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
  ✓ Managed Payments
  ✓ Billing
  ✓ Invoicing
  ✗ Customer Portal
  ✓ Radar
  ✗ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✗ Payment Intents with setup_future_usage
  ✗ Setup Intents
  ✗ Off-session payments

1. Only supports send_invoice collection method.
## Customer experience 

#### 1. Select Bancontact

The customer selects Bancontact at checkout on the business's page.

#### 2. Continue to Bancontact

The customer is redirected to a Bancontact web page on desktop or mobile.

#### 3. Choose how to pay

On desktop, the customer enters Bancontact card details or scans a QR code that opens the Bancontact app. On mobile, the customer enters card details or taps a button that deep-links to the app.

#### 4. Authorize the payment

The customer authenticates the payment using their Bancontact card or the Bancontact app within 1 hour.

#### 5. See the payment result

Bancontact immediately confirms whether the payment succeeded or failed.

#### 6. Return to the business

After authorization, the customer is automatically returned to the business's page for confirmation.

### Statement descriptors 

Set `statement_descriptor` to specify the descriptor Stripe sends for a Bancontact payment. The value shown on the customer’s bank statement varies by bank. Non-card payments use `statement_descriptor`, while `statement_descriptor_suffix` applies only to card payments. If you don’t set a payment-level descriptor, Stripe uses the account-level statement descriptor.

For Connect destination charges, Stripe uses the platform’s statement descriptor by default. If you set `on_behalf_of`, Stripe uses the connected account’s statement descriptor instead. Learn more about [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable Bancontact 

If you use Stripe front-end products, enable Bancontact in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration requires manually listing payment methods, you can [configure Bancontact as an accepted payment method](https://docs.stripe.com/payments/bancontact/accept-a-payment.md).

For connected accounts that use the Express Dashboard or no Stripe-hosted Dashboard, follow the instructions to [request capabilities for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting). Request the `bancontact_payments` capability and check that its status is `active` before accepting Bancontact payments.
