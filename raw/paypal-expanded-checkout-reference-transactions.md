<!-- Source URL: https://developer.paypal.com/docs/checkout/advanced/customize/reference-transactions/ -->
<!-- Fetched: 2026-04-13 -->

---
title: Initiate future transactions
slug: /docs/checkout/advanced/customize/reference-transactions/
createTime: '2025-02-24T07:02:32.453Z'
updateTime: '2025-08-11T08:40:05.549Z'
---


# Initiate future transactions

Website Payments Pro merchants can initiate future transactions using a transaction ID.

**Important:** Reference transactions are available only to Website Payments Pro merchants who use Expanded Checkout.



## How it works 
Website Payments Pro merchants can initiate future transactions using a transaction ID.

Use your payer's original transaction ID to charge them later with reference transactions. A reference transaction is a transaction that you initiate through an established contract with the payer and from which you can derive subsequent payments.

You need a reference transaction to start a future transaction using the same payment method. Get the following information:

- A previous order ID.
- The payment amount.
- The payer's original transaction ID.

Process:
- The payer generates a transaction ID when they purchase an item on your site.
- The payer agrees to a reference transaction.
- Use the transaction ID in future reference transactions using the same payment method.

Use cases:
- Save payer's card details for a future payer-initiated transaction.
- Initiate transactions to charge the payment method based on a previously-agreed contract.



## Know before you code 

To complete this server-side integration, you will need:

- An Expanded Checkout integration.
- The Orders v2 REST API: Create, update, retrieve, authorize, and capture orders.

NVP and SOAP integrations: You can get reference transactions from an existing NVP or SOAP integration of the DoReferenceTransaction API.


### Step 1: Create order

Provide an order ID from a previous transaction or create a new one.

API endpoint used: Create order

```bash
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer Access-Token" \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      }
    }
  ]
}'
```

Step result:
- HTTP 201 Created
- JSON response with order ID (e.g. `5O190127TN364715T`)

Sample response:
```json
{
  "id": "5O190127TN364715T",
  "status": "CREATED",
  "links": [
    { "href": "...", "rel": "self", "method": "GET" },
    { "href": "...", "rel": "approve", "method": "GET" },
    { "href": "...", "rel": "update", "method": "PATCH" },
    { "href": "...", "rel": "capture", "method": "POST" }
  ]
}
```


### Step 2: Authorize payment using previous transaction ID

API endpoint used: Authorize payment for order

#### Using PayPal transaction ID
```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer Access-Token' \
 -H 'Accept-Language: en_US' \
 -d '{
     "payment_source": {
       "token": {
         "id": "67N9717781765035V",
         "type": "PAYPAL_TRANSACTION_ID"
       }
     }
   }'
```

#### Using PNREF (Payflow legacy token)
```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/authorize \
 -H 'Content-Type: application/json' \
 -H 'Authorization: Bearer Access-Token' \
 -H 'Accept-Language: en_US' \
 -d '{
     "payment_source": {
       "token": {
         "id": "67N9717781765035V",
         "type": "PNREF"
       }
     }
   }'
```

Step result:
- HTTP 201 Created
- JSON response with order ID and status COMPLETED


### Step 3: Capture payment using previous transaction ID

API endpoint used: Capture payment for order

#### Using PayPal transaction ID
```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Request-ID: 7b92603e-77ed-4896-8e78-5dea2050476a' \
 -H 'Authorization: Bearer Access-Token' \
 -H 'Accept-Language: en_US' \
 -d '{
   "payment_source": {
      "token": {
        "id": "67N9717781765035V",
        "type": "PAYPAL_TRANSACTION_ID"
      }
   }
 }'
```

#### Using PNREF
```bash
curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/5O190127TN364715T/capture \
 -H 'Content-Type: application/json' \
 -H 'PayPal-Request-ID: 7b92603e-77ed-4896-8e78-5dea2050476a' \
 -H 'Authorization: Bearer Access-Token' \
 -H 'Accept-Language: en_US' \
 -d '{
   "payment_source": {
      "token": {
        "id": "67N9717781765035V",
        "type": "PNREF"
      }
   }
 }'
```

Step result:
- HTTP 201 Created
- JSON response with order ID and status COMPLETED

Note: `PayPal-Request-ID` prevents duplicate captures if the API call is disrupted (idempotency key).
