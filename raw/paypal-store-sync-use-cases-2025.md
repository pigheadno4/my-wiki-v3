<!-- Source URL: https://docs.paypal.ai/growth/agentic-commerce/store-sync/your-api/integration-use-cases -->
<!-- Fetched: 2026-04-18 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Integration use cases

To handle real-world shopping scenarios that AI agents encounter, implement robust error handling patterns that provide clear context and actionable resolution options. This guide shows you how to structure validation responses for common integration challenges including inventory issues, pricing changes, shipping restrictions, geographic limitations, and system maintenance scenarios.

> **Note:** You can view the complete protocol reference for the [Cart API](/reference/api/rest/cart-operations/create-cart/) and the [Complete Checkout API](/reference/api/rest/checkout-operations/complete-checkout/).

### Inventory and stock management errors

Inventory issues are among the most common errors in e-commerce. These examples show how to handle out-of-stock scenarios, back-orders, and discontinued products gracefully.

#### Out of stock with alternatives

When a requested item is out of stock, provide alternative products and clear communication about availability.

```json lines expandable theme={null}
{
  "code": "INVENTORY_ISSUE",
  "type": "BUSINESS_RULE",
  "message": "Product is no longer available",
  "user_message": "The Blue T-Shirt is temporarily out of stock. Would you like to try a different color?",
  "variant_id": "SHIRT-BLUE-M",
  "context": {
    "specific_issue": "ITEM_OUT_OF_STOCK",
    "available_quantity": 0,
    "requested_quantity": 1,
    "suggested_alternatives": ["SHIRT-RED-M", "SHIRT-GREEN-M"],
    "restock_date": "2024-07-20T00:00:00Z"
  },
  "resolution_options": [
    {
      "action": "SUGGEST_ALTERNATIVE",
      "label": "View similar colors",
      "metadata": {
        "priority": "high",
        "auto_applicable": true
      }
    },
    {
      "action": "WAIT_FOR_RESTOCK",
      "label": "Notify when back in stock",
      "metadata": {
        "estimated_time": "5-7 days",
        "priority": "medium"
      }
    },
    {
      "action": "REMOVE_ITEM",
      "label": "Remove from cart",
      "metadata": {
        "priority": "low"
      }
    }
  ]
}
```

#### Back-order scenario

For items that can be back-ordered, communicate delivery delays and allow customers to decide.

```json lines expandable theme={null}
{
  "code": "INVENTORY_ISSUE",
  "type": "BUSINESS_RULE",
  "message": "Item is currently back-ordered",
  "user_message": "This item will ship in 2-3 weeks. Would you like to proceed with your order?",
  "variant_id": "LAPTOP-PRO-15",
  "context": {
    "available_quantity": 0,
    "back_order_limit": 50,
    "estimated_ship_date": "2024-08-15T00:00:00Z",
    "current_back_orders": 23
  },
  "resolution_options": [
    {
      "action": "ACCEPT_BACK_ORDER",
      "label": "Order anyway (ships August 15th)",
      "metadata": {
        "estimated_time": "2-3 weeks",
        "priority": "high",
        "cost_impact": "$0.00"
      }
    },
    {
      "action": "SUGGEST_ALTERNATIVE",
      "label": "View similar laptops in stock",
      "metadata": {
        "priority": "medium",
        "auto_applicable": true
      }
    }
  ]
}
```

#### Discontinued product

When a product is no longer available, guide customers to newer or similar alternatives.

```json lines expandable theme={null}
{
  "code": "INVENTORY_ISSUE",
  "type": "BUSINESS_RULE",
  "message": "Product has been discontinued",
  "user_message": "This product is no longer available. Here are some similar alternatives.",
  "variant_id": "PRODUCT-OLD-MODEL",
  "context": {
    "discontinuation_date": "2024-02-01T00:00:00Z",
    "suggested_alternatives": ["PRODUCT-NEW-MODEL", "PRODUCT-SIMILAR"],
    "upgrade_available": true
  },
  "resolution_options": [
    {
      "action": "SUGGEST_ALTERNATIVE",
      "label": "View newer model (+$50)",
      "metadata": {
        "cost_impact": "+$50.00",
        "priority": "high"
      }
    },
    {
      "action": "REMOVE_ITEM",
      "label": "Remove from cart",
      "metadata": {
        "priority": "low"
      }
    }
  ]
}
```

### Pricing and financial errors

Price changes can occur between cart creation and checkout. These error patterns help you handle pricing discrepancies transparently while maintaining customer trust.

#### Price change during checkout

Handle price increases that occur between cart creation and checkout with transparency.

```json lines expandable theme={null}
{
  "code": "PRICING_ERROR",
  "type": "BUSINESS_RULE",
  "message": "Product price has changed since cart creation",
  "user_message": "The price for Ocean Blue T-Shirt has increased from $29.99 to $34.99. Continue with new price?",
  "variant_id": "SHIRT-OCEAN-BLUE",
  "context": {
    "original_price": "29.99",
    "current_price": "34.99",
    "currency_code": "USD",
    "price_change_reason": "promotional_ended",
    "price_increase": "5.00"
  },
  "resolution_options": [
    {
      "action": "ACCEPT_NEW_PRICE",
      "label": "Continue with $34.99",
      "metadata": {
        "cost_impact": "+$5.00",
        "priority": "high",
        "auto_applicable": false
      }
    },
    {
      "action": "REMOVE_ITEM",
      "label": "Remove from cart",
      "metadata": {
        "cost_impact": "-$29.99",
        "priority": "medium"
      }
    }
  ]
}
```

### Shipping and address errors

Address validation ensures successful delivery while preventing fraud. These examples demonstrate handling invalid addresses, PO box restrictions, and shipping limitations.

#### Invalid shipping address

When address validation fails, provide specific corrections to help customers fix the issue.

```json lines expandable theme={null}
{
  "code": "SHIPPING_ERROR",
  "type": "INVALID_DATA",
  "message": "Shipping address validation failed",
  "user_message": "The shipping address appears to be incomplete or invalid. Please check and correct.",
  "field": "shipping_address",
  "context": {
    "validation_failures": ["invalid_postal_code", "missing_street_number"],
    "suggested_corrections": {
      "postal_code": "90210",
      "address_line_1": "123 Main Street"
    },
    "address_quality_score": 0.3
  },
  "resolution_options": [
    {
      "action": "UPDATE_ADDRESS",
      "label": "Use suggested corrections",
      "metadata": {
        "priority": "high",
        "auto_applicable": true
      }
    },
    {
      "action": "PROVIDE_MISSING_FIELD",
      "label": "Add street number",
      "metadata": {
        "priority": "medium"
      }
    }
  ]
}
```

#### PO box restrictions

For this example, items that require signature delivery cannot be sent to a PO box. Explain why PO box delivery isn't available for those items.

```json theme={null}
{
  "code": "SHIPPING_ERROR",
  "type": "BUSINESS_RULE",
  "message": "PO box delivery not available for this order",
  "user_message": "This order contains items requiring signature confirmation and cannot be delivered to a PO box.",
  "field": "shipping_address",
  "context": {
    "restricted_items": ["ELECTRONICS-LAPTOP-001"],
    "restriction_reason": "signature_required",
    "po_box_detected": true
  },
  "resolution_options": [
    {
      "action": "UPDATE_ADDRESS",
      "label": "Use street address instead",
      "metadata": {
        "priority": "high"
      }
    },
    {
      "action": "REMOVE_ITEM",
      "label": "Remove items requiring signature",
      "metadata": {
        "cost_impact": "-$899.00",
        "priority": "low"
      }
    }
  ]
}
```

### Geographic and legal restrictions

Some products or merchants have regional restrictions due to regulations or business policies. These errors help communicate limitations clearly to customers.

#### Regional sales restrictions

Communicate geographic limitations due to business policies or regulatory compliance.

```json lines expandable theme={null}
{
  "code": "BUSINESS_RULE_ERROR",
  "type": "BUSINESS_RULE",
  "message": "Store does not sell to this region",
  "user_message": "Unfortunately, we don't ship to your location due to regulatory restrictions. Please check our shipping policy.",
  "context": {
    "restricted_region": "EU",
    "customer_country": "DE",
    "restriction_reason": "regulatory_compliance",
    "supported_countries": ["US", "CA", "GB"],
    "policy_url": "https://merchant.com/shipping-policy"
  },
  "resolution_options": [
    {
      "action": "CONTACT_SUPPORT",
      "label": "Contact support for alternatives",
      "url": "https://merchant.com/support",
      "metadata": {
        "priority": "medium"
      }
    }
  ]
}
```

### System and store errors

Temporary system issues require special handling to maintain customer relationships. These patterns show how to communicate maintenance windows and system unavailability.

#### Store maintenance mode

During scheduled maintenance, provide clear timing for when services will resume.

```json lines expandable theme={null}
{
  "code": "BUSINESS_RULE_ERROR",
  "type": "BUSINESS_RULE",
  "message": "Store is currently in maintenance mode",
  "user_message": "The store is temporarily closed for maintenance. Please try again later.",
  "context": {
    "maintenance_end_time": "2024-06-25T09:00:00Z",
    "service_status": "maintenance",
    "reason": "system_upgrade",
    "retry_after": 7200
  },
  "resolution_options": [
    {
      "action": "RETRY_LATER",
      "label": "Try again at 9:00 AM",
      "metadata": {
        "estimated_time": "2 hours",
        "priority": "high"
      }
    }
  ]
}
```
