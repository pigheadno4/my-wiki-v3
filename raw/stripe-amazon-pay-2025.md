<!-- Source URL: https://docs.stripe.com/payments/amazon-pay -->
<!-- Fetched: 2026-05-07 -->

# Amazon Pay payments

Learn how to accept payments with Amazon Pay.

[Amazon Pay](https://pay.amazon.com/) is a wallet payment method that lets your customers check out the same way as on Amazon.com.

For information on payment method transaction fees, refer to [pricing details](https://stripe.com/pricing/local-payment-methods#amazon-pay).

When customers select Amazon Pay as their payment method, Stripe redirects them to Amazon’s website, where they can check out using the shipping and payment information stored in their Amazon account. After completing the payment, Amazon redirects them back to your website.

#### Payment method properties

- **Customer locations**

  Worldwide

- **Presentment currency**

  USD, AUD, GBP, DKK, EUR, HKD, JPY, NZD, NOK, ZAR, SEK, CHF

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Wallet

- **Recurring payments**

  Yes

- **Payout timing**

  Standard payout timing applies

- **Connect support**

  Yes

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/amazon-pay.md#disputed-payments)

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/amazon-pay.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept Amazon Pay payments:

- AT
- BE
- CH
- CY
- DE
- DK
- ES
- FR
- GB
- HU
- IE
- IT
- LU
- NL
- PT
- SE
- US

#### Product support

- Connect
- Checkout
- Payment Links
- Elements
- Subscriptions
- Invoicing

## Payment flow

Below is a demonstration of the Amazon Pay payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/AmazonPayDemo3.mp4)

## Get started

You don’t have to integrate Amazon Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Amazon Pay. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Amazon Pay from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure Amazon Pay as a payment](https://docs.stripe.com/payments/amazon-pay/accept-a-payment.md).

## Refunds

Amazon Pay supports partial or full refunds for up to 90 days after the original purchase, and processes them asynchronously. After Stripe initiates a refund, Amazon Pay issues the refund to the customer’s original form of payment. We notify you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails, the Refund object’s status transitions to `failed` and we return the amount to your Stripe balance. You then need to arrange an alternative way to provide your customer with a refund.

For some Amazon Pay transactions that use non-card payment methods, refunds can take up to 14 calendar days from the purchase date to return a status.

## Disputes

Customers must authenticate Amazon Pay payments by logging into their Amazon account. This requirement helps reduce the risk of fraud or unrecognized payments.

Customers have up to 240 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md)).

- Stripe holds back the disputed amount from your balance until Amazon resolves the dispute.

- Stripe requests that you upload compelling evidence that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include:
  - A received return confirmation (for shipped goods returned from the customer to you)
  - The tracking ID
  - The shipping date
  - A record of purchase for intangible goods, such as IP address or email receipt
  - A record of purchase for services or physical goods, such as phone number or proof of receipt

- This information helps Amazon determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 10 calendar days. Amazon Pay makes a decision within 90 calendar days of evidence submission. If Amazon resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Amazon rules in favor of the customer, the balance charge becomes permanent.

Amazon Pay offers an [A-to-z Guarantee](https://www.amazon.com/gp/help/customer/display.html?nodeId=GQ37ZCNECJKTFYQV) that protects buyers from issues related to timely delivery and the condition of their items. A buyer can make a claim against this guarantee, which follows the same dispute process described above. A-to-z Guarantee claims don’t incur dispute fees. In the Dashboard and in the dispute object, you can distinguish A-to-z Guarantee claims as `dispute_type = claim`.

> If you prefer to handle disputes programmatically, you can [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

## Supported currencies

You can create Amazon Pay payments in any of the supported currencies, regardless of the country your business operates in with the exception of the US.

| Country                                                                                                                                                                   | Currency                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, Switzerland, United Kingdom, United States | `aud`, `gbp`, `dkk`, `eur`, `hkd`, `jpy`, `nzd`, `nok`, `zar`, `sek`, `chf`, `usd` |

## Available payment methods

Use Amazon Pay to store card credentials. They support the following alternative payment methods:

| Country                                                                                                                                    | Payment methods                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| United States                                                                                                                              | Amazon Store Card, Amazon Store Card Installments, Amazon Visa Card Installments, Citi Flex Pay, Affirm, and Shop with Points |
| Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Luxembourg, Netherlands, Portugal, Spain, Sweden, Switzerland | SEPA Direct Debit                                                                                                             |
