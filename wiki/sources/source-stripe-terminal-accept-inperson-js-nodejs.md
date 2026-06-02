---
title: "Stripe Terminal: Accept In-Person Payments (JavaScript SDK + Node.js)"
type: source
date_ingested: 2026-04-24
original_format: notes
raw_files:
  - "stripe-terminal-accept-inperson-js-nodejs-2025.md"
tags: [stripe, terminal, in-person, javascript, nodejs, integration, paymentintents, card-present, simulated-reader]
---

## Stripe Terminal: Accept In-Person Payments (JavaScript SDK + Node.js)

Complete working code sample for Terminal integration: US / Stripe Reader S700 / JavaScript SDK / Node.js backend. Includes server, client HTML, CSS, and JavaScript.

## Key Takeaways

### PaymentIntent requirements for Terminal

```javascript
stripe.paymentIntents.create({
  amount: req.body.amount,
  currency: 'usd',
  payment_method_types: ['card_present'],  // required for Terminal
  capture_method: 'automatic',
  payment_method_options: {
    card_present: {
      capture_method: 'manual_preferred'  // prefer manual capture when available
    }
  }
});
```

- `payment_method_types` must include `'card_present'` for Terminal payments
- `manual_preferred` allows manual capture when supported, falls back to automatic

### ConnectionToken rules

- Create a `/connection_token` endpoint on your server
- **Authenticate this endpoint** — the secret grants access to your readers
- **Do not cache ConnectionTokens** — the SDK manages the lifecycle
- Pass a `location` ID when creating to scope reader access
- For Connect: scope to the relevant connected account

### JavaScript SDK loading rule

```html
<script src="https://js.stripe.com/terminal/v1/"></script>
```

- Must always load **directly from `https://js.stripe.com`**
- **Do not bundle or self-host** — this breaks integration without warning when reader firmware updates

### SDK initialization

```javascript
var terminal = StripeTerminal.create({
  onFetchConnectionToken: fetchConnectionToken,
  onUnexpectedReaderDisconnect: unexpectedDisconnect,
});
```

Both callbacks are required.

### Reader discovery and connection

```javascript
// Simulated reader
terminal.discoverReaders({simulated: true})
  .then(result => terminal.connectReader(result.discoveredReaders[0]));
```

Filter by `location` to discover intended readers more easily.

### Testing different card scenarios

```javascript
// Set BEFORE calling collectPaymentMethod
terminal.setSimulatorConfiguration({testCardNumber: '4242424242424242'});
```

Test cards:
- `4242 4242 4242 4242` — payment succeeds
- `4000 0000 0000 9995` — payment declined

### Payment flow

1. Server creates PaymentIntent → returns `client_secret`
2. Client calls `terminal.collectPaymentMethod(client_secret)`
3. Client calls `terminal.processPayment(result.paymentIntent)`
4. Client notifies server to capture: `POST /capture_payment_intent`
5. Server calls `stripe.paymentIntents.capture(id)`

### macOS local network note

The Terminal JavaScript SDK requires local network access. On macOS, you must explicitly allow browser apps access to local network devices.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-accept-inperson-js-nodejs-2025]] — complete working code sample (server.js, index.html, global.css, client.js)
