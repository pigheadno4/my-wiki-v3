<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/effortless-chargeback-protection -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Effortless Chargeback Protection Tool
slug: /articles/guides/fraud-tools/premium/effortless-chargeback-protection/
createTime: '2025-04-01T22:51:41.092Z'
updateTime: '2025-04-01T22:51:41.114Z'
---



# Effortless Chargeback Protection Tool


### Effortless Chargeback Protection Tool

The Effortless Chargeback Protection tool* expands upon the value of Chargeback Protection tool by eliminating the requirement to submit delivery confirmation for eligible fraud chargebacks. This tool helps to reduce operational overhead and integration complexity by simplifying the types of evidence you need to submit when new fraud chargeback cases are opened. Availability for Effortless Chargeback Protection Tool varies by country.


## Fraud Evaluation and Chargebacks

Just as with the Chargeback Protection tool, when you enable the Effortless Chargeback Protection tool, PayPal provides a risk evaluation and decision on each credit and debit transaction. If a transaction is not deemed fraudulent/high risk, PayPal will process the payment. If a transaction is considered high risk, PayPal will decline to process the payment. There is no option to process a payment if PayPal declines the transaction due to fraud risk. All transactions happen in real time, with no manual review or later re-review of declined transactions.

When the Effortless Chargeback Protection tool is enabled, if a fraud chargeback is received on an eligible transaction, * PayPal will waive the PayPal chargeback fees** and disputed amount without requiring you to submit any evidence. When a product not received chargeback is chargeback is received on an eligible transaction*, PayPal will waive the PayPal chargeback fees** and disputed amount, as long as required evidence is provided. Evidence requirements may vary based on the types of goods or services you provide. For more information see [here](https://www.paypal.com/us/webapps/mpp/ua/seller-protection#proof-delivery).

When an eligible chargeback is received, you’ll receive a notification and be asked to provide [proof of delivery or shipment](https://www.paypal.com/us/webapps/mpp/ua/seller-protection#proof-delivery). Evidence requirements may vary based on the types of goods or services you provide. For more information see [here](https://www.paypal.com/us/webapps/mpp/ua/seller-protection#proof-delivery).


## Required Transaction Data

Your business’s risk profile is based on a number of factors that may include your geographical region, the types of goods or services you sell, or how long your business has been operating. PayPal takes an individualized approach to risk management, and will ask that you provide risk data tailored to your industry using our Set Transaction Context API. For more information about the STC requirements for your business, please contact us.

In addition, PayPal uses device information to evaluate the riskiness of a transaction. Using PayPal’s client-side device data collection tools, you’ll be able to share this information as part of the transaction flow, helping to ensure higher, less risky authorization rates.


## Transaction Statuses

If PayPal declines a transaction with Effortless Chargeback Protection tool enabled, there is no option to override or bypass this decision. Approved transactions will display their protection status in the Premium Fraud Management Tools section of the transaction detail page.


## Managing Chargebacks

When a chargeback case is created, you will be notified that the case is open, and will have the option to submit evidence for that case. All chargebacks will include an indicator called Dispute Protection Level. If the reason code is “Item not received” and the Protection Level is “Effortless Chargeback Protection tool,” simply provide [proof of delivery or shipment](https://www.paypal.com/us/webapps/mpp/ua/seller-protection#proof-delivery) through your API integration or through the Control Panel. If the reason code is “fraud” and the Protection Level is “Effortless Chargeback Protection tool,” you do not need to submit any evidence.

Not all chargebacks are eligible for the Chargeback Protection tool, including, but not limited to, chargebacks with the reason code “Not As Described.” For these cases, the Dispute Protection Level is indicated as “No Protection.” You should respond to these cases according to the guidelines described in [Braintree’s Disputes Guide](https://developer.paypal.com/braintree/docs/guides/disputes/evidence-requirements).

Evidence Requirements by Reason Code:

| Protection Level | Reason | Evidence Required |
| --- | --- | --- |
| Effortless Chargeback Protection tool | Fraud | None |
| Effortless Chargeback Protection tool | Product Not Received | [Delivery Confirmation](https://www.paypal.com/us/webapps/mpp/ua/seller-protection#proof-delivery) |
| No Protection | All other reasons | [See Disputes Guide](https://developer.paypal.com/braintree/docs/guides/disputes/evidence-requirements) |

In some cases, we may contact you after you have submitted evidence to request more information. Be sure to respond to these requests as directed to ensure the chargeback is eligible for the Chargeback Protection tool. Typically, when we request additional evidence, it is because we have encountered a problem with the evidence you submitted. These problems may include:


- The evidence you submitted is for a different chargeback/transaction;
- The evidence you submitted does not contain proof of delivery;
- The evidence you submitted is not legible; or
- The proof of delivery you submitted indicates the product was not delivered.


## Payment methods supported

In regions where Chargeback Protection tool and Effortless Chargeback Protection tool are supported, these tools are compatible with debit and credit card transactions. Other payment methods are not available for the Chargeback Protection tools at this time.

* Terms apply to the Chargeback Protection tool. Certain transactions and chargebacks are not eligible for the Chargeback Protection tool. [See Terms](https://www.braintreepayments.com/legal/payment-services-agreement) for details.   ** You may be assessed additional chargeback fees by acquiring banks and card networks, which will not be waived but will be passed through to you at cost.

