---
title: "Braintree Google Pay Configuration — iOS v7 Availability Notice"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/google-pay/configuration/ios/v7"
raw_files:
  - "braintree/docs/guides/google-pay/configuration/ios/v7-2026-09-16.md"
tags: [braintree, google-pay, ios, configuration, availability]
---

## Overview

This captured Braintree website page is stored at a Google Pay configuration route selected as iOS v7, but its substantive body provides no Google Pay configuration procedure for iOS. Its availability notice instead says Google Pay is available only for the JavaScript v3 SDK and Android SDK. The route and version segment are navigation context, not evidence of an iOS Google Pay integration. See [[braintree]] and [[braintree-payment-methods]].

The page separately retains a dated Braintree Mobile certificate notice. It says the iOS and Android SDK certificates were set to expire on March 30, 2026, directs an iOS upgrade to 6.17.0+ and Android upgrades to 4.45.0+ or 5.0.0+, and warns that traffic from app versions retaining older SDKs would fail unless those versions were decommissioned or force-upgraded by that date. Because this is a 2026-09-16 website snapshot carrying deadline wording from March 2026, treat it as historical page text rather than current certificate-status or release-support evidence.

## Key takeaways

- The page's only Google Pay support statement excludes iOS: it names JavaScript v3 and Android, while the body contains no iOS request, SDK call, browser flow, client-to-server handoff, account enablement, or Sandbox/Production configuration.
- The only local configuration action is the historical mobile-certificate remediation: upgrade to the listed SDK floors, or decommission/force-upgrade app versions that retain the older SDKs. The page's stated consequence is failure of 100% of customer traffic for those affected app versions after the deadline.
- Follow the linked JavaScript v3 or Android route for platform implementation detail, and evaluate each page on its own evidence. Their links are navigation only here and were not used to infer behavior.
- This website snapshot does not establish current Google Pay availability, merchant or buyer eligibility, account enablement, browser support, exact package behavior, server behavior, payment execution, or SDK release history. Exact GitHub source and release evidence remain separate.

> [!warning] Route, support and date boundary
> The canonical URL is an iOS v7 route, but the captured availability notice limits Google Pay to JavaScript v3 and Android. Do not infer iOS support from the route. The March 30, 2026 certificate warning is retained historical wording, not proof of current certificate state or current support.

## Detail locators

- **Route identity:** raw lines 1 and 5–14 contain the canonical source URL, page metadata and `# Configuration` heading.
- **Certificate versions and deadline:** raw lines 17–18 contain the `IMPORTANT` notice, March 30, 2026 expiry wording, iOS `6.17.0+` floor and Android `4.45.0+` or `5.0.0+` floors.
- **Affected-version consequence:** raw line 20 contains the decommission-or-force-upgrade condition and the stated `100%` customer-traffic failure consequence.
- **Platform availability:** raw lines 23–24 contain the `AVAILABILITY` notice and its JavaScript v3 and Android SDK links.
- **Malformed navigation artifact:** raw line 26 contains `Next Page: undefined`; it is capture/navigation residue and not product behavior.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Route context: [[braintree-ios-sdk]]

## Related raw API references

The following platform links are reproduced from the fully read page as unread navigation only; they were not used as behavioral evidence for this source entry:

- [Google Pay client-side guide — JavaScript v3](https://developer.paypal.com/braintree/docs/guides/google-pay/client-side/javascript/v3)
- [Google Pay client-side guide — Android v4](https://developer.paypal.com/braintree/docs/guides/google-pay/client-side/android/v4)

## Raw Sources

- [[raw/braintree/docs/guides/google-pay/configuration/ios/v7-2026-09-16|Braintree Google Pay configuration — iOS v7 route (captured 2026-09-16)]] - complete captured page containing the historical mobile-certificate warning and platform-availability notice
