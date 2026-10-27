---
title: "Adyen Bank Transfer"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer/2026-09-15.md"
tags: [adyen, bank-transfer, virtual-bank-account, asynchronous, api-only]
---

## Overview

Adyen's 2026-09-15 Bank Transfer overview describes an asynchronous, shopper-initiated bank-transfer option for invoices or high-value B2B and B2C transactions. A payment response supplies a unique virtual bank account and country/region-specific details; the shopper separately initiates the transfer in their banking environment. The payment remains `Open` until Adyen receives funds, after which Adyen sends a webhook and the merchant can inform the shopper and fulfill. This is distinct from a merchant-initiated direct-debit mandate. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The merchant shows the virtual account and other required transfer details returned by the payment request. The shopper copies them into online or mobile banking and initiates the transfer. Because settlement is asynchronous, the checkout must clearly explain how to complete payment and when the order will be delivered; selection of Bank Transfer or issuance of account details is not proof of funds (raw lines 19-31).
- The source's payment-status sequence is explicit: `Open` lasts until Adyen receives funds on the virtual account, then Adyen sends a webhook, and the merchant informs the shopper and fulfills. Fulfillment should follow received-funds notification rather than the initial payment response (raw lines 23-29).
- The snapshot capability table labels the method `Bank transfer` with `Additional action`, countries `International`, currency EUR, recurring and refunds/partial refunds/multiple partial refunds marked available, and separate/partial/multiple partial captures and chargebacks marked unavailable. The recurring cell says “See note,” but this captured page gives no recurring procedure or conditions; do not infer automatic bank debit, mandate authorization or current account/country eligibility from the marks (raw lines 33-35).
- This overview says Bank Transfer is supported for API-only integrations and links a child guide whose UI can be built for a website, iOS or Android app. That is an integration route, not evidence that Web Drop-in/Components or native SDK method modules implement this bank-transfer flow (raw lines 37-45).

## Detail locators

- Purpose, virtual-account handoff, `Open` state, funds webhook and fulfillment: raw lines 15-31.
- Snapshot capability marks and missing recurring detail: raw lines 33-35.
- API-only route and channel UI link: raw lines 37-45.

## Related raw API references

- [[raw/adyen/docs/payment-methods/bank-transfer/api-only/2026-09-15|Bank Transfer API-only child guide (unread navigation)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer/2026-09-15|Bank Transfer overview (2026-09-15 snapshot)]]
