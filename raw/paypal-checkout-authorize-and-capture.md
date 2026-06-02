---
title: Authorize a payment and capture funds later
slug: /docs/checkout/standard/customize/authorization/
createTime: '2024-02-28T23:46:13.692Z'
updateTime: '2025-05-09T10:10:31.770Z'
---

# Authorize a payment and capture funds later

The PayPal Checkout integration supports a 2-step authorize and capture payment model.

Authorize a buyer's funds before you capture them, then settle the purchase later. An authorization places a hold on the funds and is valid for 29 days. For example, use authorize and capture to complete a task before finalizing the payment, such as verifying that you have the item in stock.

## How it works

- The payer checks out and provides a payment method.
- You authorize the payment.
- A hold is placed on the payment method until you are ready to capture payment.
- You finalize the transaction and capture the payment.
- The payer's payment method is charged.

## Know before you code

### You need a developer account to get sandbox credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.
- Client secret: Authorizes an app in your sandbox. Keep this secret safe and don't share it.

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- JavaScript SDK: Adds PayPal-supported payment methods.
- Orders REST API: Create, update, retrieve, authorize, and capture orders.
- Payments REST API: Authorize, capture, retrieve, and refund payments.

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs.

The default approval intent of the JavaScript SDK is to both authorize the transaction and capture payment immediately. To split authorize and capture into separate actions, add `&intent=authorize` to the JavaScript SDK script tag, as shown in the following example:

#### Change intent sample code

```javascript
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&intent=authorize">
</script>
```

The `onApprove` function in the default integration captures the payment immediately. Replace the existing `onApprove` function with the following code. This code authorizes the payment but doesn't capture it.

#### onApprove code sample

```javascript
onApprove: function(data) {
  // Authorize the transaction
  return fetch('/my-server/authorize-paypal-order', {
    method: 'post',
    body: JSON.stringify({
      orderID: data.orderID
    })
  })
  .then(response => response.json())
  .then((authorizePayload) => {
      // Get the authorization id from your payload
      const authorizationID = authorizePayload.authorizationID;
      // Optional message given to purchaser
      alert(`
        You have authorized this transaction.
        Order ID: ${data.orderID}
        Authorization ID: ${authorizationID}
      `);

      // Later you can use your server to validate and capture the transaction
    });
  })
}
```

### Step result

A successful authorization results in:

- A Pending transaction in your business account.
- A hold on the money that is valid for 29 days. After a successful authorization, capture the payment within the 3-day honor period. Payment capture is subject to risk and money availability.

You can use your server-side code to capture the order ID and authorization ID passed in the fetch method in the `onApprove` function.

## Capture order and authorization IDs

Each server implementation is different. Make sure you have logic in your server-side code to receive the order ID and authorization ID that you pass from the client-side JavaScript fetch function.

Copy the following code and modify it to save the details to your server-side database.

### Sample request

API endpoint used: Show order details (`GET /v2/checkout/orders/{order_id}`)

#### Show order details sample request

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/48S239579N169645 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN"
```

Modify the following:
- `Access-Token` — Your access token.
- Order ID — Replace the sample ID (`48S239579N169645`) with your order ID.

### Step result

A successful request results in:

- HTTP 200 OK
- JSON response body containing order details to save to your server-side database.

After you capture the order details, you can complete any business tasks (e.g. verifying inventory) before capturing payment.

### Sample response — Save order information

```json
{
  "id": "48S239579N1696452",
  "intent": "AUTHORIZE",
  "purchase_units": [{
    "reference_id": "default",
    "amount": {
      "currency_code": "USD",
      "value": "30.00"
    },
    "payee": {
      "email_address": "payee@example.com",
      "merchant_id": "JK9AB28SRU4XL"
    },
    "shipping": {
      "name": { "full_name": "Firstname Lastname" },
      "address": {
        "address_line_1": "123 Main St.",
        "admin_area_2": "Anytown",
        "admin_area_1": "CA",
        "postal_code": "12345",
        "country_code": "US"
      }
    },
    "payments": {
      "authorizations": [{
        "status": "CREATED",
        "id": "66P728836U784324A",
        "amount": { "currency_code": "USD", "value": "30.00" },
        "seller_protection": {
          "status": "ELIGIBLE",
          "dispute_categories": ["ITEM_NOT_RECEIVED", "UNAUTHORIZED_TRANSACTION"]
        },
        "expiration_time": "2020-01-01T15:57:51Z",
        "links": [
          { "href": "https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A", "rel": "self", "method": "GET" },
          { "href": "https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A/capture", "rel": "capture", "method": "POST" },
          { "href": "https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A/void", "rel": "void", "method": "POST" },
          { "href": "https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A/reauthorize", "rel": "reauthorize", "method": "POST" },
          { "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/48S239579N1696452", "rel": "up", "method": "GET" }
        ],
        "create_time": "2020-02-03T15:57:51Z",
        "update_time": "2020-02-03T15:57:51Z"
      }]
    }
  }],
  "payer": {
    "name": { "given_name": "Firstname", "surname": "Lastname" },
    "email_address": "payer@example.com",
    "payer_id": "8Y7QBG68GYPHQ",
    "address": { "country_code": "US" }
  },
  "create_time": "2020-02-03T15:57:17Z",
  "update_time": "2020-02-03T15:57:51Z",
  "links": [
    { "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/48S239579N1696452", "rel": "self", "method": "GET" }
  ],
  "status": "COMPLETED"
}
```

If you haven't captured the payment within 3 days of authorization, you can reauthorize the payment to make sure the money is still available.

You can issue multiple reauthorizations within the 29-day authorization period after the honor period expires. A reauthorization generates a new authorization ID and restarts the 3-day honor period. Use the new authorization ID on subsequent captures.

If you reauthorize on the 27th day of the authorization period, you get only 2 days of the honor period.

### Sample request — Reauthorize payment

API endpoint used: Reauthorize authorized payment (`POST /v2/payments/authorizations/{authorization_id}/reauthorize`)

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A/reauthorize \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: PAYPAL-REQUEST-ID"
```

Modify the following:
- `Access-Token` — Your access token.
- Authorization ID — Replace `66P728836U784324A` with your authorization ID.
- `PAYPAL-REQUEST-ID` — A unique alphanumeric ID you generate to prevent duplicate authorizations (idempotency key).

### Step result

A successful request results in:

- HTTP 201 Created
- JSON response body containing a new authorization ID to use for capture.

### Sample response — Reauthorize payment

```json
{
  "id": "8AA831015G517922L",
  "status": "CREATED",
  "links": [
    { "rel": "self", "method": "GET", "href": "https://api-m.paypal.com/v2/payments/authorizations/8AA831015G517922L" },
    { "rel": "capture", "method": "POST", "href": "https://api-m.paypal.com/v2/payments/authorizations/8AA831015G517922L/capture" },
    { "rel": "void", "method": "POST", "href": "https://api-m.paypal.com/v2/payments/authorizations/8AA831015G517922L/void" },
    { "rel": "reauthorize", "method": "POST", "href": "https://api-m.paypal.com/v2/payments/authorizations/8AA831015G517922L/reauthorize" }
  ]
}
```

### Sample request — Capture payment

API endpoint used: Capture authorized payment (`POST /v2/payments/authorizations/{authorization_id}/capture`)

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A/capture \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
  -H "PayPal-Request-Id: PAYPAL-REQUEST-ID"
```

Modify the following:
- `ACCESS-TOKEN` — Your access token.
- Authorization ID — Replace `66P728836U784324A` with your authorization ID (original or from reauthorization).
- `PAYPAL-REQUEST-ID` — A unique alphanumeric ID you generate (idempotency key).

### Step result

A successful request results in:

- HTTP 201 Created
- JSON response body with captured payment details. Save the capture ID for future refunds.
- Transaction in your business account changes from Pending to Completed.

### Sample response — Capture payment

```json
{
  "id": "5KA38057EC136584R",
  "status": "COMPLETED",
  "links": [
    { "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/5KA38057EC136584R", "rel": "self", "method": "GET" },
    { "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/5KA38057EC136584R/refund", "rel": "refund", "method": "POST" },
    { "href": "https://api-m.sandbox.paypal.com/v2/payments/authorizations/66P728836U784324A", "rel": "up", "method": "GET" }
  ]
}
```

## Next steps and customizations

- **Test integration** — Test in the sandbox environment before going live.
- **Go live** — Move from PayPal's production environment to go live.
- **Implement 3D Secure** — Authenticate cardholders through card issuers.
- **Authorization and honor period** — Authorization and capture timing for 2-step payments.
- **Payments API** — Learn more about the Payments API.
- **Void an authorization** — Cancel an authorized payment using the Payments API.
- **Handle a refund** — Refund a captured payment using the Payments API.
