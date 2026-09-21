<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/credit-cards -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Credit Cards
slug: /docs/reference/client-reference/javascript/v2/credit-cards/
createTime: '2025-04-02T02:08:51.993Z'
updateTime: '2025-04-02T02:08:52.258Z'
---



# Credit Cards


## Credit card direct tokenization


**IMPORTANT**
For a merchant to be eligible for the easiest level of PCI compliance (SAQ A), payment fields can't be hosted on your checkout page. To learn how to implement our hosted solution within a custom integration, [visit the Hosted Fields guide](/braintree/docs/guides/hosted-fields/overview) .


### Tokenize card

If you are doing more complex things with your form, such as your own submit callbacks or custom validation, we recommend using a lower-level integration. To do that, create a Braintree client and use it to tokenize card data:
### JavaScript
```javascript
var client = new braintree.api.Client({
    clientToken: 'TOKEN'
});
client.tokenizeCard({
    number: '4111111111111111',
    expirationDate: '10/20'
}, function (err, nonce) {
    // Send nonce to your server
});
```

**NOTE**
Payment method nonces expire after 3 hours.


### Options

The full set of options available to you inclient.tokenizeCardare:
### JavaScript
```javascript
var client = new braintree.api.Client({
    clientToken: 'CLIENT-TOKEN-FROM-SERVER'
});
client.tokenizeCard({
    number: '4111111111111111',
    cardholderName: 'John Smith',
    // You can use either expirationDate
    expirationDate: '10/20',
    // or expirationMonth and expirationYear
    expirationMonth: '10',
    expirationYear: '2015',
    // CVV if required
    cvv: '832',
    // Address if AVS is on
    billingAddress: {
        postalCode: '94107'
    }
}, function (err, nonce) {
    // Send nonce to your server
});
```

**NOTE**
A nonce will be created even if there are input validation issues like empty fields or invalid input (see [Client-side validation](/braintree/docs/reference/client-reference/javascript/v2/credit-cards/#client-side-validation) ). 

 An error in the form of the string "Unable to tokenize card." will be returned if the tokenizeCard call does not return a nonce. This may happen if the Braintree gateway is unreachable at the time of the call.


### Client-side validation

Integrations such as[Drop-in](/braintree/docs/guides/drop-in/overview/)and[Hosted Fields](/braintree/docs/guides/hosted-fields/overview)handle validation and card type detection out of the box. However, when using a custom credit card integration it is up to you to run client-side validations and present appropriate UI to your users.

While you may use any library you wish to do this, we have built a couple to help you out:


- [Credit Card Type](https://github.com/braintree/credit-card-type)
- [Card Validator](https://github.com/braintree/card-validator)


## 3D Secure UI options


### JavaScript
```javascript
client.verify3DS({
    useDefaultLoader: true, // or false
    onLookupComplete: function () {
        // ...
    },
    onUserClose: function () {
        // ...
    }
});
```

- useDefaultLoaderindicates whether the default loading indicator should be displayed. Default value is`true`.
- onLookupCompleteis invoked after a successful lookup and before the authorization modal is displayed. If using a custom loading indicator, this callback can be used to remove necessary DOM elements.
- onUserCloseis invoked after the authorization modal has been closed from a user initiated action.

