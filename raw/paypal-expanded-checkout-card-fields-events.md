<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/card-fields-events/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / Subscribe to Card Field events

# Subscribe to Card Field events

> This JavaScript SDK documentation uses the CardFields component. If integrated with the legacy HostedFields component, see Hosted Field Events instead.

## Subscribe to events

Subscribe to advanced credit and debit card payment events using an event listener to update form UI based on field state.

### inputEvents

Pass an `inputEvents` object to the parent `cardField` component (applies to every field) or to each individual card field (overrides parent). 

## Supported input event callbacks

| Event Name | Description |
| ---------- | ----------- |
| `onChange` | Called when the input in any field changes. |
| `onFocus` | Called when any field gets focus. |
| `onBlur` | Called when any field loses focus. |
| `onInputSubmitRequest` | Called when a payer submits the field (e.g. presses Enter). |

### Example: inputEvents on parent component

```javascript
const cardField = paypal.CardFields({
    inputEvents: {
        onChange: function(data) {
            // Do something when an input changes
        },
        onFocus: function(data) {
            // Do something when a field gets focus
        },
        onBlur: function(data) {
            // Do something when a field loses focus
        },
        onInputSubmitRequest: function(data) {
            if (data.isFormValid) {
                // Submit the card form for the payer
            } else {
                // Inform payer that some fields are not valid
            }
        }
    }
})
```

### Example: inputEvents on individual component

```javascript
const cardField = paypal.CardFields(/* options */)
const nameField = cardField.NameField({
    inputEvents: {
        onChange: function(data) {
            // Only fires when name field changes
        },
        onInputSubmitRequest: function(data) {
            if (data.isFormValid) {
                // Submit the card form for the payer
            } else {
                // Inform payer that some fields are not valid
            }
        }
    }
});
```

### Sample state object

Each event callback returns a state object:

```javascript
data: {
    cards: [{code: {name: 'CVV', size: 3}, niceType: "Visa", type: "visa"}],
    emittedBy: "number",  // Not returned for getState()
    isFormValid: false,
    errors: ["INVALID_CVV"],
    fields: {
        cardCvvField: { isFocused: false, isEmpty: true, isValid: false, isPotentiallyValid: true },
        cardNumberField: { isFocused: true, isEmpty: false, isValid: false, isPotentiallyValid: true },
        cardNameField: { isFocused: false, isEmpty: true, isValid: false, isPotentiallyValid: true },
        cardExpiryField: { isFocused: false, isEmpty: true, isValid: false, isPotentiallyValid: true },
    },
}
```

### Validate individual fields

```javascript
const cardNumberField = cardFields.NumberField({
    inputEvents: {
        onChange: (data) => {
            cardContainer.className = data.fields.cardNumberField.isValid ? 'valid' : 'invalid';
        }
    }
})
```

### Validate entire card form

```javascript
const cardFields = paypal.CardFields({
    inputEvents: {
        onChange: (data) => {
            formContainer.className = data.isFormValid ? 'valid' : 'invalid'
        }
    }
});
```

## Methods on parent card fields

### `getState()` → `{promise | void}`

Returns a promise resolving to a `stateObject` with state of all fields, possible card types, and errors array. Note: `emittedBy` is NOT included in `getState()` response.

```javascript
cardFields.getState().then((data) => {
    if (data.isFormValid) {
        cardFields.submit().then(() => {
            // Submit success
        }).catch((error) => {
            // Submit error
        });
    }
});
```

### `isEligible()` → `{Boolean}`

Checks if a cardField instance can render based on configuration and business rules.

```javascript
if (cardFields.isEligible()) {
    cardFields.NumberField().render("#card-number-field-container");
    cardFields.CVVField().render("#card-cvv-field-container");
}
```

### `submit()` → `{promise | void}`

Submits payment information.

```javascript
multiCardFieldButton.addEventListener("click", () => {
    cardField.submit().then(() => {
        console.log("Card Fields submit");
    }).catch((err) => {
        console.log("There was an error with card fields: ", err);
    });
});
```

## Methods on individual card fields

| Method | Return | Description |
| ------ | ------ | ----------- |
| `addClass(className)` | promise/void | Adds a class to a field for dynamic styling |
| `clear()` | void | Clears the field value |
| `focus()` | void | Focuses the field |
| `removeAttribute(attr)` | promise/void | Removes an attribute. Supported: `aria-invalid`, `aria-required`, `disabled`, `placeholder` |
| `removeClass(className)` | promise/void | Removes a class from a field |
| `render(containerOrSelector)` | promise/void | Renders to DOM. Accepts DOM element OR CSS selector string |
| `setAttribute(attr, value)` | promise/void | Sets a supported attribute and value |
| `setMessage(message)` | void | Sets a message for screen readers |
| `close()` | promise/void | Tears down the field (disposes component created by render) |

### `render()` — accepts both DOM element and selector string

```javascript
// DOM element reference
cardField.NumberField().render(cardNumberContainer);
// OR CSS selector string
cardField.NumberField().render("#card-number-field-container")
```

### `removeAttribute()` — supported attributes

`aria-invalid`, `aria-required`, `disabled`, `placeholder`

## Type definitions

### `cardSecurityCode`

| Property | Type | Description |
| -------- | ---- | ----------- |
| `name` | string | `CVV`, `CID`, or `CVC` |
| `size` | number | Expected length (typically 3 or 4) |

### `cardType`

| Property | Type | Description |
| -------- | ---- | ----------- |
| `type` | string | Code-readable: `visa`, `mastercard`, `american-express`, `discover`, `diners-club`, `jcb`, `maestro`, `unionpay`, `elo`, `hiper`, `hipercard` |
| `niceType` | string | Human-readable: Visa, Mastercard, American Express, etc. |
| `code` | object cardSecurityCode | Security code requirements (name + size) |

### `cardFieldData` (per field in stateObject)

| Property | Type | Description |
| -------- | ---- | ----------- |
| `isFocused` | boolean | Field is currently focused |
| `isEmpty` | boolean | No value entered |
| `isPotentiallyValid` | boolean | Current input could become valid (e.g. `41` for card number) |
| `isValid` | boolean | Input is valid and can be submitted |

### `stateObject`

| Property | Type | Description |
| -------- | ---- | ----------- |
| `cards` | array of cardType | Potential card types. Single item once type is determined |
| `emittedBy` | string | Field name that triggered event. **Not in getState().** Values: `"name"`, `"number"`, `"cvv"`, `"expiry"` |
| `errors` | array | Invalid fields: `INELIGIBLE_CARD_VENDOR`, `INVALID_NAME`, `INVALID_NUMBER`, `INVALID_EXPIRY`, `INVALID_CVV` |
| `isFormValid` | boolean | Entire form is valid |
| `fields` | object | `cardNameField`, `cardCvvField`, `cardNumberField`, `cardExpiryField` — each a `cardFieldData` object |

## Full integration example

See raw file for complete HTML integration example including all fields, events, submit button, and `isEligible()` check.
