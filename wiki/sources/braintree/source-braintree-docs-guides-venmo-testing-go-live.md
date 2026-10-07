---
title: "Braintree Venmo Testing and Go Live"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/venmo/testing-go-live"
raw_files:
  - "braintree/docs/guides/venmo/testing-go-live-2026-09-16.md"
tags: [braintree, venmo, sandbox, testing, production, go-live]
---

## Overview

This collected, unversioned Braintree Venmo testing-and-go-live page distinguishes a limited Sandbox app-switch simulation from the separate Production setup, application, review and approval path. The 2026-09-16 snapshot names no mobile platform or SDK family, so it is a product-level route rather than Android, iOS or JavaScript implementation authority; its Sandbox fixtures do not demonstrate a real Venmo purchase, and its go-live instructions do not establish current eligibility or Production enablement before approval.

## Key takeaways

- Sandbox testing is limited to an app-switch flow that returns a payment method nonce. The simulated flow shows a test merchant with Braintree branding, and a successful switch returns a nonce for the test user `VenmoJoe`.
- Sandbox purchases are not reflected in the Venmo app. Removing a connection from Venmo to a Sandbox app is not allowed, and the page says an attempt returns HTTP 400.
- The page names `fake-venmo-account-nonce` for Braintree Sandbox use. With that nonce, amount `62.00` creates an `Under Review` test dispute and `62.01` creates an `Open` test dispute; it routes dispute-response testing to the Control Panel and SDK documentation. These are Sandbox fixtures, not Production transaction or dispute outcomes.
- Going live is a separate action: after integration testing, the merchant must set up Venmo in the Production Control Panel and complete an application; Braintree says it reviews the application and enables Production Venmo payments upon approval.

## Detail locators

- Sandbox app-switch-only scope and simulated merchant, user and app-display behavior: `## Sandbox testing`, raw lines 17-24.
- Sandbox connection-removal prohibition and HTTP 400 result: `## Sandbox testing`, raw line 24.
- Test nonce and amount-selected dispute fixtures: raw lines 26-34.
- Production Control Panel setup, application review and approval-dependent enablement: `## Go live`, raw lines 35-38.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

- Venmo server-side connection removal route: raw line 24 (navigation only; linked page not read for this entry).
- General test payment-method nonce route: raw lines 26-27 (navigation only; linked page not read for this entry).
- Control Panel and SDK dispute-response routes: raw line 34 (navigation only; linked pages not read for this entry).
- Venmo Production go-live application route: raw lines 37-38 (navigation only; linked page not read for this entry).

## Raw Sources

- [[raw/braintree/docs/guides/venmo/testing-go-live-2026-09-16|Braintree Venmo Testing and Go Live]] - complete captured page for Sandbox app-switch fixtures, test disputes and approval-dependent Production enablement
