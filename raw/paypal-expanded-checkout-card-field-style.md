<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/ -->
<!-- Fetched: 2026-04-13 -->

Online / Checkout / Expanded / Customize / Card Fields Style Guide

# Card Fields Style Guide

> **Important:** This JavaScript SDK documentation uses the CardFields component. If you are integrated with the legacy HostedFields component, see Hosted Fields Style Guide instead.

Change the layout, width, height, and outer styling of the card fields. Modify the elements you supply as containers with your current stylesheets. For example, `input: { border: 1px solid #333; }`.

## Supported CSS properties

The CSS properties listed are the only properties supported in the advanced credit and debit card payments configuration. If you specify an unsupported CSS property, a warning is logged to the browser console.

- appearance
- background
- border
- border-radius
- box-shadow
- color
- direction
- font
- font-family
- font-size
- font-size-adjust
- font-stretch
- font-style
- font-variant
- font-variant-alternates
- font-variant-caps
- font-variant-east-asian
- font-variant-ligatures
- font-variant-numeric
- font-weight
- height
- letter-spacing
- line-height
- opacity
- outline
- padding
- padding-bottom
- padding-left
- padding-right
- padding-top
- text-shadow
- transition
- -moz-appearance
- -moz-osx-font-smoothing
- -moz-tap-highlight-color
- -moz-transition
- -webkit-appearance
- -webkit-osx-font-smoothing
- -webkit-tap-highlight-color
- -webkit-transition

## Examples

You can pass a style object into a parent cardField component or each card field individually.

### Style parent fields

Pass a style object to the parent cardField component to apply to every field:

```javascript
const cardStyle = {
  'input': {
    'font-size': '16px',
    'font-family': 'courier, monospace',
    'font-weight': 'lighter',
    'color': '#ccc',
  },
  '.invalid': {
    'color': 'purple',
  },
};
const cardField = paypal.CardFields({
  style: cardStyle
});
```

### Style individual fields

Pass a style object to an individual card field to apply to that field only. This **overrides** any object passed through a parent component:

```javascript
const nameFieldStyle = {
  'input': {
    'color': 'blue'
  },
  '.invalid': {
    'color': 'purple'
  },
};
const nameField = cardField.NameField({
  style: nameFieldStyle
}).render('#card-name-field-container');
```

## See also

- Card field properties
- JavaScript SDK reference
