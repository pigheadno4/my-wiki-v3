# Q1 — Purpose, scope and limits

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gopay-api-only.md` → pinned raw.

The 2026-09-15 source adds GoPay to an existing **API-only Advanced-flow** integration with redirect handling and Customer Area setup (raw `adyen/docs/payment-methods/gopay/api-only/2026-09-15.md:15-29`). It covers ID/IDR discovery, a merchant-built form, and GoPay `/payments` redirect (raw lines 38-146). It does not prove current merchant eligibility, enabled access, full base integration behavior or successful payments. The prose claims item information is included, but the dedicated request table/sample omit item fields; the discovery example omits table-listed `channel`, and the payment example has JSON-looking `browserInfo` inside quotes plus lowercase `web` (raw lines 31-35,48-73,89-129).

# Q2 — Central capability, prerequisites and warnings

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-gopay-api-only.md`. For stored-payment retrieval, `wiki/adyen-index.md` → `wiki/concepts/adyen-tokenization.md` → the same source.

The API-only branch requires a redirect-capable existing integration and method addition in Customer Area; the `/payments` table marks `gopay_wallet`, `browserInfo` and applicable `channel` (raw `adyen/docs/payment-methods/gopay/api-only/2026-09-15.md:23-29,89-97`). Token creation needs `storePaymentMethod: true`, `shopperReference` (minimum three characters) and a recurring model; **after settlement**, `recurring.token.created` supplies the stored ID (raw lines 148-167). Subscription uses stored ID/`ContAuth`/`Subscription` with final status via `AUTHORISATION` webhook; CardOnFile uses stored ID/`ContAuth`/`CardOnFile` but requires the shopper's GoPay PIN redirect, a return `/payments/details` call and a later final-status webhook (raw lines 169-181,386-419). TEST guidance says contact Support; live GoPay requires a live Customer Area request before acceptance (raw lines 421-427).
