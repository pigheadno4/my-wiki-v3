<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/package-tracking/client-side -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Client-side configuration
slug: /docs/guides/package-tracking/client-side/
createTime: '2025-04-02T00:05:54.691Z'
updateTime: '2025-04-23T09:03:08.030Z'
---



# Client-side configuration

Here is an example that demonstrates client integration and can be used for any Server integration for creating user approval. 
**NOTE**
If you have already submitted line item information in the Client SDK integration and there have been no changes to it, you can skip line item information in the server integration.   *The code snippet here does not include the entire integration, so to emphasize the change, please refer [our guide](https://developer.paypal.com/braintree/docs/guides/paypal/overview/javascript/v3/).

  
### javascript
```java
  fundingSource: paypal.FUNDING.PAYPAL,
createOrder: function () {
  return paypalCheckoutInstance.createPayment({
    flow: 'checkout', // Required
    amount: 10.00, // Required
    currency: 'USD', // Required, must match the currency passed in with loadPayPalSDK
    intent: 'capture', // Must match the intent passed in with loadPayPalSDK
    enableShippingAddress: true,
    shippingAddressEditable: false,
    shippingAddressOverride: {…},
    lineItems: [{
      quantity: 1,
      unitAmount: 10.00,
      name: "item name",
      kind: "debit",
      upcCode: "012345678912",
      upcType: "UPC-A", //New field
      url: "https://example.com", //New field
      imageUrl: "https://example.com/product1.jpeg", //New field
    }]
  });
},
```
  
### swift
```java
let request = BTPayPalCheckoutRequest(amount: "1.00")
let lineItem = BTPayPalLineItem(quantity: "1", unitAmount: "1", name: "item", kind:.debit)
lineItem.imageURL = URL(string: "http://example/image.jpg")
```
  
### kotlin
```java
val request = PayPalCheckoutRequest(
    amount = "12.34",
    hasUserLocationConsent = true
)

val item = PayPalLineItem(
    kind = PayPalLineItemKind.DEBIT,
    name = "An Item",
    quantity = "1",
    unitAmount = "1",
    imageUrl = "http://example.com/image.jpg",
    upcCode = "upc-code",
    upcType = PayPalLineItemUpcType.UPC_TYPE_2
)

request.lineItems = listOf(item)
```
    [Next Page: Server-side configuration →](/braintree/docs/guides/package-tracking/server-side/java)

