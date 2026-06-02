---
title: "Stripe — Radar Sessions (Provide Additional Fraud Data)"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-sessions-2026.md"
tags: [stripe, radar, radar-sessions, fraud, device-fingerprint, tokenization, direct-api]
---

## Summary

Radar Sessions capture browser/device metadata for direct API or third-party tokenization flows where Stripe.js isn't present during checkout. Not needed for Checkout, Payment Links, Elements, or mobile SDK integrations.

## When to Use

**Use Radar Sessions** when:
- Card tokenization is done by a third party
- Raw card numbers sent to Stripe from your server
- Stripe.js not present during checkout

**Don't use Radar Sessions** when:
- Using Payment Links, Checkout, Elements, or Stripe mobile SDKs (data auto-captured)

## What It Captures

Snapshot of: IP address, browser info, screen/device info, other device characteristics.

## Integration Flow

1. Include Stripe.js on page (or use iOS SDK ≥v21.6.0 / Android SDK ≥v16.9.0)
2. Client: call `stripe.createRadarSession()` as late as possible in checkout; don't abort flow on error
3. Send Radar Session ID to server
4. Server: attach via `radar_options: { session: '{{RADAR_SESSION_ID}}' }`

## Attachment Strategy by Scenario

| Scenario | Where to attach Radar Session |
| --- | --- |
| On-session | PaymentMethod creation **AND** PaymentIntent create/confirm (with `confirm: true`) |
| Off-session | PaymentMethod creation only |

**On-session best practice**: attaching to both allows Radar to compare device info at payment method save vs actual payment time — better fraud detection.

**Important**: Radar Sessions only works on PaymentIntent creation requests that result in a charge attempt (`confirm: true` required when creating).

## Verification

Check API response for `"radar_options": { "session": "{{RADAR_SESSION_ID}}" }` on PaymentIntent or PaymentMethod.

## Related Pages

- [[stripe-radar]] — concept page (updated with Radar Sessions)
- [[source-stripe-radar-optimize-risk-factors]] — risk factor impact (advanced signals +36%)

## Raw Sources

- [[stripe-radar-sessions-2026]] — verbatim Radar Sessions integration guide
