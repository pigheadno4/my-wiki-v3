* [#2119](https://github.com/stripe/stripe-php/pull/2119) Surface `object` property on `EventNotification`
* [#2117](https://github.com/stripe/stripe-php/pull/2117) Emit Claude Code plugin hint at module load time
* [#2115](https://github.com/stripe/stripe-php/pull/2115) Fix v2 timestamp phpdoc type annotations ([#2114](https://github.com/stripe/stripe-php/issues/2114))
* [#2105](https://github.com/stripe/stripe-php/pull/2105) add/adjust event parsing helpers
  
  - Added methods that return their respective `Event`/`EventNotification` class instances without verifying authenticity. Use them when you've previously verified an event (e.g. you verified, put the event in a queue, and are now processing). Supports events from [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge) and [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) natively.
    - `Webhook::constructEventWithoutVerification($payload)`
    - `BaseStripeClient::constructEventWithoutVerification($payload)`
    - `BaseStripeClient::parseEventNotificationWithoutVerification($payload)`
  - Added `WebhookSignature::generateSignatureHeader($payload, $secret, $timestamp = null)`, which computes a full `Stripe-Signature` header for the given payload. Useful for unit tests!
* [#2112](https://github.com/stripe/stripe-php/pull/2112) Add `stripe.major_api_version` constant

See [the changelog for more details](https://github.com/stripe/stripe-php/blob/v21.2.0/CHANGELOG.md).
