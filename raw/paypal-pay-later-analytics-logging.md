<!-- Source URL: https://docs.paypal.ai/payments/methods/pay-later/analytics-logging -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Analytics logging

Use callback functions in the PayPal Messages SDK to monitor key user interactions and rendering events for your <a href="https://docs.paypal.ai/payments/methods/pay-later/overview" target="_blank">Pay Later</a> integration. The data you collect about critical events and user interactions helps optimize your payment flow.

The following example renders a message using a JavaScript configuration. This example includes `console.log` statements in many of the configuration callback functions and events. The functions in this example log in the console when an event occurs.

For details about how to log when a custom event or hook occurs, see your analytics platform's documentation. You can put that code in the function body of the event hook properties for the Fetch Content or Learn More configuration objects. For more information about these configuration objects, see [Get started with Pay Later](/payments/methods/pay-later/get-started).

```html theme={null}
<head>
  <script src="https://www.paypal.com/web-sdk/v6/core"></script>
  <script src="https://www.paypal.com/web-sdk/v6/paypal-messages"></script>
</head>
<body>
  <paypal-message></paypal-message>
  <script>
    const sdkInstance = await window.paypal.createInstance({ clientId: "YOUR_CLIENT_ID" });
    const messagesInstance = sdkInstance.createPayPalMessages();
    const content = await messagesInstance.fetchContent({
      amount: "300.00",
      currencyCode: "USD",
      logoType: "MONOGRAM",
      textColor: "MONOCHROME",
      onTemplateReady: (content) => {
        // ANALYTICS LOG EXAMPLE
        console.log("Cached Template Rendered");
        messageElement.setContent(content);
      },
      onContentReady: (content) => {
        // ANALYTICS LOG EXAMPLE
        console.log("Fetched Content Rendered");
        messageElement.setContent(content);
      },
    });
    function triggerAmountUpdate(amount) {
      content.update({ amount });
    }
    const learnMore = await messagesInstance.createLearnMore({
      onShow: (content) => {
        // ANALYTICS LOG EXAMPLE
        console.log("Learn More Shown");
      },
      onApply: (content) => {
        // ANALYTICS LOG EXAMPLE
        console.log("Learn More Apply");
      },
      onClose: (content) => {
        // ANALYTICS LOG EXAMPLE
        console.log("Learn More Closed");
      },
    });
    messageElement.addEventListener("paypal-message-click", (event) => {
      event.preventDefault();
      learnMore.open(event.detail.config);
      // ANALYTICS LOG EXAMPLE
      console.log("Message Learn More Clicked");
    });
  </script>
</body>
```
