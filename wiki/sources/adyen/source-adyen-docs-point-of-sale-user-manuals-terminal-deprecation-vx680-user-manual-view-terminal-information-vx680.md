---
title: "Adyen VX680 Quick Info device display (historical)"
type: source
date_ingested: 2026-10-23
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/view-terminal-information-vx680"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/view-terminal-information-vx680/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, vx680, quick-info, deprecation]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] VX680 manual page describes the terminal's **Quick Info** display for looking up network and device identifiers. It is a historical device-information route in the terminal-deprecation subtree, not proof of current connectivity, boarding or payment readiness. The separately captured [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation|eVo deprecation table]] lists VX680 under **29 March 2024 "No more transactions"**. See [[adyen-payment-terminals]].

## Key takeaways

- **Menu access:** The page says to press a pictured terminal key and `5` at the same time to open Quick Info. The first key is shown only as an image; identify it from the raw illustration, not the image filename. This page states no PIN or user-role step, so it does not establish either a required credential or unrestricted access. See pinned raw lines 19–25.
- **Displayed information:** The page lists IP address, terminal ID and software version. It also says a QR code encodes IP address, MAC address, network name, store name, merchant account name and terminal ID. These are listed display fields, not observed values for a specific device. See pinned raw lines 27–32.
- **Status boundary:** An IP address or software-version display alone does not test reachability, terminal boarding, current software eligibility or payment outcome. Consult the separate relevant diagnostics and model-deprecation sources for those questions.

## Detail locators

- Quick Info purpose and pictured-key + `5` access step: pinned raw lines 17–25.
- Directly displayed fields and QR-encoded identifiers: pinned raw lines 27–32.

## Related

- [[adyen-payment-terminals]] — physical-terminal model context.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate dated eVo transaction cutoff.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/vx680-user-manual/view-terminal-information-vx680/2026-09-15|VX680 Quick Info guide, captured 2026-09-15]]
