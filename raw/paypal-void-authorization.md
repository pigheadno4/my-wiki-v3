<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/void-an-authorization -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Void an authorized payment

Cancel an authorized payment before capturing it to release the customer's held funds. Voiding an authorized payment saves processing fees compared to refunding a captured payment. Common scenarios include:

- Customer cancels an order before shipment
- Item is out of stock after authorization
- Order fails fraud verification
- Customer requests cancellation during fulfillment

Add the void endpoint to cancel authorizations. This integration uses the Payments API v2 and requires an authorized payment that hasn't been captured yet.

[What's the difference between authorization and capture?](/payments/methods/paypal/overview#authorization-vs-capture)

## Prerequisites

- Complete [the quick start PayPal integration](/payments/methods/paypal/integrate).
- Implement an authorization and capture flow that doesn't use immediate capture.
- Have an authorization ID from an order creation. Store authorization IDs in your database when creating orders. You'll need them to void the authorization.
- Optional for production:
  - Automated void triggers for inventory and fraud checks
  - Customer notifications on voided payments
  - Void reason tracking for analytics

## Integrate server side

Add the following to your existing server file from the quick start integration.

<CodeGroup>
  ```bash cURL lines theme={null}
  # Void an authorization
  curl -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/AUTHORIZATION_ID/void \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{}'
  ```

```javascript Node.js expandable lines theme={null}
// Add this endpoint to your existing server.js from the quick start integration
// The PayPal client and addNegativeTesting helper are already configured

// Void an authorization (cancel before capture)
app.post("/api/authorizations/:authID/void", async (req, res) => {
  const request = new paypal.payments.AuthorizationsVoidRequest(
    req.params.authID,
  );

  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);

  try {
    const voidResult = await client.execute(request);
    res.json({
      id: voidResult.result.id,
      status: voidResult.result.status,
    });
  } catch (err) {
    // Handle specific void errors
    if (err.statusCode === 422) {
      const errorDetail = err.details?.[0];
      if (errorDetail?.issue === "AUTHORIZATION_ALREADY_CAPTURED") {
        res.status(400).json({
          error: "Cannot void - already captured. Use refund instead.",
          captureId: errorDetail.description,
        });
      } else if (errorDetail?.issue === "AUTHORIZATION_VOIDED") {
        res.status(400).json({ error: "Authorization already voided" });
      } else {
        res.status(400).json({ error: "Invalid authorization state" });
      }
    } else {
      res.status(500).json({ error: err.message });
    }
  }
});
```

```python Python expandable lines theme={null}
from paypalrestsdk import Api, Authorization
import os

# Configure PayPal SDK
api = Api({
  'mode': 'sandbox',
  'client_id': os.environ['PAYPAL_CLIENT_ID'],
  'client_secret': os.environ['PAYPAL_CLIENT_SECRET']
})

# Void an authorization
@app.route('/api/authorizations/<auth_id>/void', methods=['POST'])
def void_authorization(auth_id):
  try:
    authorization = Authorization.find(auth_id)

    if authorization.void():
      return jsonify({
        "id": authorization.id,
        "status": authorization.state
      })
    else:
      # Handle errors
      error = authorization.error
      if error.get('name') == 'AUTHORIZATION_ALREADY_CAPTURED':
        return jsonify({
          "error": "Cannot void - already captured. Use refund instead."
        }), 400
      elif error.get('name') == 'AUTHORIZATION_VOIDED':
        return jsonify({
          "error": "Authorization already voided"
        }), 400
      else:
        return jsonify({
          "error": "Invalid authorization state"
        }), 400

  except Exception as e:
    return jsonify({"error": str(e)}), 500
```

```java Java theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.payments.AuthorizationsVoidRequest;
import com.paypal.payments.Authorization;

HttpClient httpClient = new PayPalHttpClient(
  new SandboxEnvironment(
    System.getenv("PAYPAL_CLIENT_ID"),
    System.getenv("PAYPAL_CLIENT_SECRET")
  )
);

// Void an authorization
@PostMapping("/api/authorizations/{authId}/void")
public ResponseEntity<?> voidAuthorization(@PathVariable String authId) {
  try {
    AuthorizationsVoidRequest request = new AuthorizationsVoidRequest(authId);

    HttpResponse<Authorization> response = httpClient.execute(request);
    Authorization authorization = response.result();

    return ResponseEntity.ok(Map.of(
      "id", authorization.id(),
      "status", authorization.status()
    ));

  } catch (HttpClientException e) {
    if (e.statusCode() == 422) {
      String issue = extractIssue(e);
      if ("AUTHORIZATION_ALREADY_CAPTURED".equals(issue)) {
        return ResponseEntity.badRequest().body(
          Map.of("error", "Cannot void - already captured. Use refund instead.")
        );
      } else if ("AUTHORIZATION_VOIDED".equals(issue)) {
        return ResponseEntity.badRequest().body(
          Map.of("error", "Authorization already voided")
        );
      } else {
        return ResponseEntity.badRequest().body(
          Map.of("error", "Invalid authorization state")
        );
      }
    }
    return ResponseEntity.status(500).body(
      Map.of("error", e.getMessage())
    );
  }
}
```

```php PHP expandable lines theme={null}
<?php
use PayPalCheckoutSdk\Core\SandboxEnvironment;
use PayPalCheckoutSdk\Core\PayPalHttpClient;
use PayPalCheckoutSdk\Payments\AuthorizationsVoidRequest;

$environment = new SandboxEnvironment(
  getenv('PAYPAL_CLIENT_ID'),
  getenv('PAYPAL_CLIENT_SECRET')
);
$client = new PayPalHttpClient($environment);

// Void an authorization
$app->post('/api/authorizations/{authID}/void', function ($request, $response, $args) use ($client) {
  $authID = $args['authID'];

  $voidRequest = new AuthorizationsVoidRequest($authID);

  try {
    $voidResponse = $client->execute($voidRequest);
    $authorization = $voidResponse->result;

    $response->getBody()->write(json_encode([
      "id" => $authorization->id,
      "status" => $authorization->status
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    $statusCode = $e->statusCode;
    $errorData = json_decode($e->getMessage(), true);

    if ($statusCode === 422) {
      $issue = $errorData['details'][0]['issue'] ?? '';
      if ($issue === 'AUTHORIZATION_ALREADY_CAPTURED') {
        $response->getBody()->write(json_encode([
          "error" => "Cannot void - already captured. Use refund instead."
        ]));
        return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
      } else if ($issue === 'AUTHORIZATION_VOIDED') {
        $response->getBody()->write(json_encode([
          "error" => "Authorization already voided"
        ]));
        return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
      } else {
        $response->getBody()->write(json_encode([
          "error" => "Invalid authorization state"
        ]));
        return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
      }
    }

    $response->getBody()->write(json_encode([
      "error" => $e->getMessage()
    ]));
    return $response->withStatus(500)->withHeader('Content-Type', 'application/json');
  }
});
```

```ruby Ruby expandable lines theme={null}
require 'paypal-sdk'

# Configure PayPal SDK
PayPal::SDK.configure(
  :mode => "sandbox",
  :app_id => ENV['PAYPAL_APP_ID'],
  :client_id => ENV['PAYPAL_CLIENT_ID'],
  :client_secret => ENV['PAYPAL_CLIENT_SECRET']
)

# Void an authorization
post '/api/authorizations/:auth_id/void' do
  auth_id = params['auth_id']

  begin
    authorization = PayPal::SDK::PaymentsApi::Authorization.find(auth_id)

    if authorization.void
      content_type :json
      {
        id: authorization.id,
        status: authorization.status
      }.to_json
    else
      error = authorization.error
      if error['name'] == 'AUTHORIZATION_ALREADY_CAPTURED'
        status 400
        { error: 'Cannot void - already captured. Use refund instead.' }.to_json
      elsif error['name'] == 'AUTHORIZATION_VOIDED'
        status 400
        { error: 'Authorization already voided' }.to_json
      else
        status 400
        { error: 'Invalid authorization state' }.to_json
      end
    end

  rescue => e
    status 500
    { error: e.message }.to_json
  end
end
```

</CodeGroup>

## Test endpoint

<Info>
  Endpoint: [`/v2/payments/authorizations/{authorization_id}/void`](/reference/api/rest/authorizations/void-authorized-payment)
</Info>

<CodeGroup>
  ```bash cURL expandable lines theme={null}
  # Test voiding an authorization (replace with actual authorization ID)
  curl -X POST http://localhost:3000/api/authorizations/8AA831015G517922L/void \
    -H "Content-Type: application/json"

# Expected success response:

# {"id":"8AA831015G517922L","status":"VOIDED"}

# Test voiding already captured authorization (should fail)

curl -X POST http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void \
 -H "Content-Type: application/json"

# Expected error response:

# {"error":"Cannot void - already captured. Use refund instead."}

````

```javascript Node.js expandable lines theme={null}
// Test voiding an authorization
const voidResponse = await fetch('http://localhost:3000/api/authorizations/8AA831015G517922L/void', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
});
const voidResult = await voidResponse.json();
console.log('Void result:', voidResult);
// Expected: {"id":"8AA831015G517922L","status":"VOIDED"}

// Test voiding already captured authorization (should fail)
const capturedVoidResponse = await fetch('http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
});
const capturedVoidResult = await capturedVoidResponse.json();
console.log('Error result:', capturedVoidResult);
// Expected: {"error":"Cannot void - already captured. Use refund instead."}
````

```python Python expandable lines theme={null}
import requests

# Test voiding an authorization
void_response = requests.post(
  'http://localhost:3000/api/authorizations/8AA831015G517922L/void',
  headers={'Content-Type': 'application/json'}
)
print('Void result:', void_response.json())
# Expected: {"id":"8AA831015G517922L","status":"VOIDED"}

# Test voiding already captured authorization (should fail)
captured_void_response = requests.post(
  'http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void',
  headers={'Content-Type': 'application/json'}
)
print('Error result:', captured_void_response.json())
# Expected: {"error":"Cannot void - already captured. Use refund instead."}
```

```java Java lines expandable theme={null}
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();

// Test voiding an authorization
HttpRequest voidRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/authorizations/8AA831015G517922L/void"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.noBody())
  .build();

HttpResponse<String> voidResponse = client.send(
  voidRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Void result: " + voidResponse.body());
// Expected: {"id":"8AA831015G517922L","status":"VOIDED"}

// Test voiding already captured authorization (should fail)
HttpRequest capturedVoidRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.noBody())
  .build();

HttpResponse<String> capturedVoidResponse = client.send(
  capturedVoidRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Error result: " + capturedVoidResponse.body());
// Expected: {"error":"Cannot void - already captured. Use refund instead."}
```

```php PHP lines expandable theme={null}
<?php
// Test voiding an authorization
$voidResponse = file_get_contents(
  'http://localhost:3000/api/authorizations/8AA831015G517922L/void',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json'
    ]
  ])
);
echo "Void result: " . $voidResponse . "\n";
// Expected: {"id":"8AA831015G517922L","status":"VOIDED"}

// Test voiding already captured authorization (should fail)
$capturedVoidResponse = file_get_contents(
  'http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json'
    ]
  ])
);
echo "Error result: " . $capturedVoidResponse . "\n";
// Expected: {"error":"Cannot void - already captured. Use refund instead."}
```

```ruby Ruby lines expandable theme={null}
require 'net/http'
require 'json'

# Test voiding an authorization
uri = URI('http://localhost:3000/api/authorizations/8AA831015G517922L/void')
void_request = Net::HTTP::Post.new(uri)
void_request['Content-Type'] = 'application/json'

void_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(void_request)
end
puts "Void result: #{void_response.body}"
# Expected: {"id":"8AA831015G517922L","status":"VOIDED"}

# Test voiding already captured authorization (should fail)
captured_uri = URI('http://localhost:3000/api/authorizations/CAPTURED_AUTH_ID/void')
captured_void_request = Net::HTTP::Post.new(captured_uri)
captured_void_request['Content-Type'] = 'application/json'

captured_void_response = Net::HTTP.start(captured_uri.hostname, captured_uri.port) do |http|
  http.request(captured_void_request)
end
puts "Error result: #{captured_void_response.body}"
# Expected: {"error":"Cannot void - already captured. Use refund instead."}
```

</CodeGroup>

## Best practices

- **Void promptly:** Cancel authorizations immediately when an order won't be fulfilled to release customer funds. Don't let an authorization expire.
- **Void before capture:** Always void instead of refund when possible. Voiding can save up to 3% in processing fees.
- **Automate cancellations:** Trigger voids automatically for out-of-stock scenarios or fraud detection.
- **Handle timing:** Authorizations expire after 3 days (standard) or 29 days (honor period).

## Important details

- **Void vs. refund:** Void cancels an authorization before capture. Refund returns money after a payment has been captured. Voiding saves processing fees.
- **Finding authorization IDs:** You need the authorization ID to void, not the order ID. The authorization ID is returned when you create an order with `AUTHORIZE` intent. Store this value in your database immediately.
- **All-or-nothing operation:** You cannot partially void an authorization. Voids cancel the entire authorized amount.
- **Voided authorizations cannot be captured:** Once voided, an authorization is permanently cancelled and cannot be captured. Attempting to capture will fail with an error.
- **Fund release time:** In sandbox mode, funds release immediately. In production, funds can take up to 24 hours depending on the customer's bank.

## Test your integration

- Create test authorizations with `AUTHORIZE` intent.
- Test at different intervals: immediately after authorization, after 1 day, and after 3 days.
- Verify funds are released in the sandbox buyer account after voiding.

### Standard testing

| Test scenario            | Setup                          | Expected result                 |
| :----------------------- | :----------------------------- | :------------------------------ |
| Void fresh authorization | Default settings               | Status: `VOIDED` returned       |
| Void after capture       | Capture first                  | Error: Already captured         |
| Void already voided      | Void twice                     | Error: Already voided           |
| Void after 3 days        | Wait 3 days post-authorization | Success if honor period enabled |

### Negative testing

For negative testing:

1. Make sure to enable negative testing in your sandbox business account as described in the [quick start prerequisites](/payments/methods/paypal/integrate#prerequisites).
2. In the `.env` file, set `ENABLE_NEGATIVE_TESTING=true` and set `NEGATIVE_TEST_TYPE` to one of the error codes in the table.
3. Restart the server after changing the `.env` file: `node server.js`.

| Test scenario              | Error code              | Expected result                |
| :------------------------- | :---------------------- | :----------------------------- |
| Void expired authorization | `AUTHORIZATION_EXPIRED` | Error: Authorization expired   |
| Void not found             | `RESOURCE_NOT_FOUND`    | Error: Authorization not found |
| Permission denied          | `PERMISSION_DENIED`     | Error: not authorized to void  |
| Internal server error      | `INTERNAL_SERVER_ERROR` | 500 error returned             |

## Go-live checklist

- Test void flow in sandbox with real authorization IDs.
- Implement void reason tracking.
- Set up customer cancellation notifications.
- Train support team on void vs refund scenarios.
- Configure automatic void triggers, such as out of inventory or a fraudulent transaction.
- Monitor void success rates.
- Test with real \$1 authorization and void it.

## Post-launch monitoring

These values are suggested monitoring thresholds for your integration, not performance guarantees from PayPal.

| Metric               | Target      | Action if below target             |
| :------------------- | :---------- | :--------------------------------- |
| Void success rate    | 99%         | Check for expired authorizations.  |
| Time to void         | \<1 hour    | Automate cancellation workflow.    |
| Void vs refund ratio | 80% void    | Train team to void before capture. |
| Failed void rate     | \<1%        | Review error patterns.             |
| API response time    | \<2 seconds | Check PayPal API status.           |
