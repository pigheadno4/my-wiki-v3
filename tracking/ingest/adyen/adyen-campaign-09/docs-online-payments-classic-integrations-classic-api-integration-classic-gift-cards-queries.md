# Fixed retrieval checks: Classic gift-card payments

## Q1 — Purpose and scope

**Query:** What gift-card integration does the Adyen Classic page describe, and can it authorize a new integration or every stored-value operation?

**Expected answer:** It documents gift-card payments with Classic Payment API `/authorise` for an existing API-only integration. The endpoint is inactive and unsupported for new builds; new integrations are directed to Checkout API. The dated page names Givex, SVS, Fiserv/ValueLink and some local providers, but does not prove a merchant's current enablement or currency/card/provider eligibility. The guide routes issuing, separate balance checks and deactivation to the JSON-only Stored Value API. Do not extend this online Classic route to POS Terminal API gift-card operations.

**Raw locators:** `# Gift cards (classic)`, lines 15–33; `## Next steps`, lines 132–142. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-gift-cards]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-gift-cards/2026-09-15|pinned raw]].

## Q2 — Balance versus redemption and payment result

**Query:** What does a zero-value `/authorise` gift-card request return, and what distinguishes it from a payment request or successful authorization?

**Expected answer:** The documented `amount.value` of 0 returns `additionalData.currentBalanceValue`, the remaining balance. That balance response is not evidence of a nonzero redemption or successful payment. A payment request uses amount currency/value in minor units, gift-card number/expiry, merchant reference and selected brand; cardholder name and PIN/security code are optional in the page's field list. The response's `resultCode` reports the payment result, `pspReference` identifies it, and `authCode` is populated only when authorization succeeds. The sample `Authorised` response is illustrative, not guaranteed. Separate card management and balance-check operations are linked to Stored Value API.

**Raw locators:** `## Make a payment`, lines 35–57; request examples, lines 59–112; `#### Response`, lines 114–130; `## Next steps`, lines 132–142. **Canonical retrieval route:** [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-classic-gift-cards]] → [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/classic-gift-cards/2026-09-15|pinned raw]].
