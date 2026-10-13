---
title: "Adyen Docs: In-person tipping options"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping"
raw_files:
  - "adyen/docs/point-of-sale/tipping/2026-09-15.md"
tags: [adyen, point-of-sale, tipping, terminal-api, gratuity]
---

## Overview

This Adyen Docs overview is a **navigation and choice guide** for adding gratuity to in-person payments. It distinguishes three integrated-payment paths by **who supplies the tip and when money is authorized or captured**: a POS-app proposal accepted or changed on the terminal, a terminal prompt or total entry by the shopper, and a written receipt tip handled after the initial pre-authorization. It separately points standalone merchants to an account-configured terminal tip prompt. See [[adyen-terminal-api]] and [[adyen]].

## Key takeaways

- **From the POS app:** the merchant POS puts a suggested tip amount in its payment request. The shopper can accept, change, or decline it on the terminal before completing that payment. This is a during-payment tip proposal, not a later authorization adjustment. [Raw: options list, Tipping from the POS app]
- **From the terminal:** the merchant payment request triggers a terminal prompt with fixed/percentage/custom options or a total-amount entry prompt. The shopper chooses a tip, enters an amount or higher total, or declines. This overview does not define the exact request fields, enablement, supported methods, or terminal software for those variants. [Raw: options list, Tipping from the terminal]
- **On the receipt:** the merchant makes a pre-authorization request; after completing payment, the shopper can write a tip on the receipt. If needed, the merchant increases the original authorization, then manually captures the final amount. This is a later amount/capture path and should not be merged with the two terminal-choice flows. [Raw: options list, Tipping on the receipt]
- **Standalone:** Adyen says it can configure an account to prompt automatically for a tip with every standalone payment. The page links separate standalone setup rather than describing a POS Terminal API request. This statement is not proof that a particular account is configured. [Raw: Using our Standalone solution?; implementation links]

## Detail locators

- Raw `Using our Standalone solution?` and the three bullets before `How do you want to implement tipping?` contain the page's substantive scope and timing distinctions.
- Raw `How do you want to implement tipping?` repeats navigation links to the POS-app, terminal, receipt, and standalone detail guides. Their detailed version, method, region, hardware, configuration, and legal conditions were not read for this overview.
- The overview gives no specific card-method or country eligibility, numeric tip limit, or current legal rule; use the linked detailed sources and current applicable guidance for those questions.

## Related

- [[adyen-terminal-api]] — existing in-person concept and separate detailed tipping routes
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/2026-09-15|Tipping — Adyen Docs snapshot, 2026-09-15]]
