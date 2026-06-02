---
title: "GitHub: paypal/Payouts-PHP-SDK"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-payouts-php-sdk.md"
tags: [paypal, payouts, php, sdk, github]
---

## Summary

PayPal's official PHP SDK for the Payouts REST API. Wraps `POST /v1/payments/payouts` and related item/batch endpoints with a typed request class pattern. Handles OAuth 2.0 authentication automatically via `PayPalHttpClient`.

## Key Patterns

### Client setup

```php
use PaypalPayoutsSDK\Core\PayPalHttpClient;
use PaypalPayoutsSDK\Core\SandboxEnvironment;

$environment = new SandboxEnvironment($clientId, $clientSecret);
$client = new PayPalHttpClient($environment);
```

Use `ProductionEnvironment` for live. Credentials read from env vars.

### Create payout

```php
use PaypalPayoutsSDK\Payouts\PayoutsPostRequest;

$request = new PayoutsPostRequest();
$request->body = [
    'sender_batch_header' => ['email_subject' => 'Your payout'],
    'items' => [[
        'recipient_type' => 'EMAIL',
        'receiver' => 'recipient@example.com',
        'amount' => ['currency' => 'USD', 'value' => '1.00'],
        'sender_item_id' => 'item-001',
        'note' => 'Thanks!'
    ]]
];
$response = $client->execute($request);
// $response->result->batch_header->payout_batch_id
// $response->result->batch_header->batch_status
```

### Retrieve batch / item

```php
use PaypalPayoutsSDK\Payouts\PayoutsGetRequest;
use PaypalPayoutsSDK\Payouts\PayoutsItemGetRequest;
use PaypalPayoutsSDK\Payouts\PayoutsItemCancelRequest;

$response = $client->execute(new PayoutsGetRequest($batchId));
$response = $client->execute(new PayoutsItemGetRequest($itemId));
$response = $client->execute(new PayoutsItemCancelRequest($itemId));
```

### Error handling

```php
try {
    $response = $client->execute($request);
} catch (HttpException $e) {
    var_dump(json_decode($e->getMessage()));
}
```

## Request Classes (4)

| Class | Endpoint |
| --- | --- |
| `PayoutsPostRequest` | `POST /v1/payments/payouts` |
| `PayoutsGetRequest` | `GET /v1/payments/payouts/{batch_id}` |
| `PayoutsItemGetRequest` | `GET /v1/payments/payouts-item/{item_id}` |
| `PayoutsItemCancelRequest` | `POST /v1/payments/payouts-item/{item_id}/cancel` |

## Related Pages

- [[paypal-payouts]] — Payouts concept page
- [[source-paypal-payouts-overview]] — Full Payouts integration docs

## Raw Sources

- [[github-paypal-payouts-php-sdk]] — stub file pointing to detail directory
