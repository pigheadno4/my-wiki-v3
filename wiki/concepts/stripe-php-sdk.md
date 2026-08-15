---
title: "Stripe PHP SDK (stripe-php)"
type: concept
category: technology
tags: [stripe, php, sdk, payment-intents, checkout, subscriptions, webhooks, idempotency]
---

## Definition

The official Stripe server SDK for PHP, distributed as the `stripe/stripe-php` Composer package. The latest retained wiki baseline is `stripe-php@21.2.0` at SHA `edf8118f0b96d69f06f372da9168d613d1aed072`, pinned to Stripe API `2026-07-29.dahlia` and requiring PHP 7.2+.

## Integration Pattern

```php
$stripe = new \Stripe\StripeClient('sk_test_...');

$session = $stripe->checkout->sessions->create([
    'mode' => 'payment',
    'line_items' => array(array(
        'price' => 'price_...',
        'quantity' => 1,
    )),
    'success_url' => 'https://example.com/success',
    'cancel_url' => 'https://example.com/cancel',
]);
```

Use `StripeClient` services for new code. Legacy static resource methods remain available for older integrations.

## Operational Rules

- Use one PaymentIntent per order or customer session; retry the same intent rather than creating duplicate payment histories.
- Enable network retries deliberately. Idempotency keys make retryable mutations safer, but a local timeout does not prove Stripe stopped processing.
- Verify public webhook payloads with `Webhook::constructEvent()` and the exact raw body. Default timestamp tolerance is 300 seconds.
- Use `constructEventWithoutVerification()` and `parseEventNotificationWithoutVerification()` only after separate verification or for a trusted cloud event source.
- Record both package and pinned API versions in version-sensitive answers.
- Treat generated method presence as SDK evidence, not proof of merchant eligibility or payment-method availability.

## Checkout-Relevant Services

| Area | Service surface |
| --- | --- |
| Custom payments | `paymentIntents`, `setupIntents`, `paymentMethods` |
| Managed checkout | `checkout->sessions`, `paymentLinks` |
| Recurring billing | `subscriptions`, `subscriptionItems`, `subscriptionSchedules`, `invoices` |
| Fulfillment | `events`, webhook and event-notification helpers |
| In-person | `terminal->readers`, locations, configurations, connection tokens |

## Version Boundary

The retained v21.2.0 baseline includes both v1 form-encoded and v2 JSON request modes. Null values can encode differently across those modes. Its exact release adds pre-verified event parsers and related event-notification helpers; those names describe a trust boundary, not a shortcut for public webhook verification.

## Sources

- [[source-github-stripe-php]] - cumulative exact-SHA SDK evidence
- [[changelog-github-stripe-php]] - package-qualified release history
- [[stripe-payment-intents]] - PaymentIntent lifecycle and integration choices
- [[stripe-checkout]] - Checkout Sessions integration paths
