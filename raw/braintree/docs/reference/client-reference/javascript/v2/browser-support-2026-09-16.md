<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/browser-support -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Browser Support
slug: /docs/reference/client-reference/javascript/v2/browser-support/
createTime: '2025-04-01T23:38:16.633Z'
updateTime: '2025-04-01T23:38:16.652Z'
---



# Browser Support

The Braintree JavaScript v2 SDK provides support for numerous browsers and devices. There are, however, caveats with certain integrations and browser combinations.
### Desktop


- Chrome latest
- Firefox latest
- Internet Explorer 8+
- Safari 7+


#### Internet Explorer caveats


##### Quirks Mode

Quirks Mode is not supported for any version of IE. See our[best practices](/braintree/docs/reference/general/best-practices#internet-explorer-quirks-mode)to learn more.
##### Older TLS versions

On June 26, 2018, Braintree ended support for both server-side API requests and client requests via TLS 1.0 and 1.1. Internet Explorer 9 and 10 do not use TLS 1.2 by default. Now that client-side support for older TLS versions has been dropped, this SDK will only work in those IE versions if customers have explicitly enabled TLS 1.2 in their IE settings.
### Mobile


#### iOS


- Safari 8+
- Chrome (iOS 8+)


#### Android


- Native browser 4.2+
- Chrome
- Firefox

While the JS v2 SDK will work in other browsers, these represent the platforms against which we actively test. If you have problems with a specific browser or device,[contact us](/braintree/help?issue=HelpIntegration).
### Webviews

For the most part, webviews on iOS and Android are supported; however, we do not support Chrome for iOS before iOS 8.
#### PayPal and webviews

Additionally, there are a few known issues with PayPal and webviews in our JS v2 SDK:


- PayPal is not supported in webviews on Android versions lower than 4.4.
- iOS has trouble scrolling the PayPal checkout in bothUIWebViews andWKWebViews.

In general, PayPal best practices discourage the use of webviews in order to ensure the applications you develop are secure and optimized for the best possible user experience. Webviews do not offer these benefits – customers can't see a URL bar to verify that the login is legitimate.

**For this reason, we do not intend to fix the known issues above.**Instead, we recommend that you use an appropriate Braintree SDK to manage the PayPal experience or launch the PayPal web page within the system browser or an approved browser-view mechanism, such as Safari View Controller on iOS or Chrome Custom Tabs on Android.
#### Runtime environments

The Braintree JS v2 SDK is neither tested nor developed for hybrid runtimes such as Cordova, PhoneGap, Ionic, React Native, Electron, and Adobe AIR. While some success may be had in such environments, our SDK is optimized for the browser and its security policies and may not function correctly outside of them.