<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/payment-method-types-overview -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Payment Method Types
slug: /docs/guides/payment-method-types-overview/
createTime: '2025-04-01T22:44:00.431Z'
updateTime: '2026-05-27T08:48:13.947Z'
---



# Overview



 The guides in this section will show you how to add specific payment method types to your Braintree integration.

Read on to learn:


- [What you will need](#what-you-will-need)
- [Integration steps](#integration-steps)
- [How to get help](#how-to-get-help)

  **See also**
- [Get started with payment methods support article](/braintree/articles/get-started/payment-methods)
- [Support articles for each payment method type](/braintree/articles/guides/payment-methods/ach)

 


## What you will need


### Compatible Braintree account

Certain aspects of payment processing (including which payment method types you can accept) vary depending on the banking partner for your Braintree production account. When we set up your production account, we send you information about the payment method types that your banking partner supports.

If you already have a production account, refer to the Accepted Payment Methods page of your bank-specific support articles.


### Availability in your region

Some payment method types are only available in certain countries or regions, so your business location matters, too. Similarly, your customers' locations determine which payment method types they can use.

[See detailed availability and compatibility information for each payment method type in our support articles.](/braintree/articles/get-started/payment-methods)


### Braintree client and server SDK integration

The guides in this section assume that you already have client-side and server-side integrations using our SDKs. You’ll find high-level SDK support information in each guide, with more granular version support details in our SDK changelogs on GitHub.

To access the greatest range of payment method types, use our latest client and server SDK versions.

If you don’t already have a Braintree integration, follow the [basic payments integration guide](/braintree/docs/start/overview) in Get Started first.

**NOTE**
If you use Braintree through a [third-party integration or shopping cart](https://www.braintreepayments.com/features/third-party-integrations), they'll handle the client and server integration for you. Refer to their documentation and contact them directly with any questions about adding payment method types to your checkout.


## Integration steps

The guides in this section on the left will walk you through a basic integration of each payment method type we offer, from availability and features to implementation details and code snippets. There are generally 4 main steps to accepting a new type of payment method:


- **Configure the payment method type**: Enable the desired payment method type for your Braintree account and complete any required registration steps with the payment method provider
- **Update your client-side integration**: Add a customer-facing UI to your checkout to collect payment method information and set client-side options
- **Update your server-side integration (when applicable)**: Ensure your server acts on the collected payment method information appropriately
- For simple use cases, the same server-side code can handle any payment method nonce, regardless of the payment method type – so you may not need to update your server-side integration at all.
- However, some payment method types require additional data on server-side calls or don’t allow certain actions (like vaulting), and more complex use cases may require unique server-side implementations.


- **Test and go live**: Confirm your setup is working correctly end-to-end in both sandbox and production and complete any required go-live steps


**NOTE**
Inform your payers that Braintree is processing the payment by implementing one of the following options: 
- Include the following text and a link to the PayPal privacy notice at checkout: "By paying with your card, you acknowledge that your data will be processed by Braintree subject to the PayPal Privacy Statement available at[braintreepayments.com](http://braintreepayments.com)."
- Include the following language in your privacy notice, which must be shown before payment: "We use Braintree, a PayPal service, for payments and other services. If you wish to use one of these services and pay on our website, Braintree may collect the personal data you provide, such as payment and other identifying information. Braintree uses this information to operate and improve the services it provides to us and others, including for fraud detection, harm and loss prevention, authentication, analytics related to the performance of its services, and to comply with applicable legal requirements. The processing of this information will be subject to the PayPal Privacy Statement available at[braintreepayments.com](http://braintreepayments.com)."

 


## How to get help


- [Support articles](/braintree/articles): Get details on regional availability and account compatibility, fees, processing flows, and Control Panel management.
- [Reference](/braintree/docs/reference/overview): Explore advanced options and field-level details in our client and server SDK references.
- [Contact Sales](https://www.braintreepayments.com/contact/sales): Discuss pricing and which payment method types are best for your business.
- [Contact Support](/braintree/help/acceptPaymentTypes): Get help enabling or implementing a payment method type.

