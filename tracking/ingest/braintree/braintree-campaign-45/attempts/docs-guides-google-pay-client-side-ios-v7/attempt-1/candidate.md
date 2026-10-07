---
title: "Braintree Google Pay Client-Side iOS v7 Availability Notice"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/google-pay/client-side/ios/v7-2026-09-16.md"
tags: [braintree, google-pay, ios, client-side, availability]
---

## Overview

This 2026-09-16 [[braintree]] website snapshot is stored at the Google Pay client-side iOS v7 route, but its substantive Google Pay content is an availability notice naming only the JavaScript v3 SDK and an Android SDK link whose route targets v4. The captured body provides no iOS Google Pay client implementation.

The page also preserves a mobile-SDK certificate warning with a March 30, 2026 expiration date and an iOS `6.17.0+` upgrade direction. Because that date precedes the fetch, the warning is historical page wording rather than current certificate status, exact package compatibility, GitHub release-history evidence, or observed traffic behavior.

## Key takeaways

- The iOS v7 path and client-side title do not establish an iOS Google Pay integration. The body-level availability notice names JavaScript v3 and Android only, with the Android link targeting the v4 route.
- The certificate notice says Braintree Mobile iOS and Android SDK certificates were set to expire on March 30, 2026, says published app versions containing affected SDK versions would be impacted, directs an iOS upgrade to `6.17.0+`, and warns that customer traffic would fail if older app versions were neither decommissioned nor force-upgraded by the deadline. This snapshot does not establish which exact app or dependency versions remained affected after that date.
- The captured body provides no iOS client workflow, Google Pay SDK setup, readiness check, request construction, tokenization or nonce handoff. It also provides no merchant-account enablement, Sandbox/Production procedure, device eligibility, server transaction behavior, or payment outcome. The linked JavaScript, Android and next-page server routes are navigation only unless read independently.
- Page metadata records website create and update timestamps, but it does not establish SDK release history, package contents, current platform support, or correspondence with the separately versioned Braintree iOS GitHub repository.

> [!warning] Route, support and historical-notice boundary
> Do not infer iOS Google Pay support or implementation from this page's URL, title or v7 segment. Its body instead names JavaScript v3 and Android v4 routes. The certificate deadline predates collection, and neither the availability sentence nor warning proves current support, account or environment enablement, runtime behavior, payment execution, or GitHub SDK history.

## Detail locators

- Canonical iOS v7 route, page slug and client-side title: raw lines 1, 7 and 14.
- Website create/update metadata: raw lines 8-9.
- Mobile iOS/Android certificate deadline, published-app impact, iOS `6.17.0+` direction and stated decommission-or-force-upgrade consequence: `**IMPORTANT**`, raw lines 17-18.
- JavaScript v3 and Android-only availability notice, including the Android v4 link target: `**AVAILABILITY**`, raw lines 21-22.
- Unread next-page server-side navigation: raw line 24.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Android v5 client implementation, separately read and retained elsewhere: [[source-braintree-docs-guides-google-pay-client-side-android-v5]]
- Google Pay overview, separately read and retained elsewhere: [[source-braintree-docs-guides-google-pay-overview]]

## Related raw API references

The JavaScript v3, Android v4 and server-side links in this page are navigation only. No corresponding dated raw files are present at their expected collection paths, and they were not used as factual authority for this entry.

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/client-side/ios/v7-2026-09-16|Braintree Google Pay client-side iOS v7 route]] - complete captured page containing the route/body mismatch, historical mobile-certificate warning, platform availability notice and unread server-side navigation
