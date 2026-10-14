---
title: "Adyen get-started terminal manuals catalog"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, hardware-catalog, user-manuals]
---

## Overview

Adyen's “Get started manuals” page is a dated directory of physical payment-terminal models and their user manuals. It offers filters for use case, country/region, suitability, features, connectivity and PCI compliance, then lists model-specific descriptions and those fields. Each linked manual owns setup, network and menu procedures; the directory's rows are selection/navigation evidence, not proof that a model is currently sold, eligible for a particular account or region, certified at the present date, or able to complete a payment. The raw page was fetched 2026-09-15 and reports last modification 2026-04-15. [[adyen]] · [[adyen-payment-terminals]]

## Key takeaways

- **Physical-device scope:** The directory links mobile, countertop and unattended terminals, including Android and non-Android models. For a device-free Tap to Pay route or a mobile device paired with a card reader, it points to separate mobile solutions. Do not treat all catalog entries as Android terminals, standalone terminals or phone SDK flows.
- **Model comparison:** Each row is a snapshot of listed countries/regions, connectivity, suitable-for integration mode, hardware features and PCI PTS label. Consult the exact model row before claiming printer, PIN pad, replaceable battery, cellular generation, Android status or standalone suitability; these differ by model. The user manual link is a navigation route to model operating detail.
- **Ordering and locality exceptions:** The page states PCI PTS 5 terminals would no longer be available for order starting 2026-04-30; this is a dated ordering statement, not an independently verified current catalog. It states UX410 is no longer available for new orders and recommends S1U2. It lists V240m Plus only for Brazil and S1E4Pro as unavailable in Germany in this snapshot. These exceptions do not establish current stock or merchant-specific eligibility.
- **Representative mode distinctions:** The S1E2L row labels it Android, mobile and integrated; S1F2 and S1F4Pro rows list integrated and standalone with built-in printers; V400m and V240m Plus also list integrated and standalone. The UX410 description calls it a standalone self-service device while its `Suitable for` row says Integrated; preserve that unresolved wording difference rather than asserting a standalone configuration from this directory alone.

## Detail locators

- **Directory purpose, mobile alternative, dated PCI PTS 5 order statement and filters:** raw lines 15–29.
- **AMS1 through P630 rows:** raw lines 31–95; locate exact country, connection, feature and PTS labels by model heading.
- **S1E2L, S1E4Pro, S1F2, S1F4Pro, SFO1 and S1U2:** raw lines 97–161; note S1E4Pro Germany exception at line 110 and standalone labels only where the row says so.
- **UX300 and UX410:** raw lines 163–182; UX410's description and `Suitable for` row differ at 176–180, and its new-order exclusion is at line 176.
- **V240m Plus, V400c Plus, V400m and V400m with base station:** raw lines 184–226; Brazil-only V240m Plus at 184–193.

## Related

- [[adyen-payment-terminals]] — physical terminal hardware and model manuals
- [[adyen-android-terminals]] — separate Android-terminal model and on-device app guidance
- [[adyen-mobile-card-readers]] — separate paired mobile reader route
- [[adyen-standalone-terminals]] — direct-terminal solution boundary; inspect model-specific eligibility

## Related raw API references

This directory links individual model user manuals and mobile solutions. Those linked pages were not read for this entry; follow the relevant model manual for setup, security, battery, network and menu details.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/2026-09-15|Get started manuals directory, fetched 2026-09-15]]
