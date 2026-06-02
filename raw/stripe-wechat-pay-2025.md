<!-- Source URL: https://docs.stripe.com/payments/wechat-pay -->
<!-- Fetched: 2026-05-08 -->

# WeChat Pay payments

Learn about WeChat Pay, a digital wallet popular with customers from China.

As China’s largest internet company, Tencent offers a number of web and mobile products across social networking, communications, media, games, finance, and so on. WeChat, owned by Tencent, is China’s leading mobile app with over 1 billion monthly active users.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#wechat-pay).

WeChat is a leading lifestyle “super app” used for messaging between people, as well as connecting people, services, and businesses in China and around the world through a number of e-commerce and social features inside the app. WeChat Pay, the payment wallet inside the WeChat app, has over 800 million users.

Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses’ apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, food, and nutrition.

#### Payment method properties

- **Customer locations**

  Chinese consumers, overseas Chinese, and Chinese travelers

- **Presentment currency**

  CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, USD, DKK, NOK, SEK, CHF (depending on business location)

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Digital wallet

- **Recurring payments**

  No

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  [Partial](https://docs.stripe.com/payments/wechat-pay.md#connect) (request an invite to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts)

- **Dispute support**

  [No](https://docs.stripe.com/payments/wechat-pay.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/wechat-pay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept WeChat Pay payments:

- AT
- AU
- BE
- CA
- CH
- DE
- DK
- ES
- FI
- FR
- GB
- HK
- IE
- IT
- JP
- LU
- NL
- NO
- PT
- SE
- SG
- US

#### Product support

- Connect1

- Checkout2

- Payment Links
- Elements3

- Invoicing4

- Terminal5

1Partial: [request an invite](https://support.stripe.com/contact/email?topic=payment_apis) to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts.2Not supported when using Checkout in subscription mode or setup mode.3Express Checkout Element and Mobile Payment Element don’t support WeChat Pay.4Invoices only support the `send_invoice` [collection method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method).5WeChat Pay isn’t available for Terminal in Japan due to regional limitations.

## Get started

You don’t have to integrate WeChat Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable WeChat Pay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add WeChat Pay from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

If your integration requires manually listing payment methods, learn how to [manually configure WeChat Pay as a payment](https://docs.stripe.com/payments/wechat-pay/accept-a-payment.md). For example, to accept in-person payments you need to manually configure WeChat Pay. Learn how to [accept WeChat Pay on Terminal smart readers](https://docs.stripe.com/terminal/payments/additional-payment-methods.md).

## Disputes

WeChat payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment with the WeChat Pay app. Therefore, there is no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

## Refunds

Payments made with WeChat Pay can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it’s no longer possible to refund the charge. Refunds for WeChat Pay payments are asynchronous. Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` _webhook_ (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails, the Refund object’s status transitions to `failed` and Stripe returns the amount to your Stripe balance. You then need to arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create WeChat Pay payments in the currencies that map to your country. The default local currency for WeChat Pay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `cny`    | All countries                                                                                                                              |
| `aud`    | Australia                                                                                                                                  |
| `cad`    | Canada                                                                                                                                     |
| `eur`    | Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                             |
| `hkd`    | Hong Kong                                                                                                                                  |
| `jpy`    | Japan                                                                                                                                      |
| `sgd`    | Singapore                                                                                                                                  |
| `usd`    | United States                                                                                                                              |
| `dkk`    | Denmark                                                                                                                                    |
| `nok`    | Norway                                                                                                                                     |
| `sek`    | Sweden                                                                                                                                     |
| `chf`    | Switzerland                                                                                                                                |

## Connect

Wechat Pay has partial [Connect](https://stripe.com/connect) support depending on the [charge type](https://docs.stripe.com/connect/charges.md).

The following charge types are generally available.

- Destination charges
- Separate charges and transfers

The following charge types are in private preview.

- Direct charges
- `on_behalf_of`

For connected accounts with standard Dashboard access, individual connected accounts can enable Wechat Pay in the Dashboard.

For connected accounts without standard Dashboard access, the platform needs to request the `wechat_pay_payments` capability. This is a private preview feature. Contact Stripe Support to request access.
