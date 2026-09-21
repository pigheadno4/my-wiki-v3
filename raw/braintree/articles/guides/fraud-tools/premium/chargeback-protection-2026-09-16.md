<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/chargeback-protection -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Chargeback protection tools
slug: /articles/guides/fraud-tools/premium/chargeback-protection/
createTime: '2025-04-01T22:36:50.333Z'
updateTime: '2025-04-01T22:36:50.356Z'
---



# Chargeback protection tools


## Overview

The **Chargeback Protection tool** helps reduce the risk of fraudulent credit and debit card transactions in real-time. If an eligible transaction is not deemed fraudulent or high risk, the payment will be processed with the added insurance that if a chargeback is received, the disputed amount and PayPal **Chargeback fees** will be waived if required evidence is provided by the merchant.

The **Effortless Chargeback Protection tool** expands upon the value of the Chargeback Protection tool by eliminating the requirement to submit delivery confirmation for eligible fraud chargebacks. This tool also helps to reduce operational overhead.

Without the Chargeback Protection tool, merchants processing debit and credit card payments on PayPal are responsible for any transaction risk decision-making and are liable for all associated chargebacks.


### Fraud Evaluation and Chargebacks

With the Chargeback Protection tool, PayPal evaluates and decides the risk for each credit and debit transaction. If a transaction is not deemed fraudulent or high-risk, PayPal will process the payment. If a transaction is considered high-risk, PayPal will decline to process the payment. There is no option to process a payment if PayPal declines the transaction as part of this risk evaluation. All risk decisions happen in real time, with no manual review or later re-review of declined transactions.

When an eligible chargeback is received, you'll receive a notification and be asked to provide proof of delivery or shipment. Evidence requirements may vary based on the types of goods or services you provide. For more information, see the [About Your Account](https://www.paypal.com/us/legalhub/useragreement-full?locale.x=en_US#spp-proof-delivery) section of the PayPal User Agreement.


### Integration

You'll need to pass all mandatory fields as per the Chargeback Protection tools [developer guide](https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/overview). Depending on your business’s risk profile, you may also be required to provide additional data when signing up for the tools.


### Transaction statuses

If PayPal declines a transaction with a Chargeback Protection tool enabled, the merchant cannot override the decision. However, the merchant can bypass the decision using Options.SkipAdvancedFraudChecking. The merchant is required to pay for the services while waiving the right to indemnify PayPal for the chargeback amount and PayPal chargeback fee. All transactions will be displayed on the **Transaction Details Page**.

After any transaction is evaluated by any Chargeback Protection tool, it will be marked under Eligible Fraud Service Provider as “Chargeback Protection tool” or “Effortless Chargeback Protection tool” along with the decision of “Approve, Decline, or any other reason code.”

The transaction qualifies for the chargeback types mentioned in the “Eligible Chargeback Types” section. To view the details of a transaction, follow these steps:


- 1.Log in to your merchant panel.
- 2.Go to the "Transactions" tab. You'll find this at the top of the page.
- 3.Filter the transactions. Use the available options to narrow the list to the transaction you're looking for.
- 4.Select the specific transaction you want to view.
- 5.Check the "Premium Fraud Management Tools Information" section.


### Managing chargebacks

When a chargeback case is created, you will be notified that the case is open and will have the option to submit evidence for that case. Refer Chargeback Protection tools developer guide to pass evidence via Disputes API. Otherwise, you can pass the evidence using the Braintree's Dispute Panel here. You have multiple ways to access and submit evidence for a dispute:

**Method 1: Access dispute from the dispute email**


- **Select the Dispute ID**in the email you received.
- This will take you to the**disputes page.**
- **Select the "Dispute" button**to submit your evidence.
- **Upload the appropriate evidence**as required.
- **Submit the dispute.**BT dispute system will then process your dispute for contestation.

**Method 2: From the merchant panel**


- **Log in to your merchant panel.**
- **Go to the "Disputes" tab.**You'll find this at the top of the page.
- **Select the specific dispute**you want to view in detail.
- **Select the "Dispute" button**to submit your evidence.
- **Upload the appropriate evidence**as required.
- **Submit the dispute.**BT dispute system will then process your dispute for contestation.

**Method 3: Using the Disputes API** as defined in the [developer guide](https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/overview).

The proof of delivery and proof of shipment requirements can be found [here](https://www.paypal.com/us/legalhub/seller-protection?locale.x=en_US#proof-delivery).


### Supported payment technologies

In regions where the Chargeback Protection tool and Effortless Chargeback Protection tool are supported, these tools are compatible with debit and credit card transactions. Braintree should fund these transactions, which implies that Braintree is responsible for money movement from the customer's bank account to the merchant's account.


### Supported processor connections

In regions where the Chargeback Protection tool and Effortless Chargeback Protection tool are supported, these tools are compatible with Braintree's use of Fiserv, American Express and Wells Fargo.


### Eligibility


- Merchants (You) should have a Braintree business account.
- After you enable any Chargeback Protection tools, you won't be able to use Fraud Protection tools unless you disable the Chargeback Protection tool.
- The Chargeback Protection tool is available in the US and Brazil.

