<!-- Source URL: https://docs.stripe.com/payments/alipay -->
<!-- Fetched: 2026-05-07 -->

# Alipay payments

Learn about Alipay, a digital wallet popular with customers from China.

Alipay is a digital wallet in China that has more than a billion active users worldwide.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#alipay).

Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer’s login credentials.

#### Payment method properties

- **Customer locations**

  Chinese consumers, overseas Chinese, and Chinese travelers

- **Presentment currency**

  CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, MYR, NZD, USD (depending on business locations)

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallets

- **Recurring payments**

  [Requires approval](https://support.stripe.com/contact)

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Partial (request an invite to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts)

- **Dispute support**

  [No](https://docs.stripe.com/payments/alipay.md#disputed-payments)

- **Manual capture support**

  No

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/alipay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Alipay payments:

- AT
- AU
- BE
- BG
- CA
- CH
- CY
- CZ
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GI
- GR
- HK
- HR
- HU
- IE
- IT
- JP
- LI
- LT
- LU
- LV
- MT
- MY
- NL
- NO
- NZ
- PT
- RO
- SE
- SG
- SI
- SK
- US

#### Product support

- Connect1

- Checkout2

- Payment Links
- Elements3

- Subscriptions4

- Invoicing4

1Partial: [request an invite](https://support.stripe.com/contact/email?topic=payment_apis) to create charges [on behalf of](https://docs.stripe.com/connect/charges.md#on_behalf_of) other accounts.2Not supported when using Checkout in subscription mode or setup mode.3Express Checkout Element doesn’t support Alipay.4Available by invite only.

## Prohibited business categories

Both Stripe and Alipay maintain a list of prohibited businesses that aren’t allowed to use their services. To use Alipay on Stripe, your business can’t be [restricted from using Stripe](https://stripe.com/restricted-businesses) or appear on Alipay’s [prohibited business list](https://stripe.com/legal/alipay). If you’re not sure if your business is a prohibited business, or have questions about how these requirements apply to you, please [contact support](https://support.stripe.com/contact/login).

For more information about Alipay eligibility for your account, go to your [Payment methods settings](https://dashboard.stripe.com/settings/payment_methods).

## Get started

You don’t have to integrate Alipay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Alipay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

[Payment Links](https://docs.stripe.com/payment-links.md) also supports adding Alipay from the Dashboard.

If you prefer to manually list payment methods, learn how to [manually configure Alipay as a payment](https://docs.stripe.com/payments/alipay/accept-a-payment.md).

## Disputes

Alipay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment, so no dispute process exists that could create chargebacks and withdraw funds from your Stripe account. If an Alipay user contacts them about a problem with a transaction, they might direct that user to you for a resolution.

## Refunds

You can refund Alipay payments up to 90 days after the original payment. Refunds for Alipay payments are asynchronous and take up to 5 minutes to complete. Stripe notifies you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the status of the [Refund](https://docs.stripe.com/api/refunds/object.md) object transitions to `succeeded`. If a refund fails, the status of the Refund object transitions to `failed` and Stripe returns the amount to your Stripe balance. You then need to arrange an alternative way of providing your customer with a refund.

## Supported currencies

Your account must have a bank account for one of the following currencies. You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is `cny` and customers also see their purchase amount in `cny`.

| Currency | Country                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cny`    | Any country                                                                                                                                                                                                                                          |
| `aud`    | Australia                                                                                                                                                                                                                                            |
| `cad`    | Canada                                                                                                                                                                                                                                               |
| `eur`    | Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland |
| `gbp`    | United Kingdom                                                                                                                                                                                                                                       |
| `hkd`    | Hong Kong                                                                                                                                                                                                                                            |
| `jpy`    | Japan                                                                                                                                                                                                                                                |
| `myr`    | Malaysia                                                                                                                                                                                                                                             |
| `nzd`    | New Zealand                                                                                                                                                                                                                                          |
| `sgd`    | Singapore                                                                                                                                                                                                                                            |
| `usd`    | United States                                                                                                                                                                                                                                        |

If you have a bank account in another currency and want to create an Alipay payment in that currency, you can [contact support](https://support.stripe.com/email). We provide support for additional currencies on a case-by-case basis.

## Connect

Alipay has partial [Connect](https://stripe.com/connect) support depending on the [charge type](https://docs.stripe.com/connect/charges.md).

| Destination charges | Separate charges and transfers | Direct charges    | `on_behalf_of`    |
| ------------------- | ------------------------------ | ----------------- | ----------------- |
| ✓ Supported         | ✓ Supported                    | ⚠ Private preview | ⚠ Private preview |

For connected accounts with standard Dashboard access, individual connected accounts can enable Alipay in the Dashboard.

For connected accounts without standard Dashboard access, the platform needs to request the `alipay_payments` capability. This is a private preview feature; contact Stripe Support to request access.
