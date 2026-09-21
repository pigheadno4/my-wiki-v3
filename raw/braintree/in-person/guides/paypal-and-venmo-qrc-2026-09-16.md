<!-- Source URL: https://developer.paypal.com/braintree/in-person/guides/paypal-and-venmo-qrc -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: PayPal and Venmo QRC
slug: /in-person/guides/paypal-and-venmo-qrc/
createTime: '2024-11-20T19:04:53.841Z'
updateTime: '2025-04-21T02:38:46.888Z'
---



# PayPal and Venmo QRC

Enabling QR Code transactions for in person wallets can be done using a merchant-presented flow on the Braintree In-Person readers. This feature is in a limited release.

**NOTE**
Since this feature is in a limited release, additional approvals are required before enabling. If you are considering this feature for your integration please discuss approvals with your Solutions Engineer and Account Executive or Customer Success Manager before integrating.


## Access New Customers and Enable Next Generation In-Person Checkout Experiences

The PayPal and Venmo QR Code (QRC) based payment flow is meant to be a seamless experience for both integrators, merchants and customers. Once enabled, the card reader will display an option for the customer to select on the reader which when selected will prompt for the generation of a QR code which the customer can scan with either their PayPal or Venmo mobile apps.

From an integrator standpoint all you need to do is:


- Make sure[QRC is enabled on the locationId](/braintree/in-person/guides/paypal-and-venmo-qrc/#step11-creating-a-location-enabled-for-qrc)which your card reader is paired to
- Ensure that your POS system can[properly handle the API response](/braintree/in-person/guides/paypal-and-venmo-qrc/#step-3-look-for-new-payment-method-snapshot)

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Paypal%20and%20Venmo%20QRC:Access%20new%20customers.png)
## Sign Up for a PayPal Developer Account

Follow the below steps to set up your PayPal sandbox environment so that you can test the PayPal/Venmo QRC payment flows with your Braintree In-Person solution.


- First, you will need to sign up for a [PayPal developer account](https://developer.paypal.com/home)


- Then, you'll need to [create](https://developer.paypal.com/tools/sandbox/accounts/) both a sandbox Business account, as well as a sandbox Personal account.


- Once you've created your sandbox Business account, you'll need to retrieve the **Payer ID,** which is referred to as the **Account ID** in your new PayPal developer account. To do this, first find your sandbox business account and go to "Manage Accounts" &gt; click "view/edit" and your **Account ID** will be under the "Profile" tab


- The Account ID/Payer ID will be used to enable QRC on your locationId and the login credentials for the Personal account will be used to login to the [test flight app for end-to-end testing](/braintree/in-person/guides/paypal-and-venmo-qrc/#testing-qrc-flows-end-to-end).



**NOTE**
Once you have your Account ID/Payer ID, work with your Solutions Engineer or Integration Engineer to finalize the setup.


## Pre-requisite Steps to Enabling QRC

You should onboard PayPal and Braintree accounts with your Solutions Engineer before making any QRC transactions.They will help you through the following required steps: 
- Associate your Braintree merchant account for each currency to be used for retail transactions in the Braintree console panel.
- Click on**action_url**given by TAM and login to the PayPal account
- Click on**“Agree and Connect”**button, which will grant third-party permissions


- Provide the PayPal Payer ID, Business name, and Logo URL
- The business name and logo URL will show up on the consumer app during the QRC transaction




### Step 1.1 - Creating a Location enabled for QRC

During setup, pair your reader to a location that has the QRC Enabled and specify the PayPal Payer ID for the account you wish to receive funds for the QRC transactions.

By clicking on the "GraphQL Variables" tab below you will notice that there are variables called "enableQRCodePayments" which must be "true" and "payerId" which will be retrieved from your own PayPal account as mentioned in [Sign Up for a PayPal Developer Account](/braintree/in-person/guides/paypal-and-venmo-qrc/#sign-up-for-a-paypal-developer-account).

Please note that the value which is passed in the internalName API field in your location ID creation mutation call will be the value that is propagated in the storeId field in PayPal settlement reporting for QR code transactions. So, we would suggest using a store + brand identifier that is less than 64 characters.

GraphQL MutationGraphQL VariablesSample API Responsemutation CreateInStoreLocation($input: CreateInStoreLocationInput!) { createInStoreLocation(input: $input) { location { id name internalName address { streetAddress region locality postalCode countryCode } geoCoordinates { latitude longitude } } } }{ "input": { "location": { "name": "Retailer One", "internalName": "0037", "address": { "streetAddress": "18 West Side Avenue", "extendedAddress": "Unit b", "locality": "Beverly Hills", "region": "California", "postalCode": "90210", "countryCode": "USA" }, "geoCoordinates": { "latitude": 34.0736, "longitude": 118.4004 }, "enableQRCodePayments": true, "payerId": "54P2VNQ6N3PMS" } } }{ "data": { "createCustomer": { "customer": { "id": "Y3VzdG9tZXJfMjQ0NTQ2NDk4", "legacyId": "244546498", "firstName": "Rudy", "lastName": "Cremin", "email": "example@email.com", "phoneNumber": "555-452-7702", "createdAt": "2021-05-13T15:16:36.000000Z" } } }, "extensions": { "requestId": "2480667a-b577-4925-9679-ca46fcaea4aa" } }**NOTE**
You should not use more than 64 characters in the internalName field when creating your location ID. Doing this will cause an error when you attempt a QRC transaction.


### Step 1.2 Updating an existing Location to enable QRC

If you want to update a location that was already created and you want to enable the QRC, you can provide the PayPal Payer ID for that location:

GraphQL MutationGraphQL VariablesSample API Responsemutation UpdateInStoreLocation($input: UpdateInStoreLocationInput!) { updateInStoreLocation(input: $input) { clientMutationId location { id internalName geoCoordinates { latitude longitude } qrCodePaymentsEnabled payerId name address { streetAddress extendedAddress locality region postalCode countryCode } } } }{ "input": { "clientMutationId": "999", "locationId": "aW5zdG9yZWxvY2F0aW9uXyNkNTVmMWQ3MDZmOWY0YWMyOGJmMDc0NjNhMzQzZjNhZg", "location": { "payerId": "19RWNKVZY4GEZ", "enableQRCodePayments": true } } }{ "data": { "updateInStoreLocation": { "clientMutationId": "999", "location": { "id": "aW5zdG9yZWxvY2F0aW9uXyNkNTVmMWQ3MDZmOWY0YWMyOGJmMDc0NjNhMzQzZjNhZg", "internalName": "Barbershop 46217", "geoCoordinates": { "latitude": 37.77, "longitude": -122.42 }, "qrCodePaymentsEnabled": true, "payerId": "19RWNKVZY4GEZ", "name": "Barbershop St Geezy", "address": { "streetAddress": "The mart", "extendedAddress": null, "locality": "my locality", "region": "my region", "postalCode": "982634", "countryCode": "USA" } } } }, "extensions": { "requestId": "85495512-4063-470d-b2c4-28ded0e7f36e" } }
### Step 2 - Make a transaction with QRC

To make a transaction with QRC does not require any extra steps. For more details, [Make a transaction](guides/making-a-transaction/).

Note that the customer must touch the QRC button (with PayPal & Venmo logos) shown above on the main payment page. This will take the screen to the QRC page shown above on the right. After that, the customer can scan the QR code using their PayPal/Venmo app.


#### Vaulting and QRC


**NOTE**
QR Code payment methods do not support vaulting, and these payment options are automatically hidden when the vaulting flag is set to the below in your requestCharge:    vaultPaymentMethodAfterTransacting":      "when": "ON_SUCCESSFUL_TRANSACTION"    For Cash & Carry or other transactions where vaulting is not required simply remove this flag from your API call to show the QR code payment options.   Optionally you may also use the qrcOverride API flag to control whether the QRC payment method option is displayed on the reader. See the example API request below:



GraphQL MutationGraphQL VariablesSample API Responsemutation RequestChargeFromInStoreReader($input: RequestChargeFromInStoreReaderInput!) { requestChargeFromInStoreReader(input: $input) { clientMutationId inStoreContext { id status transaction { id orderId status customer{ id } paymentMethodSnapshot{ __typename ... on CreditCardDetails { brandCode bin last4 cardholderName expirationMonth expirationYear } } } reader { id name status softwareVersion } } } }{ "input": { "readerId": "your reader Id", "transaction": { "amount": "any amount", "orderId": "Your Order Id", "merchantAccountId": "your merchant account Id", "vaultPaymentMethodAfterTransacting": { "when": "ON_SUCCESSFUL_TRANSACTION", "qrcOverride": "SHOW_QRC_NO_VAULT" } } } }{ "data": { "requestChargeFromInStoreReader": { "clientMutationId": null, "inStoreContext": { "id": "aW5zdG9yZWNvzRiMzNhNDQ4MmE2MmJhNjMwNjE5I1ZFUklGT05FLTgwNS0wMTctNDU0I3VzLXdlc3QtMg", "status": "PENDING", "transaction": null, "reader": { "id": "aW5zdG9OWhjbiNWRVJJRk9ORS04MDUtMDE3LTQ1NA", "name": "Test P400", "status": "ONLINE", "softwareVersion": "4.0.0" } } } }, "extensions": { "requestId": "73b000-eaf8-4999-975e-e9fe7c3a" } }**NOTE**
Note that you have two potential options to pass in the [QRC override API flag](/braintree/graphql/reference/#Enum--VaultQRCOverride) :   •  **"SHOW_QRC** **_** **NO_VAULT"** which will display the QR code payment option. This should be used when you do NOT require a reusable payment method token.   •  **"HIDE_QRC"** which will hide the QR code payment option. This should be used when you DO require a reusable payment method token.


### Step 3 - Look for a New Payment Method Snapshot

Request a charge from the card reader like normal. After polling, the instore context will move to COMPLETE. For PayPal and Venmo transactions, you will see a new type of PaymentMethodSnapshot with additional data available.

GraphQL QueryGraphQL VariablesSample API Responsequery ID($contextId: ID!) { node(id: $contextId) { ... on RequestChargeInStoreContext { id status statusReason reader { id name status } transaction { id orderId status customer { id } statusHistory { ... on PaymentStatusEvent { status timestamp terminal ... on AuthorizedEvent { processorResponse { authorizationId emvData message legacyCode retrievalReferenceNumber } } ... on GatewayRejectedEvent { gatewayRejectionReason } ... on FailedEvent { processorResponse { retrievalReferenceNumber emvData message legacyCode } networkResponse { message code } } ... on ProcessorDeclinedEvent { processorResponse { legacyCode message authorizationId additionalInformation retrievalReferenceNumber emvData } declineType networkResponse { code message } } } } merchantAddress { company streetAddress addressLine1 extendedAddress addressLine2 locality adminArea2 region adminArea1 postalCode countryCode phoneNumber } amount { value currencyIsoCode } merchantAccountId merchantName createdAt channel customFields { name value } paymentMethodSnapshot { ... on CreditCardDetails { origin { details { ... on EmvCardOriginDetails { applicationPreferredName applicationIdentifier terminalId inputMode pinVerified } } } brandCode last4 bin expirationMonth expirationYear cardholderName binData { issuingBank countryOfIssuance prepaid healthcare debit commercial } } ... on PayPalTransactionDetails { authorizationId captureId paymentId appUsedForScanning payer { payerId email } } ... on VenmoAccountDetails { username venmoUserId } } } } } }{ "inStoreContextId": "{{last_braintree_instore_context}}" }"paymentMethodSnapshot":{ "__typename":"PayPalTransactionDetails", "authorizationId":"69030361G5125912T", "appUsedForScanning":"PAYPAL", "payer":{ "payerId":"DEY23UKDEEFJC", "email":"lucy@pp.com" } }
## Testing QRC Flows End to End

To test QR code flows for PayPal and Venmo payment methods you will also need to download the PayPal and Venmo test-flight apps to scan the QR code on your sandbox readers to complete the payment. To get you access to these test apps, you will need to request this from your Braintree Solutions Engineer or Integration Engineer.

**NOTE**
When requesting access to these test apps, we will need to know whether you will be testing on an iOS or Android device. We will also need to know the emails associated with either your Apple Store or Google App Store accounts.


## Use of the orderId field for PayPal and Venmo Transactions

By default, your PayPal account may have the "Block Payments" setting configured to "Yes, block multiple payments per invoice ID" which would reject transaction requests using the same orderId. This could either impact your regular testing or split tender transactions, which could use the same orderId. To resolve this, log into your PayPal account, navigate to Account Settings &gt; Payment Preferences &gt; Update Block Payments, and set to "No, allow multiple payments per invoice ID" as depicted below:

**NOTE**
When making this change, consult with your PayPal Solutions Engineer or Integration Engineer, as it may impact other components of your integration.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Paypal%20and%20Venmo%20QRC:Block%20Payments.png)
## Refunding Transactions with QRC

We only support [referenced refunds](/braintree/in-person/guides/making-a-transaction/#id-1-performing-a-referenced-refund) and [reversals](/braintree/in-person/guides/making-a-transaction/#id-2-using-the-reversal-api-call) for QRC transactions. In the event that you are unable to complete one of these refund types, you may complete an [unreferenced refund](/braintree/in-person/guides/making-a-transaction/#id-3-performing-an-unreferenced-refund-or-blind-credit) to an alternate payment method (credit or debit card) of the customer's choice.

[Vaulting and Customers](/braintree/in-person/guides/vaulting-and-customers/)[Display Information](/braintree/in-person/guides/display-information/)