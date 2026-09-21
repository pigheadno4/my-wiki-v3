<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/advanced-option -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Advanced Options
slug: /docs/guides/fastlane/advanced-option/
createTime: '2025-04-01T22:15:15.144Z'
updateTime: '2025-04-01T22:15:15.202Z'
---



# Advanced Options

**Add*.paypal.comto your Content Security Policy (skip if using Hosted Card Fields)**
##### Configure your Content Security Policy

Content Security Policy is a feature of web browsers that mitigates cross-site scripting and other
attacks. By limiting the origins of resources that may be loaded on your page, you can maintain
tighter control over any potentially malicious code. While browser support is relatively limited, we
recommend considering the implementation of a CSP when available. Include the following directive in
your policy:
### 
```javascript

connect-src: https://*.paypal.com https://*.paypalobjects.com https://*.braintreegateway.com https://*.braintree-api.com
font-src: https://*.paypalobjects.com
frame-src: https://*.paypal.com https://*.braintreegateway.com
img-src: https://*.paypal.com https://*.paypalobjects.com
script-src: https://*.paypal.com https://*.paypalobjects.com https://*.braintreegateway.com
style-src: unsafe-inline
 
```
Also, review Braintree's[best practices and troubleshooting guide](/braintree/docs/guides/fastlane/best-practices).
##### Specify locale

To specify the locale in which the Fastlane components should be rendered, you can set the locale
after initializing thefastlanecomponent.

fastlane.setLocale("en_us"); // en_usis the default value

Fastlane supports the following languages:

en_us(default)

es_us

fr_us

zh_us


#### Rendering Fastlane Watermark**

There are two ways to recommend Fastlane Watermark :
##### Watermark without the info icon

![](https://www.paypalobjects.com/devdoc/fastlane_email.png)
##### Watermark with the info icon


### HTML
```javascript
<!-- add a div where the watermark will be rendered -->
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg" />
</div>
```
The image tag in the watermark container div allows the watermark to be rendered instantly.
### JavaScript
```javascript
const fastlaneWatermark = (await fastlane.FastlaneWatermarkComponent({
    includeAdditionalInfo: //Boolean which determines if the info icon is present
}));
await fastlaneWatermark.render("#watermark-container");
```
![](https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg)

The mouse-over tooltip functionality will be added progressively to the image when the Watermark
component completes loading. After it loads, the information is displayed when the User hovers the
mouse pointer over the**i**section
### Watermark without the info icon

You can use the following code to render the watermark without the "info" icon:

HTML Sample
### HTML
```javascript
<!-- add a div where the watermark will be rendered -->
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg" />
</div>
```
Javascript Sample
### JavaScript
```javascript
const fastlaneWatermark = (await fastlane.FastlaneWatermarkComponent({
    includeAdditionalInfo: false
}));
await fastlaneWatermark.render("#watermark-container");
```
![](www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg)The image tag in the watermark container div allows the watermark to be rendered instantly.
##### Optimization: Preload watermark assets

For a better payer experience of Fastlane, it is recommended to preload the watermark asset by
adding the following code to theheadsection of the page. Even though this is
optional,**we highly recommend it**.
### HTML
```javascript
<link rel="preload" href="https://www.paypalobjects.com/fastlane-v1/assets/fastlane-with-tooltip_en_sm_light.0808.svg" as="image" type="image/avif" />
<link rel="preload" href="https://www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg" as="image" type="image/avif" />
```

### Shipping Address Guidelines

**Only supports US addresses:**


- While Fastlane is only available with billing addresses in the US, the shipping address can be any location that your site supports shipping to.
- For information on how to limit the available shipping addresses, please see the[reference types](https://developer.paypal.com/braintree/docs/guides/fastlane/reference)section.

**Send a new address in the server-side request :**
- If the payer adds a new address, ensure you can send that address in the server-sidetransaction.sale()request.

**Flexible Integration Template**

You can use the following code as a reference to implement the flexible integration for the payment.
It covers the following:
### HTML
```javascript
<!-- Div container for the Payment Component -->
<div id="card-container"> </div>
<div id="selected-card"> <!-- render selected card here --> </div>
<a href="" id="change-card-link"> Change card </a>
<div id="watermark-container">
    <img src="https://www.paypalobjects.com/fastlane-v1/assets/fastlane_en_sm_light.0296.svg" />
</div>
<!-- Submit Button -->
<button id="submit-button"> Submit Order </button>
```

### javascript
```javascript
const name = profileData.name;
const shippingAddress = profileData.shippingAddress;
const card = profileData.card;
var selectedCardForCheckout = card;
if (memberAuthenticatedSuccessfully && card) {
    // refer to Lookup & Authenticate section for details
    // render the card here
    // render Fastlane watermark
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

// Handle changes to the card selection
const changeCardButton = document.getElementById("change-card-button");
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
**Recommended Fields for server-side API call**| Field name | Description | Link |
| --- | --- | --- |
| device_data | An identifier that helps prevent fraud and ensures the highest authorization rates. | [Link to the documentation](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#device_data) |
| billing | The billing object contains fields related to the payer’s billing information. | [Link to the documentation](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#billing) |
| customer.firstName | The payer’s first name. | [Link to the documentation](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#customer-first_name) |
| customer.lastName | The payer's last name. | [Link to the documentation](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#customer-last_name) |
| customer.email | The payer’s email address. | [Link to the documentation](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#customer-email) |


### Store pick-up Integration

If the buyer is picking up an item from a store-front, then the shipping type should be modified
accordingly.

Ensure[shipping method](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#shipping)is set topickupInStoreorshipToStoreto ensure that the buyer profiles don’t get created
with the address of your store as their shipping address.
### Vaulting


- Transact and Vault:

If you wish to vault thepaymentTokenreturned by the Fastlane
SDK at the time of transaction, you can do so by using thestore_in_vault_on_successboolean in thetransaction.sale()request on your server. Please see the[Braintree Transaction Sale](https://developer.paypal.com/braintree/docs/reference/request/transaction/sale/ruby#options-store_in_vault_on_success)API request for reference.
- Vault and transact:

If you wish to vault thepaymentTokenreturned by the Fastlane
SDK and transact later, you can do so by using the[customer create API](https://developer.paypal.com/braintree/docs/reference/request/customer/create/ruby)request or[payment method](https://developer.paypal.com/braintree/docs/reference/request/payment-method/create/ruby)create API request.
## PayPal Members without a Fastlane Profile

PayPal members without a Fastlane profile do not require any additional handling within your
integration. Our client SDK handles this use case for you in the following ways:


- After performing thelookupCustomerByEmailmethod, we will return acustomerContextIdas if this were a Fastlane member.
- Trigger thetriggerAuthenticationFlowmethod, and our SDK will display a call to action to the buyer explaining that he/she can create a Fastlane profile populated with information from his/her PayPal account with one click.
- If the consumer clicks yes, we will returnprofileDataexactly as we would for a Fastlane member.
- If the consumer closes the dialog, we will return an emptyprofileDataobject and you will handle this as you would any Fastlane guest.

