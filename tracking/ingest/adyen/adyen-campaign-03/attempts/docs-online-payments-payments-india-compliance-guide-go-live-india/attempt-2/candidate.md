---
title: "India go-live checklist | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/payments-india-compliance-guide/go-live-india"
raw_files:
  - "adyen/docs/online-payments/payments-india-compliance-guide/go-live-india/2026-09-15.md"
tags: [adyen, india, online-payments, go-live, compliance, testing]
---

## Overview

This Adyen checklist routes merchants preparing to accept live payments in India through India compliance prerequisites, live company-account setup, finance and risk checks, India-specific API/front-end/webhook configuration, and end-to-end payment tests. It says Adyen creates the live India company and merchant account after its KYC checks are complete. The captured raw is dated 2026-09-15 and carries a 2022-09-08 `last_modified` value; it is a documentation snapshot, not current legal advice, merchant approval, live account provisioning, or evidence that any payment succeeded.

## Key takeaways

- The merchant is directed to complete the separate payments India compliance guide first. After KYC completion, the page describes a live India account whose configured test payment methods carry over with a new India merchant ID, payouts are set up, and the test admin receives an account-verification and password-change email. It separately directs merchants to contact Adyen Support for payment methods they want to offer to India shoppers; the carry-over statement should not be taken as proof of live method eligibility for a particular merchant.
- For live API traffic, the guide tells the merchant to generate an API key in the India company account, confirm credential permissions, and use the India account's live endpoint URLs. If using Adyen front-end checkout solutions, it says to set `environment` to `live-in` and use India-specific shopper SDK URLs. It defines a working setup by matching the India account's endpoints and seeing payments in that account's payment list; that checklist observation is not payment-outcome proof by itself.
- The checklist also covers live-user roles and two-factor authentication, India payout accounts and settlement reporting, risk profiles and fraud/chargeback notifications, and live India webhook setup and successful HTTP acknowledgement. It warns velocity rules may work less well initially because the India company account lacks historical transaction data.
- End-to-end tests use **real payment details and incur fees**. Make a successful real-detail payment for each offered method; separately test a `Refused` result and a `FRAUD` refusal. If the listed India local methods are implemented, also test redirect delay, cancel and abandonment. The page routes applicable card-on-file/recurring flows and a payment followed by a refund whose authorization and refund requests go through India endpoints and the India company account. These are prescribed checks, not evidence that they were performed or that every outcome can be forced reliably.

## Detail locators

- Introduction before `## Configure your live India Company Account` — prior compliance guide, KYC-triggered live setup, account/method/MID/payout/admin descriptions.
- `## Configure your live India Company Account` / account structure and team access — merchant accounts, user roles, notifications and two-factor authentication.
- `## Finance` and `### Risk` — payout accounts, reporting and reconciliation, optional Reserve, risk profiles, cold-start velocity rule qualification, NOF/NoC alerts and risk-field guidance.
- `### API communication`, `### Set up payment methods`, and `### Webhooks` — India API key and permissions, live endpoints and `live-in` front-end setup, Support contact, shopper statement and webhook acknowledgement.
- `## End-to-end testing`, `### Local payment methods`, `#### Tokenization`, and `### Refunds` — real-payment fee warning, outcome and redirect scenarios, conditional recurring flows and India-endpoint refund check.

## Related

- Company: [[adyen]]
- Concept: [[adyen-online-payments]]
- Related access concept: [[adyen-api-access]]

## Raw Sources

- [[raw/adyen/docs/online-payments/payments-india-compliance-guide/go-live-india/2026-09-15|2026-09-15 snapshot — India go-live checklist]]
