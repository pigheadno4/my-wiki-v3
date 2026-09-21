<!-- Source URL: https://developer.paypal.com/braintree/docs/deprecated/client-side-encryption/javascript-library -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Javascript
slug: /docs/deprecated/client-side-encryption/javascript-library/
createTime: '2025-04-02T01:19:43.151Z'
updateTime: '2025-04-02T01:19:43.168Z'
---



# Javascript


**NOTE**
The integration method outlined below is deprecated. [Learn more about upgrading to the Braintree SDKs.](/braintree/docs/reference/general/upgrade) 


## How it works

Client-Side Encryption allows you to encrypt sensitive payment information for processing by the
Braintree payment gateway. It is designed for use in conjunction with Braintree’s client libraries.
The encryption libraries will take data (usually submitted through a form on a mobile device or
merchant-hosted website) and encrypt it using the public key of an asymmetric key pair. On your
server, you will use our client library to send the encrypted data to the Braintree Gateway. Once
encrypted, the data may only be decrypted using the private key stored on the Braintree gateway.
When encrypted data is transmitted to the Braintree gateway, it is decrypted and processed as usual.
## Which fields to encrypt

You should encrypt any potentially sensitive information related to customer payment methods,
including:
- Credit Card Number
- CVV
- Expiration Date


## Client

Whether the client is an application on a mobile device using iOS/Android, or a web browser, the
client has the following minimum requirements:
- gets user input (typically via a form)
- uses Braintree client side encryption library to encrypt sensitive user input
- forwards encrypted data via HTTPS request to the merchant server.


## Merchant server

The server acts as a middleman between the client application and the Braintree gateway.
- receives encrypted user input from the client application
- forwards encrypted requests to the Braintree gateway via one of the Braintree client libraries.
- returns response information from the gateway to the client application

Encrypted parameters are handled exactly the same as unencrypted parameters in the client libraries.
To see an example of how to pass parameters to the Braintree gateway, see the client library
documentation for the library of your choice:
## create

```language-javascript
var braintree = Braintree.create('your-encryption-key');
```
createinstantiates and returns the Braintree.js object, and takes a single argument
which is the encryption key to use. You can find your encryption key on the front page of our
Control Panel (when logged in).
## onSubmitEncryptForm

```language-javascript
braintree.onSubmitEncryptForm('braintree-payment-form', optionalCallback);
```
onSubmitEncryptFormadds anonSubmithandler to the form specified as its
argument. It accepts an element ID, a jQuery object, or a DOM element. TheonSubmithandler encrypts any field with a data-encrypted-name attribute, then the form
is submitted to the path specified in the form’s action attribute. Optionally,onSubmitEncryptFormcan be passed a function as a second argument. It will call this
function after encrypting the form fields. The most common use case is to submit your payment form
using AJAX. This feature is provided because there is no cross-browser guarantee that multipleonSubmithandlers will be run in the intended order.
## encryptForm

```language-javascript
braintree.encryptForm(formDOMElement);
```
encryptFormis used internally byonSubmitEncryptForm. It can be used if
you’d like to write your ownonSubmitcallback that runs before fields are encrypted –
for example to do client-side validations on the credit card number. It immediately encrypts all
fields with a data-encrypted-name attribute within a form. It accepts an element ID, a jQuery
object, or a DOM element.
## encrypt

```language-javascript
var encryptedValue = braintree.encrypt('sensitiveValue');
```
encryptis used internally byencryptForm. It encrypts a string and
returns the encrypted string. This is provided for backwards compatibility and to allow full
customization of the process.