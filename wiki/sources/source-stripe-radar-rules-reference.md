---
title: "Stripe — Radar Rules Reference"
type: source
date_ingested: 2026-05-10
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/radar/rules/reference"
raw_files:
  - "stripe-radar-rules-reference-2026-11-07.md"
  - "stripe-radar-rules-reference-2026.md"
tags: [stripe, radar, rules, reference, attributes, operators, metadata, velocity, avs, cvc, boolean]
---

## Summary

The May 10 and November 7, 2026 captures describe how Stripe evaluates merchant-configured Radar rules for payments and eligible Connect accounts. The November capture also documents a separate private preview for connected-account Treasury transactions.

## Rule Processing Order

1. **Request 3DS.** Request issuer authentication where supported with Payment Intents API or Checkout. Radar still evaluates later Allow, Block and Review stages whether or not the 3DS request rule matches.
2. **Allow.** Proceed with normal payment processing and skip later Radar Block and Review rules. The issuer can still decline.
3. **Block.** Stripe rejects a matching payment and skips further evaluation.
4. **Review.** Stripe processes the payment and charges the customer, then places the payment in review.

Rules within each action type are unordered. Both captures use broad wording about stopping after a match and separately spell out that evaluation continues after Request 3DS (May raw lines 54–74, November lines 55–75). The earlier wiki summary of the Rules overview described Allow as overriding all other rules and Request 3DS as triggering authentication. The May 2026 Rules overview capture states that the issuer might not perform the requested authentication (line 88). See [[source-stripe-radar-rules]].

## Connected Account Actions

An eligible platform can raise a connected account for review or raise a review and pause its payouts while under review. Reviews appear in the Radar review queue in Connected accounts. Stripe recommends starting with review before enabling automatic payout pauses. May names Radar for Platforms. November conditions access on a Radar plan that supports the platform feature and links to the plan comparison. See May raw lines 37–39 and 76–89 and November lines 38–40 and 77–90.

## Treasury Transaction Actions (Private Preview)

The November capture covers inbound transfers and received credits on connected accounts. **Block** rejects a matching Treasury transaction and stops rule evaluation. **Review** lets Stripe process the transaction and gives the platform an opportunity to examine it. See November raw lines 92–102.

## Attribute Types

| Type | Syntax | Operators | Notes |
| --- | --- | --- | --- |
| String | `:attribute:` | `=`, `!=`, `IN`, `INCLUDES`, `LIKE` | Case sensitivity depends on the attribute. |
| Metadata | `::field::` | String or numeric operators according to use | Case-sensitive when used as a string. |
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

Metadata is case-sensitive when used as a string. Supports `IN ('a', 'b')` and `INCLUDES 'substring'`.

> **Account metadata delimiter (2026-05-10 and 2026-11-07).** Both captures show a closing double colon in the generic account-metadata syntax and a single closing colon in the worked example. The captures leave acceptance of the single-colon form unresolved. See May raw lines 184–198 and November lines 197–211.

## Operators Table

| Operator | String/Country/State | Numeric | Metadata |
| --- | --- | --- | --- |
| `=` / `!=` | ✓ | ✓ | ✓ |
| `<` / `>` / `<=` / `>=` | ✗ | ✓ | ✓ |
| `IN` | ✓ | ✓ | ✓ |
| `INCLUDES` | ✓ | ✗ | ✓ |
| `LIKE` (% wildcard) | ✓ | ✗ | ✓ |

> **String operators (2026-05-10 and 2026-11-07).** Both matrices list `IN`, `INCLUDES` and `LIKE` for String, and both prose sections describe `INCLUDES` for string attributes. The invalid-condition example correctly flags `:risk_level: < 'highest'`, but its equality-only gloss conflicts with that general matrix. Other operators on `risk_level` individually remain unresolved. The paired [[source-stripe-radar-rules-supported-attributes]] captures document `customer` as case-sensitive and `risk_level` as case-insensitive.

## Missing Attributes

- Any comparison with a missing attribute returns **false** (including `!=`)
- `NOT` of a missing attribute comparison also returns **false**
- Use `is_missing(:attr:)` to explicitly check
- Boolean attributes are **false** (not missing) when absent
- Example: `Review if is_missing(:email_domain:) OR :email_domain: IN ('yopmail.net')`

## AVS/CVC Post-Authorization Attributes

Issuer AVS and CVC checks return `pass`, `fail`, `unavailable`, `unchecked` or `not_provided`. Radar evaluates rules using these checks after rules without them. A customer can see a temporary card authorization even if the charge is ultimately blocked. Stripe cautions that requiring `pass` can exclude legitimate payments when verification is unavailable, such as wallet payments that omit CVC.

## Velocity Attributes

| Interval | Documented velocity upper bound | Bucket size |
| --- | --- | --- |
| `hourly` | 3,900 seconds | 5 minutes |
| `daily` | 90,000 seconds | 1 hour |
| `weekly` | 608,400 seconds | 1 hour |
| `yearly` | 31,622,400 seconds | 1 day |
| `all_time` | 31,622,400 seconds | 1 day |

Both captures say `all_time` includes five years of data and separately describe the velocity upper bound above. See May raw lines 386–398 and November lines 399–411.

Count excludes current payment. Bounded attributes cap at a maximum value.

## Currency Conversion

`amount_in_xyz` auto-converts: 900 GBP blocked by a `> 1000 USD` rule if converted value exceeds threshold.

## Complex Conditions

`AND`/`OR`/`NOT` (or `&&`/`||`/`!`) with standard C/Python precedence. Use parentheses to group. Example:

`Block if :card_country: != 'US' and :risk_level: = 'elevated'`

## Lists Reference

`{action} if :attribute: in @list_alias` — list alias must start with `@`. Stripe cautions EU businesses about the Geo-blocking Regulation’s prohibitions on blocking payments from customers based in EU member states.

## Related Pages

- [[stripe]] — company page
- [[stripe-radar]] — Radar concept
- [[source-stripe-radar-rules-supported-attributes]] — attribute catalog and dated applicability
- [[source-stripe-radar-rules]] — rules overview (actions, built-in rules, Radar Assistant)
- [[source-stripe-radar-lists]] — list management

## Raw Sources

- [[raw/stripe-radar-rules-reference-2026-11-07|November 7, 2026 Radar Rules reference]]
- [[stripe-radar-rules-reference-2026]] — May 10, 2026 verbatim Radar rules reference (408 lines)
