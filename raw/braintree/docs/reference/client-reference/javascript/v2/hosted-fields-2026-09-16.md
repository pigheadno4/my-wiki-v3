<!-- Source URL: https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/hosted-fields -->
<!-- Fetched: 2026-09-16 -->
<!-- Discovery: llms.txt,sitemap.xml -->

---
title: Hosted Fields
slug: /docs/reference/client-reference/javascript/v2/hosted-fields/
createTime: '2025-04-01T23:34:45.564Z'
updateTime: '2025-04-01T23:34:45.597Z'
---



# Hosted Fields


## Events

You can subscribe to events using the onFieldEvent callback. This allows you to hook into focus, blur, and fieldStateChange.


### JavaScript
```javascript

// ...
hostedFields: {
  onFieldEvent: function (event) {
    if (event.type === 'focus') {
      // Handle focus
    } else if (event.type === 'blur') {
      // Handle blur
    } else if (event.type === 'fieldStateChange') {
      // Handle a change in validation or card type
      console.log(event.isValid); // true|false
      if (event.card) {
        console.log(event.card.type);
        // visa|master-card|american-express|diners-club|discover|jcb|unionpay|maestro
      }
    }
  }
}
// ...

```
The event object will return the following:

| **Key** | **Type** | **Description** |
| type | String | | focus | Fired when the input becomes focused |
| blur | Fired when the input loses focus |
| fieldStateChange | When any state has changed within an input including: validation, focus, card type detection, etc. | |
| isEmpty | Boolean | Whether or not the user has entered a value in theinput |
| isFocused | Boolean | Whether or not theinputis currently focused |
| isPotentiallyValid | Boolean | A determination based on the future validity of the input value. This is helpful when a user is entering a card number and types"41". While that value is not valid for submission, it is still possible for it to become a fully qualified entry. However, if the user enters"4x"it is clear that the card number can never become valid andisPotentiallyValidwill return`{false}`. |
| isValid | Boolean | Whether or not the value of the associatedinputisfullyqualified for submission |
| target | Object | | container | Reference to the container DOM element on your page associated with the current event. |
| fieldKey | AStringmapping to the currently associated field:  "number"  "cvv"  "expirationDate"  "expirationMonth"  "expirationYear"  "postalCode" | |
| card | Object | The determined card type. Learn more about[card type](/braintree/docs/reference/client-reference/javascript/v2/hosted-fields#card-type). |


### Card type

With each fieldStateChange event, we will return a Card Type to describe the current user input. If not enough information is available, or if there is invalid data, this value will be null.

| **Key** | **Type** | **Description** |
| type | String | The code-friendly representation of the card type:visadiscovermaster-cardamerican-express, etc. |
| niceType | String | The pretty printed card type:VisaDiscoverMastercardAmerican Express, etc. |
| code | Object | | This object contains data relevant to the security code requirements of the card brand. For example, on a Visa card there will be acvvof 3 digits, whereas an American Express card requires a 4-digitcid. |
| **Key** | **Type** | **Value** |
| name | String | "CVV""CID""CVC" |
| size | Integer | The expected length of the security code. Typically, this is 3 or 4 | |
| lengths | Array | An array of integers of expected lengths of the card number excluding spaces, dashes, etc. (Maestro and UnionPay are card types with several possible lengths) |
| Internally, Hosted Fields uses[credit-card-type](https://github.com/braintree/credit-card-type), an open-source detection library to determine card type. Visit the[repo](https://github.com/braintree/credit-card-type)to view more detailed documentation. |


## Internal styling properties

These are the CSS properties that we support inside of our iframes. Any other CSS should be specified on your page and outside of any Braintree configuration. Trying to set unsupported properties will fail and put a warning in the console.

```syntax-inline
color
```
  ```syntax-inline
font
```
  ```syntax-inline
font-family
```
  ```syntax-inline
font-size
```
  ```syntax-inline
font-size-adjust
```
  ```syntax-inline
font-stretch
```
  ```syntax-inline
font-style
```
  ```syntax-inline
font-variant
```
  ```syntax-inline
font-variant-alternates
```
  ```syntax-inline
font-variant-caps
```
  ```syntax-inline
font-variant-east-asian
```
  ```syntax-inline
font-variant-ligatures
```
  ```syntax-inline
font-variant-numeric
```
  ```syntax-inline
font-weight
```
  ```syntax-inline
line-height
```
  ```syntax-inline
outline
```
  ```syntax-inline
opacity
```
  ```syntax-inline
text-shadow
```
  ```syntax-inline
transition
```
  ```syntax-inline
-moz-osx-font-smoothing
```
  ```syntax-inline
-moz-transition
```
  ```syntax-inline
-webkit-font-smoothing
```
  ```syntax-inline
-webkit-transition
```

The following properties are supported in versions 2.18.0 and above:

```syntax-inline
-moz-tap-highlight-color
```
  ```syntax-inline
-webkit-tap-highlight-color
```


## Options


### Top-level options

Inside the hostedFields configuration, the full list of options you can specify are:

| Key | Type | Required | Description | Reference |
| --- | --- | --- | --- | --- |
| ```syntax-inline
styles
``` | ```syntax-inline
Object
``` | no | A CSS-like object representing styles. | [Styling](/braintree/docs/guides/hosted-fields/styling) |
| ```syntax-inline
onFieldEvent
``` | ```syntax-inline
function
``` | no | Called when events happen in any of your fields. It's passed one object called```syntax-inline
event
```
. | [Events](/braintree/docs/guides/hosted-fields/events) |
| ```syntax-inline
number
``` | ```syntax-inline
Object
``` | **yes** | Field options for credit card number. | [Field-level options](#field-level-options) |
| ```syntax-inline
expirationDate
``` | ```syntax-inline
Object
``` | **yes** | Field options for expiration month and year in```syntax-inline
MM/YYYY
```
format. You may optionally split month and year into two separate fields (```syntax-inline
expirationMonth
```
and```syntax-inline
expirationYear
```
) if it works better with your layout. | [Field-level options](#field-level-options) |
| ```syntax-inline
cvv
``` | ```syntax-inline
Object
``` | no | Field options for 3 or 4 digit CVV or CID. | [AVS &amp; CVV rules](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules) |
| ```syntax-inline
postalCode
``` | ```syntax-inline
Object
``` | no | Field options for postal code or region code. | [AVS &amp; CVV rules](/braintree/articles/guides/fraud-tools/basic/avs-cvv-rules) |

* Only required when creating, saving, or using card information that is not stored in the Vault yet. When[verifying cards already in the Vault](/braintree/docs/reference/request/payment-method/update#card-verification), you can collect just the `cvv`.
### Field-level options

Inside number, expirationDate, expirationMonth, expirationYear, cvv, and postalCode, you can specify:

| Key | Type | Required | Description |
| --- | --- | --- | --- |
| ```syntax-inline
selector
``` | ```syntax-inline
String
``` | **yes** | String used to query the DOM for your container. Examples include: -```syntax-inline
"#card-container"
```
 -```syntax-inline
".card-container"
```
 -```syntax-inline
"[data-name='card-container']"
``` |
| ```syntax-inline
placeholder
``` | ```syntax-inline
String
``` | no | Will be used as the```syntax-inline
placeholder=""
```
. |

