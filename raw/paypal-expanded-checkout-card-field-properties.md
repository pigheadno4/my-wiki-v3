<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/card-field-properties/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / Card field properties for direct merchants

# Card field properties for direct merchants

> **Important:** This is version 2 of the card field properties guide for direct merchants.

The following card field properties are used to capture a payment. Use the `render()` method to render these instances to the DOM.

| Property | Type | Field created | Required |
| -------- | ---- | ------------- | -------- |
| `CVVField` | Function | Card CVV or CID, a 3 or 4-digit code | Yes |
| `ExpiryField` | Function | Card expiration date | Yes |
| `NameField` | Function | Name for the card | No |
| `NumberField` | Function | Card number | Yes |

## Card field options

Customize event callbacks or the style of each field with the following options:

| Property | Type | Description | Required |
| -------- | ---- | ----------- | -------- |
| `inputEvents` | Object inputEvents | Callbacks for when a specified input event occurs for a field. | No |
| `style` | Object style guide | Style a field with supported CSS properties. | No |
| `placeholder` | String | Custom placeholder text (each field has a default). | No |

```javascript
const cardNameContainer = document.getElementById("card-name-field-container");
const nameField = cardField.NameField({
  placeholder: "Enter your full name as it appears on your card",
  inputEvents: {
    onChange: (event) => {
      console.log("returns a stateObject", event);
    }
  },
  style: {
    ".invalid": {
      "color": "purple",
    }
  }
});
nameField.render(cardNameContainer);

const cardNumberContainer = document.getElementById("card-number-field-container");
const numberField = cardField.NumberField(/*options*/);
numberField.render(cardNumberContainer);

const cardExpiryContainer = document.getElementById("card-expiry-field-container");
const expiryField = cardField.ExpiryField(/*options*/);
expiryField.render(cardExpiryContainer);

const cardCvvContainer = document.getElementById("card-cvv-field-container");
const cvvField = cardField.CVVField(/*options*/);
cvvField.render(cardCvvContainer);
```

## See also

- Style card fields
- JavaScript SDK reference
