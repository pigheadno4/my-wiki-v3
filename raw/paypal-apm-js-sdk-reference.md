---
title: JS SDK Reference for payment fields
slug: /docs/checkout/apm/reference/js-sdk-params-payment-fields/
createTime: "2024-08-15T07:26:18.631Z"
updateTime: "2025-05-14T10:44:09.583Z"
---

# JS SDK Reference for payment fields

| **Query param** | **Default** | **Description** |
| client-id | n/a | Your PayPal REST client ID. This identifies your PayPal account and determines where transactions are paid. |
| components | buttons | A comma-separated list of components to enable. Thebuttons,payment-fields,marks, andfunding-eligibilitycomponents are required for payment fields components. |
| enable-funding | none | Funding sources to allow to be shown in the buttons and marks. By default, PayPal JavaScript SDK provides smart logic to display only appropriate marks and buttons for the current buyer. This optional parameter bypasses the buyer country check for desired payment methods.

For example:

[https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=ideal,bancontact](https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=ideal,bancontact) |
| currency | USD | Currency of the transaction. |
| locale | automatic | By default, PayPal detects the preferred locale for the buyer based on their geolocation and browser preferences. It is recommended to pass this parameter with a[supported locale](/sdk/js/configuration/)if you would like the payment fields components to render in the same language as the rest of your site. |
| intent | capture | The funds are captured immediately, while the buyer is present on your site. |
| commit | true | This indicates that the final amount won't change after the buyer returns from PayPal to your site. |
| vault | false | Displays all funding sources including those that don’t support vaulting. |

## paypal.Buttons(options)

- [style](#style)
- [createOrder](#createorder)
- [onApprove](#onapprove)
- [onCancel](#oncancel)
- [onError](#onerror)

### style

Customize your buttons by passing in the style option.

paypal.Buttons({
style: {
layout: 'vertical',
label: 'paypal'
}
}).render('#paypal-button-container');**Note:** Alternative payment methods support only vertical layout.

See additional, [optional parameters](/sdk/js/configuration/) .

### createOrder

The createOrder parameter sets up the details of the transaction. It's called when the buyer clicks the PayPal button, which launches the PayPal Checkout window where the buyer logs in and approves the transaction on the paypal.com website.

&lt;script&gt;
paypal.Buttons({
// Order is created on the server and the order id is returned
createOrder() {
return fetch("/my-server/create-paypal-order", {
method: "post",
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
.then((response) =&gt; response.json())
.then((order) =&gt; order.id);
},
}).render('#paypal-button-container');
&lt;/script&gt;### onApprove
The onApprove function is called after the buyer approves the transaction.

Make the [capture call from your server](/docs/api/orders/v2/#orders_capture) to capture the funds from the transaction and show a message to the buyer to let them know the transaction is successful.

### onCancel

When a buyer cancels a payment, they typically return to the parent page. You can instead use the onCancel function to show a cancellation page or return to the shopping cart.

### Data attributes

orderId —
ID of the order.

paypal.Buttons({
onCancel: function (data) {
// Show a cancel page, or return to cart
}
}).render('#paypal-button-container');### onError
If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the onError callback:

paypal.Buttons({
onError: function (err) {
// For example, redirect to a specific error page
window.location.href = "/your-error-page-here";
}
}).render('#paypal-button-container');**Note:** This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

### paypal.Buttons().isEligible

Before rendering marks and payment fields, you can use paypal.Buttons().isEligible to check if the funding source is eligible.

// Loop over each funding source / payment method
paypal.getFundingSources().forEach(function(fundingSource) {

// Initialize the buttons
var button = paypal.Buttons({
fundingSource: fundingSource
});

// Check if the button is eligible
if (button.isEligible()) {

    // Render the standalone button for that funding source
    button.render('#paypal-button-container');

}
});## Funding
This table includes the available alternative payment methods.

| Funding source            | Payment button    |
| ------------------------- | ----------------- |
| paypal.FUNDING.BANCONTACT | Bancontact        |
| paypal.FUNDING.EPS        | eps               |
| paypal.FUNDING.GIROPAY    | giropay (Legacy)1 |
| paypal.FUNDING.IDEAL      | iDEAL             |
| paypal.FUNDING.BLIK       | BLIK              |
| paypal.FUNDING.MYBANK     | MyBank            |
| paypal.FUNDING.P24        | Przelewy24        |
| paypal.FUNDING.SOFORT     | Sofort (Legacy)2  |
| paypal.FUNDING.APPLEPAY   | Apple Pay         |

- **1** : **Important:** giropay was sunset on June 30, 2024. PayPal will not support giropay payments starting July 1, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/giropay-deprecation-help1183) .

- **2** : **Important:** Sofort was sunset on April 18, 2024. PayPal will not support Sofort payments starting April 19, 2024. Offer your users PayPal wallet and other alternative payment methods. [Learn more](https://www.paypal.com/us/cshelp/article/sofort-deprecation-help1145) .
