# docs-payment-methods-twint-api-only retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-twint-api-only]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 guide adds TWINT to an existing API-only integration, covering additional actions, CH/CHF discovery, capture, recurring tokens and TEST/LIVE setup (pinned raw lines 15–29, 44–51, 89–155, 391–399). It provides only a high-level shopper hosted-page/app sequence, not a concrete `/payments` response, return/details call or final payment webhook (lines 31–36, 85–87). It cannot prove merchant enablement, created token, captured funds or completed payment. Canonical source stem: `source-adyen-docs-payment-methods-twint-api-only`.

## Q2 — What are central prerequisites, limits and warnings?

The source requires existing API-only action handling for `redirect` or `sdk` and TWINT added in Customer Area (pinned raw lines 23–29). The sequence says shopper form details, but the dedicated form instruction says no shopper information needs collecting; discovery specifies CH/CHF (lines 31–51). `/payments` needs no extra TWINT-specific fields (lines 85–87). Automatic capture is described for Immediate or 1–7-day settings; Manual capture must precede seven-day authorization expiry, and a partial capture cancels the rest, with no multiple partial captures (lines 89–116). The capture prose says `modificationAmount` while its JSON example uses `amount` (lines 97–114). For recurring use, token creation uses `storePaymentMethod` and shopper reference; the token webhook supplies `storedPaymentMethodId`, and later ContAuth payments use Subscription or UnscheduledCardOnFile (lines 118–155). LIVE separately requires a request in the live Customer Area (lines 391–395). Canonical source stem: `source-adyen-docs-payment-methods-twint-api-only`.
