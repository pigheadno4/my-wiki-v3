<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-later/customize/advanced-js-options/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Advanced JavaScript options
slug: /docs/checkout/pay-later/customize/advanced-js-options/
createTime: '2025-11-03T08:00:01.414Z'
updateTime: '2025-11-05T10:05:12.399Z'
---


# Advanced JavaScript options
     Advanced JavaScript Options 

Pay Later messaging relies on the messages component in the JavaScript SDK. You can integrate the messages component in a variety of ways. The following sections discuss some of the different ways you can configure and use the SDK.

Your options include:

- [Configuring the component using JavaScript](#configure-using-javascript)
- [Using event hooks](#use-event-hooks)
- [Using namespace attributes](#use-namespace-attributes)
- [Rendering multiple messages](#render-multiple-messages)
- [Updating messages without reloading the page](#update-messages-without-reloading-the-page)
- [Integrating into a single-page app](#integrate-into-a-single-page-app)

# Configure using JavaScript
You can configure and display Pay Later messages using JavaScript as an alternative to HTML attributes. The JavaScript SDK messages component uses an API that is similar to the API that the buttons component uses.

The following code sample shows how to create a message object by calling the paypal.Messages function. The paypal.Messages function takes a configuration object as its only argument and returns a message object.

The message object has a render() function that accepts an argument that defines the element in which messages are rendered. In this example, .pp-message is a CSS selector string, but you also can use an HTMLElement reference, or an array of HTMLElement references.

&lt;head&gt;
  &lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class="pp-message"&gt;&lt;/div&gt;
  &lt;script&gt;
    paypal
      .Messages({
        amount: 500,
        pageType: "product-details",
        style: {
          layout: "text",
          logo: {
          type: "inline",
          },
        },
      })
      .render('.pp-message');
  &lt;/script&gt;
&lt;/body&gt;In the code sample:

- The amount is set to 500.
- The message is added to the details of a product, so pageType: "product-details" is added to the configuration object.
- The message uses a text layout with a primary logo on top of the message.

The SDK renders the message inside any element that contains a class attribute with the value .pp-message.

The configuration object accepted by the Messages function mirrors the HTML attributes that are parsed and read from the elements targeted for messages. For example, data-pp-style-layout is the same as the configuration object path of style.layout. See the [reference](https://developer.paypal.com/studio/checkout/pay-later/us/customize/reference) to view all the configuration settings and their associated attributes and object keys.

**Note:** Both inline attributes and the JavaScript configuration object can be used independently or combined to change the message configuration. If there are conflicting settings, the inline HTML attribute setting overrides the JavaScript configuration object setting.

# Use event hooks
The messages component of the PayPal JavaScript API lets you to pass in callback functions. Certain events trigger these callback functions. The available events to hook into are onRender , onClick , and onApply .

| Event | Description |
| --- | --- |
| onRender | Invoked after each message renders into the DOM |
| onClick | Invoked after a user selects the message |
| on Apply | Invoked after a user selects the Apply button or link in the pop-up modal |

One common use case for event hooks is to send data to your own analytics platform. For example, you might have your own custom data processing, or you might use a third-party analytics provider.

To add logic to these event hooks, add a function to the associated key of the configuration object you pass to paypal.Messages() .

The following code sample calls the paypal.Messages function to create a message object with optional properties for onRender , onClick , and onApply . When any of these events happens, it triggers the associated callback function. The console log includes the following message when this happens: Callback called on render .

&lt;head&gt;
  &lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class="pp-message"&gt;&lt;/div&gt;
  &lt;script&gt;
    paypal
      .Messages({
        amount: 500,
        pageType: "product-details",
        style: {
          layout: "text",
          logo: {
            type: "inline",
          },
        },
        onRender: () =&gt; {
          console.log("Callback called on render");
          // such as send a "render event" to your analytics platform.
        },
        onClick: () =&gt; {
          console.log("Callback called on click");
          // such as send a "click event" to your analytics platform.
        },
        onApply: () =&gt; {
          console.log("Callback called on apply");
          // such as send an "apply event" to your analytics platform.
        },
      })
      .render('.pp-message');
  &lt;/script&gt;
&lt;/body&gt;# Use namespace attributes
If you're using a [legacy](https://developer.paypal.com/docs/archive/lifecycle/) integration for PayPal Checkout, you might be using the data-namespace attribute when you load the PayPal JavaScript SDK messages component.

If you configure messages using JavaScript, the value you set for data-namespace is the name of the global variable that you use to configure and render messages. This example uses "PayPalSDK" in data-namespace .

&lt;head&gt;
  &lt;script
    data-namespace="PayPalSDK"
    src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"
  &gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class="pp-message"&gt;&lt;/div&gt;
  &lt;script&gt;
    PayPalSDK.Messages({
      amount: 500,
      style: {
        layout: "text",
        logo: {
          type: "inline",
        },
      },
    }).render('.pp-message');
  &lt;/script&gt;
&lt;/body&gt;For more information about namespaces and compatibility with Checkout integrations, see [Upgrade existing integration](https://developer.paypal.com/docs/checkout/pay-later/us/upgrade-options/) .

# Render multiple messages
The SDK renders a message into any element with a data-pp-message attribute or elements that match the target that you defined in the JavaScript configuration with the Messages() function. If the inline HTML attributes and the JavaScript configuration are different, the SDK uses the inline elements.

You can use both inline attributes and JavaScript. For example, you can use the JavaScript configuration to declare shared or common settings, while you can use inline attributes to customize a specific message.

&lt;head&gt;
  &lt;script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=messages"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
  // Example list of products
  &lt;ul class="listings"&gt;
    &lt;li class="listing"&gt;
      &lt;div class="listing__content"&gt;
        &lt;div class="listing__title"&gt;Product Name 1&lt;/div&gt;
        &lt;div class="listing__price"&gt;$50&lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="pp-message"&gt;
        // Pay Later message will be inserted here
      &lt;/div&gt;
    &lt;/li&gt;
    &lt;li class="listing"&gt;
      &lt;div class="listing__content"&gt;
        &lt;div class="listing__title"&gt;Product Name 2&lt;/div&gt;
        &lt;div class="listing__price"&gt;$100&lt;/div&gt;
      &lt;/div&gt;
      &lt;div class="pp-message"&gt;
        // Pay Later message will be inserted here
      &lt;/div&gt;
    &lt;/li&gt;
  &lt;/ul&gt;
  &lt;script&gt;
    // Grab all product listings on the page
    const listings = Array.from(document.querySelectorAll(".listing"));
    // Loop through each product listing
    listings.forEach((listing) =&gt; {
      // Extract the price of the product by grabbing the text content of the
      // element that contains the price. Use .slice(1) to remove the leading
      // $ sign
      const price = Number(
        listing.querySelector(".listing__price").textContent.slice(1)
      );
      // Grab child element of this .listing element that has the
      // pp-message classname
      const messageElement = listing.querySelector('.pp-message');
      // Set data-pp-amount on this element. The PayPal SDK monitors
      // message elements for changes to its attributes, so the
      // message is updated automatically to reflect this amount.
      messageElement.setAttribute("data-pp-amount", price);
    });
    // Render all Pay Later messages
    paypal
      .Messages({
        style: {
          layout: "text",
          logo: {
            type: "primary",
            position: "top",
          },
        },
      })
      .render('.pp-message');
  &lt;/script&gt;
&lt;/body&gt;# Update messages without reloading the page
The SDK's messages component attaches observers to all attributes that start with data-pp on DOM elements that it targets with messages.

Changing an attribute can change data-pp-amount from 100 to 200 to reflect a change, such as when a customer updates an item's quantity in their cart. Don't call the render() function again when this happens, because the SDK automatically detects the change and renders a new message if necessary. However, if new HTML content is dynamically injected to the document, and you want to render a message inside this new HTML, call the render() function of paypal.Messages again.

# Integrate into a single-page app
The JavaScript SDK should only be loaded once. In many cases, you should add the &lt;script/&gt; tag into the &lt;head/&gt; of your main HTML document into which you inject your client-side app. This HTML is often called index.html.

Do not reload the SDK on state changes or router updates. If the state or routes in your SPA change enough to render new content and new messages, invoke paypal.Messages.render() again, and specify the new targets for the messages.

# See also
- For more information, see the [reference](https://developer.paypal.com/studio/checkout/pay-later/customize/reference) for this SDK.
- For information about supporting Pay Later for Canadian merchants, see [Pay Later (CA)](/docs/checkout/pay-later/ca/)
