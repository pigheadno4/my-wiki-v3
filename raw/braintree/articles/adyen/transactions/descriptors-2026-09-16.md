<!-- Source URL: https://developer.paypal.com/braintree/articles/adyen/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/adyen/transactions/descriptors/
createTime: '2025-04-02T01:48:30.298Z'
updateTime: '2025-04-02T01:48:30.416Z'
---



# Descriptors

A descriptor (or clearing name, as it's sometimes referred to) is the identifying information that your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME, CITY LOCATION £100.00

Your account supports two types of descriptors:


- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on their statement.
- **Dynamic descriptors**: A custom descriptor configured and passed with each transaction via the API. This can be helpful if you want to provide specific information about the transaction in your descriptor (e.g. the name of the product).

While the customer’s bank ultimately determines exactly how they will display descriptor information, there are certain parameters that you are required to send and guidelines you need to follow.


## Configuring descriptors

You are required to provide the following parameters for your descriptor information:


- Merchant name (trading name)
- Merchant city

We have automatically configured your hard descriptor based on information collected during the application process. To make any changes, the authorized signer on your account will need to [contact us](/braintree/help/updateDescriptor). Let us know (1) which fields you would like to change and (2) the new desired values for these fields. Keep the [restrictions below](#hard-descriptor-requirements) in mind when sending us your new values.


### Authorized signer

The authorized signer for your Braintree account is the only person who can request access or make changes to sensitive account information, such as transaction details, bank account information, or statement descriptors. This individual and their associated authorized email address were determined during the application process.

Authorized signers are not the same as the Account Admin [user role](/braintree/articles/control-panel/users-roles/managing-users-roles) in the Control Panel, and can't be managed via the Control Panel; to change your authorized signer or add additional signers, [Contact us](/braintree/help/updateBusinessDetails).


**NOTE**
 If an authorized signer calls in to request information about their account, they will need to answer specific security questions to confirm their identity.

 


## Hard descriptor requirements


### Merchant name


- Limit of 20 alphanumeric characters
- Can contain special characters . , - _


### Merchant city

For Braintree merchants, the merchant city field is not limited to identifying your location. If you prefer, you can use this field to provide your customer service phone number or URL instead. This way customers can easily contact you if they have a question about a transaction on their bank statement. The parameters are as follows:


- Limit of 20 alphanumeric characters
- Can contain special characters . , - _


## Dynamic descriptor requirements

You do not need to provide a location when using dynamic descriptors; we’ll pull this information automatically based on the location provided during the application process.

The descriptor name field on each transaction can contain your business name, product name, company URL, and/or phone number and must meet all of the following requirements:


- Limit of 135 alphanumeric characters
- Can contain special characters . , - ? | and space


**IMPORTANT**
 Many banks truncate descriptor names at 22 characters, so keep that in mind while designating your dynamic descriptor name.

 

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#dynamic-descriptors).


### Special note on Amex

If you are processing American Express transactions using Adyen’s aggregated Amex account, dynamic descriptors are not supported. If you have dynamic descriptors enabled, your hard descriptor will be passed by default for Amex transactions.

If you are processing Amex transactions through your own Amex account, you can configure dynamic descriptors directly through them. Contact Amex for assistance.

