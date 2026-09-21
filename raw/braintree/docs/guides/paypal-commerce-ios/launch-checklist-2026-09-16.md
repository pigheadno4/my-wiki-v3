<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/paypal-commerce-ios/launch-checklist -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Launch Checklist
slug: /docs/guides/paypal-commerce-ios/launch-checklist/
createTime: '2025-04-02T02:00:55.982Z'
updateTime: '2025-04-02T02:00:56.091Z'
---



# Launch Checklist

You can do a lot in the PayPal Commerce iOS SDK. This doc will make sure you are ready for the
basics.
## Required for basic functionality

**Add the PayPal Commerce SDK to your project, either via**[CocoaPods](/braintree/docs/guides/paypal-commerce-ios/setup#quick-installation)or[direct download](/braintree/docs/guides/paypal-commerce-ios/installation-without-cocoapods).
This allows your users to access your store in your app.**Ensure you are referencing**[PayPalCommerce-Acknowledgements.md](https://github.com/braintree/paypal-commerce-ios/blob/master/PayPalCommerce/PayPalCommerce-Acknowledgements.md).
Several libraries that we use require attribution in your app.****[Configure the SDK in your app delegate](/braintree/docs/guides/paypal-commerce-ios/setup#add-paypal-commerce-to-your-app-delegate).
This lets PayPal Commerce know which store to show in your app.
**IMPORTANT**
You must obfuscate the client ID and secret somehow (this protects your store and your customers).

****[Setup the custom url scheme](/braintree/docs/guides/paypal-commerce-ios/setup#custom-url-scheme-for-user-login).
This is needed to allow our email login system to work for your users, as well as allowing them to
log in with PayPal. Also, it enables deep-linking to products and categories.****[Present the store](/braintree/docs/guides/paypal-commerce-ios/setup#present-the-store)either modally or via a tab bar controller to show the store to your users.**Enable**[Spotlight Search Index](/braintree/docs/guides/paypal-commerce-ios/setup#ios-9-spotlight-search-indexing)so products found via iOS 9 search will open the app in the correct place.****[Update Info.plist](/braintree/docs/guides/paypal-commerce-ios/setup#info-plist-updates)so we can securely communicate with Cloudfront and Facebook and Loggly.**Implement**[3D Touch](/braintree/docs/guides/paypal-commerce-ios/setup#3d-touch)so your users can quickly jump to sections of your app directly from the home screen.
## Optional, but highly recommended

****[Enable push notifications](/braintree/docs/guides/paypal-commerce-ios/setup#push-notification-support).
This lets you broadcast notifications to your users and deep-link them to products and categories.****[Enable Facebook login](/braintree/docs/guides/paypal-commerce-ios/facebook-login).
A quicker authentication mechanism than email.
## Totally optional

****[Add a product card to your app](/braintree/docs/guides/paypal-commerce-ios/product-cards).
This lets you display products and enable commerce in other parts of your app.****[Enable barcode UPC and QR code scanning](/braintree/docs/guides/paypal-commerce-ios/barcode-scanning).
Your users can easily scan, find, and re-purchase products they already have at home or in your
brick and mortar store.
## A note for multiple apps

If you are building multiple iOS apps that will interact with a single PayPal Commerce store, then
you will need to setup multiple OAuth clients. This is necessary to keep our email verification
system functional. In the PayPal Commerce Panel, there's a section called**Channels**,
and under that is**iOS SDK**([commerce.paypal.com/channels/ios/sdk](https://commerce.paypal.com/channels/ios/sdk)). There you will see your primary OAuth client, as well as a space to add more. Each will provide
you with your PayPal Commerce URL scheme, as well as its own**client ID**and**secret**. Read[Configuring the Client](/braintree/docs/guides/paypal-commerce-ios/setup#configure-the-client)for more on where to put those items.