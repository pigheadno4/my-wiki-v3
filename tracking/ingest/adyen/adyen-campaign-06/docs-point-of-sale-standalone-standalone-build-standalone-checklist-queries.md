# Fixed retrieval checks — standalone integration checklist

## Query 1: What steps does Adyen's standalone checklist put before a first test payment?

**Purpose and scope:** This is a 2026-09-15 capture of a standalone terminal test-environment checklist, not a record of an executed payment. The route starts payments on the terminal without a merchant POS app.

**Capability and prerequisites:** Create a test account and choose company/merchant/store structure, requesting stores only if needed after merchant-account creation. Order a test card and printer-equipped test terminals; configure standalone mode and required features in Customer Area or through API. Store pre-assignment is optional. When the test terminal arrives, follow its model manual to inspect for tampering, load receipt paper, connect/network/board it and test the Adyen-platform connection. The checklist then directs test transactions and test Customer Area/reconciliation checks.

**Warnings and do not infer:** The listed four-business-day delivery minimum is a dated estimate, not a live promise. The checklist's manual-card-entry, cancel and refund exercises do not establish that MKE/MOTO, tipping, refunds or other variants are enabled for every account/device; follow the linked setup and standalone-use guides for their feature and passcode gates. Boarding or a connection check is not proof of payment authorization, refund completion or settlement.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-standalone-terminals]] → [[source-adyen-docs-point-of-sale-standalone-standalone-build-standalone-checklist]] → `[[raw/adyen/docs/point-of-sale/standalone/standalone-build/standalone-checklist/2026-09-15]]`, raw lines 27–143. The C06 source/index route awaits coordinator promotion.

## Query 2: Does passing the standalone test checklist make the merchant live?

**Purpose and scope:** The checklist separates building/testing a standalone solution in a test environment from applying to operate it live.

**Capability and prerequisites:** It calls for test transactions including test-card payment, manual test-card entry, cancellation and refund; lookup in the test Customer Area; and reconciliation with Settlement details reporting. After testing, the page says to apply for a live account and sign the contract before taking the standalone solution live. It also says account structure must be set up again for live. The linked standalone setup guide describes separate live-terminal preparation.

**Warnings and do not infer:** This snapshot does not show that the merchant actually executed or passed tests, has a live account, signed a contract, configured live terminals, enabled MOTO/MKE/tipping/refunds, or completed a live payment. A test Customer Area result and reporting exercise are not live or provider-outcome proof. The source metadata was last modified in 2020; current onboarding and eligibility must be checked against current provider guidance.

**Retrieval route:** [[index]] → [[adyen-index]] → [[adyen-standalone-terminals]] → [[source-adyen-docs-point-of-sale-standalone-standalone-build-standalone-checklist]] → raw lines 23–31, 108–151, especially `## Going live`. Follow [[source-adyen-docs-point-of-sale-standalone-standalone-build-set-up-standalone]] for configuration details and [[source-adyen-docs-point-of-sale-standalone-standalone-use]] for payment operation conditions.
