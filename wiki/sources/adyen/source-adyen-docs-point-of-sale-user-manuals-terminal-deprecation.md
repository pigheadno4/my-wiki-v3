---
title: "Adyen eVo terminal deprecation schedule"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, evo, deprecation, historical]
---

## Overview

This [[adyen]] page was last modified **2021-03-25** and captured 2026-09-15. It presents a **historical** deprecation schedule for previous-generation **Verifone Verix/eVo physical payment terminals**, alongside migration from classic POS libraries to [[adyen-terminal-api]]. Its dates and model alternatives are the page's dated claims, not confirmation of current device support, PCI approval, merchant eligibility or transactions. See [[adyen-payment-terminals]].

## Key takeaways

- The page tells merchants using eVo terminals to plan a fleet update, citing expiring PCI PTS approvals and Verifone's end of delivery, support and repairs. It says most listed eVo models had **PTS PCI 3** approval and e355/VX690 had **PTS PCI 4**. It describes PCI 3 expiry on 30 April 2021 and retirement by April 2023, and PCI 4 expiry in April 2023. These are historical page statements, not a current PCI compliance determination for a merchant or device. See raw lines 19–30.
- Its model table lists **31 March 2023** as end of repairs and **29 March 2024** as “No more transactions” for e315, MX925, VX675, VX680, VX820, VX820 Duet, e355 and VX690. Keep the terminal transaction cutoff separate from the later **31 March 2024** classic-library cutoff. See raw lines 32–35 and 50–54.
- For replacement, the page points to **Verifone Engage/VOS or Android** terminals, presenting countertop, mobile, multimedia and portable examples. It limits e280 purchasing to merchants in Japan in this historical snapshot. The list is a migration table, not a current order catalog or guarantee of model, market, firmware, certification or account availability. See raw lines 37–48.
- During a device switch, the page allowed initially continuing a classic library, but said merchants would eventually need to move to Terminal API. It stated transactions through a classic library would no longer be possible **after 31 March 2024**. Device replacement and POS integration migration are distinct work; this page gives no account-specific migration completion or payment-processing proof. See raw lines 19 and 50–54.

## Detail locators

- **eVo/Verix scope and PCI-support rationale:** raw lines 15–30.
- **Per-model approval, repair and terminal-transaction dates:** raw lines 32–35.
- **Dated VOS/Android replacement examples and Japan e280 note:** raw lines 37–48.
- **Classic-library to Terminal API transition and separate cutoff:** raw lines 50–60.

## Related

- [[adyen-payment-terminals]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/2026-09-15|Adyen eVo terminal deprecation — collected 2026-09-15]]
