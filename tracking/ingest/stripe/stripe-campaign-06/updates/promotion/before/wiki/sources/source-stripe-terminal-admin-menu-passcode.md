---
title: "Stripe Terminal: Configure the Admin Menu Passcode"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-admin-menu-passcode-2025.md"
tags: [stripe, stripe-terminal, configurations, fleet, security, admin-menu]
---

## Summary

The admin menu on smart readers (wifi settings, appearance, diagnostics) is protected by a 5-digit passcode. Default is `07139` — should be changed for security.

## Key Details

**Hierarchy**: same as other configurations — account-level default overrides Stripe default; location-level overrides account default.

**Propagation**: 10 minutes.

**Permissions**:
- View passcodes: Super Admin, Admin, Terminal Specialist, Developer
- Modify passcodes: Super Admin, Admin, Terminal Specialist

**API field**: `reader_security[admin_menu_passcode]` on the Configuration object (create or update).

**Dashboard**: configure from location details page or manage locations page; toggle to enable custom vs Stripe default.

## Raw Sources

- [[stripe-terminal-admin-menu-passcode-2025]] — verbatim webpage content
