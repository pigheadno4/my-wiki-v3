---
title: "Online banking Finland"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/2026-09-15.md"
tags: [adyen, finland-online-banking, finland, online-banking, payments]
---

## Overview

This 2026-09-15 Adyen method overview describes **Online banking Finland**, offered through partner Paytrail, as a Finnish bank redirect payment method. The shopper selects a bank, authenticates through bank pages or apps, confirms payment, and returns to the merchant site or app. The page also routes to platform-specific integrations. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The introductory paragraph says Online banking Finland is supported by all major banks in Finland, has bank selection in a checkout dropdown, and redirects the shopper to the bank website or app. This is a claim in the dated capture, not a current bank-coverage guarantee. See raw line 23.
- The numbered journey instead describes redirecting the shopper first to an **Adyen-hosted payment page** with available banks, selecting a bank there, authenticating with the bank, choosing an account, entering a one-time code, and returning to the merchant site or app after completing the payment. The page does not state how this bank-selection location varies by integration; keep the two descriptions qualified. See raw lines 25–32.
- The capability matrix labels this method **Online Banking**, **redirect**, **FI**, and **EUR**. It crosses recurring, separate captures, partial captures, multiple partial captures, and chargebacks; it checks refunds, partial refunds, and multiple partial refunds. The refunds cell adds **“See note”** but this capture contains no corresponding note, so it does not establish the missing refund qualification. These are snapshot method labels, not proof of account enablement. See raw lines 34–36.
- The integration chooser links Web, iOS, Android, React Native, Flutter, API-only merchant UI, and Pay by Link routes. These are navigation; implementation prerequisites and supported bank/issuer choices belong to their respective child/API guides. See raw lines 38–80.

> [!warning] Bank-selection and refund qualification
> The intro locates bank selection in the merchant checkout dropdown (raw line 23), while the numbered journey locates it on an Adyen-hosted page (lines 29–30). The source does not reconcile or scope these descriptions. Its refunds mark says “See note” (line 36), but no note appears in the pinned page. Do not choose one bank-selection route or infer the absent refund condition as a universal rule.

## Detail locators

- Partner, bank selection and redirect descriptions: raw lines 23–32.
- FI/EUR capability matrix and missing refund note pointer: raw lines 34–36.
- Platform/API-only/Pay by Link routes: raw **How do you want to integrate?**, lines 38–80.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/2026-09-15|Online banking Finland overview, captured 2026-09-15]]
