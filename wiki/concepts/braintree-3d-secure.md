---
title: "Braintree 3D Secure"
type: concept
category: technology
tags: [braintree, 3d-secure, card-authentication, sca, liability-shift]
---

## Braintree 3D Secure

Braintree's collected guide describes 3D Secure as an additional authentication step for online credit- and debit-card purchases. During checkout, Braintree performs a lookup; for an enrolled cardholder, the issuing bank decides whether supplied cardholder and device data is sufficient or whether the Braintree SDK must present an issuer-provided dialog or iframe for additional authentication. This is an authentication flow, not evidence that the payment was authorized, processor-approved, or accepted by a gateway fraud rule. [[source-braintree-fraud-tools-3d-secure]]

## Compatibility and enrollment

The guide limits compatibility to credit-card, debit-card and Secure Remote Commerce transactions. It says support covers most merchants in the US, Canada, Europe, Australia and Asia Pacific, while production accounts outside the EEA are not enrolled automatically and only certain configurations are compatible. To start supporting 3DS, it directs merchants to the developer docs and then to contact Braintree to enroll. Treat those collected statements as page-scoped routes, not proof of an individual merchant's current eligibility or enrollment.

## Liability boundary

In certain cases, 3DS can shift fraud-chargeback liability to the customer's bank, based on transaction status. The guide warns that not every 3DS transaction receives a liability shift, and that a shift does not always trigger automatic representation; the merchant must still monitor chargebacks and complete required actions. Do not treat 3DS authentication as a guarantee of chargeback protection or as a replacement for gateway fraud decisioning.

## Sources

- [[source-braintree-articles-br-transactions-three-d-secure-processing-requirements]] - Brazil article snapshot fetched 2026-09-16 (page metadata updated 2025-04-02) for card-brand-qualified debit-card 3DS processing guidance; not a general mandate, liability-shift, current-policy, merchant-eligibility or sibling-account claim
- [[source-braintree-3d-secure-advanced-options-android-v5]] - Android v5-routed advanced-options webpage snapshot for liability signals, vaulted-card and Google Pay verification routes, SCA exemptions, data-only 3DS and Visa DAF; not authorization, settlement, current SDK-support or merchant-eligibility evidence
- [[source-braintree-3d-secure-overview]] - unversioned Braintree developer overview of 3DS and SCA purpose, 3DS2 context, and the authentication handoff before later gateway operations
- [[source-braintree-3d-secure-advanced-options-javascript-v3]] - JavaScript v3 advanced-options route for liability outcomes, client/UI trust boundaries, vaulted cards, Google Pay, SCA exemptions, data-only 3DS and Visa DAF
- [[source-braintree-3d-secure-rules-manager-android-v5]] - Android v5-routed Rules Manager guide for Control Panel ruleset policy, `verifyCard()` evaluation and Android custom-field handoff; 3DS authentication remains distinct from payment authorization, capture and settlement
- [[source-braintree-3d-secure-advanced-options-ios-v7]] - iOS v7-routed advanced-options guide for liability-shift handling, vaulted-card verification, SCA exemption requests, data-only authentication, and other option routes
- [[source-braintree-3d-secure-rules-manager-javascript-v3]] - JavaScript v3-routed Rules Manager guide for Control Panel rulesets evaluated during `verifyCard()`, including client-parameter overrides, action and liability-shift limits, and custom-field matching

- [[source-braintree-fraud-tools-3d-secure]] - authentication purpose and checkout flow, compatibility and enrollment boundaries, and conditional liability-shift warning
