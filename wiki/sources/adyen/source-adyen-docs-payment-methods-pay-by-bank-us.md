---
title: "Pay by Bank (US) | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/pay-by-bank-us"
raw_files:
  - "adyen/docs/payment-methods/pay-by-bank-us/2026-09-15.md"
tags: [adyen, pay-by-bank-us, open-banking, ach, tokenization]
---

## Overview

This Adyen payment-method overview describes Pay by Bank (US) as a US/USD online-banking redirect method for account-to-account payment routed over ACH Direct Debit. On an initial payment, the shopper goes to Adyen's open-banking partner Plaid to permit an account connection and select an issuing bank, then to the bank's site or app to permit collection of the data needed for the payment, and then back to the merchant site or app. The page links separate Web, iOS, Android and API-only integration guides; it is not an endpoint or SDK implementation guide (raw lines 22–32, 50–74).

## Key takeaways

- The capability table marks recurring, refunds, partial and multiple partial refunds, separate and partial captures, and chargebacks as supported for this US/USD redirect method; it marks multiple partial captures unsupported. These are the page's capability indications, not proof of merchant enablement or a completed transaction (raw lines 30–32).
- The page recommends, rather than mandates, tokenizing payment details during the first transaction because the initial redirect steps may reduce conversion. It says later transactions using stored details can complete after selecting **Pay** without another redirect. It also says a Plaid-connected shopper need not log in to the bank on every later payment (raw lines 24–26, 34–38).
- ACH Direct Debit return rules still apply. The page says account validation, balance and risk checks reduce but do not eliminate returns. It gives B2B allowlisting of Adyen ACH Company ID **8263863381** as a possible reversal issue and describes consumer and business dispute windows of up to two years and one year after settlement, respectively (raw lines 40–44).
- A returned payment produces a debit line in the Settlement details report and a `CHARGEBACK` webhook with `chargebackReasonCode`. The page says Pay by Bank (US) chargebacks cannot be defended; retry may be allowed depending on the reason code (raw lines 46–48).

## Detail locators

- Shopper/Plaid/bank permission and redirect sequence: raw lines 22–28.
- US/USD capability matrix and multiple-partial-capture exception: raw lines 30–32.
- First-payment tokenization recommendation and later stored-detail experience: raw lines 34–38.
- ACH returns, allowlist ID, dispute windows, report/webhook and retry limits: raw lines 40–48.
- Separate Web, iOS, Android and API-only integration routes: raw lines 50–74.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/pay-by-bank-us/2026-09-15|Pay by Bank (US) overview, fetched 2026-09-15]]
