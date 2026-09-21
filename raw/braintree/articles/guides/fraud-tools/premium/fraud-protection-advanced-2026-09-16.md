<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/fraud-protection-advanced -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Fraud Protection Advanced
slug: /articles/guides/fraud-tools/premium/fraud-protection-advanced/
createTime: '2025-04-02T01:28:50.929Z'
updateTime: '2026-04-21T11:10:58.694Z'
---



# Fraud Protection Advanced

Fraud Protection Advanced is one of our [Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview) that harnesses decades of intelligence from billions of purchases processed by PayPal and Braintree. This feature applies leading-edge machine learning to evaluate card transactions and help protect your business from payment fraud.

Through the capture and analysis of a multitude of data points from customer devices and transactions, Fraud Protection Advanced is built to provide more accurate fraud scores that help merchants identify and reject transactions highly suspected for fraud, while also avoiding over-blocking likely good transactions in the process.


## Features

For our Premium Fraud Management Tools, we provide Fraud Protection Advanced integrations.


## Premium Fraud Management Tools

| Feature | Fraud Protection Advanced |
| --- | --- |
| Risk rules used to detect fraud | Customizable set of rules that you can create and manage |
| Code changes | Minimal |
| Available to | Eligible merchants who are using Braintree Direct and the latest SDKs |
| Risk data | Detailed |
| Additional features | Review transactions and receive webhooks |
| Additional fees | Yes |


## How Fraud Protection Advanced Works

Fraud Protection Advanced is integrated risk management tools designed by PayPal to provide merchants with the ability to make more accurate decisions in real time on card transactions, for the purpose of reducing false positive rejections and minimizing chargebacks.

Fraud Protection Advanced provides additional features and capabilities such as:


- Allowlist/blocklist
- Create your own rules based on 200+ predefined data features provided out of the box
- Create your own rules based on merchant-created custom fields
- Detailed risk information on a transaction
- Review queue
- Receive webhooks when a transaction has been reviewed


### Custom Fields

Fraud Protection Advanced provides several fields that can be used to build conditional filters. However, you may have a specific set of fields pertaining to your business that you want to use in certain scenarios to mitigate fraud. Using Custom Fields, you can add such specific fields to the tool and then use them in building filter conditions.

Using Custom Fields, you can add the following type of fields to the Dashboard:


- **Number fields**: Where the data type of its value is a number (INTEGER, FLOAT). Up to 40 Number fields can be added.
- **String fields**: Where the data type of its value is a string. Up to 40 String fields can be added.
- **Date fields**: Where the data type of its value is a date. Up to 20 Date fields can be added.

To add a field in the Dashboard:


- Click the Fields menu.
- Click the plus icon in the section (for example,**Number Fields**) where you want to add a new field. A row gets added to the section with**Name**and**Description**boxes and the toggle in the**Status**column is enabled (**ACTIVE**) by default.
- In the**Name**box, type the exact name (case sensitive) of the field you want to use from the fields you passed in the payment transaction details.
- For your own reference, in the**Description**box, type a description for the field.
- Click the toggle to disable (**INACTIVE**) the field if you want to enable it later. Added fields are shown in filter conditions only when their status is**ACTIVE**.
- In the**Actions**column, click the check icon to save the field.

The field will also appear in the Control Panel if its status is **ACTIVE**. To see updated custom fields in the Control Panel, refresh that page.

To edit the details of the field:


- On the**Custom Fields**page, find the field you want to edit.
- In the**Actions**column, click the edit icon.
- You can make the changes to field name and description and enable or disable the field.
- After the necessary edits are done, click the check icon to save the edits.

Once you've added custom fields to the Dashboard, you can pass these fields as part of the payment transaction details.


### Review queue

The filters suggested by Fraud Protection Advanced at the time of onboarding are capable of automatically detecting and rejecting fraudulent payments with high precision. However, there may be a few suspicious payments you feel require human judgment to make appropriate decisions on. With Fraud Protection Advanced, you can designate those payments for manual review by creating a filter with the decision label **Review**.

The review process helps you take a second look at the details of suspicious payments and analyze them using expertise in your business to understand whether a payment is fraudulent or legitimate, and then decide what action to take. You can [create webhooks](/braintree/docs/reference/general/webhooks/fraud-protection) to receive notifications when you have approved or rejected a transaction in the review queue.


### Payment methods supported

Fraud Protection Advanced is compatible with all credit and debit cards and the following:


- [Apple Pay](/braintree/articles/guides/payment-methods/apple-pay#fraud-tools)
- [Google Pay](/braintree/articles/guides/payment-methods/google-pay#fraud-tools)
- [Secure Remote Commerce](/braintree/articles/guides/payment-methods/secure-remote-commerce#fraud-tools)


## Risk decisions

When you create a new transaction, we’ll send the information to PayPal’s internal fraud management service. Fraud Protection Advanced will automatically analyze the transaction information using adaptive rules and fraud filters to reach a risk decision. Based on the risk decision, the Braintree gateway will either accept or reject each request.

| Fraud Protection risk decision | Braintree action |
| --- | --- |
| **Approve** | Always sends to the processor |
| **Decline** | Always gateway rejected |
| **Review** | Always sends to the processor |
| **Not Evaluated** | Sends to the processor by default |

By default, Transaction Risk Filter is turned on. This filter is powered by a machine learning model that scores the riskiness of transactions based on historic fraud trends. Transactions with risk scores higher than the score set on this filter will get rejected. A threshold of 1000 denotes the riskiest transaction, and 0 the least risky.

You can check a transaction's Fraud Protection risk decision on the **Transaction Detail** page:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Premium Fraud Management Tools Information**section


### Not Evaluated transactions

A transaction will receive a **Not Evaluated** risk decision when:


- The time it takes to deliver a risk decision exceeds our internal threshold and the transaction times out
- An error occurs during the evaluation process


**NOTE**
 If you're unsure if your Premium Fraud Management Tools are working properly, you can check a transaction by looking at the **Premium Fraud Management Tools Information** section on the **Transaction Detail** page in the Control Panel. If the Device Data Captured field reads **True**, then Premium Fraud Management Tools are functioning.

 

