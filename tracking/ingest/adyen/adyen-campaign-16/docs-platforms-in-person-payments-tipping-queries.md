# Fixed queries — docs-platforms-in-person-payments-tipping

## Q1 — purpose, scope, and non-inference

**Query:** What does this Adyen for Platforms tipping page route, and does its sample response prove a tip reached a user?

**Answer:** It describes adding a Tip split item to an in-person Terminal API payment request so the entire gratuity can be booked to one user's balance account; by default, the tip books to the platform liable account (raw lines 15–24, 40–53). It covers tipping proposed by a POS app or chosen at a terminal, not generic surcharge or later receipt-tipping allocation. The illustrated Success response is not evidence of a real authorization, captured funds, balance transfer, payout, legal seller or merchant-of-record status (lines 194–236, 396–438). Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-in-person-payments-tipping]] → [[raw/adyen/docs/platforms/in-person-payments/tipping/2026-09-15|pinned raw]].

## Q2 — central capability, prerequisites, and warnings

**Query:** What request fields and integration limits govern routing a POS-app or terminal-selected tip to the user balance account?

**Answer:** The page requires a Terminal API integration with payment terminals or a Mobile solution, plus linked general Platforms in-person requirements. Standalone cannot add per-authorization split instructions, and user-balance booking is unsupported for tipping on the receipt (raw lines 26–34). For either supported method, increment `split.nrOfItems`, set the Tip item's account to one user `balanceAccountID`, and exclude the tip amount from `split.totalAmount` and the Tip item amount field; it cannot be split among multiple balance accounts (lines 40–53, 242–255). A POS-app request supplies `TipAmount` with currency, original requested amount and formatted splits; terminal tipping adds `AskGratuity` and lets the shopper choose the tip. The response separates tip, original amount and total authorized amount, with minor-unit values in additional response fields (lines 149–206, 273–360, 396–408). The POS-app JSON request misses a comma and the terminal JSON request says three items while displaying four, so examples are not copy-ready (lines 182–187, 383–389). This page does not establish capture, partial-capture, refund, card-method or region behavior. Canonical route: [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-in-person-payments-tipping]] → [[raw/adyen/docs/platforms/in-person-payments/tipping/2026-09-15|pinned raw]].
