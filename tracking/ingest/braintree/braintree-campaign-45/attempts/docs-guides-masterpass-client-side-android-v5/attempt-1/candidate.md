---
title: "Braintree Masterpass Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/masterpass/client-side/android/v5-2026-09-16.md"
tags: [braintree, masterpass, android, client-side, legacy, secure-remote-commerce]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is routed as the Android v5 client-side implementation page for legacy Masterpass, but its captured body contains only an availability notice and navigation to a server-side page. The notice says Masterpass was replaced by Visa Secure Remote Commerce (SRC), directs previous Masterpass users to integrate with SRC, qualifies SRC as a limited release for eligible merchants whose API is subject to change, and tells readers to request access. Use [[braintree-payment-methods]] for the provider-wide payment-method route.

The page provides no Android setup, dependency, API call, checkout, tokenization, nonce, client-to-server handoff, transaction action, or Sandbox/Production procedure. The Android v5 URL is therefore not evidence of exact Android SDK package or commit-qualified behavior. Its statement that SRC was introduced in Android v2, iOS v4 and JavaScript v3 describes the notice's historical Client SDK generations for SRC; it does not document a v5 Android implementation or establish current SDK support.

> [!warning] Unresolved SRC support conflict
> This snapshot calls SRC a current limited release and directs prior Masterpass users toward it. The separately retained [[source-braintree-payment-methods-secure-remote-commerce|SRC authority]] says Visa Click to Pay/SRC would no longer be supported effective January 20, 2026 and warns that later attempts receive a `Payment method not supported` error and risk decline, while that same authority also retains current-tense limited-release wording. The collected pages do not resolve present Masterpass or SRC availability, merchant eligibility, or a safe executable migration path.

## Key takeaways

- The central action on this page is a historical migration direction: previous Masterpass users are told to integrate with SRC and contact Braintree to request limited-release access. This is not proof of access, enablement or migration success.
- SRC is described as limited to eligible merchants and its API as subject to change. The page does not identify eligible locations or other prerequisites; use the linked SRC authority rather than broadening this notice.
- The only flow continuation is `Next Page: Server-side`. It is navigation, not evidence that a client nonce was created, that a server request was made, or that authorization, settlement or funding succeeded.
- This website snapshot is separate from versioned Braintree Android SDK GitHub evidence. Neither the Android v5 route label nor the historical Android v2 introduction statement establishes exact library behavior, current support or runtime results.

## Detail locators

- Masterpass replacement and direction to integrate with SRC: `# Client-Side Implementation > **AVAILABILITY**`, raw line 18.
- SRC limited-release eligibility, API-change warning and Android v2/iOS v4/JavaScript v3 introduction statement: `# Client-Side Implementation > **AVAILABILITY**`, raw line 20.
- Access-request route: `# Client-Side Implementation > **AVAILABILITY**`, raw line 22.
- Server-side next-page navigation: raw line 26.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Separate SRC support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]
- Adjacent server-side route: [[source-braintree-docs-guides-masterpass-server-side-node]]

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/client-side/android/v5-2026-09-16|Braintree Masterpass client-side route (Android v5, captured 2026-09-16)]] - complete collected snapshot containing the replacement notice, qualified SRC direction and server-side navigation
