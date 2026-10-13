---
title: "Building a cloud integration | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/cloud/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, cloud-device-api, cloud-communications]
---

## Overview

This Adyen Docs guide describes a cloud Terminal API integration between a merchant POS app, Adyen's payments platform, and an Adyen payment terminal. The POS sends Terminal API messages to Cloud device API endpoints; Adyen routes them to the terminal, processes the transaction, and returns a synchronous or asynchronous result. It covers network configuration, API credentials, result delivery, timeout recovery, regional live endpoints, and migration from older cloud `terminal-api` endpoints. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The merchant POS app makes an API request to Adyen's platform, which routes it to the terminal. In synchronous mode, the POS keeps the HTTPS connection open for a payment result and must use an extended timeout greater than 150 seconds. In asynchronous mode, the request's HTTP `200 OK` means the terminal received the request; the actual Terminal API result arrives later through event notifications or can be retrieved with a transaction status request. An HTTP acknowledgment is not evidence that the payment succeeded.
- Cloud setup calls for DNS-based allowlisting of `*.adyen.com` and `*.adyenpayments.com`, outgoing HTTPS from POS apps and terminals, tcp/443 to the internet, tcp/8443 on the LAN, and contacting Adyen Support to enable WebSockets for the account. Adyen warns against hard-coding its changing IP addresses. The guide says an API key with the **Cloud Device API** POS role is required in the `x-API-key` header for cloud Terminal API requests. The key must be saved securely when generated because it cannot be copied again after leaving that page.
- The guide lists several optional GitHub Terminal API cloud libraries, yet separately says **Cloud device API is currently only supported by the Java library** and other library support is coming. These are distinct claims in this dated website snapshot, not proof that every listed library supports the new endpoint surface or of any current GitHub package version. It also says these Terminal API libraries are separate from deprecated classic libraries.
- For asynchronous delivery, the merchant must set up and acknowledge event notifications. The guide says the terminal sends the Terminal API response over a WebSocket connection to the merchant's event-notification endpoint, and the merchant must filter those responses from other events. By default, Adyen retries asynchronous Terminal API responses up to three times only when the merchant responds with HTTP 5xx; other response codes are treated as success. Support can enable a separate guarantee-payment-response-delivery feature that continues until successful acknowledgment. A delayed result can arrive while the POS is handling another transaction.
- If no payment response or timeout response arrives after 150 seconds, the guide advises an automatic transaction status request to resolve uncertainty before staff retry, cancel, or refund. It also suggests platform-generated standard webhooks as a fallback when the synchronous response or event notifications fail due to network or WebSocket issues. These are recovery instructions, not a guarantee of successful delivery or processing.
- The shown `device-api-test.adyen.com` sync/async URLs are test endpoints. For live use, the guide lists regional Cloud device API URLs and says `deviceId` in the path must match the Terminal API header's `POIID`; choose a geographically close store endpoint and appropriate data center. It strongly recommends migration from old `terminal-api` endpoints, says they remain supported but get no future development, and gives old/new endpoint tables. Endpoint tables are snapshot evidence, not proof of present availability or account enablement.

## Detail locators

- `Building a cloud integration`, lines 19–48: Postman and implementation-example links (navigation only), cloud path, Java-only Cloud device API statement, sync/async result model, build sequence.
- `1. Configure your network`, lines 50–71: firewall domains, DNS update guidance, ports, WebSocket support prerequisite.
- `2. (Optional) Install a GitHub API library`, lines 73–97: optional Terminal API cloud library list and classic-library separation; linked repositories were not reviewed for this source.
- `3. Get your API key`, lines 99–139: Cloud Device API role, test credential steps, one-time key copy, live Customer Area and `x-API-key` header.
- `4. Build your payment flow` / `Receiving a synchronous result`, lines 141–169: test sync URL, path identities, timeout requirement, optional display notifications and standard-webhook fallback.
- `Receiving an asynchronous result` / `Guarantee payment response delivery`, lines 171–209: test async URL, HTTP acknowledgment, event-notification response, 5xx-only retries, transaction-status receipt path, support-enabled continued delivery, out-of-order response warning.
- `5. Handle network issues`, lines 211–219: 150-second timeout, status inquiry and duplicate-action risk.
- `6. Going live` / `Regional data center overview`, lines 221–317: regional live URL tables, `deviceId`/`POIID` match, store proximity and data-center selection, country table.
- `Migrate to latest endpoints`, lines 319–366: migration recommendation, old-endpoint support/no-future-development statement, Java-only Cloud device API qualification, old/new test and live URL mapping.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — Terminal API message and transport concept; website claims here are separate from version-qualified GitHub examples.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/cloud/2026-09-15|Building a cloud integration (2026-09-15 snapshot)]]
