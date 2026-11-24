---
title: "Stripe — Radar Lists"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-lists-2026.md"
tags: [stripe, radar, lists, block-list, allow-list, fraud-teams, rules, fingerprint]
---

## Summary

Radar for Fraud Teams block/allow/review lists: default lists for Cards, ACH, and SEPA; custom list types; 50k item limit; fraud report auto-populates block lists.

## Default Lists

3 payment method categories — each includes: fingerprint (unique PM identifier), charge description, client IP country/address, customer ID, email, email domain. Cards also include: card BIN, card country.

Default lists can have items added/removed but cannot be edited or deleted.

## Custom List Types (11)

String, Case-sensitive string, Card fingerprint, Card BIN, Customer ID, Email, IP address, Country, SEPA fingerprint, ACH fingerprint.

Create via Dashboard or API (`/v1/radar/value_lists`). Up to **50,000 items** per list. Items filterable by value, author, date added.

## Expiration Rules

- **Default fingerprint allowlists**: max **30 days** (security protection against fraudster bypass)
- **Custom lists**: can have longer or indefinite expiration (for custom rules only)
- String items (Dashboard): selectable expiration window

## Fraud Report → Block List Auto-Population

Refunding as fraudulent (or API `fraud_details.user_report = 'fraudulent'`) automatically:
- Adds card fingerprint to default card fingerprint block list (+ other cards on same Customer)
- Adds email from: `receipt_email`, Customer.email, description fields, card `name` field

## Related Pages

- [[stripe-radar]] — concept page (updated with lists section)
- [[source-stripe-radar-risk-evaluation]] — feedback loop (fraud reporting)

## Raw Sources

- [[stripe-radar-lists-2026]] — verbatim Radar lists reference
