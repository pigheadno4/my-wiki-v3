<!-- Source URL: https://developer.paypal.com/braintree/articles/moneris/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/moneris/transactions/descriptors/
createTime: '2025-04-01T23:05:36.676Z'
updateTime: '2025-04-01T23:05:36.691Z'
---



# Descriptors

A descriptor is the identifying information that your customers will see on their bank statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME TORONTO $100.00

Your account supports two types of descriptors:


- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on the customer’s statement.
- **Dynamic descriptors**: A custom descriptor configured by you and passed with each transaction via the API. This can be helpful if you want to provide specific information about the transaction in your descriptor (e.g. the name of the product).

You are required to provide the following parameters for your descriptor information:


- Merchant name (DBA)
- Location
- Phone number*

* Your phone number is not shown in the hard descriptor by default. If you would like your phone number to be included, [contact us](/braintree/help/updateDescriptor) for assistance.


**NOTE**
 Your merchant name/DBA has a limit of 22 characters, and can only include letters, numbers, periods, and dashes.

 

We have automatically configured your hard descriptor based on information collected during the application process.

[Contact us](/braintree/help/updateDescriptor) to make any changes to your descriptors. Let us know (1) which fields you would like to change and (2) the new desired values for these fields. Keep the restrictions outlined in this article in mind when sending us your new values.


**NOTE**
 If you would like to update your descriptor for PayPal transactions, you can do so from your PayPal console. If you would like to update your Amex descriptor, you must contact American Express directly.

 


## Dynamic descriptors

Dynamic descriptors have a total limit of 22 characters and include the following parameters:


- Merchant name (DBA)
- [Dynamic descriptor name](#dynamic-descriptor-name)

Depending on the card issuer, customers’ statements will typically show the dynamic descriptor name appended to your DBA on file, separated by a forward slash (/). While the end result can vary, your customer should see a descriptor formatted similar to this on their statement:

DBA/DYNAMICNAME


### Merchant name (DBA)

The merchant name that appears in your dynamic descriptors will be the official DBA on file for your company. While there is not a limitation on the length of this field specifically, your DBA and the forward slash are included in the overall dynamic descriptor character limit of 22 characters. This means that if you have a longer DBA, the number of characters you have available for your dynamic descriptor name will be more limited.

We recommend that you shorten the DBA name we have on file if you want to show as much of the dynamic descriptor name as possible.


### Dynamic descriptor name

When designating your dynamic descriptor name, keep the following restrictions in mind:


- Can contain lower and upper case alphanumeric characters
- Can't contain spaces or special characters
- Can include a product name and/or business name*

*If your business goes by a recognizable acronym or has another name other than the DBA we have on file, it is helpful to further identify yourself to your customers within this field.


**NOTE**
 If the full length of your dynamic descriptor – including the merchant name (DBA), forward slash, and dynamic descriptor name – exceeds the 22-character limit, it will either be truncated or reverted to your hard descriptor.

 

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#descriptor). Note that you may only use the name field – phone and URL are not supported at this time.

