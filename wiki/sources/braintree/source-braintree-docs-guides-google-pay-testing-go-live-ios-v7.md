---
title: "Braintree Google Pay Testing and Go Live — iOS v7 Availability Notice"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/testing-go-live/ios/v7"
raw_files:
  - "braintree/docs/guides/google-pay/testing-go-live/ios/v7-2026-09-16.md"
tags: [braintree, google-pay, ios, testing, availability]
---

## Overview

This collected [[braintree]] developer page is stored at the Google Pay iOS v7 Testing and Go Live route, but its only substantive Google Pay guidance is an availability notice stating that Google Pay is available only for the JavaScript v3 SDK and Android v4 SDK. The captured body provides no iOS Google Pay integration, testing, Sandbox, Production, or go-live procedure.

This is a 2026-09-16 website snapshot. It does not establish current Google Pay or iOS support, merchant or device eligibility, account enablement, exact SDK compatibility or GitHub implementation history, runtime behavior, or successful payment execution.

## Key takeaways

- The route and page title identify iOS v7 testing and go-live, while the captured availability notice names only JavaScript v3 and Android v4. Do not infer an iOS v7 Google Pay integration from the URL, title, or SDK-version segment.
- The page contains no environment-specific test fixtures, Sandbox behavior, Production enablement, Google review, merchant-ID setup, or go-live steps. Follow and assess the named platform routes on their own evidence rather than importing sibling-platform behavior into this page.
- A separate mobile-SDK warning says Braintree iOS and Android SDK SSL certificates were set to expire on March 30, 2026, directs an iOS upgrade to `6.17.0+` and Android upgrades to `4.45.0+` or `5.0.0+`, and warns that all customer traffic would fail if affected older app versions were neither decommissioned nor force-upgraded by that date.

> [!warning] Historical certificate and route/support boundary
> The certificate deadline predates this page's 2026-09-16 fetch, so the notice is preserved as historical website wording, not current certificate status, exact package compatibility, GitHub release-history evidence, or observed traffic behavior. Separately, the iOS v7 route conflicts with its body-level JavaScript v3/Android v4-only availability statement; the snapshot does not establish current support for any platform.

## Detail locators

- iOS v7 route metadata and page title: raw lines 1, 7, and 14.
- Mobile SDK certificate deadline, affected published app versions, and stated iOS/Android upgrade thresholds: `**IMPORTANT**`, raw lines 17-18.
- Decommission-or-force-upgrade condition and stated 100% traffic-failure consequence: raw line 20.
- JavaScript v3 and Android v4-only Google Pay availability notice: `**AVAILABILITY**`, raw lines 23-24.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]

## Related raw API references

The following exact dated collected page was not read or used as factual authority for this source entry; it is navigation to one platform named by the availability notice:

- [[raw/braintree/docs/guides/google-pay/testing-go-live/javascript/v3-2026-09-16|Braintree Google Pay Testing and Go Live — JavaScript v3]]

The availability notice also links an Android v4 route, but no corresponding dated raw file is present at the expected collection path; that link is navigation only and is not evidence of Android behavior or support.

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/testing-go-live/ios/v7-2026-09-16|Braintree Google Pay Testing and Go Live — iOS v7 route]] - complete captured page containing the route/title mismatch, historical mobile-certificate warning, and JavaScript v3/Android v4-only availability notice
