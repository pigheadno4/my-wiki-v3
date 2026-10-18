---
title: "Adyen Capital financing-offer options"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/get-grant-offers"
raw_files:
  - "adyen/docs/capital/get-grant-offers/2026-09-15.md"
tags: [adyen, capital, platforms, financing-offers, dynamic-offers, static-offers]
---

## Overview

This 2026-09-15 Adyen Capital **offer-selection hub** compares dynamic ranges with static fixed amount-term choices for users whose processed payment volume informs Adyen's proactive risk assessment. It labels **variable 90-, 180- and 360-day repayment terms** as pilot availability. The page routes implementation to separate dynamic/static guides; it does not show a particular user's eligibility, a calculated or formal offer, offer validity, ToS acceptance, grant configuration or funding.

## Key takeaways

- **Dynamic offers** let a user choose an amount within a specified range for a repayment term. Based on processing history, a user **may** receive up to three dynamic offers, one per available 90-, 180- and 360-day term. The slider/dropdown/button ideas are presentation examples, not integration requirements or assurance that every term is offered.
- **Static offers** present fixed amounts. A user **may** receive up to nine, described as three per available 90-, 180- and 360-day term, and chooses an offered amount-term combination rather than an amount between choices. Neither maximum count nor illustrative amount is a universal grant limit.
- The example user qualifies for up to EUR 25,000 with **90- and 180-day** terms: dynamic ranges and six static amounts differ by term. This is an illustrative user, not evidence of a live offer to any account holder or 360-day availability. The pilot notice applies to variable repayment terms; this short hub does not declare all Capital offers to be pilot-only.
- The page supplies no API credential role, `getGrantOffers` capability rule, country list, dynamic calculation request, formal static-offer conversion, offer expiration, or funded-grant transition. Follow its dynamic/static child guides and separate Capital capability, ToS and grant-request sources for those facts. Displaying a choice here is not offer acceptance or disbursement proof.

## Detail locators

- Opening and pilot notice: personalized assessment and variable-term pilot scope.
- Dynamic/static comparison bullets: conditional counts, ranges versus fixed amounts, 90/180/360-day terms and illustrative UI controls.
- `*Example*`: term-dependent EUR ranges and fixed choices for one hypothetical user.
- `## Next steps`: dynamic and static implementation child routes.

## Related

- [[adyen-capital]] — main Capital concept.
- [[source-adyen-docs-capital-get-grant-offers-dynamic-offers]] — dynamic-offer implementation reference.
- [[source-adyen-docs-capital-get-grant-offers-static-offers]] — static-offer implementation reference.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/get-grant-offers/2026-09-15|Adyen Capital get-financing-offers hub (fetched 2026-09-15)]]
