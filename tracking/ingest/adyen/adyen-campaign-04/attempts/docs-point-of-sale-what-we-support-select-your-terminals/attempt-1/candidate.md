---
title: "Select payment terminals | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/select-your-terminals"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/select-your-terminals/2026-09-15.md"
tags: [adyen, point-of-sale, terminals, hardware, pci-pts]
---

## Overview

This Adyen point-of-sale terminal catalog snapshot helps a merchant shortlist physical payment-terminal models by use case, listed countries/regions, Integrated or Standalone suitability, features, connectivity, and displayed PCI PTS label. It points to separate mobile Tap to Pay/card-reader solutions when no physical terminal is needed. The 2026-09-15 capture is a historical selection aid, not an order-availability check, certification lookup, software-version matrix, accessibility assessment, current merchant support decision, or security audit.

## Key takeaways

- Each model entry must be read as a bundle: mobile, countertop or unattended use case; geography; Integrated/Standalone suitability; network and peripheral features; and its stated PCI PTS 5 or 6 label. Model names and feature lists do not establish suitability for every region, software release or integration architecture.
- The catalog describes Android models such as AMS1, S1E2L and S1F2 as capable of hosting POS and other apps, with differing cameras, scanners, printers, connectivity and suitability. It also lists Verifone and other non-Android entries. The page does not specify Android or terminal software versions, application certification, app-store entitlement, SDK compatibility, or accessibility features.
- The page states that PCI PTS 5 terminals cease being available for order starting April 30, 2026. It independently marks UX410 unavailable for new orders and recommends S1U2. The broad Europe listing for S1E4Pro is narrowed by a specific note that the model is not available in Germany in this snapshot. V240m Plus is described as Brazil-only. Check such exceptions before relying on a region cell.
- A displayed PCI PTS label is a catalog attribute, not proof of current certification validity, security of a merchant's terminal deployment or compliance of its POS app. Likewise, a listed country/region is not proof of a particular merchant's ability to order or activate the model now. The linked model manuals can guide later research but were not used as behavioral evidence here.

## Detail locators

- `# Terminals` and `## Available filters` — purpose, mobile-alternative route, PTS 5 order notice and selection dimensions.
- `## Terminal catalog` — model headings for AMS1, e285p, M400, M450, P400 Plus, P630, S1E2L, S1E4Pro, S1F2, S1F4Pro, SFO1, S1U2, UX300, UX410, V240m Plus, V400c Plus, V400m, and V400m with base station. Each entry supplies its own use case, region, connectivity, suitability, features and PCI PTS label where present.
- `S1E4Pro (Android)`, `UX410`, and `V240m Plus` — Germany exclusion, no-new-orders warning, and Brazil-only statement, respectively.
- Model-name links point to user manuals for further research; this source does not supply software versions, certification status beyond displayed PCI PTS labels, accessibility specifications, or deployed-security controls.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]] (the in-person integration hub; hardware catalog scope is distinct from API message behavior)

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/select-your-terminals/2026-09-15|2026-09-15 Adyen terminal catalog]]
