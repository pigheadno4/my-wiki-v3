---
title: "Adyen Atome payment-method overview"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome"
raw_files:
  - "adyen/docs/payment-methods/atome/2026-09-15.md"
tags: [adyen, atome, buy-now-pay-later, redirect, malaysia, singapore]
---

## Overview

This [[adyen|Adyen]] overview, fetched 2026-09-15 and marked last modified 2023-03-21, describes Atome as a three-installment buy now, pay later method in Malaysia and Singapore. Atome performs shopper risk checks before approval; the page says payments capture automatically after authorisation. See [[adyen-online-payments]]. This historical snapshot does not establish current merchant eligibility or a completed transaction.

## Key takeaways

- The shopper is redirected from a website or app to Atome. On desktop, the shopper can open the Atome app and scan a QR code; on mobile, the app path redirects automatically. Alternatively the shopper continues in browser and authenticates by phone number and OTP. Atome shows the installment breakdown, the shopper confirms, and the flow redirects back. The page says the first installment is charged during authorisation; return alone is not proof of payment success.
- The page explicitly excludes portable electronics such as phones, laptops and speakers because of high risk and instructs merchants to disable Atome for that item category in checkout business logic. This is a material product eligibility restriction in the captured guide.
- The capability matrix lists MY/MYR and SG/SGD redirect BNPL, refunds including partial and multiple partial refunds supported, and recurring, separate/partial/multiple partial captures and chargebacks unsupported. Capture is automatic after authorisation in the prose. The matrix is a captured method summary, not account-specific live proof.
- Transaction limits depend on country and card type: Malaysia MYR 10 minimum, MYR 1,500 debit-card maximum or MYR 5,000 credit-card maximum; Singapore SGD 1.50 minimum, SGD 1,000 debit maximum or SGD 3,000 credit maximum. Do not merge debit and credit caps.
- Integration routes include Web, iOS, Android, React Native, Flutter, API-only and Pay by Link. The API-only route is described as building your own UI for website or iOS/Android app. These links are navigation; method-specific request and return handling live in the child guides.

## Detail locators

- Three installments, risk checks, automatic capture and app/browser redirect journey: pinned raw lines 23–41. Portable-electronics restriction: line 43.
- Feature matrix and country/currency: lines 45–47. Country/card-type transaction limits: lines 49–56. Platform and API-only routes: lines 58–100.

## Related

- [[adyen-online-payments]] — provider integration concept

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/2026-09-15|Atome overview, fetched 2026-09-15]]
