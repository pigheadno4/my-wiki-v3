---
title: "Braintree Drop-in Setup and Integration: iOS v7 Route"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/drop-in/setup-and-integration/ios/v7"
raw_files:
  - "braintree/docs/guides/drop-in/setup-and-integration/ios/v7-2026-09-16.md"
tags: [braintree, ios, drop-in, mobile-sdk, deprecation, migration]
---

## Overview

This captured Braintree setup-and-integration page is stored at an iOS v7 Drop-in route, but its retained body says the iOS v7 SDK is not currently supported through Drop-in and directs Drop-in users to the v5 implementation guide. The page also carries dated Drop-in lifecycle and migration notices. It does not provide a v7 Drop-in setup procedure, establish compatibility between the independently versioned Drop-in package and modular iOS v7 SDK, or prove current support, merchant eligibility, tokenization, or payment processing.

## Key takeaways

- The retained note says the iOS v7 SDK is not currently supported through Drop-in and points Drop-in integrations to the v5 implementation guide. The v7 route and title are therefore navigation context, not evidence that Drop-in supports modular iOS v7 behavior.
- The captured warning schedules Drop-in deprecation for October 1, 2026, with no new features, improvements, or bug fixes after that date; it says payment processing remains supported until October 1, 2027. A second warning schedules unsupported status for October 1, 2027, after which Braintree assistance ends and processing may be suspended at any time. Treat these as snapshot-specific notices, not confirmation of current support or continued processing.
- The page's required action is migration to the Braintree iOS SDK for continued processing and ongoing updates, security fixes, and support. That alternative is the modular SDK, distinct from the independently versioned prebuilt `BraintreeDropIn` package retained elsewhere in the wiki.
- The sparse captured body contains no installation steps or rendered v5 guide label beyond the linked route. That absence is not negative evidence about the live page or other documentation.

> [!warning] Route and support boundary
> The canonical URL is an iOS v7 Drop-in setup route, while the captured body explicitly says v7 is not supported through Drop-in and routes Drop-in users to v5. Do not infer v7 Drop-in compatibility from the URL. This historical snapshot also does not prove present support status, merchant configuration, buyer eligibility, successful tokenization, or successful payment processing.

## Detail locators

- Dated deprecation, update cutoff, processing-support window, unsupported milestone, assistance cutoff, and possible suspension: `**IMPORTANT**`, lines 17-20.
- Required migration to the Braintree iOS SDK: `**IMPORTANT**`, line 22.
- iOS v7 unsupported-through-Drop-in notice and v5 guide route: `**NOTE**`, lines 27-28.
- Captured navigation to customization: line 32; the link alone does not establish setup behavior.

## Related

- Company: [[braintree]]
- Concept: [[braintree-ios-sdk]]
- Independently versioned iOS Drop-in package evidence: [[source-github-braintree-ios-drop-in]]

## Raw Sources

- [[raw/braintree/docs/guides/drop-in/setup-and-integration/ios/v7-2026-09-16|Braintree Drop-in Setup and Integration - iOS v7 route]] - complete captured page with the v7 unsupported notice, v5 alternative route, and dated lifecycle and migration warnings
