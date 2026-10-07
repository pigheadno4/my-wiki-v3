---
title: "Braintree Apple Pay Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/overview"
raw_files:
  - "braintree/docs/guides/apple-pay/overview-2026-09-16.md"
tags: [braintree, apple-pay, ios, javascript-v3, web-payments]
---

## Overview

This captured [[braintree]] website overview introduces Apple Pay as a mobile and online purchasing experience on supported iOS and macOS devices and routes Braintree integrations to an iOS SDK path for in-app acceptance and a JavaScript SDK v3 path for Safari web checkout. It is a dated overview and navigation snapshot linked from [[braintree-apple-pay]], not current merchant, customer, device, browser, or card availability; exact SDK/package history; a complete client/server payment lifecycle; or evidence of a successful payment.

## Key takeaways

- The page says the guide explains how to process Apple Pay payments with Braintree.
- Its in-app route is the Braintree iOS SDK, while its web-checkout route is JavaScript SDK v3 on Safari. The captured iOS link points to an `/ios/v6/` route, so this overview must not be silently treated as iOS v7 or exact current-package evidence.
- Compatibility and availability details are delegated to a linked Apple Pay support article rather than established on this overview page. The page's supported-device wording therefore remains conditional.
- The overview does not document configuration, client/server handoff, processing results, testing, or go-live behavior. Its linked setup and next-page targets are navigation only unless their own pinned evidence is read.

> [!warning] Snapshot scope
> Treat the iOS, macOS, Safari, and SDK wording as statements captured on 2026-09-16. Confirm current Braintree and Apple requirements and merchant-specific eligibility before relying on them.

## Detail locators

- Apple Pay identity, mobile/online scope, supported iOS/macOS-device qualification, and the separate compatibility/availability support route: raw line 16.
- Braintree processing-guide purpose plus the iOS in-app and JavaScript SDK v3 Safari web-checkout routes: raw line 18.
- The historical `/ios/v6/` destination embedded behind the generic `iOS SDK` link: raw line 18.
- Navigation to Braintree SDK architecture and SDK setup: `## See also`, raw lines 23-27.
- JavaScript v3 configuration as the captured next-page route: raw line 29.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-apple-pay]]

## Related raw API references

- [[raw/braintree/docs/start/overview-2026-09-16|Braintree SDK overview]] - unread navigation-only SDK architecture route linked under See also
- [[raw/braintree/docs/guides/apple-pay/configuration/javascript/v3-2026-09-16|Braintree Apple Pay JavaScript v3 configuration]] - unread navigation-only next-page route

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/overview-2026-09-16|Braintree Apple Pay overview]] - complete captured overview for platform and SDK-route scope
