# Fixed retrieval checks — Adyen POS cashback and cashout

## 1. Purpose, scope, and eligibility

**Query:** What is the difference between cashback and cashout here, and who can use it?

**Answer:** The page calls cash handed to a shopper with a purchase “cashback” and cash without a purchase “cashout” (raw lines 17–21). It describes a Terminal API payment-terminal feature requiring Adyen Support enablement, with card and region limits (lines 23–31). The snapshot lists eftpos debit Australia, girocard debit Germany with a purchase only, Mastercard in specific European countries with purchase only and Support confirmation, and Visa in Europe with purchase only (lines 182–189). It gives no universal amount cap, terminal software floor, or proof of current merchant/card eligibility.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-cashback-and-cash-out]] → [[raw/adyen/docs/point-of-sale/cashback-and-cash-out/2026-09-15]] (catalog promotion pending).

## 2. Request amounts and cash handoff

**Query:** Which request amounts are sent, and when may staff hand over cash?

**Answer:** `PaymentTransaction.AmountsReq.RequestedAmount` is goods plus cash and `CashBackAmount` is the cash portion; the page's AUD example is 10 goods plus 2 cash, requesting 12 (raw lines 33–50, 54–83). On a `PaymentResponse.Response.Result` of `Success`, the issuer authorized both and staff pay the response `PaymentResult.AmountsResp.CashBackAmount` to the shopper. `Partial` authorizes the purchase but **not** cashback, so cash must not be handed over on that basis (lines 123–129). These response meanings do not establish later capture or settlement. The page gives no separate no-purchase request example.

**Route:** [[index]] → [[adyen-index]] → [[adyen-terminal-api]] → [[source-adyen-docs-point-of-sale-cashback-and-cash-out]] → [[raw/adyen/docs/point-of-sale/cashback-and-cash-out/2026-09-15]] (catalog promotion pending).
