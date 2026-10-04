---
title: "Braintree Premium Fraud Management Tools Client-Side Implementation (Android v5)"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/premium-fraud-management-tools/client-side/android/v5"
raw_files:
  - "braintree/docs/guides/premium-fraud-management-tools/client-side/android/v5-2026-09-16.md"
tags: [braintree, premium-fraud-management, android, device-data, data-collector]
---

## Overview

This collected Braintree Android v5 client-side implementation guide describes using `DataCollector` to collect customer-device data, correlate it with a server-side session identifier, and send successful client output to the merchant server for inclusion in a card verification or transaction request. It assigns user-consent and possible location-disclosure responsibilities to the merchant application and carries a dated mobile-SDK certificate warning.

This is client-side integration evidence from a 2026-09-16 website snapshot. It does not document the server-side attachment procedure, identify which named Premium Fraud Management Tool is enabled, or establish current SDK support, merchant eligibility, account enablement, a fraud decision, processor approval, settlement, or chargeback protection. Named products such as **Fraud Protection**, **Fraud Protection Advanced**, and chargeback-protection tools are not interchangeable with this umbrella integration route.

## Key takeaways

- The page says `DataCollector` collects customer-device data and correlates it with a session identifier on the merchant server. For its Android v5 route, it shows the `com.braintreepayments.api:data-collector:5.8.0` dependency; that example version is a snapshot locator, not a current-version recommendation.
- The merchant creates `DataCollector` with either a Tokenization Key or Client Token and calls `collectDeviceData()` when verifying a card or creating a transaction. In the success branch, the example sends `deviceData` to the merchant server for inclusion in the verification or transaction request. A successful client callback does not prove server receipt, risk evaluation, payment execution, or successful processing.
- The merchant application is responsible for obtaining user-data consent. The page says to set `hasUserLocationConsent` to `true` only after the app has obtained consent to collect location data in compliance with Google Play policy; it also says the merchant may need a prominent disclosure and that the true flag enables sharing device-location data with PayPal for fraud detection and risk management.

> [!warning] Historical mobile-certificate lifecycle notice
> The captured page states that Braintree Mobile iOS and Android SDK certificates were due to expire on March 30, 2026, advises upgrading Android to `4.45.0+` or `5.0.0+`, and warns that customer traffic would fail if affected app versions were neither decommissioned nor force-upgraded by that date. Because the snapshot was fetched after the stated deadline, treat this as historical page evidence—not confirmation of present certificate state, current support, or compatibility for a specific app.

> [!warning] Product and execution boundary
> Device-data collection is an input to a later merchant-server verification or transaction request. This page does not transfer risk-decision states, eligibility, liability treatment, bypass behavior, or protection terms among named fraud products, and it does not show the later server or payment lifecycle completing.

## Detail locators

- Dated Braintree Mobile certificate-expiry notice, advised Android version floors, app-version remediation, and stated traffic consequence: `# Client-Side Implementation > **IMPORTANT**`, raw lines 17-20.
- Device-data purpose and server-session correlation: `## Collecting device data`, raw lines 25-27.
- Android dependency examples for `data-collector:5.8.0`: `### Get the SDK`, raw lines 30-47.
- Authorization choices and collection timing: `### Initializing`, raw lines 49-51.
- Kotlin `DataCollectorRequest`, success/failure branches, and client-to-server `deviceData` handoff example: `### Kotlin`, raw lines 54-84.
- Merchant consent responsibility, conditional `hasUserLocationConsent` setting, possible disclosure, and PayPal location-data sharing consequence: `### Kotlin > **NOTE**`, raw lines 86-89.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-fraud-tools]]
- Platform context: [[braintree-android-sdk]]

## Related raw API references

- [[raw/braintree/docs/guides/premium-fraud-management-tools/server-side/node-2026-09-16|Braintree Premium Fraud Management Tools server-side guide route]] - linked next-page navigation only; not read as factual evidence for this source

## Raw Sources

- [[raw/braintree/docs/guides/premium-fraud-management-tools/client-side/android/v5-2026-09-16|Braintree Premium Fraud Management Tools client-side implementation (Android v5)]] - complete collected snapshot for device-data collection, client-to-server handoff, consent responsibilities, location-data disclosure, and the dated mobile-certificate warning
