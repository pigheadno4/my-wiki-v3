---
title: "GitHub: paypal-examples/fastlane-sample-application"
type: source
date_ingested: 2026-04-13
original_format: github-repo
raw_files:
  - "github-fastlane-sample-application.md"
tags: [paypal, fastlane, github, node-js, python, java, vue, angular, quick-start, flexible, checkout]
---

## GitHub: paypal-examples/fastlane-sample-application

Official PayPal demo repository for Fastlane integration. Demonstrates both Quick Start and Flexible integration patterns across 3 client frameworks (HTML, Vue, Angular) and 6 server languages (Node.js, Python, Ruby, PHP, Java, .NET).

Repo URL: <https://github.com/paypal-examples/fastlane-sample-application>

Commit SHA: `bd9ba8cabede84c59919fe08791e9cec048a22c1` | Reviewed: 2026-04-13

## Key Takeaways from Source

### Repo structure

```
fastlane-sample-application/
├── client/
│   ├── html/src/
│   │   ├── init-fastlane.js          ← Quick Start JS logic
│   │   └── init-fastlane-flexible.js ← Flexible JS logic
│   ├── vue/src/views/
│   │   ├── CheckoutView.vue          ← Vue Quick Start
│   │   └── CheckoutFlexibleView.vue  ← Vue Flexible
│   └── angular/src/app/components/   ← Angular components
├── server/
│   ├── .env.example                  ← env var reference
│   ├── shared/views/
│   │   ├── checkout.html             ← Quick Start HTML template
│   │   └── checkout-flexible.html    ← Flexible HTML template
│   ├── node/src/server.js            ← Node.js (Express)
│   ├── python/server.py              ← Python (Flask)
│   ├── java/.../ServerController.java← Java (Spring Boot)
│   ├── php/src/Controller/           ← PHP (Symfony)
│   ├── ruby/src/server.rb            ← Ruby (Sinatra)
│   └── dotnet/Controllers/           ← .NET (ASP.NET Core)
```

### env vars required

```env
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...
DOMAINS=...                # comma-separated, root domains only
PAYPAL_MERCHANT_ID=...     # optional — for partner/marketplace
PAYPAL_BN_CODE=...         # optional — for partner attribution
```

### Three token functions (Node.js pattern, same across all servers)

1. **`getClientToken()`** — for SDK init (`response_type=client_token`, `intent=sdk_init`, `domains[]`)
2. **`getAccessToken()`** — for Orders API calls (standard OAuth2 `client_credentials`)
3. **`getAuthAssertionToken(clientId, merchantId)`** — JWT for partner/marketplace flows (header: `PayPal-Auth-Assertion`)

### Quick Start vs Flexible — HTML structure difference

| Section | Quick Start | Flexible |
| ------- | ----------- | -------- |
| Payment container | `<div id="payment-component">` | `<div id="selected-card">` + `<div id="card-component">` |
| Billing | Inside payment component | Separate `<section id="billing">` |
| Watermark | Inside payment component | `<div id="payment-watermark">` separate |

### Vue integration pattern

`CheckoutView.vue` uses Vue 3 Composition API — same Fastlane SDK calls wrapped in `onMounted()` and reactive refs. Pattern is structurally identical to the HTML version.

### Codespaces

18 ready-to-run configurations: 3 clients (HTML, Vue, Angular) × 6 servers (Node, Python, Ruby, PHP, Java, .NET). Each `.devcontainer/` config wires a client+server pair.

## Files Saved

See stub file for full path list and per-file descriptions: [[github-fastlane-sample-application]]

## Raw Sources

- [[github-fastlane-sample-application]] — stub file with repo metadata and file navigation table
- Detail directory: `raw/github-fastlane-sample-application/`

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-fastlane]] — Fastlane concept page
- [[source-paypal-fastlane-getting-started]] — official Fastlane docs (this repo implements those docs)
