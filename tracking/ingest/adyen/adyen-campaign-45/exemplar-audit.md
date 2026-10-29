# Adyen C45 coordinator exemplar audit

**PASS** — 2026-10-29. Coordinator independently read all three immutable manifest samples end-to-end, then compared each promoted source with its complete raw and its Q1/Q2 retrieval answers. No material partial or failure in final audited entries; no campaign-wide expansion triggered. Raw unchanged.

| Fixed sample | Full raw read | Final source and retrieval assessment |
| --- | --- | --- |
| docs-payment-methods-afterpaytouch | All 96 lines | PASS. AU/CA/NZ country/currency scope, four installments, conditional fraud-risk claim, US/UK names, unexpanded recurring/refund notes, redirect/capture outline and 120/13/30-day dispute clocks preserved. Q1/Q2 qualify snapshot and account availability. |
| docs-payment-methods-afterpaytouch-android-component | All 1750 lines in contiguous untruncated ranges | PASS. Sessions v68+/Advanced prerequisites, required shopper/address/item data, InstantPaymentComponent and Compose module/key scope, no extra method config, redirect versus finality, manual partial captures, 13-day production and one-day test expiry, remainder cancellation exception and Support enablement preserved. US sandbox choices do not establish US live method support. Narrow Node/Go example qualifications remain at exact locators. Q1/Q2 expose these conditions. |
| docs-payment-methods-oney-web-component | All 1431 lines in contiguous untruncated ranges | PASS. Existing Sessions/Advanced setup, required line totals/shopper fields, trustFlag enablement and fee payer, installment/country mapping, hidden-field request obligation, capture before shipping and six-day expiry, cancel/refund split, EUR 1 minimum and 13-month limit, test/live boundary retained. French phone, C# countryCode and Italy scope differences are explicit. Q1/Q2 route to exact raw sections without current eligibility inference. |

The complete raw pages, not worker summaries, were the comparison authority. Initial review corrections were resolved before promotion. Exhaustive link, duplicate, hash and catalog/count checks remain separate campaign-close requirements.
