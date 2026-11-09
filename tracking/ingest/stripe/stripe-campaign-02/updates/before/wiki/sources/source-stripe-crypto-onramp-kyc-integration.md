---
title: "Stripe — Crypto Onramp: KYC Tier Integration Guide"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-crypto-onramp-kyc-integration-2026.md"
tags: [stripe, crypto, onramp, kyc, embedded-components, identity-verification, private-preview]
---

## Summary

KYC tier system for the Embedded Components onramp. Three tiers (L0/L1/L2) with different identity requirements and purchase limits. Covers how to detect the user's current tier, interpret session creation errors, and determine next steps.

## KYC Tiers

| Tier | Required Inputs | API |
| --- | --- | --- |
| L0 | Name, phone, email, address | `attachKYCInfo` |
| L1 | + Date of birth, SSN | `attachKYCInfo` |
| L2 | + Photo ID, selfie | `verifyIdentity` |

- L0 required before `collectPaymentMethod` — returns `crypto_onramp_missing_minimum_identity_verification` otherwise
- L0 and L1: asynchronous — must poll until no pending verifications before creating session
- Session creation returns HTTP 400 if any tier has pending verification

## Verification Status Values

`not_available` | `not_started` | `pending` | `rejected` | `verified`

Current tier = highest tier where status is NOT `not_available` or `not_started`.

## Session Error Codes → Next Steps

| Error | Meaning | Next Step |
| --- | --- | --- |
| `crypto_onramp_missing_minimum_identity_verification` | L0 failed | Collect full L0 |
| `crypto_onramp_missing_identity_verification` | L1 required | If current=L1: full L1; if current=L0: partial (`dob`, `id_number`, `id_type` only) |
| `crypto_onramp_missing_document_verification` | L2 required | If current=L1/L2: `verifyIdentity()`; if current=L0: partial L1 first, then `verifyIdentity()` |

## Current Tier Detection (JS)

```js
const currentTier = ["l2", "l1", "l0"].find((t) =>
  ["pending", "rejected", "verified"].includes(
    customer.kyc_tiers.find((k) => k.tier === t)?.verification_status
  )
);
```

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with KYC tier system)
- [[source-stripe-crypto-onramp-embedded-components-integration]] — full integration guide

## Raw Sources

- [[stripe-crypto-onramp-kyc-integration-2026]] — verbatim KYC tier guide (142 lines)
