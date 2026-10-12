---
title: "Adyen Redirect 3D Secure Web Component Integration"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2/web-component"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/web-component/2026-09-15.md"
tags: [adyen, web-component, cards, 3d-secure, 3ds2, redirect, checkout-api]
---

## Overview

This [[adyen]] guide adds redirect 3D Secure authentication to an existing Web Card Component integration using Checkout API v49 or later and the Advanced `/payments` and `/payments/details` flow. The Card Component handles the shopper redirect after the merchant passes it a redirect action. An integration using only `/sessions` needs no additional 3D Secure configuration under this guide; Checkout API v46 or earlier is routed to a separate guide. See [[adyen-3d-secure]].

## Key takeaways

- The merchant collects payment-form and browser data, sends a server-side `/payments` request with the web 3DS parameters, and checks the response. The guide strongly recommends collecting email, cardholder name, billing address, and IP address for higher authentication rates; its request table distinguishes universally required fields from Visa/JCB or other conditional fields. The Card Component has no shopper-email form configuration, so email is collected outside it.
- If `/payments` returns `action.type: redirect`, the merchant passes the action to the Card Component's `handleAction(action)`, which redirects the shopper to the issuer and then back to the merchant's `returnUrl`. The page describes a response without an action as exempt or out of scope for 3DS, with `resultCode` used for shopper presentation.
- **Checkout API v67 and later:** the return uses HTTP GET with URL-encoded `redirectResult`; the merchant decodes it and sends it server-side in `/payments/details`. If the shopper completes payment but does not return to the site, wait for the `AUTHORISATION` webhook to learn the result.
- **Checkout API v49–v66:** store `action.paymentData` on the server. The return normally uses HTTP POST with `MD` and `PaRes`; the server sends decoded values plus `paymentData` in `/payments/details`. The page provides a conditional `redirectFromIssuerMethod` option when technical limits require GET instead.
- Use `/payments` or `/payments/details` `resultCode` to present the shopper result; the outcome also arrives asynchronously by webhook. If manual capture is configured, an `Authorised` payment still needs capture. In live use, requests for the same payment session must use the same live endpoint region; mixing regions between `/payments` and `/payments/details` may cause 3DS authentication errors.

## Detail locators

- **Opening scope and Requirements**, raw lines 26–43 — Card Component prerequisite, Checkout API version and endpoint selection, Sessions exception, earlier-version route, and PSD2 SCA guide.
- **Step 1**, raw lines 45–63 — recommended shopper data and Card Component collection options.
- **Step 2**, raw lines 65–87 — required versus conditionally required request fields, including `origin`, `returnUrl`, and Visa/JCB cases; raw lines 89–653 contain test-environment and library-version examples.
- **Step 2 response tabs**, raw lines 655–726 — action handling and the v67 versus v66-and-earlier `paymentData` split.
- **Step 3**, raw lines 728–1233 — `handleAction`, test-only credentials, redirect return methods, server-side `/payments/details` requests and responses for each version branch.
- **Step 4 and Test and go live**, raw lines 1244–1263 — result codes, webhook outcome, manual capture, test route, and live-region warning.

## Related

- [[adyen-3d-secure]]
- [[adyen-psd2-sca-and-3d-secure]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/web-component/2026-09-15|Adyen Redirect 3DS Web Component guide (2026-09-15 snapshot)]]
