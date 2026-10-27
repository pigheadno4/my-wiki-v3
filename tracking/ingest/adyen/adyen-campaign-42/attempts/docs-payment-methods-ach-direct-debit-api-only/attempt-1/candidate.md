---
title: "ACH Direct Debit API-only integration | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/api-only"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/api-only/2026-09-15.md"
tags: [adyen, ach-direct-debit, api-only, sec-code, mandate, bank-account]
---

## Overview

This 2026-09-15 Adyen guide adds ACH Direct Debit to an existing API-only integration with a merchant-built form and method-specific `/paymentMethods` and `/payments` fields. It is not a complete base integration, a standalone bank-account verification service or proof of debit completion. The related [[source-adyen-docs-payment-methods-ach-direct-debit|ACH overview]] supplies US-entity eligibility, consumer validation, B2B bank allowlisting, signed mandate, asynchronous reversal, refund and blocklist context (this raw lines 15–46; overview raw lines 23–29, 35–86).

## Key takeaways

- The page requires an existing API-only integration, ACH added in Customer Area and subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` for outdated banking details. The **Merchant allow bank-refund** role applies specifically when issuing a refund by API or Customer Area; it is not phrased as a prerequisite for taking an ACH payment. `/paymentMethods` specifies `countryCode` US or PR and USD. The overview separately requires a registered US business entity, so PR availability does not waive that merchant condition (this raw lines 23–40; overview raw lines 23–25).
- The merchant-built form collects account number, nine-digit ACH routing number (preserve leading zeros; do not use a wire routing number), checking/savings type, holder name and personal/business holder type; address is optional. Use the details to obtain the customer mandate. If `bankAccountType` is omitted, it defaults to `checking`; a savings-account mismatch can cause a chargeback, so Adyen recommends collecting the type explicitly. Routing-number genuineness validation mentioned here is narrower than consumer bank-account validation: the overview says Nacha requires the latter and points to giact (this raw lines 42–61; overview raw lines 35–37, 61–63).
- Nacha requires a correct SEC code. The guide offers `additionalData.ach.secCode`, `paymentMethod.accountHolderType` (business maps to **CCD**, personal to **WEB**), or a Support-configured default. Its prose says Adyen otherwise tries to infer from the holder name and falls back to **WEB** if uncertain; do not treat that fallback as assuring the correct authorization type. The `/payments` table calls the explicit SEC field optional and lists **CDD** for B2B, whereas the same page's prose says **CCD** and the overview consistently says CCD. The overview says API-only integrations need to specify the SEC code. Preserve this CDD/CCD and optional/fallback tension; verify the authoritative field/code path before implementation. A signed customer mandate remains required before one-off or recurring initiation, independent of SEC selection (this raw lines 63–92; overview raw lines 47–63).
- For `/payments`, the table marks `paymentMethod.type: ach`, holder name, and either clear or encrypted account number plus either clear or encrypted routing number required; bank account type and SEC/account-holder type are listed optional. The examples show opaque `adyenjs_...` values but do not explain how to generate or secure them. The curl example lacks a continuation before `-d` and has a trailing comma in its JSON; a Node example has `country: US` with `city: Amsterdam` in its billing address. Do not copy these as validated live requests or treat sample ciphertext as a reusable credential (raw lines 80–119, 255–293).
- The page offers TEST account/routing formats and an `ownerName` value `chargeback:R01` to simulate a return; it does not provide a full payment-outcome or retry procedure. The overview says ACH has no real-time bank authorization, reversals can follow and ACH chargebacks cannot be defended; reason-code-specific retry belongs to the linked chargeback authority. For refunds, the overview requires settlement and the bank-refund role and describes a three-day post-settlement delay. B2B ACH Company ID allowlisting and Adyen-wide terminal-return blocks are also overview conditions, not established by this page's test request (this raw lines 441–463; overview raw lines 29, 39–45, 65–128).

## Detail locators

- API-only/setup/refund-role distinction and `/paymentMethods` US/PR/USD: raw lines 23–40.
- Form account/routing/type/mandate and checking default: raw lines 42–61.
- SEC methods, fallback and CDD/CCD table inconsistency: raw lines 63–92.
- `/payments` clear/encrypted fields and sample limitations: raw lines 80–119, 255–293.
- TEST payment and `chargeback:R01` return simulation: raw lines 441–457.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-ach-direct-debit|ACH overview (entity, validation, mandate and reversal authority)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/api-only/2026-09-15|ACH Direct Debit API only, fetched 2026-09-15]]
