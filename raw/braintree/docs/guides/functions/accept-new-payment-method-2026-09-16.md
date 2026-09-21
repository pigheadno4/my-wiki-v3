<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/functions/accept-new-payment-method -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Accept a New Payment Method
slug: /docs/guides/functions/accept-new-payment-method/
createTime: '2025-04-02T02:04:46.180Z'
updateTime: '2025-04-02T02:04:46.244Z'
---



# Accept a New Payment Method


**AVAILABILITY**
We're building functions with the same proven expertise and rock solid foundations you expect from Braintree. Take a look at our documentation preview to get a jump start on what you'll make with functions. Email [functions-requests@braintreepayments.com](mailto:functions-requests@braintreepayments.com) to learn more.


## Initialize a New Function


### bash
```bash
$ btfns init MyNewPaymentMethod --template=paymentMethod
```
The CLI will create a new directory,MyNewPaymentMethodwith anauthorization.jsfile, which you can build off of to create your function. By default,
the CLI will also create files for capturing, voiding, refunding, and vaulting.
## Write Code

To authorize a payment you will write Javascript code within theauthorization.jsfile
to communicate with the API for the payment method service. Details from the transaction call will
be shared with the function for use in obtaining the authorization. Create the payload and HTTP
options for your request.
### JavaScript
```js
const fetch = require("node-fetch");

exports.MyNewPaymentMethod = context => {
  const transactionData = JSON.parse(context.payload.transaction);

  const orderBody = {
    purchase_country: transactionData.billing_address.country,
    purchase_currency: transactionData.currencyIsoCode,
    locale: "en-us",
    order_amount: Number(transactionData.amount) * 100,
    order_tax_amount: Number(transactionData.taxAmount) * 100,
    order_lines: transactionData.order_lines,
    billing_address: transactionData.billing_address
  };

  const httpOptions = {
    method: "POST",
    body: JSON.stringify(orderBody),
    headers: {
      "Content-Type": "application/json"
    }
  };
};
```
Execute the request and map the result back to Braintree's system.
### JavaScript
```js
return fetch("https://paymentmethod.service/authorization", options)
  .then(r => r.json())
  .then(result => {
    return {
      statusCode: 200,
      body: JSON.stringify({
        transaction: {
          status: braintree.Transaction.Status.Authorized,
          orderId: result.order_id
        }
      })
    };
  });
```
Your entire function should now look like this:
### JavaScript
```js
const fetch = require("node-fetch");

exports.MyNewPaymentMethod = context => {
  const transactionData = JSON.parse(context.payload.transaction);

  const orderBody = {
    purchase_country: transactionData.billing_address.country,
    purchase_currency: transactionData.currencyIsoCode,
    locale: "en-us",
    order_amount: Number(transactionData.amount) * 100,
    order_tax_amount: Number(transactionData.taxAmount) * 100,
    order_lines: transactionData.order_lines,
    billing_address: transactionData.billing_address
  };

  const httpOptions = {
    method: "POST",
    body: JSON.stringify(orderBody),
    headers: {
      "Content-Type": "application/json"
    }
  };

  return fetch("https://paymentmethod.service/authorization", httpOptions)
    .then(r => r.json())
    .then(result => {
      return {
        statusCode: 200,
        body: JSON.stringify({
          transaction: {
            status: braintree.Transaction.Status.Authorized,
            orderId: result.order_id
          }
        })
      };
    });
};
```

## Test and Deploy Your Function


### Testing

Before deploying, it is important to test your function locally. You can use the built-in testing
tool to ensure everything works as expected.
### bash
```bash
$ btfns test
```
You can also generate a custom mock dataset for use in your own custom testing.
### bash
```bash
$ btfns generate-test-data
```
This will create atestData.jsonfile in the__tests__directory which
will contain an example payload as you can expect from Braintree’s services.
### Deployment

When your function is ready, make sure your configuration file is correct.
### yaml
```yaml
name: "MyNewPaymentMethod"
type: "paymentMethod"
triggers:
  authorization: "authorization.js"
  capture: "capture.js"
  refund: "refund.js"
  void: "void.js"
  vault: "vault.js"
```
Run thedeploycommand.
### bash
```bash
$ btfns deploy
```
By default this will be deployed to your sandbox account, but you can select theproductionoption in the prompt or run:btfns deploy --production.
## Create a Transaction

You can interact with your new function by using the name when creating a new sale.
### JavaScript
```js
gateway.transaction.sale(
  {
    amount: "10.00",
    functionName: "MyNewPaymentMethod",
    customFields: {
      // Provide custom data to your function handler
    }
  },
  function(err, result) {
    if (result.success) {
      // See result.transaction for details
    } else {
      // Handle errors
    }
  }
);
```
Passing thefunctionNamewill automatically call your function at each of triggers
defined in your configuration file. Subsequent calls for this transaction will automatically route
to your function so you do not need to pass any additional information to refund or void the
transaction. If you need to pass additional data to your function that is not available in the
Transaction API, use Custom Fields.
### JavaScript
```js
gateway.transaction.refund(
  "theTransactionId",
  function(err, result) {
  }
);
```
