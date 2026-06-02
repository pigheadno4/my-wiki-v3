---
title: Custom style for payment fields
slug: /docs/checkout/apm/reference/style/
createTime: "2024-08-15T07:29:45.589Z"
updateTime: "2025-05-14T15:00:52.289Z"
---

# Custom style for payment fields

Supported variables and rules parameters for payment fields style object:

| **Variables** | |
| **Parameter** | **Description** |
| fontFamily | Set the font-family of payment fields text |
| fontSizeBase | Set the size of the input, placeholder, and dropdown text values |
| fontSizeM | Set the size of the payment fields title description |
| textColor | Set the color of the payment fields title description, input, and dropdown text |
| colorTextPlaceholder | Set the color of the placeholder text |
| colorBackground | Set the background color of the input and dropdown fields |
| colorDanger | Set the color for the invalid field border and validation text |
| borderRadius | Set the border radius for the input and dropdown fields |
| borderWidth | Set the border width for the input and dropdown fields |
| borderFocusColor | Set the border color of the field that is focused |
| spacingUnit | Set the distance between fields (when there are multiple fields) |

| **Rules** | |
| **Parameter** | **Description** |
| .Input | Set CSS properties for the input fields |
| .Input:hover | Set CSS properties for the input fields on mouse hover |
| .Input:focus | Set CSS properties for the input fields on focus |
| .Input:active | Set CSS properties for the input fields when clicked |
| .Input--invalid | Set CSS properties for the input fields when invalid input is entered |
| .Label | Set CSS properties for the input field labels |

The following example shows how you can use the styles object:

paypal.PaymentFields({  
 fundingSource: paypal.FUNDING.OXXO,

// style object is optional
style: {
// customize field attributes (optional)
variables: {
fontFamily: "'Helvetica Neue', Arial, sans-serif",
fontSizeBase: "0.9375rem",
fontSizeSm: "0.81rem",
fontSizeM: "0.93rem",
fontSizeLg: "1.0625rem",
textColor: "#2c2e2f",
colorTextPlaceholder: "#2c2e2f",
colorBackground: "#fff",
colorInfo: "#0dcaf0",
colorDanger: "#d20000",
borderRadius: "0.2rem",
borderColor: "#dfe1e5",
borderWidth: "1px",
borderFocusColor: "black",
spacingUnit: "10px",
},

    // set custom rules to apply to fields classes (optional)
    // see https://www.w3schools.com/css/css_syntax.asp fore more on selectors and declarations
    rules: {
      ".Input": {},
      ".Input:hover": {},
      ".Input:focus": {
        color: 'blue',
        boxShadow: '0px 2px 4px rgb(0 0 0 / 50%), 0px 1px 6px rgb(0 0 0 / 25%)',
      },
      ".Input:active": {},
      ".Input--invalid": {},
      ".Label": {},
    },

},
})
.render("#oxxo-container");
