---
title: "UX410 user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/ux410-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/ux410-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, ux410, unattended, hardware]
---

## Overview

Adyen's UX410 manual covers physical installation and boarding of an unattended contactless terminal for self-service machines. The device has a separate NFC reader and controller, with LEDs, an illuminated contactless logo and a buzzer instead of a display. Its captured discontinuation notice says new orders are unavailable except in the EU, UK and UAE, repairs continue until April 2029, and Adyen recommends S1U2. The separate terminal catalog captured on the same date says UX410 is unavailable for new orders without listing those exceptions, so current regional ordering and repair terms need direct verification. This manual does not prove the condition, boarding, connectivity or payment result of any deployed unit. See [[adyen]], [[adyen-payment-terminals]], and [[adyen-terminal-management]].

## Key takeaways

- The installation sequence is store assignment, shipment/device inspection, physical installation, then boarding. Unlike most terminals, the manual says an unattended UX410 must be assigned to a store before boarding; use the **controller-unit** serial number when assigning through Customer Area or API. It mounts its NFC reader at the machine front and controller inside the machine. The supplied RF and RJ45 cables connect reader to controller; an Ethernet cable connects the controller's **LAN** port to the network, and power uses **DC IN**. Follow the machine manufacturer's installation instructions and the raw dimensions/torque details.
- Verify intact tamper tape and box, controller serial against the Customer Area order if accessible, carrier delivery, matching part/serial numbers on box and devices, and absence of suspicious screws, wires, labels, holes or attachments. The manual says to contact Adyen Support immediately if a check fails. Its red LED 1 warning may indicate tampering: stop using the terminal and contact Support immediately. A failed key load is a separate replacement condition.
- The cable warning is consequential: connect regular Ethernet only to **LAN**; another cable or port, including **COM1** RS232, may severely damage the device. The reader's RJ45 communication cable goes to **COMM**, not **COM1**. The controller must not be mounted in a removable machine chassis.
- During onboarding, LEDs distinguish no local network, no Adyen-platform connection, and not-boarded states. Slow-blinking LED 4 is the manual's ready indicator after boarding, not evidence of a completed or authorized payment. If not assigned, the terminal remains not boarded. The manual says it retries boarding after two minutes but stops after ten tries while the LED display remains ambiguous; disconnecting and reconnecting controller power restarts boarding. Payment-request/read-card LEDs only show local interaction stages.
- The manual's order/repair and LED/network instructions are a dated snapshot. It does not provide on-terminal PIN-pad, passcode-menu, or totals-reset procedures for the UX410; do not import those procedures from manuals for display terminals. The separate catalog's UX410 order statement is broader than this manual's EU/UK/UAE exception.

## Detail locators

- `UX410 user manual`, pinned raw lines 15–35: discontinuation notice, contactless role, two-unit hardware and self-service use.
- `Get started` / `Assign the terminal`, lines 37–46 and 66–72: setup order, LED 4 readiness cue, mandatory pre-assignment and controller serial identity.
- `Inspect the terminal`, lines 74–89: shipment, serial/delivery and device tamper checks plus Support escalation.
- `Install the terminal`, lines 91–132: supplied/other components, mounting, RF/COMM/LAN/DC IN connections and physical damage warnings.
- `Monitor the boarding process`, lines 134–167: staged LED diagnostics, assignment block, retry limit and power-cycle recovery.
- `Other LED signals`, lines 169–199: payment-interaction indicators, key-load replacement condition, red LED tamper warning and stop-use instruction.

## Related

- [[adyen-payment-terminals]] — physical model and safety hub.
- [[adyen-terminal-management]] — store assignment and boarding administration.
- [[source-adyen-docs-point-of-sale-what-we-support-select-your-terminals]] — same-date catalog with a broader no-new-orders UX410 statement; verify current regional status.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/ux410-user-manual/2026-09-15|Adyen UX410 manual, fetched 2026-09-15]]
