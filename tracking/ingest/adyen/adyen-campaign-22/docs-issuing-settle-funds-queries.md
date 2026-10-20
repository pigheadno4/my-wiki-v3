# C22 Issuing settle-funds retrieval checks

## Q1 — How does this guide move acquired payment proceeds into a balance account?

For payments accepted through Adyen, the guide starts with pending funds in a store's merchant account; after the configured settlement delay (T+2 default), Adyen deducts fees, groups remaining funds into payable batches at the configured settlement frequency, and describes one internal transfer per batch to the balance account configured for that merchant account (raw lines 19–28). A Settlement Details Report can be generated for each batch (raw line 26). The route presupposes merchant accounts, a balance platform and the relevant merchant-to-balance-account configuration; it gives no separate eligibility or API setup procedure. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-settle-funds]] → [[raw/adyen/docs/issuing/settle-funds/2026-09-15]].

## Q2 — Which timing, currency and outcome limits matter?

T+2 is stated as the default configured delay, while batch frequency is configurable and may yield multiple payable batches a day (raw lines 23–25). The hotel example pays SEK 400 at Stockholm, deducts SEK 20 and gives a SEK 380 net batch/destination, but line 48 incorrectly calls its merchant-account amount EUR 400 (raw lines 39–68). This is an example currency conflict, not evidence of FX conversion. The page describes the intended internal-transfer route and sample amounts; it does not independently prove a specific batch booked, an external-bank payout or bank receipt. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-settle-funds]] → [[raw/adyen/docs/issuing/settle-funds/2026-09-15]].
