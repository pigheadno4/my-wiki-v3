---
title: Standalone payment buttons
slug: /docs/checkout/standard/customize/standalone-buttons/
createTime: '2024-03-04T20:48:59.868Z'
updateTime: '2025-05-09T09:56:22.044Z'
---

# Standalone payment buttons

Add standalone buttons to customize how payment methods show up on your checkout page.

By default, all eligible payment buttons display in a single location on your page.

Use this integration to show individual, standalone payment buttons for each payment method. For example, show the PayPal button, Venmo button, and PayPal Pay Later offers on different parts of the checkout page, alongside different radio buttons, or on other pages.

Your standalone payment button integration uses the PayPal JavaScript SDK smart eligibility logic to show only the correct payment buttons for each payer on your checkout page.

> **Note (UK merchants):** Credit is a regulated activity in the UK. Before integrating a PayPal Credit button, you must be authorized to act as a credit broker and have a credit agreement with PayPal.

## Know before you code

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

> **Important:** Venmo is not supported in the sandbox.

## Supported buttons

| Payment method | Description |
| --- | --- |
| `paypal.FUNDING.PAYPAL` | PayPal |
| `paypal.FUNDING.CARD` | Credit or debit cards |
| `paypal.FUNDING.PAYLATER` | Pay Later (US, UK), Pay in 4 (AU), 4X PayPal (France), Paga en 3 plazos (Spain), Paga in 3 rate (Italy), Später Bezahlen (Germany) |
| `paypal.FUNDING.CREDIT` | PayPal Credit (US, UK) |
| `paypal.FUNDING.VENMO` | Venmo |

> **Note for US and UK merchants:** If you're enabling Pay Later or PayPal Credit, show both `paypal.FUNDING.PAYLATER` and `paypal.FUNDING.CREDIT` when eligible. Depending on payer eligibility, payment buttons render either the Pay Later or PayPal Credit button.

## Script tag

Update the JavaScript SDK tag to include `buttons` and `funding-eligibility` components:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=test&components=buttons,funding-eligibility"></script>
```

## Implementation patterns

### Standalone — all eligible buttons

```javascript
// Loop over each payment method
paypal.getFundingSources().forEach(function(fundingSource) {
    var button = paypal.Buttons({ fundingSource: fundingSource });
    if (button.isEligible()) {
        button.render('#paypal-button-container');
    }
});
```

### Set of buttons — specific subset

```javascript
var FUNDING_SOURCES = [
    paypal.FUNDING.PAYPAL,
    paypal.FUNDING.VENMO,
    paypal.FUNDING.PAYLATER,
    paypal.FUNDING.CREDIT,
    paypal.FUNDING.CARD,
];
FUNDING_SOURCES.forEach(function(fundingSource) {
    var button = paypal.Buttons({ fundingSource: fundingSource });
    if (button.isEligible()) {
        button.render('#paypal-button-container');
    }
});
```

### Radio buttons — Marks component

For radio button integrations, add the `marks` component to the script tag:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=test&components=buttons,funding-eligibility,marks"></script>
```

Then render marks alongside radio buttons:

```javascript
paypal.getFundingSources().forEach(function(fundingSource) {
    var mark = paypal.Marks({ fundingSource: fundingSource });
    if (mark.isEligible()) {
        mark.render('#paypal-mark-container');
    }
});
```

### Two divs — buttons in different page sections

Render PayPal and Venmo buttons in separate containers on the same page:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=test&currency=USD&components=buttons,funding-eligibility&enable-funding=venmo&disable-funding=card"></script>
<script>
createButton(paypal.FUNDING.PAYPAL);
createButton(paypal.FUNDING.VENMO);

function createButton(fundingSource) {
    var config = {
        fundingSource: fundingSource,
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{ "amount": { "currency_code": "USD", "value": 1 } }]
            });
        },
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                alert('Transaction completed by ' + details.payer.name.given_name + '!');
            });
        }
    };
    var button = paypal.Buttons(config);
    if (button.isEligible()) {
        button.render('#' + fundingSource + '-button');
    }
}
</script>
```
