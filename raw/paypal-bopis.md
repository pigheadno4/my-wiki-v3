<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/buy-online-pick-up-in-store -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Buy online, pick up in store

Handle payments for orders that customers purchase online and pick up at a physical store location. This pattern authorizes payment at checkout and captures funds after verifying pickup. This ensures payment is secured and collected only when the customer receives their items.

Common scenarios include:

- Retail stores offering same-day pickup
- Grocery orders for curbside pickup
- Restaurant orders for takeout
- Click-and-collect services

<Tip>Before you begin, you'll need to complete [the quick start PayPal integration](/payments/methods/paypal/integrate).</Tip>

## Integrate server side

Add the following endpoints to your existing server file from the quick start integration.

<CodeGroup>
  ```bash cURL lines expandable theme={null}
  # Create BOPIS order (authorization)
  curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{
      "intent": "AUTHORIZE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": "75.00"
        },
        "custom_id": "PICKUP-PICK789",
        "description": "Pickup at Store #123"
      }]
    }'

# Authorize the order

curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/authorize \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN"

# Capture payment at pickup

curl -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/AUTH_ID/capture \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN"

````

```javascript Node.js lines expandable theme={null}
// The PayPal client and addNegativeTesting helper are already configured from the quick start integration

// Modify create order for BOPIS (authorize instead of capture)
app.post('/api/orders/bopis', async (req, res) => {
  const { amount, pickupLocation, pickupCode } = req.body;
  const request = new paypal.orders.OrdersCreateRequest();
  request.requestBody({
    intent: 'AUTHORIZE', // Authorize for pickup verification
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: amount || '100.00'
      },
      custom_id: `PICKUP-${pickupCode}`, // Store pickup code
      description: `Pickup at ${pickupLocation}`
    }]
  });
  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);
  try {
    const order = await client.execute(request);
    // Store pickup details with order
    await storePickupDetails(order.result.id, pickupCode, pickupLocation);
    res.json({ id: order.result.id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Capture payment after the customer picks up the order
app.post('/api/orders/bopis/:orderId/pickup', async (req, res) => {
  const { authorizationId, pickupCode } = req.body;
  // Verify pickup code matches
  if (!await verifyPickupCode(req.params.orderId, pickupCode)) {
    return res.status(401).json({ error: 'Invalid pickup code' });
  }
  const request = new paypal.payments.AuthorizationsCaptureRequest(authorizationId);
  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);
  try {
    const capture = await client.execute(request);
    res.json({
      status: 'PICKED_UP',
      captureId: capture.result.id
    });
  } catch (err) {
    if (err.statusCode === 422) {
      res.status(400).json({ error: 'Authorization expired - order canceled' });
    } else {
      res.status(500).json({ error: err.message });
    }
  }
});
````

```python Python lines expandable theme={null}
from paypalrestsdk import Api, Order, Authorization
import os

# Configure PayPal SDK
api = Api({
  'mode': 'sandbox',
  'client_id': os.environ['PAYPAL_CLIENT_ID'],
  'client_secret': os.environ['PAYPAL_CLIENT_SECRET']
})

# Create BOPIS order (authorization)
@app.route('/api/orders/bopis', methods=['POST'])
def create_bopis_order():
  try:
    amount = request.json.get('amount', '100.00')
    pickup_location = request.json.get('pickupLocation')
    pickup_code = request.json.get('pickupCode')

    order_data = {
      "intent": "AUTHORIZE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": amount
        },
        "custom_id": f"PICKUP-{pickup_code}",
        "description": f"Pickup at {pickup_location}"
      }]
    }

    order = Order(order_data)
    if order.create():
      # Store pickup details with order
      store_pickup_details(order.id, pickup_code, pickup_location)
      return jsonify({"id": order.id})
    else:
      return jsonify({"error": order.error}), 500

  except Exception as e:
    return jsonify({"error": str(e)}), 500

# Capture payment after pickup
@app.route('/api/orders/bopis/<order_id>/pickup', methods=['POST'])
def capture_at_pickup(order_id):
  try:
    authorization_id = request.json.get('authorizationId')
    pickup_code = request.json.get('pickupCode')

    # Verify pickup code matches
    if not verify_pickup_code(order_id, pickup_code):
      return jsonify({"error": "Invalid pickup code"}), 401

    authorization = Authorization.find(authorization_id)
    capture = authorization.capture()

    if capture.success():
      return jsonify({
        "status": "PICKED_UP",
        "captureId": capture.id
      })
    else:
      error = capture.error
      if error.get('name') == 'AUTHORIZATION_EXPIRED':
        return jsonify({
          "error": "Authorization expired - order canceled"
        }), 400
      else:
        return jsonify({"error": error.get('message')}), 500

  except Exception as e:
    return jsonify({"error": str(e)}), 500
```

```java Java lines expandable theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.orders.OrdersCreateRequest;
import com.paypal.orders.OrderRequest;
import com.paypal.orders.PurchaseUnitRequest;
import com.paypal.orders.AmountWithBreakdown;
import com.paypal.payments.AuthorizationsCaptureRequest;
import com.paypal.payments.Capture;

HttpClient httpClient = new PayPalHttpClient(
  new SandboxEnvironment(
    System.getenv("PAYPAL_CLIENT_ID"),
    System.getenv("PAYPAL_CLIENT_SECRET")
  )
);

// Create BOPIS order (authorization)
@PostMapping("/api/orders/bopis")
public ResponseEntity<?> createBopisOrder(@RequestBody BopisOrderRequest bopisRequest) {
  try {
    OrdersCreateRequest request = new OrdersCreateRequest();

    OrderRequest orderRequest = new OrderRequest()
      .checkoutPaymentIntent("AUTHORIZE")
      .purchaseUnits(Arrays.asList(
        new PurchaseUnitRequest()
          .amountWithBreakdown(
            new AmountWithBreakdown()
              .currencyCode("USD")
              .value(bopisRequest.getAmount() != null ?
                bopisRequest.getAmount() : "100.00")
          )
          .customId("PICKUP-" + bopisRequest.getPickupCode())
          .description("Pickup at " + bopisRequest.getPickupLocation())
      ));

    request.requestBody(orderRequest);
    HttpResponse<Order> response = httpClient.execute(request);
    Order order = response.result();

    // Store pickup details with order
    storePickupDetails(order.id(), bopisRequest.getPickupCode(),
                      bopisRequest.getPickupLocation());

    return ResponseEntity.ok(Map.of("id", order.id()));

  } catch (Exception e) {
    return ResponseEntity.status(500).body(
      Map.of("error", e.getMessage())
    );
  }
}

// Capture payment after pickup
@PostMapping("/api/orders/bopis/{orderId}/pickup")
public ResponseEntity<?> captureAtPickup(
  @PathVariable String orderId,
  @RequestBody PickupRequest pickupRequest
) {
  try {
    // Verify pickup code matches
    if (!verifyPickupCode(orderId, pickupRequest.getPickupCode())) {
      return ResponseEntity.status(401).body(
        Map.of("error", "Invalid pickup code")
      );
    }

    AuthorizationsCaptureRequest request =
      new AuthorizationsCaptureRequest(pickupRequest.getAuthorizationId());

    HttpResponse<Capture> response = httpClient.execute(request);
    Capture capture = response.result();

    return ResponseEntity.ok(Map.of(
      "status", "PICKED_UP",
      "captureId", capture.id()
    ));

  } catch (HttpClientException e) {
    if (e.statusCode() == 422) {
      return ResponseEntity.badRequest().body(
        Map.of("error", "Authorization expired - order canceled")
      );
    }
    return ResponseEntity.status(500).body(
      Map.of("error", e.getMessage())
    );
  }
}
```

```php PHP lines expandable theme={null}
<?php
use PayPalCheckoutSdk\Core\SandboxEnvironment;
use PayPalCheckoutSdk\Core\PayPalHttpClient;
use PayPalCheckoutSdk\Orders\OrdersCreateRequest;
use PayPalCheckoutSdk\Payments\AuthorizationsCaptureRequest;

$environment = new SandboxEnvironment(
  getenv('PAYPAL_CLIENT_ID'),
  getenv('PAYPAL_CLIENT_SECRET')
);
$client = new PayPalHttpClient($environment);

// Create BOPIS order (authorization)
$app->post('/api/orders/bopis', function ($request, $response) use ($client) {
  $body = $request->getParsedBody();

  $orderRequest = new OrdersCreateRequest();
  $orderRequest->body = [
    "intent" => "AUTHORIZE",
    "purchase_units" => [[
      "amount" => [
        "currency_code" => "USD",
        "value" => $body['amount'] ?? "100.00"
      ],
      "custom_id" => "PICKUP-" . $body['pickupCode'],
      "description" => "Pickup at " . $body['pickupLocation']
    ]]
  ];

  try {
    $orderResponse = $client->execute($orderRequest);
    $order = $orderResponse->result;

    // Store pickup details with order
    storePickupDetails($order->id, $body['pickupCode'], $body['pickupLocation']);

    $response->getBody()->write(json_encode([
      "id" => $order->id
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    $response->getBody()->write(json_encode([
      "error" => $e->getMessage()
    ]));
    return $response->withStatus(500)->withHeader('Content-Type', 'application/json');
  }
});

// Capture payment after pickup
$app->post('/api/orders/bopis/{orderId}/pickup', function ($request, $response, $args) use ($client) {
  $orderId = $args['orderId'];
  $body = $request->getParsedBody();

  // Verify pickup code matches
  if (!verifyPickupCode($orderId, $body['pickupCode'])) {
    $response->getBody()->write(json_encode([
      "error" => "Invalid pickup code"
    ]));
    return $response->withStatus(401)->withHeader('Content-Type', 'application/json');
  }

  $captureRequest = new AuthorizationsCaptureRequest($body['authorizationId']);

  try {
    $captureResponse = $client->execute($captureRequest);
    $capture = $captureResponse->result;

    $response->getBody()->write(json_encode([
      "status" => "PICKED_UP",
      "captureId" => $capture->id
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    $statusCode = $e->statusCode;

    if ($statusCode === 422) {
      $response->getBody()->write(json_encode([
        "error" => "Authorization expired - order canceled"
      ]));
      return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
    }

    $response->getBody()->write(json_encode([
      "error" => $e->getMessage()
    ]));
    return $response->withStatus(500)->withHeader('Content-Type', 'application/json');
  }
});
```

```ruby Ruby lines expandable theme={null}
require 'paypal-sdk'

# Configure PayPal SDK
PayPal::SDK.configure(
  :mode => "sandbox",
  :app_id => ENV['PAYPAL_APP_ID'],
  :client_id => ENV['PAYPAL_CLIENT_ID'],
  :client_secret => ENV['PAYPAL_CLIENT_SECRET']
)

# Create BOPIS order (authorization)
post '/api/orders/bopis' do
  request_body = JSON.parse(request.body.read)

  begin
    order_data = {
      intent: 'AUTHORIZE',
      purchase_units: [{
        amount: {
          currency_code: 'USD',
          value: request_body['amount'] || '100.00'
        },
        custom_id: "PICKUP-#{request_body['pickupCode']}",
        description: "Pickup at #{request_body['pickupLocation']}"
      }]
    }

    order = PayPal::SDK::Orders::Order.new(order_data)

    if order.create
      # Store pickup details with order
      store_pickup_details(order.id, request_body['pickupCode'],
                          request_body['pickupLocation'])

      content_type :json
      { id: order.id }.to_json
    else
      status 500
      { error: order.error }.to_json
    end

  rescue => e
    status 500
    { error: e.message }.to_json
  end
end

# Capture payment after pickup
post '/api/orders/bopis/:order_id/pickup' do
  order_id = params['order_id']
  request_body = JSON.parse(request.body.read)

  begin
    # Verify pickup code matches
    unless verify_pickup_code(order_id, request_body['pickupCode'])
      status 401
      return { error: 'Invalid pickup code' }.to_json
    end

    authorization = PayPal::SDK::PaymentsApi::Authorization.find(
      request_body['authorizationId']
    )
    capture = authorization.capture

    if capture.success?
      content_type :json
      {
        status: 'PICKED_UP',
        captureId: capture.id
      }.to_json
    else
      error = capture.error
      if error['name'] == 'AUTHORIZATION_EXPIRED'
        status 400
        { error: 'Authorization expired - order canceled' }.to_json
      else
        status 500
        { error: error['message'] }.to_json
      end
    end

  rescue => e
    status 500
    { error: e.message }.to_json
  end
end
```

</CodeGroup>

### Test endpoints

1. Create an authorization.

<Info>Endpoint: [`/v2/checkout/orders/{id}/authorize`](/reference/api/rest/orders/authorize-payment-for-order)</Info>

```bash lines theme={null}
# 1. Create BOPIS order (authorization)
curl -X POST http://localhost:3000/api/orders/bopis \
  -H "Content-Type: application/json" \
  -d '{"amount": "75.00", "pickupLocation": "Store #123", "pickupCode": "PICK789"}'
```

2. Capture payment at pickup.

<Info>Endpoint: [`/v2/payments/authorizations/{authorization_id}/capture`](/reference/api/rest/authorizations/capture-authorized-payment)</Info>

```bash lines theme={null}
# 2. Complete pickup (capture payment)
curl -X POST http://localhost:3000/api/orders/bopis/ORDER_ID/pickup \
  -H "Content-Type: application/json" \
  -d '{"authorizationId": "AUTH_ID", "pickupCode": "PICK789"}'
```

## Best practices

- **Set clear pickup timeframes:** Communicate pickup windows. Typical holds: 7 days for retail, 24 hours for restaurants or groceries. Balance customer convenience with inventory management. Automatically void expired authorizations.
- **Implement pickup verification:** Require order number and pickup code. Capture payment only after verifying the customer.
- **Handle partial pickups:** If part of the order is collected, capture the partial amount and void the remainder.
- **Train store staff:** Ensure staff know when to trigger capture and how to handle pickup exceptions.
- **Monitor unclaimed orders:** Track unclaimed orders and void authorizations promptly to release funds.

## Important details

- **Capture only after pickup verification:** Do not capture payment before verifying the customer has received their items. This protects both you and the customer from fraud.
- **Add items at pickup:** If customers want to add items at pickup, process additional items as a separate transaction at the store.
- **Handle partial pickups:** If only part of an order is available, capture only the amount for available items and void the remaining authorization.
- **Notification timing:** Email customers when orders are ready for pickup, but only capture payment after pickup. The authorization secures payment while the order waits.
- **Identity verification methods:** Verify customer identity through order number, pickup code, photo ID, or app confirmation before capturing. Works the same for in-store, curbside, or drive-up pickup.

## Test your integration

Before testing pickup flows, authorize an order to obtain an authorization ID.

### Standard testing

| Test scenario       | Setup                                     | Expected result                                         |
| :------------------ | :---------------------------------------- | :------------------------------------------------------ |
| Successful pickup   | Create order and verify with correct code | Authorization succeeds and capture completes on pickup. |
| Invalid pickup code | Use incorrect pickup code                 | Returns 401 error: invalid pickup code.                 |
| Abandoned order     | Do not pick up within timeframe           | Authorization is voided automatically.                  |
| Partial pickup      | Authorize \$100, pick up \$60             | Capture \$60 and void remaining \$40.                   |

### Negative testing

For negative testing:

1. Make sure to enable negative testing in your sandbox business account as described in the [quick start prerequisites](/payments/methods/paypal/integrate#prerequisites).
2. In the `.env` file, set `ENABLE_NEGATIVE_TESTING=true` and set `NEGATIVE_TEST_TYPE` to one of the error codes in the table.
3. Restart the server after changing the `.env` file: `node server.js`.

| Test scenario         | Error code                       | Expected result                                  |
| :-------------------- | :------------------------------- | :----------------------------------------------- |
| Expired authorization | `AUTHORIZATION_EXPIRED`          | Error: authorization expired and order canceled. |
| Already picked up     | `AUTHORIZATION_ALREADY_CAPTURED` | Error: authorization already captured.           |

## Go-live checklist

- Integrate store pickup system with payment capture.
- Test pickup verification at all store locations.
- Configure automatic voids for unclaimed orders.
- Train store staff on capture process.
- Test with a real \$1 order and pickup.

## Post-launch monitoring

These values are suggested monitoring thresholds for your integration, not performance guarantees from PayPal.

| Metric                        | Target      | Action if below target                                  |
| :---------------------------- | :---------- | :------------------------------------------------------ |
| Authorization success rate    | 95%         | Investigate authorization failures.                     |
| Capture success at pickup     | 90%         | Check for expired authorizations or staff process gaps. |
| Authorization expiration rate | \<15%       | Monitor for abnormal increases.                         |
| Void success rate (abandoned) | 98%         | Investigate void failures.                              |
| API response time             | \<2 seconds | Check PayPal API status.                                |
