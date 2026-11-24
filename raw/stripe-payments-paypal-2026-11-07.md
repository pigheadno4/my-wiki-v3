<!-- Source URL: https://docs.stripe.com/payments/paypal -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# PayPal payments

Learn about PayPal, a popular digital wallet.

PayPal is a payment method that enables customers in any country to pay using their PayPal account.

To pay using PayPal, customers are redirected from your website to PayPal. They choose a funding source: PayPal wallet, linked card or bank account, or buy now, pay later. Then they authenticate the payment. After successful authorization, the customer is redirected back to your website. You receive an [immediate notification](https://docs.stripe.com/payments/payment-methods.md#payment-notification) of the payment’s success or failure.

> This page covers PayPal processed through Stripe, available to businesses in [supported European countries](https://docs.stripe.com/payments/paypal.md#business-locations). If your Stripe account is outside these countries, or you want to process PayPal payments through your own PayPal account, see [PayPal custom payment method](https://docs.stripe.com/payments/payment-methods/custom-payment-methods/paypal.md).

#### Payment method properties

- **Customer locations**

  Worldwide

- **Presentment currency**

  EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD

- **Payment method family**

  Wallets

- **Payment confirmation**

  Customer-initiated

- **Payout timing**

  [Standard payout timing](https://docs.stripe.com/payouts.md#payout-speed) applies

- **Connect support**

  Partial (requires manual approval, see details [below](https://docs.stripe.com/payments/paypal.md#connect))

- **Recurring payments**

  Yes, but might [require approval](https://docs.stripe.com/payments/paypal/set-up-future-payments.md#enable-recurring-payments)

- **Dispute support**

  [Yes](https://docs.stripe.com/payments/paypal.md#disputed-payments)

- **Refunds / Partial refunds**

  [Yes / Yes](https://docs.stripe.com/payments/paypal.md#refunds)

#### Business locations

Stripe accounts in the following countries can accept PayPal payments:

- AT
- BE
- BG
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
- GR
- HR
- IE
- IT
- LI
- LT
- LU
- LV
- MT
- NL
- NO
- PL
- PT
- RO
- SE
- SI
- SK

#### Product support

- Connect
- Checkout
- Payment Links
- Elements
- Subscriptions
- Invoicing

## Payment flow 
![](https://b.stripecdn.com/docs-statics-srv/assets/checkout.4af16ecfd4f0a3f4044c56d6100c4a42.svg)

*Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) selects PayPal at checkout
![](https://b.stripecdn.com/docs-statics-srv/assets/redirect.f6e6ccf58078e0a25815560086204c24.svg)

Customer is redirected to PayPal and enters login details
![](https://b.stripecdn.com/docs-statics-srv/assets/pincode-sms.d10a5a14a3a7e5d3c00942531f9143cd.svg)

Customer completes authorization process
![](https://b.stripecdn.com/docs-statics-srv/assets/redirect-success.740e23b33b6f52a746e8ec50285e2805.svg)

Customer is notified that payment is complete
![](https://b.stripecdn.com/docs-statics-srv/assets/success.1ee3b6d34d944693e654e84f6d1be9f3.svg)

(Optional) Customer returns back to business’s site for payment confirmation

## Connect 

PayPal is available for online marketplaces using [Stripe Connect](https://stripe.com/connect). These online marketplaces include businesses such as Deliveroo and ManoMano that collect payments from customers, and later pay out to sub-accounts or service providers. PayPal isn’t available for platforms that onboard other businesses and enable them to accept payments directly, such as Shopify or Squarespace.

### Request access

To use PayPal for Connect charges, online marketplaces must request access.

1. In the Dashboard, go to [Payment method settings](https://dashboard.stripe.com/settings/payment_methods).
2. Click **Request access** next to PayPal, and complete the form.

Stripe and PayPal review each request, which can take several weeks. You can track the progress on the **Payment method settings** page.

After your request is approved, you receive instructions for connecting your PayPal account.

Because PayPal doesn’t support direct charges or `on_behalf_of`, you don’t need to enable it on connected accounts’ payment method configurations.

The following [Connect charges](https://docs.stripe.com/connect/charges.md) types, typically used by online marketplaces, are available to businesses using PayPal.

| Destination charges | Separate charges and transfers | Direct charges | on_behalf_of |
| --- | --- | --- | --- |
| ✓ Supported | ✓ Supported | ❌ Not supported | ❌ Not supported |

## Get started 

Add PayPal and other payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) without making updates to your code. For each customer, Stripe determines the list of supported payment methods most likely to drive conversion. Learn how to [accept PayPal and other payment methods automatically](https://docs.stripe.com/payments/accept-a-payment.md) with Checkout or Elements. To accept PayPal and other payment methods without any code, use [Payment Links](https://docs.stripe.com/payment-links.md).

When you’re ready to go live, [activate PayPal payments](https://docs.stripe.com/payments/paypal/activate.md).

## Disputed payments 

Customers must authenticate payments with their PayPal accounts, helping to reduce the risk of fraud or unrecognized payments. However, customers can still dispute transactions after they complete payment. Some common reasons for disputes are customers determining that items weren’t as described, or not receiving items at all. You can submit evidence to contest a dispute directly from the Stripe Dashboard.

Learn how to [manage PayPal disputes](https://docs.stripe.com/payments/paypal/disputed-payments.md) in the Dashboard.

For certain dispute types, PayPal enables you communicate directly to customers to try resolving the dispute. Contacting customers directly must be handled through the PayPal dashboard, and not the Stripe Dashboard.

## Refunds 

PayPal payments can be refunded up to 180 days after the original payment. Stripe uses either your Stripe balance or your PayPal balance to refund the payment, depending on the [settlement preference you selected](https://docs.stripe.com/payments/paypal/choose-settlement-preference.md).

You can use the Stripe Dashboard or API to initiate refund requests, as with other payment methods. If you choose to settle funds to Stripe, refunds will be withdrawn from the funds available in your Stripe account. If you choose to settle funds to PayPal, refunds funded using your PayPal balance or any other funding source available on your PayPal account.

## Reporting

PayPal fees are included in the **Less fees** sections of [Balance and Balance Activity reports](https://dashboard.stripe.com/reports/balance). PayPal fees aren’t included in your [tax invoice from Stripe](https://dashboard.stripe.com/settings/documents). You can access these documents from your PayPal dashboard.

## Seller protection

PayPal’s Seller Protection program offers coverage for sellers under eligible transactions. It includes scenarios such as unauthorized transactions or customers’ claims of non-receipt of item. For more information on the Seller Protection program and eligibility, visit [PayPal Seller Protection](https://www.paypal.com/uk/legalhub/seller-protection).

## Prohibited business categories

In addition to the business categories restricted from using Stripe overall, PayPal requires pre-approval to accept payments for certain services. Refer to the [PayPal Acceptable Use Policy](https://www.paypal.com/us/legalhub/acceptableuse-full) for details.

## Minimum and maximum charge amounts

PayPal doesn’t have a minimum charge amount, but Stripe enforces the same [minimum and maximum charge amounts](https://docs.stripe.com/currencies.md#minimum-and-maximum-charge-amounts) for PayPal as for other payment methods.
