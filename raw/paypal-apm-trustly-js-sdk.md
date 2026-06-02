---
title: Integrate Trustly using the JavaScript SDK
slug: /docs/checkout/apm/trustly/js-sdk/
createTime: "2024-12-09T07:10:39.565Z"
updateTime: "2025-08-17T21:48:46.050Z"
---

# Integrate Trustly using the JavaScript SDK

Use the JavaScript SDK to render payment fields and buttons, and process payments with the Orders API.

### Buyer experience

## Know before you code

- Request approval to enable Trustly by visiting these sandbox and live links: - Sandbox: [https://www.sandbox.paypal.com/bizsignup/entry?product=trustly&capabilities=TRUSTLY&country.x=&lt;merchant's country&gt;](https://www.sandbox.paypal.com/bizsignup/entry?product=trustly&capabilities=TRUSTLY&country.x=)
  - Live: [https://www.paypal.com/bizsignup/add-product?product=trustly&capabilities=TRUSTLY&country.x=&lt;merchant's country&gt;](https://www.paypal.com/bizsignup/add-product?product=trustly&capabilities=TRUSTLY&country.x=)

- Partners: Be sure to onboard your merchants upfront, [before they accept payments](/docs/multiparty/seller-onboarding/before-payment/) . Onboarding after making payments, specifically Progressive Onboarding, isn't supported for alternative payment methods.

Note: The integration steps for implementing alternative payment methods are similar. If you've integrated another alternative payment method before, you can likely reuse that code with adjustments for this payment method.- Complete the steps in [Get started](https://developer.paypal.com/api/rest/) to get your sandbox account information from the Developer Dashboard: - Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.

- Client Secret: Authorizes an app inyour sandbox. Keep this secret safe and don't share it.
- Business account credentials.

- Make sure the preference for receiving payments in your PayPal business account is set to accept and convert them to the default currency. To verify, in your profile select **Account Settings &gt; Payment preferences &gt; Block payments** and select **Update** to mark this preference.
- This client-side and server-side integration uses the following: - [PayPal JavaScript SDK](https://developer.paypal.com/sdk/js/)
- [Webhooks Management REST API](/docs/api/webhooks/v1/)
- [Orders REST API](/docs/api/orders/v2/)

- Make sure you're [subscribed to the following webhook events](/docs/checkout/apm/reference/subscribe-to-webhooks/) : - Listen for the CHECKOUT.ORDER.APPROVED webhook in order to retrieve order details.
- Listen for the PAYMENT.CAPTURE.PENDING , PAYMENT.CAPTURE.COMPLETED , and PAYMENT.CAPTURE.DENIED webhooks , which indicate payment capture status.

- By adding funding sources to your checkout integration, you agree to the [PayPal alternative payment methods agreement](https://www.paypal.com/us/webapps/mpp/ua/apm-tnc) . This is in addition to the user agreement applicable to the country in which your business is physically located.

## To get started

### Run in Postman

Use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](https://developer.paypal.com/api/rest/postman/) .

### Get up and running in GitHub Codespaces

GitHub Codespaces are cloud-based development environments where you can code and test your PayPal integrations. [Learn more](https://developer.paypal.com/api/rest/sandbox/codespaces/) .

Add or update the JavaScript SDK script on your web page.

#### **`Add PayPal JavaScript SDK code /docs/checkout/apm/trustly/js-sdk`**

```html
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&components=buttons,payment-fields,marks,funding-eligibility&enable-funding=trustly&currency=EUR"></script>
```

This table lists the parameters you pass to the JavaScript SDK.

| **Query param** | **Default** | **Description** |
| client-id | none | Your PayPal REST client ID. This identifies your PayPal account and determines where transactions are paid. |
| components | buttons | A comma-separated list of components to enable. Thebuttons,payment-fields,marks, andfunding-eligibilitycomponents are required for payment fields components. |
| enable-funding | none | The enabled payment methods to show in buttons and marks. **Note:**By default, PayPal JavaScript SDK provides smart logic to display only appropriate marks and buttons for the current buyer. This optional parameter bypasses the buyer country check for desired payment methods.For example: src=" [https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo](https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo) " |
| currency | USD | This is the currency for the payment. This value needs to match the currency used when creating the order. |
| locale | automatic | The locale renders components. By default PayPal detects the correct locale for the buyer based on their geolocation and browser preferences. It is recommended to pass this parameter with a[supported locale](https://developer.paypal.com/sdk/js/configuration/#link-locale)if you need the PayPal buttons to render in the same language as the rest of your site. |
| intent | capture | The intent for the transaction. This determines whether the funds are captured immediately while the buyer is present on the page. |
| commit | true | This indicates that the final amount won't change after the buyer returns to your site from PayPal. |
| vault | false | Whether the payment information in the transaction will be saved. Save your customers' payment information for billing agreements, subscriptions, or recurring payments. Marking this parameterfalseshows all funding sources, including payment methods that can't be saved. |

See additional, [optional parameters](https://developer.paypal.com/sdk/js/configuration/) .

You can use a [mark integration](/docs/checkout/standard/customize/display-payment-methods/) for payment field components to present the buyer's payment method options as radio buttons.

#### **`Payment mark`**

```javascript
paypal
  .Marks({
    fundingSource: paypal.FUNDING.TRUSTLY,
  })
  .render("#trustly-mark");
```

## Render payment fields

Integrate payment fields to collect payment information from buyers. Fields dynamically render based on the selected payment source. You can customize the fields to align with your brand.

You can choose from the following checkout flows:

- [Single page](#single-page)
- [Multi-page](#multi-page)

### Single page

The Trustly payment fields collect first name and last name.

If there are validation errors in the input fields, they'll show when the buyer selects the button.

#### **`Payment fields`**

```javascript
paypal
  .PaymentFields({
    fundingSource: paypal.FUNDING.TRUSTLY,
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
  .render("#trustly-container");
```

For style parameters, please reference this style page: [Custom style for payment fields](/docs/checkout/apm/reference/style/)

### Multi-page

A multi-page checkout flow spreads the checkout steps into two or more pages. This experience is applicable when an order details page needs to be shown to the buyer before an order is placed.

**Tip:**German merchants can leverage the multi-page flow to comply with local regulations.

#### First page of the checkout flow

This example renders the mark and payment fields, but not the payment button, on your checkout page.

#### **`Payment mark`**

```javascript
paypal
  .Marks({
    fundingSource: paypal.FUNDING.TRUSTLY,
  })
  .render("#trustly-mark");
```

#### **`Payment fields`**

```javascript
paypal.PaymentFields({
  fundingSource: paypal.FUNDING.TRUSTLY,
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

      if (paymentSource === paypal.FUNDING.TRUSTLY) {
        e.preventDefault();

        actions.validate().then((valid) => {
          if (valid) {
            window.location.href = `/second-page.html?payment-option=${paypal.FUNDING.TRUSTLY}`;
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
.render("#trustly-container");****
```

#### Second page of the checkout flow

Based on the payment method selected on the first page, the payment button displays, along with the order details on the second page. To complete checkout, your buyer clicks the payment button, authorizes, and confirms payment. You get the code to render the payment button in [step 4](#render-payment-button) .

For style parameters, please reference this style page: [Custom style for payment fields](/docs/checkout/apm/reference/style/)

#### **`Render payment button`**

```javascript
paypal
  .Buttons({
    fundingSource: paypal.FUNDING.TRUSTLY,
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
      // You do not need to capture the order, as the order is already captured
      // You can show a "Thank you" message and listen for the PAYMENT.CAPTURE.COMPLETED or PAYMENT.CAPTURE.DENIED webhooks to get the capture status
      // To show a "Thank you" message you can do
      // const element = document.getElementById('paypal-button-container');
      // element.innerHTML = '<h3>Thank you for your payment!</h3>';
      // Or go to another URL:  window.location.href = 'thank_you.html';
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
  .render("#trustly-btn");
```

- createOrder Implement the createOrder function to allow the JavaScript SDK to submit buyer information and set up the transaction when the buyer selects the button. **Note:**Create Trustly orders in theEUR,DKK,SEK,GBP, orNOKcurrency. This currency must match thecurrencyparameter passed in the JavaScript SDK&lt;script&gt;tag during**Add PayPal JavaScript SDK.** Use your server-side [Create order](/docs/api/orders/v2/#orders_create) call to set up the details of a one-time transaction, such as the amount, line item details, and shipping information.
  If order creation fails, the Orders API can [return an error](https://developer.paypal.com/api/rest/reference/orders/v2/errors/) in the console.

After order creation, orders are confirmed with the buyer's selected payment source. If the order can't be processed with the selected payment source, the relevant errors show up in the console.

- onCancel() Implement the optional onCancel() function to show a cancellation page or return to the shopping cart.

- onError() Implement the optional onError() function to handle errors and display a generic error message or page to the buyer. This error handler is a catch-all. Errors at this point aren't expected to be handled beyond showing a generic error message or page.

Use paypal.Buttons().isEligible() to check if the payment source is eligible.

#### **`Integrate Trustly`**

```javascript
var mark = paypal.Marks({
  fundingSource: paypal.FUNDING.TRUSTLY,
});
var fields = paypal.PaymentFields({
  fundingSource: paypal.FUNDING.TRUSTLY,
});
var button = paypal.Buttons({
  fundingSource: paypal.FUNDING.TRUSTLY,
});
if (button.isEligible()) {
  mark.render("#trustly-mark");
  fields.render("#trustly-container");
  button.render("#trustly-btn");
}
```

## Handle webhook events

Set up a webhook handler on your server to manage and respond to any webhooks that hit your listener URL.

- CHECKOUT.ORDER.APPROVED - Listen for this webhook to retrieve order details. Order capture is performed automatically. No additional code required.
- PAYMENT.CAPTURE.PENDING - Listen for this webhook to confirm that payment initialization was successful, the payment is pending, and the buyer needs to complete the transaction. Note that the funds have not yet been credited to the payee's PayPal account.
- PAYMENT.CAPTURE.COMPLETED - Listen for this webhook to confirm that the money for this payment was credited to the payee's PayPal account. The buyer completed the transaction, and you can ship the order at this point.
- PAYMENT.CAPTURE.DENIED - Listen for this webhook to confirm that the money couldn't be captured. The buyer didn't complete the payment before the voucher's expiration, or the bank declined the payment. You can cancel the order at this point.

See [Subscribe to checkout webhooks](https://developer.paypal.com/beta/apm-beta/additional-information/subscribe-to-webhooks/) for more information.

Here are some additional resources as you create webhook handler code:

- [Webhook Management API](/docs/api/webhooks/v1/) - Manage webhooks, list event notifications, and more.
- Webhook events - [Checkout webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/#checkout-buyer-approval) - Checkout buyer approval-related webhooks.
- [Order webhook events](https://developer.paypal.com/api/rest/webhooks/event-names/) - Other order-related webhooks.

- [Show order details endpoint](/docs/api/orders/v2/#orders_get) - Determine the status of an order.

**Note:**Once the buyer authorizes the payment, payment completion happens within 7 days, depending on the bank used for the payment. You should wait until payment completion to ship the goods.

If createOrder in [Step 4](#render-payment-button) is unsuccessful and returns an HTTP 422 Unprocessable Entity status code, the JSON response body should contain an error code in the `issue` parameter.

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

#### **`Sample request`**

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ACCESS-TOKEN' \
--header 'PayPal-Request-Id: PAYPAL-REQUESTID' \
--data-raw '{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
            "amount": {
                "currency_code": "SEK",
                "value": "100.00"
            }
        }
    ],
    "payment_source": {
        "trustly": {
            "country_code": "NL",
            "name": "John Doe"
        }
    },
    "processing_instruction": "ORDER_COMPLETE_ON_PAYMENT_APPROVAL",
    "application_context": {
        "locale": "en-NL",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
    }
}'
```

#### **`Sample response `**

```javascript
{
    "name": "UNPROCESSABLE_ENTITY222",
    "details": [
        {
            "issue": "CURRENCY_NOT_SUPPORTED_BY_PAYMENT_SOURCE",
            "description": "The currency_code provided in the order cannot be processed by the provided payment source."
        }
    ],
    "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
    "debug_id": "eccdbdf073eea",
    "links": [
        {
            "href": "https://developer.paypal.com/docs/api/orders/v2/#error-CURRENCY_NOT_SUPPORTED_BY_PAYMENT_SOURCE",
            "rel": "information_link",
            "method": "GET"
        }
    ]
}
```

### Step result

An unsuccessful request results in the following:

- A return status code of HTTP 422 Unprocessable Entity .
- A JSON response body that contains an error code in the issue parameter and the error description in the description parameter.

## Next steps

- [Handle uncaptured payments](https://developer.paypal.com/beta/apm-beta/additional-information/handle-uncaptured-payments/) - Listen for the CHECKOUT.PAYMENT-APPROVAL.REVERSED webhook as an indication that an approved order wasn't captured for certain reasons resulting in a cancellation of the order and a refund the buyer's account. Then notify your buyer of the problem and the reversed order.
- [Test in PayPal sandbox](https://developer.paypal.com/api/rest/sandbox/) .
- [Go live in PayPal's production environment](https://developer.paypal.com/reference/production/) .
