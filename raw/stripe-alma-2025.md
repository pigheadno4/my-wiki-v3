<!-- Source URL: https://docs.stripe.com/payments/alma -->
<!-- Fetched: 2026-05-06 -->

# Alma payments

Offer European customers the ability to pay in 2, 3, or 4 installments while getting paid instantly.

[Alma](https://almapay.com/) is a Buy Now, Pay Later payment method available in France, Italy, Spain, Netherlands, Belgium, and Luxembourg that gives your customers payment installment choices.

When customers select Alma as their payment method, Stripe redirects them to Alma’s website, where they get the ability to choose between 2, 3, or 4 installments to complete their purchase. You’re paid immediately.

Alma is only available for payments between 50 EUR and 5,000 EUR.

#### Payment method properties

- **Customer locations**

  France, Italy, Spain, Netherlands, Belgium, Luxembourg

- **Presentment currency**

  EUR

- **Payment confirmation**

  Customer-initiated

- **Payment method family**

  Buy Now, pay later

- **Recurring payments**

  No

- **Payout timing**

  T+3

- **Connect support**

  [Yes](https://docs.stripe.com/payments/alma.md#connect)

- **Dispute support**

  Yes

- **Manual capture support**

  Yes

- **Refunds / Partial refunds**

  Yes / yes

#### Business locations

Stripe accounts in the following countries can accept Alma payments:

- BE
- ES
- FR
- IT
- LU
- NL

## Payment flow

Below is a demonstration of the Alma payment flow from your checkout page:
![](https://d37ugbyn3rpeym.cloudfront.net/videos/alma-payment-flow-demo.mp4)

## Get started

You don’t have to integrate Alma and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Go to the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) and enable Alma. To get started with one of our hosted UIs, follow a quickstart:

- [Checkout](https://docs.stripe.com/checkout/quickstart.md): Our prebuilt, hosted checkout page.
- [Elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md): Our drop-in UI components.

### Other payment products

The following Stripe products also let you add Alma from the Dashboard:

- [Payment Links](https://docs.stripe.com/payment-links.md)

If your integration requires manually listing payment methods, learn how to [manually configure Alma as a payment](https://docs.stripe.com/payments/alma/accept-a-payment.md).

## Payment options

Depending on the customer’s billing country and the transaction amount, Alma can present customers with various payment options. Cart ranges and geographic availability for payment options are determined by Alma and might change at their discretion. Regardless of the underlying payment option selected, Stripe makes the full amount of the funds (minus fees) available to you upfront and Alma collects the purchase amount from your customer, who repays Alma directly. These options include:

Pay in 2, 3, or 4 (also known as Installments): Customers pay for the purchase in two,three or four interest-free payments. The total transaction amount is typically spread equally across the installments, but Alma might occasionally charge your customer more in the first installment based on the customer’s purchase power and other credit factors.

The following table lists the available payment options for supported Alma locations.

| **Payment option** | **Currency** | **Minimum** | **Maximum** |
| ------------------ | ------------ | ----------- | ----------- |
| **Pay in 2**       | EUR          | 50          | 5,000       |
| **Pay in 3**       | EUR          | 50          | 5,000       |
| **Pay in 4**       | EUR          | 50          | 5,000       |

## Prohibited business categories

In addition to the industry and business categories listed in [Prohibited and restricted business](https://stripe.com/restricted-businesses), Alma prohibits the following categories:

- Sole proprietorships or individual accounts
- Business to Business Services
- Educational services
- Professional services (including, but not limited to, legal, consulting, and accounting)
- Transportation services
- Travel services
- Telecommunication services and utilities
- Veterinary services

See a [full list of prohibited activities](https://help.almapay.com/hc/en-gb/articles/360006779359-Which-activities-are-not-eligible-for-payment-with-Alma). Even if an activity isn’t listed as prohibited, your business might still be ineligible for Alma due to risk-related reasons.

## Customer terms

Alma requires that you add the following terms to your general terms of sale:

- Customers can make purchases in installments using Alma.
- A customer’s purchase using Alma is subject to Alma’s terms and conditions.
- Non-approval by Alma for a purchase can result in the cancellation of that purchase.
- A customer using Alma to purchase a good or service has a period of 14 calendar days in which they can withdraw the purchase.

## Refunds

Alma supports full and partial refunds. The refund period is up to 180 days after the purchase. Refunds for Alma payments are asynchronous and take up to 5 minutes to complete. We’ll notify you of the final refund status using the `refund.updated` or `refund.failed` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. When a refund succeeds, the [Refund](https://docs.stripe.com/api/refunds/object.md) object’s status transitions to `succeeded`. If a refund fails, the Refund object’s status transitions to `failed` and we return the amount to your Stripe balance. You then need to arrange an alternative way of providing your customer with a refund.

## Disputes

Customers must authenticate Alma payments by logging into their Alma account. This requirement helps reduce the risk of fraud or unrecognized payments. While Alma covers losses incurred from customer fraud, Alma might contact you and request to stop or pause shipment before incurring any losses. Please comply promptly with these requests.

Customers have up to 120 calendar days from the date of purchase to file a dispute. The dispute process works like this:

- After the customer initiates a dispute, Stripe notifies you through email, the Stripe Dashboard, and an API `charge.dispute.created` event (if your integration is set up to receive [webhooks](https://docs.stripe.com/webhooks.md)).

- Stripe holds back the disputed amount from your balance until Alma resolves the dispute.

- Stripe requests that you upload compelling evidence that you fulfilled the purchase order [using the Stripe Dashboard](https://docs.stripe.com/disputes/responding.md#respond). This evidence can include:
  - A received return confirmation (for shipped goods returned from the customer to you)
  - The tracking ID
  - The shipping date
  - A record of purchase for intangible goods, such as IP address or email receipt
  - A record of purchase for services or physical goods, such as phone number or proof of receipt

- This information helps Alma determine if a dispute is valid or if it should be rejected. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 14 calendar days. Alma makes a decision within 25 calendar days of evidence submission. If Alma resolves the dispute with you winning, Stripe returns the disputed amount to your Stripe balance. If Alma rules in favor of the customer, the balance charge becomes permanent.

If you prefer to handle disputes programmatically, you can [respond to disputes using the API](https://docs.stripe.com/disputes/api.md).

> Alma requires merchants to maintain reasonable fraud and dispute rates. Increases to your fraud and dispute rates might result in losing access to Alma.

## Connect

Alma is available for online marketplaces using [Stripe Connect](https://stripe.com/connect). These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. Alma isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

> Online marketplaces need to submit an onboarding request from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) to get access to Alma. Stripe sends email updates about the progress of all requests, and the current status is also reflected on the [Payment methods settings page](https://dashboard.stripe.com/settings/payment_methods).

The following [Connect charges](https://docs.stripe.com/connect/charges.md) types, typically used by online marketplaces, are available to businesses using Alma.

| Destination charges | Separate charges and transfers | Direct charges | `on_behalf_of` |
| ------------------- | ------------------------------ | -------------- | -------------- |
| ✓ Supported         | ✓ Supported                    | ✓ Supported    | ✓ Supported    |

## Supported currencies

You can create Alma payments in the currencies that map to your country. The default local currency for Alma is `eur` and customers also see their purchase amount in `eur`.

| Currency | Country                                                |
| -------- | ------------------------------------------------------ |
| `eur`    | France, Italy, Spain, Netherlands, Belgium, Luxembourg |
