<!-- Source URL: https://docs.stripe.com/payments/twint -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# TWINT payments

Learn about TWINT, a popular payment method in Switzerland.

TWINT is a payment method used in Switzerland that allows customers to [authenticate and approve](https://docs.stripe.com/payments/payment-methods.md#customer-actions) payments using an approved TWINT mobile app.

You get [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) on whether the payment succeeded or failed.
Payment method family: Wallets
Usability: Reusable
Access type: Approval required
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-ch/pricing/local-payment-methods#twint
## Eligibility and availability 

### Account eligibility
Business location: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SI, SK, SM
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✗ B2B, ✓ B2C
Business category: View list of prohibited and restricted business categories
Before requesting access to TWINT in the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) or through the [Capabilities API](https://docs.stripe.com/api/capabilities.md), meet the account and website requirements in this section:

- Your website must be functional. It must not be password protected or in a “coming soon” state.
- Display the required business information in your website’s legal notice, terms of service, or terms and conditions. For sole proprietorships, include the business owner’s full first and last name. Your business address must include the street, house number, postal code, and city.
- If you sell physical goods, you must make Switzerland available as a shipping destination.
- You must display prices in CHF (Swiss francs) by the time the customer reaches checkout.

> #### Display prices in CHF
> 
> You can use [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) to automate currency displays without explicitly pricing your products in CHF.

The `twint_payments` capability stays in a `pending` state until compliance with TWINT onboarding requirements is verified. Contact [Stripe support](https://support.stripe.com/contact) if you’re unsure about your capability status.

Your account might be reviewed after activation to confirm eligibility. In addition to meeting the criteria above, you must also provide a website that meets the following requirements in addition to the [Stripe account activation requirements](https://support.stripe.com/questions/business-website-for-account-activation-faq):

- Must be publicly accessible.
- Must display pricing in the local currency of the customer.
- Must clearly display the legal business name.
- Must clearly display the legal form of the business.
- Must clearly display the business address.
- Must display terms of service.
- Must not engage in deceptive marketing or business practices.
- Provide at least 1 of the following:
  - Must clearly display a contact email address.
  - Must clearly display a contact phone number.

You can contact [Stripe support](https://support.stripe.com/) to appeal any TWINT capability restrictions.

### Termination rights 

In addition to the termination and suspension rights included in the [Stripe Services Agreement](https://stripe.com/legal/ssa), TWINT has the right to suspend or terminate your use of TWINT, such as for breaches of the [account eligibility requirements](https://docs.stripe.com/payments/twint.md#account-eligibility) that aren’t promptly remedied.

Review the list of *merchant category codes* (A Merchant Category Code (MCC) is a four-digit number that classifies the type of goods or services a business offers) that are prohibited or restricted for TWINT.

- **Prohibited**: You can’t use this payment method with these MCCs.
- **Restricted**: You might be able to use this payment method with these MCCs, but you must provide additional information when you create the account.

MCC requirements depend on your business country. Countries with the same requirements share a table.

**Business countries:** Austria, Belgium, Bulgaria, Switzerland, Cyprus, Czech Republic, Germany, Denmark, Estonia, Spain, Finland, France, United Kingdom, Gibraltar, Greece, Croatia, Hungary, Ireland, Italy, Liechtenstein, Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia.

| MCC | Description | Type |
| --- | --- | --- |
| 3000–3482 | Description unavailable | Restricted |
| 3483–3484 | Car Rental Agencies | Restricted |
| 3485–3500 | Description unavailable | Restricted |
| 3501 | Holiday Inns | Restricted |
| 3502–3999 | Description unavailable | Restricted |
| 4112 | Passenger Railways | Restricted |
| 4131 | Bus Lines | Restricted |
| 4411 | Cruise Lines | Restricted |
| 4511 | Airlines, Air Carriers | Restricted |
| 4551 | Description unavailable | Restricted |
| 4722 | Travel Agencies, Tour Operators | Restricted |
| 4814 | Telecommunication Services | Restricted |
| 4829 | Money Orders - Wire Transfers | Prohibited |
| 5094 | Precious Stones and Metals, Watches and Jewelry | Restricted |
| 5122 | Drugs, Drug Proprietaries, and Druggist Sundries | Restricted |
| 5816 | Digital Goods – Games | Restricted |
| 5960 | Direct Marketing - Insurance Services | Restricted |
| 5961 | Description unavailable | Restricted |
| 5962 | Direct Marketing - Travel | Restricted |
| 5963 | Door-To-Door Sales | Restricted |
| 5964 | Direct Marketing - Catalog Merchant | Restricted |
| 5965 | Direct Marketing - Combination Catalog and Retail Merchant | Restricted |
| 5966 | Direct Marketing - Outbound Telemarketing | Restricted |
| 5967 | Adult Content and Services | Restricted |
| 5968 | Direct Marketing - Subscription | Restricted |
| 5969 | Direct Marketing - Other | Restricted |
| 5999 | Miscellaneous Specialty Retail | Restricted |
| 6010 | Manual Cash Disburse | Prohibited |
| 6011 | Financial Service | Prohibited |
| 6012 | Financial Institutions | Prohibited |
| 6050 | Description unavailable | Prohibited |
| 6051 | Cryptocurrency exchanges and wallets | Prohibited |
| 6211 | Security Brokers and Dealers | Restricted |
| 6540 | Non-FI, Stored Value Card Purchase and Load | Prohibited |
| 7012 | Timeshares | Restricted |
| 7273 | Dating and Escort Services | Restricted |
| 7922 | Theatrical Ticket Agencies | Restricted |
| 7994 | Video Game Arcades | Restricted |
| 7995 | Betting and Casino Gambling | Restricted |
| 9223 | Bail and Bond Payments | Restricted |
| 9754 | Lodging - Hotels, Motels, and Resorts (Continued) | Restricted |

**Business countries:** Iceland, Monaco, San Marino.

MCC requirements aren’t available for this country. Contact [Stripe support](https://support.stripe.com/).

Stripe accounts in the following countries can accept TWINT payments that settle in a supported currency.

EMEA: AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GI, GR, HR, HU, IE, IS, IT, LI, LT, LU, LV, MC, MT, NL, NO, PL, PT, RO, SE, SI, SK, SM

Customers in the following countries can use TWINT.

EMEA: CH

### Payment support
Customer location: CH
Presentment currency: CHF
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 0.50 CHF

Maximum amount: 5,000 CHF
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
  Processing time: a few minutes

Disputes:
  ✗ Partial disputes
  ✓ Full disputes
### Refunds 

You can refund TWINT charges up to 180 days after the payment completes. Refunds usually take a few minutes to complete. TWINT supports full, partial, and multiple partial refunds. The total amount of all refunds can’t exceed the amount of the original payment. You can’t cancel TWINT refunds.

#### Refund process 

TWINT refunds are never processed as reversals. TWINT handles the refund directly and returns the funds to the customer’s original payment source, which is either their TWINT balance or linked payment method. The customer sees the refund reflected in their TWINT account or funding source.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

#### Dispute process 

Customers can dispute TWINT payments by filing a complaint with their bank. When Stripe receives a dispute, it creates a dispute that you can view and respond to in the Dashboard. The disputed amount is debited from your Stripe balance.

#### Dispute notifications 

Review TWINT disputes in the [Dashboard](https://dashboard.stripe.com/disputes). Each dispute includes the reason and the deadline for submitting evidence.

#### Responding to disputes 

To challenge a dispute, submit evidence through the Dashboard before the deadline shown on the dispute. Stripe forwards your evidence to TWINT for review.

To accept the dispute, select **Accept dispute** in the Dashboard. If you accept the dispute or don’t submit evidence before the deadline, the dispute is marked as lost.

#### Dispute outcomes 

Stripe updates the dispute when it receives the outcome. If you win, Stripe returns the disputed amount to your balance. If you lose, the debit to your balance becomes permanent.

### Mandates 

TWINT mandates authorize reusable, off-session payments. One-time TWINT payments don’t require a mandate. A customer creates a mandate by authorizing a SetupIntent or a PaymentIntent configured for future use in their TWINT app.

#### What customers authorize 

The customer authorizes your business to initiate merchant-initiated, off-session TWINT payments on an ad hoc basis. The mandate doesn’t specify a fixed amount or payment schedule.

#### Collect mandates 

To collect a mandate, confirm a SetupIntent or a PaymentIntent configured for future use. The customer authorizes saving TWINT for future payments in their TWINT app.

#### Manage mandates 

At a given time, only one TWINT mandate can be active between your business and a particular customer. Use the active mandate for future payments.

For Connect platforms that use indirect payments without setting `on_behalf_of`, mandate conflicts can occur if a customer creates TWINT mandates with multiple connected accounts. Because those payments treat the platform as the Merchant of Record, creating a second mandate automatically revokes the existing one, even if the connected account is different. For help with configuring Connect payments, see [the Connect Merchant of Record documentation](https://docs.stripe.com/connect/merchant-of-record.md).

Active TWINT mandates appear in the Dashboard with the customer’s saved payment methods. To retrieve the mandate identifier for a payment, inspect `charge.payment_method_details.twint.mandate`. You can retrieve mandate details with the [Mandate API](https://docs.stripe.com/api/mandates.md).

#### Cancel mandates 

To revoke a TWINT mandate as a merchant, detach the PaymentMethod from the customer using the [Detach API](https://docs.stripe.com/api/payment_methods/detach.md). Customers can revoke a mandate at any time in their TWINT app, and TWINT can also revoke a mandate. When Stripe receives the revocation, it updates the Mandate state.

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

#### 1. Select TWINT

The customer selects TWINT at checkout.

#### 2. Authorize the payment

On mobile, the customer is redirected to a TWINT-hosted page, selects their TWINT app, and then switches to that app. TWINT offers different apps depending on the customer's Swiss bank. On desktop, the customer is redirected to a TWINT-hosted page that displays a QR code. The customer scans the code using their TWINT app. The customer approves the payment in the app. While authorization is pending, the PaymentIntent remains in `requires_action`.

#### 3. Complete the payment

The customer sees confirmation in the TWINT app. After authorization, the customer is redirected back to your website or app. Stripe immediately reports the result: successful PaymentIntents transition to `succeeded`, while declined or failed payments transition to `requires_payment_method`.

### Statement descriptors 

Stripe forwards the payment’s `statement_descriptor` to TWINT as a dynamic descriptor. This doesn’t guarantee that TWINT displays the custom descriptor to the customer.

By default, the business name on your Stripe account appears to the customer. For Connect payments, direct charges and charges that use `on_behalf_of` use the connected account’s name. Destination charges and separate charges and transfers that don’t use `on_behalf_of` use the platform’s name. Learn more about [statement descriptors with Connect](https://docs.stripe.com/connect/statement-descriptors.md).

## Enable TWINT 

If you use Stripe front-end products, enable TWINT in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure TWINT as a payment method](https://docs.stripe.com/payments/twint/accept-a-payment.md).

For connected accounts that use the Express Dashboard or no Stripe-hosted Dashboard, follow the instructions to [request capabilities for your connected accounts](https://docs.stripe.com/connect/account-capabilities.md). Request the `twint_payments` capability and check that its status is `active` before accepting TWINT payments.
