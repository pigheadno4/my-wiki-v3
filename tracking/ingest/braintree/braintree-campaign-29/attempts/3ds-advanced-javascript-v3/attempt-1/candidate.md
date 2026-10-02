---
title: "Braintree 3D Secure Advanced Options for JavaScript v3"
type: source
date_ingested: 2026-10-02
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/3d-secure/advanced-options/javascript/v3"
raw_files:
  - "braintree/docs/guides/3d-secure/advanced-options/javascript/v3-2026-09-16.md"
tags: [braintree, 3d-secure, javascript, sca, liability-shift]
---

## Overview

This version-routed Braintree JavaScript v3 guide covers advanced `verifyCard()` behavior and related server-side reporting: liability-shift outcomes, optional device-data collection, vaulted-card verification, requested challenges, Brazil combo-card account selection, Google Pay eligibility, SCA exemptions, data-only 3DS and Visa DAF. The `/javascript/v3` route identifies the documentation surface; it does not establish the exact `braintree-web` package version installed by a merchant or prove current account eligibility.

## Key takeaways

- `verifyCard()` returns a new nonce plus `liabilityShifted` and `liabilityShiftPossible`. A shifted result can mean authentication succeeded or that the issuer does not support 3DS while the payment method does. A failed authentication does not make transaction creation technically impossible: the guide says card brands recommend another payment method, while a merchant with a permitting server-side risk process may use the new nonce if the server integration sets `required` to `false`. The recommendation and the configuration condition are distinct.
- The guide says advanced authentication-request parameters pass through the client first and are for UI flow only; they must not be trusted as server-side risk-assessment inputs. American Express SafeKey can later revoke a reported liability shift based on merchant behavior and fraud rate.
- 3DS authentication and its liability indicators are not transaction authorization, gateway acceptance, capture or settlement. The guide describes creating a transaction with the new nonce as a subsequent action, and separately describes reporting from payment-method single-use tokens and created transactions.
- Optional controls have qualified effects: collecting device data may reduce rejections or challenges; `challengeRequested: true` requests that the cardholder's bank issue a challenge but does not guarantee one; and domestic Brazilian combo-card handling calls for presenting account-type choice and carrying it into both 3DS and the corresponding API call.
- For a vaulted card, the server first creates a nonce from the stored payment-method token, the client passes that nonce to `verifyCard()`, and the client token should include `customer_id`. Google Pay 3DS is limited here to non-network-tokenized cards; network-tokenized cards using a DPAN cannot use 3DS.
- SCA exemptions are issuer-discretionary and never guaranteed. Even when granted, liability remains with the merchant. A `Transaction.sale()` exemption does not override normal 3DS logic after 3DS authentication; `requestedExemptionType` during `verifyCard()` requests a no-challenge path only when conditions are met, otherwise standard authentication is attempted.
- Data-only 3DS is frictionless and grants no liability shift. The captured guide limits it to Mastercard (including Maestro) and Visa on select processors, excludes PSD2-regulated countries, and directs merchants to the Control Panel to confirm account support. `dataOnlyRequested` can fall back to a standard lookup when unsupported, and `verifyCard()` remains required even when Rules Manager flags the transaction as data-only.
- Visa DAF is an eligibility-qualified, region-qualified credential route. The page says subsequent same-instrument, same-merchant transactions should be frictionless with full liability shift for up to two years, requires an acquirer TRA exemption for PSD2 transactions, and directs merchants to their acquiring bank to confirm eligibility. Treat the captured region list and program conditions as snapshot guidance, not a guarantee for a merchant or transaction.

> [!warning] Keep authentication, risk advice and payment processing separate
> Client-returned 3DS data is not trusted server risk evidence, and a successful authentication or reported liability shift does not itself authorize, capture or settle a transaction. Failed-authentication handling includes both card-brand advice to request another payment method and a qualified merchant choice to proceed; do not convert the advice into a universal prohibition or the qualified option into an approval guarantee.

## Detail locators

- Client-side trust boundary and callback/Promise outcome fields: `## Liability shift`, lines 17-54.
- Outcome meanings, failed-authentication recommendation versus `required: false` condition, ineligible-card path and American Express revocation warning: `## Liability shift`, lines 57-65.
- Server-side single-use-token and transaction reporting examples: `## Liability shift`, lines 65-259.
- Optional device attributes and qualified benefit: `## Collecting Device Data`, lines 261-274.
- Vaulted-card nonce sequence and `customer_id`: `## Verifying a vaulted card`, lines 277-331.
- Issuer-challenge request: `## Requesting a cardholder challenge`, lines 334-336.
- Domestic Brazil combo-card account-type UI and API propagation: `## Selecting an account type for combo cards in Brazil`, lines 339-375.
- Google Pay non-network-tokenized versus DPAN eligibility and Drop-in/custom UI routes: `## Verify Google Pay card using 3DS`, lines 377-401.
- Exemption discretion, low-value and TRA conditions, `Transaction.sale()` interaction and `requestedExemptionType`: `## SCA Exemptions`, lines 403-435.
- Data-only liability, processor/card/region support, Control Panel check, fallback and Rules Manager route: `## Data Only`, lines 438-454.
- Visa DAF credential duration, PSD2 TRA condition, captured regions and acquiring-bank eligibility check: `## Visa Digital Authentication Framework`, lines 457-463.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-3d-secure]]
- Related source: [[source-braintree-fraud-tools-3d-secure]]

## Raw Sources

- [[raw/braintree/docs/guides/3d-secure/advanced-options/javascript/v3-2026-09-16|Braintree 3D Secure Advanced Options for JavaScript v3]] - complete captured guide for advanced authentication controls, outcome handling, qualified liability paths and server-reporting examples
