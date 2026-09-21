<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-bf/pricing-fees -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Pricing and Fees
slug: /articles/aib-bf/pricing-fees/
createTime: '2025-04-02T01:14:38.148Z'
updateTime: '2025-04-02T01:14:38.191Z'
---



# Pricing and Fees


## Transaction fees

Before we go into the specifics of pricing and fees, it’s important to understand the different types of fees and what they are based on. Fees can be broken down into the following categories:


- **Discount rate**: Percentage we take from each transaction
- **Per transaction fee**: Static dollar amount deducted from each transaction
- **Braintree processing fees**: Discount rate and per transaction fees, combined
- **Interchange fees**: Variable fees assessed by the card issuing bank
- **Scheme fees**: Variable fees assessed by the card associations (e.g. Visa and Mastercard)
- **Chargeback fee**: Fixed fee charged by the processing banks that manage the chargeback
- **Multi-currency fee**: Percentage we take from each transaction that requires currency conversion
- **Cross border fee**: Percentage we take from each transaction made using a card that was issued outside of the country where your business is located
- **Kount fee**: Fixed fee charged for each Kount inquiry

Depending on your [pricing model](#pricing-models), interchange fees, scheme fees, and Kount fees may be charged separately or included in your Braintree processing fees. If you transact with customers from other countries, you may be charged either a multi-currency fee or a [cross border fee](#special-note-on-cross-border-fees), depending on your account setup and your customers' countries.

All fees are deducted from your daily disbursements and are only applied to **successful sale transactions**. Fees are not applied to refunds, verifications, declines, gateway rejections, or voids.

We do not display your processing fee rates in the Control Panel, but you can download a [statement](/braintree/articles/aib-bf/statements-reporting) to find your specific discount rate and per transaction fees.


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

Your pricing model was determined when you originally signed up for an account and can be identified by looking at the **Pricing Schedule** section found on your [statements](/braintree/articles/aib-bf/statements-reporting). IC+ accounts will be listed as Pricing Schedule - Interchange Plus. If your pricing schedule does not say interchange plus, then you are on our blended model.


### Blended

Blended pricing offers fixed rates, which makes it easier to accurately forecast your payment processing costs. This model only consists of Braintree processing fees - incorporating interchange into your fixed rate.


### IC+

IC+ pricing consists of the Braintree processing fees and interchange fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. The specific fees applied to each transaction vary primarily by card brand, but can also be affected by a number of other factors such as card type, region, and more.


### IC++

IC++ pricing consists of the Braintree processing fees, interchange fees, and scheme fees. Because interchange fees are variable and are not determined by Braintree, it can be harder to predict the exact amount you’ll be charged. Similar to interchange fees, scheme fees are variable and are not determined by Braintree. The specific fees applied to each transaction vary primarily by card type, but can also be affected by a number of other factors such as your type of business, cost of sale, processing technology, region, and more.


## Reporting

You can view all fees assessed and deducted from a specific sale transaction in the [Transaction Fee Report](/braintree/articles/aib-bf/statements-reporting#transaction-fee-report). This report will be available at the beginning of each month. To find this report:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Reports**in the navigation bar
- Click the**Statements**tab
- Under the**Merchant Statements**section, click the**View Statements**button
- Locate the appropriate merchant account, and click the**Transaction Fee Report**link next to the month you're interested in


## Rounding down

When calculating our processing fees, we round down if there is a remainder value past the penny. These are calculated on the transaction level, so if you manually multiply your fees by the **total** settled sales for a given month, there may be a slight discrepancy between the calculated value and the fee details listed on your statement.

As a result of rounding down, we often charge slightly less than your discount rate!


## Refunds and credits

Braintree transaction fees will not be returned for refunded transactions. This means that if you issue a full or partial refund to a buyer, or refund a donation to a donor, we won't charge additional fees to make the refund but the processing fees that you originally paid will not be returned to you.

Depending on your pricing model and the date you began processing with Braintree, we may credit back the Braintree processing fees that we charged for a transaction in the event that it is fully refunded. [Contact us](/braintree/help/feeHelp) with any questions regarding your setup.


## Chargebacks, retrievals, and pre-arbitrations

Regardless of whether you win a [chargeback or pre-arbitration](/braintree/articles/aib-bf/chargebacks-retrievals-prearbs), you will be charged a non-refundable chargeback fee. This fee only applies to chargebacks and pre-arbs; retrievals do not result in a fee at this time.

