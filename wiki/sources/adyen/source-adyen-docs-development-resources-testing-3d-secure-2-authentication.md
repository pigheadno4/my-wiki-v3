---
title: "Adyen Docs: Testing 3D Secure 2 authentication"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/testing/3d-secure-2-authentication"
raw_files:
  - "adyen/docs/development-resources/testing/3d-secure-2-authentication/2026-09-15.md"
tags: [adyen, testing, 3d-secure, authentication, test-cards]
---

## Overview

This Adyen test-platform guide provides 3D Secure 2 cards, challenge inputs, and scenario triggers for checking an integration before going live. It routes through [[adyen-payment-testing]] and [[adyen-3d-secure]]. These fixtures test integration handling; they do not prove live issuer behavior, payment approval, or liability shift.

## Key takeaways

- If a configured Dynamic 3D Secure default rule is **Prefer Not**, the page lists three ways to trigger test 3DS2 scenarios: set the default to **Always**, include `authenticationData.attemptAuthentication`, or use an amount that triggers authentication. For text challenges, browser integrations use `password`; native app integrations use `1234`. A different value is the stated failed-challenge fixture.
- The enrolled-card table covers redirect, native identify, and native challenge result-code paths. Specific challenge-action and frictionless fixtures are explicitly for **Advanced flow**, not Sessions. In the frictionless example, the integration supplies a device fingerprint without a further client UI challenge.
- Native-app fixtures include text, single- and multi-select, out-of-band, malformed ACS content, empty challenge response, and timeout cases. To test a native-app route into redirect 3DS2, the guide says to omit `paymentMethod.threeDS2SdkVersion` from the test payment request.
- For ordinary test payments, the page points to test Customer Area or the `AUTHORISATION` webhook's `success` field. **Standalone authentication** is different: this guide says it uses an `AUTHENTICATION` webhook instead of `AUTHORISATION`. An authentication webhook is not itself a live payment authorization or a liability-shift guarantee.
- A separate fixture tests authentication **without liability shift** using the `NoLiabilityShift` challenge password. The advanced-scenario cards exercise `ARes.transStatus` values and transport/error cases; those are authentication response fixtures, not a general mapping from `transStatus` to payment or settlement outcome.

## Detail locators

- **Introduction, raw lines 17–37** — Dynamic 3D Secure condition, trigger choices, browser/native challenge passwords, and test-payment outcome routes.
- **Test cards, raw lines 39–68** — enrolled card table and redirect, identify, and challenge result-code descriptions.
- **3D Secure 2 challenge action / Frictionless flow, raw lines 69–92** — Advanced-only card fixtures and required action or fingerprint handling.
- **Mobile app integration, raw lines 93–116** — native challenge, OOB, malformed response, timeout fixtures, and omission of `threeDS2SdkVersion` for redirect simulation.
- **Standalone authentication / Authentication without liability shift, raw lines 118–133** — webhook-type separation and no-liability-shift fixture.
- **Advanced scenarios, raw lines 134–164** — `ARes.transStatus` and error-scenario test cards.

## Related

- [[adyen]]
- [[adyen-payment-testing]]
- [[adyen-3d-secure]]
- [[adyen-3ds2-android-sdk]]
- [[adyen-3ds2-ios-sdk]]

## Raw Sources

- [[raw/adyen/docs/development-resources/testing/3d-secure-2-authentication/2026-09-15|Adyen Docs — Testing 3D Secure 2 authentication (2026-09-15)]]
