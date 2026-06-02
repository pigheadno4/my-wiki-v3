<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/set-up-your-api/braintree-integration -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up your API

To enable AI agents to create and manage shopping carts through your store, integrate with PayPal's Cart API. This guide shows you how to implement the 3 core endpoints that handle cart creation, updates, and checkout completion, including Braintree integration for payment processing.

> **Note:** You can view the complete protocol reference for the [Cart API](/reference/api/rest/cart-operations/create-cart/) and the [Complete Checkout API](/reference/api/rest/checkout-operations/complete-checkout/).

## API endpoints

The Cart API provides 3 core endpoints that handle the complete cart lifecycle. Each endpoint serves a specific purpose in the agentic shopping flow.

- `POST /merchant-cart` [creates](#create-a-cart) a new cart.
- `PUT /merchant-cart/{id}` [updates](#update-a-cart) an existing cart.
- `POST /merchant-cart/{id}/checkout` completes the checkout process.

> **Tip:** You can view the PayPal Cart schema [here](https://github.com/paypal/agent-commerce/blob/main/v1/api-spec.yaml).

### Authentication with PayPal-supplied JWTs

- **Request authentication:** Every API call includes the token in the [authorization header](#receive-token-in-the-authorization-header).
- **Merchant identification:** Tokens contain your merchant ID and permissions.
- **Security verification:** Verify token signature using PayPal's public keys. See [Verify the token](#verify-the-token).

#### Receive token in the authorization header

Every API request must include the PayPal-supplied JWT in the authorization header.

```bash lines theme={null}
POST /api/paypal/v1/merchant-cart
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJtZXJjaGFudF9pZCI6Ik1FUkNIQU5ULTEyMyIsInNjb3BlIjpbImNhcnQiXSwiaWF0IjoxNzE5MjQwMDAwLCJleHAiOjE3MTkyNDM2MDB9.signature
Content-Type: application/json

{
  ...cart create request body
}
```

#### Verify the token

1. Parse Authorization header: `"Bearer \<token\>"`.
2. Verify token signature using the PayPal [public key](https://www.paypal.ai/.well-known/jwks.json).
3. Validate the token expiration.

### Braintree credentials

To enable agentic checkout, we will need your Braintree credentials: `merchant_id` and `tokenization_key`. For more information, see [Important gateway credentials](https://developer.paypal.com/braintree/articles/control-panel/important-gateway-credentials).

### Create a cart

To create a new shopping cart with specified items, use `POST /merchant-cart`. The cart can also include customer information, such as a shipping address and payment method to use.

#### Cart creation

This example of a request payload shows how to structure a cart creation request with items and customer information.

```bash lines theme={null}
POST /api/paypal/v1/merchant-cart
Content-Type: application/json
Authorization: Bearer <paypal-jwt>

{
  "items": [...],
  "shipping_address": {...},
  "billing_address": {...},
  "customer": {"email_address": "customer@example.com"},
  "payment_method": {"type": "paypal"},
}
```

> **Important:** PayPal uses your Braintree credentials to create a token. You do not need to return a token here.

### Update a cart

To update an existing cart by replacing its contents with the provided data, use `PUT /merchant-cart/{id}`. Use this endpoint to add or remove items, change quantities, update the shipping address, apply discounts, and so on.

> **Important:** `PUT` replaces _the entire cart_. It removes or resets any fields that you do not include in your request. This is a complete replacement operation, not a merge.

Include all current cart data when making changes, as shown in the following example.

```json lines expandable theme={null}
{
  "items": [
    {"variant_id": "EXISTING-ITEM-VARIANT", "quantity": 5}
  ],
  "customer": {
    "email_address": "customer@example.com"
  },
  "shipping_address": {
    "address_line_1": "123 Current Street",
    "admin_area_2": "Current City",
    "admin_area_1": "CA",
    "postal_code": "95131",
    "country_code": "US"
  },
  "payment_method": {...}
}
```

### Complete checkout

To complete the checkout process for a cart, use `POST /merchant-cart/{id}/checkout`. This endpoint finalizes the purchase by processing the payment using the specified payment method.

```bash lines theme={null}
POST /api/paypal/v1/merchant-cart/CART-123/checkout
Content-Type: application/json
Authorization: Bearer <paypal-jwt-token>

{
  "payment_method": {
    "type": "paypal",
    "token": "15a93f45-fda1-12ee-7e10-1e0a3bdf2503", //BT nonce
  }
}
```

> **Important:** Within this endpoint, PayPal passes a Braintree nonce, which you can then use to create a transaction.

## Merchant cart response

The following examples show some successful responses that your API can return.

### Create and update cart response

Return comprehensive cart details including status, items, totals, and payment information.

```json lines expandable theme={null}
{
  "id": "CART-123",
  "status": "CREATED",
  "validation_status": "VALID",
  "validation_issues": [],
  "items": [
    {
      "variant_id": "SHIRT-001",
      "quantity": 1,
      "name": "Blue T-Shirt",
      "unit_amount": { "currency_code": "USD", "value": "25.00" },
      "item_total": { "currency_code": "USD", "value": "25.00" }
    }
  ],
  "shipping_address": {...},
  "billing_address": {...},
  "totals": {
    "subtotal": { "currency_code": "USD", "value": "25.00" },
    "shipping": { "currency_code": "USD", "value": "5.99" },
    "tax": { "currency_code": "USD", "value": "2.70" },
    "total": { "currency_code": "USD", "value": "33.69" }
  },
  "payment_method": {
    "type": "PAYPAL",
  },
}
```

### Complete checkout response

After successful checkout, return the completed cart status with payment confirmation.

```json lines expandable theme={null}
{
  "id": "CART-123",
  "status": "COMPLETED",
  "validation_status": "VALID",
  "validation_issues": [],
  "payment_confirmation": {
    "merchant_order_number": "ORDER-789",
    "order_review_page": "https://yourstore.com/orders/789"
  },
  "totals": {
    "total": {
      "currency_code": "USD",
      "value": "37.19"
    }
  }
}
```

## Next steps

Continue by [learning more about response handling](/growth/agentic-commerce/store-sync/your-api/set-up-your-api/response-handling).
