# docs-payment-methods-pad — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-pad]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-pad]] is the Canadian PAD method overview: shopper-authorized bank-account debit over ACSS, a CA/CAD capability table, merchant-held PAD agreement requirements, chargeback/notification risks and Web/API-only routes (raw lines 23–74). It is not an endpoint guide, a current Payments Canada legal opinion, proof of a merchant's Canadian account or PAD enablement, or evidence of submission, authorization, capture or settlement for a particular debit (full raw, lines 1–81). The raw is a 2026-09-15 snapshot (raw lines 2, 11).

## Q2 — What central capability, prerequisites, and warnings are stated?

[[source-adyen-docs-payment-methods-pad]] says PAD supports recurring and one-off debit but recommends against one-off due to chargebacks; the merchant must have a Canadian account at a Canadian financial institution (raw lines 23–27). Before either kind of PAD, the merchant must obtain and save a PAD agreement with the source-listed authorization, bank, schedule, rights, cancellation, processor and conditional waiver content; it points to Payments Canada Rule H1 for detail (raw lines 33–51). The historical CA/CAD matrix marks refunds and recurring available but captures unavailable (raw lines 29–31). PAD lacks real-time authorization; personal-account chargebacks can be initiated up to 90 days from initial debit, business up to 10 days; no PAD chargeback defense is available and retry depends on reason code (raw lines 53–60). The Notification of Change webhook requires subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` before the documented `eft.notificationOfChange` route applies (raw line 58).
