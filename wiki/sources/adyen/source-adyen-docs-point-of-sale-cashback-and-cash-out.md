---
title: "Adyen Docs: POS cashback and cashout"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/cashback-and-cash-out"
raw_files:
  - "adyen/docs/point-of-sale/cashback-and-cash-out/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, cashback, cashout]
---

## Overview

Adyen's “Cashback” guide, fetched 2026-09-15 with raw metadata last modified 2023-08-10, covers a shopper receiving cash in hand from their account **with a purchase** or **without a purchase** (“cashout”). It explains a Terminal API payment request and how the merchant reads its response. This is a card-funded POS cash disbursement attached to a payment request, not an online refund, payout API, or claim that every card/account/region supports cashout. [[adyen]] · [[adyen-terminal-api]]

## Key takeaways

- The page requires a Terminal API integration with payment terminals and Adyen Support enablement before cashback. Card and country/region support is limited. It states no terminal-software floor, exact cash-amount limit, or current merchant eligibility, so the example cannot supply those missing conditions.
- The POS determines the cash amount and the amount due for goods, then sends `PaymentTransaction.AmountsReq.RequestedAmount` as **purchase plus cash** and `CashBackAmount` as the cash portion. For no-purchase cashout, the definition has no goods amount, but the page does not provide a separate cashout request example or alternate API action. The AUD example of 10 goods plus 2 cash yields `RequestedAmount=12` and `CashBackAmount=2`; it illustrates the arithmetic rather than a universal limit.
- On a `PaymentResponse.Response.Result` of **Success**, the issuer authorized both payment and cash portion; the merchant pays out the `PaymentResult.AmountsResp.CashBackAmount` reported in the response to the shopper in cash. **Partial** means the issuer authorized the payment but **not** cashback, so it must not be treated as authorization to hand over the requested cash. This is an issuer-authorization interpretation, not proof of later capture, settlement, or cash drawer reconciliation.
- The dated support list names **eftpos debit** in Australia; **girocard debit** in Germany **with a purchase only**; **Mastercard** in specific European countries/regions **with a purchase only** and Support confirmation of countries; and **Visa** in Europe **with a purchase only**. The page does not establish that every card in these brands, European country, or merchant account is eligible.

## Detail locators

- **Definition and prerequisites:** raw lines 17–31. The cashout term means no purchase; Support enablement and card/region limits remain separate gates.
- **Amounts in Terminal API request:** “Issue a cashback,” lines 33–50. Use the response-specific `CashBackAmount` for cash handling; the example request at lines 54–121 uses `ProtocolVersion=3.0`, a test-style AUD purchase/cash amount, and sample IDs. It does not pin an SDK release or prove a live transaction.
- **Authorization outcome:** lines 123–129 and response example lines 130–180. `Success` versus `Partial` changes whether cash is authorized. The example's `PaymentBrand=eftpos_australia_sav`, `AuthorizedAmount=12`, `CashBackAmount=2`, and `cashBackAmountValue=200` are illustrative response values.
- **Card and region matrix:** “Supported cards and countries/regions,” lines 182–189. Preserve the purchase-only restrictions and Mastercard's narrower country condition; verify current support and account enablement before offering the flow.

## Related

- [[adyen-terminal-api]] — POS payment request and response route
- [[source-adyen-docs-point-of-sale-capturing-payments]] — separate capture lifecycle guidance

## Related raw API references

Linked Terminal API payment, Support, POS capture, and payment-method pages were not read for this entry and serve as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/cashback-and-cash-out/2026-09-15|Adyen Cashback and cashout guide, fetched 2026-09-15]]
