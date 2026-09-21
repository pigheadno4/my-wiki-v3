<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/reporting/decline-analysis -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Decline Analysis
slug: /articles/control-panel/reporting/decline-analysis/
createTime: '2025-04-01T22:48:25.290Z'
updateTime: '2025-04-01T22:48:25.311Z'
---



# Decline Analysis

While we monitor your decline rates and will notify you if we see anything unusual, you can also proactively keep an eye on these rates. You can do this by first running an advanced search for all declined transactions, and then analyzing the results.


## Running a decline search

To search for declines:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Under**Status**, leave only the box next toProcessor Declinedchecked
- Adjust the date range as needed
- Click the**Search**button
- If you'd like to download a CSV file, click the**Download**button


**NOTE**
 If you aren’t finding the declines you expected and you’re using card verification, try running a [verification search](/braintree/articles/control-panel/search#verifications) instead.

 


## Analyzing the results

The analysis process will be unique to your business, but in general, the more data you collect on customer transactions, the more helpful these results will be. For example, if you pass cardholder names or email addresses with transactions, you can often spot fake ones easily.


### Processor responses

We find the easiest way to spot trends in your downloaded search results is to organize the data by processor response. You can do this by generating a [pivot table](http://office.microsoft.com/en-001/excel-help/quick-start-create-a-pivottable-report-HA010359471.aspx) filtered by Processor Response Text. For more information about what each processor response indicates, [see our developer docs](/braintree/docs/reference/general/processor-responses/authorization-responses#declines).

Keep in mind that repeated transaction attempts with the same payment method can skew your decline rates. You can [remove duplicate values](http://office.microsoft.com/en-us/excel-help/filter-for-unique-values-or-remove-duplicate-values-HP010073943.aspx) from your CSV to get a clearer picture of unique declines.


### Bank identification numbers

If you’ve noticed a spike in processor declines for your transactions, you can use the [bank identification numbers (BINs)](/braintree/articles/control-panel/transactions/bank-identification-numbers) to identify trends in the declined cards.

Generate a [pivot table](http://office.microsoft.com/en-001/excel-help/quick-start-create-a-pivottable-report-HA010359471.aspx) of your decline data, filtered by First Six of Credit Card. You can then look up the BINs in a [BIN database](/braintree/articles/control-panel/transactions/bank-identification-numbers#bin-databases) to see where they’re coming from. From there, you may be able to pinpoint whether the declines are specific to a card type, location, or possible [prohibited transactions](/braintree/articles/risk-and-security/compliance/prohibited-transactions).

For example, if you find that 40% of your declines are coming from BINs connected to the same bank, you could contact the bank to see if they have had any processing issues that would explain the declines.


## Reducing declines

You can generally reduce your decline rates due to fraudulent transactions by implementing [Braintree’s Fraud Tools](/braintree/articles/guides/fraud-tools/overview). [Contact us](/braintree/help/FraudProtectionQuestion) if you have any questions or concerns.

