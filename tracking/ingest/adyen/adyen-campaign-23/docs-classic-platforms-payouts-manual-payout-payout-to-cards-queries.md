# C23 worker queries — Classic manual payout to cards

Route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-payouts-manual-payout-payout-to-cards]] → [[raw/adyen/docs/classic-platforms/payouts/manual-payout/payout-to-cards/2026-09-15]].

## Q1. How does a Classic platform set up and submit an eligible card payout?

This Classic Fund API v5+ route is for eligible Mastercard/Visa debit cards and needs Support enablement (raw lines 19–27). The platform sends a zero-value `/payments` request with `enablePayOut: true`, merchant account, card details and account-holder `shopperReference`, then checks `payoutEligible` (raw lines 29–88). Raw card data is restricted to a fully PCI-compliant platform; otherwise use the Card Component (raw line 38). For an eligible card, use its tokenized `recurring.recurringDetailReference` in `/updateAccountHolder` to add the payout method, wait for `ACCOUNT_HOLDER_UPDATED`, then submit `/payoutAccountHolder` with the resulting `payoutMethodCode` plus account/account-holder codes, amount and reference (raw lines 88–174).

## Q2. What eligibility and outcome boundaries prevent overclaiming?

`Y` means eligible, `D` is Mastercard domestic-only, and `N`/`U` cannot be used for payouts (raw lines 81–86). Step 2's HTTP 200/202 response still requires `ACCOUNT_HOLDER_UPDATED` before treating the payout method as added (raw lines 137–140). The payout example returns `Received`, and the guide requires `ACCOUNT_HOLDER_PAYOUT` for status; neither proves card credit (raw lines 162–174). A 30-minute arrival statement is dated product guidance (raw line 23). The prose says the recurring detail reference is needed for later payouts, while Step 3 uses payoutMethodCode; the sample also changes the recurring reference value (raw lines 88, 105–106, 125–129, 142–160).
