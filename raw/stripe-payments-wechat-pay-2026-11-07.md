<!-- Source URL: https://docs.stripe.com/payments/wechat-pay -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# WeChat Pay payments

Learn about WeChat Pay, a digital wallet popular with customers from China.

WeChat Pay is a digital wallet in the WeChat app. Chinese customers and travelers use it to pay for goods and services in businesses’ apps and websites.
Payment method family: Wallets
Usability: Single-use
Access type: Instant provisional access
Payment confirmation timing: Immediate
Settlement timing: Standard payout schedule
Pricing: https://stripe.com/en-us/pricing/local-payment-methods#wechat-pay
## Eligibility and availability 

### Account eligibility
Business location: AT, AU, BE, CA, CH, DE, DK, ES, FI, FR, GB, HK, IE, IT, JP, LU, NL, NO, PT, SE, SG, US
Account type: ✓ Merchant, ✓ Platform or marketplace (Connect)
Business model: ✗ B2B, ✓ B2C
### Prohibited business categories 

To accept WeChat Pay on Stripe, your business must comply with [Stripe’s restricted-business rules](https://stripe.com/restricted-businesses) and WeChat Pay’s [Proper Use Rules](https://pay.weixin.qq.com/index.php/public/wechatpay_en/proper_rule#:~:text=2.%20Forbidden%20and%20Restricted%20Categories), including its forbidden and restricted business categories. If you have questions about how these requirements apply to your business, [contact Stripe Support](https://support.stripe.com/contact/login).

For information about WeChat Pay eligibility for your account, go to your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).

### Website requirements 

WeChat Pay requires a complete, operational business website that clearly displays your products or services, prices, and a working checkout page. A social media profile alone doesn’t qualify as your business website. Your website’s business information must match the information you provide to Stripe, and the site must be accessible for review. These requirements apply in addition to Stripe’s general requirements.

### Request a review 

If your ability to accept WeChat Pay is restricted or disabled and you believe the decision is incorrect, [contact Stripe Support](https://support.stripe.com/contact/login) to request a review. If Stripe has requested changes or additional information, follow those instructions and reply to the notification after completing them. Reinstatement depends on the review outcome and isn’t guaranteed.

Stripe accounts in the following countries can accept WeChat Pay payments that settle in a supported currency.

AMER: CA, US

EMEA: AT, BE, CH, DE, DK, ES, FI, FR, GB, IE, IT, LU, NL, NO, PT, SE

APAC: AU, HK, JP, SG

Customers in the following countries can use WeChat Pay.

APAC: CN

### Payment support
Customer location: CN
Presentment currency: AUD, CAD, CHF, CNY, DKK, EUR, GBP, HKD, JPY, NOK, SEK, SGD, USD
Geographic coverage: ✓ Domestic, ✓ Crossborder
Transaction limits: Minimum amount: 0.50 USD
### Supported currencies 

You can create WeChat Pay payments in currencies that map to your account country. CNY is available in every supported account country, and customers see the purchase amount in CNY.

| Currency | Account country |
| --- | --- |
| `cny` | All supported countries |
| `aud` | Australia |
| `cad` | Canada |
| `eur` | Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland |
| `gbp` | United Kingdom |
| `hkd` | Hong Kong |
| `jpy` | Japan |
| `sgd` | Singapore |
| `usd` | United States |
| `dkk` | Denmark |
| `nok` | Norway |
| `sek` | Sweden |
| `chf` | Switzerland |

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
  Submission window: 180 days
  Processing time: Same day; linked-card refunds can take an additional 2–5 days

Disputes:
  ✗ Partial disputes
  ✗ Full disputes
### Refunds 

You can request a full or partial WeChat Pay refund within 180 days of the original payment. Refunds are asynchronous. Stripe processes refunds requested on the same day as the original payment immediately and processes later requests in a daily noon batch (UTC+8). Buyer receipt depends on the original funding source; linked-card refunds can take an additional 2–5 days. You can’t cancel WeChat Pay refunds.

#### Refund process 

WeChat Pay refunds are never processed as reversals. WeChat Pay handles the refund directly and returns the funds to the customer’s original payment source, which is either their WeChat Pay balance or linked payment method. The customer sees the refund reflected in their WeChat Pay account or funding source.

#### Tracking refunds 

To check a refund’s status, open the payment in the [Dashboard](https://dashboard.stripe.com/payments) and click **View details** on the refund entry. You can also [retrieve the Refund object](https://docs.stripe.com/api/refunds/retrieve.md) and check its `status` field.

Stripe notifies you of the final status through a `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. [Verify webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) to confirm that events came from Stripe. You can also use Stripe’s [public IP addresses](https://docs.stripe.com/ips.md) for network allowlisting. When a refund succeeds, the [Refund object](https://docs.stripe.com/api/refunds/object.md) status changes to `succeeded`. If the refund fails, the status changes to `failed` and Stripe returns the amount to your Stripe balance. You must refund the customer using another method.

### Disputes 

WeChat Pay requires customers to authenticate payments directly with the WeChat Pay app, which reduces the risk of fraud and unrecognized transactions. As a result, WeChat Pay doesn’t support the standard dispute process—customers can’t file a chargeback, and funds are never withdrawn from your Stripe balance because of a dispute.

If a customer contacts WeChat Pay about a payment, they might be directed back to you. You can then issue a full or partial refund.

### Recurring payments 

Recurring WeChat Pay payments are in private preview and support off-session use only.

[Sign up for early access](https://docs.stripe.com/payments/wechat-pay.md#wechat_recurring_beta_preview).

### Interested in getting early access to recurring payments for WeChat Pay?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/wechat-pay" \
  -d '{"email": "EMAIL", "preview": "wechat_recurring_beta_preview"}'
```

### Mini-program payments 

WeChat Pay for mini-programs is in private preview. [Sign up for early access](https://docs.stripe.com/payments/wechat-pay.md#wechat_mini_program_beta_preview).

### Interested in getting early access to WeChat Pay for mini-programs?

Enter your email to request access.

```bash
curl https://docs.stripe.com/preview/register \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Referer: https://docs.stripe.com/payments/wechat-pay" \
  -d '{"email": "EMAIL", "preview": "wechat_mini_program_beta_preview"}'
```

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
  ✗ Billing
  ✓ Invoicing
  ✗ Customer Portal
  ✓ Radar
  ✓ Terminal
  ✓ Connect

APIs:
  ✓ Checkout Sessions (Recommended)
  ✓ Payment Intents
  ✗ Payment Intents with setup_future_usage
  ✗ Setup Intents
  ✗ Off-session payments
Connect supports destination charges and separate charges and transfers. Direct charges and charges using `on_behalf_of` are in private preview. [Contact Stripe Support](https://support.stripe.com/contact/email?topic=payment_apis) to request access. Checkout doesn’t support WeChat Pay in subscription mode or setup mode. Invoices only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method). WeChat Pay isn’t available for Terminal in Japan due to regional limitations.

### Terminal payments 

To accept WeChat Pay in person, manually configure the payment method and follow the [Terminal smart-reader integration guide](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

## Customer experience 

#### 1. Select WeChat Pay

The customer selects WeChat Pay at checkout.

#### 2. Open WeChat Pay

On desktop, the customer scans the displayed QR code with the WeChat Pay app. In a supported native mobile integration, the merchant app opens WeChat Pay directly.

#### 3. Authorize the payment

The customer reviews and authorizes the payment in the WeChat Pay app. The desktop checkout remains on the QR-code screen; native mobile flows return the customer to the merchant app.

#### 4. Confirm the payment

After a successful payment, customers using Stripe's hosted WeChat Pay payment instructions page see a payment success confirmation and the amount paid. For a custom checkout or native mobile integration, show the customer a success message or order confirmation page after your server confirms that the PaymentIntent succeeded.

### Authorization time limit 

For the desktop QR-code flow, customers must complete authorization within two hours after the payment request is created. If the request expires, they must start a new payment attempt.

### Statement descriptors 

Stripe sends WeChat Pay an order description containing the settlement merchant’s business name, `online`, and the individual payment’s statement descriptor. WeChat also maintains a separately registered buyer-visible merchant name.

You can provide a statement descriptor for an individual payment. This value contributes to the order information sent to WeChat Pay, but it doesn’t guarantee the exact text that WeChat displays in the customer’s transaction history or that appears on a linked card or bank statement.

For Connect payments, the charge type determines which account supplies the business name in the WeChat order description:

| Charge type | Business-name source in the WeChat order description |
| --- | --- |
| Destination charge without `on_behalf_of` | Platform account |
| Destination charge with `on_behalf_of` | Connected account specified by `on_behalf_of` |
| Direct charge | Connected account on which the payment is created |

The individual payment’s `statement_descriptor` contributes to the order description in all three cases.

Direct charges and charges using `on_behalf_of` require WeChat Pay private-preview access. For general Connect guidance, see [statement descriptors](https://docs.stripe.com/connect/statement-descriptors.md) and [the on_behalf_of parameter](https://docs.stripe.com/connect/charges.md#on_behalf_of).

To reconcile a payment with WeChat Pay, retrieve the PaymentIntent, expand `latest_charge`, and read `latest_charge.payment_method_details.wechat_pay.transaction_id`.

## Enable WeChat Pay 

If you use Stripe front-end products, enable WeChat Pay in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). Stripe automatically determines which payment methods are most relevant to each customer.

If your integration lists payment methods manually, learn how to [configure WeChat Pay as a payment method](https://docs.stripe.com/payments/wechat-pay/accept-a-payment.md).

### Account requirements

To enable WeChat Pay for your connected accounts, provide the following properties on the [Account](https://docs.stripe.com/api/accounts/object.md) object:

| Field | Description |
| --- | --- |
| [`capabilities.wechat_pay_payments.requested`](https://docs.stripe.com/api/accounts/update.md) | For connected accounts without standard Dashboard access, the platform must request the `wechat_pay_payments` capability. This capability is in private preview. [Contact Stripe Support](https://support.stripe.com/contact/email?topic=payment_apis) to request access. Connected accounts with standard Dashboard access can enable WeChat Pay in their Dashboard. |
