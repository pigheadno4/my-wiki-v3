---
title: "Stripe Terminal: Collect Tips"
type: source
date_ingested: 2026-04-27
original_format: webpage
raw_files:
  - "stripe-terminal-collect-tips-2025.md"
tags: [stripe, stripe-terminal, tipping, in-person-payments, payment-intents]
---

## Summary

Overview of the two voluntary tip collection methods in Stripe Terminal, plus guidance on mandatory tips. Both methods use the PaymentIntents API and require manual capture.

## Key Takeaways

- **Two voluntary tip methods**:
  - **On-reader tipping** — reader displays suggested tip amounts to the customer before payment is collected; tip is automatically added by the reader and appears in `amount_details` on the PaymentIntent
  - **On-receipt tipping** — tip is added by the merchant at capture time via `amount_to_capture`; most commonly used with printed paper receipts
- **Mandatory tips** must be baked into the original `PaymentIntent` `amount`; on-receipt and on-reader methods cannot be used for mandatory tips
- **Can't mix methods**: once on-reader tipping is used on a `PaymentIntent`, on-receipt tipping cannot be applied to the same `PaymentIntent`

## On-reader vs On-receipt: Key Differences

| Dimension | On-reader | On-receipt |
| --- | --- | --- |
| Country availability | Wide (AU, CA, FR, DE, IE, NL, NZ, SG, GB for WisePad 3; many more for S700/S710 + WisePOS E) | US only |
| Supported readers | BBPOS WisePad 3, WisePOS E, Stripe Reader S700/S710 | Any reader |
| Merchant category | Any | Restricted |
| Card brands | Any | Visa, Mastercard, American Express, Discover |
| Customer experience | Tip prompt shown on reader screen | Tip set via POS integration or paper receipt |
| Credit card statement | Shows full amount immediately | Shows pending auth updated at settlement |

## API Behavior

| | On-reader | On-receipt |
| --- | --- | --- |
| How tip is submitted | Reader adds tip automatically during payment processing | Merchant passes `amount_to_capture` (inclusive of tip) at capture |
| Tip in API response | Returned in `amount_details` object on the PaymentIntent | Derivable from Charge: `amount` − `amount_authorized` |
| Charge object fields | `amount`, `amount_authorized`, `amount_captured` all equal (inclusive of tip) | `amount_authorized` = pre-tip; `amount` = `amount_captured` = inclusive of tip |

## See Also

- [[stripe-terminal-tipping]] — concept page for tipping in Stripe Terminal
- [[stripe-terminal]] — full Stripe Terminal concept page
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-terminal-collect-tips-2025]] — verbatim webpage content
