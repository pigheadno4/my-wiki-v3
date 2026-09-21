<!-- Source URL: https://developer.paypal.com/braintree/articles/wells-flat/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/wells-flat/transactions/descriptors/
createTime: '2025-04-01T23:13:38.137Z'
updateTime: '2026-06-15T16:54:03.337Z'
---



# Descriptors


**NOTE**
 If you’d like to update your descriptor for PayPal transactions, you can do so from your PayPal console.

 

A descriptor is what your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME 555-123-1234 NM $100.00

There are three types of descriptors:


- **Soft Descriptors**: The descriptor that shows up after a transaction has been authorized. While the charge is in a pending state, the soft descriptor will be displayed on the customer's statement.
- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on the customer’s statement.
- **Dynamic descriptors**: A custom descriptor configured and passed with each transaction via the API.

You are required to provide the following parameters for your descriptor information:


- Merchant name (DBA)
- Merchant state/province
- Customer service phone

We have automatically configured your hard and soft descriptors based on information collected during the application process. You can view and edit your descriptors directly from the Business page in the [Control Panel](https://developer.paypal.com/braintree/help/updateDescriptor). Keep the restrictions below in mind when updating your descriptors.


## Hard and soft descriptor requirements


### Merchant name (DBA)


- Limit of 22 characters
- Can contain letters and numbers but must be all CAPS
- Can contain special characters & . , and space


### Merchant state


- Must be 2 characters all CAPS


### Merchant phone


- Must contain exactly 10 digits
- Can contain dashes


## Dynamic descriptor requirements

Dynamic descriptors are composed of a name, state, and phone number or URL. You do not need to provide the state when using dynamic descriptors; we will pull this information for you.


### Name


- Composed of a business name and product name, separated by an asterisk (*)
- Business name must be either 3, 7, or 12 characters; product descriptor can be up to 18, 14, or 9 characters respectively (with an * in between for a total of 22 characters).
- Can contain special characters – . + -
- Can contain lower and upper case
- Can contain spaces, but can't start with a space

Some examples of valid descriptor names are:


- cmp*order number 
- company*reference num 
- greatcompany*product 


### Phone


- Must contain exactly 10 digits
- Can contain up to 14 characters total, including special characters
- Can contain special characters ( ) -


### URL


- Limit of 13 characters
- Can contain special characters . @

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#descriptor).


**NOTE**
 When issuing a refund, the descriptor will default to the dynamic descriptor that was passed on the original transaction.

 


## American Express descriptors

By default you are able to accept American Express through Braintree’s aggregated Amex account. If you have chosen to use your own Amex account, this information does not apply.

If you are using Braintree’s aggregated Amex account, the following soft descriptor appears on customers' statements while transactions are in a pending status:

DBA: [braintreecharge.com](https://www.braintreepayments.com/charge)    Address: 222 W. Merchandise Mart Plaza, Chicago, IL 60654   Phone: 877-434-2894

Once the transaction has settled, your customers will see your specific hard descriptor information on the top level. Braintree’s information will remain in an expandable text field below your descriptor.

