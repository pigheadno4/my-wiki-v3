<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/upgrade/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Upgrade your Checkout integration
slug: /docs/checkout/advanced/upgrade/
createTime: '2024-08-05T20:54:16.578Z'
updateTime: '2025-05-12T14:36:52.178Z'
---


# Upgrade your Checkout integration

If you have an Express Checkout or PayPal Checkout integration, PayPal recommends upgrading to Expanded Checkout using the JavaScript SDK.

The JavaScript SDK has the following benefits:

- Dynamically renders payment buttons instead of using static images.
- Launches payment flow in a pop-up window instead of redirecting to a new page.
- Supports greater control over payment button styles.



## Getting started 

### 1. Review current integration

#### PayPal Checkout
PayPal Checkout uses the same APIs as Expanded Checkout. You don't need to change your API calls or collect parameter information about your current PayPal Checkout integration when you upgrade to Expanded Checkout.

#### Express Checkout
If you have an Express Checkout integration, collect information about your current integration, such as API calls and parameters, so you can set up your new integration.

1. Identify core API calls — locate SetExpressCheckout, GetExpressCheckoutDetails, DoExpressCheckoutPayment in your code
2. Document parameters (e.g. PAYMENTREQUEST_0_AMT)
3. Use the Parameter Mapping Tool at /tools/limited/api-transformer/mapping/ in PayPal API Transformer

### 2. Set up your sandbox

Get credentials: client ID, client secret, access token.

This integration requires a sandbox business account with the **Expanded Credit and Debit Card Payments** capability enabled:
- PayPal Developer Dashboard → toggle Sandbox → Apps & Credentials → select app → Features → Accept payments → enable Expanded Credit and Debit Card Payments → Save Changes

Note: If you created sandbox account via sandbox.paypal.com and capability is disabled, complete sandbox onboarding at sandbox.paypal.com/bizsignup/.



## Set up front end

### PayPal Checkout → Expanded Checkout

Just add `components=buttons,card-fields` to the script tag:

**Before (PayPal Checkout):**
```html
<script src="https://www.paypal.com/sdk/js?currency=USD&client-id=YOUR_SANDBOX_CLIENT_ID"></script>
```

**After (Expanded Checkout):**
```html
<script src="https://www.paypal.com/sdk/js?currency=USD&client-id=YOUR_SANDBOX_CLIENT_ID&components=buttons,card-fields"></script>
```

### Express Checkout → Expanded Checkout

For NVP/SOAP-only integrations:
1. Follow steps 1-5 of the Integrate PayPal Checkout guide to set up JS SDK v5
2. Add `components=buttons,card-fields` to the script tag

For NVP/SOAP + JS SDK v4:
1. Upgrade SDK from v4 to v5 (see upgrade guide)
2. Add `components=buttons,card-fields` to the script tag



## Create and render card fields and payment buttons

### PayPal Checkout → Expanded Checkout

**Before:**
```html
<div id="paypal-button-container"></div>
<script>
  paypal.Buttons({
    // Button configuration and event handlers
  }).render('#paypal-button-container');
</script>
```

**After:**
```html
<div id="paypal-button-container"></div>
<div class="card-fields-container">
  <div id="card-fields" class="card-fields"></div>
  <button id="card-fields-submit">Submit</button>
</div>
<script>
  paypal.Buttons({
    // Button configuration and event handlers
  }).render('#paypal-button-container');

  paypal.CardFields({
    createOrder: function() {
      return fetch('/create-order', { method: 'post' })
        .then(function(res) { return res.json(); })
        .then(function(orderData) { return orderData.id; });
    }
  }).render('#card-fields');

  document.getElementById('card-fields-submit').addEventListener('click', function() {
    paypal.CardFields().submit()
      .then(function(result) { alert('Payment authorized'); })
      .catch(function(err) {
        console.error('Payment authorization failed:', err);
        alert('Payment authorization failed');
      });
  });
</script>
```

### Express Checkout → Expanded Checkout

```javascript
paypal.CardFields({
  createOrder: function() {
    return fetch('/create-order', { method: 'post' })
      .then(function(res) { return res.json() })
      .then(function(orderData) { return orderData.id; });
  }
}).render('#card-fields');

document.getElementById('card-fields-submit').addEventListener('click', function() {
  paypal.CardFields().submit()
    .then(function(result) { alert('Payment authorized'); })
    .catch(function(err) {
      console.error('Payment authorization failed:', err);
      alert('Payment authorization failed');
    });
});
```



## Set up server-side processing

### PayPal Checkout → Expanded Checkout
No server-side changes needed. Same APIs.

### Express Checkout → Expanded Checkout

#### NVP/SOAP → Orders v2 API mapping

| NVP/SOAP API | Orders v2 REST API |
| --- | --- |
| METHOD=SetExpressCheckout | POST /v2/checkout/orders |
| METHOD=GetExpressCheckout | GET /v2/checkout/orders/{order_id} |
| METHOD=DoExpressCheckout (capture) | POST /v2/checkout/orders/{order_id}/capture |
| METHOD=DoExpressCheckout (update + capture) | PATCH /v2/checkout/orders/{order_id} + POST /v2/checkout/orders/{order_id}/capture |

**Important:** In NVP/SOAP, DoExpressCheckout could update and capture in one call. In Orders v2, these are **two separate calls**.

Use the API Transformer tool at developer.paypal.com/tools/limited/api-transformer/converter/ to help convert NVP/SOAP request bodies.

#### Example payload mappings

**1. SetExpressCheckout → POST /v2/checkout/orders**

NVP: `METHOD=SetExpressCheckout&PAYMENTREQUEST_0_AMT=111.11&PAYMENTREQUEST_0_PAYMENTACTION=Sale`

REST:
```bash
curl -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders' \
-H 'Content-Type: application/json' \
-H 'Prefer: return=representation' \
-H 'Authorization: Bearer bearer_access_token' \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [{ "amount": { "currency_code": "USD", "value": "111.11" } }],
  "payment_source": {
    "paypal": {
      "experience_context": {
        "return_url": "http://mywebsite.com/return",
        "cancel_url": "http://mywebsite.com/cancel"
      }
    }
  }
}'
```

**2. GetExpressCheckoutDetails → GET /v2/checkout/orders/{id}**

NVP: `METHOD=GetExpressCheckoutDetails&TOKEN=EC-72D0681527109671C`

REST:
```bash
curl https://api-m.sandbox.paypal.com/v2/checkout/orders/2HX49812L18884342 \
-H 'Authorization: Bearer bearer_access_token'
```

**3. DoExpressCheckoutPayments → POST /v2/checkout/orders/{id}/capture**

NVP: `METHOD=DoExpressCheckoutPayments&TOKEN=EC-72D0681527109671C&PAYMENTREQUEST_0_PAYMENTACTION=Sale&PAYMENTREQUEST_0_AMT=111.11`

REST:
```bash
curl -X POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/2HX49812L18884342/capture' \
-H 'Content-Type: application/json' \
-H 'Prefer: return=representation' \
-H 'Authorization: Bearer bearer_access_token'
```

#### Generate access token (OAuth2 vs NVP credentials)

NVP/SOAP used USER/PWD/SIGNATURE directly in requests. Orders v2 uses OAuth2:

```javascript
const generateAccessToken = async () => {
  try {
    if (!PAYPAL_CLIENT_ID || !PAYPAL_CLIENT_SECRET) {
      throw new Error("MISSING_API_CREDENTIALS");
    }
    const auth = Buffer.from(PAYPAL_CLIENT_ID + ":" + PAYPAL_CLIENT_SECRET).toString("base64");
    const response = await fetch(`${base}/v1/oauth2/token`, {
      method: "POST",
      body: "grant_type=client_credentials",
      headers: { Authorization: `Basic ${auth}` },
    });
    const data = await response.json();
    return data.access_token;
  } catch (error) {
    console.error("Failed to generate Access Token:", error);
  }
};
```

#### Handle API responses

```javascript
async function handleResponse(response) {
  try {
    const jsonResponse = await response.json();
    return { jsonResponse, httpStatusCode: response.status };
  } catch (err) {
    const errorMessage = await response.text();
    throw new Error(errorMessage);
  }
}
```



## Test integration
- PayPal payment: use personal sandbox accounts, verify money arrives in sandbox business account
- Card payment: use credit card generator at developer.paypal.com/tools/sandbox/card-testing/

## Go live
- Log into Developer Dashboard with PayPal business account
- Obtain live credentials (client ID + client secret)
- Update endpoint from api-m.sandbox.paypal.com to api-m.paypal.com
