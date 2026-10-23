---
title: "Adyen e315 legacy terminal LED status colors"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/understand-the-led-colors-e315"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/understand-the-led-colors-e315/2026-09-15.md"
tags: [adyen, point-of-sale, e315, terminal-leds, legacy]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] e315 manual table maps terminal LED behaviors to named status labels. It sits in the terminal-deprecation subtree and is a historical model-specific interpretation aid, not evidence of current e315 support or a diagnostic result for a particular terminal. See [[adyen-payment-terminals]].

## Key takeaways

- **Green:** A blink every four seconds is labeled Sleep; continuously on is Normal Operation. See pinned raw lines 20–22 and 27.
- **Red and orange:** Red at 1 Hz/50% duty cycle with 3.7 V battery voltage is Battery Low; red at 4 Hz/50% with 3.6 V is Battery Extremely Low. Orange at 1 Hz/50% is Battery Charging; continuously on is Charging Timer Fault. These are the table's stated indicator patterns and conditions, not a diagnosis of the cause or repair instruction. See pinned raw lines 23–26.
- **LEDs off:** The table labels Off as LEDs turned off **when charging the terminal on a gang charger**. Do not read Off alone as proof that the device has no power or has completed charging. See pinned raw line 28.

## Detail locators

- Complete behavior/status table, including frequency, duty cycle, voltage and gang-charger condition: pinned raw lines 20–28.

## Related

- [[adyen-payment-terminals]] — physical-terminal model context.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — separate deprecation timeline and model scope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e315-user-manual/understand-the-led-colors-e315/2026-09-15|e315 LED-color table, captured 2026-09-15]]
