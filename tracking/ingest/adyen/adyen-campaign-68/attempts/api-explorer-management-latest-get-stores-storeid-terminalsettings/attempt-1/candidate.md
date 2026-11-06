---
title: "Adyen Management API: get store terminal settings by store ID"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/stores/(storeId)/terminalSettings"
raw_files:
  - "adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalSettings/2026-11-07.md"
tags: [adyen, management-api, point-of-sale, terminal-settings]
---

## Overview

This 2026-11-07 Management API `latest` snapshot describes `GET /stores/{storeId}/terminalSettings` on the listed TEST `/v3` server. It reads settings configured for the identified store; those settings apply to terminals under the store unless an individual terminal has different values. The read does not establish on-device application or payment execution. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- `storeId` is the required path parameter and the unique store identifier. No query parameter or request body is listed. The caller's API credential needs Terminal settings read or read and write; reading sensitive settings additionally needs Terminal settings Advanced read and write. Live requests are rate limited, without a numerical limit in this reference.
- The documented success is `200`, with optional response groups including receipts, connectivity, gratuities, hardware, Terminal API URLs and shared key, payment/refund settings, standalone and offline features, surcharge, and Wi-Fi. Required markers within nested arrays do not make their optional parent groups mandatory. The `200` JSON is illustrative, including its passcode values; it does not state defaults or guarantee each group appears.
- Field descriptions retain consequential conditions: DCC enablement carries receipt/terms responsibilities; first contactless-currency change needs Adyen contact and a compliance check; unreferenced refunds carry liability for fraud or duplicates; store-and-forward prose requires `maxAmount`, `maxPayments`, and `supportedCardTypes` to be configured or inherited. These are field descriptions, not required inputs for this GET or evidence of activated features.
- Documented failures are `400` request problem, `401` authentication required, `403` insufficient permission, `422` validation error, and `500` server processing error. A `200` configuration read is not proof of a terminal's effective state, Live eligibility, compliance, authorization, capture, or settlement.

## Detail locators

- Purpose, role gates, Live rate-limit notice, TEST server, and store ID: pinned raw lines 5–29.
- `200` optional response schema, nested conditions, units, limits and defaults: pinned raw lines 31–196. Inspect lines 42, 47–56, 70–77, 103–105, 134–163, and 172–196 for feature-specific constraints.
- Error shapes: pinned raw lines 199–296. Illustrative `200` JSON: lines 298–419; the example includes passcodes at lines 395–399.

## Related

- [[adyen-terminal-management]] — terminal fleet configuration concept and task references.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/stores/(storeId)/terminalSettings/2026-11-07|2026-11-07 pinned GET store terminal settings reference]]