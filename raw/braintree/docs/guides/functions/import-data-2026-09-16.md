<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/functions/import-data -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Import Data
slug: /docs/guides/functions/import-data/
createTime: '2025-04-01T22:53:37.890Z'
updateTime: '2025-04-01T22:53:37.972Z'
---



# Import Data


**AVAILABILITY**
We're building functions with the same proven expertise and rock solid foundations you expect from Braintree. Take a look at our documentation preview to get a jump start on what you'll make with functions. 

 Email [functions-requests@braintreepayments.com](mailto:functions-requests@braintreepayments.com) to learn more.


## Initialize a New Function


### bash
```bash
$ btfns init MyImportFunction --template=dataImport
```
The CLI will create a new directory,MyImportFunctionwith anindex.jsfile, which you can build off of to create your function.
## Write Code to Ingest Data

To ingest data you will write Javascript code within theindex.jsto accept incoming
requests and create corresponding Braintree entities.
### JavaScript
```js
exports.MyImportFunction = context => {
    const transactionData = JSON.parse(context.payload);

    const transactionAttributes = {
        amount: String(Number(transactionData.orderAmount / 100).toFixed(2)),
        orderId: <a href="http://transactionData.id">transactionData.id</a>,
        status: transactionData.state === "approved" ? braintree.Transaction.Status.Authorized : braintree.Transaction.Status.Declined,
        currencyIsoCode: transactionData.currencyIsoCode,
        billingAddress: transactionData.billingAddress
    };
};
```
Then, make the call and map the result back to Braintree's system.
### JavaScript
```js
... return { transaction: transactionAttributes } ...
```
Your entire function should now look like this:
### JavaScript
```js
exports.MyImportFunction = context => {
    const transactionData = JSON.parse(context.payload);

    const transactionAttributes = {
        amount: String(Number(transactionData.orderAmount / 100).toFixed(2)),
        orderId: <a href="http://transactionData.id">transactionData.id</a>,
        status: transactionData.state === "approved" ? braintree.Transaction.Status.Authorized : braintree.Transaction.Status.Declined,
        currencyIsoCode: transactionData.currencyIsoCode,
        billingAddress: transactionData.billingAddress
    };

    return { transaction: transactionAttributes };
};
```

### Validation Errors

What you return from the function will be validated using our normal validations. If your data does
not conform to our validations we'll return a422witherrorsto the
calling service and log the errors to your console.
## Test and Deploy Your Function


### Testing

Before deploying, it is important to test your function locally. You can use the built-in testing
tool to ensure everything works as expected. You can create an example JSON file that mirrors your
expected inbound payload and the testing tool will provide it to your function alongside the
appropriate metadata.

For example:
### JSON
```json
{
    "orderAmount": 12300,
    "id": "076580eb-fd0d-4c69-be41-f1714f43b8be",
    "state": "authorized",
    "currencyIsoCode": "USD",
    "billingAddress": {}
}
```
And then point to that file when runningtest:
### bash
```bash
$ btfns test -p tests/sample.json
```

### Deployment

When your function is ready, make sure your configuration file is correct.
### yaml
```yaml
{
    `name: "MyImportFunction",
    type: "dataImport",
    events: <ul>
        <li>http: method: "POST"</li>
    </ul>
}
```
Then, run thedeploycommand.
### bash
```bash
{
    `$ btfns deploy <blockquote>
        Success! .... <a href="https://sandbox.btfns.co/076580eb-fd0d-4c69-be41-f1714f43b8be">https://sandbox.btfns.co/076580eb-fd0d-4c69-be41-f1714f43b8be</a>
    </blockquote>`
}
```
By default this will be deployed to your sandbox account, but you can select theproductionoption in the prompt or run:btfns deploy --production.