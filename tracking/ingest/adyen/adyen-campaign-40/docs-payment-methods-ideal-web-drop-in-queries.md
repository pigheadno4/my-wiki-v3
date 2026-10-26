# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ideal-web-drop-in.md` → pinned raw.

The 2026-09-15 source adds iDEAL | Wero to an **existing Web Drop-in** integration through separate Sessions and Advanced branches; it is not the complete base integration (raw `adyen/docs/payment-methods/ideal/web-drop-in/2026-09-15.md:15-25,330-340`). Checkout API v68+ is listed for Sessions, not in the Advanced requirements table (raw lines 33-36, 336-340). It does not establish current method enablement, live eligibility or an executed payment. Its Advanced base-guide link has an unresolved encoded platform template (raw line 338), so the linked URL should not be treated as a confirmed resolved route.

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-ideal-web-drop-in.md`. Recurring retrieval can also pass through `wiki/concepts/adyen-tokenization.md`.

Both branches require redirect handling and Customer Area method setup; ordinary `/sessions` and `/payments` calls need no iDEAL-specific additions. Individual `Redirect` import is optional for tree shaking (raw `adyen/docs/payment-methods/ideal/web-drop-in/2026-09-15.md:29-54,334-358`). Recurring iDEAL | Wero uses SEPA Direct Debit standard tokenization fields, the `recurring.token.created` webhook's `storedPaymentMethodId`, and shopper-absent `UnscheduledCardOnFile` or `Subscription` reuse (raw lines 56-83,360-387). The Java recurring examples omit `shopperReference` present in curl and other examples; avoid treating a sample as a full field contract (raw lines 92-136,395-440). `Received` is an intermediate response; use webhooks to track success (raw lines 283-288,587-592). TEST is unreliable and the page recommends live penny testing; TEST simulations are conditional, with expiration yielding `Pending` or `Received` (raw lines 292-328,596-632).
