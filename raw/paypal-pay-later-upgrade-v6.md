<!-- Source URL: https://docs.paypal.ai/payments/methods/pay-later/upgrade -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Pay Later to SDK v6

Use this guide to upgrade Pay Later messaging from the JavaScript SDK v5 to v6.

> **Tip:** You don't have to upgrade other PayPal components, such as PayPal Checkout, before you upgrade Pay Later messaging. To upgrade everything, follow [this guide](/developer/upgrade/sdk/js/v5-v6) first.

## Pay Later messaging features in SDK v6

Among the other [benefits of SDK v6](/developer/upgrade/sdk/js/v5-v6#compare-v5-and-v6), it brings these important features to Pay Later messaging:

- Support for local, CDN, and site caching for faster content visibility
- An auto-bootstrap feature for easy integration
- Customizable logo types, text sizes, logo positions, offer types, presentation modes, and caching types
- More visibility for improved analytics and diagnostics
- Support for passing customizations through the HTML component, JavaScript, or both through `getFetchContentOptions`
- Support for flexible authentication using a client ID or a server-side client token
- Improved performance

## Upgrade Pay Later messaging to SDK v6

Pay Later messaging is a component of PayPal's SDK v6. To upgrade Pay Later messaging to SDK v6, you must first upgrade the core SDK.

### 1. Import the SDK and the `messages` script

The SDK v5 script uses a `client-id` value. It also specifies which components to use. For example, this code sample uses the `messages` and `buttons` components.

```html lines theme={null}
<script
  src="https://www.sandbox.paypal.com/sdk/js?client-id=CLIENT_ID&components=messages,buttons"
  data-namespace="PayPalSDK"
></script>
```

SDK v6 supports 2 authentication types. Choose the one that best fits your integration:

- `clientId`: Pass your PayPal client ID directly to `createInstance()` with no server-side token generation required.
- `clientToken`: Generate a client token on the server side using your [client ID and client secret](https://docs.paypal.ai/developer/how-to/api/get-started#1-get-your-client-id-and-client-secret), then pass it to `createInstance()`. For more information, see [Set up JavaScript SDK v6](/developer/how-to/sdk/js/v6/configuration).

> **Tip:** If you followed the [general upgrade guide for SDK v6](/developer/upgrade/sdk/js/v5-v6/) and have the SDK core script, you only need to add `paypal-messages` to the components list when you initialize the SDK, as shown in the following example.

```javascript lines theme={null}
// Option 1: Using clientId (no server-side token generation required)
const sdkInstance = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  components: ["paypal-payments", "venmo-payments", "paypal-messages"],
  pageType: "checkout",
});

// Option 2: Using clientToken (requires server-side token generation)
const sdkInstance = await window.paypal.createInstance({
  clientToken,
  components: ["paypal-payments", "venmo-payments", "paypal-messages"],
  pageType: "checkout",
});
```

After you import the resources using HTML, use JavaScript to initialize the SDK and instantiate `web-sdk-messages`, as shown in the following examples.

<CodeGroup>
  ```html lines HTML  theme={null}
  <head>
    <!-- Load just the v6 SDK Core script -->
    <script src="https://www.paypal.com/web-sdk/v6/core"></script>
  </head>
  ```

```javascript lines expandable JavaScript theme={null}
// Instantiate the SDK Instance, and specify paypal-messages as a component
const sdkInstance = await window.paypal.createInstance({
  clientId: "YOUR_CLIENT_ID",
  // Include paypal-messages in the components to load
  components: ["paypal-messages"],
});

// Instantiate web-sdk-messages
const messagesInstance = sdkInstance.createPayPalMessages({
  buyerCountry: "US",
});
```

</CodeGroup>

### 2. Create a container element for Pay Later messaging

Create a container element in your HTML to display the Pay Later messaging.

PayPal's SDK v5 created an element with a truthy attribute, `data-pp-message`, or you could fetch content from `paypal.Messages` in JavaScript and render it to any `div` element dynamically. In contrast, SDK v6 uses a custom Lit component called `paypal-message`. You can use this component in place of a `div` element to support more sophisticated HTML formatting, such as auto-bootstrap layouts. It also makes it easier to encapsulate the element from its containing page, provides better visibility into the lifecycle of the component, and improves reusability.

Treat `paypal-message` as a custom HTML element. The minimum requirement after you import the scripts is to include this element in your HTML.

```html theme={null}
<paypal-message></paypal-message>
```

The `paypal-message` element provides optional, customizable attributes for adjusting the logo type, logo position, and more. It also includes a boolean `auto-bootstrap` attribute that simplifies how you connect `fetchContent` and `learnMore` calls, eliminating the need to include them in your JavaScript.

For more information about setting up your integration, see [Get started with Pay Later](/payments/methods/pay-later/get-started).

### 3. Configure Pay Later messaging

You have 2 configuration options for SDk v6:

- For a streamlined approach, use the customizable `auto-bootstrap` option.
- If you do not use the `auto-bootstrap` option, use the PayPal `Messages` JavaScript interface. This interface provides 2 instance methods:
  - `fetchContent` (required)
  - `createLearnMore` (optional)

Similar to SDK v5, SDK v6 also allows you to pass your configuration through HTML or JavaScript. However, SDK v6 also enables you to pass configurations through both HTML attributes and JavaScript properties.

For more information about customizing your message and configuring with `auto-bootstrap` or JavaScript, see [Get started with Pay Later](/payments/methods/pay-later/get-started).
