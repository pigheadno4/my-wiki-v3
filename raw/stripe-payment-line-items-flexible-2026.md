<!-- Source URL: https://docs.stripe.com/payments/payment-line-items/flexible-payment-scenarios -->
<!-- Fetched: 2026-05-11 -->

# Use payment line items for flexible payments

Learn how to use payment line items with complex payments, such as multicapture and overcapture payments.

You can use payment line items for [complex payments](https://docs.stripe.com/payments/flexible-payments.md), such as multicapture and overcapture payments.

## Multicapture

You can use payment line items during multicaptures.

> Multicapture isn’t supported for Klarna or PayPal.

#### Create and confirm an uncaptured PaymentIntent

> The API response doesn’t include line items by default. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`.

Specify the `capture_method` as `manual` when creating the PaymentIntent and use the `if_available` parameter to request multicapture for this payment. The created PaymentIntent allows multiple captures if the payment method supports it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4600,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_method_options: {
    card: {
      request_multicapture: "if_available",
    },
  },
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 200,
    tax: {
      total_tax_amount: 400,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 400,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  confirm: true,
  capture_method: "manual",
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items specified on the PaymentIntent.

```json
{
  "amount": 4600,
  "amount_capturable": 4600,
  "amount_received": 0,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 400
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 400
    },
    "line_items": [
      {
        "product_code": "SKU001",
        "product_name": "Product 001",
        "unit_cost": 2000,
        "quantity": 1,
        "unit_of_measure": "feet",
        "payment_method_options": {
          "card": {
            "commodity_code": "123123"
          }
        }
      },
      {
        "product_code": "SKU002",
        "product_name": "Product 002",
        "unit_cost": 2000,
        "quantity": 1,
        "unit_of_measure": "gallons",
        "payment_method_options": {
          "card": {
            "commodity_code": "123123"
          }
        }
      }
    ]
  }
  ...
}
```

#### Capture the PaymentIntent

- You can add `amount_details` on the first capture even if they weren’t specified at creation.
- If you provided `amount_details` at creation, you must either pass in `amount_details` or unset them on the first capture.

The same rules apply to `amount_details[line_items]`—you can add them on the first capture if not specified at creation, but must include or explicitly unset them if they were present at creation.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxxxxxxx", {
  amount_to_capture: 2300,
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 100,
    tax: {
      total_tax_amount: 200,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 200,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  final_capture: false,
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items specified on the first capture.

```json
{
  "amount": 4600,
  "amount_capturable": 2300,
  "amount_received": 2300,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 100,
    "tax": {
      "total_tax_amount": 200
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 200
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_123",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "requires_capture"
  ...
}
```

The PaymentIntent remains in a `requires_capture` state. At this point, you can either:

- Continue to capture the PaymentIntent multiple times up to the full amount of the PaymentIntent.
- Transition the PaymentIntent to a `succeeded` state by setting `final_capture` to `true`, or making a capture without the `final_capture` parameter (because `final_capture` defaults to `true`).

#### Capture the PaymentIntent again

- If previous captures included `amount_details` or `amount_details[line_items]`, you must continue to include them in subsequent captures.
- If previous captures didn’t include these fields, you can’t add them in later captures.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxxxxxxx", {
  amount_to_capture: 2300,
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 100,
    tax: {
      total_tax_amount: 200,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 200,
    },
    line_items: [
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  final_capture: false,
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items from the first two captures, according to the following rules:

- `discount_amount`, `tax.total_tax_amount` and `shipping.amount` are summed across captures.
- `shipping.from_postal_code` and `shipping.to_postal_code` might be omitted in the captures, but if it’s provided, you must not change it across captures.
- `line_items` will be aggregated across captures.

```json
{
  "amount": 4600,
  "amount_capturable": 0,
  "amount_received": 4600,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 400
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 400
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_123",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_234",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "succeeded"
  ...
}
```

#### Partially capture the PaymentIntent

Pass `amount_to_capture` with `0` and `final_capture` with `true` to transition the partially captured PaymentIntent to a `succeeded` state.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxxxxxxx", {
  amount_to_capture: 0,
  final_capture: true,
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field only contains the line items specified on the first capture.

```json
{
  "amount": 4600,
  "amount_capturable": 2300,
  "amount_received": 2300,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 100,
    "tax": {
      "total_tax_amount": 200
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 200
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_123",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "succeeded"
  ...
}
```

## Overcapture

You can use payment line items during overcaptures.

#### Create and confirm an uncaptured PaymentIntent

> The API response doesn’t include line items by default. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`.

Specify the `capture_method` as `manual` when creating the PaymentIntent and use the `if_available` parameter to request overcapture for this payment. The created PaymentIntent allows overcapture if the payment method supports it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4600,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_method_options: {
    card: {
      request_overcapture: "if_available",
    },
  },
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 200,
    tax: {
      total_tax_amount: 400,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 400,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  confirm: true,
  capture_method: "manual",
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items specified on the PaymentIntent.

```json
{
  "amount": 4600,
  "amount_capturable": 4600,
  "amount_received": 0,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 400
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 400
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_345",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_456",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  }
  ...
}
```

#### Capture the PaymentIntent

To capture more than the currently authorized amount on a PaymentIntent, use the [capture](https://docs.stripe.com/api/payment_intents/capture.md) endpoint and provide an [amount_to_capture](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_to_capture) up to the [maximum_amount_capturable](https://docs.stripe.com/api/charges/object.md#charge_object-payment_method_details-card-overcapture).

Pass in an updated `amount_details` hash that is consistent with the capture amount during Capture.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture("pi_xxxxxxxx", {
  amount_to_capture: 5000,
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 200,
    tax: {
      total_tax_amount: 600,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 600,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items specified during capture.

```json
{
  "amount": 5000,
  "amount_capturable": 0,
  "amount_received": 5000,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 600
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 600
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_567",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_678",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "succeeded"
  ...
}
```

## Incremental authorization

You can use payment line items during incremental authorization to authorize additional amounts on a PaymentIntent after the initial authorization.

#### Create and confirm an uncaptured PaymentIntent

> The API response doesn’t include line items by default. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`.

Specify the `capture_method` as `manual` when creating the PaymentIntent and use the `if_available` parameter to request incremental authorization for this payment. The created PaymentIntent allows incremental authorization if the payment method supports it.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 4600,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_method_options: {
    card: {
      request_incremental_authorization: "if_available",
    },
  },
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    discount_amount: 200,
    tax: {
      total_tax_amount: 400,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 400,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  confirm: true,
  capture_method: "manual",
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items specified on the PaymentIntent.

```json
{
  "amount": 4600,
  "amount_capturable": 4600,
  "amount_received": 0,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 400
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 400
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_789",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_890",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  }
  ...
}
```

#### Increment the authorization

To authorize additional amounts on a PaymentIntent beyond the initially authorized amount, use the [increment_authorization](https://docs.stripe.com/api/payment_intents/increment_authorization.md) endpoint and provide an [amount](https://docs.stripe.com/api/payment_intents/increment_authorization.md#increment_authorization-amount) up to the maximum incremental authorization amount supported by the payment method.

Pass in an updated `amount_details` hash that is consistent with the total authorized amount after the increment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.incrementAuthorization(
  "pi_xxxxxxxx",
  {
    amount: 5000,
    payment_details: {
      customer_reference: "customer_reference",
      order_reference: "order_reference",
    },
    amount_details: {
      discount_amount: 200,
      tax: {
        total_tax_amount: 600,
      },
      shipping: {
        from_postal_code: "94110",
        to_postal_code: "94117",
        amount: 600,
      },
      line_items: [
        {
          product_code: "SKU001",
          product_name: "Product 001",
          unit_cost: 2000,
          quantity: 1,
          unit_of_measure: "feet",
          payment_method_options: {
            card: {
              commodity_code: "123123",
            },
          },
        },
        {
          product_code: "SKU002",
          product_name: "Product 002",
          unit_cost: 2000,
          quantity: 1,
          unit_of_measure: "gallons",
          payment_method_options: {
            card: {
              commodity_code: "123123",
            },
          },
        },
      ],
    },
    expand: ["amount_details.line_items"],
  },
);
```

In the response, the `amount_details` field contains the line items specified during the increment authorization, and the PaymentIntent’s total authorized amount is updated.

```json
{
  "amount": 5000,
  "amount_capturable": 5000,
  "amount_received": 0,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 600
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 600
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_901",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_012",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "requires_capture"
  ...
}
```

## Partial authorization

You can use payment line items with partial authorizations.

### Create and confirm an uncaptured PaymentIntent

> The API response doesn’t include line items by default. To return line items, [expand](https://docs.stripe.com/expand.md#includable-properties) `amount_details.line_items`.

Specify the `capture_method` as `manual` when creating the `PaymentIntent` and use the `if_available` parameter to request partial authorization for this payment.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_debit_partialAuthorization",
  payment_method_options: {
    card: {
      request_partial_authorization: "if_available",
    },
  },
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    tax: {
      total_tax_amount: 100,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 100,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 800,
        quantity: 1,
        unit_of_measure: "feet",
      },
    ],
  },
  confirm: true,
  capture_method: "manual",
  expand: ["amount_details.line_items"],
});
```

If you provided line item data before the partial authorization, the sum of the line item amounts might not match the total amount on the `PaymentIntent`. In that case, the [amount_details.error](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-amount_details-error) hash in the response has a `code` of `amount_details_amount_mismatch` and includes the mismatch amount in the `message` property.

The example response below shows the transaction being partially authorized for 7 USD, which is less than the originally requested 10 USD.

```json
{
  "id": "pi_3SpkXE2QCQbYXizB1WscY8lW",
  "object": "payment_intent",
  "amount": 700,
  "amount_capturable": 700,
  "amount_details": {
    "error": {
      "code": "amount_details_amount_mismatch",
      "message": "Invalid amount_details. The calculated amount is Sum(line_items[#].unit_cost * line_items[#].quantity + line_items[#].tax.total_tax_amount - line_items[#].discount_amount) + shipping.amount or Sum(line_items[#].unit_cost * line_items[#].quantity) + tax.total_tax_amount + shipping.amount - discount_amount which does not match the total amount charged. In this case the calculated amount 1000 is not equal to the total amount 700 on the PaymentIntent."
    },
    "line_items": {
      "object": "list",
      "data": [
        {
          "id": "uli_TnLDKPQgGwfFxD",
          "object": "payment_intent_amount_details_line_item",
          "discount_amount": null,
          "payment_method_options": null,
          "product_code": "SKU001",
          "product_name": "Product 001",
          "quantity": 1,
          "tax": null,
          "unit_cost": 800,
          "unit_of_measure": "feet"
        }
      ],
      "has_more": false,
      "url": "/v1/payment_intents/pi_3SpkXE2QCQbYXizB1WscY8lW/amount_details_line_items"
    },
    "shipping": {
      "amount": 100,
      "from_postal_code": "94110",
      "to_postal_code": "94117"
    },
    "tax": {
      "total_tax_amount": 100
    },
    "tip": {}
  },
  "status": "requires_capture"
}
```

### Capture the PaymentIntent

#### Capture the PaymentIntent with updated line items

[Capture](https://docs.stripe.com/api/payment_intents/capture.md) the `PaymentIntent` and pass an updated [amount_details](https://docs.stripe.com/api/payment_intents/capture.md#capture_payment_intent-amount_details) that matches the partially authorized amount.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_3SpkXE2QCQbYXizB1WscY8lW",
  {
    amount_details: {
      line_items: [
        {
          product_code: "SKU002",
          product_name: "Product 002",
          unit_cost: 500,
          quantity: 1,
          unit_of_measure: "feet",
        },
      ],
    },
    expand: ["amount_details.line_items"],
  },
);
```

Updating `amount_details` removes the mismatch `error` hash from the `PaymentIntent`. For card payments, that allows Stripe to send the line item data to card networks.

```json
{
  "id": "pi_3SpkXE2QCQbYXizB1WscY8lW",
  "object": "payment_intent",
  "amount": 700,
  "amount_capturable": 0,
  "amount_details": {
    "line_items": {
      "object": "list",
      "data": [
        {
          "id": "uli_TnM6fcFHBk7BMk",
          "object": "payment_intent_amount_details_line_item",
          "discount_amount": null,
          "payment_method_options": null,
          "product_code": "SKU002",
          "product_name": "Product 002",
          "quantity": 1,
          "tax": null,
          "unit_cost": 500,
          "unit_of_measure": "feet"
        }
      ],
      "has_more": false,
      "url": "/v1/payment_intents/pi_3SplOI2QCQbYXizB0DaGWmQT/amount_details_line_items"
    },
    "shipping": {
      "amount": 100,
      "from_postal_code": "94110",
      "to_postal_code": "94117"
    },
    "tax": {
      "total_tax_amount": 100
    },
    "tip": {}
  },
  "amount_received": 700,
  "status": "succeeded"
}
```

#### Capture the PaymentIntent without updating line items

[Capture](https://docs.stripe.com/api/payment_intents/capture.md) the `PaymentIntent` without updating the `amount_details`.

For card payments, Stripe doesn’t send mismatched line item data to card networks. That prevents the transaction from qualifying for L2/L3 interchange savings.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.capture(
  "pi_3SpkXE2QCQbYXizB1WscY8lW",
  {
    expand: ["amount_details.line_items"],
  },
);
```

```json
{
  "id": "pi_3SpkXE2QCQbYXizB1WscY8lW",
  "object": "payment_intent",
  "amount": 700,
  "amount_capturable": 0,
  "amount_details": {
    "error": {
      "code": "amount_details_amount_mismatch",
      "message": "Invalid amount_details. The calculated amount is Sum(line_items[#].unit_cost * line_items[#].quantity + line_items[#].tax.total_tax_amount - line_items[#].discount_amount) + shipping.amount or Sum(line_items[#].unit_cost * line_items[#].quantity) + tax.total_tax_amount + shipping.amount - discount_amount which does not match the total amount charged. In this case the calculated amount 1000 is not equal to the total amount 700 on the PaymentIntent."
    },
    "line_items": {
      "object": "list",
      "data": [
        {
          "id": "uli_TnLDKPQgGwfFxD",
          "object": "payment_intent_amount_details_line_item",
          "discount_amount": null,
          "payment_method_options": null,
          "product_code": "SKU001",
          "product_name": "Product 001",
          "quantity": 1,
          "tax": null,
          "unit_cost": 800,
          "unit_of_measure": "feet"
        }
      ],
      "has_more": false,
      "url": "/v1/payment_intents/pi_3SpkXE2QCQbYXizB1WscY8lW/amount_details_line_items"
    },
    "shipping": {
      "amount": 100,
      "from_postal_code": "94110",
      "to_postal_code": "94117"
    },
    "tax": {
      "total_tax_amount": 100
    },
    "tip": {}
  },
  "amount_received": 700,
  "status": "succeeded"
}
```

## Add a surcharge

You can use payment line items with [surcharges](https://docs.stripe.com/payments/cards/surcharge.md).

### Create and confirm a PaymentIntent

When you create a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-payment_method), make sure to follow the [standard flow for surcharging](https://docs.stripe.com/payments/collect-surcharges.md). Specify the total `amount` inclusive of the surcharge and pass the surcharge amount in `amount_details[surcharge][amount]`. Don’t create a separate line item for the surcharge.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5003,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    surcharge: {
      amount: 3,
    },
    discount_amount: 200,
    tax: {
      total_tax_amount: 600,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 600,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
    ],
  },
  capture_method: "manual",
  confirm: true,
  expand: ["amount_details.line_items"],
});
```

In the response, the `amount_details` field contains the line items that you specified on the PaymentIntent.

```json
{
  "amount": 5003,
  "amount_capturable": 5003,
  "amount_received": 0,
  "payment_details": {
    "customer_reference": "customer_reference",
    "order_reference": "order_reference"
  },
  "amount_details": {
    "surcharge": {
      "amount": 3
    },
    "discount_amount": 200,
    "tax": {
      "total_tax_amount": 600
    },
    "shipping": {
      "from_postal_code": "94110",
      "to_postal_code": "94117",
      "amount": 600
    },
    "line_items": {
      "object": "list",
      "url": "/v1/payment_intents/pi_xxxxxxxx/amount_details_line_items",
      "has_more": false,
      "data": [
        {
          "_id": "li_789",
          "product_code": "SKU001",
          "product_name": "Product 001",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "feet",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        },
        {
          "_id": "li_890",
          "product_code": "SKU002",
          "product_name": "Product 002",
          "unit_cost": 2000,
          "quantity": 1,
          "unit_of_measure": "gallons",
          "payment_method_options": {
            "card": {
              "commodity_code": "123123"
            }
          }
        }
      ]
    }
  },
  "status": "requires_capture"
  ...
}
```

### Example of an incorrect implementation

The following example shows what happens if you add a surcharge line item in addition to specifying `amount_details[surcharge][amount]` when creating the PaymentIntent. In this example, the line items won’t correctly add up to the amount exclusive of the surcharge amount, and the request will 400.

```node
// Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
// Find your keys at https://dashboard.stripe.com/apikeys.
// This example uses the public preview SDK. See https://github.com/stripe/stripe-node#public-preview-sdks
const stripe = require("stripe")("<<YOUR_SECRET_KEY>>");

const paymentIntent = await stripe.paymentIntents.create({
  amount: 5003,
  currency: "usd",
  payment_method_types: ["card"],
  payment_method: "pm_card_visa",
  payment_details: {
    customer_reference: "customer_reference",
    order_reference: "order_reference",
  },
  amount_details: {
    surcharge: {
      amount: 3,
    },
    discount_amount: 200,
    tax: {
      total_tax_amount: 600,
    },
    shipping: {
      from_postal_code: "94110",
      to_postal_code: "94117",
      amount: 600,
    },
    line_items: [
      {
        product_code: "SKU001",
        product_name: "Product 001",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "feet",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "SKU002",
        product_name: "Product 002",
        unit_cost: 2000,
        quantity: 1,
        unit_of_measure: "gallons",
        payment_method_options: {
          card: {
            commodity_code: "123123",
          },
        },
      },
      {
        product_code: "surcharge",
        product_name: "surcharge",
        unit_cost: 3,
        quantity: 1,
      },
    ],
  },
  capture_method: "manual",
  expand: ["amount_details.line_items"],
});
```

```json
{
  "error": {
    "message": "The total value of `amount_details` (5003) does not match the `amount` (5000). Make sure that the total value of `line_items` matches the amount to charge, taking into account any discounts, tax, and shipping. See https://docs.stripe.com/payments/payment-line-items",
    "param": "amount_details",
    "request_log_url": "https://dashboard.stripe.com/acct_1PXoBsF71U5YydpB/test/workbench/logs?object=req_OFmFBVHdRVDIIP",
    "type": "invalid_request_error"
  }
}
```
