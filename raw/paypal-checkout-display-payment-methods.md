---
title: 'Display other payment methods '
slug: /docs/checkout/standard/customize/display-payment-methods/
createTime: '2024-02-23T23:17:30.935Z'
updateTime: '2025-05-13T15:25:29.444Z'
---

# Display other payment methods

Use radio buttons to present other funding sources alongside PayPal.

You can also use marks to automatically show images for all PayPal payment options, such as PayPal, Venmo, Pay Later, and debit and credit cards. For more information, see Marks in the JavaScript SDK reference.

## Know before you code

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

### You need a developer account to get sandbox credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- **Client ID**: Authenticates your account with PayPal and identifies an app in your sandbox.
- **Client secret**: Authorizes an app in your sandbox. Keep this secret safe and don't share it.

You need a combination of PayPal and third-party tools:

- Android SDK: Adds PayPal-supported payment methods for Android.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

## How it works

- You add marks and radio buttons to your checkout page that show PayPal and other payment options.
- Your payer selects a payment method.
- Other payment methods are hidden.

Steps:

- Modify the components in your script so they contain `buttons` and `marks`.
- Create a label for PayPal.
- Show the PayPal marks and buttons with the PayPal radio button.
- Create a label and radio button for other payment methods.
- Add an event listener to check for changes to the radio buttons.
- Show and hide payment options based on the payer's selection.

#### Show PayPal and other payment methods

```javascript
// Add the PayPal JavaScript SDK with both buttons and marks components
<script src="https://www.paypal.com/sdk/js?client-id=test&components=buttons,marks"></script>
// Render the radio buttons and marks
<label>
  <input type="radio" name="payment-option" value="paypal" checked>
  <img src="paypal-mark.jpg" alt="Pay with PayPal">
</label>
<label>
  <input type="radio" name="payment-option" value="alternate">
  <div id="paypal-marks-container"></div>
</label>
<div id="paypal-button-container"></div>
<div id="alternate-button-container">
  <button>Pay with a different method</button>
</div>
<script>
  // Render the PayPal marks
  paypal.Marks().render('#paypal-marks-container');
  // Render the PayPal buttons
  paypal.Buttons().render('#paypal-button-container');
  // Listen for changes to the radio buttons
  document.querySelectorAll('input[name=payment-option]')
    .forEach(function (el) {
      el.addEventListener('change', function (event) {
        // If PayPal is selected, show the PayPal button
        if (event.target.value === 'paypal') {
          document.body.querySelector('#alternate-button-container')
            .style.display = 'none';
          document.body.querySelector('#paypal-button-container')
            .style.display = 'block';
        }
        // If alternate funding is selected, show a different button
        if (event.target.value === 'alternate') {
          document.body.querySelector('#alternate-button-container')
            .style.display = 'block';
          document.body.querySelector('#paypal-button-container')
            .style.display = 'none';
        }
      });
    });
  // Hide non-PayPal button by default
  document.body.querySelector('#alternate-button-container')
    .style.display = 'none';
</script>
```
