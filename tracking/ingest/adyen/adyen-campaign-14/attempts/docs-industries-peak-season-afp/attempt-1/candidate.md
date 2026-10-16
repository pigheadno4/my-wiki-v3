---
title: "Adyen for Platforms peak-season readiness"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/industries/peak-season/afp"
raw_files:
  - "adyen/docs/industries/peak-season/afp/2026-09-15.md"
tags: [adyen, peak-season, platforms, chargebacks, kyc]
---

## Overview

This Adyen for Platforms peak-season page (last modified and captured 2026-09-15) addresses two platform/marketplace-specific preparations: chargeback split logic and outstanding KYC reviews for onboarded users. It says the rest of the broader readiness guide also applies when users' payments are processed through Adyen. The page is operational guidance, not evidence of current account availability, merchant-of-record identity, funds ownership, transfer execution, payout, bank receipt or compliance completion. Route through [[adyen-peak-season-readiness]].

## Key takeaways

- If chargeback split logic is not set up, the page says Adyen withdraws the **full disputed amount** from the platform/marketplace's liable balance account when a chargeback occurs. The described alternatives book the full amount to the platform's liable account, to the involved user's liable account, or allocate it across balance accounts according to original-payment splits. This is chargeback debit/credit booking logic, not a declaration of legal seller, merchant of record, or ultimate bank receipt (raw lines 23–31).
- Chargeback splits can be set at balance-platform level or individual-payment level; payment-specific splits override the platform-level rule. For platforms, the page recommends split configuration profiles to automate preferred payment/capture/refund/chargeback splits. It links to separate platform and marketplace split-chargeback guides for detail; those child pages are navigation, not imported here (raw lines 27–35).
- Onboarded users may need Adyen re-verification, for example near ID-document expiry. The page says they can keep needed capabilities during an initial response period, but missing required information in time may let capabilities expire and block payouts. This is a conditional risk, not proof that a particular account is verified or a payout is presently eligible (raw lines 37–41).
- Platforms/marketplaces should monitor `balancePlatform.accountHolder.updated` webhooks for outstanding data reviews and ask the account holder to address a verification error. The page gives code `3_10` / “Review of data is required” as an example; a webhook or reminder is not itself KYC approval or a transfer result (raw lines 41–45).

## Detail locators

- Applicability of broader readiness guide and page scope: raw lines 19–21.
- Default chargeback booking, alternatives and override precedence: raw lines 23–35.
- Re-verification, capability/payout risk and webhook example: raw lines 37–45.
- Child links for split chargebacks and verification: raw lines 47–60.

## Related

- [[adyen-peak-season-readiness]] — seasonal operations concept and source route.
- [[adyen]] — provider page.

## Raw Sources

- [[raw/adyen/docs/industries/peak-season/afp/2026-09-15|Adyen for Platforms peak-season guidance, captured 2026-09-15]]
