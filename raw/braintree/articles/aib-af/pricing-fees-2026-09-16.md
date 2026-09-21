<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-af/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/aib-af/pricing-fees/
createTime: '2025-04-02T00:28:06.810Z'
updateTime: '2025-04-02T00:28:06.845Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Fees can be broken down into the following categories:


- **Ad valorem**: Percentage we take from each transaction
- **Per transaction fee**: Static monetary amount deducted from each transaction
- **Chargeback fee**: Fixed fee charged by the processing banks that manage the chargeback
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Scheme fees**: Variable fees assessed by the card associations (e.g. Visa and Mastercard)
- **Multi-currency fee**: Percentage we take from each transaction that requires currency conversion (this fee is included in your ad valorem percentage)
- **Cross border fee**: Percentage we take from each transaction made using a card that was issued outside of the country where your business is located

Depending on your [pricing model](#pricing-models), interchange fees and scheme fees may be charged separately or included in your ad valorem percentage. If you transact with customers from other countries, you may be charged either a multi-currency fee or a [cross border fee](#special-note-on-cross-border-fees), depending on your account setup and your customers' countries.

All fees are deducted from your disbursements, and Braintree’s processing fee is only applied to **successful sale transactions**. It is not applied to refunds, verifications, declines, gateway rejections, or voids. Interchange and scheme fees, however, may be applied to any type of transaction.


**IMPORTANT**
 If you use your own AmEx account, you will not be charged an ad valorem, but you will be charged a per transaction fee on top of both interchange fees and what you are charged by AmEx directly.

 


### Special note on cross border fees

Cross border fees will not be applied to transactions made with Mastercard and Visa cards issued in certain countries.

Countries without cross border fees


**NOTE**
 The X indicates that cross border fees are not applied to cards issued in that country.

 

| Country | Mastercard | Visa |
| --- | --- | --- |
| Aland Islands | X |  |
| Austria | X | X |
| Belgium | X | X |
| Bulgaria | X | X |
| Croatia | X | X |
| Cyprus | X | X |
| Czech Republic | X | X |
| Denmark | X | X |
| Estonia | X | X |
| Faroe Islands |  | X |
| Finland | X | X |
| France | X | X |
| French Guiana | X | X |
| Germany | X | X |
| Gibraltar | X | X |
| Greece | X | X |
| Greenland |  | X |
| Guadeloupe | X |  |
| Guernsey |  | X |
| Hungary | X | X |
| Iceland | X | X |
| Ireland | X | X |
| Isle of Man |  | X |
| Italy | X | X |
| Jersey |  | X |
| Latvia | X | X |
| Liechtenstein | X | X |
| Lithuania | X | X |
| Luxembourg | X | X |
| Malta | X | X |
| Martinique | X |  |
| Mayotte | X |  |
| Netherlands | X | X |
| Norway | X | X |
| Poland | X | X |
| Portugal | X | X |
| Romania | X | X |
| Saint Barthelemy |  | X |
| Saint Martin - French | X | X |
| Saint Pierre and Miquelon |  | X |
| Slovakia | X | X |
| Slovenia | X | X |
| Spain | X | X |
| Svalbard and Jan Mayen | X |  |
| Sweden | X | X |
| United Kingdom | X | X |


## Pricing models

Your pricing model was determined when you originally signed up for an account. [Contact us](/braintree/help/feeHelp) if you have questions about which pricing model applies to your account.

You can view your pricing model fee rates by looking at the [**Merchant Service Charges**](/braintree/articles/aib-af/statements#merchant-service-charges) portion of your statement.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. The blended model consists of an ad valorem and per transaction fee. Depending on your account setup, you may have different rates for debit cards and credit cards.


### IC+

IC+ pricing consists of the Braintree processing fees and interchange fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees applied to each transaction vary primarily by card brand, but can also be affected by a number of other factors such as card type, region, and more.


### IC++

IC++ pricing consists of an ad valorem, per transaction fee, interchange fees, and scheme fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. Similar to interchange fees, scheme fees are variable and are not determined by Braintree. The specific fees that are applied to each transaction depend primarily on card type, but include a number of other factors such as the type of merchant, cost of sale, processing technology, region, and more.


## Reporting

You can view all fees assessed and deducted from a specific transaction in the AIB Transaction Fee Report. This report will be available the day a [transaction is disbursed](/braintree/articles/get-started/transaction-lifecycle). To find this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Next to**AIB Transaction Fee Report**, click the**Run Report**button


## Refunds and credits

Braintree transaction fees will not be returned for refunded transactions. This means that if you issue a full or partial refund to a buyer, or refund a donation to a donor, we won't charge additional fees to make the refund but the processing fees that you originally paid will not be returned to you.


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/aib-af/chargebacks-retrievals-prearbs), you will be charged a non-refundable chargeback fee. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time.

