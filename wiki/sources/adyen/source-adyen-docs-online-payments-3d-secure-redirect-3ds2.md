---
title: "3D Secure 2 redirect authentication | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/redirect-3ds2"
raw_files:
  - "adyen/docs/online-payments/3d-secure/redirect-3ds2/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, redirect, online-payments]
---

## Overview

This 2026-09-15 [[adyen]] Docs route page introduces redirect-based 3D Secure 2 authentication: Adyen provides a URL at which the shopper can complete identity verification. It directs API-only integrations toward Web, iOS, or Android Component guides. Use the linked platform guides for implementation instructions; this page itself gives no API sequence, SDK version, or final transaction result. [[adyen-3d-secure]]

## Key takeaways

- The page describes passive, biometric, or two-factor identity verification as possible ways to complete 3D Secure 2 authentication for a card payment. It points to native 3DS2 in a website or mobile app as an alternative to shopper redirection.
- Under its platform chooser, the page says API-only integrations should use the Web, iOS, or Android Component to support 3D Secure. The Web, iOS, and Android entries are navigation to separate guides, not implementation steps or promises of eligibility on this page.
- A redirect URL and a shopper authentication step do not by themselves establish successful authentication, payment authorization, capture, or settlement.

## Detail locators

- **Purpose, native alternative, authentication and redirect URL:** raw lines 15-25.
- **API-only Component recommendation and platform navigation:** raw lines 27-47.
- **Adjacent card-payment and regulation guides:** raw lines 49-53.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure]] — broader 3DS2 overview
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-web-component]] — separately documented Web Component route
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-ios-component]] — separately documented iOS Component route
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2-android-component]] — separately documented Android Component route

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/redirect-3ds2/2026-09-15|Adyen 3D Secure 2 redirect authentication — collected 2026-09-15]]
