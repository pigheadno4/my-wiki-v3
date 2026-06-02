<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-with-venmo/integrate/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Pay with Venmo integration
slug: /docs/checkout/pay-with-venmo/integrate/
createTime: '2024-02-20T02:09:57.130Z'
updateTime: '2025-05-09T15:51:44.903Z'
---


# Pay with Venmo integration

Add the Venmo button to your Checkout integration.



## Know before you code 
- If you are a new merchant, sign up for a [PayPal business account](https://www.paypal.com/us/business) .
- Complete [Get started](https://developer.paypal.com/api/rest/) to set up your PayPal account, client ID, and sandbox emails for testing.
- Complete a [PayPal Checkout integration](https://developer.paypal.com/docs/checkout/standard/) .


- Add the JavaScript SDK code to display the Venmo button on your product and checkout pages.
- Determine where the SDK should render the Venmo button. Use button options to control the layout of the button.


#### **`Add Venmo button`**
```javascript
<!-- Set up a container element for the button -->
<div id="paypal-button-container"></div>

<!-- Include the PayPal JavaScript SDK. Replace `YOUR_CLIENT_ID` with your client ID.-->
<!-- Note that `enable-funding=venmo` is added as a query parameter -->
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&enable-funding=venmo"></script>

<script>
  // Render the Venmo button into #paypal-button-container
  paypal.Buttons().render('#paypal-button-container')
</script>
```
### Step result

## Test and go live 
Venmo is available in the US only. To simulate the Venmo button in the PayPal sandbox, add the buyer-country=US parameter to your JS SDK code.

Pay with Venmo is a mobile experience, so ensure you have the Venmo iOS or Android app installed. You can test this featureon an iOS Safari or Android Chrome browser.

In the sandbox environment, you can test your integration without moving any money. For more information on testing Venmo, see [Test Venmo in sandbox](https://developer.paypal.com/docs/checkout/pay-with-venmo/test/) .


### Enable Venmo as a funding source
Venmo isn't displayed as a payment option in Checkout integrations by default. Add enable-funding=venmo as a query parameter to your JavaScript SDK &lt;script&gt; to display Venmo as a payment option.

### Allow for Venmo placement
If you have an existing vertical button stack, an additional Venmo button renders under the stack. Make sure you leave enough room on your page for the Venmo button.

### Display funding source used
If you have a confirmation page or a notification to the user that shows the funding source that was used, use an onClick handler to display Venmo in the confirmation notification.


#### **`fundingSource`**
```javascript
let fundingSource

paypal.Buttons({
  onClick: (data) => {
    // fundingSource = "venmo"
    fundingSource = data.fundingSource

    // Use this value to determine what funding source was used to pay
    // Update your confirmation pages and notifications from "PayPal" to "Venmo"
  },
})
```
