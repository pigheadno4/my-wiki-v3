---
title: "Ratepay payment method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ratepay"
raw_files:
  - "adyen/docs/payment-methods/ratepay/2026-09-15.md"
tags: [adyen, ratepay, buy-now-pay-later, direct-debit]
---

## Overview

This Ratepay method overview, last modified 2022-12-15 and captured 2026-09-15, describes Ratepay Open Invoice buy now, pay later and secured direct debit, its risk and payout statements, a capability matrix, and Web/API-only integration routes. It is a dated source snapshot, not evidence of current availability, account enablement, or a successful live payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The prose says Open Invoice is available in Austria, Germany, the Netherlands, and Switzerland, while secured direct debit is described for Austria, Germany, and the Netherlands. The capability matrix, however, combines “Buy Now Pay Later, Direct Debit” in **DE, AT, NL / EUR** and omits Switzerland. Treat Switzerland availability as an **internal page mismatch** requiring verification against current method/merchant configuration; do not silently extend the matrix to CH or erase the prose (raw lines 17, 23, 29–31).
- Ratepay performs shopper risk checks **before approval**. The page says that **if successful**, Ratepay takes full fraud risk and pays the merchant up front. For shoppers choosing Buy Now Pay Later, the page further says Ratepay pays the merchant as soon as the payment is captured; these are source claims with the stated conditions, not a guarantee of approval or settlement timing for a merchant (raw lines 25–27).
- In the combined DE/AT/NL EUR capability row, the payment flow is “Additional action.” The row marks recurring and chargebacks with crosses, and refunds, partial refunds, multiple partial refunds, separate captures, partial captures, and multiple partial captures with checks. Because the row combines two payment types and conflicts with the prose country list, use it as the source's matrix rather than a current per-product eligibility promise (raw lines 29–31).
- The page routes Web integrations to pre-built website UI solutions and API-only integrations to building a custom UI for website, iOS, or Android app (raw lines 33–45).

## Detail locators

- Method geography, product distinction, risk and payout: raw `# Ratepay` lines 15–27.
- Capability row and its CH-versus-matrix discrepancy: raw lines 29–31.
- Integration chooser: raw `## How do you want to integrate?` lines 33–45.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/ratepay/2026-09-15|Ratepay method overview, captured 2026-09-15]]
