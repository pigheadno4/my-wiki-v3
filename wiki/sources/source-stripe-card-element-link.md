---
title: "Stripe Docs — Link in the Card Element"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-card-element-link-2025.md"
tags: [stripe, link, card-element, deprecated, connect, disablelink]
---

## Summary

Overview of Link in the Card Element — a **deprecated integration path**. Stripe no longer recommends Card Element for Web Elements; use Link Authentication Element, Express Checkout Element, or Payment Element instead.

## Deprecation Notice

Use instead: Link Authentication Element, Express Checkout Element, or Payment Element.

## Key Facts (for existing integrations)

- **Two forms**: single-line Card Element and split Elements (Card Number/Expiry/CVC) — Link behavior identical in both
- **90-day auth window**: same as Payment Request Button; any Link-enabled site
- **Automatically enabled**; disable via Dashboard OR `disableLink: true` parameter (one control sufficient)
- **Not supported in India**; requires granted access

## Display Requirements

Link NOT visible if:
- Container < 350px wide or < 28px tall (other factors: font size, locale, placeholders)
- Browser doesn't support popups (in-app browsers excluded)
- `Cross-Origin-Opener-Policy: same-origin` — Link popup must communicate back to parent page

**Supported browsers**: Chrome, Chrome Mobile, Edge; Safari desktop/iOS (last 3 major versions)

## Connect Eligibility

**Connected accounts CAN manage their own Link settings** if platform uses:
- Direct charges + payment methods on connected accounts + connected accounts have full Dashboard access

**Platform controls Link** (connected accounts cannot customize) if:
- Payment methods cloned from platform, OR destination/separate charges, OR no full Dashboard access
- `disableLink` param can target specific accounts in this case

## CDN Assets

- `raw/assets/stripe-link-card-element-returning.png` — Link autofilling returning customer (98 KB)
- `raw/assets/stripe-link-card-element-new-user.png` — Link sign-up for new customer (98 KB)
- `raw/assets/stripe-link-card-element-dialog.png` — Link authentication dialog (161 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Card Element deprecated section)
- [[source-stripe-payment-request-button-link]] — Payment Request Button (also deprecated)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-card-element-link-2025]] — verbatim webpage content (134 lines)
