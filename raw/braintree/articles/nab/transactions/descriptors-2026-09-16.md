<!-- Source URL: https://developer.paypal.com/braintree/articles/nab/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/nab/transactions/descriptors/
createTime: '2025-04-01T21:38:14.208Z'
updateTime: '2025-04-01T21:38:14.230Z'
---



# Descriptors

A descriptor is the identifying information that your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

\nMYCOMPANYNAME 0499999999 SYDNEY AU $100.00

Your account supports two types of descriptors:


- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on the customer’s statement.
- **Dynamic descriptors**: A custom descriptor configured by you and passed with each transaction via the API. This can be helpful if you want to provide specific information about the transaction in your descriptor (e.g. the name of the product).

You are required to provide the following parameters for your descriptor information:


- Merchant name (trading name)
- Location
- Phone number or URL (only required when using a dynamic descriptor)

We have automatically configured your hard descriptor based on information collected during the application process.

[Contact us](/braintree/help/updateDescriptor) to make any changes to your descriptors. Let us know (1) which fields you would like to change and (2) the new desired values for these fields. Keep the restrictions below in mind when sending us your new values.


**NOTE**
 If you would like to update your descriptor for PayPal transactions, you can do so from your [PayPal console](https://www.paypal.com/signin/). If you would like to update your Amex descriptor, you must contact them directly.

 


## Hard descriptor requirements


### Merchant name


- Limit of 22 characters
- Can only contain letters, numbers, dashes, and periods
- Must match the registered trading name that was provided to NAB during the application process


### Location


- Limit of 13 alphanumeric characters


### Phone number


- Limit of 13 digits
- Must be an Australian phone number
- Can only contain numbers, dashes, and periods


## Dynamic descriptor requirements


### Merchant name


- Limit of 22 characters
- Can only contain letters, numbers, dashes, and periods
- Must match the registered trading name that was provided to NAB during the application process


### Phone number


- Limit of 13 digits
- Must be an Australian phone number
- Can only contain numbers, dashes, and periods


### URL


- Limit of 13 characters
- Can only contain letters, numbers, dashes, slashes, and periods

Your dynamic descriptor can only show either your phone number **or** URL, so you’ll want to pick whichever works best for you and your business.

You can find more information on how to pass dynamic descriptors for individual transactions in our [developer docs](/braintree/docs/reference/request/transaction/sale/ruby#descriptor).

