<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/bank-identification-numbers -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Bank Identification Numbers
slug: /articles/control-panel/transactions/bank-identification-numbers/
createTime: '2025-04-02T00:16:42.886Z'
updateTime: '2025-10-08T13:07:44.961Z'
---



# Bank Identification Numbers

The first 6 digits of a debit or credit card are known as the bank identification number (BIN), or issuer identification number (IIN).

Looking up the BINs associated with cards you’re processing can provide a lot of insight into your business – like identifying trends in [declines](/braintree/articles/control-panel/reporting/decline-analysis) or purchases (e.g. where most of your customers are located, or what types of cards they use).

You can view and store BINs without compromising or changing your [PCI compliance requirements](/braintree/articles/risk-and-security/compliance/pci-compliance).


**NOTE**
Effective April 2022, Visa and Mastercard will begin assigning 8-digit issue BINs. [See more about 8-digit BIN readiness](/braintree/articles/control-panel/transactions/bank-identification-numbers#8-digit-bin-expansion-readiness) . If you do not use the BIN in your integration, there is no action needed for you as a result of this change.


## Finding BINs in the gateway

For a single transaction, you can view the associated card's BIN in the Control Panel. Find these details by running a transaction search:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button

You will see the BIN in the search results, as the first 6 digits under the Payment Information column.

If you want to compare BINs across multiple transactions, download your transaction search into a CSV file by clicking the **Download** button at the top of the search results page. The BINs will be in the First Six of Credit Card column of the CSV file.

You can also find BINs by [searching a transaction ID via the API](/braintree/docs/reference/request/transaction/search). The response object will include the BIN as one of the parameters, and you can investigate from there.


## 8-Digit BIN expansion readiness

Effective April 2022, both Visa and Mastercard will begin assigning 8-digit issuer BINs, and all stakeholders that process with Visa and Mastercard must be ready to handle and process 8-digit BINs at this time. Braintree already processes 8-digit bins and this expansion will not have any impact to your current Braintree payment processing integration.


### Existing issued card processing and current practices

Because Primary Account Number (PAN) length will remain 16 digits, there is no need to proactively reissue existing cards. The BIN will become the existing first 8 digits of the PAN.


#### Integrations

There are no required changes to your integration.


#### BIN data availability

Existing Braintree APIs, GraphQL integrations, console search, and BIN reports will continue to provide 6 digit BINs.


### Payment Card Industry Data Security Standards (e.g. PCI, DSS) and BIN Expansion


#### Display of PAN

PCI standards* require that the PAN must be masked when it appears (the first six and/or last four digits is the maximum number of digits that will appear), so that only staff with a legitimate business need can see more than the first six/last four digits of the PAN (e.g 123456******0001).


#### Data at rest

PCI standards* allow merchants to safely store the PAN of the card through truncation. Merchants that use truncation as their only method of complying with the PCI requirement for protecting data at rest will need to add one or more of the other acceptable methods for data protection, such as encryption, hashing, or tokenization.

For more information, [see this post from the PCI security standards blog](https://blog.pcisecuritystandards.org/8-digit-bins-and-pci-dss-what-you-need-to-know)   and the [Visa webinar on 8-digit BIN PCI impact](https://usa.visa.com/supporting-info/eight-digit-bin-pci-impact-webinar.html)

* PCI DSS v3.2.1 standard, 3.3 requirement


### Additional resources


- [Visa 8-digit BIN FAQs](https://usa.visa.com/dam/VCOM/global/partner-with-us/documents/visa.com-numerics-faq.pdf)


- [Mastercard 8-digit BIN announcement](https://www.mastercard.com/content/dam/public/mastercardcom/globalrisk/pdf/8-Digit%20BIN%20Expansion%20and%20PCI%20Standards%20-%20FINAL%20(10-20-2021).pdf)



