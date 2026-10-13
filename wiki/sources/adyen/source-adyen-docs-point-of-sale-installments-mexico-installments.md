---
title: "Installments in Mexico | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/installments/mexico-installments"
raw_files:
  - "adyen/docs/point-of-sale/installments/mexico-installments/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, installments, mexico]
---

## Overview

Adyen's Mexico in-store installments guide explains how a merchant POS flags debit versus credit and requests **credit-card** installment payments through Terminal API. The shopper chooses with store staff, who enter that choice and installment count into the POS before the card is presented to the terminal. The pinned webpage was fetched 2026-09-15 and itself reports `last_modified` 2026-09-15; its program/issuer list and terms are dated documentation, not proof of current card eligibility, interest terms, legal compliance, or a successful payment. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- This is for Terminal API integrations with payment terminals **in Mexico** and only specified participating issuing banks/programs. The page says most credit cards and debit/credit combo cards can be used for installment purchases, but the supported-card section narrows Adyen's documented programs to Prosa, Mastercard, Nubank, Citibanamex, and Bancoppel with named issuers. For cards issued by other banks, it says the merchant must have a direct legal agreement with that bank. Do not infer approval for every card, scheme, issuer, account, or region from the general description.
- Staff ask whether the shopper wants debit or credit; for credit, whether to pay once or in installments; and, if installments, how many. The **POS app**, not an automatic terminal menu described here, puts these choices in the Terminal API `PaymentRequest`. Set `TransactionConditions.DebitPreferredFlag` to `true` for debit or `false` for credit. For a credit installment request add `PaymentData.PaymentType: Instalment` and `Instalment.TotalNbOfPayments` from **3 to 18**; debit or one-off credit needs no further installment parameters. The guide's request table requires unique `ServiceID` per terminal within 48 hours and recommends a unique sale transaction reference per payment.
- When the transaction is approved, the response contains receipt data with `productType` for debit, credit, or installment choice. An installment response also has `PaymentResult.PaymentType: Instalment` and the installment details. The example's `Response.Result: Success` is a sample approved result, not a guarantee that the request or issuer will approve.
- The page says the **full purchase amount** is deducted from the shopper's credit limit; the issuing bank then debits each monthly installment from the shopper's debit account. The merchant receives the full purchase amount from the issuing bank and is responsible for issuer-charged installment fees. This describes who pays and receives the full amount, not an interest-free promise, a specific fee rate, or a guaranteed settlement time.
- The page does not define merchant-setting enablement, terminal software versions, pre-authorization/capture adjustments, interest rates, shopper installment disclosures, or broader legal duties. Those must be established from their own current authority before use; Brazil or online installment instructions are separate flows.

## Detail locators

- Mexico scope, shopper/POS choice and merchant fee: pinned raw, introduction and `## How it works` (lines 15–46).
- Terminal API requirement and supported-issuer condition: pinned raw, `## Requirements` (lines 25–30).
- Debit/credit flag, installment request fields, 3–18 range, request identities, and sample payloads: pinned raw, `## Make a payment` (lines 48–214).
- Approved response, receipt `productType`, and installment fields: pinned raw, `## Make a payment`, result section (lines 216–252).
- Credit-limit, issuing-bank monthly debit, merchant full amount and fee responsibility: pinned raw, `## Reconciling installments` (lines 254–258).
- Five program/issuer lists and direct-bank legal-agreement condition: pinned raw, `## Supported cards` (lines 260–274).

## Related

- [[adyen-terminal-api]] — in-person Terminal API payment architecture.
- [[source-adyen-docs-point-of-sale-installments-brazil-installments]] — separate Brazil POS installments guide.
- [[adyen]] — provider hub.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/installments/mexico-installments/2026-09-15|Installments in Mexico — 2026-09-15 snapshot]]
