---
title: "Braintree 3D Secure Advanced Options — Android v5"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/advanced-options/android/v5"
raw_files:
  - "braintree/docs/guides/3d-secure/advanced-options/android/v5-2026-09-16.md"
tags: [braintree, 3d-secure, android, sca, google-pay, liability-shift]
---

## Overview

This collected Android v5-routed Braintree webpage describes advanced 3D Secure (3DS) options: interpreting liability information, verifying vaulted cards and eligible Google Pay cards, handling Brazilian combo-card account type, requesting SCA exemptions, and using data-only 3DS or Visa DAF. It is a dated webpage snapshot, not proof of current Android package support, merchant eligibility, account enablement, or a successful payment.

## Key takeaways

- The Android client result exposes `liabilityShifted` and `liabilityShiftPossible`, but the guide says these parameters pass through the client first and are for UI flow only; they must not be trusted for server-side risk assessment. Server-side payment-method single-use tokens and created transactions separately expose 3DS information for reporting.
- The page describes `liabilityShifted = true` as successful 3DS authentication with fraud liability shifted to the bank, including its stated case where the issuer does not support 3DS but the payment method does. It separately warns that American Express may later revoke a SafeKey liability shift based on merchant behavior and fraud rate.
- When liability shift is possible but did not occur, the card brands recommend asking for another payment method. That is a recommendation rather than an unconditional integration requirement: the page says a merchant with suitable server-side risk assessment may still create a transaction with the new nonce, provided the server integration sets the `required` option to `false`. When neither liability flag is true, the card is described as ineligible for 3DS; a transaction can still be created, but without liability shift.
- The vaulted-card route first creates a payment-method nonce on the server from the stored payment-method token. For Brazilian domestic combo cards, the page says customers should be offered account-type selection and that the selected `accountType` should be reflected in both the `verifyCard()` request and the corresponding transaction, payment-method, or customer API call.
- For Google Pay, the page limits 3DS to non-network-tokenized cards whose PAN is accessible; it says network-tokenized DPAN cards cannot be used with 3DS. The Drop-in subsection carries a separate lifecycle notice assigning July 14, 2025 as the deprecation date and July 14, 2026 as the unsupported date; it also says unsupported processing may be suspended and requests migration to the Braintree SDK. Those captured notice statements do not independently prove present status or establish the support status or exact compatibility of a modular Braintree Android SDK package.
- SCA exemptions are issuer-discretionary and never guaranteed; even when granted, liability remains with the merchant. The page distinguishes requesting an exemption through `Transaction.sale()` when no Braintree 3DS authentication is performed from using `requestedExemptionType` in `verifyCard()`. A sale-time exemption does not override normal 3DS logic, and unmet exemption conditions fall back to a standard 3DS authentication attempt.
- Data-only 3DS is described as frictionless and intended to seek improved issuer authorization rates, but it grants no liability shift. The captured scope is Mastercard (including Maestro) and Visa on select processors, excluding PSD2-regulated countries; unsupported card-brand or processor combinations fall back to a standard lookup, and `verifyCard()` remains required even when Rules Manager flags data-only.
- Visa DAF establishes an authentication payment credential through issuer step-up. The page says subsequent same-instrument, same-merchant transactions should be frictionless with full liability shift, not that they are guaranteed to be so. It gives a validity of up to two years, requires an acquirer TRA exemption when PSD2 applies, and directs merchants to their acquiring bank to confirm eligibility.

> [!warning] Authentication is not authorization or settlement
> A successful 3DS result or liability-shift signal authenticates the cardholder and produces information associated with a nonce. The page still directs the merchant to create a transaction with that nonce; it does not establish processor authorization, gateway acceptance, capture, settlement, or successful payment execution.

> [!warning] Keep client data out of server risk decisions
> The guide expressly limits the client-returned liability parameters to UI flow. Server-side risk decisions need trusted server-side evidence and policy rather than those client-passed values.

> [!warning] Preserve route and lifecycle scope
> This is an Android v5-routed webpage captured on 2026-09-16. Its Drop-in lifecycle notice concerns the separately described Drop-in SDK and must not be generalized into current support or compatibility claims for an exact modular Android SDK package.

## Detail locators

- Client liability fields, UI-only trust boundary, outcome interpretations, `required = false` alternative, ineligible-card path, SafeKey revocation warning, and server reporting objects: `## Liability shift`, lines 17-151.
- Vaulted-card server nonce creation and language examples: `## Verifying a vaulted card`, lines 249-296.
- Brazilian domestic combo-card UI and `accountType` propagation: `## Selecting an account type for combo cards in Brazil`, lines 301-316.
- Google Pay PAN/DPAN distinction, Drop-in lifecycle notice, automatic Drop-in behavior, custom-UI nonce requirement, and network-token check examples: `## Verify Google Pay card using 3DS`, lines 318-363.
- Issuer discretion, merchant-retained liability, low-value and TRA conditions, and the distinct sale-time versus `verifyCard()` request paths: `## SCA Exemptions`, lines 365-397.
- Data-only purpose, no-shift boundary, captured brand/processor/region scope, fallback, Rules Manager alternative, and required `verifyCard()` call: `## Data Only`, lines 400-416.
- DCAP data checklist: `## Data Only`, lines 410-416.
- Visa DAF credential, qualified frictionless wording, validity, PSD2/TRA and regional conditions, request field, and acquiring-bank eligibility route: `## Visa Digital Authentication Framework`, lines 419-425.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]
- Platform concept: [[braintree-android-sdk]]
- Provider-level 3DS purpose and enrollment route: [[source-braintree-fraud-tools-3d-secure]]

## Related raw API references

- [[raw/braintree/docs/guides/google-pay/configuration/android/v5-2026-09-16|Braintree Google Pay configuration — Android v5]] - unread navigation-only route for generating the Google Pay nonce
- [[raw/braintree/docs/guides/3d-secure/rules-manager/android/v5-2026-09-16|Braintree 3D Secure Rules Manager — Android v5]] - unread navigation-only alternative for flagging data-only transactions
- [[raw/braintree/docs/guides/client-sdk/deprecation-policy/android/v5-2026-09-16|Braintree client SDK deprecation policy — Android v5]] - unread navigation-only lifecycle-policy route linked by the Drop-in notice

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/advanced-options/android/v5-2026-09-16|Braintree 3D Secure advanced options — Android v5]] - complete collected webpage covering advanced liability, verification, exemption, data-only, and Visa DAF options
