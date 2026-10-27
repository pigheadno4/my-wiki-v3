---
title: "ACH Direct Debit overview"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/2026-09-15.md"
tags: [adyen, ach-direct-debit, bank-debit, mandates, chargebacks, refunds, online-payments]
---

## Overview

This 2026-09-15 Adyen ACH Direct Debit overview describes US-network bank debits for online payments, including entity eligibility, consumer validation, B2B bank allowlisting, SEC codes, signed mandates, chargebacks, refund timing, and blocked-account recovery. It is an overview with links to Web, native, API-only and Pay by Link routes; it does not itself prove account activation or a successful debit. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page describes ACH Direct Debit as used in the **US and Puerto Rico**, processed via the ACH network, while requiring the accepting merchant to have a **registered business entity in the United States**. Its capability table is a 2026-09-15 snapshot: PR/US, USD, Direct flow; it marks recurring, refunds, partial/multiple partial refunds, separate captures and chargebacks supported, but partial/multiple partial captures unsupported. These marks are not current account or bank coverage proof. See raw lines 23–33.
- Both one-off and recurring payments are supported, but Adyen **does not recommend one-off ACH Direct Debit** because of chargeback risk. ACH cannot give real-time authorization; insufficient funds may reverse a transaction, and the page says consumers can dispute up to **two years after settlement** on unauthorized or revoked-authorization grounds. Do not treat an initial authorization state as irrevocable funds. See raw lines 27–29 and 65–74.
- For **consumer** accounts, the page says Nacha requires bank-account validation and points to Adyen's giact flow. For **B2B** accounts, merchants should have business customers allowlist Adyen's ACH Company ID `8263863381`; otherwise an unknown-entity transaction can return as **R29**. These are distinct consumer-validation and business-bank-permission conditions. See raw lines 35–45.
- Every ACH payment needs a correct **SEC code** identifying its authorization type: CCD for B2B, PPD for consumer authorization obtained in writing, and WEB for consumer online/mobile authorization. A mismatch can lead to chargeback. Components and Drop-in handle the SEC code automatically; API-only integrations must specify it. This is separate from Nacha's **customer mandate** requirement before one-off or recurring initiation: the signed authorization describes the account, transaction type/frequency/amount and revocation information. See raw lines 47–63.
- Reversals produce a settlement-report credit/debit pair and a `CHARGEBACK` webhook with `chargebackReasonCode`. ACH Direct Debit chargebacks **cannot be defended**; a retry may be allowed depending on reason code. This page delegates detailed reason-code, process and testing guidance to the ACH chargebacks child page. [[adyen-risk-management]] See raw lines 65–74.
- Refunds require a **settled payment** and the `Merchant allow bank-refund` role, via Customer Area or API. Adyen delays the refund for **three days after settlement**; if a chargeback begins within that period, the refund request is automatically canceled and a `CHARGEBACK` webhook follows. See raw lines 76–80.
- Adyen says terminal bank-account returns/rejections can create an **Adyen-wide block** for that bank account across merchants/platforms. A subsequent attempt fails immediately with Customer Area code `1063_101` or `CAPTURE_FAILED`; listed triggers are R02, R03, R04, R12, R13, R14, R15, R20 and R34. If details have changed, a new payment can use updated details; otherwise unblock requires a permanently resolved issue, official bank documentation and Support review. Do not infer that a merchant can self-unblock or that all failed ACH attempts trigger the list. See raw lines 82–128.

## Detail locators

- ACH geography, US business entity, one-off warning and capability table: raw lines 23–33.
- Consumer validation, B2B Company ID and R29: raw lines 35–45.
- SEC code types, integration responsibility and signed mandate: raw lines 47–63.
- Reversal/chargeback signals and nondefensibility: raw lines 65–74.
- Settled-only refunds, role and three-day cancellation overlap: raw lines 76–80.
- Adyen-wide blocklist, return codes and documented unblock options: raw lines 82–128.
- Web, iOS, Android, Flutter, API-only and Pay by Link guide choices: raw lines 130–166.

## Related

- [[adyen-online-payments]] — main online-bank-debit route.
- [[adyen-risk-management]] — chargeback and blocked-account outcomes.
- [[adyen-payment-capture]] — general capture context; method table limits are on this page.
- [[source-adyen-docs-risk-management-chargeback-guidelines-ach-chargebacks]] — ACH reason-code and dispute guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/2026-09-15|ACH Direct Debit overview, captured 2026-09-15]]
