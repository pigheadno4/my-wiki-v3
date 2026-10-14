---
title: "e285p and e285 user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/e285-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e285p, e285, user-manual]
---

## Overview

Adyen's e285p/e285 user manual, captured 2026-09-15, covers physical inspection, first setup and boarding, connectivity and diagnostics, battery care, menus, device information and support. Use [[adyen-payment-terminals]] as the physical-terminal model route and [[adyen-terminal-management]] for fleet assignment and boarding context. This dated manual does not establish current order availability, carrier coverage, account enablement, terminal integrity, or a successful payment.

## Key takeaways

- The snapshot labels both models discontinued and says neither can be newly ordered. It says Adyen repairs existing e285p terminals until April 2029 but does not repair e285 terminals, and recommends AMS1 instead. Treat these as the manual's dated statements, not a present-day inventory or service check.
- The standard e285 is stated to support terminal software only through 1.86. A later generic menu note says terminals from software 1.90 share a menu structure; do not assume that newer menu structure applies to a standard e285. The manual gives no equivalent e285p software ceiling.
- The first-setup sequence calls for inspection, at least four hours of charging, network configuration, boarding with a store selection, then separate Adyen-platform and POS-system connection tests. It says boarding can take up to 30 minutes; if the boarding option is absent, it advises waiting for the next platform synchronization (on average three hours) and trying again. These are manual instructions and estimates, not proof of boarding or payment success.
- On receipt, compare box/order/device serials and inspect packaging and hardware for tampering; contact Adyen Support immediately if a check fails. Passing those checks does not itself certify the device's security. The terminal lacks 4G and later cellular technology, so the manual warns that 2G/3G network shutdowns affect reliance on cellular connectivity. Its cellular-failover statement is qualified for terminals boarded before 2022 whose SIM subscription may not have been activated.
- For stored batteries, the manual advises 40–70% charge, cool/dry storage, and six-month checks for leakage or swelling. It says to dispose of a faulty battery under local rules and never include it in a terminal return package because of leakage and thermal-discharge risk. It specifies a 5V DC, 1A charger and use of the supplied USB-C cable.
- Settings access for Network, Software, Configuration and Power, and certain standalone transaction actions, is passcode-protected. The menu lists configuration removal, totals reset and a standalone “Bypass PIN” entry; this catalog does not establish that a particular account or transaction is eligible for those actions.

## Detail locators

- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#e285p and e285 user manual|Model notice and components]] — discontinuation, repair, 4G/software limits, charger and components (lines 15–47).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Get started|Get started]] — inspection, charging, network, store boarding and two connection tests (lines 49–67).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Inspect the terminal|Inspect the terminal]] — serial/packing/device checks and failed-check support escalation (lines 69–84).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Connect to your network|Connect to your network]] — Wi-Fi, conditional cellular failover and physical-SIM handling (lines 86–141).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Test the payments platform connection|Connection diagnostics]] and [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Test the POS system connection|POS-system diagnostics]] — separate terminal diagnostic checks (lines 143–161).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Maintain battery performance|Maintain battery performance]] and [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Use the USB-C charging cable|USB-C charging cable]] — storage, failure/return and cable-care warnings (lines 183–220).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Payment terminal menus|Payment terminal menus]] — passcodes and action list; note the 1.90 general menu claim against the standard e285's stated 1.86 maximum (lines 222–258).
- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Device info|Device info]] and [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15#Troubleshooting|Troubleshooting]] — identification, diagnostics and support information (lines 260–286).

## Related

- [[adyen]] — provider context and dated website-source catalog.
- [[adyen-payment-terminals]] — model and physical-device retrieval route.
- [[adyen-terminal-management]] — store assignment, boarding and fleet administration.
- [[adyen-terminal-api]] — separate POS-to-terminal messaging route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/e285-user-manual/2026-09-15|e285p and e285 user manual (fetched 2026-09-15)]]