<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/kount-custom -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Kount Custom
slug: /articles/guides/fraud-tools/premium/kount-custom/
createTime: '2025-04-01T22:44:48.121Z'
updateTime: '2025-04-01T22:44:48.144Z'
---



# Kount Custom


**AVAILABILITY**
 We are no longer offering Kount Custom to new merchants. If you wish to deter fraud with an integrated, enterprise-grade risk management solution, you can refer to our [Fraud Protection Advanced](/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced) product.

 


### Braintree and Kount interaction

It’s important to understand how Braintree and Kount communicate – and how they don’t.

When you create a new transaction, we’ll send the information to Kount and allow a small window of time for Kount to provide their [risk decision](#risk-decisions). Depending on the final decision from Kount, Braintree will either send the transaction to the processor or reject the transaction.


**IMPORTANT**
 Once the window of communication between Kount and Braintree closes, Braintree considers the risk decision finalized and will not re-evaluate the transaction for risk. However, Kount can continue to evaluate transactions beyond that window, which can sometimes cause discrepancies in risk decisions between Braintree and Kount. [See more details below.](#risk-decision-discrepancies)

 


### Risk decisions

The rules you set within your Kount Custom account influence Kount’s risk decisions. These decisions ultimately determine how Braintree will handle each transaction.

| Kount risk decision | Braintree action |
| --- | --- |
| **Approve** | Always sends to the processor |
| **Decline** | Always gateway rejected |
| **Review** | Always sends to the processor |
| **Escalate*** | Always sends to the processor |
| **Not Evaluated** | Sends to the processor by default |

*The Escalate risk decision is treated the same as the Review decision in the Braintree gateway, so while you may see the Escalate decision in your Kount Agent Web Console, it will be reflected as the Review decision in the gateway.

While Braintree's action for each decision can't be changed, you can influence the decisions that Kount makes for certain transactions by using Kount rules and [user defined fields](#user-defined-fields). Your Kount Account Manager can help you determine what rules are best for your business – contact them for guidance.


#### Not Evaluated transactions

A transaction will receive a **Not Evaluated** risk decision when:


- Kount takes too long to deliver a risk decision and the transaction times out
- An error occurs during the evaluation process

You can choose to gateway reject all transactions that are **Not Evaluated** due to a timeout. [Contact us](/braintree/help?issue=AdvancedFraudProtectionQuestion) to configure this setting.


#### Risk decision discrepancies

Because Kount may continue to evaluate each transaction after the window of communication with Braintree has closed, the same transaction may have a different risk decision on the Braintree side versus the Kount side.

If we don't receive a risk decision back from Kount before the window of communication closes, we will list the transaction as **Not Evaluated** in the Braintree gateway. Kount will continue to evaluate the transaction and will display their final decision in your Kount Agent Web Console. Because we do not re-open communication for risk decisions, the transaction will remain listed as **Not Evaluated** even after Kount has made a decision.


### User defined fields

If you’re looking for extra security and reporting, you can create user defined fields (UDFs) in Kount and pass corresponding [custom fields](/braintree/articles/control-panel/custom-fields) to Kount along with your transactions. These UDFs can be used in conjunction with your Kount rules to monitor high risk transactions.

UDFs must have a corresponding custom field in the gateway, or they will not work properly. When setting up your UDF, make sure to:


- Create a UDF in your Kount Agent Web Console
- [Create a custom field via the Braintree Control Panel](/braintree/articles/control-panel/custom-fields#creating-a-custom-field)
- Check theStore and Pass Backoption and give the custom field the exact same name as the UDF, but with one of the following fraud prefixes:
- For text fields, prefix the field name withfraud_
- For numeric fields, prefix the field name withfraud_numeric_
- For date fields, prefix the field name withfraud_date_(note: date UDFs must be formatted MM/DD/YYYY, and dates including timestamps are not supported)





For example, if you create the UDF product_type in Kount, the corresponding custom field in the gateway must read fraud_product_type. For assistance with UDFs, contact your Kount Account Manager.


**NOTE**
 If you’ve processed a transaction and can’t find it in Kount, it’s likely that either there is a UDF that doesn’t have a corresponding custom field in your Braintree gateway, or your corresponding custom field does not have the correct fraud prefix. Make sure your UDFs always have a corresponding custom field in the gateway. If you're unable to resolve this issue, contact your Kount Account Manager for help.

 


#### Payment method UDFs

You may also notice 2 UDFs automatically passed along by Braintree for certain payment methods.

| Name | Description | Values |
| --- | --- | --- |
| PAYMENT_DISPLAY_NAME | A field that represents the payment method the user transacted with. | Apple Pay Card, Credit Card, Google Pay, Masterpass Card, Visa Checkout Card |
| NETWORK_TOKENIZED | Indicates whether the payment method was network tokenized as a DPAN. | 1 = TRUE, 0 = FALSE |


### Getting help

Contact your Kount Account Manager for questions on:


- Transaction scores
- Fraud rules
- Reporting in Kount
- Your Kount Agent Web Console
- Creating UDFs

Contact Braintree for questions on:


- Device data issues
- Creating custom fields to map to Kount’s UDFs
- Any integration issues

