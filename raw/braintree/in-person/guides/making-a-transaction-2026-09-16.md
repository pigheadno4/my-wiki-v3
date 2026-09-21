<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/making-a-transaction -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Initiate a Sale or Refund
slug: /in-person/guides/making-a-transaction/
createTime: '2024-11-20T19:04:37.405Z'
updateTime: '2025-01-21T10:25:09.143Z'
---



# Initiate a Sale or Refund

This article covers both sale and refund transactions


## Initializing the Reader for Charging

When you're ready to charge a customer, you should create an In-Store Context by [requesting a charge from a card reader](/braintree/graphql/reference/#Mutation--requestChargeFromInStoreReader). In this step, your application will specify, at minimum, the readerId, merchantAccountId and transaction.amount details to initialize the reader for payment acceptance. Note that the merchantAccountId is not validated against in the Sandbox environment; however, this is a required value in the production environment for all interactions with the card reader.

Charging is similar to authorizing, except that if the authorization is successful, Braintree will automatically capture the transaction. This is also known as [creating a Sale Transaction](/braintree/docs/reference/request/transaction/sale/).

To provide idempotency on the request charge mutation, you must also include the HTTP header Idempotency-Key with a unique value. UUIDv4 is recommended. For example, if using curl to make the request, you would include

**NOTE**
Using Idempotency-Key is an important way of preventing duplicate charges to your customer in the event of an API communication failure. For example, if you request a charge from the reader, the customer completes the charge on the reader, but for some reason, the POS does not get back the transaction result before timing out. In this scenario, the POS could recover the original transaction using the same Idempotency-Key without accidentally creating a duplicate charge.

--header 'Idempotency-Key: 94c9ea8b-31b0-488e-a231-57e32f0bfd70'GraphQL MutationGraphQL VariablesSample API Responsemutation RequestChargeFromInStoreReader($input: RequestChargeFromInStoreReaderInput!) { requestChargeFromInStoreReader(input: $input) { clientMutationId id status reader { id name status } } }{ "input": { "readerId": "your reader ID here", "transaction": { "amount": "39.85", "orderId": "ExampleOrderNumber-1221", "merchantAccountId": "ExampleLocation_2005" } } }{ "data": { "requestChargeFromInStoreReader": { "clientMutationId": "abc123sdfsdf", "id": "aW5zdG9yZWNvbnRleHRfIzRjNjQzNGMwNmM5MDQ3OWNhNjFiYWMwYWE5MDFlM2M3I1ZFUklGT05FLTgwMy00MTQtNjkzI3VzLWVhc3QtMQ", "status": "PENDING", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" } } }, "extensions": { "requestId": "d86bfaf0-2e25-4ff5-984c-9d4bd8b574ee" } }![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20Sale:Tap%20to%20pay.jpeg)
## Checking the Reader Charge Status

After the reader is initialized for payment, your application must wait for the customer to interact with it (i.e. insert a test card) and for the payment attempt to be processed. Your application should use [the node query](/braintree/graphql/reference/#Query--node) to poll on a 2-second interval between responses for the current status of the payment using the RequestChargeInStoreContext.id received at charge initialization and monitor the RequestChargeInStoreContext.status field as the transaction goes through the lifecycle.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20Sale:Checking%20the%20reader%20charge%20status.png)When the RequestChargeInStoreContext.status changes to "COMPLETE", you will also receive a transaction object RequestChargeInStoreContext.transaction in the response. Save the completed RequestChargeInStoreContext.transaction.id in your database for referencing the transaction in subsequent operations.

All successful test transactions should have a transaction amount value below $2,000 for testing. For more info on using amounts to simulate various transaction outcomes, look at [Testing Your Integration](/braintree/in-person/guides/testing-your-integration/).

[**Testing the Unhappy Paths in Sandbox**](/braintree/in-person/guides/testing-your-integration/) **:**

** **

GraphQL QueryPENDING ResponseCOMPLETE ResponseFAILED Response : DeclineFAILED Response : Network ErrorFAILED Response: Gateway Reject{ node(id: "{{last_braintree_instore_context}}") { ... on RequestChargeInStoreContext { id status statusReason reader { id name status } transaction { id orderId status statusHistory { ... on PaymentStatusEvent { status timestamp terminal ... on AuthorizedEvent { processorResponse { authorizationId emvData message legacyCode retrievalReferenceNumber } } ... on GatewayRejectedEvent { gatewayRejectionReason } ... on FailedEvent { processorResponse { retrievalReferenceNumber emvData message legacyCode } networkResponse { message code } } ... on ProcessorDeclinedEvent { processorResponse { legacyCode message authorizationId additionalInformation retrievalReferenceNumber emvData } declineType networkResponse { code message } } } } merchantAddress { company streetAddress addressLine1 extendedAddress addressLine2 locality adminArea2 region adminArea1 postalCode countryCode phoneNumber } amount { value currencyIsoCode } merchantAccountId merchantName createdAt channel customFields { name value } paymentMethodSnapshot { ... on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationPreferredName applicationIdentifier terminalId inputMode pinVerified } } } brandCode last4 bin expirationMonth expirationYear cardholderName binData { issuingBank countryOfIssuance prepaid healthcare debit commercial } } } } } } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfIzY3MzhkNmIzOGFjNzRiOGVhYzZkMTY4NTc4MjNlOTVlI1ZFUklGT05FLTgwMy00MTQtNjkzI3VzLWVhc3QtMQ", "status": "PENDING", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "transaction": null } }, "extensions": { "requestId": "8214a538-c1b5-44f6-ae2c-a14a180d9678" } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfIzAzNjcyNTVjNDc3NzRhNjc4YWRlMThiY2Y0NWZmZTU5I1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "transaction": { "id": "dHJhbnNhY3Rpb25fOWh5cmtiZmg", "orderId": "ExampleOrderNumber-12", "status": "SUBMITTED_FOR_SETTLEMENT", "statusHistory": [ { "status": "SUBMITTED_FOR_SETTLEMENT", "timestamp": "2021-12-14T20:08:57.000000Z", "terminal": false }, { "status": "AUTHORIZED", "timestamp": "2021-12-14T20:08:57.000000Z", "terminal": false, "processorResponse": { "authorizationId": "8P3FVW", "emvData": "9F240512345678908A023030", "message": "Approved", "legacyCode": "1000", "retrievalReferenceNumber": "1234567" } } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "1999.00", "currencyIsoCode": "USD" }, "merchantAccountId": "paypal", "merchantName": "DESCRIPTORNAME", "createdAt": "2021-12-14T20:08:56.000000Z", "channel": null, "customFields": null, "paymentMethodSnapshot": { "origin": { "details": { "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalId": "975af200", "inputMode": "CONTACTLESS", "pinVerified": false } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "220078d6-bae4-4902-a614-e3c28addf13d" } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfI2Y1ZTJmOGZkMzI1OTQ2MzY5OGVmNTQ1N2Q0YmZlZjY0I1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "FAILED", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "transaction": { "id": "dHJhbnNhY3Rpb25fZjMzZ3piM3g", "orderId": "ExampleOrderNumber-12", "status": "PROCESSOR_DECLINED", "statusHistory": [ { "status": "PROCESSOR_DECLINED", "timestamp": "2021-12-14T20:11:35.000000Z", "terminal": true, "processorResponse": { "legacyCode": "2999", "message": "Processor Declined", "authorizationId": null, "additionalInformation": "2999 : ", "retrievalReferenceNumber": "1234567", "emvData": "9F240512345678908A023035" }, "declineType": null, "networkResponse": { "code": "XX", "message": "sample network response text" } } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "2999.00", "currencyIsoCode": "USD" }, "merchantAccountId": "paypal", "merchantName": "DESCRIPTORNAME", "createdAt": "2021-12-14T20:11:35.000000Z", "channel": null, "customFields": null, "paymentMethodSnapshot": { "origin": { "details": { "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalId": "975af200", "inputMode": "CONTACTLESS", "pinVerified": false } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "402b24bd-ee8e-445f-886e-c34080e43540" } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfI2QwY2RiMDg0NDUzODRlZTNhMjZkZjRhZDliY2YwMjRjI1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "FAILED", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "transaction": { "id": "dHJhbnNhY3Rpb25fcHQ3emRyYjg", "orderId": "ExampleOrderNumber-12", "status": "FAILED", "statusHistory": [ { "status": "FAILED", "timestamp": "2021-12-14T20:13:40.000000Z", "terminal": true, "processorResponse": { "retrievalReferenceNumber": "1234567", "emvData": null, "message": "Processor Network Unavailable - Try Again", "legacyCode": "3000" }, "networkResponse": { "message": "sample network response text", "code": "XX" } } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "3000.99", "currencyIsoCode": "USD" }, "merchantAccountId": "paypal", "merchantName": "DESCRIPTORNAME", "createdAt": "2021-12-14T20:13:40.000000Z", "channel": null, "customFields": null, "paymentMethodSnapshot": { "origin": { "details": { "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalId": "975af200", "inputMode": "CONTACTLESS", "pinVerified": false } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "c4425b05-7fb8-40cd-9e5f-5cc05278f2fa" } }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfIzMwNzVlNDhlZmRhMDRkZjc4OTY0NjA4MWY2Y2I1YWVlI1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "FAILED", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "transaction": { "id": "dHJhbnNhY3Rpb25fNGZxc3Yyc24", "orderId": "ExampleOrderNumber-12", "status": "GATEWAY_REJECTED", "statusHistory": [ { "status": "GATEWAY_REJECTED", "timestamp": "2021-12-14T20:15:08.000000Z", "terminal": true, "gatewayRejectionReason": "APPLICATION_INCOMPLETE" } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "5001.00", "currencyIsoCode": "USD" }, "merchantAccountId": "paypal", "merchantName": "DESCRIPTORNAME", "createdAt": "2021-12-14T20:15:07.000000Z", "channel": null, "customFields": null, "paymentMethodSnapshot": { "origin": { "details": { "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalId": "975af200", "inputMode": "CONTACTLESS", "pinVerified": false } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "30e1f4b9-84ae-4290-8fbf-f992edcd4d52" } }
### Charge Flow Example Sequence Diagram

The following high-level sequence diagram depicts an example charge flow; however, this flow can vary depending on whether you are vaulting, and polling logic may also vary by application. This is just an example flow.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Charge%20Flow%20Sequence%20Diagram%20.webp)
## Recommended Timeout Logic

Knowing that every application will have different flows and architectural constraints the following recommended timeout logic is just a suggestion based on best practices, but every integration may be different.

Generally, the card reader has a built-in timeout logic of 180 seconds for a “maximum checkout time,” that is, from the moment you [request a charge](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging) from the card reader, it will hang for 180 seconds if no payment instrument is presented. However, it is recommended for the POS application to have its own timeout logic to make sure the POS stays in sync with the card reader and provides a seamless experience to the customer.


#### Recommended sequence for initializing card reader and polling for transaction result:

| **Step 1** | Generate unique Idempotency key (UUID) to be added in your request header |
| **Step 2** | Use an HTTP timeout window of 10 seconds if you do not get back a response |
| **Step 3** | Send the request again using the same Idempotency key, this allows you to recover the request session and avoid sending a duplicate request |
| **Step 4** | Once you get an InstoreContext.Id start polling against it to retrieve the transaction.Id and final transaction status |
| **Step 5** | Use an HTTP timeout window of 3 seconds if you do not get a response while polling against the InStoreContext.Id |
| **Step 6** | Send the [polling request](/braintree/in-person/guides/making-a-transaction/#checking-the-reader-charge-status) every 2-3 seconds until you get the final transaction.status, transaction.Id |


## Cancelling a Charge

If you need to stop a transaction from being paid while the reader is activated and requesting payment, you can [cancel](/braintree/graphql/reference/#Mutation--requestCancelFromInStoreReader) the InStoreContext. Cancelling an InStoreContext places the reader back into **idle mode** and returns you to the PayPal-branded screensaver. It is important to note that canceling a charge is only possible when a payment instrument has not yet been presented to the card reader. After the card reader has been presented with payment, the only way to stop that would be with a reversal or refund of payment.

Note that if you request to cancel theInStoreContextand the API returns a context status of "COMPLETE" that would indicate that the charge has already been processed. In this scenario, you should[check the reader charge status](/braintree/in-person/guides/making-a-transaction/#checking-the-reader-charge-status)again to get thetransactionIdand perform a reversal or[refund](/braintree/in-person/guides/making-a-transaction/)to cancel the charge.  ***** As of August 2022, we have introduced a new API error code 96716, which occurs when you attempt to cancel a context ID that is already in a "PROCESSING" or "COMPLETE" state**GraphQL MutationGraphQL VariablesSample API Responsemutation RequestCancelFromInStoreReader( $input: RequestCancelFromInStoreReaderInput! ) { requestCancelFromInStoreReader(input: $input) { id status reader { id name status location { id name } } } }{ "input": { "inStoreContextId": "context-id" } }{ "data": { "requestCancelFromInStoreReader": { "id": "aW5zdG9yZWNvbnRleHRfI2JmMWFkNzE1MDViMTQwZWU5NWY1MjMzNjU5NDUyMzgwI1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "CANCELLED", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE", "location": { "id": "aW5zdG9yZWxvY2F0aW9uXyMxMDY5ZTk2MGZhODg0M2JmOTMyZDMzYTE3NDlhNjZkMA", "name": "Test Location" } } } }, "extensions": { "requestId": "561448c8-40d9-4ba0-b734-a93d067873b3" } }
## Partial Authorizations

**NOTE**
The Partial Auth feature has undergone a rebuild as of October 2023. The information below represents the new behavior and integration path.

Partial Authorizations refer to transactions where a card with limited available funds is used to complete a purchase, and the available funds are less than the amount to be collected. This can occur with a debit card or a prepaid gift card. For example, if a merchant wants to charge $100, and the customer presents a card with only $50 available. With a partial authorization, the available $50 would be authorized or charged, while the POS system would need to recognize that there is a remaining balance to tender of $50. The POS should generally handle this like a split tender once it is determined that a partial authorization has occurred.

The way for the POS to know that a partial authorization has occurred would be to parse out the [statusReason](/braintree/graphql/reference/#Object--RequestChargeInStoreContext) from the context ID node query, which would show as PARTIALLY_AUTHORIZED. The [context status](/braintree/graphql/reference/#Enum--InStoreContextStatus) will be returned as COMPLETE.

In the Sandbox environment, you may test partial authorizations by using the "amount":"1004" in your request.


### Partial Authorization Enablement

There are 2 ways to enable partial authorization on your account. You may have your PayPal Solutions Engineer or Integration Engineer enable this feature on your account. Alternatively, you may pass an API flag to determine whether you want to allow partial authorizations on the particular transaction using the [acceptPartialAuthorization](/braintree/graphql/reference/#Input--InStoreAuthorizationInput) object. This API flag is a boolean ("true/false") variable that will override the Braintree account-level configuration. We recommend using this API flag if you would like to allow for partial authorization on some transactions and not others, or if you want more control of the enablement of this feature.

**NOTE**
The Partial Authorization feature does need to be enabled on the Braintree gateway account if you are not passing the acceptPartialAuthorization API flag. Please consult with your Solutions Engineer or Integration Engineer to enable it.


## Refunding Your Customer

There are 3 ways of refunding your customer once a charge has been completed.


### 1) Performing a Referenced Refund:

To perform a referenced refund, you must have the transactionId from the authorization that you are attempting to refund against. This results in a refund that is linked to the original authorization. Typically, this is the preferred refund method as it allows for easy accounting. It is important to note that referenced refunds can either be in full or of a partial amount of the original authorization; however, the refund amount can not exceed the full authorized amount.

GraphQL MutationGraphQL VariablesSample API Responsemutation refundTransaction($input: RefundTransactionInput!) { refundTransaction(input: $input) { refund { id amount { value } orderId status refundedTransaction { id amount { value } orderId status } } } }{ "input": { "transactionId": "dHJhbnN5fa20", "refund": { "amount": "9.00", "orderId": "12345Test", "merchantAccountId": "your merchant account ID" } } }{ "data": { "refundTransaction": { "refund": { "id": "cmVmd4bjU2Zh", "amount": { "value": "9.00" }, "orderId": "12345Test", "status": "SUBMITTED_FOR_SETTLEMENT", "refundedTransaction": { "id": "dHJhbnN5fa20", "amount": { "value": "256.00" }, "orderId": "ExampleOrderNumber-19221", "status": "SUBMITTED_FOR_SETTLEMENT" } } } }, "extensions": { "requestId": "7b08c-f890-4255-8e54-dfa62386" } }
#### Referenced Refund Example Sequence Diagram:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Referenced%20Refund%20Sequence%20Diagram.png)
### 2) Using the Reversal API call

Sometimes, the POS might not know whether the original authorization has already been settled or not. In this scenario, it might be best to use a reversal call, which lets Braintree determine whether the transaction can be Voided or Refunded depending on the settlement status. For more details on how this works, [follow this link](/braintree/graphql/guides/transactions/#reversing-or-refunding-a-transaction) and see the example below:

GraphQL MutationGraphQL VariablesSample API Responsemutation reverseTransaction($input: ReverseTransactionInput!) { reverseTransaction(input: $input) { reversal { __typename ... on Transaction { id legacyId orderId status statusHistory { status terminal } } ... on Refund { id legacyId orderId status amount { value } refundedTransaction { id amount { value } orderId status } } } } }{ "input": { "transactionId": "yufkjhvkffif" } }{ "data": { "reverseTransaction": { "reversal": { "__typename": "Refund", "id": "cmVdNoM3MDI1", "legacyId": "ch3t25", "orderId": "Your Order Id", "status": "SUBMITTED_FOR_SETTLEMENT", "amount": { "value": "499.00" }, "refundedTransaction": { "id": "dHJnpb25fYF0ejk", "amount": { "value": "499.00" }, "orderId": "Your Order Id", "status": "SETTLED" } } } }, "extensions": { "requestId": "3f459-7a28-4bf5-9e82-21766d" } }
#### Reversal API Call Example Sequence Diagram:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Reversal%20API%20Calll%20Sequence%20Diagram.png)
### 3) Performing an Unreferenced Refund or "Blind Credit":

To perform an unreferenced refund, your customer must be present at the time of refund, and a payment instrument must be presented to the card reader. The resulting refund will not be linked to the original authorization, so this is typically not the preferred way of refunding due to accounting reasons. Here are some of the common use cases below:


- Refunds to customers without a receipt (when original order cannot be found)


- Refunds to customers whose original authorization occurred while on your previous payment solution


- Refunds to an alternate payment instrument or tender type



**NOTE**
Note that this feature requires approval to be enabled in the production environment and needs to be requested to be enabled by your Solutions Engineer or Integration Engineer in the sandbox environment

GraphQL MutationGraphQL VariablesSample API responsemutation RequestRefundFromInStoreReader($input: RequestRefundFromInStoreReaderInput!) { requestRefundFromInStoreReader(input: $input) { clientMutationId inStoreContext { id status reader { id name status } } } }{ "input": { "readerId": "your reader ID here", "refund": { "amount": "5.00", "orderId": "ExampleOrderNumber-1221", "merchantAccountId": "your merchant account ID here" } } }{ "data": { "requestRefundFromInStoreReader": { "clientMutationId": null, "inStoreContext": { "id": "aW5zdG9yZWNvbnRleH3984hgMGVhYTQ4MjJhYTI1ZTY0YjBmOTY4I1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "PENDING", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jYWo1OWhjbiNWRVJDUtMDE3LTQ1NA", "name": "Your P400", "status": "ONLINE" } } } }, "extensions": { "requestId": "cc3887-2083-4555-b943-67e9d80" } }Once the refund is complete, you'll need to check the status of the context ID, similar to how this is done for a charge request. A status of "COMPLETE" indicates a successful refund.

GraphQL MutationGraphQL VariablesSample API Responsequery ID($inStoreContextId: ID!) { node(id: $inStoreContextId) { ... on InStoreContext { id status reader { id name status } transaction { id } refund { id orderId legacyId status paymentMethodSnapshot { __typename ... on CreditCardDetails { brandCode bin last4 expirationMonth expirationYear } } } } } }{ "inStoreContextId": "aW5zHRfIzIxZmE4YjBjMGLTgwNS0wMTctNDU0I3VzLXdlc3QtMg" }{ "data": { "node": { "id": "aW5zdG9yBjMGVhYTQ4MjJhY05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jbiNWRVJJRk9ORS04MMDE3LTQ1NA", "name": "Your P400", "status": "ONLINE" }, "transaction": { "id": "cmVI5cXM3My" }, "refund": { "id": "cmVmdW3MTNy", "orderId": "ExampleOrderNumber-1221", "legacyId": "234b13r", "status": "SUBMITTED_FOR_SETTLEMENT", "paymentMethodSnapshot": { "__typename": "CreditCardDetails", "brandCode": "VISA", "bin": "421212", "last4": "8885", "expirationMonth": "12", "expirationYear": "2025" } } } }, "extensions": { "requestId": "5fa640-ccf0-4493-955b-6faab7" } }
#### Unreferenced Refund Example Sequence Diagram:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Unreferenced%20Refund%20Sequence%20Diagram.png)
### 4) Reversing a Refund

If a refund was performed and you need to reverse that refund within the acceptable reversal window, you can use the [reverseRefund](/braintree/graphql/reference/#Mutation--reverseRefund) mutation. Keep in mind that you would need to have saved the refundId from the API response of the original refund attempt. See below example of a refund reversal. You will notice that the refundId is a required variable input to perform the reversal.

GraphQL MutationGraphQL VariablesSample API Responsemutation reverseRefund($input: ReverseRefundInput!) { reverseRefund(input: $input) { refund { ... on Refund { id status statusHistory { status terminal } } ... on Refund { id amount { value } orderId status refundedTransaction { id amount { value } orderId status } } } } }{ "input": { "refundId": "your refund ID" } }{ "data": { "reverseRefund": { "refund": { "id": "your refund ID", "status": "VOIDED", "statusHistory": [ { "status": "VOIDED", "terminal": true }, { "status": "SUBMITTED_FOR_SETTLEMENT", "terminal": false }, { "status": "AUTHORIZED", "terminal": false } ], "amount": { "value": "9.00" }, "orderId": "12345Test", "refundedTransaction": { "id": "your transaction ID", "amount": { "value": "55.23" }, "orderId": "12345Test", "status": "SUBMITTED_FOR_SETTLEMENT" } } } }, "extensions": { "requestId": "215c5-1e8a-40c2-a125-afa18b73" } }
#### Refund Reversal Example Sequence Diagram:

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Refund%20Reversal%20Sequence%20Diagram.png)
### 5) Using Auth Adjustments for partial reversals

There may be some use cases where you want to perform a partial reversal rather than fully reverse a payment. The example scenario is if a customer wants to return a single item that was part of a larger purchase, and the transaction may be in an authorized state (which would make a partial refund not possible). In this scenario, you may use the [updateTransaction](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#example-update-transaction-amount-request) API mutation to adjust the auth amount to the total purchase amount minus the partial reversal amount.


## Receipt Data Handling

To maintain EMV compliance you may need to add additional data elements to be displayed on the receipt you offer your customers. The table below highlights the data elements that are mandatory for EMV compliance and other data elements that are optional. Be sure to include the mandatory data elements listed in the "GraphQL API Field" column when you [check the reader charge status](/braintree/in-person/guides/making-a-transaction/#checking-the-reader-charge-status) so that you can parse them from the API response.

**NOTE**
EMV-compliant receipts are not enforced by PayPal/Braintree. We make all necessary data for compliance available through our API and highly suggest following EMV compliance rules. For more information about EMV-compliant receipts, see the [EMVco website](https://www.emvco.com/resources/).

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale:Receipt%20Data%20Handling.webp)This is just an example of an EMV compliant omni-cart receipt. Merchants should format their receipts in a way that make sense for their business while incorporating the below EMV elements listed in the table.**NOTE**
Please take a look at our EMV-compliant [receipt reference page](/braintree/in-person/reference/emv-receipt-reference/), including an explanation with an EMV-compliant data element as an overlay.

| **Data Element** | **Description** | **Mandatory vs. Optional** | **GraphQL API Field** |
| **Merchant Name** | The name of the merchant. | M | Transaction.merchantName |
| **Merchant Address Details** | The address details of the merchant. | M | Transaction.merchantAddress |
| **Transaction Date and Time** | The date and time of the transaction. | M | Transaction.createdAt |
| **Merchant ID (MID)** | The unique reference of the merchant. | O | Transaction.merchantId |
| **Terminal ID (TID)** | The unique reference of the terminal. | O | Transaction.paymentMethodSnapshot.origin.details.terminalId |
| **Transaction Number** | The unique reference number of the transaction. | M | Transaction.legacyId |
| **Invoice Number** | The unique reference number of the receipt. | M | Transaction.legacyId |
| **Card Type** | The name of the card issuer. | M | Transaction.paymentMethodSnapshot. creditCard.brand |
| **Account Number** | The account number printed on the card. All digits except for last 4 must be truncated. | M | Transaction.paymentMethodSnapshot. creditCard.last4 |
| **Application Preferred Name** | The name of the application used to process the transaction (e.g. MasterCard). | M | Transaction.paymentMethodSnapshot.origin.details.applicationPreferredName |
| **Application Identifier** | The unique reference number of the EMV application used for the transaction. | M | Transaction.paymentMethodSnapshot.origin.details.applicationIdentifier |
| **Approval Code** | The authorization code received from the processor for the transaction. | M | Transaction.statusHistory[…]. processorResponse.authorizationId |
| **Authorization Mode** | The authorizing entity (e.g. Issuer). | M | Transaction.paymentMethodSnapshot.origin.details.authorizationMode |
| **Transaction Kind** | The type of the transaction (e.g. Sale/Refund). | M | Transaction.kind |
| **Card Entry Method** | The method used to read the detail of the card (e.g. Chip). | M | Transaction.paymentMethodSnapshot.origin.details.inputMode |
| **Purchase Details** | A brief description of the purchased goods or services along with their prices. | M | Transaction.lineItems* * - If not provided in the authorize/charge request, then these details must be provided by the merchant. |
| **Transaction Amount** | The grand total amount for the transaction. | M | Transaction.amount.value |
| **Currency** | If specified, the currency that the transaction was processed in. If no currency is identified on the receipt, the transaction is deemed to have taken place in the currency that is legal tender at the point of sale. | O | Transaction.amount.currencyCode |
| **PIN Verify Statement** | The cardholder’s PIN verification status specific to the processed transaction (e.g. Verified). | M | Transaction.paymentMethodSnapshot.origin.details.pinVerified |
| **Return and Refund Policies** | The terms and conditions for return and refund set forth by the merchant. | M | Merchant or POS generated message that indicates return policy |

The following are data elements that are mandatory for transactions that were declined:

| **Decline Code** | The system generated decline code for the declined transaction. | M | Transaction.statusHistory[…].processorResponse.legacyCode |
| **Decline Message** | The merchant generated message for the respective decline code. | M | Merchant or POS generated message that reflects the decline code |

The following are data elements that are mandatory for transactions that were EMV chip declined:



| **Terminal Verification Results** | A series of bits set by the terminal upon reading EMV card data, where each bit represents information about the transaction. This value is contained in the response EMV data under tag 95. | M | Transaction.statusHistory[…].processorResponse.emvData |
| **Issuer Authentication Data** | Issuer provided data received in response to an online authorization request to be delivered to the EMV chip card. This value is contained in the response EMV data under tag 91. | M | Transaction.statusHistory[…].processorResponse.emvData |
| **Authorization Response Code** | The 4-character code generated by the Issuer in response to an online authorization request that represents the authorization status of the transaction. This value is contained in the response EMV data under tag 8A. | M | Transaction.statusHistory[…].processorResponse.emvData |


## Manual Key Entry Transactions

There are some use cases in which you may want to support the processing of a transaction without using the card reader by entering in the card details into another application UI. This could be for over-the-phone orders (MOTO) or as a manual key entry (MKE) fallback for when the card is not readable by the card reader, in which case you may want to enter the card details into the POS UI. To facilitate this while keeping your tech stack outside of PCI scope, we have a couple of solutions that can work for you.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20sale_Manual%20Key%20Entry%20Transactions.png)
### 1) Braintree Hosted Fields

The Braintree Hosted Fields enables you to render Braintree encrypted input fields in your application user interface. This allows for the manual key entry of card details directly into Braintree encrypted input fields. See how the [Braintree Hosted Fields](/braintree/docs/guides/hosted-fields/overview/) solution works.

**NOTE**
The Braintree Hosted Fields solution gives you more control over the checkout flow and the flexibility to blend the encrypted fields into your POS UI


### 2) Braintree Drop-in UI

The Braintree drop-in UI allows you to render Braintree encrypted forms in your application user interface. This would allow for the manual key entry of the card details directly into the Braintree Encrypted fields. The drop-in UI is a simple integration leveraging pre-built dynamic Braintree containers. See how the [Braintree Drop-in UI](/braintree/docs/guides/drop-in/overview/javascript/v3/) solution works.

**NOTE**
The drop in UI allows for a simpler integration but reduced control over the look and feel of the UI and checkout flow experience


## Important Tips for building out your charge/refund flows


- Always make sure you are passing your Braintree [Merchant Account ID](/braintree/articles/control-panel/important-gateway-credentials/#merchant-account-id) (MAID) in your charge and refund requests. This should be added as an API variable, for example:![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/InitiateAsalesMakingAtransaction.jpg)


- Use [Idempotency Keys](/braintree/in-person/guides/making-a-transaction/#initializing-the-reader-for-charging) to prevent duplicate charges to your customers


- Align your application with our [recommended timeout logic](/braintree/in-person/guides/making-a-transaction/#recommended-timeout-logic)


- Make sure you are parsing key [EMV receipt data](/braintree/in-person/guides/making-a-transaction/#receipt-data-handling) from your API response to populate on your customer receipts for EMV compliance


- Utilize the [orderId API field](/braintree/in-person/guides/reporting-and-reconciliation/#using-the-order-id-field-to-reconcile-with-braintree-settlement-reports) to pass important data for reporting and reconciliation



[Setup Reader](/braintree/in-person/guides/setup-reader/)[Initiate a Card Present Authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/)