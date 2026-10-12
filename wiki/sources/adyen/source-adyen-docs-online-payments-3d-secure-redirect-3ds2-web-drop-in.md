---
title: "Adyen Redirect 3DS Web Drop-in Integration"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/web-drop-in"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/web-drop-in/2026-09-15.md"
tags: [adyen, web-drop-in, cards, 3d-secure, 3ds2, redirect, checkout-api]
---

## Overview

This Adyen documentation page explains how to add redirect 3D Secure authentication for cards to an existing Web Drop-in integration using the advanced `/payments` and `/payments/details` flow. It applies to Checkout API 49 or later; an integration using only `/sessions` does not need the page's additional 3D Secure configuration. See [[adyen]] and [[adyen-3d-secure]].

## Key takeaways

- The merchant configures Drop-in to collect relevant shopper data, sends `state.data` plus the required or conditionally required web 3DS parameters to its server, and calls `/payments`. The field-level requirements and recommendations are preserved under `## Collect additional parameters in your payment form` and `## Make a payment`.
- When `/payments` returns a redirect `action`, the merchant passes it to the front end and Drop-in handles it with `dropin.handleAction(action)`. A response without an `action` is described as exempt or out of scope for 3DS and is handled through `resultCode`.
- After issuer authentication, for Checkout API v67 and later the redirect back to the merchant's `returnUrl` uses HTTP GET carrying `redirectResult`, which the merchant sends to its server for `/payments/details`; for v66 and earlier, the redirect uses HTTP POST carrying `MD` and `PaRes`, and `/payments/details` also needs the earlier `paymentData`.
- The synchronous `resultCode` is used for shopper presentation, while the payment outcome also arrives asynchronously by webhook. Authorization does not imply capture when manual capture is configured.

> [!warning] Live endpoint consistency
> All API requests for the same live payment session must use the same live endpoint region. Mixing regions between `/payments` and `/payments/details` can cause 3DS authentication errors.

## Detail locators

- `## Requirements` — existing Web Drop-in and backend prerequisites, card enablement, and the PSD2 SCA guide route.
- `## Collect additional parameters in your payment form` — holder name, billing address, email, and Drop-in configuration.
- `## Make a payment` — request parameters, examples, and the version-specific redirect-action response handling.
- `## Handle the redirect` — `handleAction`, return transport, and `/payments/details` completion for Checkout API v67+ versus v66 and earlier.
- `## Present the payment result` — result codes, shopper presentation, webhook outcome, and manual-capture qualification.
- `## Test and go live` — test scenarios, go-live route, and live-region consistency warning.

## Related

- [[adyen]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web-drop-in/2026-09-15|Adyen Redirect 3DS Drop-in integration (2026-09-15 snapshot)]]
