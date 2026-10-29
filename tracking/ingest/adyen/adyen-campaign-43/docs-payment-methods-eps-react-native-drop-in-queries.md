# Fixed retrieval checks: EPS React Native Drop-in

Canonical source stem: `source-adyen-docs-payment-methods-eps-react-native-drop-in`
Pinned raw: `raw/adyen/docs/payment-methods/eps/react-native-drop-in/2026-09-15.md` (SHA-256 `91a8cbbc52146bc61b4d657c6e95fed5a59a8da5bb971059e0109bd6a866075b`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-react-native-drop-in.md`

## Q1 — What is this page for, and what should a reader not infer?

It is the captured EPS-specific add-on for existing React Native Drop-in Sessions and Advanced flows (`raw/adyen/docs/payment-methods/eps/react-native-drop-in/2026-09-15.md:15-25`, `:97-107`). It gives redirect prerequisites, ordinary request/configuration additions, and a separate SEPA recurring-token recipe (`:29-89`, `:109-160`). The base flow guides own generic redirect handling (`:35`, `:106`); the page does not prove EPS account enablement, successful bank authorization, or live recurring operation. The Sessions integration-type link's URL points to Advanced despite the Sessions label (`:33`), while Sessions redirect/session links use Sessions URLs (`:35`, `:42`).

## Q2 — What capabilities, prerequisites and warnings matter most?

For Sessions, have React Native Drop-in, Checkout API v68+, `action.type=redirect` handling and EPS in Customer Area; no EPS-specific `/sessions` fields or configuration are added to the ordinary flow (`:29-48`). For Advanced, have its own Drop-in and redirect handling; no EPS-specific ordinary `/payments` fields or configuration are added (`:97-119`). Do not transfer Sessions' v68+ requirement to the Advanced branch without separate evidence (`:34`, `:101-107`). EPS recurring is routed through SEPA Direct Debit, with recommended explicit permission, `/payments` token creation (`storePaymentMethod=true`, shopper reference), a settled-payment `recurring.token.created` webhook, then future `/payments` with `storedPaymentMethodId`, ContAuth and Subscription/UnscheduledCardOnFile (`:50-89`, `:121-160`). The Sessions subsection itself uses `/payments` wording for that token recipe, not a Sessions-specific token variant (`:63-66`). Live EPS requires a live Customer Area request (`:91-95`, `:162-166`).
