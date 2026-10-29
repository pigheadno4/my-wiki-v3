---
title: "Adyen Klarna Debit Risk payment-method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna-debit-risk"
raw_files:
  - "adyen/docs/payment-methods/klarna-debit-risk/2026-09-15.md"
tags: [adyen, klarna, online-banking, redirect, chargebacks]
---

## Overview

This 2026-09-15 Adyen Docs snapshot describes Klarna Debit Risk as a bank-account payment method for primarily high-risk segments and specific merchant sectors. It is distinct from Klarna Pay Now: Debit Risk has online banking as its sole funding method and is non-guaranteed. See [[adyen]] and [[adyen-online-payments]]. The snapshot does not establish current merchant eligibility, live availability, or a completed payment.

## Key takeaways

- The overview's capability table describes a redirect flow in Austria, Belgium, Germany, the Netherlands and Spain, all in EUR. It marks recurring with a "See note" qualifier, refunds and partial/multiple partial refunds supported, separate/partial/multiple partial captures unsupported, and chargebacks with a "See note" qualifier. The captured page supplies no recurring explanatory note; do not treat the checkmark as an unconditional recurring guarantee.
- Klarna Pay Now, in contrast, lists direct debit and online banking and says Klarna bears non-settlement risk, while shopper-initiated chargebacks can still occur. Debit Risk's online-banking payments can incur non-settlement chargebacks that cannot be defended against.
- The page says that, rarely (typically less than 0.2% of cases), funds can fail to arrive after a successful `AUTHORISATION` webhook. That event means issuer/Klarna account checks passed and a bank transfer was initiated; an issuer-side risk or AML block can still prevent settlement. Adyen then books a chargeback and sends a `CHARGEBACK` webhook. The cited frequency is a page claim, not an observed rate for a particular merchant.
- This overview routes implementation to Web, iOS, Android and API-only guides. It does not specify their SDK/API versions, request fields, return handling, or method-specific prerequisites.

## Detail locators

- Method identity and Pay Now comparison: pinned raw lines 15–28.
- Capability matrix and country/currency table: pinned raw lines 30–42; the recurring "See note" is not expanded in this capture.
- Non-settlement after `AUTHORISATION` and `CHARGEBACK` webhook: pinned raw lines 44–48.
- Channel guide routes: pinned raw lines 50–74.

## Related

- [[adyen-online-payments]] — provider concept and reciprocal source route

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna-debit-risk/2026-09-15|Klarna Debit Risk overview, captured 2026-09-15]]
