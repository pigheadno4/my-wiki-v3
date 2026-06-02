---
title: "PayPal FraudNet (Web Risk)"
type: source
date_ingested: 2026-04-15
original_format: webpage
raw_files:
  - "paypal-fraudnet-overview.md"
  - "paypal-fraudnet-integrate.md"
  - "paypal-fraudnet-parameters.md"
  - "paypal-fraudnet-payloads-reference.md"
tags: [paypal, fraudnet, fraud-detection, risk-management, javascript, browser, limited-release]
---

## Overview

FraudNet is PayPal's JavaScript library for browser-based device fingerprinting and fraud risk assessment — the web counterpart to Magnes (which handles mobile). It is a limited-release product under `/limited-release/fraudnet/`.

Source URL: <https://developer.paypal.com/limited-release/fraudnet/>

Last updated: 2024-08-15

## Key Takeaways

### What FraudNet does

- JavaScript library embedded in merchant web pages
- Collects browser-based data at checkout
- Sends data directly to PayPal Risk Services for fraud and risk assessment

### Integration

**3-part integration:**

1. **Parameter block** — `<script type="application/json" fncls="fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99">` with `f` (32-char CMID) and `s` (flow ID per page, format: `MERCHANT_NAME_FLOW_NAME`)
2. **Script loader** — either `<script src="https://c.paypal.com/da/r/fb.js">` or dynamic `_loadFraudnetConfig({fnUrl: ...})`
3. **noscript fallback** — `<img>` beacon to `https://c.paypal.com/v1/r/d/b/ns?f=...&s=...&js=0&r=1`

**Backend**: pass CMID as `PAYPAL-CLIENT-METADATA-ID` header in PayPal API calls.

**Optional params**: `mm` mouse movement (default true), `ts` typing speed bot detection (with HTML element IDs), `cb1`/`cb2` POST callbacks, `fp` first-party cookie, `sandbox`, `bu` beacon toggle, `cd` cache, `b` custom beacon URL.

**CSP allowlist**: `c.paypal.com` (img-src, frame-src, script-src) + `b.stats.paypal.com` (img-src). For inline scripts: use nonce (≥128-bit random, Base64, regenerated per page load) or SHA hash — not static nonce.

### Data and privacy

- Used for risk analysis and authentication only
- PayPal does not share FraudNet data with third parties

### Scope

**Browser-based only** — FraudNet is explicitly for web. For mobile device risk data, use [[source-paypal-magnes]] (Magnes SDK).

## Raw Sources

- [[paypal-fraudnet-overview]] — verbatim overview: what FraudNet is, integration summary, data privacy, browser-only scope
- [[paypal-fraudnet-integrate]] — integration guide: 3-part pattern (param block + script loader + noscript), mandatory fncls value, CMID as PAYPAL-CLIENT-METADATA-ID header, CSP domains, nonce guidance
- [[paypal-fraudnet-parameters]] — 11 config params; only f+s required; `s` format: MERCHANT_NAME_FLOW_NAME; behavioral: mm (mouse, default true), ts (typing speed, bot detection); advanced: b/cd/bu
- [[paypal-fraudnet-payloads-reference]] — 4 payloads (P1/P2/P3/w); P1: browser fingerprint + anti-spoof flags; P2: plugins/DOM/GPU/JS heap/perf timing/supercookies; P3: IPv6+mouse; w: typing speed; deprecated Flash fields; sample JSON for P1+P2

## Payload Structure

| Payload | Key data collected |
| --- | --- |
| **P1** | Browser fingerprint: navigator (UA, language, platform), screen/window dimensions, timezone, Flash version, connection type; anti-spoof flags (`sf`, `tb` trueBrowser enum); checksums (`ph1`, `ph2`) |
| **P2** | Browser plugins list, DOM snapshot string, GPU vendor/renderer (WebGL), JS heap sizes (Chrome only), full `window.performance.timing` (20+ timing fields), supercookies (localStorage, Flash LSO, HTTP cookie) |
| **P3** | IPv6 address (from `c6.paypal.com`/Akamai), mouse movement data (`rDT`) |
| **w** | Typing speed per field (`ts1`, `ts2`) — speed only, no keylogging |

`correlationId` in payload = `f` param = CMID = `PAYPAL-CLIENT-METADATA-ID` header — same value across all layers.

## Relevant Wiki Pages

- [[paypal]] — PayPal company overview
- [[paypal-fraud-risk]] — Full PayPal fraud & risk stack concept page (FraudNet + Magnes + FP/FPA/Chargeback Protection)
- [[source-paypal-magnes]] — Magnes: mobile counterpart to FraudNet
