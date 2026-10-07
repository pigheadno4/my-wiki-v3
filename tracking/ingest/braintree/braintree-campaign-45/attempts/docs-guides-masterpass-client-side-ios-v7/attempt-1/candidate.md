---
title: "Braintree Masterpass Client-Side Availability Notice (iOS v7 Route)"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/masterpass/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/masterpass/client-side/ios/v7-2026-09-16.md"
tags: [braintree, masterpass, secure-remote-commerce, ios, legacy]
---

## Overview

This 2026-09-16 [[braintree|Braintree]] website snapshot is stored at a Masterpass client-side iOS v7 route, but its captured body contains only an availability notice. The notice says Masterpass was replaced by Visa Secure Remote Commerce (SRC) and directs prior Masterpass users to integrate with SRC; it provides no Masterpass or SRC iOS implementation procedure. This is a historical migration route under [[braintree-payment-methods]], not evidence of current support, merchant access, a safe migration, or payment execution.

## Key takeaways

- The page directs prior Masterpass users to integrate with SRC. That is the only action stated in the captured body; it does not document a Masterpass client action, tokenization, nonce handoff, server transaction, or payment lifecycle.
- The SRC direction is materially qualified: the notice calls SRC a limited release for eligible merchants, says the API is subject to change, and tells merchants to contact Braintree to request access.
- The notice says SRC was introduced in Android v2, iOS v4 and JavaScript v3 of Braintree's Client SDKs. Those are page-stated SRC introduction generations; they do not establish a Masterpass iOS v7 implementation, an exact package version, present SDK behavior, or GitHub implementation history.
- Although the canonical route and page title identify client-side iOS v7 context, the retained body supplies no iOS API, request or response shape, client/server division, environment setup, test procedure, or Production procedure.

> [!warning] Unresolved successor-support conflict
> This page directs former Masterpass users to limited-release SRC. Separately retained [[source-braintree-payment-methods-secure-remote-commerce|SRC authority]] says Visa Click to Pay/SRC would no longer be supported effective January 20, 2026 while also retaining current-tense limited-release language. The collected snapshots do not resolve present support, individual merchant eligibility, or a safe executable migration path.

## Detail locators

- iOS v7 route metadata and generic page title: frontmatter `slug` at raw line 7 and `# Client-Side Implementation` at raw line 14.
- Masterpass replacement and direction to integrate with SRC: `**AVAILABILITY**`, raw lines 17-18, first and second sentences.
- SRC limited-release eligibility, API-change warning and access-request route: `**AVAILABILITY**`, raw lines 17-18, third and fifth sentences.
- Android v2, iOS v4 and JavaScript v3 SRC introduction history: `**AVAILABILITY**`, raw lines 17-18, fourth sentence.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Successor support-status authority: [[source-braintree-payment-methods-secure-remote-commerce]]

## Raw Sources

- [[raw/braintree/docs/guides/masterpass/client-side/ios/v7-2026-09-16|Braintree Masterpass client-side iOS v7 route (captured 2026-09-16)]] - complete captured page containing the title and the qualified Masterpass-to-SRC availability notice
