<!-- Source URL: https://developer.paypal.com/braintree/in-person/get-started-1/configure-sandbox -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Configure Sandbox
slug: /in-person/get-started-1/configure-sandbox/
createTime: '2024-11-20T19:04:30.989Z'
updateTime: '2025-01-23T04:45:48.600Z'
---



# Configure Sandbox

We recommend completing the following steps to prepare your Braintree Sandbox Account to connect to your reader and to gain foundational knowledge before your Dev Kit arrives.


### 1. Create a Braintree Sandbox Account

The Dev Kit Verifone P400 reader is designed to be used only with one Braintree Sandbox Account. Once it is paired to a Braintree Sandbox Account the reader cannot be used with any other Braintree Sandbox Account. Please take some time to create a Braintree Sandbox Account or [log in](https://sandbox.braintreegateway.com/login) to your existing Braintree Sandbox Account.

**NOTE**
The Dev Kit is enabled for United States Sandbox Account only. Make sure to select "United States" during sign up.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Get-Started:Configure:Braintree%20Sandbox%20Account%20Sign%20Up.png)Braintree Sandbox Account Sign Up[![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/signup-for-braintree-sandbox.png)](https://www.braintreepayments.com/sandbox)


### 2. Review Authentication Options

Review the [API Authentication Options](/braintree/in-person/guides/api-authentication/) to determine and implement your merchant authentication method of choice. Whether you are a developer working directly with a Merchant or a third-party integrator working on behalf of a Merchant, you will need to choose the implementation that best suits your use case.

The fastest way to get up and running will be using the static 1st-party API Keys. These two values (Public Key and Private Key) are [generated inside your Braintree sandbox merchant account](/braintree/articles/control-panel/important-gateway-credentials#api-keys) and should be copied and saved in a safe place for future use.


### 3. Make a Braintree GraphQL Request

To get up and running quickly we recommend using the [Postman API Client](https://www.postman.com/product/api-client/) in conjunction with the **Braintree GraphQL - In-Store Postman Collection**.

[297KBBraintree GitBook Dev Kit Collection 5_3_24.postman_collection.json](/braintree/files/Braintree%20GitBook%20Dev%20Kit%20Collection%205_3_24.postman_collection.json)Sandbox Postman Collection Above [1KBBraintree GitBook Sandbox Postman Environment 10_2_23.postman_environment.json](/braintree/files/Braintree%20GitBook%20Sandbox%20Postman%20Environment%2010_2_23.postman_environment.json)Sandbox Postman Environment Above**NOTE**
When importing the Postman Collection and Environment, click on the links above and use the URL to import into Postman by going to your Postman workspace &gt; Import &gt; Link and paste in the URL.

After importing the collection to Postman, be sure to update the collection settings to use your Braintree sandbox credentials. To do that, click on the collection, select the Authorization tab, change Type to Basic Auth, enter your sandbox Public API Key into the Username field and Private Key into the Password field, and click Save.

![](https://www.paypalobjects.com/devdoc/btdocs-gitbook/Get-started:configure:Postman%20API%20Credential%20Setup%20Page.png)Postman API Credential Setup Page. Use your Braintree Sandbox Public Key as the Username and Private Key as the Password.[Make your first Braintree GraphQL API request](/braintree/graphql/guides/making_api_calls/#your-first-request) to ensure connectivity. Learn more about creating your own API requests and options available to you.


### 4. Configure Custom Fields in Sandbox (Optional)

Optionally, you may configure In-Store specific [custom fields](/braintree/articles/control-panel/custom-fields) if required on your sandbox merchant account. Custom fields allow you to save additional In-Person specific payment data with each transaction for visibility in the control panel and for reporting purposes. For example, a Cashier ID or tracking the employee that created the transaction.


### 5. Test a "card not present" transaction

Test [creating a card not present transaction](/braintree/graphql/guides/transactions/#creating_transactions) using GraphQL and a range of the [testing nonce values](/braintree/docs/reference/general/testing/php#payment-method-nonces).


### 6. Implement reversals

After you've charged a payment method, you might want to test how to cancel the transaction or refund the customer's money later. Follow this guide on [How to Reverse or Refund a Transaction](/braintree/graphql/guides/transactions/#reversing-or-refunding-a-transaction) using the test transactions created in the previous step. You can also find some [Auth Reversal GraphQL API examples](/braintree/in-person/guides/making-a-transaction/) in our Gitbook documentation.


### 7. Search for transactions

The search query returns the fields you can use to search for objects. Review and test [making transaction searches](/braintree/graphql/guides/search/#constructing-searches) for any back-office or reporting needs. You can also find some GraphQL API examples for using a [transaction query](/braintree/in-person/guides/additional-api-calls/) in our Gitbook documentation.

[Request Dev Kit](/braintree/in-person/get-started-1/get-started/)[Account Structure](/braintree/in-person/get-started-1/account-structure/)