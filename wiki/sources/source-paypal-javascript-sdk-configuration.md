---
title: "PayPal JavaScript SDK: Script Configuration"
type: source
date_ingested: 2026-04-13
original_format: webpage
raw_files:
  - "paypal-javascript-sdk-configuration.md"
tags: [paypal, javascript-sdk, configuration, query-parameters, script-parameters, components, funding, intent, commit, vault, locale, merchant-id]
---

## PayPal JavaScript SDK: Script Configuration

Comprehensive reference for all query parameters and script (`data-*`) attributes on the PayPal JavaScript SDK script tag. Updated 2026-02-04 — the most recently updated reference in the wiki.

Source URL: <https://developer.paypal.com/sdk/js/configuration/>

Last updated: 2026-02-04

## Key Takeaways

### Two loading methods

| Method | Package | Use case |
| ------ | ------- | -------- |
| Script tag | Direct from paypal.com | Standard integration |
| `paypal-js` npm | `@paypal/paypal-js` | Front-end tooling; fine-grained load control |
| `react-paypal-js` npm | `@paypal/react-paypal-js` | React — `PayPalScriptProvider` wrapper |

> Never bundle or self-host the SDK — load only from `https://www.paypal.com/sdk/js`.

### Critical SDK v5 note

This page covers **JS SDK v5 with CardFields**. The legacy HostedFields component is in the archived v1 reference.

### Complete query parameter reference

| Parameter | Default | Key notes |
| --------- | ------- | --------- |
| `client-id` | none (required) | Use `sb` shortcut in sandbox |
| `buyer-country` | auto (IP) | **Sandbox only** — never use in production |
| `commit` | `true` | `true` = Pay Now; `false` = Continue; must match API call |
| `components` | `buttons` | Comma-separated; see components table |
| `currency` | `USD` | 24 supported currencies |
| `debug` | `false` | Bigger script, worse perf — testing only |
| `disable-card` | none | **Deprecated** |
| `disable-funding` | none | Excludes funding sources; don't use to disable ACDC |
| `enable-funding` | none | Ensures funding source renders if eligible |
| `integration-date` | auto | Required only when `client-id` changes dynamically |
| `intent` | `capture` | Must match API call intent |
| `locale` | auto | Only pass to force a specific language |
| `merchant-id` | auto | Partner/marketplace integrations only; email addresses deprecated |
| `vault` | `false` | Filters to only saveable funding sources when `true` |

### `components` options

| Value | Purpose |
| ----- | ------- |
| `buttons` | Payment method buttons |
| `marks` | Payment method logos (for radio button layouts) |
| `messages` | Pay Later messaging |
| `funding-eligibility` | Per-method eligibility checking |
| `hosted-fields` | Hosted card input fields (Expanded Checkout) |
| `applepay` | Apple Pay button |

### `disable-funding` / `enable-funding` options

Full list: `card`, `credit`, `paylater`, `bancontact`, `blik`, `eps`, `giropay`, `ideal`, `mercadopago`, `mybank`, `p24`, `sepa`, `sofort`, `venmo`

> Pass `credit` in `disable-funding` for real money gaming merchants and non-US merchants without credit button licenses.

### `merchant-id` — email addresses deprecated

PayPal email addresses can no longer be used as merchant IDs. Use the PayPal Merchant ID (numeric) from Business Information section.

### `intent` — must match API call

If you pass `intent=authorize` in the script tag, your Create Order API call must also use `intent=AUTHORIZE`. Mismatch causes errors.

### `commit` — must match API call

Same constraint: `commit=false` in script tag must match the order creation intent (no immediate capture).

### `integration-date` — when required

Only needed when `client-id` changes dynamically (cart apps where merchants set their own client ID). Ensures no breaking changes after the specified date. Omit if your `client-id` is stable.

### Script (`data-*`) parameters

| Attribute | Purpose |
| --------- | ------- |
| `data-csp-nonce` | CSP single-use token |
| `data-client-token` | Buyer identification token |
| `data-page-type` | Analytics — `product-details`, `cart`, `checkout`, etc. |
| `data-partner-attribution-id` | BN code for revenue attribution (partner integrations) |
| `data-user-id-token` | OAuth 2.0 `id_token` from server |

### `data-page-type` values

`product-listing`, `search-results`, `product-details`, `mini-cart`, `cart`, `checkout` — tells PayPal which page type the SDK is on, used to optimise button behaviour (referenced in best practices guide).

## Raw Sources

- [[paypal-javascript-sdk-configuration]] — verbatim webpage content (locale table truncated in summary; see raw for full 150+ country list)

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-checkout]] — PayPal Checkout concept page
- [[paypal-expanded-checkout]] — uses `hosted-fields` component + `intent=authorize`
- [[source-paypal-javascript-sdk-overview]] — parent overview page
- [[source-paypal-checkout-standalone-buttons]] — uses `funding-eligibility` component
- [[source-paypal-checkout-messaging-with-buttons]] — uses `messages` component
- [[source-paypal-best-practices-one-time-payment]] — references `data-page-type`
