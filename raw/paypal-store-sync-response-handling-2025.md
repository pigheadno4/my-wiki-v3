<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/set-up-your-api/response-handling -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Response handling

To handle Cart API responses effectively and provide AI agents with the context they need for intelligent decision-making, understand the status fields and error patterns throughout the cart lifecycle. This guide explains how to interpret cart status indicators, handle validation issues, and implement proper error responses that enable automatic problem resolution.

> **Note:** You can view the complete protocol reference for the [Cart API](/reference/api/rest/cart-operations/create-cart/) and the [Complete Checkout API](/reference/api/rest/checkout-operations/complete-checkout/).

## Cart status fields

The PayPal Cart API uses 3 key status indicators that work together to communicate cart state and validation issues.

| Field               | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| `status`            | [Business outcome status](#business-outcome-status) (merchant-controlled) |
| `validation_status` | [Validation status](#validation-status)                                   |
| `validation_issues` | [Specific problems with type classification](#validation-issues)          |

> **Important:** Understanding these fields is crucial for proper error handling and cart lifecycle management.

### Business outcome status

The merchant-controlled `status` value indicates the current state of the cart.

| Value        | Description                                         |
| ------------ | --------------------------------------------------- |
| `CREATED`    | Cart was successfully created and is ready for use. |
| `INCOMPLETE` | Cart has issues that need resolution.               |
| `COMPLETED`  | Order is finalized, and payment was captured.       |

### Validation status

The `validation_status` value indicates whether the cart contents and data are valid for checkout. A valid transaction meets these requirements:

- All items are available with current pricing.
- Required information is complete (shipping address, customer data, and so on).
- No business rule violations exist.
- The `validation_issues` array is empty.

The following table describes the `validation-status` values.

| Value                             | Description                            |
| --------------------------------- | -------------------------------------- |
| `VALID`                           | Cart is ready for checkout.            |
| `INVALID`                         | Cart has problems that block checkout. |
| `REQUIRES_ADDITIONAL_INFORMATION` | PayPal requires more data to proceed.  |

For examples of validation status, see our [integration examples](https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/integration-use-cases/).

### Validation issues

The `validation_issues` array communicates business logic problems that prevent cart completion but don't require HTTP error codes. These structured error objects help AI agents understand what went wrong and how to fix it, whether that's suggesting alternative products for out-of-stock items, requesting missing information, or explaining pricing changes. Use these patterns to provide clear, actionable feedback that enables automatic resolution or guides customers to make informed decisions.

| Field     | Available Attributes                                                                                       |
| --------- | ---------------------------------------------------------------------------------------------------------- |
| `code`    | `INVENTORY_ISSUE`, `PRICING_ERROR`, `SHIPPING_ERROR`, `PAYMENT_ERROR`, `DATA_ERROR`, `BUSINESS_RULE_ERROR` |
| `type`    | `MISSING_FIELD`, `INVALID_DATA`, `BUSINESS_RULE`                                                           |
| `message` | `<SPECIFIC VALIDATION MESSAGE>`                                                                            |

#### Simple validation error (minimal fields)

Here's the minimum structure for a validation issue with just the required fields:

```json theme={null}
{
  "code": "INVENTORY_ISSUE",
  "type": "BUSINESS_RULE",
  "message": "Product availability issue"
}
```

#### Complete validation error (all fields)

For rich context that supports AI agents, include detailed information and resolution options.

Each `code` can map to a series of `specific_issue` values. For more details, see the [protocol reference](/reference/api/rest/cart-operations/create-cart#response-validation-issues-items-context-one-of-0-specific-issue).

```json lines expandable theme={null}
{
  "code": "INVENTORY_ISSUE",
  "type": "BUSINESS_RULE",
  "message": "Product availability issue",
  "user_message": "The Blue T-Shirt is currently out of stock. Would you like to try a different color?",
  "variant_id": "SHIRT-BLUE-M",
  "context": {
    "specific_issue": "ITEM_OUT_OF_STOCK",
    "available_quantity": 0,
    "requested_quantity": 1,
    "suggested_alternatives": ["SHIRT-RED-M", "SHIRT-GREEN-M"]
  },
  "resolution_options": [
    {
      "action": "SUGGEST_ALTERNATIVE",
      "label": "View similar colors",
      "metadata": { "priority": "high", "auto_applicable": true }
    }
  ]
}
```

To see examples of validation status, look at our [integration example page](/growth/agentic-commerce/store-sync/activate-checkout-and-fulfillment/store-sync-integration-examples).

#### Business logic issues

For business scenarios that AI agents can understand and potentially resolve, use `200 OK`:

- Cart validation issues (out of stock, price changes)
- Missing required information (shipping address, checkout fields)
- Payment processing issues (declined payments, business rules)

#### Technical issues

Use proper HTTP error codes for technical problems. For the complete list of error codes, see [HTTP status codes](#http-status-codes).

## Error handling

Effective error handling is critical for maintaining a smooth shopping experience. The API provides rich error context that enables AI agents to resolve issues automatically or guide customers to resolution.

Instead of handling dozens of specific error cases, focus on these essential patterns:

- **Can you fix this automatically?** If you can fix it, fix it for them.
- **Can the customer fix this?** If you can't fix it for them, show them how to fix it.

### Error categories

The Cart API organizes validation issues into logical categories that help AI agents understand the nature of problems and apply appropriate resolution strategies.

| Category              | Description                                                |
| --------------------- | ---------------------------------------------------------- |
| `INVENTORY_ISSUE`     | Stock, availability, back-orders, discontinued items       |
| `PRICING_ERROR`       | Price changes, discounts, tax calculation, currency issues |
| `SHIPPING_ERROR`      | Address validation, delivery restrictions, shipping zones  |
| `PAYMENT_ERROR`       | Payment limits, currency support, processor issues         |
| `DATA_ERROR`          | Field validation, format issues, required fields           |
| `BUSINESS_RULE_ERROR` | Account restrictions, compliance, regional limits          |

### Error types

Each validation issue includes a type field that classifies the underlying cause.

| Type            | Description                                        |
| --------------- | -------------------------------------------------- |
| `MISSING_FIELD` | Need more info (address, checkout fields)          |
| `INVALID_DATA`  | Data validation failed                             |
| `BUSINESS_RULE` | Business logic violation, such as inventory issues |

### Common error pattern

Most validation errors follow this structure with clear user messaging and actionable options.

```json lines theme={null}
{
  "code": "INVENTORY_ISSUE",
  "user_message": "Blue T-Shirt is out of stock. Try a different color?",
  "resolution_options": [
    {
      "action": "SUGGEST_ALTERNATIVE",
      "label": "View other colors"
    },
    {
      "action": "REMOVE_ITEM",
      "label": "Remove from cart"
    }
  ]
}
```

### Error handling implementation strategy

When implementing error handling for the PayPal Cart API, use the following guidelines to determine appropriate HTTP status codes and error responses.

#### 200 OK and validation_issues

Use `200 OK` for business logic issues that can be resolved through the `validation_issues` array. This allows AI agents to understand the problem and apply intelligent resolutions without needing to handle HTTP errors. Examples include:

- Inventory changes (out of stock, back-ordered)
- Price changes during checkout
- Payment processing issues that can be resolved
- Geographic restrictions
- Discount validation failures
- Customer account issues
- Address validation problems

#### 422 Unprocessable entity

Use this error code when any `validation_issue` prevents you from creating a cart. For example, if you do not create a cart for an `OUT_OF_STOCK` issue, you can send a `422 Unprocessable Entity` error with details about the error in the body.

#### 400 Bad request

Use this error code for malformed requests when client-side issues prevent processing. For example:

- Invalid JSON format
- Missing required fields (for example, the `items` array)
- Invalid field types or formats
- Malformed request structure
- Invalid cart ID format (for example, it doesn't match an expected pattern, such as `"CART-[A-Z0-9]+"`)

#### 404 not found

Use this error code when a well-formed request references a resource that doesn't exist. For example:

- **Cart ID doesn't exist in merchant's system** (well-formed ID, but not found)
- Invalid endpoint paths

#### Cart retrieval error handling

These examples use `GET /merchant-cart/{cartId}`.

**Example: Invalid cart ID format (400 response)**

When the cart ID doesn't match your expected format, return detailed validation information.

```json lines theme={null}
{
  "name": "INVALID_CART_ID",
  "message": "Cart ID format is invalid. Expected format: CART-[A-Z0-9]+",
  "debug_id": "ERROR-400-CART-FORMAT",
  "details": [
    {
      "field": "cartId",
      "issue": "INVALID_FORMAT",
      "description": "Cart ID format is invalid. Expected format: CART-[A-Z0-9]+. Provided: invalid-cart-id-123"
    }
  ]
}
```

**Example: Cart not found (404 response)**

When a well-formed cart ID doesn't exist in your system, provide clear guidance.

```json lines theme={null}
{
  "name": "CART_NOT_FOUND",
  "message": "Cart with ID 'CART-MISSING-123' does not exist",
  "debug_id": "ERROR-404-12345",
  "details": [
    {
      "field": "cartId",
      "issue": "NOT_FOUND",
      "description": "Cart with ID 'CART-MISSING-123' does not exist for merchant 'MERCHANT_789'. Verify cart ID or create a new cart."
    }
  ]
}
```

#### 500 internal server error

Use this error code for unexpected server-side issues that prevent processing. For example:

- System failures
- Database connectivity issues
- Payment processor unavailable
- Unexpected server errors

#### Error context best practices

When designing error responses, follow these practices to create actionable error messages that enable intelligent resolution.

- **Provide rich context**: Include all relevant information for smart resolution.
- **Customer-friendly messages**: Write user_message for end customers.
- **Technical details**: Include technical message for developers.
- **Resolution guidance**: Always provide actionable next steps.
- **Cost impact**: Show financial implications of resolution options.
- **Time estimates**: Provide realistic timeframes for resolutions.

#### AI agent considerations for errors

Many errors are well-suited for AI agents to handle autonomously. For example:

- **Auto-applicable actions**: AI can resolve these without human intervention.
- **Priority guidance**: Immediate action is required.
- **Context-rich**: The system has enough information for intelligent decision-making.
- **Resolution metadata**: The system helps AI choose the best resolution.

#### Resolution action types

The Cart API supports various resolution actions that AI agents can use to automatically resolve validation issues. Each action type indicates whether it can be applied automatically (without customer intervention).

| Action                | Use Case               | Auto-applicable                |
| --------------------- | ---------------------- | ------------------------------ |
| `ACCEPT_NEW_PRICE`    | Price increases        | No                             |
| `ACCEPT_BACK_ORDER`   | Inventory delays       | Depends on customer preference |
| `SUGGEST_ALTERNATIVE` | Out of stock items     | Yes                            |
| `UPDATE_ADDRESS`      | Address validation     | Yes (if correction available)  |
| `REMOVE_ITEM`         | Restriction violations | Depends on item importance     |
| `SPLIT_ORDER`         | Payment limits         | Yes                            |
| `CONTACT_SUPPORT`     | Complex issues         | No                             |
| `RETRY_LATER`         | Temporary failures     | Yes                            |

## Next steps

Continue by [looking at integration examples](/growth/agentic-commerce/store-sync/your-api/integration-use-cases).
