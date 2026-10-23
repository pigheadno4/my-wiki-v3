---
title: "Adyen e315 legacy terminal Admin menu access"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/use-the-admin-menu-e315"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/use-the-admin-menu-e315/2026-09-15.md"
tags: [adyen, point-of-sale, e315, admin-menu, legacy]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] e315 manual page describes how to open the terminal's Admin menu with version-specific key sequences and an Admin PIN. It names chip/magnetic-stripe transactions, totals printing and refunds as menu functions, but it does not provide a PIN, prove a particular user can access the menu, or document completion of those operations. The page is in a terminal-deprecation subtree and does not establish current e315 support. See [[adyen-payment-terminals]].

## Key takeaways

- **Version 1.11 and earlier:** The page shows an illustrated four-button sequence, then asks for the Admin-menu PIN. The button images are linked in the pinned raw; use those illustrations for exact physical-button identification rather than inferring labels from image file names. Unknown PINs route to the separate POS Troubleshooting Admin PIN guide. See pinned raw lines 20–23.
- **Version 1.14 and later:** The page shows an illustrated first button followed by `1`, `5`, `9`, then the Admin-menu PIN. The guide gives no route for versions 1.12–1.13; do not silently apply either sequence to that gap. See pinned raw lines 25–28.
- **Action boundary:** Opening the PIN-protected menu is distinct from performing a transaction, refund or totals print. The page provides no refund procedure or destructive device action. See pinned raw lines 16–28.

## Detail locators

- Named menu functions and version-specific illustrated key sequences: pinned raw lines 14–28.
- Admin PIN requirement and troubleshooting route: pinned raw lines 23 and 28.

## Related

- [[adyen-payment-terminals]] — physical-terminal model context.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate historical terminal-deprecation scope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/use-the-admin-menu-e315/2026-09-15|e315 Admin menu guide, captured 2026-09-15]]
