# C09 fixed queries — docs-online-payments-classic-integrations

## Q1 — Purpose, scope, and inference boundary

**Query:** What is Adyen's Classic Ecommerce integrations page for, and does it support selecting Classic API for a new online-payment integration?

**Expected answer:** It is a navigation page for inactive Classic integrations. The captured page says its endpoint is no longer supported for new integrations, directs new builds to online payments with Checkout API, and directs existing integrations to contact Adyen and migrate. Do not infer Classic API and modern Checkout API have equivalent flows or that this snapshot proves present eligibility or execution.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/2026-09-15.md:14-23`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-online-payments-classic-integrations]]` → pinned raw.

## Q2 — Central capability, prerequisites, warnings

**Query:** Which guide routes does the inactive Classic integrations page expose, and what lifecycle warning must a reader see before following them?

**Expected answer:** It links to Classic API integration for accepting payments and Modify payments for capture, cancellation, refunds, and changing an amount. The page warns that this endpoint is inactive and unsupported for new integrations; new builds should use Checkout API, while existing users should contact Adyen and migrate. The page itself does not specify modification prerequisites, detailed semantics, or operation outcomes.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/2026-09-15.md:16-31`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-online-payments-classic-integrations]]` → pinned raw.
