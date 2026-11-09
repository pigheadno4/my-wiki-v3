---
title: "Stripe Network Decline Codes"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/declines/network-codes"
raw_files:
  - "stripe-declines-network-codes-2026-11-07.md"
  - "stripe-network-decline-codes-2026.md"
tags: [stripe, declines, network-codes, cards, ach, becs, bacs, sepa, cash-app-pay, bank-debit, direct-debit]
---

## Overview

The May 9, 2026 [[stripe]] reference lists raw response codes for seven payment-method groupings: ACH Direct Debit, Australia BECS, Bacs, Cash App Pay, New Zealand BECS, Canadian pre-authorized debit, and SEPA Direct Debit. The November 7 same-URL capture retains those tables and adds **13 card-network or processor tables**. See [[stripe-declines]] for how a raw network code differs from a Stripe decline or advice code.

## Key takeaways

- The seven earlier method groupings remain in the November capture. The debit tables map a method-specific raw code to a Stripe **decline code** (ACH) or **failure code** (BECS, Bacs, PAD, SEPA), plus explanations and often next steps. Cash App Pay has a two-column raw-code-to-decline-code table without those explanations. For ACH `R05` and related mandate codes, the table says to collect a new mandate before retrying; other bank-debit rows call for updated account details or customer contact according to the exact method and code. These are conditional row-level instructions, not card-network retry rules.
- The new **Card Payments** section lists Visa, Cartes Bancaires, Eftpos AU, UnionPay, CAFIS JCB, Cybersource, Girocard, JCB International, Mastercard, American Express, Discover, NYCE, and Everlink (Interac). Each has **Raw network code** and **Explanation** columns. Unlike the debit and Cash App Pay tables, these card tables do not map each raw code to a Stripe `decline_code`, `advice_code`, or `network_advice_code`. Look up a code in the named network or processor table; the same string can mean something else elsewhere. For example, Visa `05` means “Don’t honor” while UnionPay `05` means “ID certification fails.”
- The Card Payments heading does not make every row a decline. JCB International `85` is explicitly “Not declined” for balance inquiry or zero-amount address verification. American Express `001` is “Approve with ID” and `003` is “Approve VIP (Visa only).” These are static row explanations, not evidence that any particular payment was authorized, captured, or settled.
- Mastercard rows include a raw code **with MAC value**. For example, `79 (MAC 02)` says invalid credentials and permits retry later, while `79 (MAC 03)` says account credentials not found and says not to retry. Other rows also vary by MAC. Preserve the exact combined row and do not collapse its advice into a universal retry rule or infer a Stripe `advice_code` from this reference.
- The older source's common-failure summary applies to the bank-debit examples, with method-specific next steps. `generic_could_not_process` is not a universal “contact Stripe Support” instruction: AU BECS `8`, Bacs ADDACS `R` and ARUDD `4/7/8`, and Canadian PAD `900` only say “The payment failed”; the SEPA `AG02/AM05/CNOR/DNOR/DN05/FF01/AC13` row specifically says to contact Support. Use the matching row's wording and any observed payment outcome rather than assuming a retry or escalation path.

## Detail locators

- ACH, Australia BECS, and Bacs raw-to-decline/failure mapping: [[raw/stripe-declines-network-codes-2026-11-07|November 7 reference]], lines 11–60; [[raw/stripe-network-decline-codes-2026|May 9 reference]], lines 10–59.
- Thirteen card-network and processor raw-response tables: November lines 62–815. Visa 66–137; Cartes Bancaires 139–221; Eftpos AU 223–272; UnionPay 274–344; CAFIS JCB 346–385; Cybersource 387–456; Girocard 458–482; JCB International 484–536; Mastercard 538–586; Amex 588–618; Discover 620–673; NYCE 675–753; Everlink 755–815.
- Cash App Pay, New Zealand BECS, Canadian PAD, and SEPA: November lines 817–875; May lines 61–119. Check the exact method, failure/decline column, and next-step cell before acting.

## Related

- [[stripe-declines]] — issuer declines, raw network codes, Stripe decline and advice fields.
- [[source-stripe-decline-codes]] — Stripe decline-code reference.
- [[source-stripe-declines-overview]] — decline overview.

## Raw Sources

- [[raw/stripe-declines-network-codes-2026-11-07|Stripe network codes, 2026-11-07]]
- [[raw/stripe-network-decline-codes-2026|Stripe network codes, 2026-05-09]]
