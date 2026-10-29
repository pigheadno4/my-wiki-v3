# Scalapay retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the captured Adyen Scalapay overview establish, and what does it leave to other evidence?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay]] → [[raw/adyen/docs/payment-methods/scalapay/2026-09-15]]. The overview identifies a European BNPL instalment method (raw line 19), gives a snapshot table for Redirect, FR/IT/PT/ES and EUR (raw lines 21–23), and links to integration choices (raw lines 25–49). It does not prove current merchant or shopper eligibility, payment authorization, capture or settlement, or the child guides' detailed flow.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which integration choices and transaction features appear, and what conditions must a reader preserve?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-scalapay]] → [[raw/adyen/docs/payment-methods/scalapay/2026-09-15]]. The table marks refunds and partial/multiple refunds, separate and partial/multiple partial captures, while recurring and chargebacks have x marks (raw lines 21–23). Web, iOS and Android lead to prebuilt UI guides, while API-only is for a merchant-built UI (raw lines 25–49). The overview itself does not state concrete request fields, shopper approval criteria, redirect return/expiry, outcome verification, or capture/refund operational rules; follow its child guides before implementation.
