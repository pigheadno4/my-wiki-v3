# C44 worker query check: Klarna Web Component

## Q1 — purpose, scope, and non-inference

**Query:** What does the Klarna Web Component page cover, and what does it establish?

**Answer:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-web-component]] routes to the 2026-09-15 guide for adding Klarna to an existing Web Components Sessions or Advanced integration. It covers widget or redirect checkout, not proof of present merchant eligibility, live payment success, or capture. Pinned full source: `raw/adyen/docs/payment-methods/klarna/web-component/2026-09-15.md`. Verified raw locators: introduction lines 15–25; Requirements 27–43; Test and go live 2268–2295.

## Q2 — central capability, prerequisites, and warnings

**Query:** How do its checkout and lifecycle paths work, and which conditions matter?

**Answer:** The component uses Klarna Pay Now, buy-now-pay-later, or Pay Over Time type, with widget enabled by `useKlarnaWidget: true` or redirect otherwise. Existing Web Components flow and Customer Area addition are prerequisites. Request line items must total `amount.value` with descriptions; country and billing country align. The parameter tables require locale to match country and currency, but both SE/SEK examples use `en_US`; reconcile against supported market rules before reuse without inferring a replacement from this page. Automatic capture is conditional on immediate delay and shipping within 24 hours; otherwise manual capture within 90 days. A received capture response is not final: use the CAPTURE webhook. Recurring tokens arrive after settlement only through the Recurring tokens life cycle events webhook that the server must be able to receive; the page links to Customer Area setup. The page mixes newer Checkout `/captures` with later legacy `/capture` examples, and the v6 widget configuration example is not wired into its mount snippet. Verified raw locators: API reference lines 53–74, 771–789 and example lines 85–90, 803–807; Component configuration 1512–1569; Capture 1571–1587 and 2033–2065; legacy shipping/partial capture 2068–2146; recurring 2154–2199, especially 2175.
