---
title: "Afterpay | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/afterpaytouch"
raw_files:
  - "adyen/docs/payment-methods/afterpaytouch/2026-09-15.md"
tags: [adyen, afterpay, buy-now-pay-later, redirect, chargebacks]
---

## Overview

This 2026-09-15-captured [[adyen]] overview describes **Afterpay** as a buy now, pay later redirect method for Australia, Canada and New Zealand, with AUD, CAD and NZD in its product table (raw lines 23–29). It says shoppers can pay in four installments. Afterpay performs risk checks before approval; **if successful**, the page says Afterpay takes full fraud risk for that payment and pays the merchant up front (raw line 25). The page identifies Cash App Afterpay/`$Afterpay` in the US and Clearpay in the UK as regional names; those names do not extend this overview's AU/CA/NZ product table or prove equivalent account eligibility (raw line 31). See [[adyen-online-payments]].

## Key takeaways

- **Method and lifecycle:** The table labels Afterpay a buy now, pay later redirect method. It shows checkmarks for recurring, refunds, partial and multiple partial refunds, separate and partial captures, multiple partial captures, and chargebacks; recurring and refunds each say “See note,” but this captured page does not include the note text (raw lines 27–29). Treat the table as a feature directory, and use the selected integration and modification guides for actual conditions, request shapes and operational support.
- **Principal flow:** The numbered outline has the shopper select Afterpay and enter details, the merchant include item information in the payment request, the existing integration handle the redirect, and the merchant capture the payment (raw lines 33–39). It does not specify result finality, capture timing, or all required fields; the linked child and API-only guides carry implementation detail.
- **Disputes:** The page says shoppers may initiate chargebacks directly with Afterpay up to 120 days after payment, cancellation or expected receipt. Once Afterpay opens a dispute, it gives the merchant 13 days to defend or accept; no response or acceptance loses the dispute and debits the account. If defended, Afterpay has 30 days for its decision (raw lines 41–45). These are the captured page's stated windows, not proof of the current terms for a particular account.
- **Integration routes:** This overview routes to Web, iOS, Android, React Native, Flutter, API only, and Pay by Link (raw lines 47–89). The platform labels are navigation; each route's own prerequisites and version scope must be checked.

## Detail locators

- Product scope, conditional risk/fraud statement and table qualifications: pinned raw lines 23–31.
- Numbered redirect/capture outline: `## How it works`, pinned raw lines 33–39.
- Dispute timing and result: `## Chargebacks`, pinned raw lines 41–45.
- Platform and API-only routes: `## How do you want to integrate?`, pinned raw lines 47–89.

## Related

- [[adyen-online-payments]] — online checkout context.
- [[adyen]] — provider.

## Raw Sources

- [[raw/adyen/docs/payment-methods/afterpaytouch/2026-09-15|Afterpay overview, captured 2026-09-15]]
