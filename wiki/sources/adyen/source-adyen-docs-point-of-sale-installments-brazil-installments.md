---
title: "Adyen Docs: In-person installments in Brazil"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/installments/brazil-installments"
raw_files:
  - "adyen/docs/point-of-sale/installments/brazil-installments/2026-09-15.md"
tags: [adyen, point-of-sale, brazil, installments, terminal-api]
---

## Overview

This Adyen guide covers in-store Brazilian card choice between credit, debit, and voucher, then one-off credit or credit-card installments. It describes an Adyen terminal UI flow for integrated or standalone terminals and a merchant-owned UI flow that passes shopper choices in a Terminal API payment request. Its terms and examples are dated website evidence; it does not establish current card-scheme/acquirer coverage, account eligibility, shopper interest or financing terms, or live payment success.

## Key takeaways

- The Adyen UI flow requires Support enablement at a chosen company, merchant-account, store, or terminal level, and the page requires terminal software v1.119 or later. The terminal asks the shopper for credit/debit/voucher, then one-off versus installments and a count if credit installments are chosen. The flow applies to integrated and standalone terminals. See **Requirements** and **Adyen UI**.
- In the merchant-owned UI flow, store staff, a secondary screen, or terminal input can collect the shopper's choice; the POS passes that choice in a Terminal API request. For credit installments, the request must identify credit and include `PaymentData` with `PaymentType: Instalment`, equal installments, monthly period, and `TotalNbOfPayments` from 2 through 36. A debit or one-off credit request needs no installment object in this guide. See **Your own UI → Make a payment with Terminal API**.
- The page recommends Base64-encoded `selectedAccountType` in `SaleData.SaleToPOIData` to identify `CREDIT`, `CHEQUE` (debit), or `MEAL_VOUCHER`; alternatively, `TransactionConditions.DebitPreferredFlag` supports only credit/debit (`false`/`true`). If both appear, `selectedAccountType` takes precedence. These field choices are specific to this Brazil POS flow; the request examples are illustrative, not evidence of current SDK-version behavior or all voucher products. See **Make a payment with Terminal API**.
- An integrated terminal response can show installment type/count in `PaymentResult` and `installments=` in `AdditionalResponse`. For a successful payment, generated merchant and shopper receipt data includes `productType` and Brazilian `cnpj`, with installment count when applicable. The sample 12-installment `BRL 120.00` request/response is an example, not a guarantee of approval or interest/pricing. See **Adyen UI**, **Your own UI**, and **Make a payment with Terminal API → PaymentResponse**.
- The reconciliation section says the first installment is charged to the shopper's credit card immediately, later installments automatically, and the merchant receives funds as each installment settles after a stated 30-day settlement delay. Adyen describes optional earlier advancement for an additional fee through its Account Manager. Standalone-terminal users must manually reconcile POS transactions against sales and returns. The page does not specify interest bearer, installment principal/interest allocation, scheme or acquirer applicability, or current commercial terms. See **Reconciling installments**.

## Detail locators

- **Requirements** — Brazil combo-card statement, integrated/standalone scope, Adyen UI v1.119 gate and Support configuration level.
- **Adyen UI** — terminal-owned shopper prompts, integrated/standalone applicability, receipt and integrated-response installment fields.
- **Your own UI** — shopper/staff input options and POS handoff.
- **Make a payment with Terminal API** — payment-mode encoding/precedence, request header/reference/amount, 2–36 equal monthly installments, and illustrative JSON/Java payloads.
- **Make a payment with Terminal API → PaymentResponse** — receipt keys, successful response installment fields and example payload.
- **Reconciling installments** — shopper charging schedule, merchant settlement timing, advancement fee, and standalone reconciliation responsibility.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/installments/brazil-installments/2026-09-15|Adyen Docs — Installments in Brazil (2026-09-15)]]
