---
title: "Boleto Bancário"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/boleto-bancario"
raw_files:
  - "adyen/docs/payment-methods/boleto-bancario/2026-09-15.md"
tags: [adyen, boleto-bancario, brazil, voucher, payments]
---

## Overview

This 2026-09-15 Adyen method overview describes **Boleto Bancário**, a Brazilian voucher-based payment method. The shopper receives a voucher and can pay in cash, at an ATM, or through online banking. Voucher issuance is not payment completion. The page also routes to platform-specific integration guides. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The offered voucher type is **Boleto de Proposta**: it is a proposal to provide goods or services. Paying it means the shopper accepts the offer. If the shopper does not pay before the voucher expires, the offer is declined and the merchant is no longer obliged to reserve the goods or services, according to this captured page. See raw lines 23–25.
- Payment routes include printing and paying cash at a bank or registered shop, scanning or entering the barcode at an ATM, or entering the barcode number in a bank website or app. See raw lines 31–35.
- The page says Boleto Bancário payments are guaranteed and therefore have no chargeback risk. Its matrix labels the method **Cash and ATM**, **voucher**, **BR**, **BRL**, and marks recurring, refunds (including partial/multiple partial), separate/partial/multiple partial captures, and chargebacks unsupported. These are claims from this 2026-09-15 snapshot, not a current merchant or financial guarantee. See raw lines 37 and 41–43.
- If unpaid by the due date, the transaction remains open in Customer Area for **15 days**; the page then says the Boleto expires and transaction status becomes **Offer cancelled**. Do not treat issue or due date alone as proof of payment, and preserve the page's distinct due-date and later cancellation timing. See raw line 39.
- The integration chooser links Web, iOS, Android, React Native, Flutter, API-only, and Pay by Link routes. Those links are navigation, not evidence of behavior in unread child guides. See raw lines 45–87.

## Detail locators

- Boleto de Proposta and shopper payment paths: raw lines 23–35.
- Guarantee claim, expiry status timing, and capability matrix: raw lines 37–43.
- Platform and API-only integration choices: raw **How do you want to integrate?**, lines 45–87.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/boleto-bancario/2026-09-15|Boleto Bancário overview, captured 2026-09-15]]
