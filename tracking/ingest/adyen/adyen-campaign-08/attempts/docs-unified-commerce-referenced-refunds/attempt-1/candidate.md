---
title: "Adyen Unified Commerce referenced refunds"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/unified-commerce/referenced-refunds"
raw_files:
  - "adyen/docs/unified-commerce/referenced-refunds/2026-09-15.md"
tags: [adyen, unified-commerce, omnichannel, refunds, terminal-api, checkout-api]
---

## Overview

Adyen's Unified Commerce referenced-refund guide, last modified 2022-02-01 and captured 2026-09-15, describes returning an online purchase in store or an in-store purchase through another channel while linking the refund to the original payment's PSP reference. A referenced refund returns value to the original payment method; it is not a cash handoff or refund to a newly presented card. The original payment's merchant account supplies the in-process funds even when another merchant account accepts the return. Both the Terminal API reversal and server-to-server Checkout refund paths are asynchronous. [[adyen]] [[adyen-unified-commerce]]

## Key takeaways

- The merchant needs online and in-person integrations, Standard webhooks, and access across sales-channel backends to original transaction information including the PSP reference. Returns across merchant accounts require Adyen Support to enable refunds at the company level. A shared shopper or order record by itself is not the original payment reference or proof that accounts are enabled.
- A POS app can send a Terminal API `ReversalRequest` through a terminal for a full or partial referenced refund without the shopper presenting the card. For an original POS payment, its `OriginalPOITransaction.POITransactionID.TransactionID` is `tenderReference.pspReference` plus the original timestamp. For an original ecommerce payment, the tender reference is absent: use `.pspReference` with the leading dot, original date and matching currency. The request sets `ReversalReason=MerchantCancel`; in this guide that field belongs to the referenced-refund request and does not turn receipt into a completed authorization cancellation.
- Partial Terminal API reversals add numeric `ReversedAmount` no greater than the initial payment amount, a currency matching the original payment, and a refund sale-transaction reference/timestamp. Full and multiple partial refunds are described, subject to original-payment value and remaining balance. The terminal's `ReversalResponse.Response.Result=Success`, refund PSP reference and receipt marked **REFUND REQUESTED** confirm receipt only; wait for the `CANCEL_OR_REFUND` webhook. A terminal `ServiceID` must be unique for that terminal during the preceding 48 hours, but this guide does not state an idempotent retry rule.
- The server path posts to Checkout `/payments/{paymentPspReference}/refunds` using the original payment PSP reference, `merchantAccount`, and `amount`. The amount value is the captured amount or less for a partial refund, and currency matches authorization. `reference` is generally presented as optional but required for GrabPay refunds. The API response's `status=received` and distinct refund `pspReference` are request receipt, not money movement; wait for the `REFUND` webhook. Language-specific code examples show particular library versions and idempotency-key calls, not a general guarantee for every client or pending retry.
- The two webhook event types report Adyen's refund **validation** outcome. `success=true` means validation passed and the request was sent to the card scheme; rare later rejection or reversal can still occur through `REFUND_FAILED` or `REFUNDED_REVERSED`. `success=false` includes a reason. Failure examples include exhausted remaining payment balance, insufficient in-process funds, currency mismatch, an uncaptured payment and method expiry. For an uncaptured transaction, the guide says to cancel instead or wait until settlement; do not equate refund submission with a captured payment, issuer approval or settled refund. Refund authorization is described for American Express, Discover, Mastercard and Visa; even if issuer refund authorization declines, Adyen says it still attempts processing.

## Detail locators

- Raw `# Referenced refunds` through `## Benefits` (lines 15–56): cross-channel merchant/account funds, asynchronous receipt, shared PSP reference, prerequisites and original-payment-method return.
- Raw `## Refund authorization` / `## Refund options` (lines 57–88): four named network scope, issuer decline and terminal, server, Customer Area options.
- Raw `## Send a Terminal API reversal request` (lines 89–413): POS versus ecommerce original identifiers, full/partial fields, `MerchantCancel`, receipt-only response, failure messages and `CANCEL_OR_REFUND` wait.
- Raw `### Refunding an ecommerce payment` (lines 414–514): leading-dot ecommerce PSP reference, original date/currency, zero amount fields in the immediate ecommerce full response and partial variant.
- Raw `## Send a server-to-server refund request` (lines 515–767): original PSP reference, merchant account, captured amount/currency, GrabPay reference exception, dated SDK samples and receipt response.
- Raw `## Webhooks` / `### Reasons for failed refund validation` (lines 768–911): distinct events, validation versus final outcome, later exceptions and remaining-balance/capture/funds failures.

## Related

- [[adyen-unified-commerce]] — cross-channel merchant journey and data route.
- [[adyen-refunds]] — online captured-payment refund lifecycle.
- [[adyen-terminal-api]] — in-person reversal message and terminal response.
- [[adyen-online-payments]] — Checkout API payment/capture context.

## Related raw API references

Navigation named in this guide, not additional reviewed behavior for this entry:

- Checkout payment refund endpoint — https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds
- Terminal API reversal endpoint — https://docs.adyen.com/api-explorer/terminal-api/latest/post/reversal
- Standard webhooks — https://docs.adyen.com/development-resources/webhooks

## Raw Sources

- [[raw/adyen/docs/unified-commerce/referenced-refunds/2026-09-15|Referenced refunds, fetched 2026-09-15]]
