<!-- Source URL: https://developer.paypal.com/docs/checkout/pay-with-venmo/ -->
<!-- Fetched: 2026-04-14 -->

---
title: Pay with Venmo
slug: /docs/checkout/pay-with-venmo/
createTime: '2024-02-17T00:01:54.686Z'
updateTime: '2025-05-08T14:54:03.634Z'
---


# Pay with Venmo

Add Venmo as a payment button to an existing Checkout integration to allow payers to checkout with Venmo.

When you integratewith Venmo, your payers get:

- Aseamless checkout process.
- Choice of any payment method added to the Venmo wallet.
- The ability to split purchases among friends.
- The option to share purchase information on a social feed.



## How it works 
Your existing PayPal buttons display a Venmo button. When payers select Venmo, they can pay in the Venmo app.

Payers can use Venmo on the same pages they use PayPal, including your product page, cart page, and checkout page.

**Note:** Payers must have the Venmo app installed.

### Mobile workflow
Payers can switch to the Venmo app to authorize and complete the payment.

![Payer,experience,on,mobile](assets/paypal-venmo-mobile-flow.png)

- The payer taps the Venmo button. Their mobile device switches to the Venmo app to complete payment.
- The payer taps **Pay** .
- The payer is routed back to your website.

**Note:** Payers on mobile devices must use Safari on iOS or Chrome on Android.

### Desktop browser checkout flow
Payers can scan a QR code using their Venmo app to authorize and complete the payment.

- The payer clicks the Venmo button on the desktop to generate a QR code.
![](assets/paypal-venmo-desktop-button.jpg)![](assets/paypal-venmo-desktop-qr.jpg) 

- The payer scans the QR code from the Venmo app on a mobile device or using the mobile device camera.
![](assets/paypal-venmo-qr-scan.png)- The payer completes the payment review on the Venmo app.
![](assets/paypal-venmo-qr-paysheet.png) 

- The payer is routed back to your website to complete the payment.
![](assets/paypal-venmo-desktop-confirmation.jpg)


## Eligibility 
- US-based merchants and US-based consumers only.
- Payment must be in USD.
- Must be integrated using [JavaScript SDK](/sdk/js/) .
- Buyers on mobile devices must use Safari on iOS or Chrome on Android.
- Buyers on desktop web browsers can use any major web browser.
- Buyers must have the Venmo iOS or Android app installed.  



## Supported features 
| Feature | Supported |
| --- | --- |
| One-time payments | Yes |
| Authorization and capture | Yes |
| Online purchases | Yes |
| [Save Venmo during purchase](https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/venmo/) | Yes |
| [Shipping module](https://developer.paypal.com/docs/checkout/standard/customize/shipping-module/) | Yes |
| [Multi-seller payments](/docs/multiparty/checkout/multiseller-payments/) | No |
| Save Venmo for Purchase later | No |
| Buy online, pay in store | No |
| Contact module | No |



## Integration methods 

### Pay with Venmo
Add the Venmo button to your PayPal Checkout integration.

 


### JavaScript SDK Reference
After you integrate, make sure yourbuttons renderin the layout that you want.
