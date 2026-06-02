---
title: "Stripe — Configure Smart Disputes Auto-Respond Settings"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-disputes-smart-disputes-auto-respond-2026.md"
tags: [stripe, disputes, smart-disputes, connect, auto-respond, platform]
---

## Summary

Configuration guide for Smart Disputes auto-respond for direct accounts, Connect platforms, and connected accounts. Platforms can control and optionally delegate settings to connected accounts via API.

## Direct Accounts

Toggle at Dashboard → Settings → Disputes. Disabling auto-respond means any uncountered dispute is automatically lost.

## Connect Platforms

Set platform default + control override permissions at Dashboard → Settings → Connect → Disputes.

**API**: use `accounts.update` with `settings.smart_disputes.auto_respond`:

| Field | Type | Values |
| --- | --- | --- |
| `preference` | writable | `on`, `off`, `inherit` |
| `value` | read-only | `on`, `off` (actual effective setting) |

- `inherit` (default): inherits platform default; immediately reflects any future platform default changes
- Explicit `on`/`off`: overrides platform default; unaffected by future platform default changes
- Reset to `inherit` to re-enable platform default inheritance

Applies to direct charges and destination charges (including `on_behalf_of`). Platform's own disputes configured separately.

## Connected Accounts

View at Dashboard → Settings → Disputes (separate setting per platform). If platform disabled overrides, setting is locked — contact platform to change.

## Related Pages

- [[disputes]] — concept page
- [[source-stripe-smart-disputes]] — Smart Disputes overview
- [[source-stripe-smart-disputes-setup]] — Smart Disputes setup and API

## Raw Sources

- [[stripe-disputes-smart-disputes-auto-respond-2026]] — verbatim auto-respond configuration guide
