<!-- Source URL: https://developer.paypal.com/braintree/articles/apac/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/apac/transactions/descriptors/
createTime: '2025-04-01T23:30:50.840Z'
updateTime: '2025-04-01T23:30:50.857Z'
---



# Descriptors


**NOTE**
 If you’d like to update your descriptor for PayPal transactions, you can do so from your PayPal console.

 

A descriptor is what your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME 5551231234 HKG $100.00

There are three types of descriptors:


- **Soft Descriptors**: The descriptor that shows up after a transaction has been authorized. While the charge is in a pending state, the soft descriptor will be displayed on the customer's statement.
- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on the customer’s statement.
- **Dynamic descriptors**: A custom descriptor that can be configured by you and passed with each transaction via the API. The dynamic descriptor will replace both the hard and soft descriptors when passed.

You are required to provide the following parameters for your descriptor information:


- Merchant name (DBA)
- Merchant country code
- Customer service phone

We have automatically configured your hard and soft descriptors based on information collected during the application process. [Contact us](/braintree/help/updateDescriptor) to make any changes. Let us know (1) which fields you would like to change and (2) the new desired values for these fields. Keep the restrictions below in mind when sending us your new values.


## Hard and soft descriptor requirements


### Merchant name (DBA)


- Limit of 22 characters
- Can contain letters and numbers but must be all CAPS
- Can contain special characters &amp; . , and space


### Merchant country code


- Must be 3 characters all CAPS: MYS, HKG, SGP


### Customer service phone


- Must be numeric digits
- Special characters are not recommended


## Dynamic descriptor requirements


### Merchant name


- Composed of a business name and product name, separated by an asterisk (*)
- Business name must be either 3, 7, or 12 characters; product descriptor can be up to 18, 14, or 9 characters respectively (with an * in between for a total of 22 characters)
- Can contain special characters – . + -
- Can contain lower and upper case
- Can contain spaces, but can't start with a space

Some examples of valid descriptor names are:


- cmp*order number 
- company*reference num 
- greatcompany*product 


### Merchant country code


- You don’t need to provide this when using dynamic descriptors; we will pull this information for you


### Customer service phone


- Must contain exactly 10 digits
- Can contain up to 14 characters total, including special characters
- Can contain special characters . ( ) -

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#descriptor).


**NOTE**
 When issuing a refund, the descriptor will default to the dynamic descriptor that was passed on the original transaction.

 

