---
title: "Braintree Fastlane Setup and Integration"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/fastlane/setup-integration"
raw_files:
  - "braintree/docs/guides/fastlane/setup-integration-2026-09-16.md"
tags: [braintree, paypal, fastlane, sandbox, content-security-policy]
---

## Overview

This collected, unversioned [[braintree]] setup page is an orientation route for enabling [[paypal-fastlane]] in a Braintree Sandbox account. It tells a merchant to create a Braintree Sandbox account if needed, enable Fastlane under Account Settings > Customer Checkout, review Content Security Policy guidance, and continue to the client-side integration guide.

This is a 2026-09-16 website snapshot, not current merchant/account eligibility or enablement evidence. The page names no SDK version, gives no saved-payment-method or profile lifecycle behavior, and does not provide the client/server implementation behind its integration-flow image; its PHP and Ruby server-side notes are change-summary statements, while the explicit next step is a separate client-side route. Nothing on this page establishes successful authentication, tokenization, Vault storage or payment execution.

## Key takeaways

- The documented environment is Braintree Sandbox. The setup action is account-scoped: under Account Settings, select Customer Checkout and click "Turn On" for Fastlane. The instruction does not establish that a particular merchant account is eligible or already enabled.
- The page says its CSP policy was updated following recent SDK changes and encourages merchants to update their integration policy. It explains CSP as a browser control and routes exact configuration details to the separate advanced-options page; no exact SDK version or directive list appears here.
- The integration-flow section contains an image and then routes readers to Client-side Integration. The captured text does not expose the diagram's detailed steps, so use the linked client-side and server-side guides for implementation details rather than inferring them from the image.
- The page's two server-side change notes mention PHP and Ruby support but provide neither setup code nor a version boundary. They should not be read as proof of deployed server behavior or equivalence with the separately linked browser integration.

## Detail locators

- PHP and Ruby server-side change-summary notes: introductory bullets, raw lines 17-19.
- CSP update warning tied to recent SDK changes: introductory bullets, raw lines 21-23.
- Sandbox-account prerequisite and account-setting enablement action: `#### Setup`, raw lines 27-33.
- CSP purpose and advanced-options route: `#### Configure your Content Security Policy`, raw lines 38-40.
- Integration-flow image and next client-side route: `#### Integration Flow`, raw lines 43-47.

## Related

- [[braintree]] - provider and merchant-account context
- [[paypal-fastlane]] - Fastlane identity, checkout and integration retrieval hub

## Related raw API references

- [[raw/braintree/docs/guides/fastlane/advanced-option-2026-09-16|Braintree Fastlane advanced options]] - linked CSP-detail route; navigation only and not evidence for this entry
- [[raw/braintree/docs/guides/fastlane/client-side/node-2026-09-16|Braintree Fastlane client-side integration (Node route)]] - linked next-step route; navigation only and not evidence for this entry
- [[raw/braintree/docs/guides/fastlane/server-side/node-2026-09-16|Braintree Fastlane server-side integration (Node route)]] - related implementation route; navigation only and not evidence for this entry

## Raw Sources

- [[raw/braintree/docs/guides/fastlane/setup-integration-2026-09-16|Braintree Fastlane setup and integration (collected 2026-09-16)]] - fully read pinned website snapshot
