# Fixed retrieval checks — Adyen reports and the payments lifecycle

## Q1 — Purpose, scope, and non-inference

**Question:** What does this page map, and what does finding a status in a report not prove?

**Expected answer:** It maps named payment-lifecycle statuses to Payment accounting, Settlement details, and Dispute transaction details reports. It is report-navigation and status-context guidance, not a transaction-specific result or full report schema. An accounting status entry such as `Received` or `Authorised` must not be read as settlement. A listed `Settled` status is described as captured funds released to merchant payable, which does not by itself prove bank deposit or final financial outcome for a specific payment.

**Raw locators:** `Payment statuses and corresponding reports`, lines 19–48, especially 21, 26–29, 38–43.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-reports-and-the-payments-lifecycle]] (the reporting concept is a C12 coordinator-created route).

## Q2 — Central capability, qualifications, and warnings

**Question:** Which report families carry which kinds of statuses, and what source wording requires caution?

**Expected answer:** The Payment accounting list contains `Received`, `Authorised`, `Settled/Refunded`, error/refusal and modification/cancellation/expiry-related labels (raw lines 26–36). Settlement details lists `Settled`, `Chargeback`, `Refunded`, and `ChargebackReversed` (38–43). Dispute transaction details lists `Notification of Chargeback` as pending and `Request for information` (45–48). The snapshot's `Settled/Refunded` gloss says “Payment attempt with validated details”; keep that odd text attributed to this page rather than treating it as a full settlement/refund definition. Webhook mentions apply to selected statuses only. The embedded chart is referenced, but its SVG contents are not exposed in this text snapshot; report grain, fields, timing and reconciliation require the linked report-specific sources.

**Raw locators:** Payment accounting lines 26–36, especially 30; Settlement details lines 38–43; Dispute transaction details lines 45–48; chart reference line 23; `See also` lines 50–54.

**Canonical wiki route:** [[adyen-index]] → [[adyen-reporting]] → [[source-adyen-docs-reporting-reports-and-the-payments-lifecycle]] → [[raw/adyen/docs/reporting/reports-and-the-payments-lifecycle/2026-09-15|pinned raw snapshot]].
