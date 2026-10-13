---
title: "Make Pay-at-table payments | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/pay-at-x"
raw_files:
  - "adyen/docs/point-of-sale/pay-at-x/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, pay-at-table, split-payments]
---

## Overview

Adyen's Pay-at-table guide describes a **terminal-initiated** in-person flow for a table, hotel room, or curbside while keeping the terminal integrated with a merchant POS. Staff initiate it on the terminal, but the POS identifies the bill and sends Terminal API payment requests for successive equal or unequal splits. The pinned webpage was fetched 2026-09-15 and reports `last_modified` 2020-11-02; this snapshot is not proof of current device, account, payment-method, or hosted outcome. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- This flow requires a Terminal API integration and a portable terminal with integrated printer plus Wi-Fi and cellular support. The guide says payment methods added to the merchant account, as well as cash, can be used; terminal tipping can be combined with splits. Employee-card swipe authentication is unavailable on Android terminals. Configure terminal Pay@Table settings in Customer Area, event notifications, staff authentication method through Adyen Support, and POS handling of `SaleWakeUp`; Support can configure skipping the cash/card choice if cash is not accepted.
- Staff press the terminal button and authenticate with a reference number or employee card. The terminal sends a `SaleWakeUp` `EventNotification` to the POS; `EventDetails` carries that reference/card number if configured. If the instruction field is left empty, notification follows the button press immediately without that identifier. The POS uses the identifier or terminal to find open bills and can use `InputRequest` for table/bill selection. A terminal `PrintRequest` for the bill is optional; a session spanning multiple input requests is also optional and is **not** the payment session or proof of payment.
- After choosing the bill, the **POS** sends `PaymentRequest` with `PaymentData.PaymentType: Normal`, `SplitPaymentFlag: true`, and `AmountsReq` `RequestedAmount` and `PaidAmount`. The first request uses the full bill and zero paid; later requests use the remaining amount and the sum already paid. Use a unique sale `SaleTransactionID.TransactionID` at the first request and repeat that **same sale ID** across splits for that bill. The terminal presents equal/unequal split and card/cash choices; a whole-bill single payer is an unequal split for the whole amount. Staff confirm cash on the terminal, while card shoppers interact with the terminal.
- The POS must process each result to track the cumulative paid amount. In this **split-payment** flow, `Response.Result: Success` means the current `RequestedAmount` was paid in full, while `Partial` means an amount remains due and another split request is needed. Read `AmountsResp.AuthorizedAmount` for the amount paid by that split. A later `Pay later` choice yields `Failure` with `PaymentRestriction` for the interrupted flow; the guide explicitly says it does **not** mean a preceding split failed. Restart Pay at table when another shopper is ready. Do not conflate this with the issuer-funded partial-authorization flow.
- Errors outside active payment processing reach the POS; staff near the table may need a POS-to-terminal display message. The guide gives no guarantee about concurrent terminal taps or bill selection, duplicate request recovery, final settlement, or automatic retry. Bill identity, split totals, and each payment result remain POS responsibilities.

## Detail locators

- Use cases, configured payment methods/cash, tipping, hardware and Android swipe limit: pinned raw, introduction and `## Requirements` (lines 15–38).
- Staff-terminal → `SaleWakeUp` → POS bill lookup → input/print → payment/split loop: pinned raw, `## How it works` (lines 40–77).
- Customer Area Pay@Table, event notification, Support settings, empty instruction field, and notification structure: pinned raw, `## Configure Pay at table` and `### SaleWakeUp event notification` (lines 79–141).
- Bill selection and optional multi-input session: pinned raw, `## 1. Retrieve the sale transaction` (lines 143–158).
- Same sale transaction ID, split flag, amount fields, and request examples: pinned raw, `## 2. Make a payment` (lines 160–260).
- `Success`/`Partial` for a split, authorized amount, cash/card indicators, `Pay later`/`PaymentRestriction`, decline handling: pinned raw, `## 3. Process the payment result` (lines 262–369).
- Staff authentication, navigation/cancel, and optional display feedback: pinned raw, `## Information for your staff` (lines 371–391).

## Related

- [[adyen-terminal-api]] — Terminal API message and in-person flow boundaries.
- [[source-adyen-docs-point-of-sale-partial-authorizations]] — separate issuer partial authorization of a card balance.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/pay-at-x/2026-09-15|Make Pay-at-table payments — 2026-09-15 snapshot]]
