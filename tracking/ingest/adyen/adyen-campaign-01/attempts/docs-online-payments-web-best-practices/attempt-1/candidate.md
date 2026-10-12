---
title: "Adyen Best Practices for Web Integrations"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/web-best-practices"
raw_files:
  - "adyen/docs/online-payments/web-best-practices/2026-09-15.md"
tags: [adyen, online-payments, web, drop-in, components, security]
---

## Overview

This Adyen Docs page is an unversioned best-practices guide for Web Drop-in and Web Components integrations. It covers browser lifecycle, checkout presentation, custom pay-button safeguards, hosting, browser compatibility, cookies, client-resource loading, and testing. It is guidance for those web integration surfaces, not evidence of current merchant or payment-method eligibility or successful payment execution. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Keep Drop-in/Components current. In frameworks that re-render, initialize `AdyenCheckout` and mount Components only once; with server-side rendering, execute creation and mounting on the client because these surfaces depend on browser APIs.
- A custom pay button must be disabled as soon as a payment attempt begins to prevent duplicate payments. The guide routes Sessions integrations to `beforeSubmit` and Advanced integrations to `onSubmit`. Custom pay buttons are not supported for PayPal, Klarna, or Click to Pay; those methods require the button supplied by the Component.
- Live checkout pages must use HTTPS. HTTP is limited to local development and testing and must be replaced before go-live.
- Adyen recommends avoiding an outer checkout iframe because cross-domain parent/iframe setups break redirect payment flows; if an iframe is unavoidable, the guide says to host it on the same domain as the parent. For native mobile apps it recommends native browser components instead of WebViews, especially for redirect methods.
- Browser and cookie tooling can interfere with the embedded fields that Adyen itself renders in iframes. The guide documents a Cookiebot automatic-blocking conflict that prevents card entry and says misconfigured browser extensions can also block required elements. Drop-in/Components may set the `_RP_UID` risk-management cookie, whose module is enabled by default.
- Adyen recommends loading client resources through the Adyen Web npm package. If scripts and stylesheets are embedded instead, their URL region must match the configured environment and live endpoint region; the guide also recommends Subresource Integrity and routes exact version hashes to release notes.
- Browser-version matrices, v6 versus v5-or-earlier asset URLs, code examples, cookie-testing steps, SRI attributes, and final secure-context/real-device test routes remain in the captured raw at the locators below.

## Detail locators

- `## Requirements`, lines 21–27 — scope limited to Web Drop-in and Web Components.
- `## Keep your integration up-to-date` through `## Manage Server-Side Rendering (SSR)`, lines 29–69 — update advice, single initialization/mounting, React considerations, example, and client-only SSR execution.
- `## Securely implement a custom pay button`, lines 71–116 — duplicate-submit control, Sessions/Advanced callbacks, sample state handling, and unsupported methods.
- `## Use HTTPS for your checkout` through `## Avoid WebViews`, lines 118–141 — live HTTPS requirement, local HTTP exception, outer-iframe redirect failure, and native mobile alternatives.
- `## Ensure browser compatibility`, lines 143–163 — captured desktop and mobile minimum-version tables.
- `## Understand cookie usage` through `## Account for interactions with browser extensions`, lines 165–178 — `_RP_UID`, cookie-isolation testing, Cookiebot card-field blocking/remediation, and extension interference.
- `## Manage client-side resources`, lines 184–229 — npm versus embedded loading, region/environment matching, version-qualified asset tables, and SRI guidance.
- `## Test your integration`, lines 246–256 — secure-context, real-device, end-to-end, and payment/modification test routes.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — provider-level online-payments architecture and source routes.

## Raw Sources

- [[raw/adyen/docs/online-payments/web-best-practices/2026-09-15|Adyen web integration best practices (2026-09-15 snapshot)]]
