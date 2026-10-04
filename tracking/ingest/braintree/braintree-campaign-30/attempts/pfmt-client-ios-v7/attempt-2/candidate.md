---
title: "Braintree Premium Fraud Management Tools Client-Side Implementation (iOS v7)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/client-side/ios/v7"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/client-side/ios/v7-2026-09-16.md"
tags: [braintree, premium-fraud-management, ios, device-data, data-collector]
---

## Overview

This collected Braintree iOS v7 client-side implementation guide describes collecting customer-device data with Braintree Data Collector, correlating it with a server-side session identifier, and handing the resulting `device_data` string to the merchant server for inclusion with transaction or verification data submitted to the Braintree gateway. It is an umbrella **Premium Fraud Management Tools** integration route, not evidence for the behavior of any one named fraud product.

This is client-side integration evidence from a 2026-09-16 website snapshot. It does not establish current SDK support, certificate state, merchant eligibility or enablement, successful server receipt, a fraud evaluation or decision, processor approval, settlement, or chargeback protection. **Fraud Protection**, **Fraud Protection Advanced**, Kount Custom, and chargeback-protection products are not interchangeable.

## Key takeaways

- The page assigns device-data collection to the iOS client and gateway submission to the merchant server. The client initializes `BTDataCollector`, calls `collectDeviceData`, and sends the returned string to the server with transaction or verification data; the server then includes the `device_data` parameter in its Braintree gateway request. Collecting the string is not proof that the server received or submitted it, or that the gateway evaluated it.
- Installation routes differ by package manager: CocoaPods uses `Braintree/DataCollector`, Swift Package Manager includes `BraintreeDataCollector`, and Carthage includes both `BraintreeDataCollector` and `PPRiskMagnes`. The exact Podfile and Swift snippets remain examples in the raw locators rather than compatibility guarantees for another SDK baseline.
- The page says collecting and passing device data with transactions helps reduce decline rates. Treat that as the page's stated purpose, not a guaranteed merchant outcome or evidence that a named Premium Fraud Management Tool produced a particular decision.
- For PayPal accepted through the Vault flow, the page states that collection through `BraintreeDataCollector` is required. That condition is limited to the documented PayPal Vault flow and does not establish PayPal eligibility, vault success, later payment success, or equivalence with other payment methods.

> [!warning] Automatic-vault verification boundary
> When a new payment method is automatically vaulted, the page says the verification is evaluated by Premium Fraud Management Tools without device data; subsequent transactions can still pass device data. Do not infer device-data coverage for the initial automatic-vault verification.

> [!warning] Historical certificate and version conflict
> This snapshot carries a notice that Braintree Mobile SDK certificates were set to expire on March 30, 2026, directs iOS integrations to version 7.0.0 or later, and warns that traffic from app versions retaining older certificates would fail. The stated date had already passed when the page was captured. A separate same-date iOS setup snapshot names 6.17.0+ instead, so the retained pages do not establish one reconciled current upgrade floor. Verify current official release, security, and lifecycle authority before an operational change.

## Detail locators

- Historical Mobile SDK certificate notice, iOS 7.0.0+ direction and stated traffic consequence: `# Client-Side Implementation > IMPORTANT`, raw lines 17-20.
- Device-data collection purpose and session correlation: `## Collecting device data`, raw lines 25-27.
- CocoaPods, Swift Package Manager and Carthage component routes: `### Get the SDK`, raw lines 30-53.
- Returned `device_data` purpose, `BTDataCollector` / `collectDeviceData` flow and Swift example: `### Implementation`, raw lines 56-74.
- Client-to-server handoff and server-to-gateway responsibility: `### Implementation`, raw line 76.
- Automatic-vault verification warning: `### Implementation > NOTE`, raw lines 79-80.
- PayPal Vault-flow collection requirement: `### PayPal`, raw lines 85-87.
- Server-side next-page navigation: raw line 89.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Native SDK boundary: [[braintree-ios-sdk]]
- [[source-braintree-client-sdk-setup-ios-v7]] - separate iOS v7 setup snapshot with a conflicting historical certificate upgrade floor; neither page establishes current certificate or support state

## Related raw API references

- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Premium Fraud Management Tools server-side Node.js guide]] - linked next-page family navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/client-side/ios/v7-2026-09-16|Braintree Premium Fraud Management Tools client-side implementation (iOS v7)]] - complete collected snapshot for iOS device-data collection, merchant-server handoff, automatic-vault and PayPal Vault qualifications, and the historical certificate notice
