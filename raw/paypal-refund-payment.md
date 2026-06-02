<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/refund -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Refund a payment

Refund captured payments to customers after an initial transaction. Common scenarios include:

- Customer returns a product or requests a refund from a service
- Customer cancels an order after payment
- Customer requests a partial refund

This integration uses the Payments API v2 to process full or partial refunds with the capture ID from the original payment. Add refund endpoints to your existing PayPal integration with comprehensive error handling and negative testing capabilities.

<Tip>
  If you've [authorized a payment but not captured it yet](/payments/methods/paypal/overview#authorization-vs-capture), use [void instead of refund to avoid processing fees](/payments/methods/paypal/void-an-authorization).
</Tip>

## Prerequisites

- Complete [the quick start PayPal integration](/payments/methods/paypal/integrate).
- You have a capture ID from the original payment transaction.
- You have a database or system to track payment and refund history.

## Integrate server side

Add the following to your existing server file from the quick start integration.

<CodeGroup>
  ```bash cURL expandable lines theme={null}
  # Refund a captured payment
  curl -X POST https://api-m.sandbox.paypal.com/v2/payments/captures/CAPTURE_ID/refund \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{
      "amount": {
        "value": "25.00",
        "currency_code": "USD"
      },
      "note_to_payer": "Refund processed"
    }'

# Get refund status

curl -X GET https://api-m.sandbox.paypal.com/v2/payments/refunds/REFUND_ID \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN"

````

```javascript Node.js lines expandable theme={null}
// Add these endpoints to your existing server.js from the quick start integration
// The PayPal client and addNegativeTesting helper are already configured

// Process refund
app.post('/api/captures/:captureID/refund', async (req, res) => {
  const request = new paypal.payments.CapturesRefundRequest(req.params.captureID);

  // Optional: Set refund amount (if not set, refunds full amount)
  if (req.body.amount) {
    request.requestBody({
      amount: {
        value: req.body.amount,
        currency_code: 'USD'
      },
      note_to_payer: req.body.note || 'Refund processed'
    });
  }

  // Apply negative testing if enabled (reuse helper from base integration)
  addNegativeTesting(request);

  try {
    const refund = await client.execute(request);
    res.json({
      id: refund.result.id,
      status: refund.result.status,
      amount: refund.result.amount.value
    });
  } catch (err) {
    // Handle specific refund errors
    if (err.statusCode === 422) {
      const errorDetail = err.details?.[0];
      if (errorDetail?.issue === 'CAPTURE_FULLY_REFUNDED') {
        res.status(400).json({
          error: 'Cannot refund - already refunded. Check capture status.',
          captureId: req.params.captureID
        });
      } else if (errorDetail?.issue === 'REFUND_AMOUNT_EXCEEDED') {
        res.status(400).json({
          error: 'Refund amount exceeds available balance',
          maxRefundable: errorDetail.description
        });
      } else {
        res.status(400).json({
          error: 'Invalid refund request'
        });
      }
    } else {
      res.status(500).json({
        error: err.message
      });
    }
  }
});

// Get refund status (optional but useful)
app.get('/api/refunds/:refundID', async (req, res) => {
  const request = new paypal.payments.RefundsGetRequest(req.params.refundID);
  addNegativeTesting(request);

  try {
    const refund = await client.execute(request);
    res.json({
      id: refund.result.id,
      status: refund.result.status,
      amount: refund.result.amount.value
    });
  } catch (err) {
    res.status(404).json({
      error: 'Refund not found'
    });
  }
});
````

```python Python lines expandable theme={null}
from paypalrestsdk import Api, Refund, Capture
import os

# Configure PayPal SDK
api = Api({
  'mode': 'sandbox',
  'client_id': os.environ['PAYPAL_CLIENT_ID'],
  'client_secret': os.environ['PAYPAL_CLIENT_SECRET']
})

# Process refund
@app.route('/api/captures/<capture_id>/refund', methods=['POST'])
def process_refund(capture_id):
  try:
    refund_data = {
      "amount": {
        "value": request.json.get('amount'),
        "currency": "USD"
      },
      "note_to_payer": request.json.get('note', 'Refund processed')
    }

    # Create refund
    refund = Refund({
      "capture_id": capture_id,
      **refund_data
    })

    if refund.create():
      return jsonify({
        "id": refund.id,
        "status": refund.state,
        "amount": refund.amount.total
      })
    else:
      # Handle errors
      error = refund.error
      if error.get('name') == 'CAPTURE_FULLY_REFUNDED':
        return jsonify({
          "error": "Cannot refund - already refunded"
        }), 400
      elif error.get('name') == 'REFUND_AMOUNT_EXCEEDED':
        return jsonify({
          "error": "Refund amount exceeds available balance"
        }), 400
      else:
        return jsonify({"error": error.get('message')}), 500

  except Exception as e:
    return jsonify({"error": str(e)}), 500

# Get refund status
@app.route('/api/refunds/<refund_id>', methods=['GET'])
def get_refund_status(refund_id):
  try:
    refund = Refund.find(refund_id)
    return jsonify({
      "id": refund.id,
      "status": refund.state,
      "amount": refund.amount.total
    })
  except Exception as e:
    return jsonify({"error": "Refund not found"}), 404
```

```java Java lines expandable theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.payments.CapturesRefundRequest;
import com.paypal.payments.RefundsGetRequest;
import com.paypal.payments.Refund;

HttpClient httpClient = new PayPalHttpClient(
  new SandboxEnvironment(
    System.getenv("PAYPAL_CLIENT_ID"),
    System.getenv("PAYPAL_CLIENT_SECRET")
  )
);

// Process refund
@PostMapping("/api/captures/{captureId}/refund")
public ResponseEntity<?> processRefund(
  @PathVariable String captureId,
  @RequestBody RefundRequest refundRequest
) {
  try {
    CapturesRefundRequest request = new CapturesRefundRequest(captureId);

    // Set refund amount if provided
    if (refundRequest.getAmount() != null) {
      RefundRequestBody body = new RefundRequestBody()
        .amount(new Money()
          .value(refundRequest.getAmount())
          .currencyCode("USD")
        )
        .noteToPayer(refundRequest.getNote() != null ?
          refundRequest.getNote() : "Refund processed"
        );
      request.requestBody(body);
    }

    HttpResponse<Refund> response = httpClient.execute(request);
    Refund refund = response.result();

    return ResponseEntity.ok(Map.of(
      "id", refund.id(),
      "status", refund.status(),
      "amount", refund.amount().value()
    ));

  } catch (HttpClientException e) {
    if (e.statusCode() == 422) {
      String issue = extractIssue(e);
      if ("CAPTURE_FULLY_REFUNDED".equals(issue)) {
        return ResponseEntity.badRequest().body(
          Map.of("error", "Cannot refund - already refunded")
        );
      } else if ("REFUND_AMOUNT_EXCEEDED".equals(issue)) {
        return ResponseEntity.badRequest().body(
          Map.of("error", "Refund amount exceeds available balance")
        );
      }
    }
    return ResponseEntity.status(500).body(
      Map.of("error", e.getMessage())
    );
  }
}

// Get refund status
@GetMapping("/api/refunds/{refundId}")
public ResponseEntity<?> getRefundStatus(@PathVariable String refundId) {
  try {
    RefundsGetRequest request = new RefundsGetRequest(refundId);
    HttpResponse<Refund> response = httpClient.execute(request);
    Refund refund = response.result();

    return ResponseEntity.ok(Map.of(
      "id", refund.id(),
      "status", refund.status(),
      "amount", refund.amount().value()
    ));
  } catch (Exception e) {
    return ResponseEntity.status(404).body(
      Map.of("error", "Refund not found")
    );
  }
}
```

```php PHP lines expandable theme={null}
<?php
use PayPalCheckoutSdk\Core\SandboxEnvironment;
use PayPalCheckoutSdk\Core\PayPalHttpClient;
use PayPalCheckoutSdk\Payments\CapturesRefundRequest;
use PayPalCheckoutSdk\Payments\RefundsGetRequest;

$environment = new SandboxEnvironment(
  getenv('PAYPAL_CLIENT_ID'),
  getenv('PAYPAL_CLIENT_SECRET')
);
$client = new PayPalHttpClient($environment);

// Process refund
$app->post('/api/captures/{captureID}/refund', function ($request, $response, $args) use ($client) {
  $captureID = $args['captureID'];
  $body = $request->getParsedBody();

  $refundRequest = new CapturesRefundRequest($captureID);

  // Set refund amount if provided
  if (isset($body['amount'])) {
    $refundRequest->body = [
      "amount" => [
        "value" => $body['amount'],
        "currency_code" => "USD"
      ],
      "note_to_payer" => $body['note'] ?? "Refund processed"
    ];
  }

  try {
    $refundResponse = $client->execute($refundRequest);
    $refund = $refundResponse->result;

    $response->getBody()->write(json_encode([
      "id" => $refund->id,
      "status" => $refund->status,
      "amount" => $refund->amount->value
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    $statusCode = $e->statusCode;
    $errorData = json_decode($e->getMessage(), true);

    if ($statusCode === 422) {
      $issue = $errorData['details'][0]['issue'] ?? '';
      if ($issue === 'CAPTURE_FULLY_REFUNDED') {
        $response->getBody()->write(json_encode([
          "error" => "Cannot refund - already refunded"
        ]));
        return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
      } else if ($issue === 'REFUND_AMOUNT_EXCEEDED') {
        $response->getBody()->write(json_encode([
          "error" => "Refund amount exceeds available balance"
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

// Get refund status
$app->get('/api/refunds/{refundID}', function ($request, $response, $args) use ($client) {
  $refundID = $args['refundID'];

  try {
    $refundRequest = new RefundsGetRequest($refundID);
    $refundResponse = $client->execute($refundRequest);
    $refund = $refundResponse->result;

    $response->getBody()->write(json_encode([
      "id" => $refund->id,
      "status" => $refund->status,
      "amount" => $refund->amount->value
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (Exception $e) {
    $response->getBody()->write(json_encode([
      "error" => "Refund not found"
    ]));
    return $response->withStatus(404)->withHeader('Content-Type', 'application/json');
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

# Process refund
post '/api/captures/:capture_id/refund' do
  capture_id = params['capture_id']
  request_body = JSON.parse(request.body.read)

  begin
    refund_data = {
      amount: {
        value: request_body['amount'],
        currency_code: 'USD'
      },
      note_to_payer: request_body['note'] || 'Refund processed'
    }

    # Create refund
    refund = PayPal::SDK::PaymentsApi::Refund.new(
      capture_id: capture_id,
      **refund_data
    )

    if refund.create
      content_type :json
      {
        id: refund.id,
        status: refund.status,
        amount: refund.amount.value
      }.to_json
    else
      error = refund.error
      if error['name'] == 'CAPTURE_FULLY_REFUNDED'
        status 400
        { error: 'Cannot refund - already refunded' }.to_json
      elsif error['name'] == 'REFUND_AMOUNT_EXCEEDED'
        status 400
        { error: 'Refund amount exceeds available balance' }.to_json
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

# Get refund status
get '/api/refunds/:refund_id' do
  refund_id = params['refund_id']

  begin
    refund = PayPal::SDK::PaymentsApi::Refund.find(refund_id)
    content_type :json
    {
      id: refund.id,
      status: refund.status,
      amount: refund.amount.value
    }.to_json
  rescue => e
    status 404
    { error: 'Refund not found' }.to_json
  end
end
```

</CodeGroup>

### Test endpoints

<Info>
  Endpoints:

- [`/v2/payments/captures/{capture_id}/refund`](/reference/api/rest/captures/refund-captured-payment)
- [`/v2/payments/refunds/{refund_id}`](/reference/api/rest/refunds/show-refund-details)
  </Info>

<CodeGroup>
  ```bash cURL theme={null}
  # Test full refund (replace with actual capture ID)
  curl -X POST http://localhost:3000/api/captures/3C679366HH908993F/refund \
    -H "Content-Type: application/json"

# Expected success response:

# {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

# Test partial refund with note

curl -X POST http://localhost:3000/api/captures/3C679366HH908993F/refund \
 -H "Content-Type: application/json" \
 -d '{"amount": "25.00", "note": "Partial refund for damaged item"}'

# Test refund status check

curl http://localhost:3000/api/refunds/WH4YN4SYEDZJA

# Expected response:

# {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}

````

```javascript Node.js lines expandable theme={null}
// Test full refund
const fullRefundResponse = await fetch('http://localhost:3000/api/captures/3C679366HH908993F/refund', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' }
});
const fullRefund = await fullRefundResponse.json();
console.log('Full refund:', fullRefund);
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

// Test partial refund with note
const partialRefundResponse = await fetch('http://localhost:3000/api/captures/3C679366HH908993F/refund', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    amount: '25.00',
    note: 'Partial refund for damaged item'
  })
});
const partialRefund = await partialRefundResponse.json();
console.log('Partial refund:', partialRefund);

// Test refund status check
const statusResponse = await fetch('http://localhost:3000/api/refunds/WH4YN4SYEDZJA');
const status = await statusResponse.json();
console.log('Refund status:', status);
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}
````

```python Python theme={null}
import requests

# Test full refund
full_refund_response = requests.post(
  'http://localhost:3000/api/captures/3C679366HH908993F/refund',
  headers={'Content-Type': 'application/json'}
)
print('Full refund:', full_refund_response.json())
# Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

# Test partial refund with note
partial_refund_response = requests.post(
  'http://localhost:3000/api/captures/3C679366HH908993F/refund',
  headers={'Content-Type': 'application/json'},
  json={
    'amount': '25.00',
    'note': 'Partial refund for damaged item'
  }
)
print('Partial refund:', partial_refund_response.json())

# Test refund status check
status_response = requests.get(
  'http://localhost:3000/api/refunds/WH4YN4SYEDZJA'
)
print('Refund status:', status_response.json())
# Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}
```

```java Java theme={null}
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();

// Test full refund
HttpRequest fullRefundRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/captures/3C679366HH908993F/refund"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.noBody())
  .build();

HttpResponse<String> fullRefundResponse = client.send(
  fullRefundRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Full refund: " + fullRefundResponse.body());
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

// Test partial refund with note
String partialRefundBody = "{\"amount\":\"25.00\",\"note\":\"Partial refund for damaged item\"}";
HttpRequest partialRefundRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/captures/3C679366HH908993F/refund"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.ofString(partialRefundBody))
  .build();

HttpResponse<String> partialRefundResponse = client.send(
  partialRefundRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Partial refund: " + partialRefundResponse.body());

// Test refund status check
HttpRequest statusRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/refunds/WH4YN4SYEDZJA"))
  .GET()
  .build();

HttpResponse<String> statusResponse = client.send(
  statusRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Refund status: " + statusResponse.body());
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}
```

```php PHP theme={null}
<?php
// Test full refund
$fullRefundResponse = file_get_contents(
  'http://localhost:3000/api/captures/3C679366HH908993F/refund',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json'
    ]
  ])
);
echo "Full refund: " . $fullRefundResponse . "\n";
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

// Test partial refund with note
$partialRefundData = json_encode([
  'amount' => '25.00',
  'note' => 'Partial refund for damaged item'
]);

$partialRefundResponse = file_get_contents(
  'http://localhost:3000/api/captures/3C679366HH908993F/refund',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json',
      'content' => $partialRefundData
    ]
  ])
);
echo "Partial refund: " . $partialRefundResponse . "\n";

// Test refund status check
$statusResponse = file_get_contents(
  'http://localhost:3000/api/refunds/WH4YN4SYEDZJA'
);
echo "Refund status: " . $statusResponse . "\n";
// Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}
```

```ruby Ruby lines expandable theme={null}
require 'net/http'
require 'json'

# Test full refund
uri = URI('http://localhost:3000/api/captures/3C679366HH908993F/refund')
full_refund_request = Net::HTTP::Post.new(uri)
full_refund_request['Content-Type'] = 'application/json'

full_refund_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(full_refund_request)
end
puts "Full refund: #{full_refund_response.body}"
# Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"100.00"}

# Test partial refund with note
partial_refund_request = Net::HTTP::Post.new(uri)
partial_refund_request['Content-Type'] = 'application/json'
partial_refund_request.body = {
  amount: '25.00',
  note: 'Partial refund for damaged item'
}.to_json

partial_refund_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(partial_refund_request)
end
puts "Partial refund: #{partial_refund_response.body}"

# Test refund status check
status_uri = URI('http://localhost:3000/api/refunds/WH4YN4SYEDZJA')
status_response = Net::HTTP.get_response(status_uri)
puts "Refund status: #{status_response.body}"
# Expected: {"id":"WH4YN4SYEDZJA","status":"COMPLETED","amount":"25.00"}
```

</CodeGroup>

### Best practices

Use the following best practices to ensure refunds are processed safely, accurately, and in compliance with operational and regulatory requirements.

- **Store capture IDs:** Always save capture IDs from successful payments in your database for future refunds.
- **Use idempotency keys:** Use idempotency keys when processing refunds to avoid duplicate refunds in case of network issues.
- **Validate refund amounts:** Check the refund amount doesn't exceed original payment or remaining refundable balance.
- **Log all refunds:** Keep an audit trail of who initiated refunds, when, and why. This is critical for compliance.
- **Provide refund notes:** Include clear explanation in the `note_to_payer` field for customer clarity.
- **Handle partial refunds:** Track cumulative refunded amounts to prevent over-refunding.
- **Process refunds within 180 days:** Process refunds within 180 days of the original capture date. Your customer's bank may have shorter windows. After extended periods, manual intervention through PayPal support may be required.
- **Implement approval workflows:** Processed refunds cannot be cancelled. Build approval workflows for refunds over a certain threshold.
- **Have backup manual refund process:** Have a manual refund process as backup. Log failed attempts and escalate to PayPal support with the error details.

## Important details

- **Find capture IDs:** The capture ID is returned as `capture.result.id` when you capture a payment. Store this value in your database immediately. You'll need it for any future refunds on that transaction.
- **Refund processing time:** In sandbox mode, refunds complete instantly. In production, customers see refunds in their account within 3-5 business days, though timing varies by payment method.
- **Webhook notifications:** Set up webhooks to receive `PAYMENT.CAPTURE.REFUNDED` events for real-time status updates. Always verify webhook signatures for security.
- **No refunds to different payment methods:** Refunds always go back to the customer's original payment method.
- **No currency conversion:** Always refund in the same currency as the original payment. PayPal handles any exchange rate adjustments automatically.

## Test your integration

Make sure you have [sandbox account credentials for both buyer and seller roles](/developer/how-to/api/get-started#3-get-sandbox-account-credentials). Complete a test payment to get a valid capture ID.

### Standard testing

| Test scenario                   | Setup            | Expected result                    |
| :------------------------------ | :--------------- | :--------------------------------- |
| Full refund success             | Default settings | Entire payment amount refunded.    |
| Partial refund success          | Default settings | Specified amount refunded.         |
| Multiple partial refund success | Default settings | Each refunds succeeds until limit. |
| Invalid capture ID              | Fake IDL XXX123  | 404 error: capture not found.      |
| Refund after 3 days             | Wait 3 days      | Success if within 180 days         |

### Negative testing

For negative testing:

1. Make sure to enable negative testing in your sandbox business account as described in the [quick start prerequisites](/payments/methods/paypal/integrate#prerequisites).
2. In the `.env` file, set `ENABLE_NEGATIVE_TESTING=true` and set `NEGATIVE_TEST_TYPE` to one of the error codes in the table.
3. Restart the server after changing the `.env` file: `node server.js`.

| Test scenario          | Error code                          | Expected result                       |
| :--------------------- | :---------------------------------- | :------------------------------------ |
| Exceed original amount | `REFUND_AMOUNT_EXCEEDED`            | Error: refund amount exceeds capture. |
| Already fully refunded | `CAPTURE_FULLY_REFUNDED`            | Error: already fully refunded.        |
| Refund after 180 days  | `REFUND_NOT_ALLOWED_AFTER_180_DAYS` | Error: refund period expired.         |
| Permission denied      | `PERMISSION_DENIED`                 | 403 error: no refund permission.      |
| Internal server error  | `INTERNAL_SERVER_ERROR`             | Error: 500 error occurred at refund.  |

## Go-live checklist

- Test full and partial refunds in sandbox.
- Implement refund approval workflow.
- Set up refund logging and audit trail.
- Add authentication to refund endpoints.
- Configure refund permission roles.
- Set up webhook listeners for refund events.
- Test with real \$1 payment and refund it.

## Post-launch monitoring

These values are suggested monitoring thresholds for your integration, not performance guarantees from PayPal.

| Metric                  | Target      | Action if below target                         |
| :---------------------- | :---------- | :--------------------------------------------- |
| Refund success rate     | 98%         | Check API errors and validate capture IDs.     |
| Refund processing time  | \<5 seconds | Optimize database queries.                     |
| Failed refund rate      | \<2%        | Review error logs, check amounts.              |
| Refund-to-payment ratio | \<5%        | Analyze if high - may indicate quality issues. |
| API response time       | \<2 seconds | Check PayPal API status.                       |
