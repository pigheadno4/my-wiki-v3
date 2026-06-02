<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/set-up-your-api/orders-v2-integration -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up your API

To enable AI agents to create and manage shopping carts through your store, integrate with PayPal's Cart API. This guide shows you how to implement the 3 core endpoints that handle cart creation, updates, and checkout completion, including PayPal [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/) integration for payment processing.

> **Note:** You can view the complete protocol reference for the [Cart API](/reference/api/rest/cart-operations/create-cart/) and the [Complete Checkout API](/reference/api/rest/checkout-operations/complete-checkout/).

## API endpoints

The Cart API provides 3 core endpoints that handle the complete cart lifecycle. Each endpoint serves a specific purpose in the agentic shopping flow.

- `POST /merchant-cart` [creates](#create-a-cart) a new cart.
- `PUT /merchant-cart/{id}` [updates](#update-a-cart) an existing cart.
- `POST /merchant-cart/{id}/checkout` completes the checkout process.

> **Tip:** You can view the PayPal Cart schema <a href="/api-reference/paypal-cart-agentic-commerce-v1.yaml" download="api-spec.yaml">here</a>.

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

1. Parse the authorization header: `"Bearer \<token\>"`.
2. Verify token signature using the PayPal [public key](https://www.paypal.ai/.well-known/jwks.json).
3. Validate the token expiration.

### Create a cart

To create a new shopping cart with specified items, use `POST /merchant-cart`. The cart also can include customer information, such as a shipping address and payment method to use.

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

### Update a cart

To update an existing cart by replacing its contents with the provided data, use `PUT /merchant-cart/{id}`. With this endpoint, you can add or remove items, change quantities, update the shipping address, apply discounts, and so on.

> **Important:** `PUT` replaces _the entire cart_. It removes or resets any fields that you do not include in your request. This is a complete replacement operation, not a merge.

Include all current cart data when making changes, as shown in the following example.

```json lines expandable theme={null}
{
  "items": [
    {"variant_id": "EXISTING-ITEM-VARIANT", "quantity": 5}
  ],
  "customer": {
    "email_address": "buyer@example.com"
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

> **Important:** Within this endpoint, a merchant is expected to implement [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/) integration. For more information about this, see [Cart update with an order update](#cart-update-with-an-order-update).

### Complete checkout

To complete the checkout process for a cart, use `POST /merchant-cart/{id}/checkout`. This endpoint finalizes the purchase by processing the payment using the specified payment method.

```bash lines theme={null}
POST /api/paypal/v1/merchant-cart/CART-123/checkout
Content-Type: application/json
Authorization: Bearer <paypal-jwt-token>

{
  "payment_method": {
    "type": "paypal",
    "token": "EC-7U8939823K567", //PayPal Orders V2 ID
    "payer_id": "PAYER123456789" //PayPal User Identifier
  }
}
```

> **Important:** Within this endpoint, a merchant is expected to implement [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/) integration. For more information about this, see [Cart completed with an order captured](#cart-completed-with-an-order-captured).

## PayPal Orders API integration pattern

Behind the scenes, the PayPal Cart API integrates with PayPal's [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/) to manage payment tokens and process transactions. Understanding this relationship helps you implement proper payment handling.

When implementing the Cart API, merchants must integrate with **<a href="https://developer.paypal.com/docs/api/orders/v2/" target="_blank" rel="noopener noreferrer">PayPal Orders API v2</a>** to handle payment tokens and order updates.

The following table explains when to create (`POST`) or update (`PATCH`) a cart.

| Scenario                                                     | PayPal Orders Action                    | Reason                            |
| ------------------------------------------------------------ | --------------------------------------- | --------------------------------- |
| Create a cart.                                               | `POST /v2/orders`                       | Create a new payment context.     |
| Add or remove items.                                         | `PATCH /v2/orders/{id}`                 | Update totals.                    |
| Apply or remove coupons.                                     | `PATCH /v2/orders/{id}`                 | Update totals.                    |
| Update the shipping address.                                 | `PATCH /v2/orders/{id}`                 | Update shipping and tax.          |
| Change quantities.                                           | `PATCH /v2/orders/{id}`                 | Update totals.                    |
| Create a fresh payment context when a payment token expires. | `POST /v2/orders`                       | Create a fresh payment context.   |
| Create a new cart after checkout.                            | `POST /v2/orders`                       | Prepare for a new transaction.    |
| Capture an order.                                            | `POST /v2/checkout/orders/{id}/capture` | Capture the payment for an order. |

### Examples

The following code snippets illustrate how to implement cart creation and updates.

#### Cart creation with an order

Implement cart creation by creating a PayPal order and linking it to your cart.

```javascript lines expandable theme={null}
// Merchant API implementation
async function createCart(cartData) {
  const cart = await validateAndCalculateCart(cartData);

  const paypalOrder = await paypalClient.orders.create({
    intent: "CAPTURE",
    purchase_units: [
      {
        amount: {
          currency_code: cart.totals.total.currency_code,
          value: cart.totals.total.value,
          breakdown: {
            item_total: {
              currency_code: "USD",
              value: cart.totals.subtotal.value,
            },
            shipping: {
              currency_code: "USD",
              value: cart.totals.shipping.value,
            },
            tax_total: { currency_code: "USD", value: cart.totals.tax.value },
          },
        },
      },
    ],
  });

  cart.payment_method = {
    type: "PAYPAL",
    token: paypalOrder.id, // PayPal uses order_id as token
  };

  return cart;
}
```

#### Cart update with an order update

When updating a cart, patch the corresponding PayPal order with new totals.

```javascript lines expandable theme={null}
async function updateCart(cartData) {
  const cart = await validateAndUpdateCart(cartData);
  const paypal_order_id = cart.payment_method.token;

  await paypalClient.orders.patch(paypal_order_id, [
    {
      op: "replace",
      path: "/purchase_units/@reference_id=='default'/amount",
      value: {
        currency_code: cart.totals.total.currency_code,
        value: cart.totals.total.value,
        breakdown: {
          item_total: {
            currency_code: "USD",
            value: cart.totals.subtotal.value,
          },
          shipping: { currency_code: "USD", value: cart.totals.shipping.value },
          tax_total: { currency_code: "USD", value: cart.totals.tax.value },
        },
      },
    },
  ]);

  return cart;
}
```

#### Cart completed with an order captured

Finalize the purchase by capturing the PayPal order.

```javascript lines  theme={null}
async function completeCart(cartData) {
  const paypal_order_id = cartData.payment_method.token;
  await paypalClient.orders.capture(paypal_order_id);

  return cartData;
}
```

## Merchant cart response

The following examples show some successful responses that your API can return.

### Cart response for create and update cart endpoints

Return comprehensive cart details, including status, items, totals, and payment information.

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
    "token": "EC-7U8939823K567" //PayPal Order ID
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

## Resources

To use our Postman resources, you can <a href="/data/postman/agent_commerce_collection.json" download="agent_commerce_collection.json">download our Postman collection</a>. This collection includes example requests for the Cart API endpoints, which you can use as a reference when building your API.

## Next steps

Continue by [learning more about response handling](/growth/agentic-commerce/store-sync/your-api/set-up-your-api/response-handling).
