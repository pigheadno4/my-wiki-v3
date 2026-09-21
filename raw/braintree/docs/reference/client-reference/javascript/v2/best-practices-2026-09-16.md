<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/best-practices -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Best Practices and Troubleshooting
slug: /docs/reference/client-reference/javascript/v2/best-practices/
createTime: '2025-04-02T00:09:51.344Z'
updateTime: '2025-04-02T00:09:51.415Z'
---



# Best Practices and Troubleshooting


### Script tag placement and initialization

It is best practice to place your &lt;script&gt; tag as close to the bottom of your HTML document as possible. Typically this means placing it immediately before the closing &lt;body&gt; tag.

braintree.setup() must be called after your form container element is created. If braintree.setup() runs before the container element exists, the UI may not appear.


### Optimizing for tablets and phones

If you intend on using the [Drop-in](/braintree/docs/guides/drop-in/overview/) checkout UI or customizing your existing checkout by accepting [PayPal](/braintree/docs/guides/paypal/overview), we suggest you include a viewport meta tag in the &lt;head&gt; of your website to ensure injected interfaces, such as lightboxes, display at the proper size on tablets and phones.


### HTML
```html

<meta name="viewport" content="width=device-width, initial-scale=1.0" />

```
The viewport meta tag is responsible for defining how a website behaves when it's rendered on differently sized devices.
Be sure to review your website on a tablet or phone after adding the tag to ensure it displays properly.

![Comparison,of,lightboxes,with,and,without,the,viewport,meta,tag](https://www.paypalobjects.com/btdevdoc/braintree/img/developers/pay-with-paypal/viewport-meta-tag-comparison.png)

Above are examples of a website with the viewport meta tag (left) and without the viewport meta tag (right).


### Leverage onReady

The JavaScript SDK exposes an onReady callback that will fire when your chosen integration is fully loaded and ready to be interacted with. Depending on your checkout experience and flow, you may wish to hide portions of your DOM designated for use with Braintree until this callback is received.


### Teardown

In certain scenarios you may need to remove your Braintree.js integration. This is common in single page applications, modal flows, and other situations where state management is a key factor. When calling braintree.setup, you can attach a callback to onReady which will provide an object containing a teardown method.

Invoking teardown will clean up any DOM nodes, event handlers, popups and/or iframes that have been created by the integration. Additionally, teardown accepts a callback which you can use to know when it is safe to proceed.


### JavaScript
```javascript

var checkout;
braintree.setup('CLIENT_TOKEN_FROM_SERVER', 'dropin', {
  onReady: function (integration) {
    checkout = integration;
  }
});

// When you are ready to tear down your integration
checkout.teardown(function () {
  checkout = null;
  // braintree.setup can safely be run again!
});

```
You can only invoke teardown once per.setup call. If you happen to call this method while another teardown is in progress, you'll receive an error stating Cannot call teardown while in progress. Once completed, subsequent calls to teardown will throw an error with this message: Cannot teardown integration more than once.


### Custom UI

If you wish to open the PayPal auth flow using a button other than the one provided by Braintree, you must use a combination of a [headless](/braintree/docs/reference/client-reference/javascript/v2/paypal#options) PayPal integration and the paypal.initAuthFlow method returned from the onReady callback.


### JavaScript
```javascript

var checkout;

braintree.setup('CLIENT_TOKEN_FROM_SERVER', 'custom', {
  onReady: function (integration) {
    checkout = integration;
  },
  onPaymentMethodReceived: function (payload) {
    // retrieve nonce from payload.nonce
  },
  paypal: {
    singleUse: true,
    amount: 10.00,
    currency: 'USD',
    locale: 'en_US',
    enableShippingAddress: true,
    headless: true
  }
});

// Add a click event listener to your own PayPal button
// Note: cross-browser compatibility for click handlers and events are up to you
document.querySelector('#my-button-element').addEventListener('click', function (event) {
  event.preventDefault();
  checkout.paypal.initAuthFlow();
}, false);

```

### Using Braintree.js with a Content Security Policy

[Content Security Policy](http://www.html5rocks.com/en/tutorials/security/content-security-policy/) is a feature of web browsers that mitigates cross-site scripting and other attacks. By limiting the origins of resources that may be loaded on your page, you can maintain tighter control over any potentially malicious code. While browser support is [relatively limited](http://caniuse.com/#feat=contentsecuritypolicy), we recommend considering the implementation of a CSP when available.

If you are using AJAX with CORS (by setting enableCORS to true as discussed in the [setup](/braintree/docs/reference/client-reference/javascript/v2/configuration#setup-method-options) method options), you will need to add the following directives to your policy:

|  | Sandbox | Production |
| --- | --- | --- |
| ```syntax-inline
script-src
``` | ```syntax-inline
js.braintreegateway.com
```
 ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
www.paypalobjects.com
```
 ```syntax-inline
c.paypal.com
``` | ```syntax-inline
js.braintreegateway.com
```
 ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
www.paypalobjects.com
```
 ```syntax-inline
c.paypal.com
``` |
| ```syntax-inline
style-src
``` | ```syntax-inline
'unsafe-inline'
``` | ```syntax-inline
'unsafe-inline'
``` |
| ```syntax-inline
img-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
checkout.paypal.com
```
 ```syntax-inline
data:
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
checkout.paypal.com
```
 ```syntax-inline
data:
``` |
| ```syntax-inline
child-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` |
| ```syntax-inline
frame-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
```
 ```syntax-inline
*.cardinalcommerce.com
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
```
 ```syntax-inline
*.cardinalcommerce.com
``` |
| ```syntax-inline
connect-src
``` | ```syntax-inline
api.sandbox.braintreegateway.com
```
 ```syntax-inline
client-analytics.sandbox.braintreegateway.com
```
 ```syntax-inline
*.braintree-api.com
``` | ```syntax-inline
api.braintreegateway.com
```
 ```syntax-inline
client-analytics.braintreegateway.com
```
 ```syntax-inline
*.braintree-api.com
``` |

If you're not using AJAX with CORS, you will need to add the following directives to your policy:

|  | Sandbox | Production |
| --- | --- | --- |
| ```syntax-inline
script-src
``` | ```syntax-inline
js.braintreegateway.com
```
 ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
api.sandbox.braintreegateway.com
```
 ```syntax-inline
www.paypalobjects.com
```
 ```syntax-inline
client-analytics.sandbox.braintreegateway.com
``` | ```syntax-inline
js.braintreegateway.com
```
 ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
api.braintreegateway.com
```
 ```syntax-inline
www.paypalobjects.com
```
 ```syntax-inline
client-analytics.braintreegateway.com
``` |
| ```syntax-inline
style-src
``` | ```syntax-inline
'unsafe-inline'
``` | ```syntax-inline
'unsafe-inline'
``` |
| ```syntax-inline
img-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
checkout.paypal.com
```
 ```syntax-inline
data:
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
checkout.paypal.com
```
 ```syntax-inline
data:
``` |
| ```syntax-inline
child-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` |
| ```syntax-inline
frame-src
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` | ```syntax-inline
assets.braintreegateway.com
```
 ```syntax-inline
c.paypal.com
``` |

If you are using 3D Secure, you need to setframe-srcandform-actionto*instead.


### Bypass submit handlers

By default, Braintree.js attaches handlers to the submit action of your form. While this feature itself is not configurable, you may find yourself wanting to submit your form without triggering our handlers. This is a common practice when subscribed to the onPaymentMethodReceived callback. When you wish to submit your form, you can invoke its native submit action like so:


### JavaScript
```javascript

var form = document.getElementById('my-form');
HTMLFormElement.prototype.submit.call(form);

```
If you are using a form that has no button to click, you can create your own event to submit:


### JavaScript
```javascript

var form = document.getElementById('my-form');
var e = document.createEvent('Event');

e.initEvent('submit', true, true);
form.dispatchEvent(e);

```
