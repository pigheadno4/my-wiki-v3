<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/offline-transactions -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Offline Transactions
slug: /in-person/guides/offline-transactions/
createTime: '2024-11-20T19:03:53.719Z'
updateTime: '2025-01-03T19:42:38.395Z'
---



# Offline Transactions

Enable payment acceptance even when your internet is offline.


## Introduction

Offline transaction processing, also known as store-and-forward or SAF, allows payment acceptance even when readers are offline and unable to connect to the internet. Transactions are stored on the card reader. Once the reader is able to connect to the internet again, the stored transactions are sent to Braintree for payment processing.

**NOTE**
It is recommended to use Store & Forward starting in firmware version 5.0.0 which has critical improvements to this functionality.


### Merchant Liability

For transactions that occur while in offline mode via SAF the liability for the transaction falls on the merchant. For example, if once the stored offline transaction is forwarded to Braintree for processing and then comes back as declined or refused by the issuer then the merchant will not be funded for the transaction. For this reason, we advise merchants to always think about how to best mitigate this risk.


### Offline Floor Limits

Typically for offline transactions a merchant will want to determine what is the maximum transaction amount they would like to allow for an offline transaction, this is called a "floor limit". From a Braintree perspective, we will allow for any amount to be sent to the reader in an offline session, and for this reason, it is up to the POS system (or API caller application) to create parameters around floor limits and only send the transaction request to the reader if the transaction amount is in line with the set parameters on the POS. Usually, these parameters will vary by merchant and should be configurable to some degree. You may also optionally create other risk mitigating parameters for example "maximum number of transactions to be allowed in a given offline session", or "maximum amount to be allowed in a given offline session", etc...

**NOTE**
When determining what your offline floor limits should be it is advised to consider average transaction value as well as risk tolerance for a potentially declined or refused transaction.


### Initiating an Offline Session

As you will discover once you review the technical documentation below relating to [initiating an offline transaction](/braintree/in-person/guides/offline-transactions/#initiating-an-offline-transaction), you will notice that to initiate the transaction, you must direct your requests to an endpoint on the reader itself as opposed to the cloud Braintree API endpoint. For this reason, the POS (or API caller application) must have a toggle of some sort to tell the POS to "go into offline mode" which would trigger the endpoint switching and put the POS in a state where it should adhere to offline floor limit parameters.


## Getting the Reader set up

In order to transact offline, there are a few prerequisites


- The reader and POS must be on the same local area network


- The reader and POS must have a [static IP address](/braintree/in-person/guides/setup-reader/#configuring-static-ip)



For the POS to securely initiate a transaction on the reader, they must establish a mutually authenticated connection, which will be established via mutual TLS. In order to create this mutually authenticated connection, SSL certificates will need to be generated for both the POS and reader.


### 1) Certificate Generation Overview

Certificate generation can be done via openssl. This guide will work with openssl@1.1.1. Variants other than this, like LibreSSL, etc. may work with this guide but are not guaranteed.

This guide will walk through generating a self-signed root Certificate Authority, and use that root certificate to create signed server (reader) and client (POS) certificates.


### 2) Root Certificate Authority

First, we'll need to generate a private key.

$ openssl genrsa -out ca.key 4096Next, we'll use this key to generate the root certificate.

$ openssl req \ -new -x509 -days 365 \ -key ca.key -out ca.crt \ -nodes -subj "/CN=dev-root-ca"
### 3) Reader and POS Certificates

Now, we can use our root certificate to create the POS and reader certificates. You'll need the reader and POS IP addresses for this next part.

First we will need to create an extensions file that looks like this named v3-extensions.ext

[reader] keyUsage = critical, digitalSignature, keyEncipherment extendedKeyUsage = serverAuth subjectAltName=IP:$READER_IP_ADDRESS authorityKeyIdentifier=keyid,issuer [pos] keyUsage = critical, digitalSignature, keyEncipherment extendedKeyUsage = clientAuth subjectAltName=IP:$POS_IP_ADDRESS authorityKeyIdentifier=keyid,issuerMake sure to substitute the READER_IP_ADDRESS and POS_IP_ADDRESS in the above file with your respective values.

**NOTE**
If you would like to use a shared cert across all of your devices, then you may use a generic domain instead of an IP address for the reader and POS certs, for example: **DNS:$domain_name** instead of **IP:$READER_IP_ADDRESS** and **IP:$POS_IP_ADDRESS**

Next, we will generate the reader's certificate, again substitute the reader IP address.

$ openssl genrsa -out reader.key 4096 $ openssl req \ -new -key reader.key \ -out reader.csr \ -nodes -subj "/CN=$READER_IP_ADDRESS" $ openssl x509 \ -req -days 365 \ -in reader.csr \ -CA ca.crt -CAkey ca.key \ -set_serial 1 \ -out reader.crt \ -extfile v3-extensions.ext -extensions readerFinally, we will generate the POS certificates

$ openssl genrsa -out pos.key 4096 $ openssl req \ -new -key pos.key \ -out pos.csr \ -nodes -subj "/CN=$POS_IP_ADDRESS" $ openssl x509 \ -req -days 365 \ -in pos.csr \ -CA ca.crt -CAkey ca.key \ -set_serial 2 \ -out pos.crt \ -extfile v3-extensions.ext -extensions posAfter this step you should have the following files generated:


- ca.crt


- ca.key


- reader.crt


- reader.csr


- reader.key


- pos.crt


- pos.csr


- pos.key




### 4) Verifying Certificates

Now that we have our certificates generated, there are a few ways we can ensure these will work as expected. One way is to use the openssl  s_client and s_server tools. These will let us test the mutual TLS handshake that occurs between the POS and Reader, and determine if there are any problems.

First, we'll start the "server", or reader:

$ openssl s_server \ -accept 8080 \ -cert reader.crt \ -key reader.key \ -CAfile ca.crtThis starts a server on port 8080, with the reader certificates. Now, let's test our connection like so:

$ openssl s_client \ -connect localhost:8080 \ -cert pos.crt \ -key pos.key \ -CAfile ca.crtIf running the above results in no error outputs, then the certificates are working as expected.


### 5) Getting Certificates onto Readers

In order to use these certificates, the Readers will need to download these certificates from Braintree servers and use them on start-up. In order to accomplish this, the root CA and reader certificate as well as reader private key will need to be sent to Braintree support so that the files can be provisioned for the readers.

In order to do this securely, the certificates will need to be packaged into a PKCS12 container that is password protected like so:

$ openssl pkcs12 -export -out 111-222-333.pfx -inkey reader.key -in reader.crt -certfile ca.crtWhere you see 111-222-333 in the above example is the serial number of the card reader getting the certificate installed.


## Initiating an Offline Transaction

The default port for the reader to accept store and forward transaction requests is 3030. If your reader IP address is then 192.168.0.155, the URL for API requests would be like so:

https://192.168.0.155:3030/graphqlWhen making the API call to this URL, the certificate generated for the POS will need to be sent along with the request so that the reader can verify the POS.

Like online transactions, to provide idempotency on the request charge mutation, you must also include the HTTP header Idempotency-Key with a unique value. UUIDv4 is recommended. For example, if using curl to make the request, you would include

--header 'Idempotency-Key: 94c9ea8b-31b0-488e-a231-57e32f0bfd70'A sample charge GraphQL charge request would look like this:

**NOTE**
Note that there is an additional variable to include in your request called: "deferredAuthorization": true

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestChargeFromInStoreReader($input: RequestChargeFromInStoreReaderInput!) { requestChargeFromInStoreReader(input: $input) { clientMutationId id status } }{ "input": { "clientMutationId": "mutation_id", "readerId": "$YOUR_READER_ID", "transaction": { "amount": "39.85", "orderId": "ExampleOrderNumber-1221", "deferredAuthorization": true } } }{ "data": { "requestChargeFromInStoreReader": { "clientMutationId": "mutation_id", "id": "aW5zdG9yZWNvbnRleHRfI2I5NjNmZmVlYThhMDQ0ZDFiMmI2MGRmNzI1ZTJiNzQwI1ZFUklGT05FLTgwMy00MDYtODI1", "status": "PENDING" } } }**NOTE**
The above example is for a Charge request, you may also perform a [card-present authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/) as an offline transaction

Below is an example of an offline unreferenced refund request. Context ID polling logic should be the same as for a request charge.

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestRefundFromInStoreReader($input: RequestRefundFromInStoreReaderInput!) { requestRefundFromInStoreReader(input: $input) { clientMutationId id status } }{ "input": { "clientMutationId": "your mutation ID", "readerId": "your reader ID", "refund": { "amount": "20.00", "deferredAuthorization": true, "orderId": "Your Order Id" } } }{ "data": { "requestChargeFromInStoreReader": { "clientMutationId": "mutation_id", "id": "aW5zdG9yZWNvbnRleHRfI2I5NjNmZmVlYThhMDQ0ZDFiMmI2MGRmNzI1ZTJiNzQwI1ZFUklGT05FLTgwMy00MDYtODI1", "status": "PENDING" } } }**NOTE**
It is important to note that we support the passing of merchantAccountId as well as customFields and a shopper statement descriptor in your store and forward request. However, there is no validation at the reader level against what is passed. This means that the validation occurs once the stored transactions are forwarded to Braintree and if bad values are passed then the transaction will fail once forwarded and the merchant will not be funded for the transaction.


## Checking the Status of a Charge or Refund

Similar to the [online guide](/braintree/in-person/guides/making-a-transaction/#checking-the-reader-charge-status), the reader can be continuously polled with a query for updates on the transaction's completion status. The difference with an offline transaction is that when you poll the context ID using the reader IP address as an endpoint, you will only get the transaction completion status according to whether the reader has successfully collected card details to store while offline. This DOES NOT represent the final status of the transaction.

To get the final transaction status once stored card data is forwarded, you will need to use the context ID to poll against using the Braintree cloud API endpoint, but there are a few [rules](/braintree/in-person/guides/offline-transactions/#offline-transaction-rules) to keep in mind when building this logic.


### Checking a Charge Status Example:

**NOTE**
As of [firmware version 5.3.0](/braintree/in-person/reference/app-version-release-notes/#version530), we support retrieving bin,brandCode,applicationIdentifier API fields for an offline transaction node query.

GraphQL QuerySample API Responsequery { node(id: {{context_id}}) { ... on RequestChargeInStoreContext { id status transaction { createdAt status amount { value currencyCode } paymentMethodSnapshot { ...on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationIdentifier } } } last4 expirationMonth expirationYear cardholderName bin brandCode } } } } } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfIzE2MjYzNTE5Njk5ODEjVkVSSUZPTkUtODAzLTQyOC0wMzQ", "status": "PROCESSING", "transaction": { "createdAt": "2021-07-15T12:22:02.000000Z", "status": "AUTHORIZED", "amount": { "value": "10.00", "currencyCode": "USD" }, "paymentMethodSnapshot": { "last4": "8885", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "bin": "421212", "brandCode": "VISA" } } } } }
### Checking a Refund Status Example:

GraphQL QuerySample API responsequery ID($transactionId: ID!) { node(id: $transactionId) { ... on RequestRefundInStoreContext { id status refund { createdAt status amount { value currencyCode } orderId paymentMethodSnapshot { ...on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationIdentifier } } } last4 expirationMonth expirationYear cardholderName bin brandCode } } merchantAccountId } } ... on RequestRefundInStoreContext { __typename id status refund { amount { value } createdAt orderId status merchantAccountId } } } }{ "data": { "node": { "id": "aW5zdG9yZWNvbn3NzA4NzU2NDMjVkVSSUZPTkUtODA1LTAxNy00NTQ", "status": "COMPLETE", "refund": { "createdAt": "2022-07-25T17:41:17.05786544+00:00", "status": "AUTHORIZED", "amount": { "value": "20.00", "currencyCode": "USD" }, "orderId": "Your Order Id", "paymentMethodSnapshot": { "last4": "8885", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE/TEST" }, "merchantAccountId": null, "descriptor": { "name": "test person", "phone": null, "url": null }, "customFields": [ { "name": "PayPal", "value": "Test" } ] }, "__typename": "RequestRefundInStoreContext" } } }
## Cancelling a Charge

If you need to stop a transaction from being paid while the reader is activated and requesting payment, you can [cancel](/braintree/graphql/reference/#Mutation--requestCancelFromInStoreReader) the InStoreContext. Cancelling an InStoreContext places the reader back into **idle mode** and returns you to the PayPal-branded screensaver.

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestCancelFromInStoreReader($input: RequestCancelFromInStoreReaderInput!) { requestCancelFromInStoreReader(input: $input) { clientMutationId id status } }{ "input": { "inStoreContextId": "context-id" } }{ "data": { "requestCancelFromInStoreReader": { "clientMutationId": null, "inStoreContext": { "id": "aW5zdG9yZWNvbnRleHRfI2M4M2MzYTM5NDVhMDRlNTI4MmQ3NDcxZDIxNDY5MzFlI1ZFUklGT05FLTgwMy0zOTEtMjM2I3VzLXdlc3QtMg", "status": "CANCELLED", } } } }
## Offline Transaction Rules

This section outlines the logical rules to keep in mind as you build your offline processing flow.


- The reader can store offline transactions in its memory for **up to 5 days**, after which the stored transactions will be erased. This has to do with card scheme rules for token management.


- The reader will attempt to reconnect to the network every few seconds when its in an offline state, and once reconnected it will automatically upload all stored transactions to the Braintree Platform.


- Once a stored offline transaction is successfully uploaded to the Braintree Platform, the context ID of that transaction will be **available for query for 24 hours**, after which it will be erased. See [offline transaction reconciliation](/braintree/in-person/guides/offline-transactions/#offline-transaction-reconciliation).


- A single reader can store up to approximately 1,000 transactions in a given offline session without uploading to the Braintree Platform.


- All **API inputs must be correct** for offline transactions, otherwise the context will stay in a "PROCESSING" status until the context expires after 7 days.




## Offline Transaction Reconciliation

It is important to reconcile your offline transactions every day to ensure that the final transaction status (once forwarded) is known by the POS. This helps to ensure that your POS remains in sync with the actual transaction status given by the card issuer. To do this you will need to use the context ID from the offline transaction and poll against it using the Braintree Cloud API endpoint. This should be done for every offline transaction **at least once per day** since the **context ID will expire 24 hours** after the stored transaction data is uploaded to the Braintree Platform. When you get the API response from your context ID polling make sure to store the transaction ID and the transaction status in your POS database.

**NOTE**
Braintree Sandbox Cloud API Endpoint: [https://payments.sandbox.braintree-api.com/graphql](https://payments.sandbox.braintree-api.com/graphql)

It is also important to note that if you use a unique orderId reference, you can also query the Braintree platform using the orderId to get the transaction results and other transaction details. The orderId does not expire.

You may want to build your own retry logic to handle an offline transaction being declined once forwarded. To do this, you can request to [vault a payment method](/braintree/in-person/guides/vaulting-and-customers/#vaulting-a-card-with-a-transaction) during your offline charge request. This will allow you to retrieve the [paymentMethodId](/braintree/graphql/reference/#Object--PaymentMethod) token after the transaction is forwarded. You may perform a subsequent card-not-present [authorization](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) or [charge](/braintree/graphql/reference/#Mutation--chargePaymentMethod) against this token to recover funds for the offline transaction originally declined.

**NOTE**
The ability to vault a payment method with a charge during an offline transaction was added in [firmware version 5.1.0](/braintree/in-person/reference/app-version-release-notes/#version510).


## Which API calls are supported Offline?

While we are continuously adding functionality to our offline processing offering, there are a limited number of reader interactions that are supported in an offline state. See below for the full list:


- [Initiate a charge](/braintree/in-person/guides/offline-transactions/#initiating-an-offline-transaction)


- [Initiate an authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/)


- Initiate a refund


- [Request text display](/braintree/in-person/guides/display-information/#request-text-display)


- [Request line item display](/braintree/in-person/guides/display-information/#request-line-item-display)


- [Receipt Printing API](/braintree/in-person/guides/receipt-printing-api/)



**NOTE**
Note that for these flows to work offline, your requests must be sent to the API endpoint on the reader (IP address : port /graphql) as shown [here](/braintree/in-person/guides/offline-transactions/#initiating-an-offline-transaction)

[GraphQL Error Handling](/braintree/in-person/guides/graphql-error-handling/)[Additional API Calls](/braintree/in-person/guides/additional-api-calls/)