---
title: "IRIS payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/iris"
raw_files:
  - "adyen/docs/payment-methods/iris/2026-09-15.md"
tags: [adyen, iris, greece, online-banking, redirect]
---

## Overview

This 2026-09-15 capture of Adyen's IRIS method page describes a Greek bank-account payment method, bank-contract and DIAS onboarding through Adyen as gateway, the supported-operation matrix, and Web/API-only/in-person routes. Its assertion that IRIS is mandatory for merchants with business in Greece is a **dated page claim**, not current legal guidance or proof that a particular merchant is enabled. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page describes IRIS as a Greek-bank method for customers to pay directly from bank accounts and says it is mandatory for any merchant with business in Greece, for e-commerce and in-store payments. Preserve that wording as the source's 2026-09-15 claim; current legal scope and merchant applicability need separate verification (raw lines 21–24).
- For IRIS through Adyen, the merchant needs a contract with an IRIS acquiring bank; Adyen acts as **gateway**. The bank list is expressly dated **November 2025**: Alpha Bank, National Bank of Greece, Eurobank, Piraeus Bank, Viva.com, and Credia Bank. This list is historical, not a current participation assertion (raw lines 26–28).
- Refunds and cancellations are **not supported through Adyen** for this route; handle them with the contracted Greek bank. The GR/EUR Online Banking matrix lists a Redirect flow, crosses for recurring, Adyen refunds (including partial/multiple), separate/partial/multiple captures, and chargebacks, with a “See note” pointer on refund columns. Do not interpret the crosses as saying the bank cannot process a refund or cancellation (raw lines 28–29, 39–41).
- For onboarding, contact the bank for IRIS, tell it Adyen will be the gateway/processor, and complete its Annex A DCT Creditor Parameters form to register with DIAS and obtain the five-digit DIAS Merchant Identifier. The page says item 5 Payment Code Standard must be “RI0.” Additional bank connectivity forms for Adyen are described as usually skippable because Adyen–DIAS connectivity is generic; if requested, verify applicability with the acquiring bank (raw lines 31–37).
- Web pre-built UI, API-only custom UI for website/iOS/Android, and in-person routes are listed. They are navigation to separate guides, not proof of configuration or live processing (raw lines 43–61).

## Detail locators

- Identity, dated mandatory-use statement, gateway/bank contract and operation limitation: raw `# IRIS` lines 15–29.
- Greek-bank and DIAS onboarding: raw `### Onboarding process with Greek bank` lines 31–37.
- GR/EUR Redirect capability matrix: raw lines 39–41.
- Integration chooser: raw `## How do you want to integrate?` lines 43–61.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/iris/2026-09-15|IRIS method overview, captured 2026-09-15]]
