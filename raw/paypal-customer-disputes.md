<!-- Source URL: https://developer.paypal.com/docs/disputes/ -->
<!-- Fetched: 2026-04-16 -->

---
title: Customer disputes
slug: /docs/disputes/
createTime: '2024-05-13T18:25:48.283Z'
updateTime: '2025-05-08T15:42:12.128Z'
---


# Customer disputes


**info**
Not a developer? Manage disputes directly in the PayPal Resolution Center. [Get Started](https://www.paypal.com/disputes/)


A dispute occurs when:

- A customer has not received goods or services.
- The received goods or services are not as described.
- The customer needs more details, such as a copy of the transaction or a receipt.



## How it works 
A customer can file a case with PayPal through the Resolution Center to dispute the charge or ask their bank or credit card company to reverse it.

A charge reversal is also known as a chargeback.


### Disputes in the PayPal Resolution Center
- The customer files a dispute directly with the seller or on PayPal's Resolution Center.
- The seller reviews the dispute and provides additional information.
- The customer is refunded if the dispute is settled in the customer's favor.


![disputes-flow-marketplace.svg](assets/paypal-disputes-flow-marketplace.svg)


## Disputes through the bank or card issuer 
- The customer files a dispute with the bank or card issuer.
- The dispute is created in PayPal.
- The seller reviews the dispute and provides additional information.
- The customer is refunded if the dispute is settled in the customer's favor.


![disputes-flow-bank.svg](assets/paypal-disputes-flow-bank.svg)


## Customer workflow 
In the Resolution Center, the customer selects the dispute from the following options:

- I didn't receive an item I purchased
- I received an item that's not as described
- I want to report unauthorized activity
- I have a billing issue

A dispute is created, and the Resolution Center prompts the customer to contact the seller about the problem.



## Actions available with the Disputes API 
You can also use the Disputes API to automate actions in the Resolution Center.

The following table shows the methods available as actions in the Resolution Center.

| Method | Resolution Center Actions |
| --- | --- |
| [List disputes](https://developer.paypal.com/docs/disputes/integration-guide/#list-disputes) | - Go to **Case summary** .
- Select **Open Cases** . |
| [Show dispute details](https://developer.paypal.com/docs/disputes/integration-guide/#show-dispute-details) | Under**Case ID**, select **+** to show the transaction ID, date opened, and other details. |
| [Send message to other party](https://developer.paypal.com/docs/disputes/integration-guide/#send-message-to-other-party) | - On the case summary page, click **View** .
- Select **Message** , enter the message details, and click **Send** . |
| [Make an offer to resolve a dispute](https://developer.paypal.com/docs/disputes/integration-guide/#make-offer-to-resolve-dispute) | - On the case summary page, click **View** .
- Select **Make an offer** .
- Select which offer to make: Full refund offer with item return, Partial refund offer, Replacement offer. |
| [Escalate dispute to a claim](https://developer.paypal.com/docs/disputes/integration-guide/#escalate-dispute-to-claim) | On the**Escalate to PayPal**page, enter the detailed description, and select**Send**. |
| [Provide evidence](/docs/disputes/integration-guide/#provide-evidence) | - Click **Enter tracking information and order status** .
- Enter the information and click **Submit** .

You can provide more evidence by uploading files. |
| [Accept claim](/docs/disputes/integration-guide/#accept-claim) | To accept the claim, select**I'll issue a refund to my customer and close this case**. |
| [Appeal dispute](/docs/disputes/integration-guide/#appeal-dispute) | To appeal the dispute, select**I disagree with the claim. I'd like to submit additional info**. |



## Eligibility 
Review the supported [countries](/reference/currency-codes/) and [currencies](/reference/currency-codes/) .



## Dispute use cases 
You can use the Disputes API to:

- Automate handling large volumes of disputes.
- Manage PayPal disputes from your internal dispute management tool instead of the PayPal Resolution Center.
- Show open PayPal disputes to sellers in a shopping cart without providing management of the disputes.



## How do you want to integrate? 

### Use the Disputes API
Enable Disputes and use the API actions


### Use the Resolution Center
Manually manage disputes
