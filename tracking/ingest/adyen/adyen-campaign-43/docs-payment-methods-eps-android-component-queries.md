# Fixed retrieval checks: EPS Android Component

Canonical source stem: `source-adyen-docs-payment-methods-eps-android-component`
Pinned raw: `raw/adyen/docs/payment-methods/eps/android-component/2026-09-15.md` (SHA-256 `e6af6c7ec1359841cbbbf89f3450338d72801bd39e97285ee0a839e9d3d4926c`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-android-component.md`

## Q1 — What is this page for, and what should a reader not infer?

This is a captured EPS-specific Android Components add-on with separate Sessions and Advanced branches (`raw/adyen/docs/payment-methods/eps/android-component/2026-09-15.md:15-25`, `:191-199`). It covers required base integration/redirect handling (`:29-36`, `:193-199`), importing and launching `EPSComponent` with Compose or a view (`:44-142`, `:201-301`), and a separate SEPA Direct Debit recurring-token path (`:144-183`, `:309-348`). General redirect outcome handling lives in linked base guides, and this capture does not establish current merchant enablement, successful shopper redirect, authorization or recurring payment. The Sessions v68+ prerequisite (`:34`) is not also stated in the Advanced table (`:193-199`).

## Q2 — What capabilities, prerequisites and warnings matter most?

Sessions needs existing Android Components, Checkout API v68+, `action.type=redirect` handling, and Customer Area EPS setup; it says no EPS-specific ordinary `/sessions` additions (`:29-42`). Advanced needs existing Android Components, redirect additional-action handling and EPS setup, and says no EPS-specific ordinary `/payments` additions (`:191-199`, `:303-307`). Import `eps` and, for Compose, `components-compose`; Sessions gets the EPS payment method from the session, while Advanced gets it from `/paymentMethods` (`:44-65`, `:99-142`, `:201-222`, `:256-301`). `setSubmitButtonVisible` is optional and defaults true; snippets show doubled braces and placeholder `value`, so are not copy-ready (`:69-87`, `:224-244`). EPS recurring is through SEPA Direct Debit, with recommended explicit permission, `/payments` token-creation fields and a settled-payment `recurring.token.created` webhook before future stored-method payments (`:144-183`, `:309-348`). The Sessions recurring subsection also uses `/payments` language, not a separate Sessions-specific token recipe (`:153-160`). A live Customer Area request is required before live EPS acceptance (`:185-189`, `:350-354`).
