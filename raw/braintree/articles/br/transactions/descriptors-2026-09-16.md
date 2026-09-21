<!-- Source URL: https://developer.paypal.com/braintree/articles/br/transactions/descriptors -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Descriptors
slug: /articles/br/transactions/descriptors/
createTime: '2025-04-01T23:53:10.294Z'
updateTime: '2025-04-01T23:53:10.309Z'
---



# Descriptors

A descriptor is the identifying information that your customers will see on their statement when they make a purchase through your mobile app or website. Ultimately, a customer’s bank will determine exactly how your business’s descriptors will appear on customer statements, but they are often formatted like this:

COMPNAME*TXNDESCRIPTOR

This descriptor will show up after a transaction has been authorized and after it has settled. As soon as the customer's bank has finalized the transaction status, the descriptor will be permanently displayed as the description of the charge on their statement.


## Descriptor requirements

The descriptor for your account allows a total of 22 characters.


- The first 8 characters are hardcoded and are common for all transactions. This descriptor is required when setting up your merchant account.
- Anything after the first 8 characters will be prefixed with*. This is required when setting up your merchant account. Only numbers and letters are allowed - no special characters are allowed.
- Following the*, you will have a maximum of 13 characters to specify a descriptor for a merchant account level.

Some examples of valid descriptor names are:


- cmp*wonderfulprod
- gcompany*wonderful prd
- gcompany*product

We will configure your descriptor based on the information collected during the application process. [Contact us](/braintree/help/updateDescriptor) to make any changes. Let us know the new desired values for the descriptor and keep the restrictions above in mind when sending us your new values.

