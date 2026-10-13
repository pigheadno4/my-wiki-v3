---
title: "Adyen Docs: Cellular failover for payment terminals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/2026-09-15.md"
tags: [adyen, point-of-sale, cellular-failover, terminals, connectivity]
---

## Overview

This Adyen documentation page describes cellular failover for payment terminals in Terminal API or standalone point-of-sale setups. A terminal with usable cellular access can switch from a primary Wi-Fi or Ethernet path when it cannot reach the internet and return when the primary path recovers. The page distinguishes terminal connectivity from the POS app's connectivity, explains local and cloud failure scenarios, and gives SIM-management and terminal-model qualifications. This 2026-09-15 snapshot does not prove current cellular coverage, fees, account enablement, or successful payment processing.

## Key takeaways

- Failover carries Adyen-related terminal services such as payments and diagnostics; it does not carry network requests from other apps installed on the terminal. A terminal may use built-in cellular hardware and an Adyen-supplied SIM, or a cellular router where hardware is absent. 3G-only terminals face the linked 3G-coverage sunset. See **Requirements** and **Cellular connection and alternatives**.
- In cloud communications, terminal failover can help if the POS app still has internet access to send its request through Adyen. If the POS app itself has no internet, terminal failover does not restore its send/receive path. In local communications, failover does not help when the terminal loses the LAN connection needed to receive the POS request; it can help when the LAN remains connected but the terminal's internet path fails, with the page describing a 36-second wait before cellular use. See **Understanding cellular failover scenarios**.
- The page suggests standalone backup terminals or offline payments for some failed-path scenarios. Offline payments are available as an alternative only for local communications in this page, and the merchant is fully liable for failed captures, chargebacks, and disputes related to offline payments. A standalone backup must have a built-in printer plus cellular connectivity or offline payments enabled. See **Using a cellular router** and the scenario sections.
- Adyen says SIMs are activated and cellular is enabled by default. Management API GET/PATCH terminal-settings calls can inspect or change one terminal's `simcardStatus` (`ACTIVATED` or `INVENTORY`); deactivation removes cellular access. After reactivation, the terminal needs cellular re-enabled or a reboot, with different non-Android and Android steps. The response returns all terminal settings at the requested level. See **Manage cellular connectivity on the terminal**.
- Third-party SIM use is limited here to AMS1, S1U2, S1F2, S1F2L, and S1E2L on firmware 1.93 or later; it requires account-manager activation details and the second SIM slot, without removing the pre-installed SIM. Manual operator selection has a different model list, firmware 1.134 or later, and prior Support enablement. Brazil's local-operator steps have a separate Android-terminal firmware 1.96 or later condition. See **Requirements**, **Select a network operator manually**, **Activating a third-party SIM card**, and **Switch to a local network operator in Brazil**.
- At the snapshot, the page says Adyen did not charge for cellular connection use, while forecasting Android app-traffic data bundles and continued no-fee payment/terminal-update traffic. This is dated future-looking pricing language, not current commercial terms. See **Using terminals with cellular connectivity**.

## Detail locators

- **Requirements** — Terminal API/standalone scope; third-party SIM and manual-selection model/firmware gates; Adyen-service-only traffic; Support enablement.
- **Cellular connection and alternatives → Using terminals with cellular connectivity** — built-in hardware, pre-installed SIM, primary/cellular return behavior, dated fee language, and 3G sunset.
- **Cellular connection and alternatives → Using a cellular router** — router option, standalone/offline alternatives, printer and connectivity requirements, and offline-payment liability.
- **Understanding cellular failover scenarios** — four distinct cloud/local and no-network/no-internet cases, including the local 36-second example.
- **Manage cellular connectivity on the terminal** — Management API GET/PATCH `simcardStatus`, one-terminal-at-a-time scope, return payload, and platform-specific re-enablement/reboot. Code examples name older SDK versions and do not establish current library behavior.
- **Select a network operator manually** — Support enablement, menu steps, and automatic-selection fallback.
- **Activating a third-party SIM card** — account-manager, APN/serial, firmware, second-slot, and SIM-priority steps.
- **Switch to a local network operator in Brazil** — Brazil-specific regulatory and terminal/firmware/menu qualifications.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/cellular-failover/2026-09-15|Adyen Docs — Cellular failover (2026-09-15)]]
