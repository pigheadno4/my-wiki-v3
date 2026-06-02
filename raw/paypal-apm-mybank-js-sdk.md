---
title: Integrate MyBank using the JavaScript SDK
slug: /docs/checkout/apm/mybank/js-sdk/
createTime: "2024-12-03T09:48:53.958Z"
updateTime: "2025-03-18T23:05:55.169Z"
---

# Integrate MyBank using the JavaScript SDK

Use the JavaScript SDK to render payment fields and buttons, and process payments with the Orders API.

### Buyer experience

**Note:**The payment button is disabled in the buyer experience demo. On button click, the user is redirected to their bank to authorize the transaction.

## Know before you code

**Note:**The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can likely reuse that code with adjustments for this payment method.- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get your sandbox account information from the Developer Dashboard: - Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.

- Client Secret: Authorizes an app in your sandbox. Keep this secret safe and don't share it.
- Business account credentials

- Make sure the preference for receiving payments in your PayPal business account is set to accept and convert them to the default currency. To verify, in your profile select **Account Settings &gt; Payment preferences &gt; Block payments** and select **Update** to mark this preference.
- This client-side and server-side integration uses the following: - [PayPal JavaScript SDK](https://developer.paypal.com/sdk/js/)
- [Webhooks Management REST API](/docs/api/webhooks/v1/)
- [Orders REST API](/docs/api/orders/v2/)

- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - CHECKOUT.ORDER.APPROVED - Listen for this webhook and then capture the payment.
- CHECKOUT.PAYMENT-APPROVAL.REVERSED - This webhook tells you when an approved order is cancelled and refunded because it wasn't captured within the capture window. Let the payer know about the problem and the reversed order.

- By adding funding sources to your checkout integration, you agree to the [PayPal alternative payment methods agreement](https://www.paypal.com/us/legalhub/paypal/apm-tnc) . This is in addition to the user agreement applicable to the country in which your business is physically located.

## To get started

### Run in Postman

Use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](https://developer.paypal.com/api/rest/postman/) .

### Get up and running in GitHub Codespaces

GitHub Codespaces are cloud-based development environments where you can code and test your PayPal integrations. [Learn more](https://developer.paypal.com/api/rest/sandbox/codespaces/) .

Add or update the JavaScript SDK script on your web page.

#### **`PayPal JavaScript SDK`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=mybank&currency=EUR"></script>
```

This table lists the parameters you pass to the JavaScript SDK.

| **Query param** | **Default** | **Description** |
| client-id | none | Your PayPal REST client ID. This identifies your PayPal account and determines where transactions are paid. |
| components | buttons | A comma-separated list of components to enable. Thebuttons,payment-fields,marks, andfunding-eligibilitycomponents are required for payment fields components. |
| enable-funding | none | The enabled payment methods to show in buttons and marks. ** Note:**By default, PayPal JavaScript SDK provides smart logic to display only appropriate marks and buttons for the current buyer. This optional parameter bypasses the buyer country check for desired payment methods. For example:src="[https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo](https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo)" |
| currency | USD | This is the currency for the payment. This value needs to match the currency used when creating the order. |
| locale | automatic | The locale renders components. By default PayPal detects the correct locale for the buyer based on their geolocation and browser preferences. It is recommended to pass this parameter with a[supported locale](https://developer.paypal.com/sdk/js/configuration/#link-locale)if you need the PayPal buttons to render in the same language as the rest of your site. |
| intent | capture | The intent for the transaction. This determines whether the funds are captured immediately while the buyer is present on the page. |
| commit | true | This indicates that the final amount won't change after the buyer returns to your site from PayPal. |
| vault | false | Whether the payment information in the transaction will be saved. Save your customers' payment information for billing agreements, subscriptions, or recurring payments. Marking this parameterfalseshows all funding sources, including payment methods that can't be saved. |

See additional, [optional parameters](https://developer.paypal.com/sdk/js/configuration/) .

You can use a [mark integration](/docs/checkout/standard/customize/display-payment-methods/) for payment fields components to present the payment method options to the buyer as radio buttons.

#### **`Render payment mark`**

```javascript
paypal
  .Marks({
    fundingSource: paypal.FUNDING.MYBANK,
  })
  .render("#mybank-mark");
```

## Render payment fields

Use payment fields to collect payment information from buyers. Fields dynamically render based on the selected funding source and you can customize the fields to align with your brand.

You can choose a checkout flow:

- [Single page](#single-page)
- [Multi-page](#multi-page)

### Single page

For MyBank, payment fields collect first name and last name.

If there are validation errors in the input fields, they'll show on the click of the button.

#### **`Render payment fields | Single page code`**

```javascript
paypal
  .PaymentFields({
    fundingSource: paypal.FUNDING.MYBANK,
    /* style object (optional) */
    style: {
      /* customize field attributes (optional) */
      variables: {},
      /* set custom rules to apply to fields classes (optional) */
      rules: {},
    },
    fields: {
      /* fields prefill info (optional) */
      name: {
        value: "John Doe",
      },
    },
  })
  .render("#mybank-container");
```

For style parameters, please reference this style page: [Custom style for payment fields](/docs/checkout/apm/reference/style/)

### Multi page

A multi-page checkout flow spreads the checkout steps into two or more pages. This experience is applicable when an order details page needs to be shown to the buyer before an order is placed.

**Tip:**German merchants can leverage the multi-page flow to comply with local regulations.#### First page of the checkout flow
This example renders the mark and payment fields, but not the payment button, on your checkout page.

![Multipage,Flow,Page,1](assets/paypal-apm-multipage-1.png)

#### **`Payment mark`**

```javascript
paypal
  .Marks({
    fundingSource: paypal.FUNDING.MYBANK,
  })
  .render("#mybank-mark");
```

#### **`Payment fields`**

```javascript
paypal
  .PaymentFields({
    fundingSource: paypal.FUNDING.MYBANK,
    /* style object (optional) */
    style: {
      /* customize field attributes (optional) */
      variables: {},
      /* set custom rules to apply to fields classes (optional) */
      rules: {},
    },
    onInit: (data, actions) => {
      const form = document.querySelector("form.paypal-payment-form");

      form.addEventListener("submit", (e) => {
        const formData = new FormData(form);
        const paymentSource = formData.get("payment-option");

        if (paymentSource === paypal.FUNDING.MYBANK) {
          e.preventDefault();

          actions.validate().then((valid) => {
            if (valid) {
              window.location.href = `/second-page.html?payment-option=${paypal.FUNDING.MYBANK}`;
            }
          });
        }
      });
    },
    fields: {
      /* fields prefill info (optional) */
      name: {
        value: "John Doe",
      },
    },
  })
  .render("#mybank-container");
```

#### Second page of the checkout flow

Based on the payment method selected on the first page, this example renders only the payment button along with the order details on the page. To complete checkout, the buyer clicks the payment button, authorizes, and confirms payment. You get the code to render the payment button in [step 4](#render-payment-button) .

![Multipage,Flow,Page,2](assets/paypal-apm-multipage-2.png)For style parameters, please reference this style page: [Custom style for payment fields](/docs/checkout/apm/reference/style/)

#### **`Payment button`**

```javascript
paypal
  .Buttons({
    fundingSource: paypal.FUNDING.MYBANK,
    style: {
      label: "pay",
    },
    createOrder() {
      return fetch("/my-server/create-paypal-order", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // use the "body" param to optionally pass additional order information
        // like product skus and quantities
        body: JSON.stringify({
          cart: [
            {
              sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
              quantity: "YOUR_PRODUCT_QUANTITY",
            },
          ],
        }),
      })
        .then((response) => response.json())
        .then((order) => order.id);
    },
    onApprove(data) {
      return fetch("/my-server/capture-paypal-order", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          orderID: data.orderID,
        }),
      })
        .then((response) => response.json())
        .then((orderData) => {
          // Successful capture! For dev/demo purposes:
          console.log(
            "Capture result",
            orderData,
            JSON.stringify(orderData, null, 2),
          );
          const transaction = orderData.purchase_units[0].payments.captures[0];
          console.log("Transaction Status:", transaction.status);
          console.log("Transaction ID:", transaction.id);
          // When ready to go live, remove the alert and show a success message within this page. For example:
          // const element = document.getElementById('paypal-button-container');
          // element.innerHTML = '<h3>Thank you for your payment!</h3>';
          // Or go to another URL:  window.location.href = 'thank_you.html';
        });
    },
    onCancel(data, actions) {
      console.log(`Order Canceled - ID: ${data.orderID}`);
    },
    onError(err) {
      console.error(err);
    },
  })
  .render("#mybank-btn");
```

- createOrder Implement the createOrder function to allow the JavaScript SDK to submit buyer information and set up the transaction on the click of the button. **Note:**Create MyBank orders in EUR currency. Use your server-side [Create order](/docs/api/orders/v2/#orders_create) call to set up the details of a one-time transaction including the amount, line item detail, and more.If order creation fails, the Orders API can [return an error](https://developer.paypal.com/api/rest/reference/orders/v2/errors/) in the console. After order creation, orders are confirmed with buyer selected payment source. If the order cannot be processed with the selected payment source, the relevant errors are returned in the console.

- onCancel Implement the optional onCancel() function to show a cancellation page or return to the shopping cart.

- onError Implement the optional onError() function to handle errors and display generic error message or page to the buyers. This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

Implement the onApprove function, which is called after the buyer approves the transaction.

Captures the funds from the transaction and shows a message to the buyer to let them know the transaction is successful. The method is called after the buyer approves the transaction on paypal.com.

Because this is a client-side call, PayPal calls the [Orders API](/docs/api/orders/v2/#orders_capture) on your behalf, so you don't need to provide the headers and body.

capture() - Promise returning the [order details](/docs/api/orders/v2/#orders-capture-response) .

#### **`PayPal MyBank button`**

```javascript
paypal
  .Buttons({
    fundingSource: paypal.FUNDING.MYBANK,
    createOrder() {
      return fetch("/my-server/create-paypal-order", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        // use the "body" param to optionally pass additional order information
        // like product skus and quantities
        body: JSON.stringify({
          cart: [
            {
              sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
              quantity: "YOUR_PRODUCT_QUANTITY",
            },
          ],
        }),
      })
        .then((response) => response.json())
        .then((order) => order.id);
    },
    onApprove(data) {
      return fetch("/my-server/capture-paypal-order", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          orderID: data.orderID,
        }),
      })
        .then((response) => response.json())
        .then((orderData) => {
          // Successful capture! For dev/demo purposes:
          console.log(
            "Capture result",
            orderData,
            JSON.stringify(orderData, null, 2),
          );
          const transaction = orderData.purchase_units[0].payments.captures[0];
          console.log("Transaction Status:", transaction.status);
          console.log("Transaction ID:", transaction.id);
          // When ready to go live, remove the alert and show a success message within this page. For example:
          // const element = document.getElementById('paypal-button-container');
          // element.innerHTML = '<h3>Thank you for your payment!</h3>';
          // Or go to another URL:  window.location.href = 'thank_you.html';
        });
    },
  })
  .render("#mybank-button-container");
//This function displays payment buttons on your web page.
```

For the capture call details and example responses, see [Capture payment for order](/docs/api/orders/v2/#orders_capture) in the Orders API reference.

If order capture fails, the Orders API can [return an error](https://developer.paypal.com/api/rest/reference/orders/v2/errors/) in the console.

## Handle webhook events

A webhook handler is a script you create on your server that completes specific actions on webhooks that hit your listener URL.

- We recommend subscribing to the CHECKOUT.ORDER.APPROVED webhook event in case a customer accidentally closes the browser and exits the checkout process after approving the transaction through their APM but before finalizing the transaction on your site.
- We also recommend subscribing to the CHECKOUT.ORDER.DECLINED webhook event to receive notifications of any other failure scenarios. This webhook event passes a failure reason code and error message to indicate what caused the error.
- Listen for the CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook as an indication that an approved order wasn't captured within the capture window resulting in a cancellation of the order and a refund the buyer's account. Then notify your buyer of the problem and the reversed order.
- PAYMENT.CAPTURE.PENDING , PAYMENT.CAPTURE.COMPLETED , and PAYMENT.CAPTURE.DENIED webhooks indicate capture status.

See [Subscribe to checkout webhooks](/docs/checkout/apm/reference/subscribe-to-webhooks/) for more information.

Here are some additional resources as you create webhook handler code:

- [Webhook Management API](/docs/api/webhooks/v1/) - Manage webhooks, list event notifications, and more.
- Webhook events - [Checkout webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#checkout-buyer-approval) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) - Other order-related webhooks.

- [Show order details endpoint](/docs/api/orders/v2/#orders_get) - Determine the status of an order.

## Sample integration

See a sample MyBank integration in the [PayPal GitHub repository](https://github.com/paypal-examples/mybank-paypal-payment-js-sdk) .

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
