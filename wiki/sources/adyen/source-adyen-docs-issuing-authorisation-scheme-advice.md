---
title: "Adyen Issuing scheme advice after authorization"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/scheme-advice"
raw_files:
  - "adyen/docs/issuing/authorisation/scheme-advice/2026-09-15.md"
tags: [adyen, issuing, authorisation, scheme-advice, reconciliation]
---

## Overview

Adyen's Issuing scheme-advice guide (captured 2026-09-15) describes cases where a payment scheme evaluates an issued-card payment after Adyen's initial authorization, for example when Adyen could not finish that flow in real time. Adyen updates the payment after the scheme's own authorize/refuse decision. If the two decisions differ, the scheme's advice governs the payment's final status and whether funds are reserved or released. This concerns the authorization and reserved-balance outcome; it is not evidence of capture or settlement. [[adyen-issuing]] [[adyen]]

## Key takeaways

- **Final decision and booking boundary:** Adyen defers to differing scheme advice. Later Adyen decisions can create another event booking, but the guide says these have no balance change and cannot alter the final payment status. See raw lines 19–23.
- **Transfer webhook:** A scheme-advice status change yields an additional `balancePlatform.transfer.updated` webhook. Identify it by `data.reason = schemeAdvice`, `data.status = authorised` or `refused`, and a new `data.events` booking with `adviceAuthorised` or `adviceRefused`. Use the scheme-advice webhook status as the payment's final authorization outcome. See raw lines 25–39. The shortened example changes an initial refusal to `authorised` and shows both the original `refused` event and the later `adviceAuthorised` event; it is an illustration, not a guarantee of approval. See raw lines 43–88.
- **Customer Area:** Under Balances > Transfers, the payment's Transfer lifecycle shows status history. The guide names **AdviceAuthorised** and **AdviceRefused** for the scheme's final decision and associated reserved-balance change. See raw lines 90–94.
- **Accounting report:** In the Balance Platform Accounting Report, an additional payment row carries Description `schemeAdvice` and Status `authorised` or `refused`. Scheme-advice rows are additive rather than replacements. If the original and scheme statuses differ, the `schemeAdvice` row determines the final reserved-balance change; when both authorize, the sample additional row has zero reserved change, while the reversal example assigns the change to the scheme-advice row. See raw lines 96–121.

## Detail locators

- Post-initial authorization precedence and subsequent event limits: raw lines 19–23.
- Webhook fields, final-outcome instruction and shortened refusal-to-authorization example: raw lines 25–88.
- Customer Area transfer lifecycle: raw lines 90–94.
- BPAR identification, additive-row rule and two booking examples: raw lines 96–121.

## Related

- [[adyen-issuing]] — Issuing concept.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/scheme-advice/2026-09-15|Scheme advice, captured 2026-09-15]]
