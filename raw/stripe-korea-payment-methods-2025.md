<!-- Source URL: https://docs.stripe.com/payments/countries/korea -->
<!-- Fetched: 2026-05-08 -->

# South Korean payment methods

Accept wallets and all local cards in South Korea without a local entity.

You can localize your customer experience and accept payments from the majority of payment methods available in South Korea without a local South Korean entity by using Stripe and our local processor partner.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#south-korean-payment-methods).

Card usage is popular in South Korea, with many different card issuers but not a single predominant brand. Customers typically pay by selecting their card issuer and authenticating through their card or bank’s app rather than manually entering their card details. Wallets are also becoming more popular in South Korea. To provide a familiar experience to customers and increase conversion rates, offer a selection of local wallets and cards.

## Payment flow

![](assets/stripe-korea-payment-flow.mp4)
After the customer enters their information in Stripe’s checkout page and clicks **Pay**, they’re redirected to the checkout page of the payment method provider or local processor to complete the payment.

## Available payment methods

You can accept popular local wallets and all local cards.

Popular local wallets include:

- [Naver Pay](https://pay.naver.com/)
- [Kakao Pay](https://www.kakaopay.com/) (not available in Singapore)
- [Samsung Pay](https://www.samsung.com/us/apps/samsung-wallet/)
- [PAYCO](https://www.payco.com/)

All locally issued cards are supported, including:

- [Shinhan Card](https://www.shinhancard.com/)
- [Hyundai Card](https://www.hyundaicard.com/)
- [Samsung Card](https://www.samsungcard.com/company/english/main/UHPPCI0245M0.jsp)

> Make sure that in providing goods and services to South Korean customers, your business complies with South Korean legal and tax requirements. Use Stripe Tax to [collect tax in South Korea](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=south-korea).

#### Payment method properties

- **Customer locations**

  South Korea

- **Presentment currency**

  KRW

- **Payment confirmation**

  Customer-authenticated

- **Payment method family**

  Countries

- **Recurring payments**

  Yes

- **Payout timing**

  [T + 4 (US only)](https://docs.stripe.com/payouts.md#payout-speed)

  [T + 7 (outside the US)](https://docs.stripe.com/payouts.md#payout-speed)

- **Connect support**

  Yes

- **Dispute support**

  Yes

- **Manual capture**

  Yes

- **Partial capture**

  No

- **Refunds and partial refunds**

  Yes

#### Business locations

You can accept South Korean payments in the following countries.

- AT
- BE
- CY
- DE
- DK
- EE
- ES
- FI
- FR
- GB
- GR
- HK
- HR
- HU
- IE
- IT
- JP
- LT
- LU
- LV
- MT
- NL
- PT
- SE
- SG
- SI
- SK
- US

## Get started

You don’t have to integrate South Korean payment methods and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable South Korean payment methods. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add South Korean payment methods from the Dashboard:

- [Invoicing](https://docs.stripe.com/invoicing/no-code-guide.md)
- [Payment Links](https://docs.stripe.com/payment-links.md)
- [Subscriptions](https://docs.stripe.com/billing/subscriptions/overview.md)

### Integrate through the API

You can also use the [Payment Intents API](https://docs.stripe.com/payments/payment-intents.md) to accept payments from South Korean customers using local cards and local payment methods. Follow our guide to [test the redirect-handling logic for your integration](https://docs.stripe.com/testing.md#redirects) by simulating a payment that uses a redirect flow.

## Payment process

Customers who elect to pay with South Korean cards or payment methods are redirected to the local processor or underlying payment method provider’s checkout page as applicable, where they [authorize the transaction](https://docs.stripe.com/payments/payment-methods.md#customer-actions). After the payment is approved, funds are available in your Stripe account after 4 days.

## Payment methods

We currently support all local South Korean cards and the majority of South Korean payment methods.

|                                                                                                          | One-time | Recurring |
| -------------------------------------------------------------------------------------------------------- | -------- | --------- |
| [All local cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md)                          | Yes      | Yes       |
| [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md) (not available in Singapore) | Yes      | Yes       |
| [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md)                              | Yes      | Yes       |
| [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md)                          | Yes      | No        |
| [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment.md)                                      | Yes      | No        |

## Installments

Local card issuers in South Korea can offer installments on purchases 50,000 KRW and above. This lets customers pay for their purchase over time, for example, to complete the payment over 3 months. Installments are popular with customers who want to purchase goods with higher order values.

Installments are solely between customers and their card issuers. As a business, you receive the full amount for your purchase up front, and your customer is responsible for completing the installment payments to the issuer. In the event that your customer is unable to complete their installments to their issuer, you keep the funds.

## Refunds

Payments made with South Korean payment methods can only be submitted for a refund within 365 calendar days from the date of the original charge. After 365 days, it’s no longer possible to refund the charge.

In South Korea, customers are generally entitled to a full refund within 7 days of receiving goods or services unless they’re used or damaged. You must clearly display non-refundable conditions. If the goods or services differ from the contract, customers can request a refund within 3 months of purchase or 30 calendar days after discovering the discrepancy, whichever comes first. For subscriptions, customers can cancel and receive a full refund within 7 days of signing up if they haven’t used the service. Customers can also cancel their subscription at any time during the subscription period and receive a pro-rated refund based on actual usage. Make sure your refund policy aligns with local market practices.

## Disputes

Local cards and payment methods in South Korea enforce strong authentication, which helps reduce the risk of fraud or unrecognized payments.

### Dispute Timing

Customers have up to 365 calendar days from the date of purchase to file a dispute. After a customer files a dispute, you have up to 7 days to respond and submit evidence. If you don’t respond before the deadline, you automatically lose the dispute. Dispute decisions are made within 45 days of evidence submission. This outcome is final.

### Respond to disputes

You can use our [guide](https://docs.stripe.com/disputes/responding.md) on responding to disputes to understand more about dispute reason codes and evidence submission. In South Korea, local issuers support the following dispute reason codes:

- Credit not processed
- Duplicate
- Fraudulent
- General
- Product not received
- Product unacceptable
- Subscription canceled

> #### Best practices
>
> In South Korea, the following evidence is typically considered compelling. Include these types of evidence to increase your chances of successfully defending a dispute:
>
> - [POS data and system logs](https://docs.stripe.com/disputes/visual-evidence.md#general)

- [Subscription terms and policies](https://docs.stripe.com/disputes/visual-evidence.md#subscription-canceled)
- [Usage and communications](https://docs.stripe.com/disputes/visual-evidence.md#subscription-canceled)

## Additional information for subscriptions

If you offer subscriptions to South Korean customers, you must notify your customers and obtain their consent at least 30 days before any price increase or before charging for a previously free service. You must also remind your customers 7 days before the actual payment date by email, text message, or mail.

To minimize disputes, make sure customers can easily cancel their subscription by adding a cancellation button or providing clear instructions.

Further make sure that you incorporate local requirements into your terms of service, billing, cancellations and refunds policies, and take steps to make sure that your customers clearly understand and agree to them. As a best practice:

- Consider incorporating these terms and policies into your pre-payment checkout flow and collecting explicit customer consent for them (for example, using a checkbox), and promptly address customer queries and complaints.
