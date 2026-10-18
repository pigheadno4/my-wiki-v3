---
title: "Stripe PHP SDK (stripe-php)"
type: concept
category: technology
tags: [stripe, php, sdk, payment-intents, checkout, subscriptions, webhooks, idempotency]
---

## Definition

The official Stripe server SDK for PHP, distributed as the `stripe/stripe-php` Composer package. The latest ingested full baseline is `stripe-php@22.0.0` at SHA `c4c1f658483e717519935222e47af224ef4a508b`, pinned to Stripe API `2026-09-30.endive` and requiring PHP 7.4+. The original `21.2.0` PHP7.2/Dahlia baseline and all intermediate chapters remain historical evidence in [[source-github-stripe-php]].

## 21.2.1 Agent Hint Delta

`stripe-php@21.2.1` preserves the Dahlia API/PHP7.2 baseline while removing load-time plugin hint output. Client construction/request preparation now call `AgentPluginHint::maybeEmit()`. It checks nonempty `CLAUDECODE`, no already-loaded PHPUnit test class, and CLI SAPI; `CLAUDE_CODE_CHILD_SESSION` alone no longer triggers it. Its one-attempt flag is set before eligibility checks, so later environment changes do not retry within that process. Hint exceptions are caught; this is not suppression of every SDK warning or a payment API change. Source: [[source-github-stripe-php]].

## 21.3.0 Full Baseline

PHP 7.2+ remains supported; the API pin advances to `2026-08-26.dahlia`. `notificationHandler(secret, fallback)` verifies thin notifications before typed dispatch. Register callbacks and the optional `preHandle` hook before the first `handle`; duplicate registration or later registration throws. A falsy pre-hook result skips both typed and fallback callbacks. Unknown types reach fallback with `isKnownEventType=false`. The explicit without-verification sibling is only for already authenticated input.

V2 coercion now understands nullable and discriminated-union schemas, outbound decimal strings, and array `element` schemas. Missing/non-string request discriminators throw locally; unknown strings pass through. Inbound numeric int64 strings become PHP integers; do not infer a new inbound decimal-to-float conversion. The original handler reconstructs its callback client with the event context but retains the configured Stripe account; consult later version history for context fixes. Checkout card funding restrictions, Billing cancellation feedback options and Payment Link Connect updates expand the generated contract, not account eligibility. Source: [[source-github-stripe-php]].

## 21.3.1 Request Hardening

The requestor now requires a string path starting with one slash, rejecting protocol-relative paths and parsed scheme/host/user components before concatenating the configured API base. It also rejects CR/LF/NUL in string header names/values. Thin-event `fetchEvent()` URL-encodes the notification ID. This protects specific path/header construction boundaries; it neither validates arbitrary custom API bases nor replaces webhook authentication. Source: [[source-github-stripe-php]].

## 21.3.2 Webhook Secret Guard

`WebhookSignature::verifyHeader()` rejects PHP-empty secrets with `SignatureVerificationException` after checking the timestamp/signature header shape. `empty()` also treats the string `"0"` as empty; it does not trim whitespace or enforce the error message's suggested `whsec_` prefix. The existing HMAC/timestamp checks remain; null/zero tolerance skips timestamp validation at this low-level helper, whereas public construction helpers normally pass their 300-second default. Source: [[source-github-stripe-php]].

## 22.0.0 Full Baseline and Migration

- PHP7.2/7.3 are dropped. Composer and the load-time check require PHP7.4; API and major constants become `2026-09-30.endive`/`endive`.
- Selected request-side `payment_method_types` disappears from Checkout Session create, PaymentIntent create/update/confirm, and SetupIntent create/update. Their `allowed_payment_method_types` contracts remain (new on Checkout create); Payment Links still accept `payment_method_types`. Do not apply a global field rename or assume equivalent payment-selection semantics.
- Handler callback clients now clear `stripe_account` before setting event context, keeping captured non-account configuration. Singleton-related notifications use `RelatedSingletonObject` (type/URL without an ID); null `related_object` is skipped safely. Expanded typed thin events cover checkout, payment and Billing lifecycles, but still require authentication, deduplication and authoritative payment-state checks.
- `STRIPE_SUPPRESS_NOTICES=true` (case-insensitive, not whitespace-trimmed) suppresses Stripe notices only when no AI agent is detected. The local branch does not inspect live/test API-key mode; upstream guidance is test/sandbox use. This is distinct from the older plugin-hint guard.
- Expanded union PHPDoc shapes affect IDE/static analysis, not a new runtime schema validator. PayPay/SeQura/BLIK mandate annotations and new product surfaces do not prove merchant availability.
- Subscriptions add a true `pause` endpoint, schedule pause plans, object-shaped update/resume anchors and item-level trials. See [[stripe-subscriptions]] for the preserved conflict between the older trial-only status comment and the new explicit endpoint.

Source: [[source-github-stripe-php]] and [[changelog-github-stripe-php]]. This is an additive full ingest using approved focused reading, not execution of SDK tests or payments.

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
