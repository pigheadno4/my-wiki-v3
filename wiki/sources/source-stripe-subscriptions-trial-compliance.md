---
title: "Stripe — Trial and Promotion Compliance Requirements"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-trial-compliance-2026.md"
tags: [stripe, subscriptions, trials, compliance, statement-descriptor, reminder-email]
---

## Summary

Visa card network compliance requirements for trials. Covers reminder emails, statement descriptor limits, and the manual compliance path without Stripe features.

## Reminder Emails

- Stripe-hosted: enable in Dashboard → "Link to Stripe-hosted page"; not sent in sandbox
- Self-hosted: listen to `customer.subscription.trial_will_end` event
- Timing: 7 days before trial end; if trial <7 days → sent immediately at trial start

## Statement Descriptor

22-char limit. If descriptor >10 chars → truncated to 10 + `* TRIAL OVER`. Product descriptors auto-append trial text; manual descriptors need manual trial text addition.

## Without Stripe Features

- Use `invoice.upcoming` event for email notification timing
- On `customer.subscription.updated`: check if trial ended → update `latest_invoice` statement descriptor
- Must update within 1 hour of invoice creation while in `draft` status

## Related Pages

- [[stripe-subscriptions-trial-offers]] — concept page (updated with compliance requirements)

## Raw Sources

- [[stripe-subscriptions-trial-compliance-2026]] — verbatim trial compliance guide (52 lines)
