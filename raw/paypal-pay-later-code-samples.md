---
title: Code samples for Pay Later integration
slug: /docs/checkout/pay-later/customize/code-samples/
createTime: "2025-11-03T11:19:23.626Z"
updateTime: "2025-11-06T11:14:48.280Z"
---

# Code samples for Pay Later integration

     Pay Later upgrade options

# Pay Later upgrade options

To add Pay Later messaging to an existing PayPal integration, choose one of these options:

- [Upgrade to a JavaScript SDK integration](#upgrade-to-a-javascript-sdk-integration)
- [Add Pay Later to an existing integration](#add-pay-later-to-an-existing-integration)

# Upgrade to a JavaScript SDK integration

To add Pay Later offers to a legacy integration, you add a &lt;script /&gt; tag where you want to render messages. These steps upgrade an existing PayPal integration to the latest JavaScript SDK. The new code keeps you current with messages, features, and styles.

To upgrade:

- Remove the legacy &lt;script /&gt; tags that you're currently using for PayPal messages.
- Add the PayPal JavaScript SDK in a &lt;script&gt; element with the messages component within the &lt;head&gt; element of your page, as shown in the following example. &lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;
- Add &lt;div&gt; elements with the necessary attributes inside the &lt;body&gt; of your document where you want to render messages. For more information, see [Customize Pay Later messaging](https://developer.paypal.com/docs/checkout/pay-later/us/integrate/customize-messages/) .

## Legacy JavaScript integration upgrade options

There are two ways to upgrade legacy .js integrations, depending on how you previously integrated. Review the following integration options to identify your integration, then select the tab that matches your integration to view upgrade instructions:

- Use &lt;script /&gt; tags to load a merchant.js file from a domain. For more information about this option, see [Use script tags](#use-script-tags) .
- Load assets directly from //www.paypalobjects.com/upstream/bizcomponents/js/merchant.js , ad.where.com/jin/spotlight/ads , or paypal.adtag.where.com . For more information about this option, see [Load assets directly](#load-assets-directly) .

### Use script tags

To upgrade:

- Remove the &lt;script /&gt; tags that load the merchant.js file.
- Add the PayPal JavaScript SDK to the &lt;head&gt; element of your site.
- Add &lt;div&gt; elements with the necessary attributes inside the &lt;body&gt; of your document where you want to render messages. For more information, see [Customize Pay Later messaging](https://developer.paypal.com/docs/checkout/pay-later/us/integrate/customize-messages/) .

**Note:** The value for data-pp-payerid or data-pp-pubid is a PAYER_ID . This is not the client ID that you use to load the JavaScript SDK. For more information about your client ID, see [Get started with PayPal REST APIs](https://developer.paypal.com/api/rest/) .

&lt;script type="text/javascript" data-pp-payerid="PAYER_ID"&gt;
(function (d, t) {
var s = d.getElementsByTagName(t)[0],
n = d.createElement(t);
n.src = "//www.paypalobjects.com/upstream/bizcomponents/js/merchant.js";
s.parentNode.insertBefore(n, s);
})(document, "script");
&lt;/script&gt;### Load assets directly
In this integration, you directly load assets from ad.where.com/jin/spotlight/ads , //www.paypalobjects.com/upstream/bizcomponents/js/merchant.js , or paypal.adtag.where.com .

To upgrade:

- Remove the &lt;script /&gt; tags that load the merchant.js file.
- Add the PayPal JavaScript SDK to the &lt;head&gt; element of your site.
- Add &lt;div&gt; elements with the necessary attributes inside the &lt;body&gt; of your document where you want to render messages. For more information, see [Customize Pay Later messaging](https://developer.paypal.com/docs/checkout/pay-later/us/integrate/customize-messages/) .

**Note:** The value that you supply in this integration is not the client ID that you use to load the JavaScript SDK. For more information about your client ID, see [Get started with PayPal REST APIs](https://developer.paypal.com/api/rest/) .

To load assets from ad.where.com/jin/spotlight/ads , use the following script:

&lt;script type="text/javascript"&gt;
document.write("&lt;scr");
document.write(
'ipt type="text/javascript" data-ppmnid="92820893359741" src="//ad.where.com/jin/spotlight/ads?pubid= K94SASJJZDBBQ&format=js&v=2.4&placementtype=120x90&ppmnid=92820893359741&rand=' +
Math.round(Math.random() \* 100000000000000) +
'"&gt;'
);
document.write("&lt;/scr" + "ipt&gt;");
&lt;/script&gt;To load assets from /upstream/bizcomponents/js/merchant.js , use the following script:

&lt;script type="text/javascript" data-pp-payerid="YOUR_PAYER_ID"&gt;
(function (d, t) {
var s = d.getElementsByTagName(t)[0],
n = d.createElement(t);
n.src = "//www.paypalobjects.com/upstream/bizcomponents/js/merchant.js";
s.parentNode.insertBefore(n, s);
})(document, "script");
&lt;/script&gt;To load assets from paypal.adtag.where.com subdomain , use the following script:

&lt;script type="text/javascript" data-pp-pubid="YOUR_PAYER_ID"&gt;
(function (d, t) {
var s = d.getElementsByTagName(t)[0],
n = d.createElement(t);
n.src = "//paypal.adtag.where.com/merchant.js";
s.parentNode.insertBefore(n, s);
})(document, "script");
&lt;/script&gt;# Add Pay Later to an existing integration
You can use the PayPal JavaScript SDK messages component with other components of the SDK to integrate with many PayPal features and services simultaneously. You can also use PayPal JavaScript SDK messages independently on pages that need only the Pay Later messaging.

The PayPal JavaScript SDK is also compatible with older versions of PayPal checkout integrations, such as checkout.js, the immediate predecessor to the PayPal JavaScript SDK. To use the SDK on the same page as checkout.js , you must include the data-namespace attribute on the &lt;script /&gt; tag.

The following topics provide some examples of common integration scenarios. Use these examples to identify and plan your upgrade.

**Note:** Many integrations that do not use the JavaScript SDK are [legacy](https://developer.paypal.com/docs/archive/lifecycle/) integrations. In those cases, we recommended that you update your checkout integration to use the PayPal JavaScript SDK and use components=buttons,messages as described in earlier examples.

## Pages with no other PayPal integrations

Use this approach on pages that have no existing PayPal integrations. In this scenario, you'd like to add messages to a page that has no other PayPal integrations. To do this, set the value of the components= parameter to messages in the &lt;script /&gt; tag's src attribute.

&lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;## Pages that use the SDK buttons component
Use this method for pages that use the buttons component from the PayPal JavaScript SDK. In this type of integration, you used the PayPal JavaScript SDK to add PayPal checkout buttons to your site already. You'd like to add Pay Later messages now. To do this, you add the messages component to the components= parameter in the &lt;script /&gt; tag's src attribute. Use a comma to separate individual components.

&lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,messages"&gt;&lt;/script&gt;## Legacy PayPal checkout.js
For pages with a legacy PayPal checkout.js integration, use this type of upgrade to add Pay Later messaging.

Because this is a [legacy](https://developer.paypal.com/docs/archive/lifecycle/) integration, we recommended that you update your checkout integration to use the PayPal JavaScript SDK and use components=buttons,messages , as shown in earlier examples. However, if you're unable to upgrade to the SDK but want to use Pay Later features, keep your checkout.js script and add a new script for the PayPal JavaScript SDK with the data-namespace attribute set to "PayPalSDK" .

For more information about advanced JavaScript message configuration, see the [Advanced JavaScript options](https://developer.paypal.com/docs/checkout/pay-later/us/integrate/advanced-js-options/) for Pay Later.

&lt;script src="https://www.paypalobjects.com/api/checkout.js"&gt;&lt;/script&gt;
&lt;script
data-namespace="PayPalSDK"
src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"
&gt;&lt;/script&gt;When you configure messages using JavaScript, the value that you set for data-namespace is the name of the global variable that you use to configure and render messages.

&lt;head&gt;
&lt;!--
Whatever you use for data-namespace, you have to use below
when configuring and rendering the messages
--&gt;
&lt;script
data-namespace="PayPalSDK"
src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"
&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;div class="pp-message"&gt;&lt;/div&gt;

&lt;script&gt;
// PayPalSDK is used here because this is the value we used above
// for the data-namespace attribute in the &lt;script /&gt; tag
PayPalSDK.Messages({
amount: 500,
style: {
layout: "text",
},
}).render('.pp-message');
&lt;/script&gt;
&lt;/body&gt;## Legacy PayPal REST API or static button
For the following types of integrations, you might use this option. For these pages, you can include the PayPal JavaScript SDK with only the messages component on your page without affecting your existing button integration.

- Pages with a [legacy](https://developer.paypal.com/docs/archive/lifecycle/) PayPal REST API
- Pages that use static buttons, such as an HTML form that has a static button image

&lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;
