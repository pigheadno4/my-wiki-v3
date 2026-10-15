# Fixed retrieval checks: Classic API cancel

## Q1 — Eligible state and route choice

**Query:** When should an existing Classic integration use `/cancel`, a refund, `/cancelOrRefund`, or `/technicalCancel`, and should a new integration use Classic `/cancel`?

**Expected answer:** This inactive Classic endpoint is unsupported for new integrations; Adyen directs new builds to Checkout API and existing integrations to migration. `/cancel` releases reserved funds on an authorized, uncaptured payment. If it has already been captured, use a refund; if capture status is uncertain, use `/cancelOrRefund`. `/cancel` needs the original payment `pspReference`. If that PSP reference is unavailable, such as after a timeout, `/technicalCancel` is limited to within 24 hours after authorization and to payment requests with unique merchant references. The dated snapshot does not prove current endpoint availability or success for an individual cancellation.

**Raw locators:** inactive endpoint and migration, lines 15–24; cancel/refund/unknown-state selection, lines 30–39; technical-cancel conditions, lines 138–151. **Canonical retrieval route:** [[adyen-online-payments]] → [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel/2026-09-15|pinned raw]].

## Q2 — Reference identities and asynchronous outcome

**Query:** Which reference belongs in Classic `/cancel` versus `/technicalCancel`, what does the immediate response prove, and how is the final result reported?

**Expected answer:** `POST /cancel` sends `merchantAccount` and `originalReference` equal to the original payment's `pspReference`; optional `reference` identifies the new cancel modification. Its `[cancel-received]` response contains a different modification `pspReference` and only acknowledges receipt. A `CANCELLATION` webhook reports asynchronous `success`; `success: false` includes a reason. `/technicalCancel` instead sends `originalMerchantReference` equal to the original payment request's merchant `reference`, plus an optional new modification `reference`. Its `[technical-cancel-received]` response also has a distinct modification PSP reference, and `TECHNICAL_CANCEL` reports later success or failure. The Classic guide's `CANCELLATION` webhook field description links to a Checkout cancels response; do not equate the two endpoint shapes based on that link.

**Raw locators:** `/cancel` request and receipt, lines 41–67; `CANCELLATION` webhook, lines 69–82; technical-cancel request and receipt, lines 138–170; `TECHNICAL_CANCEL` webhook, lines 172–208. **Canonical retrieval route:** [[adyen-online-payments]] → [[source-adyen-docs-online-payments-classic-integrations-modify-payments-cancel]] → [[raw/adyen/docs/online-payments/classic-integrations/modify-payments/cancel/2026-09-15|pinned raw]].
