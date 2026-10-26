# docs-payment-methods-twint-web-drop-in — Q1/Q2

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-twint-web-drop-in]].

## Q1 — What is this page for, and what cannot be inferred?

[[source-adyen-docs-payment-methods-twint-web-drop-in]] is a TWINT add-on for existing Web Drop-in, with separate Sessions and Advanced flow sections: requirements/redirect, ordinary requests, optional import, recurring token operations, live setup and capture rules (raw lines 17–250). It does not itself establish a specific merchant's enablement, a completed redirect/payment, final settlement, or a shopper-consent procedure (full raw, lines 1–250). Checkout API v68+ is stated in the Sessions requirements, not in the Advanced requirements (raw lines 29–36, 109–115). The CHF partial-capture payload is an example rather than country/currency eligibility proof (raw lines 190–209).

## Q2 — What central capability, prerequisites, and warnings are stated?

[[source-adyen-docs-payment-methods-twint-web-drop-in]] requires existing Sessions or Advanced Web Drop-in, TWINT added in Customer Area and redirect handling; Sessions explicitly requires Checkout API v68+ (raw lines 25–36, 105–115). Ordinary `/sessions` and `/payments` calls need no extra TWINT parameters, and individual `Twint` import is optional for tree shaking (raw lines 40–54, 119–133). For stored-method payments, the guide separately lists `storePaymentMethod: true`, a three-character-minimum shopper reference, a `recurring.token.created` webhook, and later `ContAuth` with `Subscription` or `UnscheduledCardOnFile` (raw lines 56–95, 135–174). It requires a live Customer Area request (raw lines 99–103, 178–182). Under Manual capture, authorization expires after seven days; one partial capture is supported, multiple partial captures are not, and the unclaimed remainder is cancelled (raw lines 184–211). The partial-capture prose says `modificationAmount`, but its example shows `amount` and labels the request `/capture`; the source does not resolve that mismatch (raw lines 190–209).
