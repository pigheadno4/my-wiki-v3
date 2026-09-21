<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/best-practices -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Best Practice Guide
slug: /docs/guides/fastlane/best-practices/
createTime: '2025-04-02T01:14:42.981Z'
updateTime: '2025-07-11T10:48:40.513Z'
---



# Best Practice Guide


#### Buyer Experience

**Present the Branded PayPal button upstream whenever possible.**

Fastlane is targeted as a way to accelerate guest checkouts for merchants. It is also a requirement to show PayPal button upstream in the cart page or alongside Fastlane email field to ensure consumers can have the option to use PayPal button.

**Email address entry should be the first step.**

Since the Fastlane accounts are looked up by the buyer's email address, the email address field should always be the first step of the checkout process. If a profile is found, Fastlane automatically retrieves shipping and payment information for the Fastlane buyer. When the email comes later in the process, it can make this a confusing experience for the buyer.

This guidance applies whether the merchant uses the Fastlane UI components or not.

**Use the Fastlane Watermark.**

The Fastlane watermark below any merchant-rendered fields for full consumer transparency. The water mark contains a link where a buyer can go to see the Fastlane ToS.![](https://www.paypalobjects.com/devdoc/fastlane_email.png)  **Streamline the process**

After a registered Fastlane member has authenticated and the profile information is received (payment nonce, shipping information and last four digits of card ). Once the Fastlane member's payment information has been rendered, hide all other payment methods under a single link.

This is because once a buyer has completed the OTP challenge, their intent is to use Fastlane. At this point, any additional areas of the UI, such as other payment methods, should still be available should the buyer change his/her mind. However, keeping the page simple and minimalistic helps boost conversion.

**Registered Fastlane Member Flows**

Once a Fastlane member authenticates, there are a few best practices that you should implement in order to reduce even more friction during the process.

Once a Fastlane member is authenticated, you should ensure:


- The user should be put on the order review page or your e-commerce site's equivalent.
- Render the returned card within your Credit or Debit card payment method field.
- The least expensive shipping option should be automatically selected.
- You should render a “change” button for the shipping address. That change button should call theshowAddressSelector()method of the client SDK. This will invoke the shipping address selector, allowing the buyer to select from shipping addresses or add a new one.
- You should render a “change” button for the card being used for the purchase. That change button should call theshowCardSelector()method of the client SDK. This will invoke the card selector, allowing the buyer to select from other cards or add a new one their profile.
- Any other use cases that need to be solved such as adding a gift message, return user can land on that specific page.

![](https://www.paypalobjects.com/devdoc/fastlane_address_example.png)![](https://www.paypalobjects.com/devdoc/fastlane_card_component.png)


#### Integration

**Be sure to load the Fastlane SDK on your checkout pagesonloadevent.**

Always make sure to load the Fastlane on your page’s load. Attempting to load the SDK after a user can interact with the page may cause conversion issues.

**Ensure that Shipping and Billing addresses are sent server-side.**

While this is always a best practice, it is particularly important in regards to Fastlane. In cases where the buyer adds a shipping address or a new card to their profile, the changes will only apply once the nonce and billing/shipping info is sent via transaction.sale() for Braintree v2/checkout/orders.

**EnsuretriggerAuthenticationFlow()is called every time the checkout page is refreshed.**

It is best practice to call the triggerAuthenticationFlow ()` method every time the checkout page is reloaded. There is internal logic within our SDK that will determine whether we will require the buyer to authenticate via OTP again or simply restore the session. In either case, the method will return the authenticatedCustomerResult. This will also include a new nonce.

**Ensure that Fastlane members can update their stored credentials.**

Whether a merchant is using our components or rendering Fastlane profile information themselves, a change button is required. These buttons are not included in the Fastlane UI components because creating edit buttons that would fit in every permutation of checkout, would be difficult and limit merchant adoption.

Merchants can render the ability to edit information in the way that best fits the look and feel of their checkout site. All they need to do is have the onclickevent call the profile.showShippingAddressSelector() or profile.showCardSelector() to launch the necessary modals.


#### Styling

Merchants should **always** ensure their checkout page is ADA compliant regardless of whether they use Fastlane or not. Couple of points to consider when it comes to styling our UI components:


- Always ensure that there is adequate contrast between thebackgroundColorandtextColortoensure that all text, especially the legal text under the opt-in, is clear and legible.
- Always ensure that there is adequate contrast between theborderColor, which drives the consent toggle coloring, and thebackgroundColor.

Colors can be any value CSS allows, including hex values, rgb, rgba, and color names.


### java
```java
  interface StyleOptions {
    root: {
    backgroundColor: string,
    errorColor: string,
    fontFamily: string,
    textColorBase: string,
    fontSizeBase: string,
    padding: string,
    primaryColor: string,
    },
    input: {
    backgroundColor: string,
    borderRadius: string,
    borderColor: string,
    borderWidth: string,
    textColorBase: string,
    focusBorderColor: string,
    },
  }
```

##### General Design Guidance

When styling the Fastlane components to match the look and feel of your checkout page, there are some general pointers that you'll need to adhere to provide an accessible and transparent experience to your payer. If the contrast ratio between the two is not 4.5:1, we will automatically set the default values in the table below.


- Ensure adequate contrast between thebackgroundColorandtextColorto ensure that all text, especially the legal text under the opt-in, is clear and legible.
- Ensure that there is adequate contrast between theborderColor, which drives the consent toggle coloring, and the backgroundColor


**NOTE**
PayPal is committed to making our product content accessible. All Fastlane integrations must conform to currently published WCAG levels A and AA. Ensure you comply with these standards when styling any Fastlane UI components.

Explore: [Advanced options](/braintree/docs/guides/fastlane/advanced-option)

