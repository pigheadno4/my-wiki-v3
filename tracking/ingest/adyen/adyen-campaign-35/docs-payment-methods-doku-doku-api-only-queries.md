# docs-payment-methods-doku-doku-api-only — attempt 1

Q1. What purpose and scope does this source serve, and what cannot be inferred?

It is a 2019-modified, 2026-09-15-captured **API-only** DOKU guide for a merchant-owned checkout form using Indonesian bank-transfer and convenience-store methods (source-adyen-docs-payment-methods-doku-doku-api-only; raw lines 15–28). It documents ID/IDR method discovery and an Alfamart voucher example; that example cannot establish the identical response/status lifecycle for every bank-transfer variant, current availability, live approval or payment completion (raw lines 44–62, 64–95, 402–445). BCA and BRI virtual-account rows alone state a local-entity condition (raw lines 56–58).

Q2. What are its central capability, prerequisites and warnings?

The merchant needs an existing API-only integration and test Customer Area addition, collects shopper first/last name and email, selects a DOKU type from `/paymentMethods` for `ID`/`IDR`, then sends a server-side `/payments` request with the type, shopper fields and minor-unit amount (raw lines 23–72). In the voucher example, `PresentToShopper` supplies an offline voucher; `PENDING`/true is **pending**, `AUTHORISATION`/true records completed shopper payment, `AUTHORISATION`/false is failure and `OFFER_CLOSED`/true is unpaid expiry (raw lines 402–445). The default virtual-account/voucher validity is 48 hours and a separate live Customer Area request precedes live acceptance (raw lines 447–457). The PHP `alfamart` type differs from the page's `doku_alfamart` prose/JSON, and Go library version label differs from its `/v9/` imports; preserve these as example conflicts (raw lines 52–68, 158–177, 259–268). The sample `returnUrl` does not override the voucher-specific no-acquirer-redirect statement (raw lines 93, 436).

Retrieval route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-doku-doku-api-only]] → [[raw/adyen/docs/payment-methods/doku/doku-api-only/2026-09-15]].
