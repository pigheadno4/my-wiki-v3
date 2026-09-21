<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/fraud-protection -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Fraud Protection
slug: /articles/guides/fraud-tools/premium/fraud-protection/
createTime: '2025-04-01T23:32:16.732Z'
updateTime: '2025-04-01T23:32:16.749Z'
---



# Fraud Protection

Fraud Protection is one of our [Premium Fraud Management Tools](/braintree/articles/guides/fraud-tools/premium/overview) that harnesses decades of intelligence from billions of purchases processed by PayPal and Braintree. This feature applies leading-edge machine learning to evaluate card transactions and help protect your business from payment fraud.

Through the capture and analysis of a multitude of data points from customer devices and transactions, Fraud Protection is built to provide more accurate fraud scores that help merchants identify and reject transactions highly suspected for fraud, while also avoiding over-blocking likely good transactions in the process.

With Fraud Protection merchants will have the visibility and control to see and tune their fraud filters via a new Fraud Protection merchant interface.


## Risk decisions

When you create a new transaction, we’ll send the information to PayPal’s internal Fraud Protection service. Fraud Protection will automatically analyze the transaction information using adaptive rules and fraud filters to reach a risk decision. Based on the risk decision, the Braintree gateway will either accept or reject each request.

| Fraud Protection risk decision | Braintree action |
| --- | --- |
| **Approve** | Always sends to the processor |
| **Decline** | Always gateway rejected |

By default, Transaction Risk Filter is turned on. This filter is powered by a machine learning model that scores the riskiness of transactions based on historic fraud trends. Transactions with risk scores higher than the score set on this filter will get rejected. A threshold of 1000 denotes the riskiest transaction, and 0 the least risky.

You can check a transaction's Fraud Protection risk decision on the **Transaction Detail** page:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on**Transactions**in the navigation bar
- Scroll to the**Transaction Search**section
- Define your desired parameters and click the**Search**button
- Click on the desired transaction**ID**link
- Scroll to the**Premium Fraud Management Tools Information**section


**NOTE**
 If you're unsure if your Premium Fraud Management Tools are working properly, you can check a transaction by looking at the **Premium Fraud Management Tools Information** section on the **Transaction Detail** page in the Control Panel. If the Device Data Captured field reads **True**, then Premium Fraud Management Tools are functioning.

 

