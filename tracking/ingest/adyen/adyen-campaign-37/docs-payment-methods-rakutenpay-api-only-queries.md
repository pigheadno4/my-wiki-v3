# docs-payment-methods-rakutenpay-api-only — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

This is a Rakuten Pay **API-only Web** add-on, not a complete base integration or current merchant-approval record (source-adyen-docs-payment-methods-rakutenpay-api-only; raw lines 15–29). It describes a merchant form, JP/JPY discovery, redirect action, recurring restrictions and TEST simulator (raw lines 31–106). Its sample does not prove `/paymentMethods` request shape, because the “available methods” example calls `/payments` yet shows a `paymentMethods` response; it also does not prove authorization, settlement or live enablement (raw lines 44–86, 100–106).

Q2. What are its central capability, prerequisites and warnings?

The merchant needs an existing API-only integration, redirect handling and Rakuten Pay added in Customer Area, with no extra Rakuten Pay form fields; `/paymentMethods` prose specifies `JP`/`JPY` (raw lines 23–51). The flow list says to include purchased-item data in the payment request, but the later `/payments` section says no extra parameters are needed; neither claim should be generalized until the conflict is resolved against endpoint-specific authority (raw lines 31–36, 88–90). Recurring card-on-file use is review-, cadence-, category- and per-model-application-qualified, with explicit shopper permission strongly recommended; the TEST route uses a named DGFT acquirer/simulator without the wallet app (raw lines 92–106). A redirect or simulator result is not a live payment outcome.

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay-api-only]] → [[raw/adyen/docs/payment-methods/rakutenpay/api-only/2026-09-15]].
