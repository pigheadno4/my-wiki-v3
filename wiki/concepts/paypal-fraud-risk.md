---
title: "PayPal Fraud & Risk Stack"
type: concept
category: technology
tags: [paypal, fraud-detection, risk-management, fraudnet, magnes, fraud-protection, chargeback-protection, device-fingerprinting, limited-release]
---

## PayPal Fraud & Risk Stack

PayPal's fraud and risk system operates in two layers: **data collection** (gathering device/browser signals) and **merchant-facing tools** (leveraging those signals for risk decisions). FraudNet and Magnes feed raw signals to PayPal Risk Services; Fraud Protection and Chargeback Protection expose risk decisions to merchants.

## Layer 1 — Data Collection

### FraudNet (web)

JavaScript library embedded in merchant web pages. Collects browser-based signals at checkout and sends them directly to PayPal Risk Services.

- **Platform**: Browser only (JS snippet)
- **Integration**: 3-part pattern — parameter block (`fncls="fnparams-dede7cc5-15fd-4c75-a9f4-36c430ee3a99"`) + script loader (`https://c.paypal.com/da/r/fb.js`) + noscript fallback; pass CMID as `PAYPAL-CLIENT-METADATA-ID` header in backend API calls
- **Required params**: `f` (32-char CMID/correlationId) + `s` (unique flow ID per page, format: `MERCHANT_NAME_FLOW_NAME`)
- **CSP**: allowlist `c.paypal.com` + `b.stats.paypal.com`
- **Payloads**: P1 (browser fingerprint, anti-spoof flags), P2 (plugins, DOM, GPU, JS heap, perf timing, supercookies), P3 (IPv6, mouse movement), w (typing speed)
- **Limited release**: `/limited-release/fraudnet/`

### Magnes (mobile)

iOS and Android SDK for mobile device fingerprinting. Generates a `PayPal-Client-Metadata-Id` that links device data to a PayPal transaction.

- **Platform**: iOS (Swift/Obj-C) + Android (Java/Kotlin)
- **Integration**: `MagnesSDK.getInstance().setUp()` → `collectAndSubmit()` → pass `PayPal-Client-Metadata-Id` in API call header
- **Key v5.5.x changes**:
  - iOS 5.5.0: Apple Privacy Manifest compliance (May 2024)
  - Android 5.5.1: `setHasUserLocationConsent(boolean)` required for Google Play compliance — defaults `false`
- **Limited release**: `/limited-release/magnes/`
- **Former codename**: "Dyson"

| | FraudNet | Magnes |
| --- | --- | --- |
| Platform | Web (browser) | Mobile (iOS + Android) |
| Language | JavaScript | Swift / Obj-C / Java / Kotlin |
| Integration point | JS snippet in page | SDK in app |
| Output | Browser payload → Risk Services | `PayPal-Client-Metadata-Id` + device payload |

## Layer 2 — Merchant-Facing Risk Tools

These tools are built on top of the Risk Services signals fed by FraudNet/Magnes.

### Fraud Protection (FP)

No-integration ML risk toolkit. Enabled via PayPal dashboard. Sends `payer.phone` and `payer.email` in API calls for stronger signal.

### Fraud Protection Advanced (FPA)

Self-serve ML tool available in 35 markets. Risk score 0–100. Offers custom filters, allow/block lists, review queue, and per-transaction fee pricing.

- Mutually exclusive with Chargeback Protection

### Chargeback Protection

Automated ML decisions (no merchant review). Waives eligible chargeback fees. Requires delivery evidence. Available in 9 countries.

- Mutually exclusive with FPA

| Tool | Markets | Pricing | Control | Requires |
| --- | --- | --- | --- | --- |
| Fraud Protection | Broad | Included | Dashboard toggle | `payer.phone`/`payer.email` in API |
| FPA | 35 | Per-transaction fee | Custom filters/lists | Expanded Checkout approval |
| Chargeback Protection | 9 | Waived chargeback fees | Automated (no manual review) | Delivery evidence |

## How the layers connect

```text
Buyer browser/device
       │
       ├─ FraudNet (JS) ──────────────────────────────────┐
       └─ Magnes SDK (iOS/Android) ──────────────────────────┤
                                                             ↓
                                              PayPal Risk Services
                                                             │
                              ┌──────────────────────────────┤
                              ↓                              ↓
                    Fraud Protection / FPA          Chargeback Protection
                    (merchant-visible decisions)    (automated waiver)
```

## Relevant Companies

- [[paypal]] — PayPal company overview

## Sources

- [[source-paypal-security-guidelines]] — Security guidelines: 12 principles (OAuth, TLS 1.2+, no client secret client-side, webhook validation, least privilege, 2FA, CSP+SRI); webhook signature verification pattern; OAuth examples in 7 languages
- [[source-paypal-fraudnet]] — FraudNet overview: browser-only JS, snippet + API header, data privacy
- [[source-paypal-magnes]] — Magnes: full docs + binary inspection (iOS 5.5.0 XCFramework, Android 5.5.1 AAR); undocumented SIMILITY/VENMO sources; telemetry APIs
- [[source-paypal-expanded-checkout-fraud-protection]] — Fraud Protection no-integration ML tool
- [[source-paypal-expanded-checkout-fraud-protection-advanced]] — FPA: self-serve ML, 35 markets, per-tx fee
- [[source-paypal-expanded-checkout-chargeback-protection]] — Chargeback Protection: automated, 9 countries, mutually exclusive with FPA
