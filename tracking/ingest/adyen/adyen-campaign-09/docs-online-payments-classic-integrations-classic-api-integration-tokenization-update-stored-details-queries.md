# C09 fixed queries — docs-online-payments-classic-integrations-classic-api-integration-tokenization-update-stored-details

## Q1 — Purpose, scope, and inference boundary

**Query:** What does the Classic Update stored details page change, and is it a current Checkout API standalone card-update or a payment capture operation?

**Expected answer:** The page covers previously stored credit-card details in an inactive Classic API integration. It updates them only as part of a new recurring `/authorise` payment request that succeeds. It is not evidence for a standalone credential-update endpoint, modern Checkout API schema, capture, or settlement. The example shows an expiry update but does not make every example field universally required.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:16-33`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:35-59`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:476-494`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-tokenization]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-update-stored-details]]` → pinned raw.

## Q2 — Central capability, prerequisites, and warnings

**Query:** How does a Classic recurring authorization update a selected stored card, what happens to the recurring detail reference, and what identity or consent scope must remain qualified?

**Expected answer:** Send new card details with Classic `/authorise` and identify the stored detail using `selectedRecurringDetailReference`; the update occurs only after successful recurring authorization. The old `recurringDetailReference` then becomes invalid, a new one is created, and the new value is not returned in that authorization response; the page routes readers to retrieve-stored-details. The sample uses a merchant API key, shopper reference, `RECURRING` contract, `Subscription`, and `ContAuth`, but does not establish those sample values as universal or document consent collection. The broader tokenization concept carries shopper consent and reference scope.

**Evidence:** `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:23-33`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:37-59`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:94-121`, `raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/update-stored-details/2026-09-15.md:476-480`.

**Canonical retrieval route:** `[[adyen-index]]` → `[[adyen-tokenization]]` → `[[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-update-stored-details]]` → pinned raw.
