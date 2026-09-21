<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/passing-lodging-data -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Passing Lodging Data
slug: /in-person/guides/making-a-transaction/passing-lodging-data/
createTime: '2024-11-20T19:03:02.299Z'
updateTime: '2025-01-03T19:13:38.843Z'
---



# Passing Lodging Data

This page will cover the passing of lodging data for card present transactions in both Auth and Charge requests. This is primarily for the Hotels & Hospitality industry.


## Feature Overview

If you are a Hotel or another eligible merchant type, it may be beneficial to provide specific lodging data in your Auth and Charge transaction requests to Braintree. This may help you achieve lower interchange fees levied by the card networks. We allow for the passing of this data, and the rest of this documentation article will discuss this feature.


#### Eligible MCC codes for passing Lodging Data:


- 7011



Merchants not under one of the above MCC codes would not be eligible to pass lodging data to Braintree.


## Passing Lodging Data

You may pass lodging data in both the [requestAuthorize](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/) and [requestCharge](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging) mutations as well as a [captureTransaction](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#capturing-funds-against-an-authorization) request. The example below will depict using a [requestAuthorize](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/) mutation.

**NOTE**
For this feature to work, the Braintree gateway must be enabled to pass lodging data fields. Please work with your Solutions Engineer or Integration Engineer to get this enabled on your account.

**NOTE**
More information on passing lodging data to Braintree can be found in the Braintree [GraphQL API documentation](/braintree/graphql/reference/#Input--IndustryLodgingInput).

GraphQL API MutationGraphQL API Variablesmutation RequestAuthorizeFromInStoreReader($input: RequestAuthorizeFromInStoreReaderInput!) { requestAuthorizeFromInStoreReader(input: $input) { clientMutationId inStoreContext { id status transaction { id orderId status customer{ id } paymentMethodSnapshot{ __typename ... on CreditCardDetails { brandCode bin last4 cardholderName expirationMonth expirationYear } } } reader { id name status softwareVersion } } } }{ "input": { "readerId": "Your reader ID", "clientMutationId": "your client mutation ID", "transaction": { "amount": "150", "orderId": "your order ID", "merchantAccountId": "your merchant account ID", "industry": { "lodging": { "folioNumber": "12345", "checkInDate": "2024-01-24", "checkOutDate": "2024-01-29", "roomRate": "100", "roomTax": "10", "noShow": "false", "advancedDeposit": "false", "fireSafe": "true", "propertyPhone":"(510)-123-1234", "additionalCharges" : [{ "kind": "MINI_BAR", "amount": "5" }, { "kind": "RESTAURANT", "amount": "5" }, { "kind": "GIFT_SHOP", "amount": "2" }, { "kind": "LAUNDRY", "amount": "1" }, { "kind": "TELEPHONE", "amount": "1" }, { "kind": "OTHER", "amount": "5" }] } } } } }
## Viewing Lodging Data in the control panel

The lodging data, once passed to Braintree, is sent onto the card networks so that the merchant benefits from lower interchange rates. It is also possible to view the lodging data that was passed by looking up your transaction in the Braintree control panel on the Transaction Details Page under the section "Industry Specific Data".


## Important Tips for passing Lodging Data


- The passing of lodging data is **NOT supported** for [offline transactions](/braintree/in-person/guides/offline-transactions/), and if these API fields are passed for an offline transaction, it will result in an API error.


- We support the passing of lodging data when using the [Request Authorize](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/) or [Request Charge](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging) API mutations; however, you may also pass this data when you send a [separate capture](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#capturing-funds-against-an-authorization) request against an authorization.



[Level 2 and Level 3 Data Processing](/braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing/)[Vaulting and Customers](/braintree/in-person/guides/vaulting-and-customers/)