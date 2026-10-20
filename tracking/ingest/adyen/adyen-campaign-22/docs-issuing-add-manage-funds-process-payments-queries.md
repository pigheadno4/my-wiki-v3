# C22 worker retrieval checks — docs-issuing-add-manage-funds-process-payments

## Q1: Who receives acquired payments and how can they fund issued cards?

This page is for **Enterprise Issuing**; Embedded Issuing has separate marketplace/platform guides (raw lines 19–21). Customers pay the business; payments arrive pending in its merchant account, become available after the configured settlement delay (T+2 default in the snapshot), have fees deducted, and are grouped into net settlement batches booked to the balance account configured for that merchant account (lines 23–30). Funds in balance accounts can then fund issued cards or pay out to a verified external-bank transfer instrument (line 30). Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-add-manage-funds-process-payments]] → [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15]].

## Q2: What can the webhooks/report prove, and is the hotel example internally consistent?

Each settlement batch is one transfer; `transfer.created` says incoming transfer **initiated** and `transfer.updated` reports status changes (raw lines 74–81). The Balance Platform Accounting Report is **batch-level**, so it cannot reconcile single acquired transactions (lines 83–87). The hotel example says Stockholm's guest paid SEK 400 (line 47), then labels the HotelChain_SEK pending amount EUR 400 (line 52), but later uses SEK 20 fees and SEK 380 net (lines 61–72); the EUR label is unresolved and does not establish FX behavior. Forward route: [[index]] → [[adyen-index]] → [[adyen-issuing]] → [[source-adyen-docs-issuing-add-manage-funds-process-payments]] → [[raw/adyen/docs/issuing/add-manage-funds/process-payments/2026-09-15]].
