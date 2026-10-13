---
title: "Network configuration | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/network-configuration"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/network-configuration/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, network, local-communications, cloud-communications]
---

## Overview

This Adyen Docs network-configuration guide applies to a Terminal API point-of-sale integration with payment terminals. It describes network access and terminal addressing needed for the merchant POS app, terminal, and Adyen platform to communicate, with separate local/cloud considerations. It is a captured website recommendation and configuration guide, not proof that a specific store network or payment path works. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The guide directs the merchant to allow **outgoing HTTPS** from POS-app and terminal IP addresses to `*.adyen.com` and `*.adyenpayments.com`, using DNS-name allowlisting that checks changing IP addresses at least every 60 seconds; Adyen says not to hard-code its IPs. It lists **tcp/443 to the internet** and **tcp/8443 on the LAN**. These are directions and scopes in the page; it does not instruct a public inbound 8443 opening. Local POS app and terminal must share a local network and protect that communication.
- Adyen says it uses TLS 1.2 for secure internet transmission. For **local** communications, terminals on software v1.81 or later cannot process transactions if the integration still uses TLS 1.0 or 1.1. The page says cloud endpoints already reject TLS below 1.2. It lists TLS 1.2 cipher choices and a local TLS-test route for qualifying non-Android terminal/software combinations; check the raw before applying a cipher or test procedure.
- A terminal needs a valid IP address for online authorization. Dynamic DHCP, DHCP reservation, and manually configured static IP are described, but the terminal IP and its DNS-server/router IP settings cannot mix dynamic and static modes; Customer Area cannot configure the terminal IP. The page **recommends** dynamic IP without reservation for cloud and DHCP reservation or static IP for local communications, with a DHCP lease of at least 24 hours if configurable.
- For local communication, a changing terminal IP risks losing the POS connection. An optional Support-enabled notification can send the new IP and `uniqueTerminalId` to a merchant endpoint so the POS can reestablish communication. The merchant supplies that endpoint URL and credentials; this is not an automatic property of every terminal installation.
- The page recommends a segmented POS network, local DNS resolving Adyen domains while honoring Adyen TTL (including 60 seconds for disaster recovery), current IDS/IPS signatures, UPS, cellular backup, and correct MTU. Its Wi-Fi guidance calls for supported WPA/WPA2 and 2.4/5 GHz access points; Enterprise encryption requires a remote Wi-Fi profile, and local communication requires disabling wireless/client isolation. A Wi-Fi association alone does not establish internet access; supported channels are region/terminal dependent.
- When connectivity causes a decline, the page names `UnreachableHost`. Cellular failover and configured offline transactions are listed as possible continuations, but **offline payments are only available for local-communication integrations** in this page and the merchant is fully liable for related failed-capture, chargeback, and dispute risk. Adyen-supplied terminals do not support proxy connections and must bypass a network proxy to reach Adyen directly.

## Detail locators

- `Network configuration` / `Requirements`, lines 15–30: Terminal API scope, local TLS version and offline limitations, optional IP-change notification setup.
- `Network communications flow`, lines 32–45: local/cloud flow headings and diagrams; diagrams give navigation/context, not a separate protocol contract.
- `Communications security`, lines 47–75: TLS 1.2 statement, v1.81 local deprecation, cloud minimum, OS/test links, and cipher list.
- `Configuring your network`, lines 77–104: outbound domain allowlist, DNS polling, ports, same-LAN and protected-local requirements, legacy serial flow control.
- `Configuring the terminal IP address` / `Recommendations`, lines 106–126: valid IP for online authorization, assignment methods, all-dynamic/all-static constraint, Customer Area limitation, local/cloud IP advice.
- `Get notified about IP address changes` / `Defining a static IP address`, lines 128–170: optional Support-mediated webhook and terminal-admin static-IP steps.
- `General networking recommendations` / `Wi-Fi recommendations`, lines 172–215: network, DNS/TTL, IDS/IPS, UPS, failover, MTU, Wi-Fi encryption/profile/isolation, and regional-channel navigation.
- `Handling loss of internet connectivity` / `Using a proxy`, lines 217–233: `UnreachableHost`, failover/offline paths, merchant offline liability, Adyen-terminal proxy limit.

## Related

- [[adyen]] — provider page.
- [[adyen-terminal-api]] — provider concept for the Terminal API POS/terminal route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/network-configuration/2026-09-15|Network configuration (2026-09-15 snapshot)]]
