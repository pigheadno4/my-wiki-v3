# Q1 — purpose and money flow

**Query:** In Classic Adyen for Platforms, how are a shopper's payment and platform fee routed, and what happens without split instructions?

**Answer:** The page is for **Classic** integrations and routes new implementations to another guide (raw line 19). Its USD 400 illustration allocates USD 300 to the seller account holder's Classic account and USD 100 to the platform's liable account as commission (raw lines 21, 46–49). It supports API split instructions at payment, capture or refund, or store split configuration for automatic payment splits; without split instructions, payment and associated fees are booked to the liable account (raw lines 23, 29–44). Classic destinations use `accountCode` (raw line 41). Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-processing-payments]] → [[raw/adyen/docs/classic-platforms/processing-payments/2026-09-15]].

# Q2 — material failure and precedence

**Query:** Does a supplied seller split guarantee that seller receives funds, and which split is used for capture or a no-split refund?

**Answer:** No. Frontend validation does not check destination accounts; a nonexistent account or `Closed` holder routes the full transaction to the liable account and produces a `PAYMENT_FAILURE` notification (raw lines 75–81). Capture splits override payment splits, but partial captures require explicit splits or all funds go to liable; capture splitting also requires a method supporting separate captures (raw lines 140–148). A no-split refund uses the **authorization** split, not the capture split, under the page's listed conditions (raw lines 283–291); its following USD 5.99 no-split example conflicts with the prose's equal-to-authorized-amount condition after the USD 10 original example (raw lines 218–240, 287, 305–307). Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-processing-payments]] → [[raw/adyen/docs/classic-platforms/processing-payments/2026-09-15]].
