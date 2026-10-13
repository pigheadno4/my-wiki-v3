---
title: "Adyen Docs: In-person installments in Japan"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/installments/japan-installments"
raw_files:
  - "adyen/docs/point-of-sale/installments/japan-installments/2026-09-15.md"
tags: [adyen, point-of-sale, japan, installments, terminal-api]
---

## Overview

This Adyen website page describes Japan credit-card installment choices on a payment terminal after Support enables the feature for a merchant account. It covers Terminal API and standalone terminal starts, regular and revolving shopper plans, terminal selection, receipts, and the merchant-versus-bank money flow. The 2026-09-15 snapshot does not establish current issuer/card eligibility, supported schemes, interest or fee terms, software/SDK versions, bonus-payment plans, or a live transaction outcome.

## Key takeaways

- The page limits the feature to Japan, covers integrated Terminal API or standalone terminals, and instructs the merchant to contact Adyen Support to enable credit-card installments on its merchant account. It says Japanese installment payments are supported automatically after that enablement; it does not promise every shopper card or issuer supports every plan. See **Installments in Japan** and **Requirements**.
- Regular plans split the purchase into 2–99 equal monthly installments. In a revolving plan, the shopper makes an initial partial payment and the remaining installments depend on the shopper's agreement with their bank. The page gives no interest rate, bonus-month schedule, or issuer-by-issuer plan rules. See **Installments in Japan**.
- Whether the merchant POS sends a Terminal API payment request or staff start payment on a standalone terminal, the page says no additional installment fields are needed in the payment request. The shopper presents the card and chooses one-off, split, or revolving on the terminal, plus the count for split payments; PIN or signature follows. On approval, receipt data is returned and the terminal prints merchant then shopper receipts. These are terminal-choice steps, not multiple POS payment requests. See **How it works**.
- For both regular and revolving plans, the page says the merchant receives the full purchase amount immediately from the bank, while the shopper pays the bank in installments. Standalone operators must manually reconcile POS transactions to their sales and returns. This is the page's stated money flow, not a promise of exact settlement timing for every merchant or bank. See **Reconciling installments**.

## Detail locators

- **Installments in Japan** — regular 2–99 equal monthly installments, revolving initial payment and bank-agreement dependence, post-enablement statement.
- **Requirements** — Japan, Terminal API/standalone scope, and Support merchant-account enablement.
- **How it works** — POS versus standalone start, no extra request fields, shopper terminal choices, verification and receipt sequence.
- **Reconciling installments** — bank-to-merchant full amount, shopper-to-bank installment repayment, and standalone manual reconciliation.
- **See also** — separate Terminal API payment, receipts, notifications, standalone, and fundamentals routes; navigation only.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/installments/japan-installments/2026-09-15|Adyen Docs — Installments in Japan (2026-09-15)]]
