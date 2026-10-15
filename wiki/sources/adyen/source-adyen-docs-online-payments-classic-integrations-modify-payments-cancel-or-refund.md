---
title: "Cancel or refund | Adyen Classic integrations"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/modify-payments/cancel-or-refund"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/modify-payments/cancel-or-refund/2026-09-15.md"
tags: [adyen, classic-integrations, online-payments, cancel, refund, webhooks]
---

## Overview

This Adyen Classic integrations guide describes `/cancelOrRefund` when a merchant wants to return funds but does not know whether the payment has been captured. The operation cancels an uncaptured payment or refunds an already captured one. The page marks this endpoint inactive and unsupported for new integrations, directs new builds to Checkout API, and points existing users to migration guidance.

## Key takeaways

- The Classic request identifies the processing `merchantAccount` and uses `originalReference` for the original payment's `pspReference`, available from the payment response or `AUTHORISATION` webhook. Optional `reference` identifies the modification for reconciliation. The documented request does not show an amount parameter; its mention of tagging a partial modification is not an amount-control specification.
- The immediate `/cancelOrRefund` response provides the modification's own `pspReference` and a `[cancelOrRefund-received]` example. Receipt does not establish a completed cancellation or refund.
- The guide calls for enabled `CANCEL_OR_REFUND` webhooks to determine whether the request succeeded. In the refund path, `success: true` means Adyen's validations passed and the refund was sent to the card scheme; later scheme rejection or reversal remains possible through `REFUND_FAILED` or `REFUNDED_REVERSED`. `success: false` indicates failed validations and includes a reason.
- For Adyen for Platforms, Classic `/cancelOrRefund` does not accept split instructions. When split-refund instructions are needed, check capture state and use the separate Checkout cancel endpoint before capture or Checkout refund endpoint after capture. Do not use Classic `/cancelOrRefund` for payments involving multiple partial captures.

## Detail locators

- Raw lines 19–38 — inactive lifecycle, unknown-capture selection, platform split limitation, separate Checkout routes, and multiple-partial-capture exclusion.
- `Cancel or refund a payment` — request identity fields, optional modification reference, example request, and immediate received response.
- `CANCEL OR REFUND webhook` — enabled-event condition, original versus modification references, validation result, later refund exceptions, and illustrative webhook payload.

## Related

- Company: [[adyen]]
- Concept: [[adyen-refunds]]
- Related concepts: [[adyen-payment-capture]], [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel-or-refund/2026-09-15|2026-09-15 snapshot — Classic cancel or refund]]
