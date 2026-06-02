---
title: Pay Later messaging reference
slug: /docs/checkout/pay-later/customize/reference/
createTime: "2025-11-03T08:22:13.233Z"
updateTime: "2026-02-02T08:37:26.853Z"
---

# Pay Later messaging reference

     Pay Later messaging reference

#

The following reference topics describe how to customize Pay Later messaging in your code. For more information about Pay Later offers, see the Pay Later overview page for your country, such as [Pay Later (US)](/checkout/pay-later/us)

# Script query parameters

Pass these parameters to the JavaScript SDK script URL as the query parameters for Pay Later messaging.

For the full set of PayPal script parameters, see [JavaScript SDK script configuration](https://developer.paypal.com/sdk/js/configuration) .

| Parameter                   | Description                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| client-id                   | ID of the client's PayPal account                                                                                                                                                                                                                                                    |
| merchant-id                 | ID of the merchant when you're acting on behalf of a merchant. Only required if you act on behalf of a merchant.                                                                                                                                                                     |
| data-partner-attribution-id | Also known as your**BN code**. PayPal issues yourdata-partner-attribution-idduring onboarding.                                                                                                                                                                                       |
| data-namespace              | Name that you use as a global variable when the SDK loads. This value is required only if you're using a legacy checkout integration, such ascheckout.js. It can be any string, exceptpaypal. For the example in the sample code, you invokePayPalSDK.Messages()in your integration. |

&lt;script
src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&merchant-id=MERCHANT_ID&components=messages"
data-partner-attribution-id="BN_CODE"
data-namespace="PayPalSDK"
&gt;&lt;/script&gt;# Messages function
The Message object configures the layout and style for Pay Later messaging. To create a Message object, invoke paypal.Messages .

# Message object

The Message object contains the following properties.

| Property | Type     | Description                                                                                                                                                                                                                                                       |
| -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| render   | Function | Tells the system where and how to render the Pay Later messages. Therenderproperty Accepts a valid CSS selector string, a singleHTMLElementreference, or an array ofHTMLElementreferences. It returns aPromisethat resolves after all messages render to the DOM. |

# Message configuration object

The following table lists all configuration properties that you can set on the configuration object. The [Messagesfunction](#messages-function) uses the properties in this object to configure your messages.

All properties have equivalent HTML custom attributes, which you can add inline on the HTML elements that you target for messages.

**Note:** Properties that you define using HTML attributes for a given message value override duplicate properties that you set using the configuration object and the paypal.Messages function.

## amount

Product price or cart amount in dollars. For example, pass $598.94 as 598.94 . We strongly recommended using this property.

| Value type | Value                              |
| ---------- | ---------------------------------- |
| Number     | Any number with 0-2 decimal places |

**Note:** The inline HTML attribute for this property is data-pp-amount .

## currency

Buyer's currency code

| Value type | Value | Description       |
| ---------- | ----- | ----------------- |
| String     | USD   | US dollar         |
|            | GBP   | British pound     |
|            | EUR   | Euro              |
|            | AUD   | Australian dollar |

**Note:** The inline HTML attribute for this property is data-pp-currency .

## language

Language to use when rendering the site. This setting is specific to Canadian merchant sites.

| Value type | Value                                                                                                                                                           |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| String     | Uselanguage=“en-CA"on your English site andlanguage="fr-CA"on your French site. Any other value or a missing attribute uses the default value:language="en-CA". |

**Note:** For more information about supporting Pay Later for Canadian merchants, see [Pay Later (CA)](/docs/checkout/pay-later/ca/) .

## style.layout

Overall style or type of message

| Value type | Value | Description                                 |
| ---------- | ----- | ------------------------------------------- |
| String     | text  | Lightweight contextual message**(Default)** |
|            | flex  | Responsive banner                           |

**Note:** The inline HTML attribute for this property is data-pp-style-layout .

## style.logo.type

Type of logo to use in messages that have the text value for style.layout

| Value type | Value       | Description                                                  |
| ---------- | ----------- | ------------------------------------------------------------ |
| String     | primary     | Single-line PayPal or PayPal Credit logo**(Default)**        |
|            | alternative | PP monogram or PP Credit logo                                |
|            | inline      | Same asprimary, but inline with the content**(Recommended)** |
|            | none        | No logo, text only                                           |

**Note:** The inline HTML attribute for this property is data-pp-style-logo-type .

## style.logo.position

Position of the logo, relative to the message content, to use in messages that have the text value for style.layout and primary or alternative for style.logo.type

| Value type | Value | Description                                       |
| ---------- | ----- | ------------------------------------------------- |
| String     | left  | Logo appears to the left of the text**(Default)** |
|            | right | Logo appears to the right of the text             |
|            | top   | Logo appears above the text                       |

**Note:** The inline HTML attribute for this property is data-pp-style-logo-position .

## style.text.color

The color of the text and logo to use in messages that have the text value for style.layout

| Value type | Value      | Description                                 |
| ---------- | ---------- | ------------------------------------------- |
| String     | black      | Black text with a colored logo**(Default)** |
|            | white      | White text with a white logo                |
|            | monochrome | Black text with a black logo                |
|            | grayscale  | Black text with a grayscale logo            |

**Note:** The inline HTML attribute for this property is data-pp-style-text-color .

## style.text.size

Font size to use in messages that have the text value for style.layout

| Value type | Value       | Description                     |
| ---------- | ----------- | ------------------------------- |
| Number     | 10,11       | Smaller text sizes              |
|            | 12          | Standard text size**(Default)** |
|            | 13,14,15,16 | Larger texts sizes              |

**Note:** The inline HTML attribute for this property is data-pp-style-text-size .

## style.text.align

Alignment to use in messages that have the text value for style.layout

| Value type | Value  | Description                          |
| ---------- | ------ | ------------------------------------ |
| String     | left   | Aligns text at the left**(Default)** |
|            | center | Centers text                         |
|            | right  | Aligns text at the right             |

**Note:** The inline HTML attribute for this property is data-pp-style-text-align .

## style.color

Background color to use for messages that have the flex value for style.layout

| Value type | Value           | Description                                                                      |
| ---------- | --------------- | -------------------------------------------------------------------------------- |
| String     | blue            | Blue background with white text and a white logo**(Default)**                    |
|            | black           | Black background with white text and a white logo                                |
|            | white           | White background with blue text, a colored logo, and a blue border               |
|            | white-no-border | White background with blue text and a colored logo and no border for the message |
|            | gray            | Light gray background with blue text and a colored logo                          |
|            | monochrome      | White background with black text and a black logo                                |
|            | grayscale       | White background with black text and a grayscale logo                            |

**Note:** The inline HTML attribute for this property is data-pp-style-color .

## style.ratio

Ratio to use for messages that have the flex value for style.layout

| Value type | Possible value | Description                                                     |
| ---------- | -------------- | --------------------------------------------------------------- |
| String     | 1x1            | 1x1 ratio that flexes between 120px and 300px wide**(Default)** |
|            | 1x4            | 1x4 ratio that is 160px wide                                    |
|            | 8x1            | 8x1 ratio that flexes between 250px and 768px                   |
|            | 20x1           | 20x1 ratio that flexes between 250px and 1129px wide            |

**Note:** The inline HTML attribute for this property is data-pp-style-ratio .

## pageType

Informs PayPal's analytics and system logging of the type of page on which you put the message

| Value type | Possible value  | Description                                       |
| ---------- | --------------- | ------------------------------------------------- |
| String     | home            | Message is on the home page of the ecommerce site |
|            | product-listing | Message is on the product listing page            |
|            | product-details | Message is on the product details page            |
|            | search-results  | Message is on the search results page             |
|            | cart            | Message is on the cart page                       |
|            | mini-cart       | Message is on the mini-cart page                  |
|            | checkout        | Message is on the checkout page                   |

**Note:** The inline HTML attribute for this property is data-pp-pageType .

## contextualComponents

Visual design and content of the message that you can use to match it to an adjacent component. Use contextualComponents when you place the message near checkout buttons or near a PayPal or Pay Later logo or mark.

**Note:** Using one of the \*\_MARK values that appear in the following table overrides some other style properties, such as the properties for a logo, for example, style.logo.position .

| Value type | Possible value   | Description                                                                             |
| ---------- | ---------------- | --------------------------------------------------------------------------------------- |
| String     | PAYPAL_BUTTON    | Messages feature both PayPal and Pay Later and use the PayPal monogram logo by default. |
|            | PAY_LATER_BUTTON | Messages feature PayLater only and use the PayPal monogram logo by default.             |
|            | PAYPAL_MARK      | Messages feature both PayPal and Pay Later and do not include a PayPal logo.            |
|            | PAY_LATER_MARK   | Messages feature only PayPal Pay Later and do not include a PayPal logo.                |

**Note:** The inline HTML attribute for this property is data-pp-contextualComponents .

## onApply

Callback function that an app calls when a user selects an **Apply** link or button in the pop-up modal.

**Note:** The inline HTML attribute for this property is data-pp-onapply .

## onClick

Callback function that an app calls when a user selects a message.

**Note:** The inline HTML attribute for this property is data-pp-onclick .

## onRender

Callback function that an app calls when a messages finishes rendering into the DOM.

**Note:** The inline HTML attribute for this property is data-pp-onrender .
