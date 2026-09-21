<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/configuration -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configuration for braintree.setup
slug: /docs/reference/client-reference/javascript/v2/configuration/
createTime: '2025-04-01T22:17:26.883Z'
updateTime: '2025-04-01T22:17:26.930Z'
---



# Configuration for braintree.setup

Braintree.js integrations are created with braintree.setup. 
### JavaScript
```javascript
braintree.setup(authorization, integrationType, options)
```

| Argument | Type | Value |
| --- | --- | --- |
| authorization | string | A string representing your client token or tokenization key |
| integrationType | string | 'dropin'or'custom' |
| options | Object | An options object. See[Setup options](#setup-method-options)for more details. |


## Setup method options

All available options which can be passed to the braintree.setup method, under the options object. These are independent from the options specific to the two supported integration types, Drop-in and Custom.

| Key | Integration | Type | Value |
| --- | --- | --- | --- |
| paypal | any | Object | See[PayPal options](/braintree/docs/reference/client-reference/javascript/v2/paypal#options). |
| dataCollector | any | Object | See[Premium Fraud Management Tools](/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v2). |
| enableCORS | any | boolean | Enabling this allows Braintree.js to use[AJAX with CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)to make requests instead of[JSONP](https://en.wikipedia.org/wiki/JSONP).  If you are using a[Content Security Policy](http://www.html5rocks.com/en/tutorials/security/content-security-policy/), you may need to tweak your directives to allow Braintree.js to communicate from your webpage. See[Using Braintree.js with a Content Security Policy](/braintree/docs/reference/client-reference/javascript/v2/best-practices#using-braintree.js-with-a-content-security-policy). |
| onReady | any | function | This callback is called when the Braintree integration is ready. It is called with one object that represents the integration. It has the following properties:

| `teardown` | Method used to remove this integration. See[Teardown](/braintree/docs/reference/client-reference/javascript/v2/best-practices#teardown)for usage. |
| paypal | Object containing methods to launch and close the PayPal flow. These methods are not available in Drop-in integrations.

| `initAuthFlow` | Opens the PayPal flow. Must be called synchronously as result of a user click event or the PayPal flow popup will automatically be blocked by the browser. Only available in Custom integrations. |
| closeAuthFlow | Closes the PayPal flow. Only available in Custom integrations. | |
| deviceData | A JSON string of device details for use in[fraud detection](/braintree/docs/guides/premium-fraud-management-tools/client-side/javascript/v2). | |
| onPaymentMethodReceived | any | function | This callback is called after the successful tokenization of a payment method.     When subscribed to this callback, we will not add a hidden nonce input to your form nor submit the form automatically. It is up to you to send data to your server as you see fit, usually inside of this callback.     This callback is called with one object that contains information about the received payment method:

| `nonce` | The payment method nonce to send to your server for transactions |
| type | A string representing the type of payment method generated; either'CreditCard'or'PayPalAccount' |
| details | An object representing more details about the payment method.[See details object for more information.](#onpaymentmethodreceived-details-object) | |
| paymentMethodNonceReceived | Drop-in | function | This callback is deprecated in favor ofonPaymentMethodReceived. |
| onError | any | function | Called when an error occurs. This typically happens when you have a configuration error but can also happen when there is a failure in tokenization. The error object provides two keys:

| `type` | A string describing the type of error that occurred (e.g."CONFIGURATION","VALIDATION", or"SERVER"). Not all types are emitted for all integrations. |
| message | A human-readable string describing the error. | |
| container | Drop-in | string | The ID of the container that Drop-in should be placed into. This field is required for Drop-in. |
| id | Custom | string | The ID of the form that Custom should be placed into. This field is required for Custom. |
| hostedFields | Custom | Object | See[Hosted Fields options](/braintree/docs/reference/client-reference/javascript/v2/hosted-fields#options). |
| defaultFirst | Drop-in | boolean | When you specify acustomerIDthat has vaulted payment methods associated with it, Drop-in displays a list of those payment methods and automatically pre-selects the one used most recently. If you passdefaultFirst, Drop-in will instead pre-select the payment method marked as default for the customer. Learn more about marking payment methods as default when[creating a customer](/braintree/docs/reference/request/customer/create#credit_card-options-make_default)or[creating a payment method](/braintree/docs/reference/request/payment-method/create#options-make_default). |


### onPaymentMethodReceiveddetailsobject

When the onPaymentMethodReceived callback is passed as part of the options parameter in braintree.setup, the callback returns a details object. The contents of the details object vary depending on the type of payment method.


#### Credit card

A credit card will return basic information about the card used. This is generally useful when updating your UI to reflect the card type used.

| **Key** | **Type** | **Value** |
| --- | --- | --- |
| `cardType` | `string` | The type of card used. Can be `'Visa'`, `'Mastercard'`, `'Discover'`, `'American Express'`, `'UnionPay'`, or `'JCB'`. |
| `lastTwo` | `string` | The last two digits of the supplied card |


#### PayPal

PayPal responses will contain the following:

| Key | Type | Value |
| --- | --- | --- |
| billingAddress | object | Returns the customer's billing address with the following properties:


- countryCodeAlpha2(String)
- locality(String)
- postalCode(String)
- region(String)
- streetAddress(String)

This option is not available to all merchants. Contact PayPal Support for details on eligibility and enabling this information. |
| email | string | Email address associated with the customer's PayPal account. |
| firstName | string | First name associated with the customer's PayPal account. |
| lastName | string | Last name associated with the customer's PayPal account. |
| payerId | string | Unique ID associated with the customer's PayPal account. |
| phone | string | Phone number associated with the customer's PayPal account. This is only available if the option is[enabled in your PayPal business account](https://developer.paypal.com/docs/admin/checkout-settings/#getting-contact-telephone-numbers). |
| shippingAddress | object | Returns the customer's shipping address along with the following properties:


- countryCodeAlpha2(String)
- locality(String)
- postalCode(String)
- region(String)
- streetAddress(String) |

[Learn more about configuring PayPal.](/braintree/docs/guides/paypal/client-side#basic-configuration)

