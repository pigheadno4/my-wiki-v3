<!-- Source URL: https://developer.paypal.com/braintree/docs/guides/fastlane/reference -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Reference Types
slug: /docs/guides/fastlane/reference/
createTime: '2025-04-01T23:27:27.904Z'
updateTime: '2025-04-01T23:27:27.985Z'
---



# Reference Types

braintree.fastlane.create()**Configuration Parameters**
### JavaScript
```javascript
interface FastlaneOptions {
  authorization: string,
  client: braintree.client,
  deviceData: string,
  shippingAddressOptions: AddressOptions,
  cardOptions: CardOptions,
  styles: StyleOptions
}

/*
 * To restrict the use of Fastlane to specific countries and/or regions, set
 * allowedLocations to an array containing the countries/regions where Fastlane
 * should be allowed.
 *
 * To allow shipping addresses within a particular country, 
 * specify only the country's ISO 3166-1 alpha-2 country code.
 *
 * To limit shipping addresses to only specific regions in a country, 
 * specify the country's ISO 3166-1 alpha-2 country code, followed by a colon (":"),  * followed by the name of the region.
 *
 * Examples:
 *   - [ "US" ] = Allow all regions within the United States
 *   - [ "US:CA", "US:AZ" ] = Allow in California in Arizona, but nowhere else
 *   - [ "US:CA", "US:AZ", "FR" ] = Allow in California, Arizona, and France,
 *       but nowhere else
 */

interface AddressOptions {
  // default: empty array = all locations allowed
  allowedLocations: [AddressLocationEnum];
  noShipping: boolean;
}

Enum AddressLocationEnum {
  {ISO-country-code}
  {ISO-country-code}:{ISO-region-code}
}

interface CardOptions {
  // default: empty array = all brands allowed
  allowedBrands: [CardBrandEnum];
}

Enum CardBrandEnum {
  VISA
  MASTERCARD
  AMEX
  DINERS
  DISCOVER
  JCB
  CHINA_UNION_PAY
  MAESTRO
  ELO
  MIR
  HIPER
  HIPERCARD
}
```
type create = (options: FastlaneOptions) =&gt; Fastlane;

**Fastlane Namespace**

This is returned as the result of calling fastlane.create({...})


### JavaScript
```javascript
interface Fastlane {
    identity {
        lookupCustomerByEmail: (email: string) => LookupCustomerResult,
        triggerAuthenticationFlow: (customerContextId: string, options: AuthenticationFlowOptions) => AuthenticatedCustomerResult
    }
    profile {
        showShippingAddressSelector: () => ShowShippingAddressSelectorResult,
        showCardSelector: () => ShowCardSelectorResult,
    }
    setLocale: (locale: string) => void, // options: en_us, es_us, fr_us, zh_us
    FastlaneCardComponent: (options: FastlaneCardComponentOptions) => FastlaneCardComponent,
    FastlanePaymentComponent: (options: FastlanePaymentComponentOptions) => FastlanePaymentComponent,
    FastlaneWatermarkComponent: (options: FastlaneWatermarkOptions) => FastlaneWatermarkComponent
}
```
**LookupCustomerResult**

The LookupCustomerResult object type is returned from the identity.lookupCustomerByEmail(email) method.


### JavaScript
```javascript
interface LookupCustomerResult {
    customerContextId: string
}
```
**AuthenticatedCustomerResult**

The AuthenticatedCustomerResult object type is returned from the identity.triggerAuthenticationFlow() call.


### JavaScript
```javascript
interface AuthenticatedCustomerResult {
    authenticationState: 'succeeded'|'failed'|'canceled'|'not_found';
    profileData: ProfileData;
}

interface ProfileData {
    name: Name;
    shippingAddress: Address;
    card: PaymentToken;
}

interface Name {
    firstName: string;
    lastName: string;
}

interface Address {
    firstName: string;
    lastName: string;
    company: string;
    streetAddress: string;
    extendedAddress?: string;
    locality: string; // City
    region: string; // State
    postalCode: string;
    countryCodeNumeric: number;
    countryCodeAlpha2: string;
    countryCodeAlpha3: string;
    phoneNumber: string;
}

interface PaymentToken {
    id: string; // This is the paymentToken
    paymentSource: PaymentSource;
}

interface PaymentSource {
    card: CardPaymentSource;
}

interface CardPaymentSource {
    brand: string;
    expiry: string; // "YYYY-MM"
    lastDigits: string; // "1111"
    name: string;
    billingAddress: Address;
}
```
**Profile Method Reference Types**


### JavaScript
```javascript
interface ShowShippingAddressSelectorResult {
    selectionChanged: boolean;
    selectedAddress: Address;
}

interface ShowCardSelectorResult {
    selectionChanged: boolean;
    selectedCard: PaymentToken;
}
```
**FastlaneCardComponent**

The FastlaneCardComponent uses the Hosted Card Fields, and the resulting interface is a subset of the Card Fields interface.

The instance of a FastlaneCardComponent can be created using:


### JavaScript
```javascript
const fastlaneCardComponent = fastlane.FastlaneCardComponent({ ... });
await fastlaneCardComponent.render("#card-container");
```
**FastlaneCardComponent Reference Types**
### JavaScript
```javascript
type FastlaneCardComponent = (options: FastlaneCardComponentOptions) => FastlaneCardComponent;

interface FastlaneCardComponent {
    render: (container) => FastlaneCardComponent;
    getPaymentToken: async (options: PaymentTokenOptions) => PaymentToken;
}

interface FastlaneCardComponentOptions {
    styles: StyleOptions;
    fields: { Field };
}

interface Field {
    placeholder: string;
    prefill: string;
    enabled: boolean;
}

interface PaymentTokenOptions {
    billingAddress: Address;
    cardholderName: string;
}
```
**FastlanePaymentComponent**

A FastlanePaymentComponent can be created using the following code:


### JavaScript
```javascript
const fastlanePaymentComponent = fastlane.FastlanePaymentComponent({ ... });
await fastlanePaymentComponent.render('#payment-container');
```
**FastlanePaymentComponent Reference Types**
### JavaScript
```javascript
type FastlanePaymentComponent = (options: FastlanePaymentComponentOptions) => FastlanePaymentComponent;

interface FastlanePaymentComponent {
    render: (container) => FastlanePaymentComponent;
    getPaymentToken: async () => PaymentToken;
    setShippingAddress: (shippingAddress: Address) => void;
}

interface FastlanePaymentComponentOptions {
    styles: StyleOptions;
    fields: Field;
    shippingAddress: Address;
}

interface Field {
    placeholder: string;
    prefill: string;
}
```
**Card Field Configurations**

You can configure the card fields in the FastlaneCardComponent or FastlanePaymentComponent when initializing the components, as shown below:


### JavaScript
```javascript
const styles = {};
const fields = {
    number: {
        placeholder: 'Number',
    },
    phoneNumber: {
        prefill: '555-555-5555'
    }
};

fastlane.FastlaneCardComponent({ styles, fields }).render(elem);
fastlane.FastlanePaymentComponent({ styles, fields }).render(elem);
```
**Available Fields**

| Name | Type | Attributes | Description |
| --- | --- | --- | --- |
| number | field | &lt;optional&gt; | A field for card number. |
| expirationDate | field | &lt;optional&gt; | A field for expiration date in MM/YYYY or MM/YY format. This should not be used with the expirationMonth and expirationYear properties. |
| expirationMonth | field | &lt;optional&gt; | A field for expiration month in MM format. This should be used with the expirationYear property. |
| expirationYear | field | &lt;optional&gt; | A field for expiration year in YYYY or YY format. This should be used with the expirationMonth property. |
| cvv | field | &lt;optional&gt; | A field for 3 or 4 digit card verification code (like CVV or CID). If you wish to create a CVV-only payment method paymentToken to verify a card already stored in your Vault, omit all other fields to only collect CVV. |
| postalCode | field | &lt;optional&gt; | A field for postal or region code. |
| cardholderName | field | &lt;optional&gt; | A field for the cardholder name on the payer’s credit card. |
| phoneNumber | field | &lt;optional&gt; | A field for the cardholder's phone number associated with the credit card. |


#### Style Options and Guidelines

Colors can be any value that CSS allows including hex values, rgb, rgba, and color names.
### JavaScript
```javascript
interface StyleOptions {
    root: {
        backgroundColor: string;
        errorColor: string;
        fontFamily: string;
        textColorBase: string;
        fontSizeBase: string;
        padding: string;
        primaryColor: string;
    },
    input: {
        backgroundColor: string;
        borderRadius: string;
        borderColor: string;
        borderWidth: string;
        textColorBase: string;
        focusBorderColor: string;
    },
}
```

#### General Design Guidance

When styling the Fastlane components to match the look and feel of your checkout page, there are some general pointers which you must adhere to in order to provide an accessible and transparent experience to your payer.


- Always ensure that there is adequate contrast between thebackgroundColorandtextColortoensure that all text, especially the legal text under the opt-in, is clear and legible. If the contrast ratio between the two is not 4.5:1, we will automatically set the to the default values in the table below.
- Always ensure that there is adequate contrast between theborderColor, which drives the consent toggle coloring, and thebackgroundColor



PayPal is committed to making our product content accessible. All Fastlane integrations must conform to currently published WCAG levels A and AA. Please be sure you are complying with these standards when styling any Fastlane UI components. 

 If the color of the legal text and toggle button are not distinguishable from the text and background, the Fastlane component colors will be reverted to the default.


#### Payment Component UI

| Value | Description | Default | Minimum | Maximum | Guidance and Thresholds |
| --- | --- | --- | --- | --- | --- |
| root.backgroundColor | The background color of the components. | #ffffff | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| root.errorColor | The color of errors in the components. | #D9360B | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| root.fontFamily | The font family used throughout the UI. | PayPal-Open | N/A | N/A | Must be one of the following:
- Sans serif
- Arial
- Verdana
- Tahoma
- Trebuchet MS


- Serif:
- Times New Roman
- Georgia
- Garamond


- Monospace:
- Courier New


- Cursive:
- Brush Script MT |
| root.fontSizeBase | The base font size. Increasing this value will change the text size of all text within the UI components. | 16px | 13px | 24px |  |
| root.textColorBase | The text color used across all text outside of inputs. | #010B0D | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| root.padding | The padding between content and borders. | 4px | 0px | 10px |  |
| root.primaryColor | This value sets the default for the checkbox for billing address, and the link for the “change”, the toggle primary color, and the legal links for privacy and terms. | #0057FF | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| input.backgroundColor | The background color of the inputs within the components. | #ffffff | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| input.borderRadius | The border radius used for the email field. | 0.25em | 0px | 32px |  |
| input.borderColor | The border color of the email field. | #DADDDD | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| input.focusBorderColor | The border color of the email field when focused. | #0057FF | N/A | N/A | May be any valid CSS color. (No transparency allowed) |
| input.borderWidth | The width of the input borders. | 1px | 1px | 5px | Default size is 1px. |
| input.textColorBase | The text color used for text within input fields. | #010B0D | N/A | N/A | May be any valid CSS color. (No transparency allowed) |


#### Loading Card Assets

| Card Brand | Image URL |
| --- | --- |
| Amex | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_amex_light.81e1.svg) |
| Diners Club | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_dinersclub_light.354d.svg) |
| Discover | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_discover_light.85a5.svg) |
| JCB | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_jcb_light.6fb4.svg) |
| Mastercard | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_mastercard_light.1621.svg) |
| Union Pay | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_unionpay_light.1519.svg) |
| Visa | [View Image](https://www.paypalobjects.com/fastlane-v1/assets/cc_visa_light.0a3a.svg) |

Explore:[Advanced Options](/braintree/docs/guides/fastlane/advanced-option)