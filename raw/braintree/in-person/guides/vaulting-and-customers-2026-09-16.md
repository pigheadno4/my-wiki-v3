<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/vaulting-and-customers -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: 'Vaulting and Customers '
slug: /in-person/guides/vaulting-and-customers/
createTime: '2024-11-20T19:03:07.060Z'
updateTime: '2025-01-03T19:19:36.421Z'
---



# Vaulting and Customers

The card reader can collect a physically presented payment method and store it for future transactions.


## Getting Started

If you're building a checkout experience that might require additional charges in the future when the customer is no longer present, you may choose to create a flow that vaults the payment method presented to the card reader.

These use cases might include keeping a card on file for members, signing a customer up for a subscription, or performing a checkout in which some items are shipped or fulfilled today and others, later.

These vaulted payment methods can be linked to a customer profile (customer ID) in Braintree which can include additional customer data such as name, email, phone #, etc... or they can be used as standalone payment method tokens (payment method ID) for future payments against a customer profile stored in your own CRM or POS application.

**NOTE**
Future charges against a Multi Use Payment Method will be processed as card-not-present and receive card not present pricing.


## Create a Customer ID (Optional)

The customer object is an important optional component of the Braintree gateway. Use customer ID's to store and organize [payment methods](/braintree/docs/guides/payment-methods/node). A single customer ID can have multiple payment methods.

GraphQL MutationGraphQL VariablesExample Responsemutation createCustomer($input: CreateCustomerInput!) { createCustomer(input: $input) { customer { id legacyId firstName lastName email phoneNumber createdAt } } }{ "input": { "customer": { "firstName": "{{$randomFirstName}}", "lastName": "{{$randomLastName}}", "email": "{{$randomEmail}}", "phoneNumber": "{{$randomPhoneNumber}}" } } }{ "data": { "createCustomer": { "customer": { "id": "Y3VzdG9tZXJfMjQ0NTQ2NDk4", "legacyId": "244546498", "firstName": "Rudy", "lastName": "Cremin", "email": "example@email.com", "phoneNumber": "555-452-7702", "createdAt": "2021-05-13T15:16:36.000000Z" } } }, "extensions": { "requestId": "2480667a-b577-4925-9679-ca46fcaea4aa" } }
## Vaulting a Card without a Transaction

This process can be used to request the vaulting of a PaymentMethod without a related transaction.


### Step 1 - Request Vault from In-Store Reader

This will initialize the card reader for vaulting flow. You will receive a inStoreContextPayload.id in the response to poll and check the status of the customer's interaction with the reader.

GraphQL MutationGraphQL VariablesExample Responsemutation RequestVaultFromInStoreReader( $input: RequestVaultFromInStoreReaderInput! ) { requestVaultFromInStoreReader(input: $input) { id status reader { id name status } } }{ "input": { "readerId": "{{BT_reader_id}}", "customerId": "{{customer_id}}" } }{ "data": { "requestVaultFromInStoreReader": { "id": "aW5zdG9yZWNvbnRleHRfIzVjMmUzNTdhNTZlZTRmYzA4NDNlMGI5NzhkNGYzNzBiI1ZFUklGT05FLTgwMy00MTUtMTY0I3VzLWVhc3QtMg", "status": "PENDING", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jaHo0YzYyeHp0OGZocjc2eSNWRVJJRk9ORS04MDMtNDE1LTE2NA", "name": "P400 Desk", "status": "ONLINE" } } }, "extensions": { "requestId": "a92a8b53-85a4-4174-a0cf-3d3874ddbd04" } }
### Step 2 - Check the Status of the Context

When the context comes back with a status of COMPLETE, you will receive a paymentMethod.id in the response to use in future requests to make charges.

GraphQL MutationVariablesExample Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestVaultInStoreContext { id status reader { id name status } paymentMethod { id legacyId usage details { ... on CreditCardDetails { brandCode bin last4 cardholderName expirationMonth expirationYear uniqueNumberIdentifier binData { prepaid debit countryOfIssuance } } } customer { id email firstName lastName } } verification { id } } } }{ "inStoreContextId": "{{last_braintree_instore_context}}" }{ "data": { "node": { "id": "aW5zdG9yZWNvbnRleHRfI2ExYWUwNzQyYTE4YzQyYTViNTY0NDg5YmM5NTk4YTE1I1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" }, "paymentMethod": { "id": "cGF5bWVudG1ldGhvZF9jY19uam5na3R3", "legacyId": "njngktw", "usage": "MULTI_USE", "details": { "brandCode": "VISA", "bin": "421212", "last4": "8885", "cardholderName": "BRAINTREE TEST", "expirationMonth": "12", "expirationYear": "2025", "uniqueNumberIdentifier": "707d5f902736a0a1d1b4c67af6dff797", "binData": { "prepaid": "UNKNOWN", "debit": "UNKNOWN", "countryOfIssuance": null } }, "customer": { "id": "Y3VzdG9tZXJfMjQ0NTQ2NDk4", "email": "example@email.com", "firstName": "Rudy", "lastName": "Cremin" } }, "verification": { "id": "dmVyaWZpY2F0aW9uX2U5MG04dmtl" } } }, "extensions": { "requestId": "7f5b29f0-3863-4825-b498-afd94e53cfe8" } }**NOTE**
To query more data about the payment method verification check our GraphQL API documentation on the [verification](/braintree/graphql/reference/#Object--Verification) object.


## Vaulting a Card with a Transaction

This process can be used when you wish to place an immediate charge on a card for a known amount, but also save the card for future usage. This might be common where a customer leaves with 3 items today, but 1 item will ship in the future from a warehouse.


### Step 1 - Request Charge from In-Store Reader

Simply include the vaultPaymentMethodAfterTransacting attribute in the requestChargeFromInStoreReader mutation. This will initialize the card reader for the normal charge flow. You will receive a inStoreContextPayload.id in the response to poll and check the status of the customer's interaction with the reader.

GraphQL MutationGraphQL VariablesSample API Responsemutation RequestChargeFromInStoreReader( $input: RequestChargeFromInStoreReaderInput! ) { requestChargeFromInStoreReader(input: $input) { clientMutationId id status reader { id name status } } }{ "input": { "readerId": "{{BT_reader_id}}", "transaction": { "amount": "{{$randomInt}}", "orderId": "Your Order Id - {{$randomUUID}}", "merchantAccountId": "ExampleLocation_2005", "vaultPaymentMethodAfterTransacting": { "when": "ON_SUCCESSFUL_TRANSACTION" } } } }{ "data": { "requestChargeFromInStoreReader": { "clientMutationId": null, "id": "aW5zdG9yZWNvbnRleHRfI2UwYWVmMWVmZDIzYzQ1NjVhYjU0MjNmMmRmNGJiMGEyI1ZFUklGT05FLTgwNC03NzUtMDg1I3VzLWVhc3QtMQ", "status": "PENDING", "reader": { "id": "aW5zdG9yZXJlYWRlcl8jZmFrZV9tZXJjaGFudCNWRVJJRk9ORS01NTUtNTU1LTU1NQ", "name": "POS Terminal #5", "status": "ONLINE" } } }, "extensions": { "requestId": "3009edfd-5e26-440e-8d49-502a5de99f2d" } }
### Step 2 - Check the Status of the Context

When the context comes back with a status of COMPLETE, you will receive a RequestChargeInStoreContext.transaction.customer object in the response to use in future requests to make charges.

GraphQL MutationGraphQL VariablesExample Response{ node(id: "{{last_braintree_instore_context}}") { ... on RequestChargeInStoreContext { id status statusReason reader { id name status } transaction { id orderId status statusHistory { ... on PaymentStatusEvent { status timestamp terminal ... on AuthorizedEvent { processorResponse { authorizationId emvData message legacyCode retrievalReferenceNumber } } ... on GatewayRejectedEvent { gatewayRejectionReason } ... on FailedEvent { processorResponse { retrievalReferenceNumber emvData message legacyCode } networkResponse { message code } } ... on ProcessorDeclinedEvent { processorResponse { legacyCode message authorizationId additionalInformation retrievalReferenceNumber emvData } declineType networkResponse { code message } } } } merchantAddress { company streetAddress addressLine1 extendedAddress addressLine2 locality adminArea2 region adminArea1 postalCode countryCode phoneNumber } amount { value currencyIsoCode } merchantAccountId merchantName createdAt channel customFields { name value } paymentMethodSnapshot { ... on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationPreferredName applicationIdentifier terminalId inputMode pinVerified } } } brandCode last4 bin expirationMonth expirationYear cardholderName binData { issuingBank countryOfIssuance prepaid healthcare debit commercial } } } } } } }{ "inStoreContextId": "your context ID" }"data": { "node": { "id": "aW5zdG9yZWNvbnRleHTk5N2I1NzRkMjE5MTkyNDJmYjFhMmMxY2QwI1ZFUklGT05FLTgwNS05NzEtMjE3I3VzLXdlc3QtMg", "status": "COMPLETE", "reader": { "id": "aW5zdG9yZXJl3B3c2Y0Mmh3OWhjbiNWRVJJRk9ORS04MDUtOTcxLTIxNw", "name": "My M400", "status": "ONLINE" }, "transaction": { "id": "dHJhbnNhY3RpbzA1M3hkZXY", "legacyId": "303xdev", "orderId": "Your Order Id - b74a44d5-515c-4f54-a3c6-c3609bbb7", "status": "SUBMITTED_FOR_SETTLEMENT", "statusHistory": [ { "__typename": "SubmittedForSettlementEvent", "status": "SUBMITTED_FOR_SETTLEMENT", "timestamp": "2023-02-27T23:18:56.000000Z", "terminal": false }, { "__typename": "AuthorizedEvent", "status": "AUTHORIZED", "timestamp": "2023-02-27T23:18:56.000000Z", "terminal": false, "processorResponse": { "authorizationId": "B9F68V", "emvData": "9F240512345678908A023030", "message": "Approved", "legacyCode": "1000", "retrievalReferenceNumber": "1234567" } } ], "merchantAddress": { "company": null, "streetAddress": null, "addressLine1": null, "extendedAddress": null, "addressLine2": null, "locality": "Braintree", "adminArea2": "Braintree", "region": "MA", "adminArea1": "MA", "postalCode": "02184", "countryCode": null, "phoneNumber": "5555555555" }, "amount": { "value": "161.00", "currencyIsoCode": "USD" }, "merchantAccountId": "Location_2005", "merchantName": "DESCRIPTORNAME", "createdAt": "2023-02-27T23:18:55.000000Z", "channel": null, "customFields": null, "paymentMethod": { "id": "cGF5bWVudG1ldGhvZF9jY182bTByYWg2dw", "legacyId": "6m0rah6w", "usage": "MULTI_USE", "details": { "__typename": "CreditCardDetails", "brandCode": "VISA", "bin": "421212", "last4": "8885", "cardholderName": "BRAINTREE TEST", "expirationMonth": "12", "expirationYear": "2025", "uniqueNumberIdentifier": "e71283dde53a937f46e889951b4e3c98", "binData": { "prepaid": "UNKNOWN", "debit": "UNKNOWN", "countryOfIssuance": null } }, "customer": { "id": "Y3VzdG9tZXJfNTAxNzgxMDgy", "email": null, "firstName": null, "lastName": null } }, "paymentMethodSnapshot": { "__typename": "CreditCardDetails", "origin": { "type": "IN_STORE_READER", "details": { "__typename": "EmvCardOriginDetails", "authorizationMode": "ISSUER", "inputMode": "CONTACTLESS", "pinVerified": false, "terminalId": "b316878e", "applicationPreferredName": "Braintree Credit", "applicationIdentifier": "A000000003101001", "terminalVerificationResult": "0000000000", "cardSequenceNumber": null, "applicationInterchangeProfile": null, "terminalTransactionDate": null, "terminalTransactionType": null, "cashbackAmount": null, "applicationUsageControl": null, "terminalCountryCode": null, "applicationCryptogram": null, "cryptogramInformationData": null, "cardholderVerificationMethodResults": null, "applicationTransactionCounter": null, "unpredictableNumber": null, "issuerActionCodeDefault": null, "issuerActionCodeDenial": null, "issuerActionCodeOnline": null } }, "brandCode": "VISA", "last4": "8885", "bin": "421212", "expirationMonth": "12", "expirationYear": "2025", "cardholderName": "BRAINTREE TEST", "binData": { "issuingBank": null, "countryOfIssuance": null, "prepaid": "UNKNOWN", "healthcare": "UNKNOWN", "debit": "UNKNOWN", "commercial": "UNKNOWN" } } } } }, "extensions": { "requestId": "5b4fcb02-b290-4319-b644-4cc654d07" } }
## Making Future Charges

Use the standard Braintree eCommerce GraphQL mutations to make future charges on the paymentMethod.id generated using the above vaulting flows.


- [chargePaymentMethod](/braintree/graphql/reference/#Mutation--chargePaymentMethod) (Sale)


- [authorizePaymentMethod](/braintree/graphql/reference/#Mutation--authorizePaymentMethod) (Auth)


- [captureTransaction](/braintree/graphql/reference/#Mutation--captureTransaction) (Capture)




## Vaulted Digital Wallet payment methods

When digital wallets (such as Apple Pay, Google Pay, and Samsung Pay) are used on the card reader, and a vaulted payment method is requested, that vaulted payment method is stored in the Braintree vault. When that paymentMethod.id token is then used for a subsequent transaction, an MIT (merchant-initiated transaction) flag will be automatically applied to the transaction. This will result in these transactions having an auth expiry window of 24 hours. This means that you should factor in this auth expiry window into your capture flow and re-auth logic.

**NOTE**
We suggest parsing the authorizationExpiresAt object from the API response, which will indicate when the authorization will expire. In the case of authorizations initiated from a paymentMethodId token originating from a card present digital wallet, these auth expiry windows will be 24 hours. You may wish to use this to support your re-auth logic.


## Tips when using Vaulting


- The [paymentMethodId](/braintree/graphql/reference/#Object--PaymentMethod) token is great for performing future charges but is unique per vaulting request, so it is not recommended to be used for customer data analytics.


- The [uniqueNumberIdentifier](/braintree/graphql/reference/#Object--CreditCardDetails) is a unique token per card number that can be used for customer analytics; however, it cannot be used for performing future charges.


- The uniqueNumberIdentifer is only available for cards and not available for [QRC](/braintree/in-person/guides/paypal-and-venmo-qrc/) payment methods (PayPal and Venmo).


- There are a [couple of options](/braintree/graphql/reference/#Enum--VaultPaymentMethodCriteria) when it comes to requesting to vault a payment method. You may request a paymentMethodId token upon a successful auth attempt or "ALWAYS" for every auth attempt, even if unsuccessful.



[Passing Lodging Data](/braintree/in-person/guides/making-a-transaction/passing-lodging-data/)[PayPal and Venmo QRC](/braintree/in-person/guides/paypal-and-venmo-qrc/)