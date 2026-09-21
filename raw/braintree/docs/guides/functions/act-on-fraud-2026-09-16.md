<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/functions/act-on-fraud -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Act on a Fraud Score from a Vendor
slug: /docs/guides/functions/act-on-fraud/
createTime: '2025-04-01T23:59:57.575Z'
updateTime: '2025-04-01T23:59:57.658Z'
---



# Act on a Fraud Score from a Vendor


**AVAILABILITY**
We're building functions with the same proven expertise and rock solid foundations you expect from Braintree. Take a look at our documentation preview to get a jump start on what you'll make with functions. Email [functions-requests@braintreepayments.com](mailto:functions-requests@braintreepayments.com) to learn more.


## Initialize a New Function


### bash
```bash
$ btfns init MyFraudCheck --template=paymentMethod --triggers=beforeAuthorization
```
The CLI will create a new directory,MyFraudCheckwith anbeforeAuthorization.jsfile, which you can build off of to create your function.
## Write Code

To obtain a fraud score you will write Javascript code within theindex.jsfile to
communicate with the API for your fraud service. Details from the transaction call will be shared
with the function for use in obtaining the result. Create the payload and HTTP options for your
request.
### JavaScript
```js
const fetch = require("node-fetch");
exports.MyNewPaymentMethod = context => {
    const transactionData = JSON.parse(context.payload.transaction);
    const scoringBody = {
        sessionId: transactionData.customFields.sessionId,
        amount: Number(transactionData.amount) * 100,
        orderId: transactionData.orderId,
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
return fetch("https://fraud.service/decisions", options)
    .then(r => r.json())
    .then(result => {
        if (result.decision === "YES") {
            return {
                statusCode: 200,
                body: JSON.stringify({
                    transaction: {
                        customFields: {
                            fraudDecision: result.decision
                        }
                    }
                })
            };
        } else {
            return {
                statusCode: 200,
                body: JSON.stringify({
                    transaction: {
                        status: braintree.Transaction.Status.GatewayRejected,
                        customFields: {
                            fraudDecision: result.decision
                        }
                    }
                })
            };
        }
    });
```
Your entire function should now look like this:
### JavaScript
```js
const fetch = require("node-fetch");
exports.MyNewPaymentMethod = context => {
    const transactionData = JSON.parse(context.payload.transaction);
    const scoringBody = {
        sessionId: transactionData.customFields.sessionId,
        amount: Number(transactionData.amount) * 100,
        orderId: transactionData.orderId,
        billing_address: transactionData.billing_address
    };
    const httpOptions = {
        method: "POST",
        body: JSON.stringify(orderBody),
        headers: {
            "Content-Type": "application/json"
        }
    };
    return fetch("https://fraud.service/decisions", options)
        .then(r => r.json())
        .then(result => {
            if (result.decision === "YES") {
                return {
                    statusCode: 200,
                    body: JSON.stringify({
                        transaction: {
                            customFields: {
                                fraudDecision: result.decision
                            }
                        }
                    })
                };
            } else {
                return {
                    statusCode: 200,
                    body: JSON.stringify({
                        transaction: {
                            status: braintree.Transaction.Status.GatewayRejected,
                            customFields: {
                                fraudDecision: result.decision
                            }
                        }
                    })
                };
            }
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
name: "MyFraudCheck"
type: "paymentMethod"
triggers:
beforeAuthorization: "beforeAuthorization.js"
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
gateway.transaction.sale({
    amount: "10.00",
    functionName: "MyFraudCheck",
    customFields: {
        // Provide custom data to your function handler
    }
}, function(err, result) {
    if (result.success) {
        // See result.transaction for details
    } else {
        // Handle errors
    }
});
```
Passing thefunctionNamewill automatically call your function at each of triggers
defined in your configuration file. If you need to pass additional data to your function that is not
available in the Transaction API, use Custom Fields.