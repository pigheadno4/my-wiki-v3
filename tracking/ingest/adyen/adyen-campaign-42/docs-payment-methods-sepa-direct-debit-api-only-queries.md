# Fixed-query evidence — SEPA Direct Debit API-only

Canonical source stem: `source-adyen-docs-payment-methods-sepa-direct-debit-api-only`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-sepa-direct-debit-api-only]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 page adds SEPA Direct Debit to an **existing Web API-only Advanced-flow** integration and covers merchant form, method discovery, payment, capture, recurring and test/live steps (raw lines 15–36, 38–53, 92–153, 1196–1212). It does not supply the full base integration or prove current merchant/bank eligibility, a valid mandate, or funded payment. Its “successful payment” example has `resultCode: Received`, so final authorization, capture and settlement cannot be inferred (raw lines 128–147). The method overview carries wider mandate, pre-debit and chargeback obligations.

## Q2 — Central capability, prerequisites, and warnings

An existing API-only integration must handle the `direct` action and have SEPA enabled in Customer Area (raw lines 23–29). `/paymentMethods` uses the listed country codes and EUR, with test v72 examples only (raw lines 51–90). The merchant-built form table asks for owner name and IBAN, despite adjacent “issuer selection” wording; a high-level purchased-item instruction also diverges from the dedicated SEPA request fields (raw lines 31–49, 92–125). `/payments` requires SEPA owner name and **unencrypted** IBAN; billing address is conditional on the enumerated non-EEA SEPA IBAN origins (raw lines 92–102). If automatic capture is off, delayed or manual capture is required, and multiple partial captures need Support enablement (raw lines 138–147). The page strongly recommends recurring consent transparency and documents `recurring.token.created` followed by shopper-absent Subscription/UnscheduledCardOnFile token payments (raw lines 149–157, 506–536, 853–879). Live acceptance requires a live Customer Area request (raw lines 1196–1208).
