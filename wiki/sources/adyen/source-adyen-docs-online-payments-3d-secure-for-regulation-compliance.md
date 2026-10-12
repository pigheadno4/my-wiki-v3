---
title: "Adyen 3D Secure for regulation compliance"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance"
raw_files:
  - "adyen/docs/online-payments/3d-secure-for-regulation-compliance/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, sca, regulation, liability-shift]
---

## Overview

This [[adyen]] documentation snapshot explains why 3D Secure is used in response to online-payment authentication regulation, surveys region-specific examples and dated scheme changes, and summarizes scheme- and flow-dependent fraud-chargeback liability-shift rules. It complements the integration routes in [[adyen-3d-secure]]; it is not universal legal advice or proof that a particular transaction is compliant, authenticated, authorized, or protected from chargeback liability.

## Key takeaways

- Adyen says many of the surveyed regulations apply to issuing banks rather than directly to merchants, while warning that an issuer may refuse a transaction it evaluates as non-compliant and thereby lower authorization rates. The page routes merchants to regulatory, scheme, EMVCo, and Adyen guidance rather than making its overview a substitute for those authorities.
- The regional section gives examples for Australia, Europe, India, Malaysia, Japan, and France. Applicability varies by actor, geography, transaction type, thresholds, exemptions, and issuer behavior; the dates and card-scheme changes on this collected page are snapshot evidence, not confirmation of current requirements.
- Adyen describes 3D Secure as an extra verification layer for card-not-present transactions. In the native 3DS2 route described here, the issuer authenticates within the merchant website or app using passive, biometric, or two-factor approaches.
- The page states a general fraud-liability rule for a successfully completed 3DS2 challenge and notes that some regions may also grant liability shift after a successful frictionless flow. Its Visa, Mastercard, and Cartes Bancaires rules remain conditioned by scheme, region, period, transaction type, authentication preference, issuer behavior, and flow outcome.

> [!warning] Liability shift is conditional
> Do not infer liability shift merely from 3DS implementation or an apparent success indicator. The page records a rare US domestic Visa case in which issuer CAVV validation can fail and prevent liability shift even when ECI 05 is returned; other scheme-specific exceptions and conditions remain in the raw tables.

## Detail locators

- `## What you need to know` and `## What you need to do` — actor scope, issuer-decline risk, 3D Secure recommendation, and routes to regulatory, scheme, EMVCo, and Adyen guidance.
- `## Overview of existing regulations` — region-specific examples and their merchant, issuer, threshold, transaction-type, wallet, and exemption qualifications.
- `## Important dates` — the page's 2023–2025 regulatory and card-scheme timeline; verify current primary authorities before operational use.
- `## Use 3D Secure for compliance` — protocol purpose and the issuer-authentication description.
- `## 3D Secure chargeback liability shift rules` — the general challenge-versus-frictionless framing and the Visa and Mastercard tables.
- `### Visa liability shift rules` and `#### CAVV reuse exceptions for Visa` — regional/period rules, the 90-day statement, the US CAVV-validation exception, and historical European reuse conditions.
- `### Mastercard liability shift rules` — region-, period-, transaction-, exemption-, issuer-, and flow-qualified table and the page's dated protection-period statement.
- `### Cartes Bancaires liability shift rules` — authentication-preference inputs and flow-dependent liability outcomes.

## Related

- [[adyen]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure-for-regulation-compliance/2026-09-15|Adyen 3D Secure for regulation compliance (2026-09-15 snapshot)]]
