---
title: JavaScript SDK performance optimization
slug: /sdk/js/performance/
createTime: "2024-08-15T06:13:41.217Z"
updateTime: "2025-12-17T14:26:25.665Z"
---

# JavaScript SDK performance optimization

**Important:**This documentation covers the JavaScript SDK v2 with theCardFieldscomponent. For the legacy v1 SDK usingHostedFields, see the[Version 1](/sdk/js/v1/reference/)documentation.

Optimize loading the JavaScript SDK and rendering the payment buttons for the best performance.

## Load the JavaScript SDK from the PayPal server

Load the JavaScript SDK from https://www.paypal.com/sdk/js only. Reasons include:

- The script is dynamically bundled, based on your client ID and the current buyer. It includes only the specific code, images, localization, and other resources needed and does not slow down your page with unnecessary code. This approach is not possible with a statically-distributed script.
- The script loads inside the button iframe and Checkout popup window to communicate with the parent window. Loading from paypal.com means your users' browsers cache the script and there is no need to download the script again inside the iframe or popup.
- Security updates and bug fixes are instantly available to your users.
- Conversion updates to drive extra sales and revenue through PayPal are instantly available.
- Backwards compatibility with previous versions of the script.

## Minified script

The script is minified by default. While you're developing, you can disable minified script, by adding debug=true to the script URL.

## Instant render

If you are rendering the payment buttons immediately on the page after it loads, you should:

- Load the JavaScript SDK prior to the element you want to render into:

&lt;script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID"&gt;&lt;/script&gt;

- Call paypal.Buttons().render('#container') as soon as possible when the container element is ready:

&lt;div id="paypal-button-container"&gt;&lt;/div&gt;

&lt;script&gt;
paypal.Buttons().render('#paypal-button-container')
&lt;/script&gt;

- For a bonus performance boost, load the JavaScript SDK asynchronously on a page that precedes the checkout page. This approach pre-caches the script, making future loads and renders instantaneous:

&lt;!-- Place on one of your landing pages or pre-checkout pages --&gt;
&lt;body&gt;
&lt;script
src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID" async&gt;
&lt;/script&gt;
&lt;/body&gt;

## Delayed render

If your app renders on the client-side, or there is a user action on the page that triggers displaying the payment buttons (like opening a cart or selecting a radio button), you should:

- Load the JavaScript SDK asynchronously in your page:

&lt;head&gt;
&lt;script src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID"&gt;&lt;/script&gt;
&lt;/head&gt; Alternatively, use JavaScript to asynchronously load the script:

var PAYPAL_SCRIPT = 'https://www.paypal.com/sdk/js?client-id=CLIENT_ID';
var script = document.createElement('script');
script.setAttribute('src', PAYPAL_SCRIPT);
document.head.appendChild(script);

- Call paypal.Buttons().render('#container') on the client-side render, route change, or user action that you want to trigger displaying the button:

&lt;div id="paypal-button-container"&gt;&lt;/div&gt;

&lt;script&gt;
document.querySelector('#myRadioField')
.addEventListener('click', function() {
paypal.Buttons().render('#paypal-button-container')
});
&lt;/script&gt; Alternatively, to ensure the button completely loads by the time it displays, render the button in advance in a hidden container, and display it on the page change or user action:

&lt;div id="paypal-button-container"&gt;&lt;/div&gt;

&lt;script&gt;
document.querySelector('#paypal-button-container')
.style.display = 'none';

paypal.Buttons().render('#paypal-button-container');

document.querySelector('#myRadioField')
.addEventListener('click', function() {
document.querySelector('#paypal-button-container')
.style.display = 'block';
});
&lt;/script&gt;

## Load the SDK as a module

Loading the SDK as a module brings certain advantages, especially when working with [single page applications](/docs/checkout/standard/customize/single-page-app/) . For example, you can optimize performance because the module lets you control loading behavior in JavaScript instead of HTML. It can also help reduce bugs by encapsulating data.

- Use the [paypal-jsnpm package](https://www.npmjs.com/package/@paypal/paypal-js) to integrate with front-end build tools. This package follows best practices such as loading the script asynchronously and providing a promise interface to know when script loading is complete.

- Use the [react-paypal-jsnpm package](https://www.npmjs.com/package/@paypal/react-paypal-js) within the React.js framework. It brings the same functionality as the paypal-js package, but tailored to the style of the framework. It ships React.js components for Buttons, Marks, and Messages on top.

See the projects' README.md documentation for further details.

## See also

- [JavaScript SDK complete reference](/docs/business/javascript-sdk/javascript-sdk-reference/) .
- [JavaScript SDK script configuration](/docs/business/javascript-sdk/javascript-sdk-configuration/) .
