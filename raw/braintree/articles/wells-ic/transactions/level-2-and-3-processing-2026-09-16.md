<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-ic/transactions/level-2-and-3-processing -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Level 2 and 3 Processing
slug: /articles/wells-ic/transactions/level-2-and-3-processing/
createTime: '2025-04-02T01:17:50.945Z'
updateTime: '2025-04-02T01:17:50.960Z'
---



# Level 2 and 3 Processing

For certain Mastercard and Visa cards, credit card processing fits into 3 levels: Level 1, Level 2, and Level 3. Each level is defined by how much information about the transaction is required and stored to complete the payment. Level 1 requires the least information for processing, and is the default at which all of your Braintree transactions are passed.

While Level 1 processing is the standard, some business cases would benefit from processing higher level transactions.


## Availability

Level 2 and 3 processing is only appropriate for specific business use-cases. Keep the following in mind:


- Some business types, like travel and entertainment, are not eligible
- Level 2 and 3 processing is intended primarily for business to business transactions
- Your Tax ID must be stored in Braintree's Control Panel
- Corporate and purchasing cards (p-cards) are eligible for Visa transactions
- Any commercial cards are eligible with Mastercard

To ensure that your business and transactions are appropriate for Level 2 or 3 processing, [contact us](/braintree/help) for complete eligibility information.


## Benefits

Providing detailed information about business transactions via Level 2 and 3 data can enable eligible merchants to receive lower interchange rates. These rates are defined by the card brands (Visa and Mastercard).

Transactions that include Level 2 and 3 data are also beneficial to the business making the purchase – the detailed information they receive back makes it easier to track their expenses.


## Settlement and funding timeline

All credit card transactions follow the same settlement and funding timeline, regardless of their level.


## Level 2 data

Level 2 processing requires the capture of specific data in credit card transactions – your tax exempt status, tax amount, and purchase order number must be included. For a complete list of Level 2 data, [see our developer docs](/braintree/docs/reference/general/level-2-and-3-processing/required-fields#level-2-data).


## Level 3 data

Level 3 processing requires the capture of specific line item data in credit card transactions. Certain fields, such as merchant name and address, invoice number, and tax amount must be included – along with line item details such as item description, quantity and unit of measure, freight amount, and commodity and product codes. For a complete list of Level 3 data, [see our developer docs](/braintree/docs/reference/general/level-2-and-3-processing/required-fields#level-3-data).


## Setup

Level 2 and 3 processing requires passing certain data with your transaction API calls. [See our developer docs](/braintree/docs/reference/general/level-2-and-3-processing/overview) for integration setup.

