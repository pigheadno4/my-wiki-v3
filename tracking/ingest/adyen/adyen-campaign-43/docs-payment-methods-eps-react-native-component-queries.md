# Fixed retrieval checks: EPS React Native Component

Canonical source stem: `source-adyen-docs-payment-methods-eps-react-native-component`
Pinned raw: `raw/adyen/docs/payment-methods/eps/react-native-component/2026-09-15.md` (SHA-256 `f3e38ea821879f86249f6664d3388e12a1c101864ffc502ba04eeacddddfc47b`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-react-native-component.md`; platform cross-route: `wiki/concepts/adyen-react-native-sdk.md`.

## Q1 — What is this page for, and what should a reader not infer?

It is the EPS-specific guide for React Native Components (`raw/adyen/docs/payment-methods/eps/react-native-component/2026-09-15.md:15-23`), explicitly excluding Sessions flow here (`:25-29`) and providing Advanced-flow requirements (`:31-53`) and a later SEPA recurring-token route (`:55-94`). The Sessions statement is scoped to this method/Component page and does not establish a general React Native SDK restriction. The page also does not establish current bank coverage, merchant enablement or successful payment; live EPS requires a live Customer Area request (`:96-100`).

## Q2 — What capabilities, prerequisites and warnings matter most?

Advanced needs an existing React Native Components integration, `action.type=redirect` handling and EPS in Customer Area (`:35-41`). Yet its integration-type label links to a Drop-in URL (`:39`), while redirect and make-payment links name Components (`:40`, `:53`); use the named integration scope, not the mismatched URL as proof of Drop-in requirements. EPS needs no extra Component configuration or ordinary `/payments` parameters (`:43-53`). For future SEPA Direct Debit recurring, explicit shopper permission and clear amount/schedule are strongly recommended (`:59-66`); send `storePaymentMethod=true` and a shopper reference in `/payments` (`:68-71`), wait until settlement for `recurring.token.created` and `storedPaymentMethodId` (`:73-80`), then use the stored ID, same reference, `ContAuth` and Subscription or UnscheduledCardOnFile in later `/payments` (`:82-92`). Test status is in test Customer Area; live EPS needs a request in live Customer Area (`:96-100`).
