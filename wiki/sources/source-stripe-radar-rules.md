---
title: "Stripe — Fraud Prevention Rules"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-rules-2026.md"
tags: [stripe, radar, rules, fraud, block, allow, review, 3ds, cvc, avs, metadata, radar-assistant]
---

## Summary

Complete reference for Stripe Radar fraud prevention rules: built-in rules, rule types (allow/block/review/3DS), custom rule syntax, 3DS attributes, Radar Assistant, and best practices.

## 4 Rule Actions

| Action | Description | Requires |
| --- | --- | --- |
| Request 3DS | Triggers 3DS authentication | All tiers |
| Allow | Overrides all other rules | Fraud Teams (contact Stripe) |
| Block | Prevents payment processing | Fraud Teams / Platforms |
| Review | Sends to review queue | All tiers |
| Pause payouts | Pauses account payouts | Platforms only |

## Built-in Rules

| Rule | Default behavior | Notes |
| --- | --- | --- |
| `if :risk_level: = 'highest'` | Blocked | **Deprecated** — replaced by risk settings |
| `if :risk_level: = 'elevated'` | Review | Default for Fraud Teams / Platforms |
| `if :account_risk_level: = 'highest'` | Blocked | Platforms only |
| `if :account_risk_level: = 'elevated'` | Review | Platforms only |
| `if CVC verification fails based on risk score` | Optional | New CVC rule (Dec 17, 2024) — skips low-risk failures |
| `if Postal code verification fails based on risk score` | Optional | New AVS rule |

Legacy CVC/AVS rules (shown to existing users who enabled them): `if CVC verification fails`, `if postal code verification fails`.

## Rule Syntax

```
{action} if {attribute} {operator} {value}
```

- Custom metadata: `::field::` or `::customer:field::`
- List membership: `:attribute: in @list_alias`
- Max: **200 transaction rules**, **100 account rules**

## Key 3DS Attributes

| Attribute | True when | Use in |
| --- | --- | --- |
| `is_3d_secure` | Card supported + 3DS attempted + not failed | Block rules (recommended) |
| `is_3d_secure_authenticated` | 3DS fully authenticated | Stricter block (excludes exemptions) |
| `has_liability_shift` | Stripe expects liability shift (includes some wallets) | Allow rules |

**Don't block wallets without cryptogram**: `not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`

## Radar Assistant

Built-in LLM in rule editor. Natural language → Radar rule. Training data consent required.

## Best Practices

- Allow rules: minimal use (override everything); always add `and :risk_level: != 'highest'`
- Block rules: keep false positives low; test before enabling
- Review rules: target narrow criteria to avoid overwhelming queue
- Backtest against last 6 months before enabling
- EU note: Geo-blocking Regulation prohibits blocking EU-based customers by location

## Related Pages

- [[stripe-radar]] — concept page (updated with rules section)
- [[source-stripe-radar-lists]] — lists used in rules (`@list_alias`)
- [[source-stripe-radar-risk-settings]] — risk controls vs custom rules

## Raw Sources

- [[stripe-radar-rules-2026]] — verbatim Radar rules reference (454 lines, 5 screenshots)
