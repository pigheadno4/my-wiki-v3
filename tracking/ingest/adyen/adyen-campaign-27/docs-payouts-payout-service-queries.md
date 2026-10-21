# docs-payouts-payout-service retrieval probes

## Q1 — What does the Payout Service landing page say about payout funding and recipients?

Answer: It positions Adyen payouts alongside online or in-person payment processing, but a payout can also be **standalone** to a third-party beneficiary (raw lines 15–19). Funding can be Adyen-acquired payment funds or externally transferred funds (line 23). It links to third-party bank-account and Mastercard/Visa card payout paths, subject to each child guide's supported locations (lines 24–25, 37–43). This page provides orientation, not specific API or account setup.

Route: [[index]] → [[adyen-index]] → [[adyen-financial-products]] → [[source-adyen-docs-payouts-payout-service]] → [[raw/adyen/docs/payouts/payout-service/2026-09-15]].

## Q2 — Does this page establish a live payout method or completed beneficiary receipt, and is it the legacy Payout API?

Answer: No. It routes to getting started, checklist, bank and card child guides without request, country/currency, role, approval or status details (raw lines 27–43). The overview's destination claims are explicitly qualified by supported-location links (lines 24–25). It does not prove current enablement, a sent transfer or bank/card receipt. Its Payout Service route should be read separately from the existing legacy Online Payout API concept; this page itself supplies no bridge equating their mechanics (lines 15–43).

Route: [[index]] → [[adyen-index]] → [[adyen-financial-products]] → [[source-adyen-docs-payouts-payout-service]] → [[raw/adyen/docs/payouts/payout-service/2026-09-15]].
