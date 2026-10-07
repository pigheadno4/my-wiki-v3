---
title: "Braintree Apple Pay Configuration for iOS v7"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/apple-pay/configuration/ios/v7"
raw_files:
  - "braintree/docs/guides/apple-pay/configuration/ios/v7-2026-09-16.md"
tags: [braintree, apple-pay, ios, configuration, certificates]
---

## Overview

This captured Braintree website guide documents Apple Pay configuration for an iOS v7 route. It covers Apple Pay Merchant ID and payment-processing-certificate provisioning across Braintree sandbox and production, certificate renewal, and the Xcode capability and provisioning-profile setup needed for an app. The page frames Apple Pay as securely passing payment data from the device Secure Element to Braintree's Vault. This is a dated configuration snapshot, not evidence of current certificate status, merchant eligibility, completed provisioning, or successful payment processing. See [[braintree]] and [[braintree-apple-pay]].

## Key takeaways

- For Apple Pay on a real device, the page requires an Apple Pay Merchant ID and Apple Pay payment processing certificate configured in Apple's Developer Center. Because Braintree sandbox and production are separate, the provisioning steps must be completed once for each environment; the page recommends separate Merchant IDs so a sandbox app cannot create production transactions.
- The certificate flow starts with a certificate signing request downloaded from the Braintree Control Panel. The page says the Braintree-provided CSR must be used rather than a self-created CSR; access may require a different Control Panel role. The resulting Apple payment processing certificate is uploaded to the Control Panel.
- A Merchant Identity Certificate is not required for in-app Apple Pay processing according to this page. Payment processing certificates are stated to expire after 25 months, and renewal requires a new certificate before expiry, upload to the Control Panel, activation with Apple, and repetition for both sandbox and production.
- In Xcode, the app enables the Apple Pay capability and both Merchant IDs, and must be compiled with an Apple development-team provisioning profile containing an Apple Pay Merchant ID. The page says Apple Pay does not support enterprise provisioning.
- The page also retains a critical Braintree Mobile SDK certificate notice stating a March 30, 2026 expiry, naming iOS SDK 7.0.0+ as the upgrade path, and warning that traffic from app versions left on older certificates will fail. Because this raw snapshot was fetched after that stated date while the notice still uses prospective wording, preserve it as captured page wording rather than proof of present certificate state or traffic behavior.

## Detail locators

- **Purpose and dated mobile-SDK certificate warning:** raw lines 14-20.
- **Real-device prerequisites and environment separation:** raw lines 21-26.
- **Merchant ID, Braintree-issued CSR, certificate generation, and Control Panel upload:** raw lines 27-75.
- **In-app Merchant Identity Certificate exclusion and 25-month renewal condition:** raw lines 76-82.
- **Renewal procedure, including Control Panel upload and Apple activation:** raw lines 83-123.
- **Xcode capability, both Merchant IDs, development-team provisioning profile, and enterprise-provisioning exclusion:** raw lines 124-126.

## Related

- [[braintree]]
- [[braintree-apple-pay]]

## Raw Sources

- [[raw/braintree/docs/guides/apple-pay/configuration/ios/v7-2026-09-16|Braintree Apple Pay configuration for iOS v7 (captured 2026-09-16)]]
