<!-- Source URL: https://docs.stripe.com/payments/boleto -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Boleto payments

Accept Boleto payments, a voucher-based payment method in Brazil.

Boleto is an official voucher-based payment method in Brazil, regulated by the Central Bank of Brazil. To complete a transaction, customers receive a voucher for the amount due and pay it before expiration at an authorized agency or bank, ATM, or online bank portal.
Payment method family: Vouchers
Usability: Reusable
Access type: Instant provisional access
Payment confirmation timing: Up to 1 business day
Settlement timing: Up to 2 business days (T+2)
Pricing: https://stripe.com/pt-br/pricing/local-payment-methods#boleto-bancario
## Eligibility and availability 

### Account eligibility
Business location: BR
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Your account might be reviewed after activation to confirm eligibility. While Boleto doesn’t enforce any additional website requirements, make sure that you provide a website that meets the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq). You can contact [Stripe support](https://support.stripe.com/) to appeal any Boleto capability restrictions.

This payment method doesn’t have any MCC requirements.

Stripe accounts in the following countries can accept Boleto payments that settle in a supported currency.

AMER: BR

Customers in the following countries can use Boleto.

AMER: BR

### Payment support
Customer location: BR
Presentment currency: BRL
Geographic coverage: ✓ Domestic, ✗ Crossborder
Transaction limits: Minimum amount: 5.00 BRL

Maximum amount: 49,999.99 BRL
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
  ✗ Partial refunds
  ✗ Full refunds

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Disputes 

Boleto doesn’t support the standard dispute process, and customers can’t file a chargeback. However, in some instances, bank-side irregularities similar to disputes can occur, such as payment mishandling. If this happens, Stripe contacts you with next steps.

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
### Get started 

To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart.md): Our drop-in UI components.

#### Other payment products

The following Stripe products also let you add Boleto from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

Check out the Boleto [sample on GitHub](https://github.com/stripe-samples/accept-a-payment).

## Customer experience 

#### 1. Select Boleto

The customer selects Boleto at checkout and provides the required contact and tax ID details.

#### 2. Receive voucher

Stripe displays a hosted voucher page where the customer can copy the Boleto number or download the voucher PDF. The voucher expires after 3 days by default, configurable from 0–60 days.

#### 3. Pay the voucher

The customer pays through a bank, ATM, authorized agency, or online bank portal. Desktop and mobile customers use the same hosted-voucher browser flow.

#### 4. Payment complete

After the customer pays, Stripe confirms the payment asynchronously, typically on the next business day, and the customer receives confirmation that the payment is complete.

### Transaction identifiers 

The Boleto voucher or bank receipt might show Stripe as the company. The exact formatting depends on the customer’s bank or payment channel.

For Boleto and other non-card payments, you can set the full [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md) using the `statement_descriptor` parameter. If you don’t set a request-level descriptor, Stripe uses the account-level statement descriptor. The `statement_descriptor_suffix` parameter only applies to card payments. A bank might display statement-descriptor information differently or omit it.

For Connect destination charges without `on_behalf_of`, the statement descriptor comes from the platform account. When you use `on_behalf_of`, it comes from the connected account, subject to legacy API-version behavior. Learn more about [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

Use `payment_intent.next_action.boleto_display_details.number` to retrieve the customer-visible Boleto number. This number identifies the voucher, but it isn’t a processor transaction ID. Boleto doesn’t expose a processor transaction ID under `latest_charge.payment_method_details.boleto`.

## Enable Boleto 

If you use Stripe front-end products, enable Boleto in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration requires manually listing payment methods, you can [configure Boleto as an accepted payment method](https://docs.stripe.com/payments/boleto/accept-a-payment.md).
