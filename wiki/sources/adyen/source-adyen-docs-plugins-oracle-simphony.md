---
title: "Adyen Oracle Simphony POS integration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/oracle-simphony"
raw_files:
  - "adyen/docs/plugins/oracle-simphony/2026-09-15.md"
tags: [adyen, oracle-simphony, hospitality, point-of-sale]
---

## Overview

This 2021-modified Adyen webpage snapshot describes an **Oracle Simphony** hospitality POS integration using **Oracle Payment Interface (OPI)** and Adyen payment terminals. It covers restaurant-style **Pay at counter** and **Pay at table** routing. It is a Simphony-specific guide, not an Oracle Xstore retail or OPERA PMS implementation reference, and it does not demonstrate a live payment, terminal boarding, refund, or settlement outcome. See [[adyen]] and [[adyen-oracle-simphony]].

## Key takeaways

- The page says Adyen payment terminals implement **OPI 6.2** for Simphony and that the plugin can integrate with a Simphony device compatible with **OPI 6.2 and later** (raw lines 23–29). It does not list supported terminal models, exact plugin/package versions, or every later OPI revision's tested compatibility.
- Before integration, create an Adyen **test account** and contact Support to **enable OPI in Customer Area** (raw lines 31–37). This is an enablement prerequisite, not evidence that a specific merchant has OPI access.
- OPI maps a transaction to the terminal list and sends the Simphony request to the specified Adyen terminal (raw lines 39–43). The page describes **Pay at counter** as the default, with POS billing information sent to the terminal; **Pay at table** is optional (lines 45–55).
- The Pay at table description includes bill retrieval/display on a portable terminal, printing, amount splitting, and optional tip in its user-flow example (raw lines 53–64). These are described capabilities and an example sequence, not proof that a particular configuration supports every option or that the illustrated payment was approved.

## Detail locators

- `Supported versions` and `Get started`, raw lines 27–37: OPI compatibility, test account and Support enablement.
- `How it works`, raw lines 39–43: Simphony–OPI–terminal request routing.
- `Features`, raw lines 45–64: counter/table distinction and example table flow.

## Related

- [[adyen-oracle-simphony]] — Simphony hospitality integration route.
- [[adyen-oracle-xstore]] — distinct Oracle retail POS product; do not transfer its compatibility/features to Simphony.
- [[adyen-terminal-api]] — provider-wide terminal interface boundary, separate from this OPI route.

## Raw Sources

- [[raw/adyen/docs/plugins/oracle-simphony/2026-09-15|Oracle Simphony, fetched 2026-09-15]]
