<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Initiate a Card Present Authorization
slug: /in-person/guides/making-a-transaction/initiate-a-card-present-authorization/
createTime: '2024-11-20T19:05:44.304Z'
updateTime: '2025-01-20T07:46:42.197Z'
---



# Initiate a Card Present Authorization

This page covers the support of separate auth from capture on the Braintree In-Person solution from a card present perspective.


## Feature Overview

For some use cases where a capture delay is required (ex: endless aisle, save the sale, tipping on receipt, hotel check-in), you may need to request an authorization rather than requesting a charge. This gives the API caller complete control over the authorization capture cadence rather than relying on automated Braintree capture logic. Generally, this operates similarly to e-commerce authorization flows, with some important differences.

**NOTE**
Separate auth and capture using the [requestAuthorization](/braintree/graphql/reference/#Mutation--requestAuthorizeFromInStoreReader) API mutation is supported starting in firmware [version 5.1.0](/braintree/in-person/reference/app-version-release-notes/#version510)


## Initializing the Reader for Authorization

When you're ready to charge a customer, you can create an In-Store Context by requesting to authorize a card on the reader. In this step, your application will specify at minimum, the readerId, merchantAccountId and transaction.amount details to initialize the reader for payment acceptance. Note that the merchantAccountId is not validated against in the Sandbox environment; however, this is a required value in the Production environment for all interactions with the card reader.

Authorizing is similar to charging, except that if the authorization is successful, Braintree will NOT capture the transaction. It would be up to the merchant to send a separate capture request using the transaction.id to complete the charge.

**NOTE**
Card present authorizations only allow for a single capture request; multiple partial capture is NOT supported. Any remaining authorized funds after the first capture will automatically be voided.

To provide idempotency on the [requestAuthorize](/braintree/graphql/reference/#Mutation--requestAuthorizeFromInStoreReader) mutation, you must also include the HTTP header Idempotency-Key with a unique value. UUIDv4 is recommended. For example, if using curl to make the request, you would include

**NOTE**
Using Idempotency-Key is an important way of preventing duplicate charges to your customer in the event of an API communication failure. For example: if you request a charge from the reader, the customer completes the charge on the reader but for some reason, the POS does not get back the result of the transaction before timing out. In this scenario, the POS could recover the original transaction using the same Idempotency-Key without accidentally creating a duplicate charge.

--header 'Idempotency-Key: 94c9ea8b-31b0-488e-a231-57e32f0bfd70'GraphQL MutationGraphQL VariablesSample API Responsemutation RequestAuthorizeFromInStoreReader($input: RequestAuthorizeFromInStoreReaderInput!) { requestAuthorizeFromInStoreReader(input: $input) { clientMutationId id status reader { id name status } } }{ "input": { "clientMutationId": "your event/request reference", "readerId": "your reader ID", "transaction": { "amount": "any amount", "orderId": "Your Order Id", "merchantAccountId": "your merchant account ID" } } }{ "data": { "requestAuthorizeFromInStoreReader": { "clientMutationId": "your event/request reference", "id": "aW5zdI2U3NzY3NTQ4YjM2Mzk0MGExNzU1Yjk5YWM3I1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "PENDING", "reader": { "id": "aW5z3B3c2Y0Mmh3hjbiNWRVJJRk9ORS04MDUtMDE3LTQ1NA", "name": "Your P400", "status": "ONLINE" } } }, "extensions": { "requestId": "1b170326-3523-47c1-add6-b079b1ab0" } }
## Checking the Reader Authorization Status

After the reader is initialized for payment, your application must wait for the customer to interact with it (i.e. insert a test card) and for the payment attempt to be processed. Your application should use [the node query](/braintree/graphql/reference/#Query--node) to poll on a 2-second interval between responses for the current status of the payment using the RequestChargeInStoreContext.id received at charge initialization and monitor the RequestAuthorizeInStoreContext.status field as the transaction goes through the lifecycle.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Initiate%20a%20card%20present%20authorrization:Checking%20the%20Reader%20Authorization%20Status.png)COMPLETE context status will indicate an "Authorized" transaction status, not "SUBMITTED_FOR_SETTLEMENT" when using the Request Authorize mutationWhen the RequestAuthorizeInStoreContext.status changes to "COMPLETE", you will also receive a transaction object RequestAuthorizeInStoreContext.transaction in the response. Save the completed RequestAuthorizeInStoreContext.transaction.id in your database for referencing the transaction in subsequent operations (ie. capture, adjust auth, void, etc...).

All successful test transactions should have a transaction amount value below $2,000 for testing. For more info on using amounts to simulate various transaction outcomes, take a look at [Testing Your Integration](/braintree/in-person/guides/testing-your-integration/).

QuerySample API response (successful auth){ node(id: "{{last_braintree_instore_context}}") { ... on RequestAuthorizeInStoreContext { id status statusReason reader { id name status } transaction { id orderId status statusHistory { ... on PaymentStatusEvent { status timestamp terminal ... on AuthorizedEvent { authorizationExpiresAt processorResponse { authorizationId emvData message legacyCode retrievalReferenceNumber } } ... on GatewayRejectedEvent { gatewayRejectionReason } ... on FailedEvent { processorResponse { retrievalReferenceNumber emvData message legacyCode } networkResponse { message code } } ... on ProcessorDeclinedEvent { processorResponse { legacyCode message authorizationId additionalInformation retrievalReferenceNumber emvData } declineType networkResponse { code message } } } } merchantAddress { company streetAddress addressLine1 extendedAddress addressLine2 locality adminArea2 region adminArea1 postalCode countryCode phoneNumber } amount { value currencyIsoCode } merchantAccountId merchantName createdAt channel customFields { name value } paymentMethodSnapshot { ... on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationPreferredName applicationIdentifier terminalId inputMode pinVerified } } } brandCode last4 bin expirationMonth expirationYear cardholderName binData { issuingBank countryOfIssuance prepaid healthcare debit commercial } } } } } } }{ "data": { "node": { "id": "aW5zdG9yZWNTQ4YjM2ZTRlZDRhMzk0MGExNzU1Yjk5YWM3I1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRY0Mmh3OWo1OWhjbiNWRVJJRk9ORS04MDUtMDE3LTQ1NA", "name": "Your P400", "status": "ONLINE" }, "transaction": { "id": "dHJhb25fYjNhc2VqY2E", "legacyId": "bsejca", "orderId": "Your Order Id", "status": "AUTHORIZED", "statusHistory": [ { "__typename": "AuthorizedEvent", "status": "AUTHORIZED", "timestamp": "2023-06-16T18:24:07.000000Z", "terminal": false, "processorResponse": { "authorizationId": "G5TJ7V", "emvData": "9F240512345678908A023030", "message": "Approved", "legacyCode": "1000", "retrievalReferenceNumber": "1234567" } } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "792.00", "currencyIsoCode": "USD" }, "merchantAccountId": "OverCapture_AdjustAuth", "merchantName": "DESCRIPTORNAME", "createdAt": "2023-06-16T18:24:06.000000Z", "channel": null, "customFields": null, "paymentMethodSnapshot": { "__typename": "CreditCardDetails", "origin": { "type": "IN_STORE_READER", "details": { "__typename": "EmvCardOriginDetails", "authorizationMode": "ISSUER", "inputMode": "CONTACTLESS", "pinVerified": false, "terminalId": "9c3b9fc0", "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalVerificationResult": "0000000000", "cardSequenceNumber": null, "applicationInterchangeProfile": null, "terminalTransactionDate": null, "terminalTransactionType": null, "cashbackAmount": null, "applicationUsageControl": null, "terminalCountryCode": null, "applicationCryptogram": null, "cryptogramInformationData": null, "cardholderVerificationMethodResults": null, "applicationTransactionCounter": null, "unpredictableNumber": null, "issuerActionCodeDefault": null, "issuerActionCodeDenial": null, "issuerActionCodeOnline": null } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "75004704-898e-4621-a37c-8ead03b1" } }
## Capturing funds against an Authorization

To capture the authorized funds, you must use the [Capture Transaction mutation](/braintree/graphql/reference/#Mutation--captureTransaction) within a 24-hour window of the funds being authorized (except for eligible Lodging MCC codes, which have expiry windows of up to 30 days). For a card-present authorization, you are allowed only a single capture attempt. Any remaining authorized funds not captured after the initial capture request will be voided. You may capture a lesser amount than what was authorized or an amount up to the maximum over-capture threshold (subject to eligibility). For merchants processing on MCC codes ineligible for over-capture, the maximum amount allowed for capture is the amount authorized.

**NOTE**
The transaction must be in an Authorized state to allow for funds capture


### Example Capture request

GraphQL MutationGraphQL VariablesSample API Responsemutation CaptureTransaction($input: CaptureTransactionInput!) { captureTransaction(input: $input) { transaction { id status } } }{ "input": { "transactionId": "transaction ID from successful authorization", "transaction": { "amount": "input amount to be captured" } } }{ "data": { "captureTransaction": { "transaction": { "id": "dHJhbnNhYfYWt6Zmp5ODM", "status": "SUBMITTED_FOR_SETTLEMENT" } } }, "extensions": { "requestId": "39f948cb-96f2-406e-9f9f-21787452f" } }
## Using Incremental Authorizations

For some merchants, for example, those in the Hotels & Hospitality or some other industries, incremental authorizations (aka adjust auth) are an important feature for use cases such as tipping adjustment, hotel room damages, or hotel mini-bar charges, etc... This feature is subject to merchant eligibility based on MCC code, and it is also not supported for AMEX transactions and some other transaction types. This feature leverages the [updateTransactionAmount API mutation](/braintree/graphql/reference/#Mutation--updateTransactionAmount) with Braintree's GraphQL API.

**NOTE**
The transaction must be in an Authorized state to be eligible for adjustment


### Example Update Transaction Amount request

GraphQL MutationGraphQL VariablesSample API Responsemutation updateTransactionAmount($input: UpdateTransactionAmountInput!) { updateTransactionAmount(input: $input) { transaction { id status customer{ email firstName lastName id } } } }{ "input": { "transactionId": "transaction ID from successful authorization", "amount": "new desired authorization amount" } }{ "data": { "updateTransactionAmount": { "transaction": { "id": "dHJhbnNhY3bTVwZWZla3M", "status": "AUTHORIZED", "customer": null } } }, "extensions": { "requestId": "f7e636cb-5da5-45dd-ac73-c94b404d" } }
### Using Estimated Auth (Pre-Auth)

Using an estimated authorization or a "pre-auth" can help avoid issuer rejections and improve authorization rates for scenarios when you may not know the final charge amount at the time of authorization. Some industries where this may be common are hotels, vehicle rentals, bars, etc... It is recommended that you use this feature if you are using incremental auth. To trigger an estimated authorization you must pass the [paymentInitiator](/braintree/graphql/reference/#Enum--InStorePaymentInitiator) flag with a value of " ESTIMATED ". See example below:

GraphQL MutationGraphQL Variablesmutation RequestAuthorizeFromInStoreReader($input: RequestAuthorizeFromInStoreReaderInput!) { requestAuthorizeFromInStoreReader(input: $input) { clientMutationId inStoreContext { id status transaction { id orderId status customer{ id } paymentMethodSnapshot{ __typename ... on CreditCardDetails { brandCode bin last4 cardholderName expirationMonth expirationYear } } } reader { id name status softwareVersion } } } }{ "input": { "readerId": "your reader ID", "transaction": { "amount": "any amount", "orderId": "your order ID", "merchantAccountId": "your merchant account ID", "paymentInitiator": "ESTIMATED" } } }
## AMEX Over Capture Rules

MCC codes such as **4821** (Taxi Cabs and Rideshares) and **5812** (Restaurants) are allowed to capture up to 20% more than the authorized amount.

MCC codes such as **7011** (Lodging), **7512** / **7513** / **7519** (Vehicle Rentals), as well as Cruise Lines, Grocery merchants, and Retailers are allowed to capture up to 15% more than the authorized amount.

If you have a direct contract with AMEX, you may need to reach out to them to have them configure your account to allow for over-captures.


## Important Tips When Integrating Separate Auth from Capture


- [Request Authorization](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#initializing-the-reader-for-authorization) is supported for [offline transactions](/braintree/in-person/guides/offline-transactions/)


- Some MCC codes are allowed to capture more (aka over capture) than the authorized amount (typically used by restaurant merchants for tipping purposes)


- Some MCC codes are allowed to use incremental authorizations (adjust auth) in order to incrementally increase the auth amount (typically used by Hotel & Hospitality merchants)


- To enable over-captures or incremental authorizations, your Braintree account must be configured accordingly. Please work with your Solutions Engineer or Integration Engineer to facilitate this


- Incremental Auth is not supported for AMEX transactions. For some use cases, you may need to perform an over-capture for an AMEX transaction


- [PayPal and Venmo QRC](/braintree/in-person/guides/paypal-and-venmo-qrc/) transactions are NOT supported for separate auth from capture


- Passing of [L2/L3 data](/braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing/) is not supported in the authorization request; however, you may pass this data in the [separate capture](/braintree/in-person/guides/making-a-transaction/initiate-a-card-present-authorization/#capturing-funds-against-an-authorization) request



[Initiate a Sale or Refund](/braintree/in-person/guides/making-a-transaction/)[Level 2 and Level 3 Data Processing](/braintree/in-person/guides/making-a-transaction/level-2-and-level-3-data-processing/)