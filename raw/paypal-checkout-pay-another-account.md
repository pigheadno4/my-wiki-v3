---
title: 'Pay another account '
slug: /docs/checkout/standard/customize/pay-another-account/
createTime: '2024-03-01T22:06:45.801Z'
updateTime: '2024-04-19T23:03:38.593Z'
---

# Pay another account

By default, money is paid to the application owner in their own account. The account receiving funds is known as the payee.

To specify a different payee when you create an order:

- Add the `payee` object to the transaction payload.
- Include the `email_address` or `merchant_id` of the account to receive the payment.

### Sample request

```javascript
async function createOrder() {
    // Create accessToken using your clientID and clientSecret
    const accessToken = "REPLACE_WITH_YOUR_ACCESS_TOKEN"
    return fetch("https://api-m.sandbox.paypal.com/v2/checkout/orders", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${accessToken}`,
            },
            body: JSON.stringify({
                intent: "CAPTURE",
                purchase_units: [{
                    amount: {
                        value: "15.00",
                        currency_code: "USD",
                    },
                    payee: {
                        email_address: "payee@example.com",
                    },
                }],
            }),
        })
        .then((response) => response.json())
        .then((data) => console.log(data));
}
```
