<!-- Source URL: https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Important Gateway Credentials
slug: /articles/control-panel/important-gateway-credentials/
createTime: '2025-04-02T01:30:18.683Z'
updateTime: '2025-04-02T01:30:18.823Z'
---



# Important Gateway Credentials

There are several different identifiers associated with your Braintree account. Here are some important ones you'll need to know.


## API credentials

API credentials are unique account identifiers that must be added to your code before you can process payments via the API. Think of them as your username and password to payment processing. The four API credentials are:


- [**Environment**](#environment)
- [**Public key**](#public-key)
- [**Private key**](#private-key)
- [**Merchant ID**](#merchant-id)


### Environment

The environment specifies where requests via the API should be directed – sandbox or production. Because you have a different set of API keys for each environment, you'll need to update your code depending on which environment you're working in.

There are both production and sandbox environments for the Control Panel and the API. [Learn more about the differences between sandbox and production.](/braintree/articles/get-started/try-it-out)


### API keys

The public and private keys together make up your user's API keys. Each user associated with your Braintree gateway will have their own set of API keys, which they can change or rotate at any time for added security. Because this affects your integration, it should be done with caution. [Learn more about rotating API keys.](/braintree/articles/risk-and-security/control-panel-security/rotating-api-keys)


**IMPORTANT**
 Sandbox API keys are different from those in the production environment, so they must be updated in your code by your developers when switching between environments. More information about switching environments is available in our [developer docs](/braintree/docs/start/go-live).

 


#### Public key

This is your user-specific public identifier. Each user associated with your Braintree gateway will have their own public key.

To find your public key:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**API Keys**section

If no API keys appear, click the **Generate New API Key** button.


#### Private key

This is your user-specific private identifier. Each user associated with your Braintree gateway will have their own private key. Your private key should not be shared outside the use of an API call – even with us.

To find your private key:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**API Keys**section
- Click the**View**link located in thePrivate Keycolumn

Your private key will be revealed in the Private Key column on the next page.


### Merchant ID


**NOTE**
 Your merchant ID is not the same as your merchant account ID. [See below for the differences.](#merchant-account-id-versus-merchant-id)

 

Your merchant ID is the unique identifier for your entire gateway account, including the multiple merchant accounts that may be in your gateway. Often referred to as the public ID or production ID, your merchant ID will be different for your production and sandbox gateways. If you contact our Support team for assistance, we may ask you to confirm this credential for your gateway account.

To find your merchant ID:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**Business**from the drop-down menu

You'll find your merchant ID at the top of this page.

Your merchant ID can also be found when logged into your Control Panel, as the string of letters and numbers following **/merchants/** in the URL.


## Additional credentials

Depending on your integration, you may need to provide other credentials in addition to those listed above.


### Merchant account ID


**NOTE**
 Your merchant account ID is not the same as your merchant ID. [See below for the differences.](#merchant-account-id-versus-merchant-id)

 

A single Braintree gateway can have multiple merchant accounts to process transactions for different businesses or currencies. Each merchant account within a gateway can be identified by its unique **merchant account ID**.

You can use this ID to [specify a merchant account when creating a transaction](/braintree/docs/reference/request/transaction/sale/ruby#specify-merchant-account-id). If you have a single merchant account, it is not necessary to specify a merchant account ID in your API requests. If you have multiple merchant accounts and choose not to specify the merchant account ID, all requests will process through your default merchant account.

Even if you only have one merchant account in your gateway, certain shopping cart integrations may require you to provide your merchant account ID.

To find your merchant account ID(s):


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**Business**from the drop-down menu
- Scroll to the**Merchant Accounts**section

From here you'll see the merchant account IDs in the first column for each account.


**NOTE**
 If you don't see your merchant account IDs in the Control Panel, check to make sure your user's role has the Add/Edit Processing Options [role permission](/braintree/articles/control-panel/users-roles/role-permissions#permission-addedit-processing-options-including-avscvv).

 


#### Adding merchant accounts in sandbox

You can add multiple merchant accounts in your sandbox to test processing in different currencies. For instructions on how to do this, [see our article on testing](/braintree/articles/get-started/try-it-out#testing-currencies).


**NOTE**
 You can only manually create additional merchant accounts in our test environment, the sandbox. [Contact us](/braintree/help/acceptCurrencies) if you need a merchant account added to your production account.

 


#### Merchant account ID versus merchant ID

While merchant account ID and merchant ID sound similar, they are different values with distinct purposes, and are often confused with one another.

Your **merchant ID** is a unique identifier for your entire gateway account and one of the [four API credentials](#api-credentials). This value is required for certain actions, such as connecting your API calls to the Braintree gateway or setting up third-party shopping carts.

Your **merchant account ID** is a unique identifier for a specific merchant account in your gateway. It is used to specify which merchant account to use when creating a transaction, creating a subscription, verifying a payment method, or generating a client token.


#### Business profiles

If you [accept Venmo as a payment method](/braintree/articles/guides/payment-methods/venmo), you can create a custom profile for different businesses or subsidiaries that share a gateway. This will let you display different information to customers paying with Venmo based on which business or site they're purchasing from. [See more about creating multiple profiles for Venmo](/braintree/articles/guides/payment-methods/venmo#multiple-profiles).


### Tokenization keys

[Tokenization keys](/braintree/docs/guides/authorization/tokenization-key) can be used for authorization in your Braintree integration. They authorize the client SDK to tokenize payment information for use on your server.

To view your tokenization keys:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**Tokenization Keys**section

If no key appears, click the **Generate New Tokenization Key** button.


### Client-Side Encryption key

The Client-Side Encryption (CSE) key is required if you are using our older integration method. Similar to the merchant ID, this value is unique to your entire Braintree gateway account, not to a specific user. Some shopping cart integrations may also require the CSE key in order to connect to Braintree.

To find your CSE key:


- Log into either the[production Control Panel](https://www.braintreegateway.com/login)or the[sandbox Control Panel](https://sandbox.braintreegateway.com/login), depending on which environment you are working in
- Click on the gear icon in the top right corner
- Click**API**from the drop-down menu
- Scroll to the**Client-Side Encryption Keys**section

