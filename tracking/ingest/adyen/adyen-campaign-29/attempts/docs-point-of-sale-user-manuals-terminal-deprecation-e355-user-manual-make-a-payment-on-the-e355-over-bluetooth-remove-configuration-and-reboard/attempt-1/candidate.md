---
title: "Adyen e355 remove configuration and reboard"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/remove-configuration-and-reboard"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/remove-configuration-and-reboard/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e355, bluetooth, reboarding, historical]
---

## Overview

This [[adyen]] guide, captured and last modified 2026-09-15, describes a **destructive e355 merchant-configuration erase** followed by a separate boarding guide in the historical Bluetooth-payment manual tree. It does not establish that erasing automatically reboards the device, restores a Bluetooth pairing, resolves a fault, enables current e355 transactions or processes a payment. The parent [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] lists a historical e355 “No more transactions” date of 29 March 2024. See [[adyen-payment-terminals]].

## Key takeaways

- **Skip condition:** if the terminal is already boarded **and** the app and terminal have the same settings, the page says this step can be skipped. It does not define how to test settings equivalence, so the condition should not be assumed from “already boarded” alone. See raw lines 14–16.
- Otherwise, the action is to **remove the current merchant configuration from the terminal**. The guide enters the Admin menu via the pictured confirm key plus **9**, then selects **3. Configuration → 6. Erase**, confirms with the pictured key, and says the terminal reboots. Erase is consequential; the page does not describe a rollback or preserve any current merchant configuration through it. See raw lines 18–27.
- **Reboarding is a separate next step**: the page links the e355 boarding procedure after reboot. The linked historical guide supplies its own internet/security and app-flow conditions; the erase/reboot line is not evidence that registration, merchant-configuration update or Bluetooth pairing succeeded. See raw lines 29–31 and [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-board-the-terminal-e355]].
- Although this page has a 2026 last-modified timestamp, its subject is an e355 under terminal deprecation. The old device transaction cutoff in the parent page prevents using this procedure as proof of current activation or a safe way to resume live payments. See the linked parent deprecation source.

## Detail locators

- **Already-boarded/same-settings skip condition:** raw lines 14–16.
- **Destructive merchant-configuration erase and reboot:** raw lines 18–27.
- **Separate reboarding route:** raw lines 29–31.

## Related

- [[adyen-payment-terminals]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation-e355-user-manual-board-the-terminal-e355]]
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/remove-configuration-and-reboard/2026-09-15|e355 configuration erase and reboard — collected 2026-09-15]]
