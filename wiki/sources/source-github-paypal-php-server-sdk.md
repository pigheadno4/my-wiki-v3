---
title: "GitHub: paypal/PayPal-PHP-Server-SDK"
type: source
date_ingested: 2026-04-16
original_format: github-repo
raw_files:
  - "github-paypal-php-server-sdk.md"
tags: [paypal, php, server-sdk, orders, payments, vault, subscriptions, oauth]
---

## Summary

PayPal's official PHP server-side SDK (`paypal/paypal-server-sdk`). PHP equivalent of the TypeScript Server SDK — same 5 controllers, same API surface, builder pattern for client initialization. v2.2.0.

## Install

```bash
composer require "paypal/paypal-server-sdk:2.2.0"
```

## Client Initialization (Builder Pattern)

```php
use PaypalServerSdkLib\Environment;
use PaypalServerSdkLib\Authentication\ClientCredentialsAuthCredentialsBuilder;
use PaypalServerSdkLib\PaypalServerSdkClientBuilder;

$client = PaypalServerSdkClientBuilder::init()
    ->clientCredentialsAuthCredentials(
        ClientCredentialsAuthCredentialsBuilder::init(
            'OAuthClientId',
            'OAuthClientSecret'
        )
    )
    ->environment(Environment::SANDBOX)  // or Environment::PRODUCTION
    ->build();
```

## PHP-Specific Configuration (vs TypeScript SDK)

| Feature | PHP SDK | TypeScript SDK |
| --- | --- | --- |
| Retry support | Built-in (`enableRetries`, `numberOfRetries`, `backOffFactor`) | Not built-in |
| Retry on timeout | `retryOnTimeout: true` (default) | N/A |
| HTTP status codes to retry | `408, 413, 429, 500, 502, 503, 504, 521, 522, 524` | N/A |
| HTTP methods to retry | `GET`, `PUT` | N/A |
| Proxy support | `ProxyConfigurationBuilder` | Not built-in |
| Logging | `LoggingConfigurationBuilder` (PSR log levels) | `LoggingOptions` |

## Controllers (5)

Same as TypeScript SDK — Orders, Payments, Vault, Subscriptions, TransactionSearch.

## Usage Example

```php
$ordersController = $client->getOrdersController();

$response = $ordersController->ordersCreate([
    'body' => OrderRequestBuilder::init(
        CheckoutPaymentIntent::CAPTURE,
        [
            PurchaseUnitRequestBuilder::init(
                AmountWithBreakdownBuilder::init('USD', '10.00')->build()
            )->build()
        ]
    )->build(),
    'prefer' => 'return=representation'
]);

$order = $response->getResult();
```

## Related Pages

- [[paypal]] — company page
- [[source-github-paypal-ts-server-sdk]] — TypeScript equivalent SDK (same API surface)
- [[paypal-vault]] — Vault/Payment Tokens concept
- [[source-github-paypal-payouts-php-sdk]] — Payouts PHP SDK (separate, older SDK)

## Raw Sources

- [[github-paypal-php-server-sdk]] — stub file pointing to detail directory
