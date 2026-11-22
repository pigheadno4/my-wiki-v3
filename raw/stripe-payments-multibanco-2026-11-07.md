<!-- Source URL: https://docs.stripe.com/payments/multibanco -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Multibanco payments

Accept payments with Multibanco, a widely used payment method in Portugal.

Multibanco is a voucher-based payment method that lets customers pay by bank transfer. It’s primarily used in Portugal. Businesses in Europe and the United States can accept Multibanco payments.

Customers receive a voucher containing an entity number, reference number, and amount, then use those details to pay outside the checkout flow through online banking or at an ATM.
Payment method family: Vouchers
Usability: Single-use
Access type: Instant provisional access
Payment confirmation timing: Delayed
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-us/pricing/local-payment-methods#multibanco
## Eligibility and availability 

### Account eligibility
Business location: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Your account might be reviewed after activation to confirm eligibility. While Multibanco doesn’t enforce any additional website requirements, make sure that you provide a website that meets the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq). You can contact [Stripe support](https://support.stripe.com/) to appeal any Multibanco capability restrictions.

Stripe accounts in the following countries can accept Multibanco payments that settle in a supported currency.

AMER: US

EMEA: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

Customers in the following countries can use Multibanco.

EMEA: PT

### Payment support
Primary customer market: PT
Presentment currency: EUR
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 0.50 EUR

Maximum amount: 99,999.00 EUR
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
  Submission window: 456 days
  Processing time: Typically 1 day, with timing varying by bank

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Refunds 

You can issue a full or partial refund for a Multibanco payment within 456 days of the original payment through the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). Funds typically reach the customer’s bank account within 1 day, but timing varies by bank. You can’t cancel a Multibanco refund after submitting it.

#### Refund process 

Multibanco refunds are sent directly to the customer’s bank account.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

#### Refund reference 

When a Multibanco refund’s `status` changes to `succeeded`, you can share the refund reference in [destination_details.multibanco.reference](https://docs.stripe.com/api/refunds/object.md#refund_object-destination_details-multibanco-reference) with the customer, if available.

### Disputes 

The risk of fraud or unrecognized payments is low with Multibanco because the customer must push funds from their bank account. As a result, there’s no dispute process that can result in a chargeback and funds withdrawn from your Stripe account.

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

#### 1. Select Multibanco

The customer selects Multibanco at checkout and provides their email address.

#### 2. Receive voucher details

Stripe displays the voucher's entity number, reference number, amount, and expiration. The voucher expires 7 days after creation. You can also [configure Stripe to email the voucher to the customer](/payments/multibanco/accept-a-payment?payment-ui=checkout#instruction-emails).

#### 3. Pay the voucher

The customer uses the voucher details to pay through online banking or at an ATM.

#### 4. Wait for confirmation

The PaymentIntent remains in `requires_action` while awaiting payment. The customer isn't redirected back to your site after paying. Payment confirmation can be delayed by several days, particularly over weekends. After the voucher expires, the PaymentIntent can remain in `processing` for up to 4 days while Stripe waits for delayed payment notifications.

#### 5. Payment complete

Stripe confirms the payment asynchronously and changes the PaymentIntent to `succeeded`. You can then fulfill the order.

### Statement descriptors 

Set `statement_descriptor` to specify the descriptor Stripe sends for a Multibanco payment. The value shown on the customer’s bank statement varies by bank. If you don’t set a payment-level descriptor, Stripe uses the account-level statement descriptor.

For Connect payments, direct charges and charges that use `on_behalf_of` use the connected account’s statement descriptor. Destination charges and separate charges and transfers that don’t use `on_behalf_of` use the platform’s statement descriptor. Learn more about [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable Multibanco 

If you use Stripe front-end products, enable Multibanco in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure Multibanco as a payment method](https://docs.stripe.com/payments/multibanco/accept-a-payment.md).

For connected accounts that use the Express Dashboard or no Stripe-hosted Dashboard, follow the instructions to [request capabilities for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). Request the `multibanco_payments` capability and check that its status is `active` before accepting Multibanco payments.
