---
title: Integrate Google Pay with JS SDK for direct merchants
slug: /docs/checkout/apm/google-pay/
createTime: "2025-02-25T12:20:48.574Z"
updateTime: "2025-05-09T09:27:48.401Z"
---

# Integrate Google Pay with JS SDK for direct merchants

## Google Pay integration

Google Pay is a mobile payment and digital wallet service provided by Alphabet Inc.

Buyers can use Google Pay on PayPal to make payments on the web using a web browser.

Sellers can use PayPal with Google Pay to sell physical goods, such as clothes and electronics, and intangible professional services, such as concerts or gym memberships.

![sdk_mobile_googlepay.png](assets/paypal-googlepay-mobile.png)

## Supported countries and currencies

Google Pay supports payments in 36 countries and 22 currencies:

- **Countries:** Australia, Austria, Belgium, Bulgaria, Canada, China, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hong Kong, Hungary, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Netherlands, Norway, Poland, Portugal, Romania, Singapore, Slovakia, Slovenia, Spain, Sweden, United States, United Kingdom
- **Currencies:** AUD , BRL , CAD , CHF , CZK , DKK , EUR , GBP , HKD , HUF , ILS , JPY , MXN , NOK , NZD , PHP , PLN , SEK , SGD , THB , TWD , USD

Note: TPAN is not supported by local processors (NTTD) and acquirers in Japan for Visa, Mastercard, JCB, or Diners Club cards.

Tip: If you want to integrate additional methods of accepting payment beyond Google Pay, visit our [Expanded Checkout guide](https://developer.paypal.com/docs/checkout/advanced/integrate/) for additional integration choices.

## How it works

- The Google Pay button shows up on your website when a customer uses a web browser.
- The buyer selects the Google Pay button on your website.
- Your website shows the buyer a payment sheet.
- The buyer can choose a different shipping address and payment method.
- The buyer authorizes the payment.

## Know before you code

### Google Pay works on most web browsers, including:

- Google Chrome.
- Mozilla Firefox.
- Apple Safari.
- Microsoft Edge.

### Currently supports Google Pay one-time payments with the buyer present.

Review Google's Google Pay API Terms of Service and Acceptable Use Policy for more information.

## Get up and running in GitHub Codespaces

GitHub Codespaces are cloud-based development environments where you can code and test your PayPal integrations. [Learn more](https://developer.paypal.com/api/rest/sandbox/codespaces/)

## Set up your sandbox account to accept Google Pay

Before you can accept Google Pay on your website, verify that your sandbox business account supports Google Pay.

Direct merchants can use the PayPal Developer Dashboard to set up their sandbox accounts to accept Google Pay.

- Log into the PayPal [Developer Dashboard](https://developer.paypal.com/dashboard) and go to your sandbox account.
- Go to **Apps & Credentials** .
- Make sure you are in the PayPal sandbox environment by selecting **Sandbox** at the top.
- Select or create an app.
- Scroll down to **Features** and check if Google Pay is enabled. If Google Pay isn't enabled, select the **Google Pay** checkbox and select the "Save" link to enable Google Pay.

If you created a sandbox business account through [sandbox.paypal.com](https://sandbox.paypal.com/) , and the Google Pay status for the account shows as disabled, [complete the sandbox onboarding steps](https://www.sandbox.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=GOOGLE_PAY) to enable Google Pay.

**Tip:** When your integration is ready to go live, read the Go live section for details about the additional steps needed for Google Pay onboarding.

This screenshot shows the Google Pay sandbox settings in the mobile and digital payments section of the PayPal Developer Dashboard. This only applies to direct merchant integrations:

![Google Pay sandbox settings in PayPal Developer Dashboard](assets/paypal-googlepay-dashboard.png)

## Getting started in your testing environment

Before you develop your Google Pay on the Web integration, you need to complete [Get started](https://developer.paypal.com/api/rest/) to set up your PayPal account, client ID, and sandbox emails for testing.

Follow this integration process to add Google Pay as a checkout option, customize the payment experience, and process payments.

### Call the Orders API

To accept Google Pay directly on your website, create API endpoints on your server that communicate with the [PayPal Orders V2 API](https://developer.paypal.com/docs/api/orders/v2/) . These endpoints can create an order, authorize payment, and capture payment for an order.

### Server-side example (Node.js)

This code demonstrates using the [PayPal Orders V2 API](https://developer.paypal.com/docs/api/orders/v2/) to add routes to an Express server for creating orders and capturing payments.

Find the complete sample code in the [GitHub repo](https://github.com/paypal-examples/googlepay) .

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
    method: "POST",
    headers: {
      "Content-Type": "application/json",
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
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
  });
  const data = await response.json();
  return data;
}
```

You need to integrate with the Google Pay JavaScript SDK and PayPal JavaScript SDK to add Google Pay to your site.

### Integrate PayPal JavaScript SDK

Use this script to integrate with the PayPal JavaScript SDK:

#### **`index.html`**

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD&buyer-country=US&merchant-id=SUB_MERCHANT_ID&components=googlepay"></script>
```

Include googlepay in the components list.

### Integrate Google JavaScript SDK

Use this script to integrate with the Google Pay JavaScript SDK:

#### **`index.html`**

```html
<script
  async
  src="https://pay.google.com/gp/p/js/pay.js"
  onload="onGooglePayLoaded()"
></script>
```

PayPal's Google Pay component interacts with your JavaScript code in 2 areas:

- Checking merchant eligibility and providing [PaymentDataRequest](https://developers.google.com/pay/api/web/reference/request-objects#PaymentDataRequest) parameters for Google Pay: paypal.Googlepay().config() .
- Handling the onPaymentAuthorized() callback: paypal.Googlepay().confirmOrder() .

Check for device and merchant eligibility before setting up the GooglePay Button.

The PayPal JavaScript SDK API paypal.Googlepay().config() response object provides the allowedPaymentMethods parameter, which is part of the" "} Google API's [isReadyToPayRequest](https://developers.google.com/pay/api/web/reference/request-objects#IsReadyToPayRequest) object.

Check whether the Google Pay API supports a device, browser, and payment method:

- Add allowedPaymentMethods to the isReadyToPayRequest .
- Call the isReadyToPay() method to check compatibility and render the Google Pay Button.

#### **`index.js`**

```javascript
/**
 * Initialize Google PaymentsClient after Google-hosted JavaScript has loaded
 *
 * Display a Google Pay payment button after confirmation of the viewer's
 * ability to pay.
 */
function onGooglePayLoaded() {
  const paymentsClient = getGooglePaymentsClient();
  paymentsClient
    .isReadyToPay(isReadyToPayRequest)
    .then(function (response) {
      if (response.result) {
        addGooglePayButton();
      }
    })
    .catch(function (err) {
      console.error(err);
    });
}
/**
 * Add a Google Pay purchase button
 */
function addGooglePayButton() {
  const paymentsClient = getGooglePaymentsClient();
  const button = paymentsClient.createButton({
    onClick: onGooglePaymentButtonClicked /* To be defined later */,
    allowedPaymentMethods: [baseCardPaymentMethod],
  });
  document.getElementById("container").appendChild(button);
}
```

**Tip:** For more information refer to steps 6 and 7 in [Google's developer documentation](https://developers.google.com/pay/api/web/guides/tutorial#isreadytopay) .

The PaymentDataRequest object manages the Google Pay payment process on the web. Create a new PaymentDataRequest each time a buyer explicitly requests a payment, such as inside the onclick handler for the Google Pay Button.

For each checkout session, create a `PaymentDataRequest` object, which includes information about payment processing capabilities, the payment amount, and shipping information.

The response object of the PayPal JavaScript SDK API paypal.Googlepay().config() provides the following parameters in the PaymentDataRequest object:

- allowedPaymentMethods
- merchantInfo

Note: For integrations in Japan, you'll need to override the allowedAuthMethods as allowedPaymentMethods[0].parameters.allowedAuthMethods = ['PAN_ONLY'] .

#### **`index.js`**

```javascript
/* Note: the `googlePayConfig` object in this request is the response from `paypal.Googlepay().config()` */
async function getGooglePaymentDataRequest() {
  const googlePayConfig = await paypal.Googlepay().config();
  const paymentDataRequest = Object.assign({}, baseRequest);
  paymentDataRequest.allowedPaymentMethods =
    googlePayConfig.allowedPaymentMethods;
  // Uncomment for Japan integrations only
  // paymentDataRequest.allowedPaymentMethods[0].parameters.allowedAuthMethods = ['PAN_ONLY'];
  paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
  paymentDataRequest.merchantInfo = googlePayConfig.merchantInfo;
  paymentDataRequest.callbackIntents = ["PAYMENT_AUTHORIZATION"];
  return paymentDataRequest;
}
function getGoogleTransactionInfo() {
  return {
    currencyCode: "USD",
    totalPriceStatus: "FINAL",
    totalPrice: "100.00", // Your amount
  };
}
```

For more details about the response parameters, see the ConfigResponse section.

For more details about how Google Pay handles paymentDataRequest , refer to steps 8, 9, and 10 in [Google's developer documentation](https://developers.google.com/pay/api/web/guides/tutorial#paymentdatarequest) .

**Tip:** See the [Google Pay PaymentDataRequest Object API reference](https://developers.google.com/pay/api/web/reference/request-objects#PaymentDataRequest) for the complete list of properties available for the PaymentDataRequest object.

### Register click handler

Register a click event handler for the Google Pay purchase button. Call loadPaymentData() in the event handler when the user interacts with the purchase button and pass the PaymentDataRequest object.

#### **`index.js`**

```javascript
/* Show Google Pay payment sheet when Google Pay payment button is clicked */
async function onGooglePaymentButtonClicked() {
  const paymentDataRequest = await getGooglePaymentDataRequest();
  const paymentsClient = getGooglePaymentsClient();
  paymentsClient.loadPaymentData(paymentDataRequest);
}
```

Add the click handler onGooglePaymentButtonClicked to the Button defined in [Set up your Google Pay button](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-setupyourgooglepaybutton) .

For more details about paymentDataRequest refer to step 9 in [Google's developer documentation](https://developers.google.com/pay/api/web/guides/tutorial#paymentdatarequest) .

### onpaymentauthorized callback

Google calls the onPaymentAuthorized() callback with a [PaymentData](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) object when a customer consents to your site collecting their payment information and optional contact details.

Register the onPaymentAuthorized() callback as part of the PaymentClient initialization as shown in Google Pay's [Client Reference page](https://developers.google.com/pay/api/web/reference/client#PaymentsClient) .

Create an order by using the [PayPal Orders V2 API](https://developer.paypal.com/api/orders/v2) . Use paypal.Googlepay().confirmOrder() to send the orderID , the Google Pay Payment Data, and optional contact details, and confirm the order.

Confirm the order using the [paypal.Googlepay().confirmOrder()](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-confirmorderconfirmorderparams) method in the API SDK Reference.

If the order confirmation status is APPROVED , capture the order using the [Capture payment for order endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) of the PayPal Orders V2 API.

For more details, see step 11 of [Google's developer documentation](https://developers.google.com/pay/api/web/guides/tutorial#authorize-payments) .

Tip: You can see an [example of an Authorize Payments call](https://developers.google.com/pay/api/web/guides/tutorial#authorize-payments_1) in the Put it all together section of Google's developer documentation.

#### **`index.js`**

```javascript
async function processPayment(paymentData) {
  return new Promise(async function (resolve, reject) {
    try {
        // Create the order on your server
        const {id} = await fetch(`/orders`, {
        method: "POST",
        body:
        // You can use the "body" parameter to pass optional, additional order information, such as:
        // amount, and amount breakdown elements like tax, shipping, and handling
        // item data, such as sku, name, unit_amount, and quantity
        // shipping information, like name, address, and address type
      });
      const confirmOrderResponse = await paypal.Googlepay().confirmOrder({
          orderId: id,
          paymentMethodData: paymentData.paymentMethodData
        });
      /** Capture the Order on your Server  */
      if(confirmOrderResponse.status === "APPROVED"){
           const response =  await fetch(`/capture/${id}`, {
              method: 'POST',
            }).then(res => res.json());
          if(response.capture.status === "COMPLETED")
              resolve({transactionState: 'SUCCESS'});
          else
              resolve({
                transactionState: 'ERROR',
                error: {
                  intent: 'PAYMENT_AUTHORIZATION',
                  message: 'TRANSACTION FAILED',
                }
      })
      } else {
           resolve({
            transactionState: 'ERROR',
            error: {
              intent: 'PAYMENT_AUTHORIZATION',
              message: 'TRANSACTION FAILED',
            }
          })
      }
    } catch(err) {
      resolve({
        transactionState: 'ERROR',
        error: {
          intent: 'PAYMENT_AUTHORIZATION',
          message: err.message,
        }
      })
    }
  });
}
```

### Customize payment experience

Customize the payment experience using the [Google Pay JavaScript SDK](https://developers.google.com/pay/api/web/reference/client) . The following table shows the 2 most popular Google Pay customizations:

| Customization                                                                                                                                                                                                                                                                                              | Details                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [](https://developer.paypal.com/docs/checkout/apm/google-pay/#paymentdatachangethis-method-is-used-to-handle-payment-data-changes-in-the-payment-sheet-such-as-shipping-address-and-shipping-options.)[PaymentDataChange](https://developers.google.com/pay/api/web/reference/client#onPaymentDataChanged) | This method is used to handle payment data changes in the payment sheet such as shipping address and shipping options. |
| [](https://developer.paypal.com/docs/checkout/apm/google-pay/#paymentdatarequestprovides-optional-properties-to-collect-details,-such-as-shipping-address-and-email.)[PaymentDataRequest](https://developers.google.com/pay/api/web/reference/request-objects#PaymentDataRequest)                          | Provides optional properties to collect details, such as shipping address and email.                                   |

The following code samples show a Google Pay integration:

#### **`HTML`**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Googlepay Example</title>
    <script src="./script.js"></script>
    <script src="https://www.paypal.com/sdk/js?client-id=<client_id>&components=googlepay"></script>
    <link rel="stylesheet" type="text/css" href="styles.css" />
  </head>
  <body>
    <main>
      <section>
        <div id="button-container"></div>
      </section>
    </main>
    <script src="https://pay.google.com/gp/p/js/pay.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", (event) => {
        if (google && paypal.Googlepay) {
          onGooglePayLoaded().catch(console.log);
        }
      });
    </script>
  </body>
</html>
```

#### **`JavaScript`**

```javascript
/*
 * Define the version of the Google Pay API referenced when creating your
 * configuration
 */
const baseRequest = {
  apiVersion: 2,
  apiVersionMinor: 0,
};
let paymentsClient = null,
  allowedPaymentMethods = null,
  merchantInfo = null;
/* Configure your site's support for payment methods supported by the Google Pay */
function getGoogleIsReadyToPayRequest(allowedPaymentMethods) {
  return Object.assign({}, baseRequest, {
    allowedPaymentMethods: allowedPaymentMethods,
  });
}
/* Fetch Default Config from PayPal via PayPal SDK */
async function getGooglePayConfig() {
  if (allowedPaymentMethods == null || merchantInfo == null) {
    const googlePayConfig = await paypal.Googlepay().config();
    allowedPaymentMethods = googlePayConfig.allowedPaymentMethods;
    merchantInfo = googlePayConfig.merchantInfo;
  }
  return {
    allowedPaymentMethods,
    merchantInfo,
  };
}
/* Configure support for the Google Pay API */
async function getGooglePaymentDataRequest() {
  const paymentDataRequest = Object.assign({}, baseRequest);
  const { allowedPaymentMethods, merchantInfo } = await getGooglePayConfig();
  paymentDataRequest.allowedPaymentMethods = allowedPaymentMethods;
  paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
  paymentDataRequest.merchantInfo = merchantInfo;
  paymentDataRequest.callbackIntents = ["PAYMENT_AUTHORIZATION"];
  return paymentDataRequest;
}
function onPaymentAuthorized(paymentData) {
  return new Promise(function (resolve, reject) {
    processPayment(paymentData)
      .then(function (data) {
        resolve({ transactionState: "SUCCESS" });
      })
      .catch(function (errDetails) {
        resolve({ transactionState: "ERROR" });
      });
  });
}
function getGooglePaymentsClient() {
  if (paymentsClient === null) {
    paymentsClient = new google.payments.api.PaymentsClient({
      environment: "TEST", // or "PRODUCTION"
      paymentDataCallbacks: {
        onPaymentAuthorized: onPaymentAuthorized,
      },
    });
  }
  return paymentsClient;
}
async function onGooglePayLoaded() {
  const paymentsClient = getGooglePaymentsClient();
  const { allowedPaymentMethods } = await getGooglePayConfig();
  paymentsClient
    .isReadyToPay(getGoogleIsReadyToPayRequest(allowedPaymentMethods))
    .then(function (response) {
      if (response.result) {
        addGooglePayButton();
      }
    })
    .catch(function (err) {
      console.error(err);
    });
}
function addGooglePayButton() {
  const paymentsClient = getGooglePaymentsClient();
  const button = paymentsClient.createButton({
    onClick: onGooglePaymentButtonClicked,
  });
  document.getElementById("container").appendChild(button);
}
function getGoogleTransactionInfo() {
  return {
    displayItems: [
      {
        label: "Subtotal",
        type: "SUBTOTAL",
        price: "100.00",
      },
      {
        label: "Tax",
        type: "TAX",
        price: "10.00",
      },
    ],
    countryCode: "US",
    currencyCode: "USD",
    totalPriceStatus: "FINAL",
    totalPrice: "110.00",
    totalPriceLabel: "Total",
  };
}
async function onGooglePaymentButtonClicked() {
  const paymentDataRequest = await getGooglePaymentDataRequest();
  paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
  const paymentsClient = getGooglePaymentsClient();
  paymentsClient.loadPaymentData(paymentDataRequest);
}
async function processPayment(paymentData) {
  try {
    const { currencyCode, totalPrice } = getGoogleTransactionInfo();
    const order = {
      intent: "CAPTURE",
      purchase_units: [
        {
          amount: {
            currency_code: currencyCode,
            value: totalPrice,
          },
        },
      ],
    };
    /* Create Order */
    const { id } = await fetch(`/orders`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(order),
    }).then((res) => res.json());
    const { status } = await paypal.Googlepay().confirmOrder({
      orderId: id,
      paymentMethodData: paymentData.paymentMethodData,
    });
    if (status === "APPROVED") {
      /* Capture the Order */
      const captureResponse = await fetch(`/orders/${id}/capture`, {
        method: "POST",
      }).then((res) => res.json());
      return { transactionState: "SUCCESS" };
    } else {
      return { transactionState: "ERROR" };
    }
  } catch (err) {
    return {
      transactionState: "ERROR",
      error: {
        message: err.message,
      },
    };
  }
}
```

When the ConfirmOrder [status](https://developer.paypal.com/docs/api/orders/v2/#definition-order_status) is PAYER_ACTION_REQUIRED , the order requires additional authentication from the payer, such as 3D Secure.

The PayPal JavaScript SDK Client provides an API to handle 3DS Secure authentication. Pass the orderId to initiatePayerAction .

**Tip:** Refer to [initiatePayerAction](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-initiatepayeractionparams) for more details.

When the payer completes authentication, confirm that the liability_shift status has shifted:

- Make a call to the [Show order details endpoint](https://developer.paypal.com/docs/api/orders/v2/#orders_get) of the Orders v2 API, using the id of the order.
- Check the liability_shift status in the [authentication_response](https://developer.paypal.com/docs/api/orders/v2/#definition-authentication_response) .

#### **`index.js`**

```javascript
...
const { status } = await paypal.Googlepay().confirmOrder({
  orderId: id,
  paymentMethodData: paymentData.paymentMethodData,
});
if (status === "PAYER_ACTION_REQUIRED") {
  console.log("==== Confirm Payment Completed Payer Action Required =====");
  paypal
    .Googlepay()
    .initiatePayerAction({ orderId: id })
    .then(async () => {
      console.log("===== Payer Action Completed =====");
      /** GET Order */
      const orderResponse = await fetch(`/orders/${id}`, {
        method: "GET",
      }).then((res) => res.json());
      console.log("===== 3DS Contingency Result Fetched =====");
      console.log(
        orderResponse?.payment_source?.google_pay?.card?.authentication_result
      );
      /* CAPTURE THE ORDER*/
      const captureResponse = await fetch(`/orders/${id}/capture`, {
        method: "POST",
      }).then((res) => res.json());
      console.log(" ===== Order Capture Completed ===== ");
    });
}
...
```

## Test your integration

Test your Google Pay integration in the PayPal sandbox and production environments to ensure that your app works correctly.

### Sandbox

Use your personal sandbox login information during checkout to complete a payment using Google Pay. Then, log into the sandbox site [sandbox.paypal.com](https://sandbox.paypal.com/) to see that the money has moved into your account.

- Open your test page with a supported web browser on any supported device.
- Add a test card to your Google Wallet on your device. Google provides test cards through their [Test card suite](https://developers.google.com/pay/api/web/guides/resources/test-card-suite) .
- Tap the Google Pay button to open a pop-up with the Google Pay payment sheet.
- Make a payment using the Google Pay payment sheet.
- If you have an additional confirmation page on your merchant website, continue to confirm the payment.
- Log in to your merchant account and continue to your confirmation page to confirm that the money you used for payment showed up in the account.

### Google Pay test card suite

Use Google Pay [test card numbers](https://developer.paypal.com/docs/checkout/apm/test-cards/google-pay/) to test your Google Pay integration.

##

## Go live

Make Google Pay available to buyers using your website or app.

Tip: Before going live, complete [production onboarding](https://www.paypal.com/bizsignup/add-product?product=payment_methods&capabilities=GOOGLE_PAY) to process Google Pay payments with your live PayPal account.

### Live environment

If you're a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business) .

Use your personal production login information during checkout to complete a Google Pay transaction. Then log into paypal.com to see the money move out of your account.

## Testing in your live environment

When testing a purchase in production, consider:

- The business account receiving money can't also make the purchase.
- If you create a personal account with the same information as the business account, those accounts might experience restrictions.

How to test Google Pay payments in a live environment:

- Open your test page with a supported browser.
- Select the Google Pay button to open a pop-up with the Google Pay payment sheet.
- Proceed with the Google Pay checkout transaction.
- If you have an additional confirmation page on your merchant website, continue to confirm the payment.
- Log in to your merchant account and confirm that the money has moved into that account.

## Troubleshoot your integration

Make sure that there are no browser console warnings or errors. The JavaScript SDK configuration attributes have distinct validation checks for input formatting and values.

If the validation fails, the web browser's developer console shows warning messages that say which property is incorrect and what you need to do to address the issue. The library generally attempts to revert to the safe default values if missing or incorrect inputs exist.

## Next steps & customizations

[Advanced credit and debit card payments](https://developer.paypal.com/docs/checkout/advanced/)

Add PayPal payment buttons and customized card fields.

## SDK/API reference

This section provides details about functions, objects, and parameters in the SDK API.

### Initialize payment with paypal.Googlepay()

Creates an instance of a PayPal Google Pay SDK Client.

Arguments

None

Returns

[JavaScript SDK Client](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-jssdkclientobject)

### JavaScript SDK client methods

Use the JavaScript SDK client methods to start a Google Pay payment and confirm an order.

### config()

Use config() to fetch the PaymentMethod data needed to start the payment.

Arguments

None

Returns

| Type                                                                                                | Description                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) | Resolved: An object that contains the payment data needed to create a PaymentDataRequest to the Google SDK. For more details, see [ConfigResponse](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-configresponse) . |

Rejected: An error object that passes information about why the call wasn't successful. |

### confirmOrder(confirmOrderParams)

Use confirmOrder() to confirm that the buyer intends to pay for the order using the payment source.

Arguments

| Name               | Description                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| confirmOrderParams | For details on the different properties you can configure, see[ConfirmOrderParams](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-confirmorderparams). |

Returns

| Name                                                                                                | Description                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) | Resolved: An object that returns the response of a successful confirmOrder . For more details, see [ConfirmOrderResponse](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-confirmorderresponse) . |

Rejected: An error object that passes information about why the call wasn't successful. |

### initiatePayerAction(initiatePayerActionParams)

Arguments

| Name                      | Description                                                                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| initiatePayerActionParams | For details on the different properties you can configure, see [InitiatePayerActionParams](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-initiatepayeractionparams) . |

Returns

| Type                                                                                                | Description                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) | Resolved: An object that passes information about 3D Secure liability shift. See [InitiatePayerActionResponse](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-initiatepayeractionresponse) for more information. |

Rejected: An error object that passes information about why the call wasn't successful. |

### Request objects

Use the following JavaScript SDK request objects in a Google Pay payment:

### ConfirmOrderParams

| Property          | Type   | Required | Description                                                                                                                                                                                                                            |
| ----------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| paymentMethodData | object | Yes      | Details about a selected payment method. When a buyer approves payment, the [PaymentData](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) response object from Google passes the paymentMethodData . |

For more details about this object, see the [Google Pay documentation](https://developers.google.com/pay/api/web/reference/response-objects#PaymentMethodData) . |
| orderId | string | Yes | The PayPal order ID. |
| shippingAddress | object | No | Passes the shipping address when shippingAddressRequired in the PaymentDataRequest is set to true .

For more details about this object, see the [Google Pay documentation](https://developers.google.com/pay/api/web/reference/response-objects#Address) . |
| billingAddress | object | No | The default billing address is part of the [CardInfo](https://developers.google.com/pay/api/web/reference/response-objects#CardInfo) object. Use this property to pass a new billing address and overwrite the default.

For more details about this object, see the [Google Pay documentation](https://developers.google.com/pay/api/web/reference/response-objects#Address) . |
| email | string | No | Passes the email address whenemailRequiredin thePaymentDataRequestis set totrue. |

### InitiatePayerActionParams

| Property | Type   | Required | Description    |
| -------- | ------ | -------- | -------------- |
| orderId  | string | Yes      | PayPal OrderID |

### Response objects

Google Pay responses include the following objects:

### JSSDKClientObject

| Property            | Type                                                                                                                     | Always exists | Description                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------- | --------------------------- |
| config              | [function](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-config)                                       | Yes           | API forPaymentData.         |
| confirmOrder        | [function](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-confirmorderconfirmorderparams)               | Yes           | API forconfirmOrder.        |
| initiatePayerAction | [function](https://developer.paypal.com/docs/checkout/apm/google-pay/#link-initiatepayeractioninitiatepayeractionparams) | Yes           | API for 3D Secure handling. |

### ConfigResponse

| Property              | Type   | Always exists | Description                                                 |
| --------------------- | ------ | ------------- | ----------------------------------------------------------- |
| allowedPaymentMethods | object | Yes           | Passes the payment methods supported by the Google Pay API. |

For more details about this object, see the [Google Pay documentation](https://developers.google.com/pay/api/web/reference/request-objects#PaymentMethod) . |
| merchantInfo | object | Yes | Passes information about the seller requesting payment data.

For more details about this object, see the [Google Pay documentation](https://developers.google.com/pay/api/web/reference/request-objects#MerchantInfo) . |

### ConfirmOrderResponse

| Property | Type   | Always exists | Description          |
| -------- | ------ | ------------- | -------------------- |
| id       | string | Yes           | The ID of the order. |
| status   | string | Yes           | The order status.    |

For a list of supported values for this property, see the [Orders API documentation](https://developer.paypal.com/docs/api/orders/v2/#definition-order_status) . |
| payment_source | object | Yes | The payment source used to fund the payment.

For more details about this object, see the [Orders API documentation](https://developer.paypal.com/docs/api/orders/v2/#definition-payment_source_response) . |
| links | array of objects | Yes | The request-related [HATEOAS](https://developer.paypal.com/api/rest/responses/#hateoas-links) link information.

For more details about this property, see the [Orders API documentation](https://developer.paypal.com/docs/api/orders/v2/#definition-link_description) . |

### InitiatePayerActionResponse

| Property       | Type   | Always exists | Description                                                                     |
| -------------- | ------ | ------------- | ------------------------------------------------------------------------------- |
| liabilityShift | string | Yes           | The liability shift indicator shows the outcome of the issuer's authentication. |

For a list of supported values for this property, see the [Orders API documentation](https://developer.paypal.com/docs/api/orders/v2/#definition-liability_shift) . |
