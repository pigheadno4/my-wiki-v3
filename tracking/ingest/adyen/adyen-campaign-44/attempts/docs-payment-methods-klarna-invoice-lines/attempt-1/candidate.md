---
title: "Adyen Klarna invoice lines and discounts"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/klarna/invoice-lines"
raw_files:
  - "adyen/docs/payment-methods/klarna/invoice-lines/2026-09-15.md"
tags: [adyen, klarna, invoice-lines, discounts, capture, refund, authorization-adjustment]
---

## Overview

This Adyen Docs page, captured 2026-09-15 with a 2025-09-04 last-modified marker, explains Klarna line-item data for payment requests, partial captures/refunds, discounts and authorization adjustments. It is request-shaping guidance, not proof that a payment, capture, refund or adjustment succeeded. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Any Klarna payment request includes price/product `lineItems`; the page says Klarna approves only if their total matches `amount.value`. The request table marks `quantity`, `description` and per-item `amountIncludingTax` required, with tax/ID/URL fields described separately. The EUR 10 example's two product lines total EUR 10. This ordinary matching rule has an explicit discount fallback below.
- For partial capture, supply `lineItems` to Checkout `/payments/{paymentPspReference}/captures`; the table marks quantity, amount excluding tax, tax percentage and description required. Partial refund uses Checkout `/payments/{paymentPspReference}/refunds` with the same listed fields and the original authorization PSP reference in the path. Each modification request returns a PSP reference, followed by a `CAPTURE` or `REFUND` webhook after processing. The examples alone do not prove final success, and both partial examples reuse `Item #1` for two different items, so their IDs should not be copied as unique-item evidence.
- Discount options are: lower each affected item's pre-tax, tax and tax-inclusive amounts; retain original product prices and add a negative `Discount` line including product and VAT discount; or let Adyen add a discount line when `amount.value` is lower than the submitted line total. The last is described as a fallback when other methods do not work. It is the page's stated exception to the ordinary total-matching instruction; validate the applicable invoice behavior rather than assuming an arbitrary mismatch is accepted. The whole-basket sample includes a `//` comment inside a `json` fence and is illustrative, not strict JSON.
- Authorization adjustment applies before full capture and is available for Klarna with Checkout API v70+. The update must include **all captured and refunded line items**, including when reducing an authorization or adding a product to a partly captured/refunded order. Its two `/amountUpdates` examples are illustrative: the base order uses SEK, while the updates use EUR, and their `curl https: //...` URL has a space. Do not treat those snippets as verified executable requests or infer an approved cross-currency adjustment.

## Detail locators

- Payment `lineItems` rule, field table and EUR 10 example: pinned raw lines 19–81. Partial capture/refund fields, examples and webhook boundaries: lines 83–189.
- Per-item, whole-basket and Adyen-added discount methods: lines 191–355; fallback exception is at lines 322–324.
- Adjustment API version/all-item rule and original SEK example: lines 357–1061. Partial cancellation and added-product `/amountUpdates` examples, including EUR and malformed URL text: lines 1063–1143.

## Related

- [[adyen-online-payments]] — provider concept and reciprocal source route

## Raw Sources

- [[raw/adyen/docs/payment-methods/klarna/invoice-lines/2026-09-15|Klarna invoice lines and discounts, captured 2026-09-15]]
