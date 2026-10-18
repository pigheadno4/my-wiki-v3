---
title: "Adyen Platforms FX refunds: book the remainder to the platform"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/online-payments/currency-conversion/refunds/your-platform"
raw_files:
  - "adyen/docs/platforms/online-payments/currency-conversion/refunds/your-platform/2026-09-15.md"
tags: [adyen, platforms, online-payments, refunds, foreign-exchange]
---

## Overview

This 2026-09-15 Adyen for Platforms guide describes a limited-availability pilot for refunding a captured, currency-converted online payment while routing the FX remainder to the platform's liable balance account. In its scenario, the shopper originally paid in the processing currency and the user received settlement currency. The refund request reuses both original amounts: the shopper is credited the original processing-currency amount, the user is debited the original settlement-currency amount, and the remainder goes to the platform's liable account. This is a request and allocation guide, not proof of current pilot access, actual FX gain or loss, completed refund, or merchant-of-record identity. See [[adyen]], [[adyen-platforms]] and [[adyen-currencies-and-fx]].

## Key takeaways

- **Pilot and prerequisites:** The page says currency conversion remains in pilot, with processes and documentation subject to change. It lists an online-payments integration and checkout UI, a Checkout API credential, a server accepting standard webhooks plus transfer or transaction webhooks, account-holder capabilities `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument`, Support configuration of required merchant-account currencies, and a captured payment before a refund. This original-amount path does not call the Foreign Exchange API in the documented steps; do not import an FX API credential or rate-calculation prerequisite from the separate user-remainder option.
- **Refund split request:** Send Checkout `POST /payments/{paymentPspReference}/refunds` with the original payment's processing-currency amount in top-level `amount` and the original settlement-currency user amount in `splits.amount`. Add a `Remainder` split whose `account` is the platform's liable balance account ID; the guide says no remainder amount is needed. Its example uses shopper PLN 201.74 and user CZK 1000.00; those are different currency amounts, not a same-unit subtraction.
- **Who bears the remainder:** The page says any currency-conversion remainder goes to the platform's liable balance account while the shopper and user retain their original respective currency amounts. It illustrates PLN 6.31, but does not establish that every refund creates that amount, that it is always a gain, or that a particular platform has realized it. A sentence says “book the remainder amount to the customer” even though the title, following bullet about the liable account, procedure and split example all identify the platform; treat that sentence as an internal wording conflict, not an instruction to route the remainder to the shopper.
- **Booking and outcome boundary:** The separate [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] guide warns that Checkout validates split format rather than balance-account existence; a nonexistent destination or closed account holder can cause the full transaction and fees to book to the platform's liable balance account. The raw sample response for this FX procedure is only `status: received`; it does not prove refund completion, shopper receipt or final split booking. Track the later outcome through the relevant webhooks and accounting records. The page does not describe a distinct partial-refund procedure.
- **Version and environment:** The request example uses test Checkout v72. Its SDK samples are versioned (Java 40.0.0, PHP 28.3.0, .NET 32.2.1, Node 30.0.0, Go 21.1.0, Python 14.0.0 and Ruby 11.0.0). They show request shapes, not a current-version or live-account guarantee.

## Detail locators

- Pilot notice, original PLN/CZK scenario, remainder example and platform/customer wording conflict: raw lines 15–30. Requirements and captured-payment condition: lines 32–44. Common flow and booking claim: lines 46–51.
- Checkout refund endpoint, original `amount`/`splits.amount` and no-amount platform `Remainder` split: raw lines 53–62. Test v72 and versioned SDK request examples: lines 64–500. Illustrative `received` response: lines 502–536.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform user and liable-balance-account context.
- [[adyen-currencies-and-fx]] — provider FX and currency context.
- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-user]] — separate path that allocates the FX remainder to the user; its second option calculates a new settlement amount.
- [[source-adyen-docs-platforms-online-payments-split-transactions-split-refunds]] — general refund split booking, invalid-account fallback and outcome context.

## Related raw API references

- The raw page links to the Checkout refund endpoint. Consult it independently for current schema and availability.

## Raw Sources

- [[raw/adyen/docs/platforms/online-payments/currency-conversion/refunds/your-platform/2026-09-15|Adyen Docs: Book the remainder to your platform (2026-09-15 snapshot; pilot)]]
