<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/delayed-capture -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Authorize and delay capture

Charge a customer after fulfilling their order, not immediately. Common use cases include:

- Reserve payment for pre-orders shipping in the future
- Charge after made-to-order items are produced
- Authorize hotels or rentals at booking, capture at check-in or check-out
- Confirm authenticity of high value items requiring verification before capturing payment

This integration uses the Orders API v2 to authorize and the Payments API v2 to capture later. To authorize first and capture later, change your integration to use `intent: "AUTHORIZE"`. This reserves funds on the customer's payment method for up to 29 days.

The highest success rate is within the first 3 days (the honor period). After 3 days, you may use reauthorization to extend the hold.

[What's the difference between authorization and capture?](/payments/methods/paypal/overview#authorization-vs-capture)

<Tip>Before you begin, you'll need to complete [the quick start PayPal integration](/payments/methods/paypal/integrate).</Tip>

## Integrate server side

Add the following to your existing server file from the quick start integration.

<CodeGroup>
  ```bash cURL lines expandable theme={null}
  # Step 1: Create order with AUTHORIZE intent
  curl -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{
      "intent": "AUTHORIZE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": "100.00"
        }
      }]
    }'

# Step 2: Capture the authorization later

curl -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/AUTHORIZATION_ID/capture \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN" \
 -d '{}'

````

```javascript Node.js lines expandable theme={null}
// Add these endpoints to your existing server.js from the quick start integration
// The PayPal client and addNegativeTesting helper are already configured

// Modify the create order endpoint to use AUTHORIZE intent
app.post('/api/orders', async (req, res) => {
  const request = new paypal.orders.OrdersCreateRequest();
  request.requestBody({
    intent: 'AUTHORIZE', // Changed from 'CAPTURE'
    purchase_units: [{
      amount: {
        currency_code: 'USD',
        value: req.body.amount || '100.00'
      }
    }]
  });

  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);

  try {
    const order = await client.execute(request);
    res.json({ id: order.result.id });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Add new endpoint to capture the authorization later
app.post('/api/orders/:orderId/capture', async (req, res) => {
  const { authorizationId } = req.body;
  const request = new paypal.payments.AuthorizationsCaptureRequest(authorizationId);

  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);

  try {
    const capture = await client.execute(request);
    res.json({
      status: capture.result.status,
      captureId: capture.result.id
    });
  } catch (err) {
    if (err.statusCode === 422) {
      res.status(400).json({ error: 'Authorization expired or invalid' });
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

# Create order with AUTHORIZE intent
@app.route('/api/orders', methods=['POST'])
def create_order():
  try:
    order = Order({
      "intent": "AUTHORIZE",
      "purchase_units": [{
        "amount": {
          "currency_code": "USD",
          "value": request.json.get('amount', '100.00')
        }
      }]
    })

    if order.create():
      return jsonify({"id": order.id})
    else:
      return jsonify({"error": order.error}), 500

  except Exception as e:
    return jsonify({"error": str(e)}), 500

# Capture authorization later
@app.route('/api/orders/<order_id>/capture', methods=['POST'])
def capture_authorization(order_id):
  try:
    authorization_id = request.json.get('authorizationId')
    authorization = Authorization.find(authorization_id)

    if authorization.capture():
      return jsonify({
        "status": authorization.state,
        "captureId": authorization.id
      })
    else:
      error = authorization.error
      if error.get('name') == 'AUTHORIZATION_EXPIRED':
        return jsonify({
          "error": "Authorization expired or invalid"
        }), 400
      else:
        return jsonify({"error": error.get('message')}), 500

  except Exception as e:
    return jsonify({"error": str(e)}), 500
```

```java Java lines expandable theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.orders.*;
import com.paypal.payments.AuthorizationsCaptureRequest;
import com.paypal.payments.Capture;

HttpClient httpClient = new PayPalHttpClient(
  new SandboxEnvironment(
    System.getenv("PAYPAL_CLIENT_ID"),
    System.getenv("PAYPAL_CLIENT_SECRET")
  )
);

// Create order with AUTHORIZE intent
@PostMapping("/api/orders")
public ResponseEntity<?> createOrder(@RequestBody OrderRequest orderRequest) {
  try {
    OrdersCreateRequest request = new OrdersCreateRequest();
    request.prefer("return=representation");
    request.body(new OrderRequest()
      .intent("AUTHORIZE")
      .purchaseUnits(List.of(
        new PurchaseUnitRequest()
          .amount(new Money()
            .currencyCode("USD")
            .value(orderRequest.getAmount() != null ?
              orderRequest.getAmount() : "100.00")
          )
      ))
    );

    HttpResponse<Order> response = httpClient.execute(request);
    return ResponseEntity.ok(Map.of("id", response.result().id()));

  } catch (Exception e) {
    return ResponseEntity.status(500).body(
      Map.of("error", e.getMessage())
    );
  }
}

// Capture authorization later
@PostMapping("/api/orders/{orderId}/capture")
public ResponseEntity<?> captureAuthorization(
  @PathVariable String orderId,
  @RequestBody Map<String, String> requestBody
) {
  try {
    String authorizationId = requestBody.get("authorizationId");
    AuthorizationsCaptureRequest request = new AuthorizationsCaptureRequest(authorizationId);

    HttpResponse<Capture> response = httpClient.execute(request);
    Capture capture = response.result();

    return ResponseEntity.ok(Map.of(
      "status", capture.status(),
      "captureId", capture.id()
    ));

  } catch (HttpClientException e) {
    if (e.statusCode() == 422) {
      return ResponseEntity.badRequest().body(
        Map.of("error", "Authorization expired or invalid")
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

// Create order with AUTHORIZE intent
$app->post('/api/orders', function ($request, $response) use ($client) {
  $body = $request->getParsedBody();

  $orderRequest = new OrdersCreateRequest();
  $orderRequest->prefer("return=representation");
  $orderRequest->body = [
    "intent" => "AUTHORIZE",
    "purchase_units" => [[
      "amount" => [
        "currency_code" => "USD",
        "value" => $body['amount'] ?? "100.00"
      ]
    ]]
  ];

  try {
    $orderResponse = $client->execute($orderRequest);
    $response->getBody()->write(json_encode([
      "id" => $orderResponse->result->id
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (Exception $e) {
    $response->getBody()->write(json_encode([
      "error" => $e->getMessage()
    ]));
    return $response->withStatus(500)->withHeader('Content-Type', 'application/json');
  }
});

// Capture authorization later
$app->post('/api/orders/{orderId}/capture', function ($request, $response, $args) use ($client) {
  $body = $request->getParsedBody();
  $authorizationId = $body['authorizationId'];

  $captureRequest = new AuthorizationsCaptureRequest($authorizationId);

  try {
    $captureResponse = $client->execute($captureRequest);
    $capture = $captureResponse->result;

    $response->getBody()->write(json_encode([
      "status" => $capture->status,
      "captureId" => $capture->id
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    if ($e->statusCode === 422) {
      $response->getBody()->write(json_encode([
        "error" => "Authorization expired or invalid"
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

# Create order with AUTHORIZE intent
post '/api/orders' do
  request_body = JSON.parse(request.body.read)

  begin
    order = PayPal::SDK::OrdersApi::Order.new(
      intent: "AUTHORIZE",
      purchase_units: [{
        amount: {
          currency_code: "USD",
          value: request_body['amount'] || "100.00"
        }
      }]
    )

    if order.create
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

# Capture authorization later
post '/api/orders/:order_id/capture' do
  order_id = params['order_id']
  request_body = JSON.parse(request.body.read)
  authorization_id = request_body['authorizationId']

  begin
    authorization = PayPal::SDK::PaymentsApi::Authorization.find(authorization_id)

    if authorization.capture
      content_type :json
      {
        status: authorization.status,
        captureId: authorization.id
      }.to_json
    else
      error = authorization.error
      if error['name'] == 'AUTHORIZATION_EXPIRED'
        status 400
        { error: 'Authorization expired or invalid' }.to_json
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

## Test endpoints

<Info>
  Endpoints:

- [`/v2/checkout/orders/{id}/authorize`](/reference/api/rest/orders/authorize-payment-for-order)
- [`/v2/payments/authorizations/{authorization_id}/capture`](/reference/api/rest/authorizations/capture-authorized-payment)
  </Info>

<CodeGroup>
  ```bash cURL lines expandable theme={null}
  # 1. Create authorization (returns orderId)
  curl -X POST http://localhost:3000/api/orders \
    -H "Content-Type: application/json" \
    -d '{"amount": "100.00"}'

# Expected response:

# {"id":"5O190127TN364715T"}

# 2. Later, capture the authorization (use authorizationId from PayPal)

curl -X POST http://localhost:3000/api/orders/ORDER_ID/capture \
 -H "Content-Type: application/json" \
 -d '{"authorizationId": "AUTH_ID_FROM_PAYPAL"}'

# Expected response:

# {"status":"COMPLETED","captureId":"3C679366HH908993F"}

````

```javascript Node.js lines expandable theme={null}
// 1. Create authorization
const createResponse = await fetch('http://localhost:3000/api/orders', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ amount: '100.00' })
});
const order = await createResponse.json();
console.log('Order created:', order);
// Expected: {"id":"5O190127TN364715T"}

// 2. Later, capture the authorization
const captureResponse = await fetch('http://localhost:3000/api/orders/ORDER_ID/capture', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ authorizationId: 'AUTH_ID_FROM_PAYPAL' })
});
const capture = await captureResponse.json();
console.log('Capture result:', capture);
// Expected: {"status":"COMPLETED","captureId":"3C679366HH908993F"}
````

```python Python lines expandable theme={null}
import requests

# 1. Create authorization
create_response = requests.post(
  'http://localhost:3000/api/orders',
  headers={'Content-Type': 'application/json'},
  json={'amount': '100.00'}
)
print('Order created:', create_response.json())
# Expected: {"id":"5O190127TN364715T"}

# 2. Later, capture the authorization
capture_response = requests.post(
  'http://localhost:3000/api/orders/ORDER_ID/capture',
  headers={'Content-Type': 'application/json'},
  json={'authorizationId': 'AUTH_ID_FROM_PAYPAL'}
)
print('Capture result:', capture_response.json())
# Expected: {"status":"COMPLETED","captureId":"3C679366HH908993F"}
```

```java Java lines expandable theme={null}
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();

// 1. Create authorization
String createBody = "{\"amount\":\"100.00\"}";
HttpRequest createRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/orders"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.ofString(createBody))
  .build();

HttpResponse<String> createResponse = client.send(
  createRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Order created: " + createResponse.body());
// Expected: {"id":"5O190127TN364715T"}

// 2. Later, capture the authorization
String captureBody = "{\"authorizationId\":\"AUTH_ID_FROM_PAYPAL\"}";
HttpRequest captureRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/orders/ORDER_ID/capture"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.ofString(captureBody))
  .build();

HttpResponse<String> captureResponse = client.send(
  captureRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Capture result: " + captureResponse.body());
// Expected: {"status":"COMPLETED","captureId":"3C679366HH908993F"}
```

```php PHP lines expandable theme={null}
<?php
// 1. Create authorization
$createData = json_encode(['amount' => '100.00']);

$createResponse = file_get_contents(
  'http://localhost:3000/api/orders',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json',
      'content' => $createData
    ]
  ])
);
echo "Order created: " . $createResponse . "\n";
// Expected: {"id":"5O190127TN364715T"}

// 2. Later, capture the authorization
$captureData = json_encode(['authorizationId' => 'AUTH_ID_FROM_PAYPAL']);

$captureResponse = file_get_contents(
  'http://localhost:3000/api/orders/ORDER_ID/capture',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json',
      'content' => $captureData
    ]
  ])
);
echo "Capture result: " . $captureResponse . "\n";
// Expected: {"status":"COMPLETED","captureId":"3C679366HH908993F"}
```

```ruby Ruby lines expandable theme={null}
require 'net/http'
require 'json'

# 1. Create authorization
uri = URI('http://localhost:3000/api/orders')
create_request = Net::HTTP::Post.new(uri)
create_request['Content-Type'] = 'application/json'
create_request.body = { amount: '100.00' }.to_json

create_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(create_request)
end
puts "Order created: #{create_response.body}"
# Expected: {"id":"5O190127TN364715T"}

# 2. Later, capture the authorization
capture_uri = URI('http://localhost:3000/api/orders/ORDER_ID/capture')
capture_request = Net::HTTP::Post.new(capture_uri)
capture_request['Content-Type'] = 'application/json'
capture_request.body = { authorizationId: 'AUTH_ID_FROM_PAYPAL' }.to_json

capture_response = Net::HTTP.start(capture_uri.hostname, capture_uri.port) do |http|
  http.request(capture_request)
end
puts "Capture result: #{capture_response.body}"
# Expected: {"status":"COMPLETED","captureId":"3C679366HH908993F"}
```

</CodeGroup>

## Best practices

- **Capture within 3-day honor period:** Authorization success rates are highest during the 3-day honor period. After the payment is authorized, ship within 3 days.
- **Track authorization expiration:** Store the date when the authorization was created in your database. Alert when approaching day 29 and have a process to handle expiring authorizations.
- **Handle partial captures:** You can capture any amount up to the authorized total. The remainder can be voided or left to expire. For multiple shipments, use multiple partial captures.
- **Void uncaptured authorizations promptly:** If you can't fulfill an order, void the authorization immediately to release customer funds.
- **Communicate holds to customers:** Inform customers that their payment is authorized, but not yet charged. Inform them when the actual charge will occur.
- **Monitor authorization validity:** Authorizations can be voided by the customer's bank or PayPal. Handle capture failures gracefully.

## Important details

- **Find authorization IDs:** The authorization ID is in the order approval response at `purchase_units[0].payments.authorizations[0].id`. Store this value in your database immediately.
- **Authorization expiration:** YYou have up to 29 days to capture. The 3-day honor period (when the cardholder's issuing bank is most likely to approve the capture) is your best window. After 29 days, the authorization automatically expires and you must create a new order to charge the customer.
- **Partial captures:** You can capture any amount up to the authorized total. Make multiple partial captures for [split shipments](/payments/methods/paypal/split-shipments) or capture less than the full amount if needed.
- **Extending authorizations:** Use reauthorization between days 4-29 to extend an authorization. See [Reauthorize an authorization](/payments/methods/paypal/reauthorize).

## Test your integration

Sandbox authorizations don't expire after 29 days. Test authorizations with negative testing instead.

### Standard testing

| Test scenario            | Setup                                                                   | Expected result                             |
| :----------------------- | :---------------------------------------------------------------------- | :------------------------------------------ |
| Authorize and capture    | Create an order with `intent: "AUTHORIZE"`, then capture after 1 minute | Authorization successful, capture completes |
| Partial capture          | Authorize \$100, capture \$60                                           | \$60 captured, \$40 remains available       |
| Invalid authorization ID | Use `"INVALID_AUTH_123"` as auth ID                                     | Returns 404 error                           |
| Capture after 5 days     | Wait 5 days past honor period                                           | Capture may succeed with lower rate         |

### Negative testing

1. Make sure to enable negative testing in your sandbox business account as described in the [quick start prerequisites](/payments/methods/paypal/integrate#prerequisites).
2. In the `.env` file, set `ENABLE_NEGATIVE_TESTING=true` and set `NEGATIVE_TEST_TYPE` to one of the error codes in the table.
3. Restart the server after changing the `.env` file: `node server.js`.

| Test scenario         | Error code                       | Expected result                                           |
| :-------------------- | :------------------------------- | :-------------------------------------------------------- |
| Expired authorization | `AUTHORIZATION_EXPIRED`          | Returns 422 error with "Authorization expired or invalid" |
| Already captured      | `AUTHORIZATION_ALREADY_CAPTURED` | Returns 422 error with "Authorization already captured"   |

## Go-live checklist

- Implement authorization tracking system.
- Integrate capture process with fulfillment workflow.
- Configure authorization expiration monitoring.
- Test customer communication about holds.
- Test with real \$1 authorization and capture.

## Post-launch monitoring

These values are suggested monitoring thresholds for your integration, not performance guarantees from PayPal.

| Metric                        | Target      | Action if below target                                |
| :---------------------------- | :---------- | :---------------------------------------------------- |
| Authorization success rate    | 95%         | Investigate authorization failures with issuing banks |
| Capture rate within 3 days    | 90%         | Optimize fulfillment workflow for faster processing   |
| Authorization expiration rate | \<2%        | Improve expiration alerts and capture automation      |
| API response time             | \<2 seconds | Check PayPal API status                               |
| Capture success rate          | 98%         | Review expired or voided authorizations               |
