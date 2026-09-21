<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/email-receipts -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Email Receipts
slug: /articles/control-panel/transactions/email-receipts/
createTime: '2025-04-02T00:59:09.531Z'
updateTime: '2026-01-20T15:03:08.293Z'
---



# Email Receipts


**NOTE**
 For information about how to alert customers when subscription payments fail, [see our article on email notifications](/braintree/articles/guides/recurring-billing/email-notifications) instead.

 

Your Braintree gateway can be configured to send email receipts to your customers for every transaction or refund that you successfully submit for settlement.

To use this feature, you must:


- [Enable email receipts in the Control Panel](#enabling-email-receipts)
- Include an email address in the customer information for all transactions created – both in the Control Panel or via the API

Braintree's email receipts can include a line of custom text, but can't otherwise be altered. If you want to customize the delivery or content of your receipts, it’s best to create and [send your own](#sending-your-own-email-receipts).


## PayPal email receipts

PayPal sends receipts to its customers for PayPal transactions by default. If you are using Braintree’s email receipts, PayPal customers will receive two receipts: one from Braintree and one from PayPal.


## Enabling email receipts

Have the authorized signer on your account contact Support to request activation of this feature. After receiving confirmation from Support, enable email receipts in the Control Panel:


- Log into the[Control Panel](https://www.braintreegateway.com/login)
- Click on the gear icon in the top right corner
- Click**Processing**from the drop-down menu
- Scroll to the**Transactions**section
- Next to**Email Receipts**, click the**Options**link
- Check the box next to**Enabled**
- [Configure your settings](#configuration-options)
- Click the**Save**button


### Configuration options

On the Edit Receipt Options page where you enabled this feature, you can also personalize the email receipts for your business:


- **Send Receipt by Default?**: With this box checked, receipts will be sent to customers for every successful transaction


**IMPORTANT**
 If you choose to enable this option, you will need to either specify an email address when creating each transaction or ensure each customer in your Vault has an associated email address. Transactions submitted for customers that do not have an email address will trigger a validation error.

 


- **Sender Email Address**: All transaction receipt emails will be sent from[no-reply@braintreegateway.com](mailto:no-reply@braintreegateway.com).
- **Reply To**: This is the email your customers will use if they need to contact you after their purchase.
- **BCC**: This allows you to send copies of all receipts to yourself (e.g.[receipt-archive@mydomain.com](mailto:receipt-archive@mydomain.com)); this email address will not be visible to customers.
- **Email Text**: Custom plain text that will appear at the top of every receipt, limited to a maximum of 1000 characters.


**NOTE**
 The **Email text** field does not support HTML markup and must be written as plain text. If you want to send fully customized email receipts, you'll need to [create and send your own](#sending-your-own-email-receipts).

 


#### Authorized signer

The authorized signer for your Braintree account is the only person who can request access or make changes to sensitive account information, such as transaction details, bank account information, or statement descriptors. This individual and their associated authorized email address were determined during the application process.

Authorized signers are not the same as the Account Admin [user role](/braintree/articles/control-panel/users-roles/managing-users-roles) in the Control Panel, and can't be managed via the Control Panel; to change your authorized signer or add additional signers, [Contact us](/braintree/help/updateBusinessDetails).


**NOTE**
 If an authorized signer calls in to request information about their account, they will need to answer specific security questions to confirm their identity.

 


## Sample email receipt

All possible transaction fields are shown in the sample below. If you are not utilizing some of these fields (e.g. Order ID), they will not appear on your customers’ receipts. Custom fields will not appear on receipts, either.

![email,receipt](https://www.paypalobjects.com/btdevdoc/braintree/img/articles/email-receipt.png)


## Sending an email receipt manually

If you need to manually generate a receipt for a transaction, you can do so on the **Transaction Details** page. You'll find a **Receipt** button at the top of that page.

If you collected the customer's email address during the transaction, the address will populate automatically.


## Sending your own email receipts

In order to send your own custom email receipts, you’ll need to work with your developers to set up custom logic on your end.

To generate a useful receipt, you’ll need to [retrieve the transaction details from the result object](/braintree/docs/reference/response/transaction#result-object) via the API. For recurring billing transactions, you’ll need to [search for the transaction details](/braintree/docs/reference/request/transaction/search). Once you have this information, use your custom logic to generate and distribute the receipt.


**IMPORTANT**
 If you create your own custom receipts, you should never display the card's expiration date or any more than the last 5 digits of the credit card number.

 

