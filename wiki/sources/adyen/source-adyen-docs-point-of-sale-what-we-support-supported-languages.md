---
title: "Locations and languages | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/supported-languages"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/supported-languages/2026-09-15.md"
tags: [adyen, point-of-sale, in-person-payments, countries, terminal-languages]
---

## Overview

This Adyen Docs page is a captured support table for Adyen **in-person payments across all integration types**. It lists countries/regions for point-of-sale availability and the user-interface languages that payment terminals can show on their **latest software version**. Its Mobile-solutions and legacy-terminal caveats matter when using the table. See [[adyen]]; [[adyen-terminal-api]] is a related in-person API route, but this page is broader than Terminal API.

## Key takeaways

- The country/region tables group supported in-person payment locations under the Americas, APAC, Europe, and Middle East. The United Kingdom entry includes Guernsey and the Isle of Man but excludes Jersey and other UK overseas territories and crown dependencies. The United Arab Emirates note says Verifone payment terminals have no 5 GHz network coverage there. These are captured support-table claims, not account-specific merchant, acquiring, device, payment-method, or current regional eligibility proof.
- **Mobile solutions do not yet support all listed countries/regions** in this snapshot; the page directs readers to a separate Mobile-solutions supported-regions page for status. The main geographic table must not be applied wholesale to a Mobile solution.
- The terminal-language table concerns the **user interface on payment terminals**, and is qualified by the terminal being on the **latest software version**. It lists language labels in the raw table, including regional variants such as English (Canada), German (Germany), Portuguese (Brazil), and Portuguese (Portugal). One cell is literally labeled **Russia**; do not silently reinterpret that table cell as a verified language code or locale.
- A separate language table applies to legacy models e315, e355, MX925, VX675, VX680, VX690, VX820, and VX820 Duet, which the page says are being deprecated for PCI-compliance reasons. It also conditions those language capabilities on the latest software version. Do not substitute the main terminal table for the legacy-model table.
- The source does **not** define how a terminal chooses a default UI language, how a shopper selects a language, whether a receipt follows that choice, terminal system-language behavior, BCP-47/ISO codes, or a Terminal API field to control language. Use the raw tables for the exact support labels; obtain selection and receipt behavior from a separately read authority.

## Detail locators

- `Locations and languages` / `Requirements`, lines 15–27: purpose and all-in-person-integration scope.
- `Supported countries/regions`, lines 29–57: Americas, APAC, Europe, Middle East tables and UK/UAE footnotes.
- `Countries/regions in Mobile solutions`, lines 59–62: Mobile geographic coverage exception and separate status link.
- `Languages on the terminal`, lines 64–75: latest-software qualifier and main terminal UI-language table; preserve table labels exactly.
- `Legacy terminals`, lines 77–90: deprecated model list, latest-software qualifier, and separate legacy UI-language table.
- `See also`, lines 92–94: supported payout-currencies link is navigation, not evidence about terminal locale or receipts.

## Related

- [[adyen]] — provider page and in-person support route.
- [[adyen-terminal-api]] — related in-person API concept; this source also covers non-Terminal-API Adyen integrations.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/supported-languages/2026-09-15|Locations and languages (2026-09-15 snapshot)]]
