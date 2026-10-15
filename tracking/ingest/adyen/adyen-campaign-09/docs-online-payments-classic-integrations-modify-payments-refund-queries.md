# C09 fixed queries — docs-online-payments-classic-integrations-modify-payments-refund

## Q1 — Purpose, scope, and inference boundary

**Query:** When is the Classic refund guide applicable, and can it be treated as the current Checkout API refund schema or a way to refund an uncaptured payment?

**Expected answer:** This is a captured-payment refund guide for inactive Classic Payment API endpoints. New integrations are directed to Checkout API, and existing integrations to migration through Adyen. An uncaptured payment is to be cancelled under this guide. Its Classic request fields and examples do not establish the modern Checkout API contract or current account eligibility.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:19-24`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:30-43`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-refunds]]` → `[[source-adyen-docs-online-payments-classic-integrations-modify-payments-refund]]` → pinned raw.

## Q2 — Central capability, prerequisites, and outcome warning

**Query:** What references, amount, permissions, and events matter for Classic referenced versus unreferenced refunds, and does an accepted refund response or `REFUND success: true` prove the shopper received funds?

**Expected answer:** Referenced `/refund` uses the original payment PSP reference as `originalReference`, with merchant account and amount no greater than the captured amount; its response carries a different refund-request PSP reference. Supported partial refunds may be multiple within the captured total. An unreferenced `/refundWithData` is limited by default and needs Adyen Support enablement; raw-card input has a PCI Level 1 or 2 condition. Outcomes arrive asynchronously by `REFUND` or `REFUND_WITH_DATA` webhook. A successful validation or `REFUND success: true` can still precede a scheme rejection (`REFUND_FAILED`) or a reversal (`REFUNDED_REVERSED`). Neither request receipt nor success flag alone proves final funds delivery.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:38-81`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:133-141`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:171-191`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:227-239`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:277-279`, `raw/adyen/docs/online-payments/classic-integrations/modify-payments/refund/2026-09-15.md:349-365`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-refunds]]` → `[[source-adyen-docs-online-payments-classic-integrations-modify-payments-refund]]` → pinned raw.
