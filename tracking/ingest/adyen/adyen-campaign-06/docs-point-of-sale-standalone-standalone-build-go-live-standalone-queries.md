# Fixed retrieval answers — docs-point-of-sale-standalone-standalone-build-go-live-standalone

## 1. Can a test standalone setup and test terminals be carried into live?

**Purpose and scope:** The pinned 2026-09-15 checklist describes a standalone terminal solution moving from test to live. It is a readiness route, not a record of live account approval or payment execution.

**Capability:** After live-account application and contract signing, configure the live account structure in the live Customer Area; the test structure is not copied. Request required live merchant accounts, with stores optional in this checklist after merchant-account confirmation. Test terminals cannot process live payments, so order live terminals. Test terminal settings do not copy either: configure standalone mode and payment/terminal features on the live fleet through Customer Area or Management API. Pre-assigning to a store is optional to ease later boarding.

**Prerequisites and warnings:** Provide payout bank-account information and set up reporting/reconciliation. Payout schedule changes and Reserve/auto-funding are described as optional or for consideration. Four- and two-business-day account/store estimates and a roughly four-business-day terminal arrival are dated guidance, not delivery commitments. These tasks do not establish an approved account or a successful live payment.

**Retrieval route:** [[source-adyen-docs-point-of-sale-standalone-standalone-build-go-live-standalone]] → `1. Set up your Adyen live account`, `2. Review your finance settings`, `3. Order live payment terminals`, and `4. Prepare your terminals` in [[raw/adyen/docs/point-of-sale/standalone/standalone-build/go-live-standalone/2026-09-15|pinned raw]]. Provider catalog route is pending coordinator promotion.

## 2. What happens after live standalone terminals arrive?

**Purpose and scope:** The checklist routes merchants to each terminal model's own manual for on-device preparation. It does not demonstrate that a terminal has actually been boarded or transacted.

**Capability:** For each received live terminal, the checklist calls for tamper inspection, receipt-paper insertion, power-on, network connection, boarding, and an Adyen-platform connectivity test. Live standalone settings and payment features must have been configured separately from test; optional prior store assignment may ease boarding.

**Prerequisites and warnings:** Model-specific steps and eligibility live in the linked manual and setup guide. A passed network diagnostic is only a point-in-time connection check. The checklist's statement that the merchant is then ready for a first live payment does not prove authorization, capture, settlement, reconciliation or payout.

**Retrieval route:** [[source-adyen-docs-point-of-sale-standalone-standalone-build-go-live-standalone]] → `4. Prepare your terminals` and `5. Get your terminals up and running` in [[raw/adyen/docs/point-of-sale/standalone/standalone-build/go-live-standalone/2026-09-15|pinned raw]]. Follow the model manual and [[source-adyen-docs-point-of-sale-standalone-standalone-build-set-up-standalone]] for their detailed setup conditions; provider catalog route is pending coordinator promotion.
