---
title: "Stripe — Best Practices for Preventing Fraud"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-prevention-best-practices-2026.md"
tags: [stripe, fraud, disputes, best-practices, radar, auth-capture, 3ds, statement-descriptor, shipping]
---

## Summary

Three-tier fraud prevention best practices: tools for everyone, Radar for Fraud Teams users, and developers. Organized by implementation complexity.

## Tools for Everyone

- **Require full ToS agreement** at checkout (full text, not just link — card issuers require this for dispute evidence)
- **Track shipping** with confirmation; provide tracking info to customers; screenshots for evidence (card issuers don't follow links)
- **Statement descriptor**: 5–22 chars, ≥5 letters, no `<>'"` — use domain or business name
- **One Stripe account per business** — allows separate descriptors and contact info
- **Proactive refund strategy**: refund immediately if sure it's fraud (unless covered by 3DS liability shift); aggressive refund strategy appropriate if: order unfulfilled, excessive disputes, in monitoring program, <100 payments/month
- **24-48hr shipping delay**: treat rush/overnight orders as higher risk; price overnight shipping extremely high as a filter

## Tools for Radar for Fraud Teams

- **Manual review queue**: payments still charged; use auth+capture if you want to hold before charging
- **Review criteria**: billing≠shipping, AVS match, email/name match, expedited orders, same-IP multiple cards, history of declined attempts
- **Country/card blocking rules**: `:ip_country:`, `:card_country:`, `:card_brand:`, `:card_funding:` attributes
- **Ship to verified address**: AVS-verified billing address is safest; scrutinize orders with different shipping address

## Tools for Developers

- **Process on Stripe** — required for Visa CE 3.0 eligibility (prior transaction history needed)
- **Collect maximum data**: customer name, email, CVC, full billing + shipping address, tracking info
- **3D Secure** — liability shift on authenticated payments; still receive EFWs
- **Stripe Identity** — government ID + selfie verification for high-risk scenarios
- **Auth and capture**: separate authorization from capture (up to 7 days); cardholders can't dispute uncaptured charges; use with Radar review queue
- **Dynamic statement descriptor with verification code**: ask customer to confirm code from their statement
- **Fraud rate alerts**: `spike` (single-day) and `sustained_attack` (multi-day) alert types

## Key Rules

- ToS must show full policy text (not just link) — card issuers reject link-only checkbox as insufficient evidence
- Card issuers won't follow links in dispute evidence — always provide screenshots

## Related Pages

- [[disputes]] — concept page (updated with best practices summary)
- [[source-stripe-disputes-verification]] — CVC/AVS verification
- [[source-stripe-radar-reviews]] — review queue detail
- [[stripe-3d-secure]] — 3DS liability shift

## Raw Sources

- [[stripe-disputes-prevention-best-practices-2026]] — verbatim fraud prevention best practices (180 lines)
