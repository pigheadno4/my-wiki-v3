---
title: "Adyen Raise disputes API v4 overview (transfers-api URL)"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers-api/latest/overview"
raw_files:
  - "adyen/api-explorer/transfers-api/latest/overview/2026-09-15.md"
tags: [adyen, issuing, disputes, api-explorer]
---

## Overview

At this `transfers-api/latest/overview` URL, the 2026-09-15 capture is headed **Raise disputes API v4** and describes an **Issuing dispute API** for transactions on Adyen-issued cards and fraud reports. It says users can raise, add supporting attachments to, update, submit for chargeback, or close a dispute. This captured page is not the separately documented Transfers API v4 overview for moving funds. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The page documents authentication by `X-API-Key` using an Adyen-provided API key or by username/password basic authentication. It says the API credential needs an additional role set up by an Adyen contact, but does not name that role. The version suffix format is `vXX`; the listed TEST and LIVE bases are `https://balanceplatform-api-test.adyen.com/btl/api/v4` and `https://balanceplatform-api-live.adyen.com/btl/api/v4`. The page says a live API credential is provided separately.
- The eight listed paths cover dispute list and creation, listing/adding/getting/deleting dispute attachments, and getting/patching a dispute by ID. They use `disputeId` for attachment paths and `id` for the get/patch dispute paths as printed. Although the introduction mentions submission for chargeback and closure, the endpoint table does not show a separate submit or close route. The overview does not define request bodies, response codes, attachment deletion effects, dispute status or chargeback outcomes.
- The URL segment `transfers-api` and the page's dispute heading, prose, `/disputes` example and endpoint table disagree on family labeling. Preserve both as captured; do not import transfer-creation, payout, balance-account movement or financial-finality semantics from the distinct Transfers API.

## Detail locators

- Captured heading, Issuing dispute purpose and listed activities: pinned raw lines 5–7.
- API key/basic authentication, additional role and versioned TEST/LIVE host statements: raw lines 9–47.
- Eight dispute and attachment endpoint summaries, including `disputeId` versus `id`: `## Endpoints > ### General`, raw lines 49–61.

## Related

- [[adyen-issuing]] — issued-card and dispute context.
- [[source-adyen-api-explorer-transfers-latest-overview]] — separate Transfers API v4 overview for funds movement; do not conflate the two similarly named routes.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/transfers-api/latest/overview/2026-09-15|Raise disputes API v4 captured at transfers-api URL]]
