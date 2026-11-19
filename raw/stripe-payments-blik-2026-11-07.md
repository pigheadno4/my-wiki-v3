<!-- Source URL: https://docs.stripe.com/payments/blik -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# BLIK payments

BLIK is a bank debit payment method most commonly used in Poland.

BLIK is a payment method commonly used in Poland. Customers generate a six-digit code in their banking app and enter it in the payment form. Their bank then sends a push notification asking them to authorize the payment in the app. A BLIK code is valid for 2 minutes, but the customer must authorize the payment within 60 seconds after it starts. Customers typically approve BLIK payments in less than 10 seconds.
Payment method family: Bank debits
Usability: Reusable
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/pl/pricing/local-payment-methods#blik
## Eligibility and availability 

### Account eligibility
Business location: AT, AU, BE, BG, CA, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✓ B2B, ✓ B2C
Your account might be reviewed after activation to confirm eligibility. While BLIK doesn’t enforce any additional website requirements, make sure that you provide a website that meets the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq). You can contact [Stripe support](https://support.stripe.com/) to appeal any BLIK capability restrictions.

Stripe accounts in the following countries can accept BLIK payments that settle in a supported currency.

AMER: CA, US

EMEA: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK

APAC: AU, SG

Customers in the following countries can use BLIK.

EMEA: PL

### Payment support
Customer location: PL
Presentment currency: PLN
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 2.00 PLN

Maximum amount for one-time payments: 999,999.99 PLN

Maximum amount for off-session recurring payments: 2,000 PLN per charge
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
  Submission window: 2 years
  Processing time: 120 minutes

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
### Refunds 

BLIK requires that you submit a refund within 730 days from the original payment using the [Dashboard](https://dashboard.stripe.com/payments) or [Refunds API](https://docs.stripe.com/api/refunds/create.md). This is the maximum the payment method allows. Your return policy determines what you offer customers.

Refunds for BLIK payments are asynchronous and can’t be canceled.

#### Refund process 

BLIK processes the refund to the customer’s bank account. Depending on the customer’s bank, the refund takes up to 120 minutes to complete.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

#### Dispute process 

When a customer opens a BLIK dispute, Stripe withholds the disputed amount from your balance and notifies you through the Dashboard, email, and webhook events. Submit evidence by the deadline shown on the Dispute object. BLIK reviews the evidence and notifies Stripe when it reaches a decision. BLIK doesn’t provide a guaranteed decision timeframe.

#### Dispute notifications 

When BLIK disputes are opened, Stripe notifies you through:

- Email
- The [Stripe Dashboard](https://dashboard.stripe.com/disputes)
- A [charge.dispute.created](https://docs.stripe.com/api/events/types.md#event_types-charge.dispute.created) event

The dispute reason is available in the Dashboard and in the `reason` field of the [Dispute object](https://docs.stripe.com/api/disputes/object.md). The evidence submission deadline is available in the Dashboard and in the `evidence_details.due_by` field of the Dispute object.

#### Responding to disputes 

You have 12 calendar days from dispute creation to submit evidence.

This evidence can include a tracking ID, shipping date, a record of purchase for intangible goods such as an IP address or email receipt, a record of purchase for services or physical goods such as a phone number or proof of receipt, or a record of a refund for a purchase you’ve already refunded.

You can submit evidence and manage BLIK disputes in the [Dashboard](https://dashboard.stripe.com/disputes) or programmatically using the [Disputes API](https://docs.stripe.com/api/disputes/update.md). In the Dashboard, on the **Needs Response** tab, click the disputed payment, then click **Counter dispute** to submit your evidence, or **Accept dispute** to accept the loss. To submit evidence through the API, upload supporting files using the [Files API](https://docs.stripe.com/api/files/create.md) and include the returned file IDs when you update the [Dispute Evidence object](https://docs.stripe.com/api/disputes/update.md).

#### Dispute outcomes 

If BLIK resolves the dispute in your favor, Stripe returns the disputed amount to your Stripe balance.

If they rule in favor of the customer, the balance charge becomes permanent.

#### Dispute fees and appeals

BLIK doesn’t charge dispute fees. You can’t appeal a BLIK dispute decision.

#### Customer notification period

Customers must notify their payment service provider without delay after discovering an unauthorized transaction. Polish law generally provides a maximum notification period of 13 months, subject to statutory exceptions.

### Mandates 

Saving a reusable BLIK payment method lets you charge the customer later without asking them to enter another BLIK code. The customer authorizes future off-session payments during the initial recurring setup, and Stripe associates the mandate with the reusable PaymentMethod.

#### What customers authorize 

The customer authorizes your business to make future off-session payments using the reusable BLIK PaymentMethod under the agreed terms.

#### Collect mandates 

The customer authorizes the mandate in their bank app during the initial BLIK recurring setup.

#### Manage mandates 

Use the [Mandates API](https://docs.stripe.com/api/mandates.md) to retrieve and manage the mandate associated with the reusable PaymentMethod.

#### Cancel mandates 

Detach the reusable [PaymentMethod](https://docs.stripe.com/api/payment_methods/detach.md) to unregister the BLIK alias and end future-use authorization. Customers can also revoke authorization in their bank app. After a mandate is revoked or expires, collect a new mandate before making future off-session payments.

### Reusable BLIK payments 

Save a reusable BLIK payment method for off-session recurring payments. To save it during a payment, create a PaymentIntent with `setup_future_usage=off_session`. To save it without an initial payment, create a SetupIntent with `usage=off_session`.

See [BLIK recurring payments](https://docs.stripe.com/payments/blik/recurring-payments.md), [save BLIK details during a payment](https://docs.stripe.com/payments/blik/save-during-payment.md), and [set up future BLIK recurring payments](https://docs.stripe.com/payments/blik/set-up-payment.md).

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
  ✓ Radar
  ✗ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✓ Payment Intents with setup_future_usage
  ✓ Setup Intents
  ✓ Off-session payments
Payment Element doesn’t support integrations that collect payment details before creating a PaymentIntent. See [collect payment details before creating a PaymentIntent](https://docs.stripe.com/payments/accept-a-payment-deferred.md).

### Connect account requirements 

To accept BLIK payments through Connect, the `blik_payments` capability must be active on your platform and on each connected account that accepts BLIK. [Request account capabilities](https://docs.stripe.com/connect/account-capabilities.md#requesting-unrequesting).

For recurring BLIK payments, request `blik_payments` before `blik_recurring_payments` on the platform and each connected account that accepts recurring payments. Both capabilities must be active before you use `setup_future_usage=off_session` or a SetupIntent with `usage=off_session`. See [BLIK recurring payments](https://docs.stripe.com/payments/blik/recurring-payments.md) for eligibility and setup details.

## Customer experience 

#### 1. Enter a BLIK code

The customer generates and enters a six-digit BLIK code in the payment form. The code is valid for 2 minutes.

#### 2. Approve in the banking app

The customer receives a push notification from their bank and approves the payment in the banking app within 60 seconds. The merchant page remains open and isn’t redirected.

#### 3. See the payment result

Stripe receives BLIK’s asynchronous result normally within 60 seconds, and the page shows the payment status. On mobile, the customer must manually return to the merchant page because BLIK doesn’t redirect them back.

### Payment flow 
![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_1.7e386c77d6410d13caf823130b7ec68a.svg)

Customer selects BLIK at checkout.
![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_2.5caa9f807d50579710cc01b361a2d0fc.svg)

Customer is directed to their mobile banking app to generate a 6-digit code.
![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_3.8e52c5c894b439baae7bec85b96b71b2.svg)

Customer puts the code into the checkout.
![](https://b.stripecdn.com/docs-statics-srv/assets/blik_payment_flow_4.a93b15c949981d6a0b61463ff201fc53.svg)

Customer is notified that payment is complete.

### Statement descriptors 

Set the full `statement_descriptor` for non-card BLIK payments. The exact presentation on a customer’s bank statement can vary by bank. `statement_descriptor_suffix` applies only to card payments. If you don’t set a payment-level descriptor, Stripe uses the account-level statement descriptor.

For direct charges, the connected account owns the statement descriptor. For destination charges and separate charges and transfers, the platform’s descriptor is used by default; set `on_behalf_of` to use the connected account’s descriptor. Learn more about [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable BLIK 

If you use Stripe front-end products, enable BLIK in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure BLIK as a payment method](https://docs.stripe.com/payments/blik/accept-a-payment.md).
