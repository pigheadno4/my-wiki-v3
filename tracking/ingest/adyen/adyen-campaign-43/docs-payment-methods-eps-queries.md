# Fixed-query evidence — EPS overview

Canonical source stem: `source-adyen-docs-payment-methods-eps`
Pinned raw: `raw/adyen/docs/payment-methods/eps/2026-09-15.md`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-eps]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 overview identifies EPS as Austrian online banking operated by Stuzza and sketches bank selection, bank-site redirect/confirmation and return to the merchant website (pinned raw lines 15–31). It does not give implementation fields, action/webhook states, guarantee terms or settlement timing; redirect return alone does not establish payment success. The historical table and route links do not prove current bank coverage or merchant eligibility (pinned raw lines 33–73).

## Q2 — Central capability, prerequisites, and warnings

The capability table labels EPS Online Banking/redirect for AT/EUR, marks refunds and partial/multiple partial refunds available, capture variants and chargebacks unavailable, and recurring with a checkmark plus “See note.” No corresponding note appears in this capture, so recurring conditions must be verified in a child guide (pinned raw lines 33–35). The page routes to pre-built Web, iOS, Android, React Native and Flutter guides, and an API-only UI route for website/iOS/Android, but sets no API/SDK version, request-field or go-live requirement itself (pinned raw lines 37–73).
