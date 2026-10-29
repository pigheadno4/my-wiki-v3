# Klarna Debit Risk Web Drop-in retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the captured Web Drop-in guide add to an existing integration, and what does it not establish?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-debit-risk-web-drop-in]] → [[raw/adyen/docs/payment-methods/klarna-debit-risk/web-drop-in/2026-09-15]]. The guide covers Sessions and Advanced Web Drop-in method additions (raw lines 15–54, 1066–1094), a separate SEPA-token recurring route (raw lines 58–1054, 1098–2094), and test/live gates (raw lines 1056–1064, 2096–2104). For product identity and settlement risk, follow [[source-adyen-docs-payment-methods-klarna-debit-risk]]: Debit Risk is distinct from Pay Now and an AUTHORISATION webhook does not guarantee settlement. These snapshots do not prove current eligibility or a successful live payment.

## Q2 — Central capability, prerequisites, and warnings

**Question:** What setup and token conditions govern Sessions versus Advanced Drop-in?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-debit-risk-web-drop-in]] → [[raw/adyen/docs/payment-methods/klarna-debit-risk/web-drop-in/2026-09-15]]. Sessions requires Checkout API v68+, existing Sessions Web Drop-in and redirect handling; Advanced requires its own base Web Drop-in/redirect setup; both need Customer Area addition and ordinary requests have no method-specific parameters (raw lines 25–42, 1066–1094). Recurring is through SEPA Direct Debit, with explicit-permission recommendation, token-creation fields and `recurring.token.created` webhook; token use is restricted in this guide to absent-shopper Subscription or UnscheduledCardOnFile (raw lines 58–87, 437–445, 1098–1127, 1477–1485). The table's Ecommerce/countryCode wording differs from ContAuth/omitted-country examples (raw lines 79–112 and 1119–1152). Test and live enablement are separate (raw lines 1056–1064, 2096–2104).
