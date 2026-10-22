# C28 Payout Service card-detail retrieval checks

## Q1 — Purpose and prerequisites

**Query:** How does a Payout Service integrator prepare a third-party card for a card payout, and what determines raw versus encrypted input?

**Answer:** The page describes collecting recipient-card details, enabling additional Checkout response data, probing payout eligibility with a zero-value `POST /payments`, and tokenizing the card for non-fully-PCI or recurring-payout paths before a later separate Transfers API payout request (raw lines 19–29, 45–78, 849–874, 1911–1915). A Payout Service integration, Checkout roles, webhook receiver and Adyen feature enablement are listed; only a fully PCI-compliant integration may submit raw card data, otherwise it must collect/encrypt through the Card Component (raw lines 19–43). Route: [[index]] → [[adyen-index]] → [[adyen-card-payouts]] → [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-manage-card-details]] → [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/manage-card-details/2026-09-15]].

## Q2 — Eligibility, token and payout boundary

**Query:** Does an Authorised zero-auth response or token prove that a card payout was sent, and how are eligibility fields interpreted?

**Answer:** No. The zero-auth response's `payoutEligible` values are scheme-specific: `Y` eligible, `D` Mastercard domestic-only (Visa N/A), `N`/`U` ineligible; `fundsAvailability` appears only for `Y`/`D`, with `I` meaning Visa fast-funds support but Mastercard prepaid/debit product type (raw lines 793–847). A token is created after successful payment authorization, and its ID comes from the additional-data response when enabled or a token-created webhook; pair it with the shopper reference for the later request (raw lines 1845–1909). This page ends by routing to a separate card payout request and contains no disbursement or recipient-credit outcome (raw lines 1911–1915). Route: [[index]] → [[adyen-index]] → [[adyen-card-payouts]] → [[source-adyen-docs-payouts-payout-service-pay-out-to-cards-manage-card-details]] → [[raw/adyen/docs/payouts/payout-service/pay-out-to-cards/manage-card-details/2026-09-15]].
