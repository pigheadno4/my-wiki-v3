<!-- Source URL: https://docs.stripe.com/payments/payment-methods/overview -->
<!-- Fetched: 2026-11-07 -->
<!-- Discovery: reconciled llms.txt,sitemap.xml -->

# Add payment methods

Find the payment methods your customers prefer and learn how to offer them.

Customers in different regions prefer different ways to pay, and not all customers have or prefer a card. Stripe supports a range of payment methods so you can offer the ones your customers expect.

Use the following resources to answer common questions about offering payment methods:

| Question | Resource |
| --- | --- |
| Which payment methods can my business offer? | [Country and currency support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#country-currency-support) |
| How much does each payment method cost? | [Pricing for payment methods](https://stripe.com/pricing/local-payment-methods) |
| How do I turn on payment methods? | [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) |
| Which Stripe products support each payment method? | [Product support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#product-support) |
| How do I add payment methods to my integration? | [Payment method integration options](https://docs.stripe.com/payments/payment-methods/integration-options.md) |

## Turn on payment methods 

If you use [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) with [Checkout](https://docs.stripe.com/payments/checkout.md), the [Payment Element](https://docs.stripe.com/payments/payment-element.md), [Payment Links](https://docs.stripe.com/payment-links.md), or the hosted invoice page, you can turn on most payment methods in your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) without changing your code. Stripe then displays the eligible payment methods to each customer.

If your integration lists payment methods explicitly with [payment_method_types](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-payment_method_types), you must update your code to add a payment method. Some payment methods have additional requirements, so check the documentation for each payment method before you turn it on.

## Payment method families 

Stripe groups payment methods into the following payment method families. Payment methods in the same family have similar features and checkout experiences. After you integrate one payment method, you can usually add another in the same family with minimal changes to your integration.

- [Cards](https://docs.stripe.com/payments/payment-methods/overview.md#cards)
- [Bank debits](https://docs.stripe.com/payments/payment-methods/overview.md#bank-debits)
- [Bank redirects](https://docs.stripe.com/payments/payment-methods/overview.md#bank-redirects)
- [Bank transfers](https://docs.stripe.com/payments/payment-methods/overview.md#bank-transfers)
- [Buy now, pay later](https://docs.stripe.com/payments/payment-methods/overview.md#buy-now-pay-later)
- [Real-time payments](https://docs.stripe.com/payments/payment-methods/overview.md#real-time-payments)
- [Stablecoin payments](https://docs.stripe.com/payments/payment-methods/overview.md#stablecoin-payments)
- [Vouchers](https://docs.stripe.com/payments/payment-methods/overview.md#vouchers)
- [Wallets](https://docs.stripe.com/payments/payment-methods/overview.md#wallets)
- [Gift cards](https://docs.stripe.com/payments/payment-methods/overview.md#gift-cards)

Payment methods labeled **Private preview** or **Public preview** have limited availability. To request access to a payment method in private preview, see the documentation for that payment method.
[Watch on YouTube](https://www.youtube.com/watch?v=tJin1R6KLyA)
## Cards 

Cards are a common way for customers and businesses to pay online or in person. Stripe supports [global and local card networks](https://docs.stripe.com/payments/cards.md#supported-card-brands).

Payment methods are grouped by the regions where they’re commonly used. See the documentation for each method to understand its eligibility for your business and customers.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| [Visa](https://docs.stripe.com/payments/cards.md#supported-card-brands) | [Discover](https://docs.stripe.com/payments/cards.md#supported-card-brands) | [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires.md) | [eftpos](https://docs.stripe.com/payments/cards.md#supported-card-brands) | — |
| [Mastercard](https://docs.stripe.com/payments/cards.md#supported-card-brands) | [Interac (In-person only)](https://docs.stripe.com/terminal/payments/regional.md?country=CA) |  | [JCB](https://docs.stripe.com/payments/cards.md#supported-card-brands) |  |
| [American Express](https://docs.stripe.com/payments/cards.md#supported-card-brands) |  |  | [China UnionPay](https://docs.stripe.com/payments/cards.md#supported-card-brands) |  |
| [Diners Club](https://docs.stripe.com/payments/cards.md#supported-card-brands) |  |  | [South Korean cards](https://docs.stripe.com/payments/countries/korea.md) |  |

Some card payments support [installments](https://docs.stripe.com/payments/installments.md). For example, customers in Mexico can split credit card purchases into monthly payments with [Meses sin intereses](https://docs.stripe.com/payments/mx-installments.md).

In-person payments support different card brands, depending on the country and reader type. For more information, see Terminal’s [supported card brands](https://docs.stripe.com/terminal/payments/collect-card-payment/supported-card-brands.md#payment-method-availability).

## Bank debits 

With [bank debits](https://docs.stripe.com/payments/bank-debits.md), you pull funds directly from your customer’s bank account for one-time and recurring payments. Payment confirmation can take several business days. For fees, see [pricing details](https://stripe.com/pricing/local-payment-methods).

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | [ACH Direct Debit](https://docs.stripe.com/payments/ach-direct-debit.md) | [Bacs Direct Debit](https://docs.stripe.com/payments/bacs-debit.md) | [AU BECS Direct Debit](https://docs.stripe.com/payments/au-becs-debit.md) | — |
|  | [Canadian pre-authorized debits](https://docs.stripe.com/payments/acss-debit.md) | [SEPA Direct Debit](https://docs.stripe.com/payments/sepa-debit.md) | [NZ BECS Direct Debit](https://docs.stripe.com/payments/nz-bank-account.md) |  |
|  | [Instant Bank Payments](https://docs.stripe.com/payments/link/instant-bank-payments.md) |  |  |  |

## Bank redirects 

With [bank redirects](https://docs.stripe.com/payments/bank-redirects.md), customers pay online by authenticating with their bank and approving the payment from their bank account.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | — | [Bancontact](https://docs.stripe.com/payments/bancontact.md) | [FPX](https://docs.stripe.com/payments/fpx.md) | — |
|  |  | [BLIK](https://docs.stripe.com/payments/blik.md) |  |  |
|  |  | [EPS](https://docs.stripe.com/payments/eps.md) |  |  |
|  |  | [iDEAL | Wero](https://docs.stripe.com/payments/ideal.md) |  |  |
|  |  | [P24](https://docs.stripe.com/payments/p24.md) |  |  |
|  |  | [Wero (Public preview)](https://docs.stripe.com/payments/wero.md) |  |  |

## Bank transfers 

With [bank transfers](https://docs.stripe.com/payments/bank-transfers.md), you give customers a virtual bank account number, and they push money to it from their online bank or a bank branch. Stripe uses the virtual account number to reconcile payments automatically without exposing your bank account details. Bank transfers are common for large payments between businesses, and in some countries for payments by individuals.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | [USD bank transfer](https://docs.stripe.com/payments/bank-transfers.md) | [SEPA bank transfer](https://docs.stripe.com/payments/bank-transfers.md) | [Japan bank transfer (Furikomi)](https://docs.stripe.com/payments/bank-transfers.md) | [Mexico bank transfer](https://docs.stripe.com/payments/bank-transfers.md) |
|  |  | [UK bank transfer](https://docs.stripe.com/payments/bank-transfers.md) |  |  |

## Buy now, pay later 

With [buy now, pay later](https://docs.stripe.com/payments/buy-now-pay-later.md) payment methods, customers pay in installments or at a later date. Your business is paid in full up front, and your customer pays nothing or a portion of the total cost at checkout.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | [Affirm](https://docs.stripe.com/payments/affirm.md) | [Affirm (UK businesses only, private preview)](https://docs.stripe.com/payments/affirm.md) | [Afterpay (Australian and New Zealand businesses only)](https://docs.stripe.com/payments/afterpay-clearpay.md) | — |
|  | [Afterpay](https://docs.stripe.com/payments/afterpay-clearpay.md) | [Alma](https://docs.stripe.com/payments/alma.md) | [Klarna](https://docs.stripe.com/payments/klarna.md) |  |
|  | [Klarna](https://docs.stripe.com/payments/klarna.md) | [Billie (Business customers only)](https://docs.stripe.com/payments/billie.md) | [Zip (Australian businesses only)](https://docs.stripe.com/payments/zip.md) |  |
|  | [Sunbit (US businesses only)](https://docs.stripe.com/payments/sunbit.md) | [Clearpay (UK businesses only)](https://docs.stripe.com/payments/afterpay-clearpay.md) |  |  |
|  | [Zip (US businesses only)](https://docs.stripe.com/payments/zip.md) | [Klarna](https://docs.stripe.com/payments/klarna.md) |  |  |
|  |  | [Kriya (UK business customers only, private preview)](https://docs.stripe.com/payments/kriya.md) |  |  |
|  |  | [Mondu (Business customers only, private preview)](https://docs.stripe.com/payments/mondu.md) |  |  |
|  |  | [Scalapay](https://docs.stripe.com/payments/scalapay.md) |  |  |
|  |  | [SeQura (Spanish businesses only)](https://docs.stripe.com/payments/sequra.md) |  |  |

## Real-time payments 

With [real-time payments](https://docs.stripe.com/payments/real-time.md), customers send money directly from their bank account or other funding source, using an intermediary such as a phone number or app to authenticate.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | — | [Bizum](https://docs.stripe.com/payments/bizum.md) | [PayNow](https://docs.stripe.com/payments/paynow.md) | [Pix](https://docs.stripe.com/payments/pix.md) |
|  |  | [Pay by Bank](https://docs.stripe.com/payments/pay-by-bank.md) | [PayTo](https://docs.stripe.com/payments/payto.md) |  |
|  |  | [Swish (Private preview)](https://docs.stripe.com/payments/swish.md) | [PromptPay](https://docs.stripe.com/payments/promptpay.md) |  |
|  |  |  | [UPI](https://docs.stripe.com/payments/upi.md) |  |

## Stablecoin payments 

With stablecoin payments, customers pay with stablecoins from their preferred crypto wallet, and completed payments settle in your Stripe balance in your local currency. See [stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) to learn more.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| [Stablecoin payments](https://docs.stripe.com/payments/stablecoin-payments.md) | — | — | — | — |

## Vouchers 

With [vouchers](https://docs.stripe.com/payments/vouchers.md), customers complete online purchases in person. At checkout, customers receive a voucher with the transaction details, and then pay with it at a local store, bank, or other location.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | — | [Multibanco](https://docs.stripe.com/payments/multibanco.md) | [Konbini](https://docs.stripe.com/payments/konbini.md) | [Boleto](https://docs.stripe.com/payments/boleto.md) |
|  |  |  |  | [OXXO](https://docs.stripe.com/payments/oxxo.md) |

## Wallets 

With [wallets](https://docs.stripe.com/payments/wallets.md), customers pay with a saved card or a stored balance.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| [Apple Pay](https://docs.stripe.com/apple-pay.md) | [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) | [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md) | [AEON Pay (Private preview)](https://docs.stripe.com/payments/aeon-pay.md) | — |
| [Google Pay (Not available in India)](https://docs.stripe.com/google-pay.md) | [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md) | [MB WAY](https://docs.stripe.com/payments/mb-way.md) | [Alipay](https://docs.stripe.com/payments/alipay.md) |  |
| [Link](https://docs.stripe.com/payments/wallets/link.md) |  | [MobilePay](https://docs.stripe.com/payments/mobilepay.md) | [au PAY (Private preview)](https://docs.stripe.com/payments/au-pay.md) |  |
| [Secure Remote Commerce](https://docs.stripe.com/secure-remote-commerce.md) |  | [PayPal](https://docs.stripe.com/payments/paypal.md) | [d-Barai (Private preview)](https://docs.stripe.com/payments/d-barai.md) |  |
|  |  | [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md) | [GrabPay](https://docs.stripe.com/payments/grabpay.md) |  |
|  |  | [Satispay](https://docs.stripe.com/payments/satispay.md) | [Kakao Pay](https://docs.stripe.com/payments/countries/korea.md) |  |
|  |  |  | [Merpay (Private preview)](https://docs.stripe.com/payments/merpay.md) |  |
|  |  |  | [Naver Pay](https://docs.stripe.com/payments/countries/korea.md) |  |
|  |  | [TWINT](https://docs.stripe.com/payments/twint.md) | [PAYCO](https://docs.stripe.com/payments/countries/korea.md) |  |
|  |  |  | [PayPay](https://docs.stripe.com/payments/paypay.md) |  |
|  |  |  | [Rakuten Pay (Private preview)](https://docs.stripe.com/payments/rakuten-pay.md) |  |
|  |  |  | [Samsung Pay](https://docs.stripe.com/payments/countries/korea.md) |  |
|  |  |  | [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) |  |

## Gift cards 

With closed-loop gift cards, customers pay with stored value that they can redeem only with your business or a related group of businesses. Gift card payments settle outside of Stripe. See [gift cards](https://docs.stripe.com/payments/gift-cards.md) to learn more.

| Global | US and Canada | Europe | Asia Pacific | Latin America |
| --- | --- | --- | --- | --- |
| — | [Gift cards (US only, private preview)](https://docs.stripe.com/payments/gift-cards.md) | — | — | — |

## Custom payment methods 

If you need a payment method that’s not on this page, see [custom payment methods](https://docs.stripe.com/payments/payment-methods/custom-payment-methods.md).

## See also

- [Payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support.md)
- [Dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md)
- [Guide to payment methods](https://stripe.com/payments/payment-methods-guide)
