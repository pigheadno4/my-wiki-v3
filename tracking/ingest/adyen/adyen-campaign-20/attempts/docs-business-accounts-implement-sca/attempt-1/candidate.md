---
title: "Adyen Business Accounts: Implement SCA"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/implement-sca"
raw_files:
  - "adyen/docs/business-accounts/implement-sca/2026-09-15.md"
tags: [adyen, business-accounts, sca, authentication]
---

## Overview

This 2022-11-30-modified, 2026-09-15-captured [[adyen]] overview describes Strong Customer Authentication (SCA) for some Business Accounts actions and points integrators to Adyen's client-side Authentication SDK and child procedures. It frames its opening in EEA-or-UK PSD2 terms, then has a linked install callout saying that installation guide applies only to EEA. The page does not resolve that scope tension or show successful authentication, a booked transfer, or a user's account access.

## Key takeaways

- The page says identity verification with SCA applies to some Business Accounts procedures, naming third-party bank transfers, consulting account transaction history, and creating transfer limits as examples. It describes two factors drawn from knowledge, possession and inherence. Treat these as the page's dated PSD2 guidance, not as a jurisdiction-wide rule for every action.
- Adyen says its client-side Authentication SDK combines possession with knowledge or inherence and supports a second verification method through a separate channel, such as a native mobile app or web-enabled device. The setup path is to install the SDK for iOS, Android or web, register the user's device, then follow action-specific authentication guides for funds transfers and transaction-history reads. The page does not provide a complete transaction or transfer-limit procedure.
- The opening says Business Accounts use in the EEA or UK must comply with PSD2 (raw line 19), while the install link at the bottom says `This only applies to the European Economic Area (EEA)` (raw line 56). Do not infer UK coverage or exclusion from this overview alone; check the current, action-specific product guidance.

## Detail locators

- Opening scope and SCA examples (raw lines 15–31): EEA/UK framing, three procedure examples and two-of-three-factor explanation.
- SDK role (raw line 33): possession plus knowledge/inherence and separate-channel description.
- `How to use the Authentication SDK` (raw lines 35–46): installation, device registration, transfer and history child routes.
- `Next steps` (raw lines 48–60): install and API-SCA routes, including the EEA-only linked callout.

## Related

- [[adyen-business-accounts]] — Business Accounts context.
- [[source-adyen-docs-business-accounts-sca-for-funds-transfers]] — action-specific transfer authentication route.

## Raw Sources

- [[raw/adyen/docs/business-accounts/implement-sca/2026-09-15|Adyen Business Accounts implement SCA, captured 2026-09-15]]
