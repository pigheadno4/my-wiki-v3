---
title: "Braintree ACH Direct Debit Client-Side Availability (Android v5 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/ach/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/ach/client-side/android/v5-2026-09-16.md"
tags: [braintree, ach, direct-debit, android-v5, javascript-v3, availability]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is routed as an ACH Direct Debit client-side page for Android v5, but its retained substantive body says only that ACH Direct Debit is available to eligible merchants using the JavaScript v3 SDK. It provides no Android client setup, bank-data collection or tokenization procedure. Treat the route as a platform/version scope boundary, not as evidence that ACH Direct Debit is implemented by or available through Android SDK v5.

## Key takeaways

- The captured availability notice conditions ACH Direct Debit on merchant eligibility and points to JavaScript v3. It does not establish present availability, eligibility or enablement for any merchant.
- The page contains no ACH request fields, nonce creation, vaulting, bank-account verification, server transaction action, settlement, funding or return behavior. Its final server-side link is navigation only and does not establish a client/server lifecycle.
- The page provides no Sandbox-versus-Production behavior, account configuration or environment-specific outcome, and it is not evidence of successful payment execution.

> [!warning] Android route versus retained body
> The canonical URL and slug end in `/android/v5`, but the body names the JavaScript v3 SDK and supplies no Android ACH integration procedure. Do not infer Android v5 ACH capability, package compatibility or platform parity from the route.

> [!warning] Historical mobile-certificate notice
> The captured page says Braintree Mobile iOS and Android SDK SSL certificates were set to expire on March 30, 2026, directs Android integrations to SDK `4.45.0+` or `5.0.0+`, and warns that all customer traffic from affected app versions would fail unless those versions were decommissioned or force-upgraded by the deadline. Because the snapshot was fetched after that date and the wording is preserved website content, treat it as historical notice evidence—not confirmation of current certificate state, current SDK support, exact-package compatibility or observed traffic failure.

## Detail locators

- Canonical URL and collection metadata: lines 1-3.
- Page title, Android v5 slug and creation/update timestamps: frontmatter, lines 5-10.
- Android-routed page heading: `# Client-side Implementation`, line 14.
- Eligible-merchant and JavaScript v3 availability wording: `**AVAILABILITY**`, lines 17-18.
- Mobile certificate deadline, named Android upgrade floors and stated failure consequence: `**IMPORTANT**`, lines 21-24.
- Server-side destination: `Next Page: Server-side`, line 26; navigation only, not factual authority for server behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- ACH lifecycle overview: [[source-braintree-docs-guides-ach-overview]]
- Android SDK evidence boundary: [[braintree-android-sdk]]; exact package implementation and release history belong to its separately retained GitHub sources, not this website route.

## Raw Sources

- [[raw/braintree/docs/guides/ach/client-side/android/v5-2026-09-16|Braintree ACH Direct Debit client-side page - Android v5 route (captured 2026-09-16)]]
