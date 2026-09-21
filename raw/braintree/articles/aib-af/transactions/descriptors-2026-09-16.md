<!-- Source URL: https://developer.paypal.com/braintree/articles/aib-af/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/aib-af/transactions/descriptors/
createTime: '2025-04-01T23:22:20.536Z'
updateTime: '2025-04-01T23:22:20.556Z'
---



# Descriptors

A descriptor (or clearing name, as it's sometimes referred to) is the identifying information that your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME, LOCATION $100.00

There are three types of descriptors:


- **Soft descriptors**: The descriptor that shows up after a transaction has been authorized. While the charge is in a pending state, the soft descriptor will be displayed on the customer's statement.
- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on their statement.
- **Dynamic descriptors**: A custom descriptor configured and passed with each transaction via the API. This can be helpful if you want to provide specific information about the transaction in your descriptor (e.g. the name of the product).

You are required to provide the following parameters for your descriptor information:


- Merchant name (trading name)
- Clearing city or phone number

We have automatically configured your hard and soft descriptors based on information collected during the application process. [Contact us](/braintree/help/updateDescriptor) to make any changes. Let us know (1) which fields you would like to change and (2) the new desired values for these fields. Keep the restrictions below in mind when sending us your new values.


**NOTE**
 If you would like to update your descriptor for PayPal transactions, you can do so from your PayPal console. If you would like to update your Amex descriptor, you must contact them directly.{" "}

 


## Hard and soft descriptor requirements


### Merchant name (trading name)


- Limit of 22 alphanumeric characters
- Can contain periods, hyphens, and spaces
- Must begin with an alphanumeric character


### Clearing city or phone number


- Limit of 14 alphanumeric characters
- No special characters are supported


## Dynamic descriptor requirements


**NOTE**
 When issuing a refund, the descriptor will default to the dynamic descriptor that was passed on the original transaction.

 

Dynamic descriptors are typically composed of a name and phone number or URL. You do not need to provide a location when using dynamic descriptors; we’ll pull this information automatically based on the location provided during the application process.


### Name


- Must be composed of your DBA business name and then a product name or identifier, separated by an asterisk (*).
- Business name must be either 3, 7, or 12 characters; product descriptor can be up to 18, 14, or 9 characters respectively (with an * in between for a total of 22 characters).
- Can contain special characters . + -
- Can contain lower and upper case
- Can contain spaces, but can't start with a space

Some examples of valid descriptor names are:


- cmp*order number
- company*reference num
- greatcompany*product


### Phone


- Must contain exactly 10 digits
- Can contain up to 14 characters total, including special characters
- Can contain special characters . ( ) -


### URL


- Limit of 13 characters

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#descriptor).

