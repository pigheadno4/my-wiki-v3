---
title: Messaging with buttons
slug: /docs/checkout/standard/customize/messaging-with-buttons/
createTime: '2024-04-25T23:13:06.289Z'
updateTime: '2024-12-16T05:33:01.281Z'
---

# Messaging with buttons

Integrate messaging directly with your buttons to promote Pay Later offers and other PayPal value propositions to your customers. Adding messaging can help improve conversion and attract new customers.

![Pay Later messaging shown alongside PayPal buttons in horizontal layout.](assets/paypal-messaging-header-horizontal.png)

> **Note:** Messaging is currently only supported for US merchants and US customers. Merchants must be eligible for Pay Later to display Pay Later offers with buttons. Other PayPal value propositions will still show, if ineligible for Pay Later.

## Know before you code

### Prerequisites

This feature modifies an existing checkout integration and uses the following:

- PayPal JavaScript SDK
- Orders REST API — Create order endpoint

## Integration

Include your messaging options to the buttons configuration object. To display the strongest message to the customer, use `message.amount` with the current total based on the product or cart.

> **Note:** The `message.amount` option functions independently from the captured order total and has no impact on it.

### Add messaging to buttons

```javascript
const buttons = paypal.Buttons({
  message: {
    amount: 100, // Update to your cart or product total amount
    align: 'center',
    color: 'black',
  }
});
buttons.render('#paypal-button-container');
```

### Button examples

The message content adapts to the buttons that are displayed:

**Vertical Stack**

```javascript
paypal.Buttons({
  style: { layout: "vertical" },
  message: { amount: 100 }
});
```

Note: The message is positioned to the top to make room for the text that accompanies the debit/credit Card button.

![Vertical stack layout with Pay Later messaging above buttons.](assets/paypal-messaging-vertical-stack.png)

**Horizontal Stack**

```javascript
paypal.Buttons({
  style: { layout: "horizontal" },
  message: { amount: 100 }
});
```

![Horizontal stack layout with Pay Later messaging.](assets/paypal-messaging-horizontal-stack.png)

**Standalone PayPal**

```javascript
paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYPAL,
  message: { amount: 20 }
});
```

![Standalone PayPal button with non-Pay Later messaging.](assets/paypal-messaging-standalone-paypal.png)

**Standalone Pay Later**

```javascript
paypal.Buttons({
  fundingSource: paypal.FUNDING.PAYLATER,
  message: { amount: 100 }
});
```

![Standalone Pay Later button with Pay Later messaging.](assets/paypal-messaging-standalone-paylater.png)

### Update the message amount

As the product count or cart total changes, update `message.amount` to reflect the latest total:

```javascript
buttons.updateProps({
  message: {
    amount: 200, // Update to your cart or product total amount
    align: 'center',
    color: 'black',
  }
});
```

> **Note:** Ensure that all previously specified message options are passed into `updateProps` including any options that have not changed; otherwise, they will be overwritten with default values.

## Complete your integration

Return to the Set up standard payments guide to create and capture the order.

## See also

- **Pay Later messaging** — Learn more about adding messaging next to your product price and cart totals.
- **JavaScript SDK** — Learn more about passing parameters to customize your integration.
