# Klarna raw response retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What do the captured Klarna raw acquirer response rows tell an operator?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-raw-responses]] → [[raw/adyen/docs/payment-methods/klarna/raw-responses/2026-09-15]]. The table maps common raw strings to last journal types and descriptions for success, refusal, error and cancellation (raw lines 14–40). It is diagnostic reference, not proof of a specific payment's capture, settlement, final result or shopper eligibility.

## Q2 — Central capability, prerequisites, and warnings

**Question:** How should PENDING, ACCEPTED, validation errors, expired token and refusal be distinguished?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-klarna-raw-responses]] → [[raw/adyen/docs/payment-methods/klarna/raw-responses/2026-09-15]]. PENDING is expected for the Klarna Widget and has no last journal type; ACCEPTED maps to Authorised (raw lines 20–21). BAD_VALUE and other Error rows point to request, tax, currency, address, merchant-data or configuration diagnostics (raw lines 22–35). NOT_FOUND Invalid session id maps to OfferCancelled for an expired offer (raw line 36). The invalid authorisation-token diagnostic is not linked to payment status and can reflect premature /payments/details or a token expired after 60 minutes (raw lines 37–38). Risk refusals map to Refused, with unpaid balance only a possible reason (raw lines 39–40).
