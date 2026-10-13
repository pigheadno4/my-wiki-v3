---
title: "Choose an integration architecture | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, local-communications, cloud-communications]
---

## Overview

This Adyen Docs architecture guide helps a merchant choose local or cloud communication for a point-of-sale system integrated with Adyen payment terminals through Terminal API. The choice determines whether the POS sends Terminal API requests directly to a terminal on the local network or through the Adyen payments platform over the internet. It also points to standalone terminals for merchants that do not need a full API integration. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- In local communication, the POS sends a request to the terminal's IP address over the local network and receives the payment result synchronously. For direct requests, the terminal listens for POST on `/nexo` at port 8443; an Android POS app installed on the terminal can use localhost or 127.0.0.1. Adyen advises a DHCP reservation or static terminal IP and requires the POS app to add Adyen's certificate and encrypt local messages.
- In cloud communication, the POS sends Terminal API requests to an Adyen platform endpoint that forwards them to the terminal. The integration can choose synchronous or asynchronous results. The listed `device-api-test.adyen.com` `/sync` and `/async` URLs are **test** endpoints; they use `merchantAccount` and `deviceId` path parameters, and `deviceId` must match the message header's `POIID`. This snapshot does not supply a live endpoint.
- The guide strongly recommends migrating existing legacy `terminal-api` cloud endpoints to `device-api` endpoints. Its linked migration page is navigation, not reviewed evidence for migration procedure or endpoint availability. This website snapshot does not establish a GitHub client or SDK version.
- The decision tree says local integration supports offline EMV and Store-and-forward processing, while cloud integration does not; loss of internet prevents transactions through that cloud integration. Adyen suggests standalone terminals, a secondary local integration, or cellular failover as possible fallbacks. Offline capability and successful payment execution in a particular deployment are not demonstrated by this page.
- Architecture selection depends on POS cloud support, terminal use and power, offline needs, network quality, and local network expertise. The tree recommends local communication for unattended terminals, and advises contacting Adyen to assess cloud use with portable or battery-powered terminals. The location's network team or provider must be able to configure and troubleshoot its network; Adyen says it cannot support network issues at the physical location.

## Detail locators

- `Choose an integration architecture`, lines 19–26: standalone alternative, Terminal API architecture choice, local versus cloud path.
- `Local communications`, lines 36–49: synchronous local flow; POST `/nexo` port 8443; Android on-terminal localhost option; stable IP and certificate/encryption guidance.
- `Cloud communications` and `Test endpoints`, lines 51–70: platform forwarding; result mode; test URL table; `deviceId`/`POIID` condition; legacy endpoint migration recommendation.
- `Choosing between cloud and local` / `Decision tree`, lines 72–142: selection criteria, offline distinction, fallback suggestions, cloud POS and terminal-use branches, unattended recommendation.
- `Technical know-how`, lines 144–158: local versus cloud IP guidance, DHCP lease suggestion, and on-site network support boundary.
- `Next steps`, lines 160–168: links to the separate local and cloud implementation guides; those targets were not read for this entry.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — provider concept for the Terminal API message surface and source routes.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/2026-09-15|Adyen architecture choice guide (2026-09-15 snapshot)]]
