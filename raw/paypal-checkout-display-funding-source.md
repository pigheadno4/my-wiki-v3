---
title: Display funding source used
slug: /docs/checkout/standard/customize/display-funding-source/
createTime: '2024-03-01T01:59:02.872Z'
updateTime: '2025-05-13T15:56:41.533Z'
---

# Display funding source used

Display the funding source used to your buyers to provide a unique experience.

If you have a confirmation page or notification in your checkout workflow, display the payment source the payer selected.

For example, if the payer paid with Venmo, show Venmo as the payment source on the confirmation page or notification.

## Know before you code

### You need a developer account to get sandbox credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.
- Client secret: Authorizes an app in your sandbox. Keep this secret safe and don't share it.

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs.

Your Checkout experience might have a confirmation page or a notification to the user that they're paying with PayPal. Ensure the funding source the user chose, such as Venmo, shows as expected or it might lead to confusion and reduced Checkout conversion.

Use an `onClick` handler to get the funding source and display it on a confirmation page.

#### Show funding source

```javascript
let fundingSource;

paypal.Buttons({
    onClick: (data) => {
        // fundingSource = "venmo"
        fundingSource = data.fundingSource;

        // Use this value to determine the funding source used to pay
        // Update your confirmation pages and notifications from "PayPal" to "Venmo"
    }
})
```

The following table shows supported `fundingSource` values:

| Funding source | Description |
| --- | --- |
| `paypal.FUNDING.PAYPAL` | PayPal |
| `paypal.FUNDING.CARD` | Credit or debit cards |
| `paypal.FUNDING.PAYLATER` | Pay Later (US, UK), Pay in 4 (AU), 4X PayPal (France), Paga en 3 plazos (Spain), Paga in 3 rate (Italy), Später Bezahlen (Germany) |
| `paypal.FUNDING.CREDIT` | PayPal Credit |
| `paypal.FUNDING.VENMO` | Venmo |

## Next steps and customizations

- **Test integration** — Test in the sandbox environment before going live.
- **Go live** — Move from PayPal's production environment to go live.
- **JavaScript SDK Reference** — Customize your integration with script config parameters.
