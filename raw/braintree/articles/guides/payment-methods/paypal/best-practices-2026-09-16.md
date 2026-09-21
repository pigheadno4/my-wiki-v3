<!-- Source URL: https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Best Practices
slug: /articles/guides/payment-methods/paypal/best-practices/
createTime: '2025-04-02T03:08:43.300Z'
updateTime: '2025-05-07T17:46:26.239Z'
---



# Best Practices


## Introducing the next generation of Pay with PayPal

The new streamlined Pay with PayPal payment experience accelerates the buyer's checkout journey for every merchant use case!


### Supported payment flows

![Screenshots,showing,supported,payment,flows,,One-Time,Payments,,Vaulted,Payments,,and,Recurring,Payments](https://paypalobjects.com/devdoc/best-practices/screenshot_braintree_%20supported-payments_best-practices-page.png)
### Pay with PayPal use cases

Depending on your use case, you can implement **One-Time Checkout** for most purchases, **Vaulted Payments** to securely store PayPal as a payment method for fast, frictionless, low-value future payments, or **Recurring Payments** for subscriptions and automated billing.


#### One-Time Checkout

The PayPal button and PayPal payment review page help merchants accept one-time PayPal payments.

Review the [Pay with PayPal for One-Time Payments](https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices#pay-with-paypal-for-one-time-payments) guide to see best practices for merchants who want to accept one-time PayPal payments for physical and digital goods.


#### Vaulted Payments

PayPal's Vaulted Payments flow provides a seamless checkout experience by storing payment methods for high-frequency and low average-order-value services such as rides, meal pickups, and other quick purchases.

Review the [Pay with PayPal for Vaulted Payments](https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices#vaulted-payments) guide to see best practices for merchants who want to store PayPal as a payment method and streamline repeat payments in mobile-first scenarios such as ordering food or taking a ride.


#### Recurring Payments

PayPal's Recurring Payments review page shows the customer information about the recurring payments for their subscription or other purchase.

Review the [**Pay with PayPal for Recurring Payments**](https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices#pay-with-paypal-for-recurring-payments) guide to see best practices for merchants who want to simplify the process of subscribing to a service, trying it out, or automatically reloading an account, making it easier for customers to manage their payments.


## Pay with PayPal for One-Time Payments

![Screenshot,showing,a,sample,flow,for,a,One-Time,Payment,with,PayPal](https://www.paypalobjects.com/devdoc/best-practices/screenshot_one-time-payments_one-click_combined.png)
### Overview

Pay with PayPal's One-Time Payment flow provides a one-click solution to accelerate your buyer's checkout experience by skipping manual data entry.


#### Purpose

This guide shows best practices for merchants using Pay with PayPal to accept one-time payments for physical and digital goods. Setting up the PayPal button and PayPal payment review page using these tips can help improve engagement, reduce cart abandonment, and ensure a secure payment experience.


#### Who is this section for?

Developers, designers, and product managers building ecommerce solutions for businesses selling physical goods, including retail, apparel, electronics, and other tangible products.


### Best practices for end-to-end Pay with PayPal buyer experience

The PayPal button and PayPal payment review page help you accept one-time payments. This guide shows how to present the PayPal button and PayPal payment review page to improve the buyer flow.


### Presenting the PayPal button

Buyers can use PayPal to check out at any point in their shopping journey. Placing payment buttons on the cart, product details page, or another page as a checkout shortcut can reduce steps to pay. For example:


- Buyers can select the button to check out from any page. Any items in their carts will show up at checkout.
- Buyers can skip manually adding contact details, shipping address, and payment details.
- Your shipping methods and rules are still used to complete the order.

This guide explains how to show the PayPal button upstream and during checkout. Follow these best practices to give customers the fewest steps to pay.


#### Upstream presentment

Simplify the payment experience for new customers and reinforce PayPal as a payment option by placing the PayPal button as a checkout shortcut before the buyer manually enters any information, for example, on your cart page where the buyer reviews the items they selected.

Offering the PayPal button upstream simplifies the shopping experience for the buyer and the merchant:


- The buyer gets a streamlined, one-click purchase option.
- The merchant automatically receives the buyer's shipping, billing, and other payment information from the buyer's PayPal account. The buyer doesn't need to enter this information.

See the **Integrating Contact Module** section in the [One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal) guide for more information.


**NOTE**
 Per our User Agreement, you are required to follow certain standards when presenting PayPal or Venmo payment methods. You must treat PayPal and Venmo payment methods equally to other payment methods at your points of sale, including logo placement, payment flow, and fees. You need to show the PayPal and Venmo services prominently in the checkout experience, and don't present any other payment methods earlier in the checkout flow.

 

**Best practices**

Place checkout buttons on your cart and product details pages so buyers can start checkout whenever they're ready.


- Ensure that the PayPal button shows up earlier in the checkout experience, ahead of any other merchant-provided checkout flows that require data entry from the user.
- Place PayPal Pay Later messaging close to the order total so buyers can see it clearly as a financing option. See[Message placement](https://developer.paypal.com/braintree/docs/guides/paypal/pay-later-offers/javascript/v3/#pay-later-messaging)for more information.
- Be sure to pass the data-page-type through the JavaScript SDK to indicate the type of page where you place the button. The data-page-type parameter helps PayPal optimize button behavior based on page types. See the[JavaScript SDK script configuration](/sdk/js/configuration/#link-datapagetype)page for more information.

![Screenshot,showing,a,sample,checkout,button,placement,for,a,One-Time,Payment,with,PayPal](https://www.paypalobjects.com/devdoc/best-practices/screenshot_one-time-payments_example-placement_combined.png)**Optional placement**You can place the PayPal button upstream, such as on the product description page, to encourage quick, single-product checkouts.


- Ensure any modifiers for items show up ahead of the PayPal button.
- Pay Later messaging shows buyers that they can buy now and pay later if they check out with PayPal. Adding Pay Later messaging to your website can help improve conversion, attract new customers, and increase order values.


#### Enable shipping address callback

The shipping address callback helps PayPal to show the accurate price, including shipping fees and taxes, when a buyer provides or updates their address.

If you don't integrate the shipping address callback, PayPal can't display accurate shipping costs. The buyer must return to the merchant site to see the final price and complete the payment. Use the shipping address callback to save buyers this extra step.

This callback applies to upstream flows where the buyer has not already provided their address to the merchant, such as when the user clicks the PayPal button on the merchant cart page.

See the **Integrating Shipping Module** section in the [One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal) guide for more information.


**NOTE**
 The callback may not be necessary when shipping fees don't change or aren't applicable.

 


#### Enable shipping options callback

Allow buyers to choose a delivery method during checkout. Use the shipping options callback to update the cart amount based on the selected shipping option.

If you don't integrate shipping options, PayPal can't display your delivery options. The buyer must return to the site to select delivery options before completing the payment.

See the **Integrating Shipping Module** section in the [One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal) guide for more information.



 Use the shipping options callback for physical goods even when only one delivery method is available.

 

This callback applies to upstream flows where the buyer has not already selected a shipping method for their order, such as when the user clicks the PayPal button on the merchant cart page.


#### Checkout presentment

If the buyer chooses to proceed manually through merchant checkout, have the user enter their shipping details, select their shipping method, and provide any other required details before presenting the PayPal button.

**Best practices**

For all payments, we recommend the following best practices:


- Set up your checkout flow to identify PayPal users and proactively select the PayPal payment option to reduce decision fatigue for customers ready to complete their purchases.
- Clicking the PayPal button should be the buyer's last action in your checkout experience.
- After the buyer approves the payment on the PayPal Checkout experience, redirect the buyer to the order success page.
- For payments initiated from merchant checkout pages, set up your server-side[SDK](/braintree/docs/guides/paypal/server-side/)or[GraphQL](/braintree/graphql/integration_guides/paypal/)integration to pass the buyer's provided shipping address and contact information. See the**Integrating Pass Buyer Identifier**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.

![Screenshot,showing,a,sample,checkout,page,for,a,One-Time,Payment,with,PayPal](https://www.paypalobjects.com/devdoc/best-practices/screenshot_one-time-payments_example-checkout-page.png)
### Implementing PayPal to deliver the highest conversion


#### Optimize your buyer's PayPal login experience

**Best practices**


- If you have the buyer's email address, set up your server-side[SDK](/braintree/docs/guides/paypal/server-side/)or[GraphQL](/braintree/graphql/integration_guides/paypal/)integration to pass that information. See the**Integrating Pass Buyer Identifier**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.
- For merchants showing PayPal in web view, ensure the PayPal payment experience is always full height and never presented in an iframe.

![Screenshot,showing,a,sample,loading,page,for,a,One-Time,Payment,with,PayPal](https://www.paypalobjects.com/devdoc/best-practices/screenshot_one-time-payments_example-loading-page.png)
#### Optimize your buyer's PayPal Checkout experience

**Best practices**

For all payments, we recommend the following best practices:


- Include a[Pay Now](https://developer.paypal.com/braintree/articles/guides/payment-methods/paypal/best-practices#pay-with-paypal-for-one-time-payments)button the PayPal review page so the buyer can complete the payment in a checkout hosted by PayPal and then return to an order success or receipt page.
- Set up the PayPal payment review page in your client SDK, such as Android, iOS, or JavaScript. See[Client-Side Implementations](/braintree/docs/guides/paypal/client-side)for more details.
- Ensure no more buyer action is needed after they complete payment through the PayPal payment review page.
- For payments initiated from merchant checkout pages, set up your server-side[SDK](/braintree/docs/guides/paypal/server-side/)or[GraphQL](/braintree/graphql/integration_guides/paypal/)integration to pass the buyer's provided shipping address and contact information. See the**Integrating Pass Buyer Identifier**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.
- For payments initiated from upstream, such as cart and product pages, create the order with all supported shipping options when applicable. Integrate with shipping callbacks to calculate the shipping options, cost, and taxes based on the buyer's selected address. See the**Integrating Shipping Module**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.
- Pass the invoice line item and SKU details when you create the order. PayPal displays these details during checkout, which enhances buyer experience, provides greater transparency, increases conversion, and minimizes disputes as buyers can verify the specifics of their purchase. See the**Integrating Pass Line-item Details**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.

![Screenshot,showing,a,sample,payment,review,page,for,a,One-Time,Payment,with,PayPal](https://www.paypalobjects.com/devdoc/best-practices/screenshot_one-time-payments_example-paysheet.png)
## Pay with PayPal for Vaulted Payments

Pay with PayPal's Vaulted Payments flow provides a seamless checkout experience by storing payment methods for high-frequency and low average-order-value services such as rides, meal pickups, and other quick purchases.

This flow is recommended **only** for business models where the average transaction size is less than $40. For the vast majority of business models, it is recommended to go with the [One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal) integration.

![Screenshot,showing,a,sample,integration,of,onboarding,a,customer,for,Vaulted,Payments](https://www.paypalobjects.com/devdoc/best-practices/screenshot_vault-onboarding_combined.png)
### Overview


#### Purpose

This guide provides best practices for merchants who want to store PayPal as a payment method and streamline repeat payments in mobile-first scenarios such as ordering food or taking a ride.

Using these tips to support online-to-offline (O2O) use cases makes it easier for your customers to confidently save, manage, and use PayPal for frictionless repeat payments.


#### Who is this section for?

This guide is for developers, designers, and product managers building mobile payment flows for businesses providing O2O services such as ride-hailing, food delivery, and quick-service dining. Customers typically use their phones to start a payment on a merchant's app and then complete the payment using the PayPal app.


### Best practices for implementing PayPal Vaulted Payments


#### Preselect PayPal for payment-ready PayPal users at onboarding

PayPal Vaulted Payments simplify O2O payments by allowing users to save and manage their payment methods securely.


- **Use the latest PayPal marks and logos**: Maintain brand trust and consistency by displaying updated PayPal branding.
- **Identify active PayPal users**: During onboarding, use PayPal APIs to determine if a customer has a valid payment method saved in their PayPal wallet.
- **Preselect PayPal for active users**: Drive higher conversions by selecting PayPal as the default payment option for identified users.
- **Pass user contact information**: When initiating the PayPal flow, share customer contact details with PayPal for a smoother and more personalized experience.

![Screenshot,of,a,sample,integration,onboarding,a,payer,with,Vaulted,Payments](https://www.paypalobjects.com/devdoc/best-practices/screenshot_vaulted-payments_01_onboarding.png)
#### Enable frictionless login across all surfaces

Enhance user experience and streamline login processes by implementing PayPal's frictionless login features for native experiences. Enabling support for App Switch can optimize the checkout experience, provide smoother transitions between apps, and ensure secure, efficient customer logins.


- **Native Apps**: Use the PayPal Native SDK to enable frictionless login experiences in fully native apps.
- **Hybrid Apps**: Implement the PopUp Bridge SDK for apps that use a website inside the app to provide secure web views for PayPal.
- **Websites**: Support for App Switch in the PayPal Javascript SDK is coming soon.
- **Non-SDK Merchants**: Set up seamless integration by manually rendering PayPal in a secure webview, such as AS-WAS on iOS or CCT on Android.

![Screenshot,showing,a,sample,integration,of,frictionless,login,with,Vaulted,Payments](https://www.paypalobjects.com/devdoc/best-practices/screenshot_vaulted-payments_frictionless-login_combined.png)
## Pay with PayPal for Recurring Payments

PayPal Checkout offers recurring payments to support merchant-initiated payments initiated at regular intervals, such as meal kit delivery subscriptions, automatic bill payments, auto-reloads, and installments.


### Purpose

This guide provides best practices for creating a seamless experience for customers who want to set up automatic payments with PayPal Checkout. By following these guidelines, you can simplify the process of subscribing to a service, trying it out, or automatically reloading an account, making it easier for customers to manage their payments.


### Who is this section for?

Use this documentation if you are a digital service provider or a member of a technical team managing recurring billing services. Examples include digital media platforms, content subscriptions, and other SaaS companies. Typically, the buyer has an existing account and shipping address on file with the merchant.


## Best practices for implementing Recurring Payments review page

PayPal offers a recurring payment review page to show customers information about recurring payments for their subscriptions or other purchases. Correctly setting up this review page can streamline recurring payments, simplify subscription management, and reduce disputes.


- Ensure that the order card shows plan information and a recurring indicator for greater transparency. The buyer can review this information on the payment review page before accepting the terms. See the[Recurring Payment Module](/braintree/docs/guides/paypal/recurring-payments)guide for more information.
- If you have the buyer's email address, pass it during order creation. See the**Integrating Pass Buyer Identifier**section in the[One-Time Payments](/braintree/docs/guides/paypal/checkout-with-paypal)guide for more information.

![Screenshot,of,a,sample,integration,of,the,Recurring,Payments,flow](https://www.paypalobjects.com/devdoc/best-practices/screenshot_recurring-payments_example-implementation.png)[Next Page: Setup Guide](/braintree/articles/guides/payment-methods/paypal/setup-guide)