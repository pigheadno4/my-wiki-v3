---
title: "Adyen point-of-sale offline payments"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/offline-payment"
raw_files:
  - "adyen/docs/point-of-sale/offline-payment/2026-09-15.md"
tags: [adyen, point-of-sale, offline-payments, offline-emv, store-and-forward, terminal-api, mobile-sdk]
---

## Overview

This Adyen Docs page explains how configured point-of-sale integrations can continue taking payments during a temporary internet loss, using offline EMV or store and forward. It covers eligibility, merchant risk, setup, offline response recognition, later processing and reconciliation, retries, refunds, and testing. See [[adyen]] and [[adyen-terminal-api]] for the provider and in-person interface route. This dated website snapshot does not establish current account enablement, card/scheme or regional eligibility, successful issuer authorization, capture, or settlement for a particular transaction.

## Key takeaways

- A transaction normally needs internet access from the payment terminal or Mobile SDK. Offline payments require prior enablement and configured limits; Adyen says to ask Support to enable the chosen type and configure its limits, then check the settings in Customer Area. A cellular terminal connection is a separate online alternative during an internet outage.
- The stated supported paths are a Terminal API integration with locally communicating payment terminals, standalone terminals with a built-in printer, and specified iOS Mobile SDK solutions. Cloud terminal communication has a narrow offline window: the payment request must have reached the terminal before internet access is lost. Mobile SDK solutions do not support offline EMV or refunds while offline; magnetic-stripe transactions cannot use offline payments. The types also vary by card, scheme, and region.
- Offline approval occurs before the merchant receives funds and, for store and forward, before issuer authorization. Adyen assigns the merchant full liability for failed captures, chargebacks, and disputes, and requires a per-transaction floor limit. Offline EMV asks an eligible chip card to approve after checking offline PIN, while store and forward has the terminal or Mobile SDK approve without verification and submit later, with higher issuer-decline risk. Do not read an offline `Success` response as final funding.
- On connection loss, the terminal or Mobile SDK checks enabled modes, card/issuer and scheme support, amount and stored-payment limits; when both modes are enabled it tries offline EMV first. If the offline payment is approved, it stores card/transaction details and sends them to Adyen for further processing when connectivity returns. Some scheme rules override account settings: the page gives Germany girocard offline EMV and Australia American Express as examples.
- For Mobile SDK store and forward, the platform must attest the device while it is online. The page describes a 24-consecutive-hour window after a secure evaluation and says this mode does not work during an Adyen platform outage. While offline, deleting the POS app or removing the device passcode loses stored card and transaction data; restarting prevents further transactions until internet reconnects.
- An offline Terminal API response lacks Adyen-generated PSP and issuer-authorization data and initially carries only the terminal's tender reference. The page recommends webhooks if reconciliation uses PSP references; those arrive for stored payments once online. It also describes tender-reference reconciliation and handling later issuer declines. Auto Rescue retries eligible failed store-and-forward authorizations for one calendar month if separately enabled; fraud-flagged payments are ineligible.
- While still offline, only unreferenced refunds are supported, as offline EMV, subject to card support and a Support-configured maximum; Mobile solutions cannot refund offline. After reconnection, the page describes unreferenced or referenced refund routes using the original tender reference/terminal identifier or a recovered PSP reference. See the raw refund section for exact request forms and conditions.

## Detail locators

- Internet requirement, cellular alternative, and scope: `# Offline payments`, raw lines 19–27; integration and mode limits: `## Requirements`, lines 29–42.
- Merchant exposure and required floor limit: `## Risk with offline payments`, raw lines 44–50. Mode mechanics, eligible cards/schemes and exclusions: `## Types of offline payment`, lines 52–67.
- Offline checks, EMV-first order, storage and later platform submission: `## Offline payment flow`, raw lines 69–92. Mobile attestation, 24-hour window, platform-outage and data-loss warnings: `## Offline payments in a Mobile solution`, lines 94–108.
- Support setup, per-mode limits, and regional scheme exceptions: `## Set up offline payments`, raw lines 110–157.
- Missing PSP/authorization fields and offline indicators: `## Recognize the offline payment response`, raw lines 159–200; examples continue through line 269. Reconciliation and issuer-decline handling: lines 271–278.
- Auto Rescue eligibility, enablement and retry identifiers: `## Retry failed store-and-forward authorizations`, raw lines 280–294. Offline and later-online refund routes: lines 296–326. Test procedure and post-reconnection checks: lines 328–354.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — in-person Terminal API route; this page also covers standalone terminals and Mobile SDK conditions.

## Related raw API references

- The raw page links to local communications, Terminal API fundamentals, webhooks, Mobile SDK troubleshooting, refund requests, reporting, and Auto Rescue. Those linked targets are navigation until independently read; see raw lines 35–41, 98, 280–326, and 356–363.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/offline-payment/2026-09-15|Adyen Docs: Offline payments (2026-09-15 snapshot)]]
