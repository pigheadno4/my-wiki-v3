---
title: "Adyen terminal 2G/3G coverage sunset"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/end-of-3g"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/end-of-3g/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, cellular-connectivity, 2g, 3g, network-sunset]
---

## Overview

This Adyen Docs page is a dated terminal-connectivity planning note about mobile operators ending 2G/3G coverage. Terminals limited to those cellular generations cannot accept payments when a transaction depends on that unavailable cellular path. The page names affected models, gives a nondefinitive country/region table, and suggests other connectivity or hardware routes. See [[adyen]] and [[adyen-terminal-api]] for provider and POS context. It does not establish current carrier coverage, terminal availability, network configuration, local/cloud POS connectivity, or payment outcomes.

## Key takeaways

- The page identifies e285, e285p, V240m Plus, and VX690 as terminal models whose cellular connections support at most 3G. It says V240m Plus is used only in Brazil and, in the page's own time frame, reports no then-current adverse impact because Brazilian operators did not intend a near-term 3G shutdown. That historical statement is not a live Brazil coverage check.
- The country/region table mixes completed shutdowns, projected years, and unspecified dates. Adyen expressly says the list is incomplete and should not be used for the latest status; ask the relevant local mobile network operator. Some table entries still use future-tense 2025 projections in the 2026-09-15 capture, reinforcing that these rows are historical planning evidence rather than verified current status. Keep any country or carrier decision tied to a fresh operator check.
- For the named models using 2G/3G, the page says a terminal can fall back from 3G to 2G if 2G is available. It warns that 2G coverage is also ending and that configuration and software updates over 2G can be slow or interrupted. Fallback is conditional on actual 2G service, not a durable fix.
- The alternatives listed are attaching affected terminals over Wi-Fi to a router with a 4G cellular connection, or ordering newer terminals with similar capabilities that support 4G. These are possible connectivity/hardware changes, not a claim that the older terminal's modem becomes 4G-capable or that every POS integration and payment will work without further network, software, or account checks.
- The page concerns the terminal's cellular path to service. It does not specify Terminal API local versus cloud POS-message transport, POS app internet availability, firmware versions, carrier support per device, or SDK requirements. Follow those separate routes before inferring an end-to-end integration result.

## Detail locators

- Sunset mechanism and conditional payment impact: `# End of 2G/3G network coverage`, raw lines 15–25.
- Affected terminal models and Brazil-specific historical statement: `## Terminals affected`, raw lines 27–35.
- Nondefinitive country/region table and explicit operator-verification warning: `## Countries/regions affected`, raw lines 37–79. The table's country and year values are a 2026-09-15 snapshot, not current carrier status.
- Conditional 2G fallback, software-update warning, 4G-router-over-Wi-Fi option, and 4G terminal replacement: `## Possible solutions`, raw lines 81–92.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — POS terminal integration route; its local/cloud paths and versioned GitHub evidence have separate provenance.

## Related raw API references

- The raw page links to model manuals, cellular failover, and terminal-selection pages. They are navigation until independently read; see raw lines 31–33 and 90–96.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/end-of-3g/2026-09-15|Adyen Docs: End of 2G/3G network coverage (2026-09-15 snapshot)]]
