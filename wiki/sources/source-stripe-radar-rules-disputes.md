---
title: "Stripe — Dispute Resolution Rules"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-rules-disputes-2026.md"
tags: [stripe, radar, rules, disputes, dispute-resolution, dispute-prevention]
---

## Summary

Radar dispute resolution rules automatically refund matching incoming disputes. Requires dispute prevention signup. Same rule syntax as transaction rules with a dispute-specific attribute set.

## Rule Structure

```
Resolve dispute if {condition}
```

Action is always `Resolve dispute`. Uses same syntax as other Radar rules.

Example: `Resolve dispute if :amount_in_usd: <= 10.00`

## Dispute-Specific Attributes

| Attribute | Type | Notes |
| --- | --- | --- |
| `amount_in_xyz` | Numeric | Disputed amount (may differ from payment amount); auto-converts currency |
| `card_brand` | String | `visa` or `mc` only |
| `card_bin` | String | First 6 digits of card |
| `card_country` | Country | 2-letter ISO |
| `currency` | String | 3-letter currency code |
| `is_fraudulent` | Boolean | true = fraud dispute; false = product/service/cancellation dispute |
| `network_reason_code` | String | Visa network codes only (currently) |
| `statement_descriptor` | String | Statement descriptor on payment |
| `account` | String (case-sensitive) | Connect destination/on_behalf_of account |

## Related Pages

- [[stripe-radar]] — concept page (updated with dispute resolution rules)
- [[source-stripe-disputes-prevention]] — dispute prevention overview (RDR/Ethoca)
- [[source-stripe-radar-rules]] — transaction rule structure

## Raw Sources

- [[stripe-radar-rules-disputes-2026]] — verbatim dispute resolution rules reference
