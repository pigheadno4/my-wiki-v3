<!-- Source URL: https://developer.paypal.com/braintree/docs/start/hosted-fields -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Hosted Fields
slug: /docs/start/hosted-fields/
createTime: '2025-04-01T23:46:04.442Z'
updateTime: '2025-04-01T23:46:04.467Z'
---



# Hosted Fields

Hosted Fields is a way to accept credit card payments securely using our JavaScript SDK, while staying in control of the style of your desktop and mobile website checkout UI.


### Inputs for credit card data

Hosted Fields provides custom iframes for collecting certain sensitive payment fields, which are rendered as inputs directly onto your checkout page.

[See the examples](/braintree/docs/guides/hosted-fields/examples/javascript/v3)![Hosted,fields,code,window](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/hosted-fields/hosted_fields_code_window.svg)![Hosted,fields,lock,icon](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/hosted-fields/hosted_fields_lock_icon.svg)
##### Securely-hosted credit card data

Use Hosted Fields to remain eligible for SAQ A PCI compliance.

![Hosted,fields,palette,icon](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/hosted-fields/hosted_fields_palette_icon.svg)
##### Your customized look and feel

Style your checkout form according to your specific brand guidelines.

![Hosted,fields,code,icon](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/hosted-fields/hosted_fields_code_icon.svg)
##### Card-specific form events

Check for valid credit card inputs and update your UI accordingly.


## Hosted Fields and your server

Data collected using Hosted Fields is sent directly from your client to Braintree, so your customers' raw payment information never touches your server.

Braintree associates that data with a secure, one-time-use string called a payment method nonce, which is used instead.

This exchange helps safeguard your customers' card data – and helps keep your PCI compliance scope to a minimum.


## Integrate Hosted Fields


##### Step-by-step


- [Set up your server](/braintree/docs/start/hello-server)with one of our server SDKs in the language of your choice.
- [Set up your web client](/braintree/docs/guides/client-sdk/setup)with our JavaScript SDK, then[add Hosted Fields](/braintree/docs/guides/hosted-fields/setup-and-integration).
- Consider adding other[payment methods](/braintree/docs/guides/payment-method-types-overview)to complete your integration.
- If needed,[set up your iOS](/braintree/docs/guides/client-sdk/setup/ios/v5)and[Android clients](/braintree/docs/guides/client-sdk/setup/android/v4)using our mobile SDKs.

Want to dig deeper? Our JavaScript v3 client reference has all the details.

[See the Hosted Fields reference](https://braintree.github.io/braintree-web/current/HostedFields.html)If you're looking for a pre-formatted form to start accepting payments on mobile and web, consider reading about the [Drop-in UI](/braintree/docs/start/drop-in), the quickest way to get set up with Braintree.

