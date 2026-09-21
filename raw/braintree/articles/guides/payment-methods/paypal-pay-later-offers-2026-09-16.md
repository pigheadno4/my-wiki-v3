<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal-pay-later-offers -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PayPal Pay Later Offers
slug: /articles/guides/payment-methods/paypal-pay-later-offers/
createTime: '2025-04-01T23:04:05.486Z'
updateTime: '2025-12-12T10:20:48.871Z'
---



# PayPal Pay Later Offers

PayPal offers short-term, interest-free payments, longer-term, monthly installments, and other special financing options that buyers can use to buy now and pay later, while merchants get paid up-front. Pay Later offers are included with PayPal Checkout at no additional cost to you unless you are in the US.

Pay Later offers include the following, depending on the country of your customers:

| Country | Pay Later offers | Notes |
| --- | --- | --- |
| US | **Pay in 4**, which eligible US buyers can use to pay for purchases of $30 to $1500 in four, interest-free payments.      **Pay Monthly**, a longer-term installment offer available to eligible US buyers for purchases of $199 to $10,000, with terms of 6, 12, or 24 monthly payments. | About Pay in 4: Loans to CA residents are made or arranged pursuant to a CA Financing Law License. PayPal, Inc. is a GA Installment Lender Licensee, NMLS #910457. RI Small Loan Lender Licensee.     Pay Monthly is subject to consumer credit approval. Term lengths and fixed APR of 9.99-35.99% vary based on the customer’s creditworthiness. The lender for Pay Monthly is WebBank. PayPal, Inc. (NMLS #910457): RI Loan Broker Licensee. VT Loan Solicitation Licensee. |
| UK | **Pay in 3**, which eligible UK buyers can use to pay for purchases of £30.00 to £2,000 in three, interest-free payments.      **PayPal Credit** has two promotional offers, 0% for 4 months on purchases over £99 and merchant-specific Instalment offers. | If you offer PayPal Credit Instalments, you can't offer Pay in 3.     PayPal Credit is a regulated consumer credit product in the UK. Eligible customers can use it as a payment method through PayPal. However, you should only promote this product if you have the necessary regulatory permissions. For more information, please contact business customer support through [paypal.com](http://paypal.com). |
| FR | **Pay in 4X**, which eligible FR buyers can use to pay for purchases of €30.00 to €2,000 in four, interest-free payments. | PayPal Pay in 4X is subject to PayPal account status and eligibility criteria. Exclusions apply. Credit approval required. |
| AU | **Pay in 4**, which eligible AU buyers can use to pay for purchases of $30 to $1500 in four, interest-free payments. | Offer subject to PayPal account status and eligibility criteria. Exclusions apply. Credit approval required and may affect some customers’ credit report. |
| DE | **PayPal Ratenzahlung**, which eligible DE buyers can use to pay for purchases of €99 to €5,000 in 3, 6, 12, or 24 monthly installments.      **PayPal Pay in 30**, which eligible DE buyers can use to make purchases up to €1,000 and pay for it after 30 days without additional costs. | You can offer special financing to your customers by activating our [0% financing](https://www.paypal.com/merchantapps/appcenter/accelerategrowth/buydown) offer. This will further drive PayPal [Ratenzahlung’s](https://www.paypal.com/de/webapps/mpp/installments) adoption. |
| IT | **PayPal Pay in 3 instalments**, which eligible IT buyers can use to pay for purchases of €30 to €2,000 in three interest-free payments. | PayPal Pay in 3 instalments is subject to PayPal account status and eligibility criteria. Exclusions apply. Credit approval required. |
| ES | **PayPal Pay in 3 instalments**, which eligible ES buyers can use to pay for purchases of €30 to €2,000 in three interest-free payments. | PayPal Pay in 3 instalments is subject to PayPal account status and eligibility criteria. Exclusions apply. Credit approval required. |


## Availability

Consumers based in above countries are eligible for Pay Later offers across most of our integrations. Eligibility for merchants differs and depends on your location and integration. See the [overview](/braintree/docs/guides/paypal/overview) section for details and reach out to your PayPal account manager or [contact us](/braintree/help/acceptPaymentTypes) for more information.

To enable Pay Later offers on your [Checkout with Vault](/braintree/docs/guides/paypal/checkout-with-vault) integration, reach out to your PayPal account manager or [contact us](/braintree/help/acceptPaymentTypes).


### Customer availability

Your customers can apply to use this financing option by selecting **Pay Later** in your checkout. From there, their eligibility to use Pay Later options will be determined in seconds. [Learn more about how PayPal Pay Later works for customers](https://developer.paypal.com/docs/business/payment-methods/pay-later/).


## Setup

To enable PayPal Pay Later messaging, you must make a few minor changes to your existing [PayPal setup](/braintree/articles/guides/payment-methods/paypal/setup-guide). Full integration instructions are available in our [developer docs](/braintree/docs/guides/paypal/pay-later-offers).


### Pay Later messaging

Let your customers know they can buy now and pay later. With dynamic messaging, we'll show them the right offer for what they're buying - from short-term, interest-free installments, longer-term, monthly installments, to other special financing options. You must show the Pay Later button if you present Pay Later messaging. For details on how to integrate Pay Later messaging, see our [developer docs](/braintree/docs/guides/paypal/pay-later-offers#pay-later-messaging).

You can learn more about the effectiveness of messaging on the web and get the code from [PayPal messaging documentation](https://developer.paypal.com/docs/business/checkout/pay-later-messaging). The portal also includes guides for choosing the type of messaging and recommendations on where to place them.


**IMPORTANT**
 Please note that, while this option provides messaging that can be displayed on your website to help promote this feature to your customers, no additional content, wording, marketing or other material should be created by you to encourage use of this product. PayPal reserves the right to take action in accordance with the User Agreement.

 

