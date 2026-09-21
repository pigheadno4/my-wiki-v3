<!-- Source URL: https://developer.paypal.com/braintree/docs/start/example-integrations-drop-in/using-the-examples -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Using the Examples
slug: /docs/start/example-integrations-drop-in/using-the-examples/
createTime: '2025-04-02T00:45:16.394Z'
updateTime: '2026-09-02T15:14:29.572Z'
---



# Using the Examples


**IMPORTANT**
 **Starting October 1, 2026**, the Drop-in SDK will be [**deprecated**](/braintree/docs/guides/client-sdk/deprecation-policy/ios/v6/#status-categories). No new features, improvements, or bug fixes will be released after this date. Payment processing will continue to be supported until **October 1, 2027**, but we strongly recommend migrating to the Braintree SDK as soon as possible to avoid future disruption.

  **Starting October 1, 2027**, the Drop-in SDK will become [**unsupported**](/braintree/docs/guides/client-sdk/deprecation-policy/ios/v6/#status-categories). Braintree support team will no longer provide assistance for this SDK, and payment processing may be suspended at any time.

  **Action required:** Migrate to the [Braintree Android SDK](/braintree/docs/guides/client-sdk/setup/android/v5/), [Braintree iOS SDK](https://braintree.github.io/braintree_ios/current/), or [Braintree JavaScript SDK](/braintree/docs/guides/client-sdk/setup/javascript/v3/) to continue processing payments and receive ongoing updates, security fixes, and support.

 

We have created example repositories on GitHub with end-to-end integrations for each server-side language that Braintree supports. These examples use our [Drop-in UI for web](/braintree/docs/guides/drop-in/overview) for the client-side integration.


## Repositories


- [Java (Spring)](https://github.com/braintree/braintree_spring_example)
- [.NET (ASP.NET)](https://github.com/braintree/braintree_aspnet_example)
- [Node.js (Express)](https://github.com/braintree/braintree_express_example)
- [PHP](https://github.com/braintree/braintree_php_example)
- [PHP (Slim)](https://github.com/braintree/braintree_slim_example)
- [Python (Flask)](https://github.com/braintree/braintree_flask_example)
- [Ruby (Rails)](https://github.com/braintree/braintree_rails_example)


### Running example repos

The end-to-end example integrations are made to run on a local server or on Heroku. You'll need a Braintree sandbox account and a couple of things handy:


- Merchant ID
- Public key
- Private key

For details on where to find these values, [see our support articles](/braintree/articles/control-panel/important-gateway-credentials#api-credentials).

To set up an example locally, follow the setup instructions found in the project's README.


### Test with the examples

Once you have the example repository up and running in your chosen server language, you should be able to run some test transactions.


#### Test credit cards

Try making some credit card transactions with our [test card numbers](/braintree/docs/reference/general/testing#credit-card-numbers). See our [testing reference](/braintree/docs/reference/general/testing) for more information on testing transactions.


#### PayPal sandbox

To test PayPal transactions, follow the instructions for [linking a PayPal sandbox account](/braintree/docs/guides/paypal/testing-go-live#linked-paypal-testing) with your Braintree sandbox account. You will then be able to go through a sandbox PayPal flow through the Drop-in UI and log in to PayPal with your sandbox credentials.

