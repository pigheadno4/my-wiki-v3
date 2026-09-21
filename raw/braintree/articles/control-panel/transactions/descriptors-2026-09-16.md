<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/control-panel/transactions/descriptors/
createTime: '2025-04-01T22:59:29.508Z'
updateTime: '2026-06-15T16:49:44.443Z'
---



# Descriptors

A descriptor is what your customers will see on their bank statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

MYCOMPANYNAME 555-123-1234 NM $100.00

There are three types of descriptors:


- **Soft Descriptors**: The descriptor that shows up after a transaction has been authorized. As long as the charge is in a pending state, the soft descriptor will be displayed on the customer's statement.
- **Hard descriptors**: The descriptor that shows up after a transaction has settled. As soon as the customer's bank has finalized the transaction status, the hard descriptor will be permanently displayed as the description of the charge on the customer’s statement.
- **Dynamic descriptors**: A custom descriptor you configure and pass with each transaction via the API. Some processors only support soft dynamic descriptors, while others support both hard and soft dynamic descriptors.

If you are located in the United States, Europe, or Australia, you can view and edit your account’s descriptors directly from the Business page in your [Control Panel](https://www.braintreegateway.com/login).

If you are located in other regions, please [contact us](https://developer.paypal.com/braintree/help/updateDescriptor) for assistance with descriptor updates.

Descriptor requirements and availability can be found in your bank-specific articles. If you're unsure where to find those, [contact us](https://developer.paypal.com/braintree/help/updateDescriptor).

If you’d like to update your descriptor for PayPal transactions, you can do so from your [PayPal console](https://www.paypal.com/login).

