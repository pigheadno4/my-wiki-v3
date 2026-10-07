---
title: "Braintree Apple Pay Client-Side Availability (Android v5 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/apple-pay/client-side/android/v5-2026-09-16.md"
tags: [braintree, apple-pay, android, ios, javascript, client-sdk]
---

## Overview

This 2026-09-16 captured [[braintree]] website page is published at an Apple Pay client-side Android v5 URL, but its body provides no Android Apple Pay integration procedure. Instead, it says Apple Pay is available only through the linked iOS v5 or JavaScript SDK v3 routes. It also retains a dated Braintree Mobile SDK certificate warning. This route/body mismatch is snapshot evidence, not proof of current platform support, account or merchant eligibility, environment configuration, a client/server payment lifecycle, or successful payment execution. See [[braintree-apple-pay]].

## Key takeaways

- The canonical route is `/apple-pay/client-side/android/v5`, while the retained availability notice directs Apple Pay readers to iOS v5 or JavaScript SDK v3. The linked destinations were not read for this entry and are navigation only; no behavior from them is imported here.
- The page says Braintree Mobile iOS and Android SDK SSL certificates were set to expire on March 30, 2026, names Android SDK `4.45.0+` or `5.0.0+` as upgrade targets for new certificates, and warns that all customer traffic would fail for affected published app versions unless they were decommissioned or force-upgraded by the deadline.
- Because the March 30, 2026 date precedes this page's September 16, 2026 fetch, preserve the notice as historical page wording rather than confirmation of current certificate state, current SDK support, exact package compatibility, or observed traffic failure. The `/android/v5` website route is not exact-version GitHub or package-release evidence.
- The page does not document Apple Pay request construction, tokenization, nonce handoff, server transaction processing, account enablement, or sandbox/production configuration. Use the linked platform guides or separate authorities for those questions.

## Detail locators

- **Route and generic page title:** raw lines 1 and 5-14.
- **Apple Pay platform/SDK availability and linked routes:** raw lines 17-18.
- **Historical mobile SDK certificate notice, Android upgrade targets, and failure warning:** raw lines 21-22.

## Related

- [[braintree]]
- [[braintree-apple-pay]]

## Related raw API references

- iOS v5 Apple Pay client-side route (`/braintree/docs/guides/apple-pay/client-side/ios/v5`) - linked navigation only; not read as factual evidence for this source.
- JavaScript SDK v3 Apple Pay client-side route (`/braintree/docs/guides/apple-pay/client-side/javascript/v3`) - linked navigation only; not read as factual evidence for this source.

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/client-side/android/v5-2026-09-16|Braintree Apple Pay client-side Android v5 route (2026-09-16 snapshot)]]
