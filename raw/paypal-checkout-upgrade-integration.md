---
title: Upgrade your Checkout integration
slug: /docs/checkout/standard/upgrade-integration/
createTime: '2024-03-04T23:56:06.384Z'
updateTime: '2025-05-09T11:05:00.429Z'
---

# Upgrade your Checkout integration

If you have previous checkout integrations, such as Express Checkout or `checkout.js`, PayPal recommends upgrading your integration with the JavaScript SDK.

The JavaScript SDK has the following benefits:

- Dynamically renders payment buttons instead of using static images.
- Launches payment flow in a pop-up window instead of redirecting to a new page.
- Supports greater control over payment button styles.

> **Warning:** If you want to continue offering Pay Later at checkout, integrate Billing With Purchase instead. It has the same features as Billing Agreement, but works with the payment options you already have.

## Know before you code

### Get sandbox account information

Complete the steps in Get started to get the following sandbox account information from the Developer Dashboard:

- Your client ID.
- Your personal and business sandbox accounts.

## Payer experience

After the payer authorizes the transaction, the payment buttons call your JavaScript callback rather than redirecting the payer to a return URL.

The payer takes the following actions:

1. Selects a payment button.
2. Logs into PayPal.
3. Approves the transaction on PayPal.
4. Returns to your site where you show a confirmation page.

![Flow diagram showing the new PayPal Checkout experience.](assets/paypal-checkout-upgrade-flow-diagram.svg)

Add the JavaScript SDK and payment buttons to your page:

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID">
        // Replace YOUR_CLIENT_ID with your sandbox client ID
    </script>
    <div id="paypal-button-container"></div>
</body>
</html>
```

Update the script tag to pass parameters including currency, intent, commit, and vault:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=EUR&intent=order&commit=false&vault=true">
</script>
```

## createOrder

When your payer selects the PayPal button, the script calls a `createOrder()` function. Return a promise for an order ID from the Orders v2 API.

**Note:** `createOrder()` replaces the `payment()` function from `checkout.js`. Migrate `actions.payment.create()` to a server-side call to the Create order endpoint.

### HTML example

```javascript
paypal.Buttons({
    createOrder() {
        return fetch("/my-server/create-paypal-order", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    cart: [{ sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT", quantity: "YOUR_PRODUCT_QUANTITY" }],
                }),
            })
            .then((response) => response.json())
            .then((order) => order.id);
    }
}).render('#paypal-button-container');
```

### Node.js example

```javascript
const { CLIENT_ID, APP_SECRET } = process.env;
const baseURL = {
    sandbox: "https://api-m.sandbox.paypal.com",
    production: "https://api-m.paypal.com"
};

app.post("/create-paypal-order", async(req, res) => {
    const order = await createOrder();
    res.json(order);
});

async function createOrder() {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
            intent: "CAPTURE",
            purchase_units: [{ amount: { currency_code: "USD", value: "100.00" } }],
        }),
    });
    const data = await response.json();
    return data;
}

async function generateAccessToken() {
    const auth = Buffer.from(CLIENT_ID + ":" + APP_SECRET).toString("base64");
    const response = await fetch(`${baseURL.sandbox}/v1/oauth2/token`, {
        method: "POST",
        body: "grant_type=client_credentials",
        headers: { Authorization: `Basic ${auth}` },
    });
    const data = await response.json();
    return data.access_token;
}
```

## onApprove / captureOrder

After the payer approves the transaction, the script calls `onApprove()`.

**Note:** `onApprove()` replaces `onAuthorize()` from `checkout.js`. Migrate `actions.payment.execute()` to a server-side call to the Orders Capture endpoint.

### HTML example

```javascript
paypal.Buttons({
    onApprove(data) {
        return fetch("/my-server/capture-paypal-order", {
                method: "POST",
                body: JSON.stringify({ orderID: data.orderID })
            })
            .then((response) => response.json())
            .then((orderData) => {
                const transaction = orderData.purchase_units[0].payments.captures[0];
                alert(`Transaction ${transaction.status}: ${transaction.id}`);
            });
    }
}).render('#paypal-button-container');
```

### Node.js example

```javascript
app.post("/capture-paypal-order", async(req, res) => {
    const { orderID } = req.params;
    const captureData = await capturePayment(orderID);
    res.json(captureData);
});

async function capturePayment(orderId) {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders/${orderId}/capture`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    });
    const data = await response.json();
    return data;
}
```

## Fix deprecations

Migration table from `checkout.js` to JavaScript SDK:

| Deprecated (`checkout.js`) | Upgrade to (JS SDK) |
| -------------------------- | ------------------- |
| Script → `paypalobjects.com/api/checkout.js` | Script → `paypalobjects.com/sdk/js` |
| `paypal.Button.render({}, '#el')` | `paypal.Buttons({}).render('#el')` |
| `payment()` callback | `createOrder()` callback |
| `actions.payment.create()` | Server-side `POST /v2/checkout/orders` |
| `onAuthorize()` callback | `onApprove()` callback |
| `actions.payment.execute()` | Server-side `POST /v2/checkout/orders/:id/capture` |
| `style.size` (small/medium/large/responsive) | Set container element size |
| `client` option in `render()` | `client-id=xyz` in script tag |
| `commit: true/false` in `render()` | `commit=true/false` in script tag |
| `env` option | Auto-detected from `client-id` |
| `locale` option | `locale=xx_XX` in script tag |
| `style.fundingicons` | Card buttons display automatically |
| `funding.allowed` | PayPal auto-selects optimal buttons |
| `funding.disallowed` | `disable-funding` or `disable-card` in script tag |
| `paypal.request` / `paypal.request.get/post` | Browser `fetch()` |
| `paypal.Promise` | Browser `Promise` |
| `return`/`cancel` URLs + `actions.redirect()` in `onAuthorize`/`onCancel` | `window.location.href` in `onApprove`/`onCancel` |
