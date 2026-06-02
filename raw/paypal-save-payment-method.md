<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/save -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Save PayPal information for future payments

Charge a customer's saved PayPal account without requiring the customer to approve each payment. Common scenarios include:

- Subscription renewals
- On-demand services billed after usage
- Automatic bill payments
- One-click purchases for returning customers

Use PayPal's vault parameter to save the customer's PayPal information. The customer approves once. Then you can charge their PayPal account without them present.

## Prerequisites

- Complete [the quick start PayPal integration](/payments/methods/paypal/integrate).
- Have a secure database to store payment tokens.
- Build a mechanism to collect customer consent.

## Integrate server side

<Info>
  Endpoint: [`POST /v2/checkout/orders`](/reference/api/rest/orders/)
</Info>

<CodeGroup>
  ```bash cURL expandable lines theme={null}
  # Step 1: Create order with vault=true
  curl -X POST https://api-m.paypal.com/v2/checkout/orders \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{
      "intent": "CAPTURE",
      "payment_source": {
        "paypal": {
          "experience_context": {
            "return_url": "https://example.com/return",
            "cancel_url": "https://example.com/cancel"
          },
          "attributes": {
            "vault": {
              "store_in_vault": "ON_SUCCESS",
              "usage_type": "MERCHANT",
              "customer_type": "CONSUMER"
            }
          }
        }
      },
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": "10.00"
        }
      }]
    }'

# Step 2: After customer approval, capture the order

curl -X POST https://api-m.paypal.com/v2/checkout/orders/{order_id}/capture \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN"

# Extract payment token from response:

# capture.payment_source.paypal.attributes.vault.id

# Step 3: Later, charge using saved token

curl -X POST https://api-m.paypal.com/v2/checkout/orders \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN" \
 -d '{
"intent": "CAPTURE",
"payment_source": {
"token": {
"id": "PAYMENT_TOKEN_ID",
"type": "PAYMENT_METHOD_TOKEN"
}
},
"purchase_units": [{
"amount": {
"currency_code": "USD",
"value": "29.99"
}
}]
}'

````

```javascript Node.js expandable lines theme={null}
const paypal = require('@paypal/checkout-server-sdk');

// Step 1: Create order with vault=true
async function createVaultOrder() {
  const request = new paypal.orders.OrdersCreateRequest();
  request.prefer("return=representation");
  request.requestBody({
    intent: 'CAPTURE',
    payment_source: {
      paypal: {
        experience_context: {
          return_url: 'https://example.com/return',
          cancel_url: 'https://example.com/cancel'
        },
        attributes: {
          vault: {
            store_in_vault: 'ON_SUCCESS',
            usage_type: 'MERCHANT',
            customer_type: 'CONSUMER'
          }
        }
      }
    },
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '10.00'
      }
    }]
  });

  const response = await client.execute(request);
  return response.result.id;
}

// Step 2: After capture, extract payment token
async function captureAndSaveToken(orderID) {
  const request = new paypal.orders.OrdersCaptureRequest(orderID);
  request.prefer("return=representation");

  const capture = await client.execute(request);
  const paymentToken = capture.result.payment_source.paypal.attributes.vault.id;

  // Save paymentToken to your database
  await saveToDatabase({ paymentToken, customerId });

  return paymentToken;
}

// Step 3: Later, charge using saved token
async function chargeWithToken(paymentToken) {
  const request = new paypal.orders.OrdersCreateRequest();
  request.prefer("return=representation");
  request.requestBody({
    intent: 'CAPTURE',
    payment_source: {
      token: {
        id: paymentToken,
        type: 'PAYMENT_METHOD_TOKEN'
      }
    },
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '29.99'
      }
    }]
  });

  const response = await client.execute(request);
  return response.result;
}
````

```python Python expandable lines theme={null}
from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest

# Step 1: Create order with vault=true
def create_vault_order():
    request = OrdersCreateRequest()
    request.prefer('return=representation')
    request.request_body({
        'intent': 'CAPTURE',
        'payment_source': {
            'paypal': {
                'experience_context': {
                    'return_url': 'https://example.com/return',
                    'cancel_url': 'https://example.com/cancel'
                },
                'attributes': {
                    'vault': {
                        'store_in_vault': 'ON_SUCCESS',
                        'usage_type': 'MERCHANT',
                        'customer_type': 'CONSUMER'
                    }
                }
            }
        },
        'purchase_units': [{
            'amount': {
                'currency_code': 'USD',
                'value': '10.00'
            }
        }]
    })

    response = client.execute(request)
    return response.result.id

# Step 2: After capture, extract payment token
def capture_and_save_token(order_id):
    request = OrdersCaptureRequest(order_id)
    request.prefer('return=representation')

    capture = client.execute(request)
    payment_token = capture.result.payment_source.paypal.attributes.vault.id

    # Save payment_token to your database
    save_to_database(payment_token, customer_id)

    return payment_token

# Step 3: Later, charge using saved token
def charge_with_token(payment_token):
    request = OrdersCreateRequest()
    request.prefer('return=representation')
    request.request_body({
        'intent': 'CAPTURE',
        'payment_source': {
            'token': {
                'id': payment_token,
                'type': 'PAYMENT_METHOD_TOKEN'
            }
        },
        'purchase_units': [{
            'amount': {
                'currency_code': 'USD',
                'value': '29.99'
            }
        }]
    })

    response = client.execute(request)
    return response.result
```

```java Java expandable lines theme={null}
import com.paypal.orders.*;
import com.paypal.core.PayPalHttpClient;
import com.paypal.http.HttpResponse;

// Step 1: Create order with vault=true
public String createVaultOrder() throws IOException {
    OrderRequest orderRequest = new OrderRequest();
    orderRequest.checkoutPaymentIntent("CAPTURE");

    PaymentSourceDefinition paymentSource = new PaymentSourceDefinition();
    PayPalWallet paypalWallet = new PayPalWallet();

    ExperienceContext experienceContext = new ExperienceContext();
    experienceContext.returnUrl("https://example.com/return");
    experienceContext.cancelUrl("https://example.com/cancel");
    paypalWallet.experienceContext(experienceContext);

    VaultAttributes vaultAttributes = new VaultAttributes();
    vaultAttributes.storeInVault("ON_SUCCESS");
    vaultAttributes.usageType("MERCHANT");
    vaultAttributes.customerType("CONSUMER");

    PayPalAttributes paypalAttributes = new PayPalAttributes();
    paypalAttributes.vault(vaultAttributes);
    paypalWallet.attributes(paypalAttributes);

    paymentSource.paypal(paypalWallet);
    orderRequest.paymentSource(paymentSource);

    PurchaseUnitRequest purchaseUnit = new PurchaseUnitRequest();
    AmountWithBreakdown amount = new AmountWithBreakdown();
    amount.currencyCode("USD");
    amount.value("10.00");
    purchaseUnit.amountWithBreakdown(amount);

    orderRequest.purchaseUnits(Arrays.asList(purchaseUnit));

    OrdersCreateRequest request = new OrdersCreateRequest();
    request.prefer("return=representation");
    request.requestBody(orderRequest);

    HttpResponse<Order> response = client.execute(request);
    return response.result().id();
}

// Step 2: After capture, extract payment token
public String captureAndSaveToken(String orderId) throws IOException {
    OrdersCaptureRequest request = new OrdersCaptureRequest(orderId);
    request.prefer("return=representation");

    HttpResponse<Order> capture = client.execute(request);
    String paymentToken = capture.result()
        .paymentSource()
        .paypal()
        .attributes()
        .vault()
        .id();

    // Save paymentToken to your database
    saveToDatabase(paymentToken, customerId);

    return paymentToken;
}

// Step 3: Later, charge using saved token
public Order chargeWithToken(String paymentToken) throws IOException {
    OrderRequest orderRequest = new OrderRequest();
    orderRequest.checkoutPaymentIntent("CAPTURE");

    PaymentSourceDefinition paymentSource = new PaymentSourceDefinition();
    Token token = new Token();
    token.id(paymentToken);
    token.type("PAYMENT_METHOD_TOKEN");
    paymentSource.token(token);
    orderRequest.paymentSource(paymentSource);

    PurchaseUnitRequest purchaseUnit = new PurchaseUnitRequest();
    AmountWithBreakdown amount = new AmountWithBreakdown();
    amount.currencyCode("USD");
    amount.value("29.99");
    purchaseUnit.amountWithBreakdown(amount);

    orderRequest.purchaseUnits(Arrays.asList(purchaseUnit));

    OrdersCreateRequest request = new OrdersCreateRequest();
    request.prefer("return=representation");
    request.requestBody(orderRequest);

    HttpResponse<Order> response = client.execute(request);
    return response.result();
}
```

```php PHP expandable lines theme={null}
<?php
use PayPalCheckoutSdk\Orders\OrdersCreateRequest;
use PayPalCheckoutSdk\Orders\OrdersCaptureRequest;

// Step 1: Create order with vault=true
function createVaultOrder() {
    $request = new OrdersCreateRequest();
    $request->prefer('return=representation');
    $request->body = [
        'intent' => 'CAPTURE',
        'payment_source' => [
            'paypal' => [
                'experience_context' => [
                    'return_url' => 'https://example.com/return',
                    'cancel_url' => 'https://example.com/cancel'
                ],
                'attributes' => [
                    'vault' => [
                        'store_in_vault' => 'ON_SUCCESS',
                        'usage_type' => 'MERCHANT',
                        'customer_type' => 'CONSUMER'
                    ]
                ]
            ]
        ],
        'purchase_units' => [[
            'amount' => [
                'currency_code' => 'USD',
                'value' => '10.00'
            ]
        ]]
    ];

    $response = $client->execute($request);
    return $response->result->id;
}

// Step 2: After capture, extract payment token
function captureAndSaveToken($orderId) {
    global $client;

    $request = new OrdersCaptureRequest($orderId);
    $request->prefer('return=representation');

    $capture = $client->execute($request);
    $paymentToken = $capture->result->payment_source->paypal->attributes->vault->id;

    // Save paymentToken to your database
    saveToDatabase($paymentToken, $customerId);

    return $paymentToken;
}

// Step 3: Later, charge using saved token
function chargeWithToken($paymentToken) {
    global $client;

    $request = new OrdersCreateRequest();
    $request->prefer('return=representation');
    $request->body = [
        'intent' => 'CAPTURE',
        'payment_source' => [
            'token' => [
                'id' => $paymentToken,
                'type' => 'PAYMENT_METHOD_TOKEN'
            ]
        ],
        'purchase_units' => [[
            'amount' => [
                'currency_code' => 'USD',
                'value' => '29.99'
            ]
        ]]
    ];

    $response = $client->execute($request);
    return $response->result;
}
?>
```

```ruby Ruby expandable lines theme={null}
require 'paypal-checkout-sdk'

# Step 1: Create order with vault=true
def create_vault_order
  request = PayPalCheckoutSdk::Orders::OrdersCreateRequest.new
  request.prefer('return=representation')
  request.request_body({
    intent: 'CAPTURE',
    payment_source: {
      paypal: {
        experience_context: {
          return_url: 'https://example.com/return',
          cancel_url: 'https://example.com/cancel'
        },
        attributes: {
          vault: {
            store_in_vault: 'ON_SUCCESS',
            usage_type: 'MERCHANT',
            customer_type: 'CONSUMER'
          }
        }
      }
    },
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '10.00'
      }
    }]
  })

  response = client.execute(request)
  response.result.id
end

# Step 2: After capture, extract payment token
def capture_and_save_token(order_id)
  request = PayPalCheckoutSdk::Orders::OrdersCaptureRequest.new(order_id)
  request.prefer('return=representation')

  capture = client.execute(request)
  payment_token = capture.result.payment_source.paypal.attributes.vault.id

  # Save payment_token to your database
  save_to_database(payment_token, customer_id)

  payment_token
end

# Step 3: Later, charge using saved token
def charge_with_token(payment_token)
  request = PayPalCheckoutSdk::Orders::OrdersCreateRequest.new
  request.prefer('return=representation')
  request.request_body({
    intent: 'CAPTURE',
    payment_source: {
      token: {
        id: payment_token,
        type: 'PAYMENT_METHOD_TOKEN'
      }
    },
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: '29.99'
      }
    }]
  })

  response = client.execute(request)
  response.result
end
```

</CodeGroup>
