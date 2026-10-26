# docs-payment-methods-twint retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-twint]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 Adyen TWINT overview describes a Swiss mobile payment method, online shopper handoff paths, a CH/CHF capability table and platform guide routes (pinned raw lines 15–36, 38–80). It does not specify Checkout response/return/webhook behavior, account-specific enablement or a completed payment. The capture-dependent transfer sentence cannot by itself prove authorization, capture or settlement for a particular transaction (line 32). Canonical source stem: `source-adyen-docs-payment-methods-twint`.

## Q2 — What is the central capability and what conditions or warnings matter?

For online mobile checkout, the source describes TWINT app opening or webpage/short-code handoff; desktop checkout uses a TWINT webpage offering QR scan or short-code entry (pinned raw lines 23–28). In-store QR scanning is a separate terminal flow (line 30). The page says funds transfer is in real time **after capture** (line 32). Its CH/CHF redirect-wallet table marks recurring/refund/capture/chargeback capabilities but marks multiple partial captures unsupported; it does not state account eligibility or detailed conditions for the marks (lines 34–36). Web, iOS, Android, Flutter, API-only, Pay by Link and POS links lead to separate implementation authorities (lines 38–80). Canonical source stem: `source-adyen-docs-payment-methods-twint`.
