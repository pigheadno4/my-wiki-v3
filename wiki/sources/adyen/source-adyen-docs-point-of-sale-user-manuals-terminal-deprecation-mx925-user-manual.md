---
title: "Adyen MX925 terminal user manual (deprecated model)"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, mx925, deprecated]
---

## Overview

This 2021-modified, 2026-09-15-captured MX925 payment-terminal manual is a short **historical** quickstart in Adyen's terminal-deprecation subtree. It explicitly says new terminals of this type cannot be ordered and points to the eVo-terminal deprecation guide. The separately captured eVo deprecation table lists MX925 **“No more transactions” on 29 March 2024** (see [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]], its pinned raw lines 32-35). That is a dated published cutoff, not a live account/device observation. Its setup checklist is not evidence of current ordering, support, certification, boarding capability or successful payment processing. [[adyen]] [[adyen-payment-terminals]]

## Key takeaways

- The page says new MX925 terminals cannot be ordered. The quickstart's reference to getting a “new terminal” running and its closing “ready to process payments” statement must be read as historical manual wording, not current processing guidance: the separately captured deprecation table lists the MX925 no-transactions cutoff as **29 March 2024**. See this manual's raw lines 15-19 and 23-37, and the deprecation guide's pinned raw lines 32-35.
- Its stated sequence is to connect power to the PED, connect Ethernet to the **ETH port on the power cable**, perform the linked device security inspection, and board the terminal using the linked model-specific guide. The page does not give the inspection or boarding procedure itself. See raw lines 23-35.
- **Physical damage warning:** the manual says a wrong cable in a wrong port, such as Ethernet in RS232, might severely damage the device. Do not treat the pictured device or a similar-looking port as a substitute for the stated cable/port guidance. See raw lines 27-31.
- The supplied-component list names the MX 925 PED, power supply and Ethernet dongle. It does not specify firmware, network configuration, merchant-account roles or a current replacement model; those details belong to their linked or separate guides. See raw lines 39-43.

## Detail locators

- Opening and deprecation notice, raw lines 15-21.
- `## Quickstart`, raw lines 23-37: power/Ethernet order, cable-port damage warning, linked security inspection and boarding.
- `## Provided components`, raw lines 39-43: PED, power supply and Ethernet dongle.

## Related

- [[adyen-payment-terminals]] — model-specific physical-terminal documentation.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate eVo-terminal deprecation overview; this page itself only states new MX925 units cannot be ordered.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-mx925-user-manual-board-the-terminal-mx925]] — separate model-specific boarding guide.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/mx925-user-manual/2026-09-15|Adyen MX925 historical user manual, captured 2026-09-15]]
