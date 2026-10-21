# docs-marketplaces-multi-pay-in-top-up-multi-pay-in retrieval probes

## Q1 — Why and how does a platform top up multi pay-in, and which account sends funds?

Answer: A pay-in partner's withholding or bank-cost offset can leave the multi pay-in account short of the amount intended for user allocation; the platform can fund it from its **liable balance account** (raw lines 17–19). The guide requires Transfers API credentials and transfer or transaction webhooks (lines 21–29). POST `/transfers` with `amount`, source `balanceAccountId` = liable account, `counterparty.balanceAccountId` = multi pay-in account, and `category: internal` (lines 31–44). This is an internal balance-account transfer, distinct from a pay-in partner's bank deposit or later allocation.

Route: [[index]] → [[adyen-index]] → [[adyen-multi-pay-in]] → [[source-adyen-docs-marketplaces-multi-pay-in-top-up-multi-pay-in]] → [[raw/adyen/docs/marketplaces/multi-pay-in/top-up-multi-pay-in/2026-09-15]].

## Q2 — What proves the top-up was booked, and what example mismatch must not be copied as fact?

Answer: The API example marks the request `authorised`, while non-authorised results can be refused for `notEnoughBalance` (raw lines 352–390). Transfer webhooks distinguish outgoing liable and incoming multi pay-in legs (lines 406–427, 713–722); later booked transfer and transaction events evidence the liable debit (lines 579–711) and multi pay-in credit (lines 870–1001). The TEST request asks for USD 2.40/`value: 240` (lines 46–70), but the illustrated API response says `amount.value: 10000` (lines 352–388), so those sample values cannot be treated as one reconciled transfer. The prose names `balancePlatform.transfer.updated` for authorised/booked changes, but the illustrated envelopes say `balancePlatform.transfer.created` (lines 500/573, 581/669, 793/864, 872/959); verify the event contract before relying on either type. No example proves live top-up, user allocation, or bank payout.

Route: [[index]] → [[adyen-index]] → [[adyen-multi-pay-in]] → [[source-adyen-docs-marketplaces-multi-pay-in-top-up-multi-pay-in]] → [[raw/adyen/docs/marketplaces/multi-pay-in/top-up-multi-pay-in/2026-09-15]].
