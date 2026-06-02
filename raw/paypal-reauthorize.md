<!-- Source URL: https://docs.paypal.ai/payments/methods/paypal/reauthorize -->
<!-- Fetched: 2026-04-17 -->

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.paypal.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Extend an authorization

Extend the validity of an existing authorization when fulfillment takes longer than the initial authorization period. In the United States, authorizations are valid for 3 days, and up to 29 days in other regions. Reauthorization allows the merchant to keep funds available without requiring the buyer to re-approve payment.

Common scenarios include:

- Custom or made-to-order items with extended production times
- Backorders with delayed inventory availability
- International shipments with longer fulfillment windows
- Pre-orders for unreleased products
- Fulfillment delays due to operational or external factors
- High-value orders requiring additional verification before shipping

This integration uses the Payments API v2 to reauthorize an existing authorization and generate a new authorization with a refreshed expiration date.

## Prerequisites

- Complete [the quick start PayPal integration](/payments/methods/paypal/integrate).
- An existing authorization ID that is past the initial honor period (3+ days old).
- A server environment capable of securely calling PayPal REST APIs.

## Integrate server side

Add the following endpoint to your existing server file from the quick start integration.

<CodeGroup>
  ```bash cURL lines expandable theme={null}
  # Reauthorize for the same amount
  curl -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/AUTHORIZATION_ID/reauthorize \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ACCESS_TOKEN" \
    -d '{}'

# Reauthorize for a higher amount (up to 115% of original)

curl -X POST https://api-m.sandbox.paypal.com/v2/payments/authorizations/AUTHORIZATION_ID/reauthorize \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN" \
 -d '{
"amount": {
"currency_code": "USD",
"value": "115.00"
}
}'

# Get reauthorization status

curl -X GET https://api-m.sandbox.paypal.com/v2/payments/authorizations/NEW_AUTHORIZATION_ID \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer ACCESS_TOKEN"

````

```javascript Node.js lines expandable theme={null}
// Add endpoint for reauthorization
app.post('/api/paypal/reauthorize-payment', async (req, res) => {
  const { authorizationID, amount } = req.body;
  if (!authorizationID) {
    return res.status(400).json({ error: 'Missing authorizationID' });
  }
  const accessToken = await getPayPalAccessToken();
  const apiBase = process.env.PAYPAL_API_BASE || 'https://api-m.sandbox.paypal.com';
  const reauthorizeRequest = {
    amount: amount || undefined // Optional: up to 115% of original amount
  };
  try {
    const response = await fetch(
      `${apiBase}/v2/payments/authorizations/${authorizationID}/reauthorize`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${accessToken}`,
        },
        body: JSON.stringify(reauthorizeRequest),
      }
    );
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Reauthorization failed');
    }
    const reauthorization = await response.json();
    res.json({
      status: 'REAUTHORIZED',
      newAuthorizationId: reauthorization.id,
      amount: reauthorization.amount,
      expirationTime: reauthorization.expiration_time
    });
  } catch (err) {
    if (err.message.includes('AUTHORIZATION_ALREADY_COMPLETED')) {
      res.status(400).json({ error: 'Authorization already captured or voided' });
    } else if (err.message.includes('REAUTHORIZE_NOT_ALLOWED')) {
      res.status(400).json({ error: 'Reauthorization not allowed (too soon or expired)' });
    } else {
      res.status(500).json({ error: err.message });
    }
  }
});
````

```python Python lines expandable theme={null}
from paypalrestsdk import Api, Authorization
import os

# Configure PayPal SDK
api = Api({
  'mode': 'sandbox',
  'client_id': os.environ['PAYPAL_CLIENT_ID'],
  'client_secret': os.environ['PAYPAL_CLIENT_SECRET']
})

# Process reauthorization
@app.route('/api/paypal/reauthorize-payment', methods=['POST'])
def reauthorize_payment():
  try:
    authorization_id = request.json.get('authorizationID')
    amount = request.json.get('amount')

    if not authorization_id:
      return jsonify({'error': 'Missing authorizationID'}), 400

    # Get authorization
    authorization = Authorization.find(authorization_id)

    # Reauthorize with optional amount
    reauthorize_data = {}
    if amount:
      reauthorize_data['amount'] = {
        'value': amount['value'],
        'currency_code': amount.get('currency_code', 'USD')
      }

    # Execute reauthorization
    reauthorization = authorization.reauthorize(reauthorize_data)

    if reauthorization.success():
      return jsonify({
        'status': 'REAUTHORIZED',
        'newAuthorizationId': reauthorization.id,
        'amount': reauthorization.amount,
        'expirationTime': reauthorization.expiration_time
      })
    else:
      error = reauthorization.error
      if error.get('name') == 'AUTHORIZATION_ALREADY_COMPLETED':
        return jsonify({
          'error': 'Authorization already captured or voided'
        }), 400
      elif error.get('name') == 'REAUTHORIZE_NOT_ALLOWED':
        return jsonify({
          'error': 'Reauthorization not allowed (too soon or expired)'
        }), 400
      else:
        return jsonify({'error': error.get('message')}), 500

  except Exception as e:
    return jsonify({'error': str(e)}), 500
```

```java Java lines expandable theme={null}
import com.paypal.core.PayPalEnvironment;
import com.paypal.core.PayPalHttpClient;
import com.paypal.payments.AuthorizationsReauthorizeRequest;
import com.paypal.payments.Authorization;
import com.paypal.payments.Money;

HttpClient httpClient = new PayPalHttpClient(
  new SandboxEnvironment(
    System.getenv("PAYPAL_CLIENT_ID"),
    System.getenv("PAYPAL_CLIENT_SECRET")
  )
);

// Process reauthorization
@PostMapping("/api/paypal/reauthorize-payment")
public ResponseEntity<?> reauthorizePayment(
  @RequestBody ReauthorizeRequest reauthorizeRequest
) {
  try {
    String authorizationId = reauthorizeRequest.getAuthorizationID();

    if (authorizationId == null || authorizationId.isEmpty()) {
      return ResponseEntity.badRequest().body(
        Map.of("error", "Missing authorizationID")
      );
    }

    AuthorizationsReauthorizeRequest request =
      new AuthorizationsReauthorizeRequest(authorizationId);

    // Set reauthorization amount if provided (up to 115% of original)
    if (reauthorizeRequest.getAmount() != null) {
      ReauthorizeRequestBody body = new ReauthorizeRequestBody()
        .amount(new Money()
          .value(reauthorizeRequest.getAmount().getValue())
          .currencyCode(reauthorizeRequest.getAmount()
            .getCurrencyCode() != null ?
            reauthorizeRequest.getAmount().getCurrencyCode() : "USD")
        );
      request.requestBody(body);
    }

    HttpResponse<Authorization> response = httpClient.execute(request);
    Authorization reauthorization = response.result();

    return ResponseEntity.ok(Map.of(
      "status", "REAUTHORIZED",
      "newAuthorizationId", reauthorization.id(),
      "amount", reauthorization.amount(),
      "expirationTime", reauthorization.expirationTime()
    ));

  } catch (HttpClientException e) {
    String issue = extractIssue(e);
    if ("AUTHORIZATION_ALREADY_COMPLETED".equals(issue)) {
      return ResponseEntity.badRequest().body(
        Map.of("error", "Authorization already captured or voided")
      );
    } else if ("REAUTHORIZE_NOT_ALLOWED".equals(issue)) {
      return ResponseEntity.badRequest().body(
        Map.of("error", "Reauthorization not allowed (too soon or expired)")
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
use PayPalCheckoutSdk\Payments\AuthorizationsReauthorizeRequest;

$environment = new SandboxEnvironment(
  getenv('PAYPAL_CLIENT_ID'),
  getenv('PAYPAL_CLIENT_SECRET')
);
$client = new PayPalHttpClient($environment);

// Process reauthorization
$app->post('/api/paypal/reauthorize-payment', function ($request, $response) use ($client) {
  $body = $request->getParsedBody();
  $authorizationID = $body['authorizationID'] ?? null;

  if (!$authorizationID) {
    $response->getBody()->write(json_encode([
      'error' => 'Missing authorizationID'
    ]));
    return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
  }

  $reauthorizeRequest = new AuthorizationsReauthorizeRequest($authorizationID);

  // Set reauthorization amount if provided (up to 115% of original)
  if (isset($body['amount'])) {
    $reauthorizeRequest->body = [
      'amount' => [
        'value' => $body['amount']['value'],
        'currency_code' => $body['amount']['currency_code'] ?? 'USD'
      ]
    ];
  }

  try {
    $reauthorizeResponse = $client->execute($reauthorizeRequest);
    $reauthorization = $reauthorizeResponse->result;

    $response->getBody()->write(json_encode([
      'status' => 'REAUTHORIZED',
      'newAuthorizationId' => $reauthorization->id,
      'amount' => $reauthorization->amount,
      'expirationTime' => $reauthorization->expiration_time
    ]));
    return $response->withHeader('Content-Type', 'application/json');

  } catch (HttpException $e) {
    $statusCode = $e->statusCode;
    $errorData = json_decode($e->getMessage(), true);
    $issue = $errorData['details'][0]['issue'] ?? '';

    if ($issue === 'AUTHORIZATION_ALREADY_COMPLETED') {
      $response->getBody()->write(json_encode([
        'error' => 'Authorization already captured or voided'
      ]));
      return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
    } else if ($issue === 'REAUTHORIZE_NOT_ALLOWED') {
      $response->getBody()->write(json_encode([
        'error' => 'Reauthorization not allowed (too soon or expired)'
      ]));
      return $response->withStatus(400)->withHeader('Content-Type', 'application/json');
    }

    $response->getBody()->write(json_encode([
      'error' => $e->getMessage()
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

# Process reauthorization
post '/api/paypal/reauthorize-payment' do
  request_body = JSON.parse(request.body.read)
  authorization_id = request_body['authorizationID']

  if authorization_id.nil? || authorization_id.empty?
    status 400
    return { error: 'Missing authorizationID' }.to_json
  end

  begin
    # Get authorization
    authorization = PayPal::SDK::PaymentsApi::Authorization.find(authorization_id)

    # Prepare reauthorization data
    reauthorize_data = {}
    if request_body['amount']
      reauthorize_data[:amount] = {
        value: request_body['amount']['value'],
        currency_code: request_body['amount']['currency_code'] || 'USD'
      }
    end

    # Execute reauthorization
    reauthorization = authorization.reauthorize(reauthorize_data)

    if reauthorization.success?
      content_type :json
      {
        status: 'REAUTHORIZED',
        newAuthorizationId: reauthorization.id,
        amount: reauthorization.amount,
        expirationTime: reauthorization.expiration_time
      }.to_json
    else
      error = reauthorization.error
      if error['name'] == 'AUTHORIZATION_ALREADY_COMPLETED'
        status 400
        { error: 'Authorization already captured or voided' }.to_json
      elsif error['name'] == 'REAUTHORIZE_NOT_ALLOWED'
        status 400
        { error: 'Reauthorization not allowed (too soon or expired)' }.to_json
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

## Test endpoint

<Info>
  Endpoint: [`/v2/payments/authorizations/{authorization_id}/reauthorize`](/reference/api/rest/authorizations/reauthorize-authorized-payment)
</Info>

<CodeGroup>
  ```bash cURL lines expandable theme={null}
  # Reauthorize for the same amount
  curl -X POST http://localhost:3000/api/paypal/reauthorize-payment \
    -H "Content-Type: application/json" \
    -d '{"authorizationID": "5AB67890CD123456E"}'

# Expected success response:

# {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

# Reauthorize for a higher amount (up to 115% of original)

curl -X POST http://localhost:3000/api/paypal/reauthorize-payment \
 -H "Content-Type: application/json" \
 -d '{
"authorizationID": "5AB67890CD123456E",
"amount": {
"currency_code": "USD",
"value": "115.00"
}
}'

# Expected success response:

# {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}

````

```javascript Node.js lines expandable theme={null}
// Test reauthorize for the same amount
const sameAmountResponse = await fetch('http://localhost:3000/api/paypal/reauthorize-payment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    authorizationID: '5AB67890CD123456E'
  })
});
const sameAmount = await sameAmountResponse.json();
console.log('Reauthorized:', sameAmount);
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

// Test reauthorize for a higher amount (up to 115% of original)
const higherAmountResponse = await fetch('http://localhost:3000/api/paypal/reauthorize-payment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    authorizationID: '5AB67890CD123456E',
    amount: {
      currency_code: 'USD',
      value: '115.00'
    }
  })
});
const higherAmount = await higherAmountResponse.json();
console.log('Reauthorized with higher amount:', higherAmount);
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}
````

```python Python lines expandable theme={null}
import requests

# Test reauthorize for the same amount
same_amount_response = requests.post(
  'http://localhost:3000/api/paypal/reauthorize-payment',
  headers={'Content-Type': 'application/json'},
  json={'authorizationID': '5AB67890CD123456E'}
)
print('Reauthorized:', same_amount_response.json())
# Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

# Test reauthorize for a higher amount (up to 115% of original)
higher_amount_response = requests.post(
  'http://localhost:3000/api/paypal/reauthorize-payment',
  headers={'Content-Type': 'application/json'},
  json={
    'authorizationID': '5AB67890CD123456E',
    'amount': {
      'currency_code': 'USD',
      'value': '115.00'
    }
  }
)
print('Reauthorized with higher amount:', higher_amount_response.json())
# Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}
```

```java Java lines expandable theme={null}
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

HttpClient client = HttpClient.newHttpClient();

// Test reauthorize for the same amount
String sameAmountBody = "{\"authorizationID\":\"5AB67890CD123456E\"}";
HttpRequest sameAmountRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/paypal/reauthorize-payment"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.ofString(sameAmountBody))
  .build();

HttpResponse<String> sameAmountResponse = client.send(
  sameAmountRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Reauthorized: " + sameAmountResponse.body());
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

// Test reauthorize for a higher amount (up to 115% of original)
String higherAmountBody = "{\"authorizationID\":\"5AB67890CD123456E\",\"amount\":{\"currency_code\":\"USD\",\"value\":\"115.00\"}}";
HttpRequest higherAmountRequest = HttpRequest.newBuilder()
  .uri(URI.create("http://localhost:3000/api/paypal/reauthorize-payment"))
  .header("Content-Type", "application/json")
  .POST(HttpRequest.BodyPublishers.ofString(higherAmountBody))
  .build();

HttpResponse<String> higherAmountResponse = client.send(
  higherAmountRequest,
  HttpResponse.BodyHandlers.ofString()
);
System.out.println("Reauthorized with higher amount: " + higherAmountResponse.body());
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}
```

```php PHP lines expandable theme={null}
<?php
// Test reauthorize for the same amount
$sameAmountData = json_encode([
  'authorizationID' => '5AB67890CD123456E'
]);

$sameAmountResponse = file_get_contents(
  'http://localhost:3000/api/paypal/reauthorize-payment',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json',
      'content' => $sameAmountData
    ]
  ])
);
echo "Reauthorized: " . $sameAmountResponse . "\n";
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

// Test reauthorize for a higher amount (up to 115% of original)
$higherAmountData = json_encode([
  'authorizationID' => '5AB67890CD123456E',
  'amount' => [
    'currency_code' => 'USD',
    'value' => '115.00'
  ]
]);

$higherAmountResponse = file_get_contents(
  'http://localhost:3000/api/paypal/reauthorize-payment',
  false,
  stream_context_create([
    'http' => [
      'method' => 'POST',
      'header' => 'Content-Type: application/json',
      'content' => $higherAmountData
    ]
  ])
);
echo "Reauthorized with higher amount: " . $higherAmountResponse . "\n";
// Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}
```

```ruby Ruby lines expandable theme={null}
require 'net/http'
require 'json'

# Test reauthorize for the same amount
uri = URI('http://localhost:3000/api/paypal/reauthorize-payment')
same_amount_request = Net::HTTP::Post.new(uri)
same_amount_request['Content-Type'] = 'application/json'
same_amount_request.body = {
  authorizationID: '5AB67890CD123456E'
}.to_json

same_amount_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(same_amount_request)
end
puts "Reauthorized: #{same_amount_response.body}"
# Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"100.00"},"expirationTime":"2024-02-05T10:23:23Z"}

# Test reauthorize for a higher amount (up to 115% of original)
higher_amount_request = Net::HTTP::Post.new(uri)
higher_amount_request['Content-Type'] = 'application/json'
higher_amount_request.body = {
  authorizationID: '5AB67890CD123456E',
  amount: {
    currency_code: 'USD',
    value: '115.00'
  }
}.to_json

higher_amount_response = Net::HTTP.start(uri.hostname, uri.port) do |http|
  http.request(higher_amount_request)
end
puts "Reauthorized with higher amount: #{higher_amount_response.body}"
# Expected: {"status":"REAUTHORIZED","newAuthorizationId":"8CD12345EF678901A","amount":{"currency_code":"USD","value":"115.00"},"expirationTime":"2024-02-05T10:23:23Z"}
```

</CodeGroup>

## Best practices

- **Reauthorize within the valid window:** Reauthorization is allowed only between days 4-29 after the original authorization, depending on region.
- **Reauthorize only once:** Each authorization can be reauthorized a single time. If more time is required, create a new order.
- **Monitor authorization expiration:** Track expiration dates and trigger reauthorization before the authorization lapses.
- **Respect amount limits:** You can reauthorize for up to 115% of the original amount in most regions. Regional limits may vary.
- **Handle failures gracefully:** If reauthorization fails, void the original authorization and request a new payment from the customer.

## Important details

- **Authorization validity periods:** Authorizations are valid for 3 days in the US and up to 29 days in most other regions. After expiration, funds are automatically released to the customer.
- **Reauthorization timing window:** You can only reauthorize between days 4-29 after the initial authorization. Attempts before day 3 or after day 29 will fail.
- **Single reauthorization limit:** Each authorization can be reauthorized only once. If you need more time after reauthorization, void the authorization and create a new order.
- **No customer interaction required:** Reauthorization happens server-side without customer approval. However, consider notifying customers as a courtesy when extending payment holds.
- **Handling reauthorization failures:** If reauthorization fails, void the original authorization and request new payment from the customer. Common failures include insufficient funds, authorization already captured or voided, or attempting outside the valid window.

## Test your integration

Run the following standard tests on your integration.

| Test scenario                     | Setup                                                           | Expected result                                          |
| :-------------------------------- | :-------------------------------------------------------------- | :------------------------------------------------------- |
| Successful reauthorization        | Create authorization, wait 4+ days, reauthorize for same amount | New authorization created with a fresh expiration date.  |
| Reauthorize for higher amount     | Reauthorize for 110% of original amount                         | New authorization created for increased amount.          |
| Reauthorize too soon              | Attempt within 3 days of original authorization                 | Error: reauthorization not available yet.                |
| Reauthorize expired authorization | Attempt after 30+ days                                          | Error: authorization expired and cannot be reauthorized. |
| Reauthorize more than once        | Reauthorize successfully, then attempt again                    | Error: cannot reauthorize more than once.                |

## Go-live checklist

- Test reauthorization in sandbox using the time machine.
- Verify handling of amount limits (up to 115%).
- Test error handling for all reauthorization error cases.
- Implement authorization expiration monitoring.
- Switch to production API credentials.
