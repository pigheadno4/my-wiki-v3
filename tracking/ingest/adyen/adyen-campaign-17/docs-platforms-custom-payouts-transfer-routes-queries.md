# Transfer routes — retrieval probes

## Q1 — Purpose and scope

**Query:** What does the Platforms custom-payout transfer-routes endpoint tell me, and does a returned route mean a payout has been sent or received?

**Expected answer:** The Configuration API POST /transferRoutes/calculate checks possible bank-payout routes before a separate funds transfer. It can calculate by destination country/region or specific counterparty and returns supported currency, priority and route-specific requirements; the counterparty response also lists country. The guide recommends this check because a recipient bank or regulator can restrict priorities or amounts. A response is no payout request or outcome, and does not prove current eligibility, booking or bank receipt. Keep this Platforms guide distinct from the legacy Payout API and from internal balance-account transfers.

**Raw locators:** lines 15-21 (purpose/recommendation); 32-48 (country method); 301-305 (route response); 359-372 (counterparty method); 716-721 (counterparty response); 782-785 (separate payout guides). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-custom-payouts-transfer-routes]] → [[raw/adyen/docs/platforms/custom-payouts/transfer-routes/2026-09-15]].

## Q2 — Conditions and examples

**Query:** What inputs and permissions are documented for calculating a counterparty payout route, and can I reuse the example amount limits for all recipients?

**Expected answer:** The captured page requires an Adyen for Platforms integration and Configuration API credential with Balance Platform BCL role. Counterparty mode documents balancePlatform, currency, category set to bank and counterparty; priorities is optional. A source balanceAccountId becomes required if counterparty contains transferInstrumentId. The sample response includes amount, address, bank-account identification and payment-instrument requirements, but its amounts and priorities belong to that illustrative request; each returned route's own requirements must be checked. The page does not establish an account's current capability or any payout cutoff, failure, return or retry outcome.

**Raw locators:** lines 23-30 (requirements); 359-372 (counterparty fields/condition); 716-780 (example route responses and requirements). **Canonical discovery route:** [[adyen-index]] → [[adyen-platforms]] → [[source-adyen-docs-platforms-custom-payouts-transfer-routes]] → [[raw/adyen/docs/platforms/custom-payouts/transfer-routes/2026-09-15]].
