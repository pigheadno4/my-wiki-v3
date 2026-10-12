---
title: "Adyen PSD2 SCA and 3D Secure"
type: concept
category: regulation
tags: [adyen, psd2, sca, 3d-secure, authentication, exemptions]
---

## Adyen PSD2 SCA and 3D Secure

Adyen's online PSD2 SCA guidance assumes an online payments integration with 3D Secure and presents three provider-control layers: default handling by Adyen's Authentication Engine, merchant-configured Dynamic 3D Secure rules, and per-transaction API preferences. The API-preference route overrides Adyen's default PSD2 compliance-handling logic, including Adyen's check of whether the transaction is out of scope and its exemption selection and routing, so Adyen recommends it only for integrations with extensive PSD2 SCA and 3D Secure knowledge.

Applicability remains transaction-, regulation-, scheme- and issuer-dependent. Exemption requests can be granted or denied by the issuer, and challenge preferences do not control the issuer's challenge decision. Liability stays with the merchant when the merchant, Adyen on its behalf, or its acquirer requests an exemption and the issuer accepts it; liability shifts when the issuer applies the exemption. This provider compliance scope is distinct from [[adyen-3ds2-ios-sdk]] and [[adyen-3ds2-android-sdk]], which document native client transaction and challenge runtimes.

## Sources

- [[source-adyen-docs-online-payments-psd2-sca-compliance-and-implementation-guide]] — PSD2 SCA overview, processing-entity scope test, issuer/merchant responsibility framing, and 3D Secure route

- [[source-adyen-docs-online-payments-psd2-sca-compliance-and-implementation-guide-sca-options]] — online PSD2 SCA prerequisite, default/Dynamic/API control layers, exemption and issuer boundaries, and liability qualification

## Related

- [[adyen]] — company and knowledge-status page
