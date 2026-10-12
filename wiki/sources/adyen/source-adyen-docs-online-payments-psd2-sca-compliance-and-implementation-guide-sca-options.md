---
title: "Adyen docs: Implement SCA compliance"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-options"
raw_files:
  - "adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/sca-options/2026-09-16.md"
tags: [adyen, psd2, sca, 3d-secure, online-payments, compliance]
---

## Overview

This Adyen documentation page describes PSD2 strong customer authentication options for an online payments integration that already implements 3D Secure. It separates three control layers: Adyen's default compliance handling, merchant-configured Dynamic 3D Secure rules, and per-transaction API preferences. This is provider compliance and request-routing guidance, not documentation for the independently versioned native 3DS2 SDK runtimes.

## Key takeaways

- Under the default option, Adyen's Authentication Engine determines whether to trigger 3D Secure and requests an exemption when applicable; the page says it does not trigger 3D Secure for out-of-scope transactions or when the issuer does not enforce it.
- Dynamic 3D Secure adds merchant-configured conditions, such as requesting authentication for transactions the merchant considers high risk. When no rule matches, the page routes handling back to the Authentication Engine.
- Per-transaction API preferences override Adyen's default PSD2 compliance-handling logic, including Adyen's check of whether the transaction is out of scope and its exemption selection and routing; relevant authentication fields also override Dynamic 3D Secure rules. Adyen recommends this route only for integrations with extensive PSD2 SCA and 3D Secure knowledge.
- An exemption request can be granted or denied by the issuer. In the documented authorization-only flow, a granted exemption must also be applied using authentication response values; a challenge preference does not determine whether the issuer challenges the shopper.

> [!warning] Scope and liability
> Applicability depends on regulations and scheme rules; this snapshot is not universal legal advice. The page also distinguishes chargeback liability based on who applies an exemption: liability stays with the merchant when a merchant, Adyen on its behalf, or its acquirer requests an accepted exemption, while issuer-applied exemptions shift liability to the issuer.

## Detail locators

- Prerequisite and authentication-factor framing: `Requirements` and `Guidelines for compliance` (raw lines 23-46).
- One-off, subscription, automatic-top-up and non-fixed-schedule request patterns: `SCA requirements for online payments` (raw lines 48-77).
- Default, Dynamic 3DS and API preference choices: `Compliance options with Adyen` (raw lines 79-109).
- Per-transaction authentication controls and the Checkout API v69 boundary: `Option 3: Specify your preference in the API request` > `Perform 3DS authentication` (raw lines 105-130); earlier-version fields and language-specific examples follow in the raw.
- Exemption request preferences, issuer decision boundary and API-version fields: `Request or apply an exemption` > `Step 1: Request an exemption` (raw lines 1206-1234 and 1752-1772).
- Authentication-only outcomes and applying an exemption during authorization: `Possible responses` and `Step 2: Apply the exemption in the authorization` (raw lines 2286-2326).

## Related

- Company: [[adyen]]
- Provider concept: [[adyen-psd2-sca-and-3d-secure]]
- Native runtime boundaries: [[adyen-3ds2-ios-sdk]], [[adyen-3ds2-android-sdk]]

## Raw Sources

- [[raw/adyen/docs/online-payments/psd2-sca-compliance-and-implementation-guide/sca-options/2026-09-16|Adyen — Implement SCA compliance (2026-09-16)]]
