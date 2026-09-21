<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/flexible-payment -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Flexible Payment Integration
slug: /docs/guides/fastlane/flexible-payment/
createTime: '2025-04-01T23:04:12.849Z'
updateTime: '2025-07-08T10:14:58.726Z'
---



# Flexible Integration

The Flexible Integration allows developers to customize the payment experience for their users. This approach offers more control and flexibility compared to the Quick Start Integration, enabling you to tailor the payment flow to meet specific business requirements. This guide will walk you through the steps to implement Flexible Integration on the client side, highlighting areas where it differs from Quick Start Integration. For a faster, default setup, refer to the [Quick Start Integration Guide.](https://developer.paypal.com/braintree/docs/guides/fastlane/client-side)


#### Quick Start vs Flexible Integration

The table below outlines the key differences between Quick Start and Flexible Integration. Use this as a reference to determine which integration method is best suited for your project.

| Feature | Quick Start | Flexible |
| Initialize Fastlane | Same | Same |
| Collect Email | Same | Same |
| Authenticate consumer | Same | Same |
| Profile Data | Same | Same |
| Billing Address (guest) | Collected by Payment Component | Collected by Merchant |
| Billing Address (member) | Billing address is tied to the Fastlane returned card. | Same |
| Shipping Address (guest & member) | Same | Same |
| Card details (guest) | Render Payment Component | Render Card Component |
| Card details (member) | Render Payment Component | Merchant renders card details & integrates Fastlane's card selector. |
| Fastlane Payment Token (guest) | Always call getPaymentToken | Always call getPaymentToken with customer's name and billing address (required) |
| Fastlane Payment Token (member | Always call getPaymentToken | Use payment token returned in profile data or card selector callback. |


# Client-side Integration


#### Step 1: Initialize the Braintree SDK


- Load the necessary Braintree SDK modules.
- Ensure all modules are the same version (3.120.0 or greater).


### HTML
```html
<script src="https://js.braintreegateway.com/web/3.120.0/js/client.min.js"></script>
<script src="https://js.braintreegateway.com/web/3.120.0/js/fastlane.js"></script>
<script src="https://js.braintreegateway.com/web/3.120.0/js/data-collector.min.js"></script>
```

#### Step 2: Initialize Fastlane Component


- Create a client instance.
- Create a data collector instance.
- Define[custom styling](https://developer.paypal.com/braintree/docs/guides/fastlane/reference/#style-options-and-guidelines)for the Fastlane component (Optional).
- [Initialize Fastlane component](https://developer.paypal.com/braintree/docs/guides/fastlane/reference/).
- Define the[customer's locale](https://developer.paypal.com/braintree/docs/guides/fastlane/advanced-option/#specify-locale)(Optional).
- Define the[merchant's accepted card brands](https://developer.paypal.com/braintree/docs/guides/fastlane/reference/)(Optional).
- Extract identity, profile and events from the braintree.fastlane.create function response as local variables


### JavaScript
```javascript
const clientInstance = await braintree.client.create({
  authorization: "<YOUR CLIENT TOKEN>"
});

const dataCollectorInstance = await braintree.dataCollector.create({
  client: clientInstance,
});

const styles = {
  //specify global styles here
  root: {
    backgroundColorPrimary: "#ffffff"
  }
}

const deviceData = dataCollectorInstance.deviceData;

// For all configuration options for the fastlane construct 
// please refer to the Reference types section
const fastlane = await braintree.fastlane.create({
  authorization: "<YOUR CLIENT TOKEN>",
  client: clientInstance,
  deviceData: deviceData,
  styles: styles
});

const identity = fastlane.identity;
const profile = fastlane.profile;
const {
    checkoutPageLoaded,
    apmSelected,
    emailSubmitted,
    orderPlaced,
    checkoutEnd,
    storeAccountCreated,
} = fastlane.events;
```

#### Step 3: Render Email Field Fastlane Watermark


- Add a div for the watermark.
- Display the Fastlane watermark with the email input field.

When sharing the email with Fastlane, certain countries and regulations require you to [display the Fastlane watermark](https://developer.paypal.com/braintree/docs/guides/fastlane/advanced-option/#rendering-fastlane-watermark) to inform consumers about the data sharing.

![Email,field,input,with,Fastlane,Watermark,and,info,icon](https://www.paypalobjects.com/devdoc/fastlane_email.png)
### HTML
```javascript
<!-- add a div where the watermark will be rendered -->
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg" />
</div>
```
The image tag within the watermark container div ensures the watermark is rendered immediately.


### JavaScript
```javascript
const fastlaneWatermark = (await fastlane.FastlaneWatermarkComponent({
    includeAdditionalInfo: //Boolean which determines if the info icon is present
}));
await fastlaneWatermark.render("#watermark-container");
```



#### Step 4: Customer Lookup and Authentication


- Lookup the customer by email.
- Trigger authentication flow if the customer is a Fastlane member.
- Retrieve authentication state and profile data.

After collecting the email address, call identity.lookupCustomerByEmail(email) to check if the email is associated with a Fastlane or PayPal member.

Fastlane members must authenticate themselves before their profile information can be accessed. They will receive an OTP on their registered mobile number or alternate methods to complete the authentication.


**IMPORTANT**
 In Sandbox, the OTP passcode will always be "111111" or "222222" to successfully authenticate. All other codes will fail authentication.

 

![](https://www.paypalobjects.com/devdoc/fastlane_confirmation_code.png)


### JavaScript
```javascript
const {
    customerContextId
   } = await identity.lookupCustomerByEmail(document.getElementById("email").value);

   var renderFastlaneMemberExperience = false;

   if (customerContextId) {
   // Email is associated with a Fastlane member or a PayPal member, 
   // send customerContextId to trigger the authentication flow.
   const {
    authenticationState,
    profileData
   } = await identity.triggerAuthenticationFlow(customerContextId);

   if (authenticationState === "succeeded") {
    // Fastlane member successfully authenticated themselves
    // profileData contains their profile details
    renderFastlaneMemberExperience = true;
    const name = profileData.name;
    const shippingAddress = profileData.shippingAddress;
    const card = profileData.card;
   } else {
    // Member failed or cancelled to authenticate. Treat them as a guest payer
    renderFastlaneMemberExperience = false;
    }
   } else {
   // No profile found with this email address. This is a guest payer
   renderFastlaneMemberExperience = false;
   }
```

- Succeeded Authentication: An**authenticationState**value of**succeeded**indicates a Fastlane member has authenticated and then you should set**renderFastlaneMemberExperience**to**true**.
- Guest User:Any other**authenticationState**value indicates a Fastlane guest user and you should render the guest experience specified in step 5.
- Profile Data: Fastlane members**card details**and**shipping address**are returned with the**profileData**object contents on**successful**authentication and the**renderFastlaneMemberExperience**is set to**True.**




#### Step 5: Fastlane Member Experience


- Render the customer's shipping address.
- Allow the customer to change their shipping address.
- Render the customer's card details.
- Last 4 of card
- Brand of card
- Exp Date (Optional)


- Allow the customer to change their card.
- Render the Fastlane Watermark with the shipping and card details.


##### Render Shipping Address

![](https://www.paypalobjects.com/devdoc/fastlane_address_component.png)

![](https://www.paypalobjects.com/devdoc/fastlane_address_example.png)


**NOTE**
 When integrating Fastlane by PayPal, keep the following points in mind regarding shipping addresses

  
- Handle Missing Shipping Addresses: Fastlane members might not have a shipping address in their profile. Ensure your integration can handle this scenario gracefully.
- When a customer changes their shipping address, be sure to update the address rendered on your site.
- Send shipping address in server side request.
- [Refer to Advanced Guidelines:](/braintree/docs/guides/fastlane/advanced-option#shipping-address-guidelines)For more detailed information, refer to the shipping address guidelines in the advanced section.

 


##### Set change link


### HTML
```javascript
<div id="selected-address"> <!-- render selected shipping address here --> </div>
<a href="" id="your-change-address-button"> Change address </a>
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg" />
</div>
```

##### Shipping Address Selector


### JavaScript
```javascript

    if (renderFastlaneMemberExperience) {
    if (profileData.shippingAddress) {
    // render shipping address from the profile
  
    const changeAddressButton = document.getElementById("your-change-address-button");
    
    changeAddressButton.addEventListener("click", async () => {
      const {
        selectedAddress,
        selectionChanged
      } = await profile.showShippingAddressSelector();
    
      if (selectionChanged) {
        // selectedAddress contains the new address
      } else {
        // selection modal was dismissed without selection
      }
    });
    } else {
    // render your shipping address form
    }
    } else {
    // render your shipping address form
    }
    
```

##### Card details


**NOTE**
 When integrating Fastlane by PayPal, keep the following points in mind regarding card details

  
- Handle no cards: Fastlane members might not have a saved card in their profile. Ensure your integration can handle this scenario gracefully by rendering the card component.
- When a customer changes their card, be sure to update the card details rendered on your site.

 


##### Card Selector

Render the card detals returned within the profileData after a Fastlane consumer has successfully authenticated. Include a change link that will allow the customer to change to another card within their Fastlane profile.

Set Change Link
### JavaScript
```javascript
<div id="selected-card"> <!-- render selected card here --> </div>
<a href="" id="your-change-card-button"> Change card </a>
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg" />
</div>
```
Card Selector
### JavaScript
```javascript
// Handle changes to the card selection
const changeCardButton = document.getElementById("your-change-card-button");
changeCardButton.addEventListener("click", async () => {
    const { selectionChanged, selectedCard } = await profile.showCardSelector();
    if (selectionChanged) {
        // selectedCard contains the new card
        // selectedCard.id contains the paymentToken
        // selectedCard.paymentSource.card contains more details such as last 4
        selectedCardForCheckout = selectedCard;
        // re-render the selected card UI if required
    } else {
        // selection modal was dismissed without selection
    }
});
```

#### Step 6: Fastlane Guest Experience


- Have the customer enter their shipping address manually.
- Have the customer enter their billing address manually.
- Setup the Card Component.
- Set the event to trigger when Fastlane will retrive the payment token, usually the payment submission or confirmation button.
- Define the[styling object](https://developer.paypal.com/braintree/docs/guides/fastlane/reference/)to send as a parameter to the payment component (Optional)
- Define the[fields object](https://developer.paypal.com/braintree/docs/guides/fastlane/reference/)to prefill/disable available fields within the Card component (Optional)
- Render Card Component.
- When the event to trigger the Fastlane token occurs, callfastlaneCardComponent.getPaymentToken()to retrieve the payment token.

Only render the Card component if you have a Fastlane guest user or a Fastlane member who doesn't have a saved card.


##### Setup Card component and trigger for getPaymentToken:


### HTML
```javascript
<!-- Div container for the Card Component -->
<div id="card-container"> </div>
<!-- Submit Button -->
<button id="submit-button"> Submit Order </button>
```

##### Render Card Component


### JavaScript
```javascript
const name = profileData.name;
const shippingAddress = profileData.shippingAddress;
const card = profileData.card;
var selectedCardForCheckout = card;
if (memberAuthenticatedSuccessfully && card) {
    // refer to Lookup & Authenticate section for details
    // render the card here
    // render Fastlane Watermark
    // render a change button and call profile.showCardSelector() when it is clicked
} else {
    // User is a guest, failed to authenticate or does not have a card in the profile.
    // render the card fields
    const fastlaneCardComponentOptions = {
        fields: {
            phoneNumber: {
                // Example of how to prefill the phone number field in the FastlaneCardComponent
                prefill: "4026607986"
            },
            cardholderName: {
                // Example of disabling and prefilling the cardholder name field
                prefill: "John Doe",
                enabled: false
            }
        },
        styles: {
            root: {
                // specify styles here
                backgroundColorPrimary: "#ffffff"
            }
        }
    };
    const fastlaneCardComponent = await fastlane.FastlaneCardComponent(fastlaneCardComponentOptions);
    fastlaneCardComponent.render("#card-container");
}
```

##### Generate Fastlane Payment Token


### JavaScript
```javascript
// Handle form submission
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", async () => {
    var paymentToken = null;
    // if the Card Component is rendered,
    // pass the billing address and get the paymentToken
    if (selectedCardForCheckout) {
        paymentToken = selectedCardForCheckout.id;
    } else {
        paymentToken = await fastlaneCardComponent.getPaymentToken({
            billingAddress: {
                cardholderName: "John Doe",
                streetAddress: "2211 North 1st St",
                locality: "San Jose",
                region: "CA",
                postalCode: "95131",
                // you can also use the countryCodeAlpha3 or countryCodeNumeric formats
                countryCodeAlpha2: "US"
            }
        });
    }
    // Send the paymentToken and previously captured device data to server
    // to complete checkout
});
```

- Use the Fastlane Payment token the same as a paymentMethodNonce to:

- [Transact](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/)
- [Vault](https://developer.paypal.com/braintree/docs/reference/request/payment-method/create)


