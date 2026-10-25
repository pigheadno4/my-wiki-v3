---
title: "FPX Online Banking Malaysia"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/2026-09-15.md"
tags: [adyen, online-payments, fpx, malaysia]
---

## Overview

Adyen's historical FPX Online Banking Malaysia overview describes an ecommerce payment method offered from PayNet through Razer Merchant Services (RMS, formerly MOLPay). It is a redirect method for Malaysia (MY) and MYR. The shopper completes the bank-side step in their bank's browser; the final result is asynchronous and requires webhooks to determine whether the payment succeeded.

## Key takeaways

- The capability matrix marks refunds, partial refunds and multiple partial refunds available. It marks recurring, separate/partial/multiple partial captures and chargebacks unavailable. These are snapshot capability labels, not proof that any individual payment or refund completed.
- The overview routes readers to Web, iOS, Android, React Native, Flutter, API-only and Pay by Link integration pages. These links are navigation; this page does not supply their implementation prerequisites, SDK/API versions or account-specific availability.
- A shopper's bank-page completion or return is not the final payment result. Use the asynchronous webhook result described here; this source does not document an actual authorization, capture, settlement or refund.

## Detail locators

- Provider identity and payment flow: pinned raw lines 23–25.
- Country/currency and capability matrix: pinned raw lines 27–29. The general Capture link at line 79 does not override the FPX-specific capture marks in this matrix.
- Integration directory and Pay by Link navigation: pinned raw lines 31–73.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Related raw API references

The overview links to these integration-specific pages; their contents are not evidence for this entry:

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/web/2026-09-15|FPX Web]]
- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios/2026-09-15|FPX iOS]]
- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/android/2026-09-15|FPX Android]]
- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/api-only/2026-09-15|FPX API only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/2026-09-15|FPX overview — captured 2026-09-15]]
