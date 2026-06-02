---
title: "Stripe — Radar Rules Reference"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-rules-reference-2026.md"
tags: [stripe, radar, rules, reference, attributes, operators, metadata, velocity, avs, cvc, boolean]
---

## Summary

Complete technical reference for Radar rule syntax: processing order, attribute types, operators, metadata patterns, missing attribute handling, velocity attributes, and complex conditions.

## Rule Processing Order

1. Request 3DS (evaluated first)
2. Allow (stops evaluation — no block/review applied)
3. Block (stops evaluation — no review applied)
4. Review

First match wins; same-action-type rules are unordered.

## Attribute Types

| Type | Syntax | Operators | Notes |
| --- | --- | --- | --- |
| String | `:attribute:` | `=`, `!=`, `IN`, `INCLUDES`, `LIKE` | Case-insensitive |
| Metadata | `::field::` | All (string ops + numeric if number) | **Case-sensitive** |
| Country | `:attribute:` | `=`, `!=`, `IN`, `INCLUDES`, `LIKE` | Must be 2-letter ISO code |
| State | `:attribute:` | `=`, `!=`, `IN`, `INCLUDES`, `LIKE` | ISO without country prefix (e.g. `CA` not `US-CA`) |
| Numeric | `:attribute:` | `=`, `!=`, `<`, `>`, `<=`, `>=`, `IN` | — |
| Boolean | `:attribute:` | None (no operator/value) | False (not missing) when attribute absent |

## Metadata Syntax

| Scope | Syntax |
| --- | --- |
| Payment metadata | `::field::` |
| Customer metadata | `::customer:field::` |
| Destination metadata | `::destination:field::` |
| Account metadata (Platforms) | `::account:field::` |

Metadata is case-sensitive. Supports `IN ('a', 'b')` and `INCLUDES 'substring'`.

## Operators Table

| Operator | String/Country/State | Numeric | Metadata |
| --- | --- | --- | --- |
| `=` / `!=` | ✓ | ✓ | ✓ |
| `<` / `>` / `<=` / `>=` | ✗ | ✓ | ✓ |
| `IN` | ✓ | ✓ | ✓ |
| `INCLUDES` | ✓ | ✗ | ✓ |
| `LIKE` (% wildcard) | ✓ | ✗ | ✓ |

## Missing Attributes

- Any comparison with a missing attribute returns **false** (including `!=`)
- `NOT` of a missing attribute comparison also returns **false**
- Use `is_missing(:attr:)` to explicitly check
- Boolean attributes are **false** (not missing) when absent
- Example: `Review if is_missing(:email_domain:) OR :email_domain: IN ('yopmail.net')`

## AVS/CVC Post-Authorization Attributes

Values: `pass`, `fail`, `unavailable`, `unchecked`, `not_provided`. Rules using these execute after other rules. May create temporary auth hold on card even if ultimately blocked.

## Velocity Attributes

| Interval | Lookback window | Bucket size |
| --- | --- | --- |
| `hourly` | 3,900s | 5 min |
| `daily` | 90,000s | 1 hour |
| `weekly` | 608,400s | 1 hour |
| `yearly` | 31,622,400s | 1 day |
| `all_time` | 5 years | 1 day |

Count excludes current payment. Bounded attributes cap at a maximum value.

## Currency Conversion

`amount_in_xyz` auto-converts: 900 GBP blocked by a `> 1000 USD` rule if converted value exceeds threshold.

## Complex Conditions

`AND`/`OR`/`NOT` (or `&&`/`||`/`!`) with standard C/Python precedence. Use parentheses to group. Example:

`Block if :card_country: != 'US' and :risk_level: = 'elevated'`

## Lists Reference

`{action} if :attribute: in @list_alias` — list alias must start with `@`.

## Related Pages

- [[stripe-radar]] — concept page (updated with reference details)
- [[source-stripe-radar-rules]] — rules overview (actions, built-in rules, Radar Assistant)
- [[source-stripe-radar-lists]] — list management

## Raw Sources

- [[stripe-radar-rules-reference-2026]] — verbatim Radar rules reference (408 lines)
