---
title: "Adyen board a payment terminal"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/managing-terminals/board-terminal"
raw_files:
  - "adyen/docs/point-of-sale/managing-terminals/board-terminal/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-management, boarding, store-assignment]
---

## Overview

This Adyen guide describes registering a physical payment terminal for an assigned store. Assignment and boarding are distinct: a terminal must be assigned to a store and then boarded before this guide treats it as ready for payments. The page covers manual boarding for integrated Terminal API and standalone terminals, plus an enabled one-time-password (OTP) flow for eligible integrated terminals. It is a device/store configuration procedure, not a Terminal API payment request. [[adyen]] [[adyen-terminal-management]] [[adyen-terminal-api]]

## Key takeaways

- Boarding requires at least one payment method configured for the merchant account or store. The page says the process can take up to 30 minutes. For manual boarding, staff power on and connect the terminal when prompted, then confirm the assigned store or select the correct store where the display allows it. Non-Android and Android terminal screens differ; the terminal reboots one or more times. If the displayed store is wrong and cannot be changed on-device, reassign it in Customer Area before trying again.
- OTP boarding is available only for integrated terminals on software version 1.94 or later, and needs Account Manager or Support enablement. Standalone terminals can only be boarded manually. The OTP API path needs an API credential/key with Management API — Terminal actions read and Management API - Reassign terminal to an entity roles.
- For eligible terminals still in company or merchant inventory, store staff connect the device to the network and scan its displayed barcode or enter its OTP. Merchant system logic queries GET /terminals with otpQuery to find the terminal id; when otpQuery is used, other query parameters are ignored. It then POSTs /terminals/{terminalId}/reassign with that id and the unique store identifier. The guide says the terminal then boards automatically and downloads configuration. API request examples are versioned examples, not current execution proof.
- An already boarded OTP terminal must be reassigned to use a different store; otherwise it continues processing payments over the old store. Staff initiate Reassign device on the terminal, then the system resolves the new OTP and reassigns it. The terminal reboots. If WebSockets are disabled, reassignment can take up to three hours. This delay is separate from the page's general up-to-30-minute boarding statement.
- The page's manual non-Android branch says an absent Board the terminal button can indicate already boarded state; after recent reassignment it advises waiting for the next platform synchronization, averaging three hours. Do not infer that an assignment API response alone proves the correct store is active on the physical device or that a test payment succeeded.

## Detail locators

- Assignment-before-boarding definition and general duration: pinned raw lines 15–23.
- Integration, credential roles, payment-method, software and standalone limits, and OTP enablement: pinned raw lines 25–37.
- Manual non-Android and Android display/confirm/reassignment branches: pinned raw lines 39–77.
- OTP physical staff action and Management API sequence: pinned raw lines 79–103 and 270–300.
- Already boarded terminal reassignment and WebSockets-disabled delay: pinned raw lines 302–313.

## Related

- [[adyen-terminal-management]] — physical device assignment and boarding hub.
- [[adyen-terminal-api]] — in-person message/payment architecture; this source concerns device boarding.
- [[adyen-pos-store-management]] — store setup and payment-method settings, distinct from terminal boarding.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/managing-terminals/board-terminal/2026-09-15|Adyen board the terminal guide, fetched 2026-09-15]]
