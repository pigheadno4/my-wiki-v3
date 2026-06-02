---
title: Integrate Apple Pay with JS SDK for direct merchants
slug: /docs/checkout/apm/apple-pay/
createTime: "2024-10-23T07:41:57.004Z"
updateTime: "2025-08-06T13:52:33.583Z"
---

# Integrate Apple Pay with JS SDK for direct merchants

## Apple Pay integration

Apple Pay is a mobile payment and digital wallet service provided by Apple Inc.

Buyers can use Apple Pay to make payments on the web using the Safari web browser or an iOS device.

Sellers can use Apple Pay to sell:

- Physical goods, such as clothes and electronics.
- Digital goods, such as software.
- Intangible professional services, such as concerts or gym memberships.

[Visit this site](https://developer.apple.com/documentation/passkit/apple_pay) for more information about Apple Pay.

![applepay-sheet-xxl-m.png](assets/paypal-applepay-sheet.png)

## Supported countries and currencies

Apple Pay supports payments in 34 countries and 22 currencies:

- **Countries:** Australia, Austria, Belgium, Bulgaria, Canada, China, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, United States, United Kingdom
- **Currencies:** AUD , BRL , CAD , CHF , CZK , DKK , EUR , GBP , HKD , HUF , ILS , JPY , MXN , NOK , NZD , PHP , PLN , SEK , SGD , THB , TWD , USD

**info**
If you want to integrate additional methods of accepting payment beyond Apple Pay, visit our [Advanced Checkout guide](/docs/checkout/advanced/integrate/) for additional integration choices.

**info**
Apple Pay Recurring for Japan is not supported.

## How it works

The Apple Pay button shows up on your website when a customer uses the Safari web browser on an eligible device.

When your buyer selects the Apple Pay button:

- Your website shows the buyer a payment sheet.
- The buyer confirms the purchase details, such as the shipping address and payment method.
- The buyer authorizes the purchase on the payment sheet.

The payment sheet helps streamline the checkout process by showing the customer the information needed to make the payment.

Payment sheets can show the user's name, address, shipping information, and email address. You can customize this payment sheet to include the user details and payment information you need for your Apple Pay integration.

[Visit this site](https://support.apple.com/en-us/HT208531) for more details about Apple Pay's compatibility.

![applepay_mobile.png](assets/paypal-applepay-mobile.png)

## Integration video

Watch our video tutorial for this integration:

## Know before you code

You must be an approved partner to integrate the Apple Pay SDK.

For customers to pay with Apple Pay, they must be in a region where Apple Pay is supported, and their devices must meet the following requirements:

- Device compatibility: The device must support Apple Pay.
- iOS version: iOS 12.1 or later.
- Desktop: macOS 10.14.1 or later.
- Supported browsers: Safari. With the [latest Apple Pay SDK](https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js) , customers can also pay using non-Safari browsers.

PayPal also provides iframe support for ApplePay. To use ApplePay within an iframe:

- The iframe tag must have the attribute allow="payment" .
- The parent domain hosting the iframe needs to have it's domain validated by following the usual process with PayPal.

Currently supports Apple Pay one-time payments with the buyer present.

- Review Apple's terms and conditions for the Apple Pay platform.
- See Apple's developer terms for more information.

Get up and running in GitHub Codespaces

GitHub Codespaces are cloud-based development environments where you can code and test your PayPal integrations. [Learn more](/api/rest/sandbox/codespaces/)

[Open in Codespaces](https://github.com/codespaces/new/paypal-examples/applepay)

## Set up your sandbox account to accept Apple Pay

Before you can accept Apple Pay on your website, verify that your sandbox business account supports Apple Pay. Use the PayPal Developer Dashboard to set up your sandbox account to accept Apple Pay.

- Log into the [PayPal Developer Dashboard](/dashboard/applications/sandbox) and go to your sandbox account.
- Go to **Apps & Credentials** .
- Make sure you are in the PayPal sandbox environment by selecting **Sandbox** at the top.
- Select or create an app.
- Scroll down to **Features** and check if Apple Pay is enabled. If Apple Pay isn't enabled, select the **Apple Pay** checkbox and select the "Save" link to enable Apple Pay.

If you created a sandbox business account through [sandbox.paypal.com](https://sandbox.paypal.com/) , and the Apple Pay status for the account shows as disabled, [complete the sandbox onboarding steps](https://www.sandbox.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY&_ga=1.255056589.491931369.1702610895) to enable Apple Pay.

**info**
**Tip:** When your integration is ready to go live, read the Go live section for details about the additional steps needed for Apple Pay onboarding.

## Getting started in your testing environment

Before you develop your Apple Pay on the Web integration, you need to complete [Get started](/api/rest/) to set up your PayPal account, client ID, and sandbox emails for testing.

- **Download and host** the domain association file for your sandbox environment.
- **Register your sandbox domain.**
- **Create an Apple Pay sandbox account** for testing. You don't need an Apple developer account to go live.

**info**
Important: You need to verify any domain names that you want to show an Apple Pay button. Apple rejects payments from unverified domains. The Apple Pay payment method won't work if the domain isn't registered.

## Download and host sandbox domain association file

- Download the domain association file for your sandbox environment.
- Host the file on your test environment at /.well-known/apple-developer-merchantid-domain-association.

[Download](https://paypalobjects.com/devdoc/apple-pay/sandbox/apple-developer-merchantid-domain-association)

## Register your sandbox domains

- Go to your PayPal Developer Dashboard.
- Register all high-level domains and subdomains that show the Apple Pay button, such as businessexample.com and checkout.businessexample.com.
- After the domains and subdomains are registered, you can test the Apple Pay buttons after you register the domains and subdomains.

## Create Apple Pay sandbox account

Create an Apple Pay sandbox account on the Apple Developer website to get a test wallet and test cards to test your Apple Pay integration.

If you already have an Apple sandbox account, you can use that account and move on to the next step.

- Create an [Apple developer account](https://developer.apple.com/) .
- Create an [Apple sandbox account](https://developer.apple.com/apple-pay/sandbox-testing/) .
- Get test cards from your Apple sandbox account.

## Integrate Apple Pay checkout

Follow this integration process to add Apple Pay as a checkout option, customize the payment experience, and process payments.

**info**
**Important:** You can find a complete example in the [GitHub repo](https://github.com/paypal-examples/applepay) .

### Call the Orders API

To accept Apple Pay directly on your website, create API endpoints on your server that communicate with the [PayPal Orders V2 API](/docs/api/orders/v2/) . These endpoints can create an order, authorize payment, and capture payment for an order.

### Server-side example (Node.js)

The following example uses the [PayPal Orders V2 API](/docs/api/orders/v2/) to add routes to an Express server for creating orders and capturing payments.

#### **`server.js`**

```javascript
import * as PayPal from "./paypal-api.js";

/* Create Order route Handler */
app.post("/api/orders", async (req, res) => {
  const order = await PayPal.createOrder();
  res.json(order);
});

/* Capture Order route Handler */
app.post("/api/orders/:orderID/capture", async (req, res) => {
  const { orderID } = req.params;
  const captureData = await PayPal.capturePayment(orderID);
  res.json(captureData);
});
```

#### **`paypal-api.js`**

```javascript
// create an order
export async function createOrder() {
  const purchaseAmount = "100.00";
  const accessToken = await generateAccessToken();
  const url = `${base}/v2/checkout/orders`;
  const response = await fetch(url, {
    method: "post",
    headers: {
      "Content=Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
    body: JSON.stringify({
      intent: "CAPTURE",
      purchase_units: [
        {
          amount: {
            currency_code: "USD",
            value: purchaseAmount,
          },
        },
      ],
    }),
  });
  const data = await response.json();
  return data;
}

// capture payment for an order
export async function capturePayment(orderId) {
  const accessToken = await generateAccessToken();
  const url = `${base}/v2/checkout/orders/${orderId}/capture`;
  const response = await fetch(url, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
  });
  const data = await response.json();
  return data;
}
```

You need to Integrate with the Apple Pay JavaScript SDK and PayPal JavaScript SDK to add Apple Pay to your site.

### Integrate PayPal JavaScript SDK

Use this script to integrate with the PayPal JavaScript SDK:

#### **`Integrate PayPal JavaScript SDK`**

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD&buyer-country=US&merchant-id=SUB_MERCHANT_ID&components=applepay"></script>
```

Include applepay in the components list.

Use this script to integrate with the Apple JavaScript SDK:

#### **`Integrate Apple JavaScript SDK`**

```html
<script src="https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js"></script>
```

PayPal's Apple Pay component interacts with your JavaScript code in 4 areas:

- Checking merchant eligibility for Apple Pay: paypal.Applepay().config() .
- Creating an Apple Pay session.
- Handling the onvalidatemerchant callback: paypal.Applepay().validateMerchant() .
- Handling the onpaymentauthorized callback: paypal.Applepay().confirmOrder() .

Before you show the Apple Pay button, make sure that you can create an Apple Pay instance and that the device can make an Apple Pay payment.

Use ApplePaySession.canMakePayments to check if the device can make Apple Pay payments.

**info**
Tip: When testing, you need to be logged into the iCloud account for your testing environment. Testing in the sandbox requires you to log into an [iTunes Connect sandbox tester account](https://developer.apple.com/apple-pay/sandbox-testing/) , which you can create with an [Apple Developer account](https://developer.apple.com/help/account/) . When you test in a live environment, log into a live iCloud account.

Check for device and merchant eligibility before setting up the Apple Pay button.

To check eligibility, use the PayPal JavaScript SDK API paypal.Applepay().config() .

#### **`Apple container`**

```html
<div id="applepay-container"></div>
```

#### **`!window.ApplePaySession`**

```javascript
if (!window.ApplePaySession) {
  console.error("This device does not support Apple Pay");
}
if (!ApplePaySession.canMakePayments()) {
  console.error("This device is not capable of making Apple Pay payments");
}
const applepay = paypal.Applepay();
applepay
  .config()
  .then((applepayConfig) => {
    if (applepayConfig.isEligible) {
      document.getElementById("applepay-container").innerHTML =
        '<apple-pay-button id="btn-appl" buttonstyle="black" type="buy" locale="en">';
    }
  })
  .catch((applepayConfigError) => {
    console.error("Error while fetching Apple Pay configuration.");
  });
```

**info**
Tip: You can find more details on how to set up the Apple Pay button in [Apple's developer documentation](https://developer.apple.com/documentation/applepayjs/displaying_apple_pay_buttons) .

The ApplePaySession object manages the Apple Pay payment process on the web. Create a new ApplePaySession each time a buyer explicitly requests a payment, such as inside an onclick event. If you don't create an ApplePaySession each time, you get a "Must create a new ApplePaySession from a user gesture handler" JavaScript exception. For more information about this error, visit Apple's Creating an Apple Pay Session page.

For each ApplePaySession , create an [ApplePayPaymentRequest](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest) object, which includes information about payment processing capabilities, the payment amount, and shipping information.

The response object of the PayPal JavaScript SDK API paypal.Applepay().config() provides the following parameters in the ApplePayPaymentRequest object:

- countryCode
- merchantCapabilities
- supportedNetworks

#### **`ApplePayPaymentRequest`**

```javascript
const paymentRequest = {
  countryCode: applepayConfig.countryCode,
  merchantCapabilities: applepayConfig.merchantCapabilities,
  supportedNetworks: applepayConfig.supportedNetworks,
  currencyCode: "USD",
  requiredShippingContactFields: ["name", "phone", "email", "postalAddress"],
  requiredBillingContactFields: ["postalAddress"],
  total: {
    label: "Demo",
    type: "final",
    amount: "100.00",
  },
};
const session = new ApplePaySession(4, paymentRequest);
```

Include the new ApplePaySession inside a gesture handler, such as an onclick event or an addEventListener click handler.

Creating an ApplePaySession object throws a JavaScript exception if any of the following occurs:

- Any Apple Pay JavaScript API is called from an insecure page that doesn't use https .
- An incorrect payment request is passed. Payment requests are incorrect if they contain missing, unknown or invalid properties, or if the total amount is negative.

Use paypal.Applepay().validateMerchant() in the onvalidatemerchant callback to create a validated Apple Pay session object:

#### **`onvalidatemerchant callback`**

```javascript
session.onvalidatemerchant = (event) => {
  applepay
    .validateMerchant({
      validationUrl: event.validationURL,
      displayName: "My Store",
    })
    .then((validateResult) => {
      session.completeMerchantValidation(validateResult.merchantSession);
    })
    .catch((validateError) => {
      console.error(validateError);
      session.abort();
    });
};
```

Safari calls the onpaymentauthorized callback with an event object. The event object passes a token which you need to send to PayPal to confirm the order.

Capture the order using the [PayPal Orders V2 API](/api/orders/v2) . Use paypal.Applepay().confirmOrder() to send the orderID , the Apple Pay token, billing contact details, and confirm the order.

#### **`onpaymentauthorized callback`**

```javascript
session.onpaymentauthorized = (event) => {
  console.log("Your billing address is:", event.payment.billingContact);
  console.log("Your shipping address is:", event.payment.shippingContact);
  fetch("/api/orders", {
    method: "post",
    body: {},
  })
    .then((res) => res.json())
    .then((createOrderData) => {
      var orderId = createOrderData.id;
      applepay
        .confirmOrder({
          orderId: orderId,
          token: event.payment.token,
          billingContact: event.payment.billingContact,
        })
        .then((confirmResult) => {
          session.completePayment(ApplePaySession.STATUS_SUCCESS);
          fetch(`/api/orders/${orderId}/capture`, {
            method: "post",
          })
            .then((res) => res.json())
            .then((captureResult) => {
              console.log(captureResult);
            })
            .catch((captureError) => console.error(captureError));
        })
        .catch((confirmError) => {
          if (confirmError) {
            console.error("Error confirming order with applepay token");
            console.error(confirmError);
            session.completePayment(ApplePaySession.STATUS_FAILURE);
          }
        });
    });
};
```

After you have created the Apple Pay session and added the callbacks, call the session.begin method to show the payment sheet. You can only call the begin method when a buyer explicitly requests a payment, such as inside an onclick event. The begin method throws a JavaScript exception if the buyer does not explicitly request the action:

#### **`Show the payment sheet`**

```javascript
session.begin();
```

After the buyer starts a payment in the browser, they use their Apple device to authorize the payment.

### Customize payment

Customize the payment experience using the [Apple Pay JavaScript SDK](https://developer.apple.com/documentation/apple_pay_on_the_web) .

Per Apple's development guidelines, your Apple Pay integration needs to follow these rules:

- The last step of an Apple Pay transaction should be when the buyer uses the payment sheet to confirm the payment.
- Don't ask the buyer to complete additional confirmation after they use the Apple Pay payment sheet to confirm the payment.
- Don't allow changes to the order after the buyer confirms the payment on the Apple Pay payment sheet.

The commonly used customizations for Apple Pay are:

| Customization                                                                                                                                                                                                                       | Apple Pay SDK Details                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [](#a-set-of-line-items-that-explain-the-subtotal,-tax,-discount,-and-additional-charges-for-the-payment.lineitems)A set of line items that explain the subtotal, tax, discount, and additional charges for the payment.            | [lineItems](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/1916120-lineitems)                                                                                                                                                                                                                                                                           |
| [](#the-billing-information-fields-that-the-buyer-must-provide-to-fulfill-the-order.requiredbillingcontactfields)The billing information fields that the buyer must provide to fulfill the order.                                   | [requiredBillingContactFields](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/2216120-requiredbillingcontactfields)                                                                                                                                                                                                                                     |
| [](#the-shipping-information-fields-that-the-buyer-must-provide-to-fulfill-the-order.requiredshippingcontactfields)The shipping information fields that the buyer must provide to fulfill the order.                                | [requiredShippingContactFields](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/2216121-requiredshippingcontactfields)                                                                                                                                                                                                                                   |
| [](#the-buyer's-billing-contact-information.billingcontact)The buyer's billing contact information.                                                                                                                                 | [billingContact](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/1916125-billingcontact)                                                                                                                                                                                                                                                                 |
| [](#the-buyer's-shipping-contact-information.requiredshippingcontactfieldscall-the-onshippingcontactselected-event-handler-when-the-user-selects-a-shipping-contact-in-the-payment-sheet.)The buyer's shipping contact information. | [requiredShippingContactFields](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaypaymentrequest/2216121-requiredshippingcontactfields) Call the[onshippingcontactselected](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778009-onshippingcontactselected)event handler when the user selects a shipping contact in the payment sheet. |
| [](#the-shipping-method-for-a-payment-request.applepayshippingmethodcall-the-onshippingmethodselected-event-handler-when-the-user-selects-a-shipping-method-in-the-payment-sheet.)The shipping method for a payment request.        | [ApplePayShippingMethod](https://developer.apple.com/documentation/apple_pay_on_the_web/applepayshippingmethod) Call the[onshippingmethodselected](https://developer.apple.com/documentation/apple_pay_on_the_web/applepaysession/1778028-onshippingmethodselected)event handler when the user selects a shipping method in the payment sheet.                                                 |

## Test your integration

Test your Apple Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

Use your personal sandbox login information during checkout to complete a payment using Apple Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com) to see that the money has moved into your account.

- Open your test page with the Safari web browser on an iOS device or computer.
- Get a test card from your Apple sandbox account.
- Add the test card to your Apple Wallet on your iOS device or by using the Safari browser on the web.
- Tap the Apple Pay button to open a pop-up with the Apple Pay payment sheet.
- Make a payment using the Apple Pay payment sheet.
- If you have an additional confirmation page on your merchant website, continue to confirm the payment.
- Log in to your merchant account and continue to your confirmation page to confirm that the money you used for payment showed up in the account.

## Go live

Make Apple Pay available to buyers using your website or app.

**info**
Important: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=APPLE_PAY) to process Apple Pay payments with your live PayPal account.

### Live environment

If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business) .

Use your personal production login information during checkout to complete an Apple Pay transaction. Then log into paypal.com to see the money move out of your account.

### Getting started in your live environment

Verify any domain names in your live environment that will show an Apple Pay button. Apple Pay transactions only work on a domain and site registered to you.

- [Download and host](#download-host) the domain association file for your live environment.
- [Register your live domain](#register-your-live-domain) on your PayPal Developer Dashboard.

**info**
Important: The Apple Pay payment method won't work if the domain and site aren't registered. The merchant that owns the domain is responsible for registering that domain.

Prerequisites

Enable Apple Pay for your live account:

- Log into the PayPal Developer Dashboard with your live PayPal account.
- Select the Sandbox/Live toggle so it shows Live .
- Go to Apps & Credentials .
- Scroll down to Features .
- Select the Apple Pay checkbox and select the Save link.

Create an app:

- Log into the PayPal Developer Dashboard with your live PayPal account.
- Select the Sandbox/Live toggle so it shows Live .
- Go to Apps & Credentials .
- Create an app similar to what you created in the sandbox. You don't need to log into a separate test account.

Download and host live domain association file

Host a domain association file for each high-level domain and subdomain that show the Apple Pay button.

- Download the domain association file for your live environment.
- Host the file on your live site for each domain and subdomain you want to register, at /.well-known/apple-developer-merchantid-domain-association . For example: - https://example.com/.well-known/apple-developer-merchantid-domain-association
- https://subdomain.example.com/.well-known/apple-developer-merchantid-domain-association

[Download](https://paypalobjects.com/devdoc/apple-pay/well-known/apple-developer-merchantid-domain-association)

**info**
Note: Remove the file extension from the domain association file when you host it on your server.

**Register your live domain on PayPal**

Add all high-level domains that show the Apple Pay button.

- Log into the PayPal Developer Dashboard with your live PayPal account.
- Select the Sandbox/Live toggle so it shows Live.
- Go to Apps & Credentials.
- Select your app.
- Scroll down to Features &gt; Accept payments &gt; Advanced Credit and Debit Card Payments.
- Check if Apple Pay is enabled. If Apple Pay isn't enabled, select the Apple Pay checkbox and select the Save link to enable Apple Pay.
- Select the Manage link in the Apple Pay section.
- Select Add Domain and enter your domain name.
- Select Register Domain. If registration fails, check that the domain association file is live and saved to the right place on your live site.

**info**
**Note:** When Apple verifies a domain, it makes a request to retrieve the domain verification file. Ensure that:

- The file is not served with a 3XX status code. Apple does not support HTTP URL redirects for the domain association file.
- This file is served via HTTPS 1.1.
- **Important:** This file is served with Content-Type: application/octet-stream to indicate that this is a binary file download.
- The HTTP response for this request returns this file as a binary object and not as HTML, or plain text.
- Access to this file is not behind a firewall. See [Apple documentation](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server) on allowing Apple IP addresses.

After your domain is registered:

- The domain appears under **Domains registered with Apple Pay** .
- Buyers can make payments using the Apple Pay button on the registered website.

## Testing in your live environment

When testing a purchase in production, consider:

- The business account receiving money can't also make the purchase.
- If you create a personal account with the same information as the business account, those accounts might experience restrictions.

How to test Apple Pay payments in a live environment:

- Open your test page with Safari on iOS or desktop.
- Select the Apple Pay button to open a pop-up with the Apple Pay payment sheet.
- Proceed with the Apple Pay checkout transaction.
- If you have an additional confirmation page on your merchant website, confirm the payment.
- Log in to your merchant account and confirm that the money has moved into that account.

## Troubleshoot your integration

Make sure that there are no browser console warnings or errors. The JavaScript SDK configuration attributes have distinct validation checks for input formatting and values.

If the validation fails, the web browser's developer console shows warning messages that say which property is incorrect and what you need to do to address the issue. The library generally attempts to revert to the safe default values if missing or incorrect inputs exist.

## Next steps & customizations

[Advanced credit and debit card payments](/docs/checkout/advanced/)

Add PayPal payment buttons and customized card fields.
