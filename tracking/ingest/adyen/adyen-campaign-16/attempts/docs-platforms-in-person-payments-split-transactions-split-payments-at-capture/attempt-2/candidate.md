---
title: "Adyen Platforms in-person split at capture"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/split-transactions/split-payments-at-capture"
raw_files:
  - "adyen/docs/platforms/in-person-payments/split-transactions/split-payments-at-capture/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, capture, split-transactions]
---

## Overview

This Adyen for Platforms in-person guide (last modified 2023-03-27; captured 2026-09-15) describes adding or overriding balance-account split instructions in a Checkout API capture request for a previously authorized Terminal API payment when split amounts are decided later. It is not an online-payment capture rule or evidence that a capture, balance booking or payout succeeded. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Prerequisites and support:** The page assumes the general Platforms in-person requirements and a Terminal API integration with terminals or mobile solution, or a standalone solution. Manual capture must be enabled or capture delay configured; CAPTURE and CAPTURE_FAILED events must be monitored. Capture-time splitting works only for payment methods supporting separate capture. Most in-person wallets do not, and Alipay/WeChat Pay capture immediately. Adyen recommends putting splits in the original payment request even if capture will change them, because methods without delayed capture need correct initial booking.
- **Capture instruction and precedence:** Take the authorization PSP reference from the payment-response transactionID, then POST /payments/{paymentPspReference}/captures with a splits array. Capture instructions can override earlier payment-request splits. If capture amount differs from authorization, the guide requires splits in the capture request; otherwise the full amount books to the platform liable balance account. This is distinct from the capture response's own PSP reference and its received status. CAPTURE webhook supplies the request outcome; received alone is not successful capture.
- **Split fields:** BalanceAccount books sale amount to a user's balanceAccountId; Commission goes to the liable balance account without an account field. Transaction-fee types can be directed to balance accounts; PaymentFee books all transaction fees, whose amount is not known at payment time. The table makes split amount.value generally required except fees, amount.currency conditional for currency conversion, and reference conditional for BalanceAccount. The USD 80 example allocates USD 76 user sale, USD 4 commission and fee deduction from a user account; it is illustrative, not a fee quote.
- **Unsupported types and source conflicts:** The limitations expressly exclude Surcharge and Tip split types at capture. A later general 'Additional split instructions' section links Surcharges, Chargebacks and Top-ups; that navigation does not override the capture-specific exclusion or establish capture support for those types. The test snippets conflict on currency (NodeJS JavaScript uses EUR amid USD examples). The fee transfer names a second user balance account while the fee transaction.created sample names the first; the commission prose and transfer describe an incoming liable-account credit, but its captured transfer changes liable-account ID and its transaction.created sample shows -400 on a user balance account. Do not infer an actual booked sign or balance account from these examples; check the current endpoint schema and observed transaction records.
- **Booking check:** The capture API validates split format, not the named balance accounts. A nonexistent balance account or one linked to a closed account holder causes the full transaction and fees to book to the liable balance account even if the transaction is successful; the page points to internal transfer as a correction route. Track CAPTURE/CAPTURE_FAILED and per-split Transfer/Transaction webhooks: payment PSP and modification PSP references differ; received, authorised, captured and booked refer to separate stages. The example webhooks are test data, not proof of real booking or bank receipt.

## Detail locators

- Delayed split rationale, override, manual/delayed capture and method/type limits: pinned raw lines 19-48.
- Capture reference, splits fields, conditional amount/currency/reference and USD fee example: pinned raw lines 50-110.
- Dated test SDK examples and internally inconsistent currency: pinned raw lines 111-587.
- Capture received response versus CAPTURE outcome, split-account validation and liable fallback: pinned raw lines 590-660.
- Illustrative per-split payment/fee/commission transfer and transaction statuses: pinned raw lines 663-1635; additional-type navigation/conflict: lines 1636-1655.

## Related

- [[adyen-platforms]] — platform split-processing concept and reciprocal source route.
- [[source-adyen-docs-platforms-process-payments]] — broad platform channel/split overview.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/split-transactions/split-payments-at-capture/2026-09-15|Adyen Split payments at capture, captured 2026-09-15]]
