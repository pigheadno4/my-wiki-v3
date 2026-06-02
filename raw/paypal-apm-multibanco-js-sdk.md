---
title: Integrate Multibanco using the JavaScript SDK
slug: /docs/checkout/apm/multibanco/js-sdk/
createTime: "2024-12-06T05:37:05.329Z"
updateTime: "2025-02-20T06:17:48.588Z"
---

# Integrate Multibanco using the JavaScript SDK

Merchants can use PayPal-hosted UI components, called payment fields, to collect payment information for alternative payment methods.

## Know before you code

- Request approval to enable Multibanco by visiting these sandbox and live links: - Sandbox: [https://www.sandbox.paypal.com/bizsignup/entry?product=multibanco&capabilities=MULTIBANCO&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=multibanco&capabilities=MULTIBANCO&country.x=)
- Live: [https://www.paypal.com/bizsignup/add-product?product=multibanco&capabilities=MULTIBANCO&country.x=&lt;merchant's country&gt;](https://www.paypal.com/bizsignup/add-product?product=multibanco&capabilities=MULTIBANCO&country.x=)

- Partners: Be sure to onboard your merchants upfront, [before they accept payments](/docs/multiparty/seller-onboarding/before-payment/) . Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.

**Note:**The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can reuse that code with adjustments for this payment method.- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get your sandbox account information from the Developer Dashboard: - Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.

- Client Secret: Authorizes an app in your sandbox. Keep this secret safe and don't share it.
- Business account credentials.

- Make sure the preference for receiving payments in your PayPal business account is set to accept and convert them to the default currency. To verify, in your profile select **Account Settings &gt; Payment preferences &gt; Block payments** and select **Update** to mark this preference.
- This client-side and server-side integration uses the following: - [PayPal JavaScript SDK](https://developer.paypal.com/sdk/js/)
- [Webhooks Management REST API](https://developer.paypal.com/api/webhooks/v1/)
- [Orders REST API](https://developer.paypal.com/api/orders/v2/)

- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - Listen for the CHECKOUT.ORDER.APPROVED webhook in order to retrieve order details.
- Listen for the PAYMENT.CAPTURE.PENDING , PAYMENT.CAPTURE.COMPLETED , and PAYMENT.CAPTURE.DENIED webhooks, which indicate payment capture status.

- By adding funding sources to your checkout integration, you agree to the [PayPal alternative payment methods agreement](https://www.paypal.com/us/webapps/mpp/ua/apm-tnc) . This is in addition to the user agreement applicable to the country in which your business is physically located.

## To get started

### Run in Postman

Use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](https://developer.paypal.com/api/rest/postman/) .

### Get up and running in GitHub Codespaces

GitHub Codespaces are cloud-based development environments where you can code and test your PayPal integrations. [Learn more](https://developer.paypal.com/api/rest/sandbox/codespaces/) .

Add or update the JavaScript SDK script on your web page.

#### **`Add PayPal JavaScript SDK`**

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=multibanco&currency=EUR"></script>
```

This table lists the parameters you pass to the JavaScript SDK.

| **Query param** | **Default** | **Description** |
| client-id | none | Your PayPal REST client ID. This identifies your PayPal account and determines where transactions are paid. |
| components | buttons | A comma-separated list of components to enable. Thebuttons,payment-fields,marks, andfunding-eligibilitycomponents are required for payment fields components. |
| enable-funding | none | The enabled payment methods to show in buttons and marks. **Note:**By default, PayPal JavaScript SDK provides smart logic to display only appropriate marks and buttons for the current buyer. This optional parameter bypasses the buyer country check for desired payment methods. For example:src=[https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo](https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo) |
| currency | USD | This is the currency for the payment. This value needs to match the currency used when creating the order. |
| locale | automatic | The locale renders components. By default PayPal detects the correct locale for the buyer based on their geolocation and browser preferences. It is recommended to pass this parameter with a[supported locale](https://developer.paypal.com/sdk/js/configuration/#link-locale)if you need the PayPal buttons to render in the same language as the rest of your site. |
| intent | capture | The intent for the transaction. This determines whether the funds are captured immediately while the buyer is present on the page. |
| commit | true | This indicates that the final amount won't change after the buyer returns to your site from PayPal. |
| vault | false | Whether the payment information in the transaction will be saved. Save your customers' payment information for billing agreements, subscriptions, or recurring payments. Marking this parameterfalseshows all funding sources, including payment methods that can't be saved. |

See additional, [optional parameters](https://developer.paypal.com/sdk/js/configuration/) .

You can use a [mark integration](/docs/checkout/standard/customize/display-payment-methods/) for payment fields components to present the payment method options to the buyer as radio buttons.

![image](assets/paypal-apm-multibanco-mark.png)

#### **`Render payment mark`**

```javascript
paypal
  .Marks({
    fundingSource: paypal.FUNDING.MULTIBANCO,
  })
  .render("#multibanco-mark");
```

Payment fields offer easy integration to collect payment information from buyers. Fields dynamically render based on the selected funding source and you can customize the fields to align with your brand.

The MULTIBANCO payment fields collect first name and last name.

If there are validation errors in the input fields, they'll show on the click of the button.

#### **`Render payment fields`**

```javascript
paypal
  .PaymentFields({
    fundingSource: paypal.FUNDING.MULTIBANCO,
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
  .render("#multibanco-container");
```

For style parameters, please reference this style page: [Custom style for payment fields](/docs/checkout/apm/reference/style/)

#### **`Render payment button`**

```javascript
paypal
  .Buttons({
    fundingSource: paypal.FUNDING.MULTIBANCO,
    style: {
      label: "pay",
    },
    createOrder() {
      return fetch("/my-server/create-paypal-order", {
        method: "post",
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
        method: "post",
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
      /* Incomplete checkout. Buyer closed the window before order confirmation. */
      /* Show a message to restart the checkout process. */
      console.log(`Order Canceled - ID: ${data.orderID}`);
    },
    onError(err) {
      console.error(err);
    },
  })
  .render("#multibanco-btn");
```

Use paypal.Buttons().isEligible() to check if the funding source is eligible.

#### **`Render payment button`**

```javascript
var mark = paypal.Marks({
  fundingSource: paypal.FUNDING.MULTIBANCO,
});
var fields = paypal.PaymentFields({
  fundingSource: paypal.FUNDING.MULTIBANCO,
});
var button = paypal.Buttons({
  fundingSource: paypal.FUNDING.MULTIBANCO,
});

if (button.isEligible()) {
  mark.render("#multibanco-mark");
  fields.render("#multibanco-container");
  button.render("#multibanco-btn");
}
```

- createOrder Implement the createOrder function to allow the JavaScript SDK to submit buyer information and set up the transaction on the click of the button.

  **Note:**Create Bancontact orders in EUR currency. Use your server-side [Create order](/docs/api/orders/v2/#orders_create) call to set up the details of a one-time transaction including the amount, line item detail, and more.

  If order creation fails, the Orders API [returns an error](https://developer.paypal.com/api/rest/reference/orders/v2/errors/) in the console.

  After order creation, orders are confirmed with the buyer-selected payment source. If the order cannot be processed with the selected payment source, relevant errors are returned in the console.

- onCancel Implement the optional onCancel() function to show a cancellation page or return to the shopping cart.

- onError Implement the optional onError() function to handle errors and display generic error message or page to the buyers. This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

## Handle webhook events

A webhook handler is a script you create on your server that completes specific actions on webhooks that hit your listener URL.

- CHECKOUT.ORDER.APPROVED - Listen for this webhook to retrieve order details, including the BARCODE_URL for the voucher. Use this URL to send the voucher in emails or to display it again. Order capture is performed automatically. No additional code required.
- PAYMENT.CAPTURE.PENDING - The funds for this payment were not yet credited to the payee's PayPal account. The buyer has not yet completed the transaction.
- PAYMENT.CAPTURE.COMPLETED - The funds for this payment were credited to the payee's PayPal account. The buyer completed the transaction and goods can be delivered.
- PAYMENT.CAPTURE.DENIED - The funds could not be captured. The buyer did not complete the transaction before the voucher's expiration.

See [Subscribe to checkout webhooks](https://developer.paypal.com/beta/alternative-payment-methods-js-sdk/additional-information/subscribe-to-webhooks/) for more information.

Here are some additional resources as you create webhook handler code:

- [Webhook Management API](https://developer.paypal.com/api/webhooks/v1/) - Manage webhooks, list event notifications, and more.
- Webhook events - [Checkout webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#checkout-buyer-approval) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) - Other order-related webhooks.

- [Show order details endpoint](/docs/api/orders/v2/#orders_get) - Determine the status of an order.

## Next steps

### Test integration

Test the integration in the PayPal sandbox environment.

### Go live

Take your application live in the PayPal production environment once testing is successful.
