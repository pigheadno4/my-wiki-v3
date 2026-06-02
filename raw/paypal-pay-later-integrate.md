---
title: Add Pay Later messages and buttons
slug: /docs/checkout/pay-later/integrate/
createTime: "2025-11-03T07:35:49.771Z"
updateTime: "2026-02-06T08:34:04.436Z"
---

# Add Pay Later messages and buttons

     Integrate Pay Later messaging and buttons  Integrate Pay Later messaging to show customized payment offers for your buyers. You can get started quickly with this copy-and-paste integration.

**Note:** Pay Later messaging requires a PayPal Checkout integration. To integrate PayPal Checkout, see our [PayPal Checkout documentation](https://developer.paypal.com/studio/checkout/standard/getstarted) or [video tutorial](https://developer.paypal.com/video/watch/?videoId=MBfJEUGNNs0) .

# Country-specific integration options

For country-specific information about integrating Pay Later offers in your region, see the overview page for Pay Later offers for that country. For example, for information about supporting French and English sites for Canadian merchants, see [Pay Later (CA)](https://developer.paypal.com/docs/checkout/pay-later/ca/) .

Country-specific overview pages for Pay Later offers are available for the following locales:

- [United States](https://developer.paypal.com/docs/checkout/pay-later/us/)
- [Australia](https://developer.paypal.com/docs/checkout/pay-later/au/)
- [Canada](https://developer.paypal.com/docs/checkout/pay-later/ca/)
- [France](https://developer.paypal.com/docs/checkout/pay-later/fr/)
- [Germany](https://developer.paypal.com/docs/checkout/pay-later/de/)
- [Italy](https://developer.paypal.com/docs/checkout/pay-later/it/)
- [Spain](https://developer.paypal.com/docs/checkout/pay-later/es/)
- [United Kingdom](https://developer.paypal.com/docs/checkout/pay-later/gb/)

# 1. Enable Pay Later messaging on your website

Add the PayPal JavaScript SDK to your website to enable Pay Later messaging. Copy the following code and paste it in the head tag of your website. Replace CLIENT_ID with your [sandbox or production client ID](https://developer.paypal.com/dashboard/applications/sandbox) .

If you've already added the PayPal JavaScript SDK to your website, add 'messages' to components in src , as shown in the following example.

&lt;script
src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&components=messages,buttons"
data-namespace="PayPalSDK"&gt;
&lt;/script&gt;# 2. Customize and preview Pay Later messaging
Decide where you want dynamic messaging to appear and how you want it to look.

The places that you choose for displaying this option to users determines what options you have when you display the image. For more information, select one of the options from the following list.

- [Product page](#product-page)
- [Cart](#cart)
- [Checkout](#checkout)
- [Home page](#home-page)
- [Category page](#category-page)

The following topics provide some basic examples of the code to use. For more information about what you can with the messaging on these pages, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

## Product page

For messages on a product page, you can:

- Specify a logo type to use.
- Choose text and logo color formats for the message.
- Choose a text size for the message.

For examples of these options, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

Add the following code to the body of your product page to display Pay Later messaging with the specified formatting and update the data-pp-amount value.

&lt;div
data-pp-message
data-pp-style-layout="text"
data-pp-style-logo-type="inline"
data-pp-style-text-color="black"
data-pp-style-text-size="12"
data-pp-amount=ENTER_VALUE_HERE
data-pp-placement=product&gt;
&lt;/div&gt;## Cart
For messages on a cart page, you can:

- Specify a logo type to use.
- Choose text and logo color formats for the message.
- Choose a text size for the message.

For examples of these options, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

Add the following code to the body of your cart page to display Pay Later messaging with the specified formatting and update the data-pp-amount value.

&lt;div
data-pp-message
data-pp-style-layout="text"
data-pp-style-logo-type="inline"
data-pp-style-text-color="black"
data-pp-style-text-size="12"
data-pp-amount=ENTER_VALUE_HERE
data-pp-placement=cart&gt;
&lt;/div&gt;## Checkout
For messages on a checkout page, you can:

- Specify a logo type to use.
- Choose text and logo color formats for the message.
- Choose a text size for the message.

For examples of these options, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

Add the following code to the body of your checkout page to display Pay Later messaging with the specified formatting and update the data-pp-amount value.

&lt;div
data-pp-message
data-pp-style-layout="text"
data-pp-style-logo-type="inline"
data-pp-style-text-color="black"
data-pp-style-text-size="12"
data-pp-amount=ENTER_VALUE_HERE
data-pp-placement=payment&gt;
&lt;/div&gt;## Home page
For banners on a home page, you can:

- Specify a banner color theme.
- Choose a size for the banner, either 8x1 or 20x1 .

For examples of these options, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

Add the following code to the body of your home page to display Pay Later banner with the specified formatting and update the data-pp-amount value.

&lt;div
data-pp-message
data-pp-style-color="white-no-border"
data-pp-style-layout="flex"
data-pp-style-ratio="8x1"
data-pp-amount=ENTER_VALUE_HERE
data-pp-placement=home&gt;
&lt;/div&gt;## Category page
For banners on a category page, you can:

- Specify a banner color theme.
- Choose a size for the banner, either 8x1 or 20x1 .

For examples of these options, see the [Pay Later messaging reference](https://developer.paypal.com/docs/checkout/pay-later/customize/reference/) .

Add the following code to the body of your category page to display Pay Later banner with the specified formatting and update the data-pp-amount value.

&lt;div
data-pp-message
data-pp-style-color="white-no-border"
data-pp-style-layout="flex"
data-pp-style-ratio="8x1"
data-pp-amount=ENTER_VALUE_HERE
data-pp-placement=category&gt;
&lt;/div&gt;# 3. Test and go live
Save your website and publish it to start testing your Pay Later messaging. Confirm that the messages appear everywhere that you expect it to appear and that it looks and behaves as intended.

When you've tested everything, you're ready to go live.

- Change your sandbox CLIENT_ID to a production CLIENT_ID in the PayPal JavaScript SDK and in your HTML.
- If you created or updated pages on a website, move that code from the test environment to the live environment.

# Troubleshooting

Message components, console warnings, and errors include configuration attributes and object validations. Configuration properties have distinct validation checks for input formatting and values. For a full list of accepted options, see the Pay Later messaging reference.

If validation fails, the developer console in your web browser displays warning messages that tell you which property is invalid and what you should do to resolve the issue. Depending on the message type, the library will attempts to fall back to the relevant default values.
