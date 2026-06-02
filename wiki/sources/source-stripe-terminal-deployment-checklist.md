---
title: "Stripe Terminal: Deployment Checklist"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-deployment-checklist-2025.md"
tags: [stripe, stripe-terminal, deployment, checklist, integration]
---

## Summary

10-item checklist for ensuring a complete and correct Stripe Terminal deployment.

## Checklist Items

1. **ConnectionToken endpoint**: authenticated backend endpoint; never hard-code; use Locations for smart reader access control
2. **Capture PaymentIntents**: for `manual` capture, notify backend to capture when SDK returns processed PaymentIntent
3. **Provide receipts**: prebuilt or custom; save custom receipt copies as dispute evidence
4. **Reconcile payments daily**: catch uncaptured PaymentIntents (abandoned checkouts, failed capture notifications)
5. **Chipper 2X BT updates**: doesn't auto-update; app must support manual updates with progress UI and block navigation
6. **Reader registration**: server-side API; for Connect direct charges use `Stripe-Account` header; destination charges register to platform
7. **Use Locations**: one per physical site; required for proper regional configuration
8. **Discover multiple readers with helpful UI**: Bluetooth Proximity for multiple BT readers; LAN verification for smart readers
9. **Stay on latest SDK**: Android, iOS, JS, React Native
10. **Custom admin passcode**: change default `07139`

## Raw Sources

- [[stripe-terminal-deployment-checklist-2025]] — verbatim webpage content
