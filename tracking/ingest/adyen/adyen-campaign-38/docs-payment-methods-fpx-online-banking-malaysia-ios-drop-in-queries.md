# docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in retrieval queries

Canonical source: [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in]] (`wiki/sources/adyen/source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in.md`).
Forward route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in]] → [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/ios-drop-in/2026-09-15|pinned raw]].

## Q1 — What is the purpose and scope, and what cannot be inferred?

This 2026-09-15 page is an FPX Online Banking Malaysia add-on for existing iOS Drop-in Sessions and Advanced integrations (raw lines 15–25, 58–68). It does not itself enumerate issuer IDs, document the bank return/webhook sequence, prove merchant eligibility, or show authorization, capture or settlement; TEST guidance and a redirect prerequisite are not observed transaction outcomes (raw lines 48–56, 64–90). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in]] → pinned raw above.

## Q2 — What central capability, prerequisites and warnings matter?

Sessions requires iOS Drop-in, Checkout API v68+ and Customer Area method setup, with no extra `/sessions` or FPX configuration parameters stated (raw lines 25–46). Advanced requires existing iOS Drop-in, redirect-action handling and Customer Area setup, with no extra FPX configuration or `/payments` parameters; it states no Advanced API minimum (raw lines 58–80). For TEST, the page points to issuer IDs available to the Online Banking Malaysia Component for the relevant country/region and TEST Customer Area status; it does not list those IDs. A separate live Customer Area request is required before accepting live payments (raw lines 48–56, 82–90). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia-ios-drop-in]] → pinned raw above.
