---
title: "Stripe: Apple Pay Liability Shift, Disputes, and Refunds"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/apple-pay/disputes-refunds"
raw_files:
  - "stripe-apple-pay-disputes-refunds-2026-11-07.md"
  - "stripe-apple-pay-disputes-refunds-2025.md"
tags: [stripe, wallets, apple-pay, disputes, liability-shift, refunds, visa, ios]
---

## Overview

This short [[stripe]] guide covers Apple Pay disputes, liability shift, and refunds. The 2026-05-07 and 2026-11-07 captures at the same URL have the same substantive guidance; the later capture changes only heading whitespace. See [[stripe-wallets]] for the broader wallet context.

## Key takeaways

- Apple Pay account authentication can reduce fraud or unrecognized payments, but a user can still dispute a completed payment. Stripe says evidence can be submitted directly to contest a dispute and the dispute process is the same as for card payments. This page does not identify a specific submission interface or promise that a contest succeeds.
- Stripe's dated guide says Apple Pay supports liability shift globally for major networks, with a **Visa qualification**: iOS 16.2 or later receives that shift globally; on an earlier iOS version, Visa liability shift applies only when the card was issued in Europe. The guide does not establish the outcome for a particular charge or dispute.
- A successful Apple Pay payment can be refunded in full or in part using the card-payment refund process. The page does not give a settlement or recipient timing and is not proof that a refund was performed.

## Detail locators

- Disputes and evidence: [[raw/stripe-apple-pay-disputes-refunds-2026-11-07|November 2026 guide]], line 13; [[raw/stripe-apple-pay-disputes-refunds-2025|May 2026 guide]], line 12.
- Network and Visa liability-shift qualification: November line 17; May line 16.
- Full or partial refunds: November line 21; May line 20.

## Related

- [[stripe-wallets]] — Stripe wallet overview.

## Raw Sources

- [[raw/stripe-apple-pay-disputes-refunds-2026-11-07|Stripe Apple Pay disputes and refunds, 2026-11-07]]
- [[raw/stripe-apple-pay-disputes-refunds-2025|Stripe Apple Pay disputes and refunds, 2026-05-07]]
