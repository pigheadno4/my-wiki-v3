---
title: "Braintree 3D Secure Advanced Options — iOS v7"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/advanced-options/ios/v7"
raw_files:
  - "braintree/docs/guides/3d-secure/advanced-options/ios/v7-2026-09-16.md"
tags: [braintree, 3d-secure, ios, sca, liability-shift]
---

## Overview

This iOS v7-routed Braintree guide snapshot collects advanced 3D Secure options and their boundaries: interpreting liability-shift information, verifying a vaulted card, requesting a cardholder challenge, handling Brazilian combo-card account type, requesting SCA exemptions, using data-only authentication, and requesting Visa DAF. It is a platform- and version-qualified documentation snapshot, not proof of current merchant eligibility, successful authentication, payment authorization, settlement, or payment completion. See [[braintree]], [[braintree-3d-secure]], and [[braintree-ios-sdk]].

## Key takeaways

- The liability fields pass through the client first. The guide limits them to UI-flow use and says not to trust them for server-side risk assessment; choosing to make such assessments can leave the merchant accepting fraud liability.
- `liabilityShifted` and `liabilityShiftPossible` describe authentication and liability conditions, not downstream payment completion. After failed authentication, asking for another payment method is presented as a card-brand recommendation; the guide separately says a merchant with supporting server-side risk assessment can still create a transaction with the new nonce when the server-side `required` option is `false`. An ineligible card can also continue without liability shift. For American Express SafeKey, a returned `liabilityShifted = true` can later be revoked based on merchant behavior and fraud rate.
- SCA exemptions are requests subject to issuer discretion, never guaranteed. Even when granted, the guide says liability remains with the merchant. A `Transaction.sale()` exemption request does not override normal 3DS logic when 3DS authentication was performed; an unmet exemption request during 3DS falls back to a standard authentication attempt.
- Data-only 3DS is frictionless but grants no liability shift. The captured guide limits it to named card brands and select processors, excludes PSD2-regulated countries, requires checking merchant-account support, and says unsupported card-brand or processor combinations fall back to a standard lookup. Using Rules Manager as the flagging route does not remove the need to call `verifyCard()`.

## Detail locators

- **Liability result interpretation, client/server trust boundary, American Express warning, and server reporting examples:** `## Liability shift` (raw lines 17–229).
- **Vaulted-card nonce creation and client handoff:** `## Verifying a vaulted card` (raw lines 231–276).
- **Challenge request:** `## Requesting a cardholder challenge` (raw lines 277–279). The option requests that the cardholder's bank issue a challenge; the snapshot does not state that a challenge is guaranteed.
- **Brazilian domestic combo-card account-type UI and API placement:** `## Selecting an account type for combo cards in Brazil` (raw lines 280–290).
- **Exemption types and the distinct `Transaction.sale()` versus 3DS request paths:** `## SCA Exemptions` (raw lines 292–312).
- **Data-only purpose, support checks, fallback, Rules Manager alternative, and DCAP data routes:** `## Data Only` (raw lines 313–329).
- **Credential duration, PSD2/TRA condition, captured regional list, request field, and acquiring-bank eligibility route:** `## Visa Digital Authentication Framework` (raw lines 332–334).

## Related

- [[braintree-3d-secure]] — authentication, eligibility, and conditional liability-shift boundaries.
- [[braintree-ios-sdk]] — separately versioned native iOS SDK context; this website snapshot does not establish current package support.

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/advanced-options/ios/v7-2026-09-16|Braintree 3D Secure advanced options — iOS v7 (2026-09-16 snapshot)]]
