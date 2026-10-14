---
title: "Adyen Android terminal remote troubleshooting session"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals/start-remote-session"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/start-remote-session/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, remote-support, customer-area]
---

## Overview

Adyen's remote troubleshooting guide describes a Customer Area session that duplicates an Android payment terminal's screen and lets an authorized Customer Area user interact with terminal menus and Android apps for support or configuration. A person at the terminal must start the requested session by entering a one-time passcode. This is a dated procedure snapshot (fetched 2026-09-15; raw last modified 2020-10-09), not evidence that a session was started, that any screen was accessed, or that a configuration/payment outcome occurred. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- **Scope and permission gates:** The requirements table names Terminal API integration with payment terminals or a standalone solution, Customer Area POS terminal management/support roles, Android terminal hardware and enabled WebSockets. Its role cell joins `Merchant POS Terminal Management Admin` and `Merchant POS Terminal Support` with ambiguous formatting; do not infer whether both or one role is sufficient without current role guidance. It states a Verifone Android M450/P360 software floor of 1.115 and a 1.105.2 floor for other terminal models. These are dated guide thresholds, not current compatibility proof.
- **Operator participation and session lifecycle:** A Customer Area user chooses a terminal and requests `Start remote session`; a one-time passcode appears. A person operating that terminal selects `Start session` there and enters the code. Only then does the guide say a duplicate screen appears in Customer Area for menu interaction. Either side may end the session; a new session requires another one-time-password authentication. Requesting a session or generating a code alone is not proof of remote screen access.
- **Network/security qualification:** Depending on network or security requirements, firewall allowlisting may be needed. The page recommends DNS resolution and domain-based allowlisting and lists a specific URL, IP and ports as historical connection detail. Use the raw `## Allowlisting` locator and current provider/security guidance before changing firewall policy; this source does not establish today's endpoint address or authorization for remote access.

## Detail locators

- **Purpose, duplicated screen and operator requirement:** raw lines 15–21, `# Remote troubleshooting`.
- **Integration, roles, model/software floors and WebSockets:** raw lines 23–33, `## Requirements`. The role row's punctuation is ambiguous in the raw table.
- **Network allowlisting recommendation and historical URL/IP/port list:** raw lines 35–44, `## Allowlisting`.
- **Customer Area initiation, terminal-side one-time code, end and reauthentication:** raw lines 46–58, `## Start a remote session`.
- **Further troubleshooting, manual and allowlisting navigation:** raw lines 60–64, `## See also`; linked pages were not read for this entry.

## Related

- [[adyen-android-terminals]] — Android payment-terminal scope and source route
- [[adyen-terminal-management]] — separate fleet administration; remote screen session is operator-assisted troubleshooting

## Related raw API references

The linked user-role, cloud-connection, troubleshooting, terminal-manual and general allowlisting guides were not read for this entry; use their raw pages for current permission, connectivity and security details.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/start-remote-session/2026-09-15|Remote troubleshooting, fetched 2026-09-15]]
