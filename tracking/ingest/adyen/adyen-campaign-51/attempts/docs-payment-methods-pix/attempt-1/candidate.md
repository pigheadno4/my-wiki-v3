---
title: "Pix payment method overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pix"
raw_files:
  - "adyen/docs/payment-methods/pix/2026-09-15.md"
tags: [adyen, pix, brazil, brl, qr-code, bank-transfer]
---

## Overview

This 2026-09-15-captured Adyen overview describes **Pix** as a Brazil instant bank-transfer method operated through participating banks, digital accounts and wallets. An online shopper scans a QR code or copies its data in a banking or wallet app, then confirms payment. The page covers merchant locality, transaction checks, a capability matrix, the Pix Special Return Mechanism and integration routes. It is a historical documentation snapshot, not evidence of current merchant eligibility or live payment success. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The source says money moves from the shopper account to **Adyen's account** when Pix approves the transfer, and Adyen then transfers to the merchant bank account **once a day** (raw lines 23–25, 34). Do not conflate the instant Pix transfer with merchant settlement. The merchant must have a **local entity in Brazil** to accept Pix (raw line 36).
- In the online flow, the merchant website or app shows a Pix QR code or copyable data; the shopper opens a participating bank/wallet app, scans or pastes it and confirms (raw lines 27–34). Before approval, Pix checks Central Bank transaction conditions, including sufficient funds, maximum transaction time, fraud/regulatory suspicion, authentication issues and participant exclusion; Adyen or the acquirer bank can also reject for fraud/regulatory suspicion or Pix ecosystem technical issues (raw lines 42–55). This overview does not state a specific QR expiry interval or make QR display proof of payment.
- The matrix labels **real-time payments / `qrCode` / BR / BRL**. It marks recurring and refunds available; partial and multiple partial refunds have checkmarks with “See note”, but the captured page supplies no corresponding explanatory note. It marks separate, partial and multiple partial captures unavailable. The Chargebacks cell is marked unavailable with “See note”, yet the page separately describes the **Pix Special Return Mechanism** for suspected fraud or operational failure (raw lines 38–40, 57–67). Do not treat the crossed-out Chargebacks cell as an absence of Pix disputes.
- For an unrecognized Pix transaction, the page says a shopper can raise a bank dispute **within 90 days**. It says the merchant need take no action for the Special Return Mechanism; dispute status can be viewed in Customer Area. Its described progression includes `OpenDispute`, `RequestForInformation` with a `REQUEST_FOR_INFORMATION` webhook, and Adyen auto-defense followed by `InformationSupplied` with an `INFORMATION_SUPPLIED` webhook. These are the described dispute workflow, not an assertion that every case follows that path or that a QR checkout itself proves final settlement (raw lines 57–67).
- The page routes to Web, iOS, Android, React Native, Flutter and API-only online integration guides, plus a separate in-person Pix route (raw lines 69–111). Use the relevant child guide for request fields, QR timing and asynchronous status handling; this overview alone does not specify an end-to-end API/webhook recipe.

## Detail locators

- Identity, transfer/settlement distinction, shopper QR flow and local-entity condition: raw `# Pix`, lines 23–36.
- BR/BRL method matrix and unresolved “See note” markers: raw lines 38–40.
- Pix and Adyen/acquirer transaction rejection conditions: raw `## Transaction conditions`, lines 42–55.
- Special Return Mechanism, 90-day dispute window and status/webhook description: raw `## Chargebacks`, lines 57–67.
- Online platform/API-only and separate in-person routes: raw `## How do you want to integrate?`, lines 69–111.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pix/2026-09-15|Pix overview, captured 2026-09-15]]
