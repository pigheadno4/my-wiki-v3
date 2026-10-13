---
title: "Adyen Docs: Building a local Terminal API integration"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/local"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, local-communications, terminal-security]
---

## Overview

This Adyen documentation page guides merchants building a local-communications point-of-sale integration between their POS system and Adyen-supplied payment terminals. It covers network setup, optional Terminal API libraries, required local-communication protection for live transactions, shared-key setup, synchronous payment handling, and transaction-status recovery. It is a local architecture and setup guide; cloud communications, current SDK behavior, merchant enablement, and successful live execution require separate evidence. See [[adyen-terminal-api]].

## Key takeaways

- In the local flow, the POS sends a Terminal API request across the LAN to the terminal IP address; the terminal routes the shopper-completed transaction to Adyen's payments platform and returns a synchronous API response to the POS. Display notifications are optional. This is distinct from cloud communication, which the page tells merchants to choose between before implementation. See **How it works** and the introduction.
- Network configuration includes DNS-name allowlisting for outgoing HTTPS to `*.adyen.com` and `*.adyenpayments.com`, dynamic IP checks at least every 60 seconds, no hard-coded Adyen IP addresses, internet TCP 443 and LAN TCP 8443, suitable TLS/ciphers, and terminal IP assignment. See **1. Configure your network** for exact instructions.
- A Terminal API library is optional; the page lists .NET, iOS, Java, and Node libraries for this local path and distinguishes them from deprecated classic libraries. Its Management API examples name older library versions, including Node v16.2.0, and do not establish behavior of a current package release. See **2. (Optional) Install an API library** and **Create a shared key with an API call**.
- Local communication security is not enforced while building a test integration, but live transactions require securing POS-to-terminal requests. The guide calls for Adyen root-certificate validation of the terminal certificate and shared-key encryption/decryption; it separates test and live roots and provides fingerprint checks. Shared-key creation through API calls requires the Management API Terminal Advanced settings read/write credential role; Customer Area setup requires Merchant POS Terminal Management Admin. See **Requirements** and **3. Protect local communications**.
- A shared key may be set at company, merchant, store, or terminal level via Customer Area or Management API terminal settings. The API response returns accessible settings, including the passphrase; treat it as sensitive and store key identifier, passphrase, and version securely. The guide's request/response examples and passphrase rules are at **Set up a shared key**.
- Local terminals listen for Terminal API POST requests to `/nexo` on LAN port 8443. For a synchronous payment response, the POS HTTPS timeout must exceed 120 seconds. If no payment response, or a timeout response, is received after 150 seconds, the guide says to automatically request transaction status before staff try canceling, refunding, or making another transaction. See **4. Build your payment flow** and **5. Handle network issues**.

## Detail locators

- **Requirements** — architecture scope and roles required for the two shared-key setup paths.
- **How it works** — POS, LAN terminal, Adyen platform, and synchronous response sequence.
- **1. Configure your network** — DNS allowlist and refresh guidance, ports, TLS/ciphers, and terminal IP assignment.
- **2. (Optional) Install an API library** — optional Terminal API libraries and classic-library deprecation boundary.
- **3. Protect local communications → Install Adyen's root certificate** — test/live certificate download routes, fingerprints, trust-store steps, and Windows/iOS examples.
- **3. Protect local communications → Set up a shared key** — scope inheritance, Customer Area and Management API methods, passphrase rules, request/response examples, and secure storage; examples are version-specific.
- **3. Protect local communications → Add code to protect local communications** — terminal-certificate validation and encryption via a library or custom code.
- **4. Build your payment flow** — common payment-flow features, local `/nexo` POST endpoint, synchronous timeout, and optional display notifications.
- **5. Handle network issues** — transaction-status request timing and duplicate-transaction risk.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/choose-your-architecture/local/2026-09-15|Adyen Docs — Building a local integration (2026-09-15)]]
