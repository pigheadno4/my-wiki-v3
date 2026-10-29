# Fixed retrieval checks: EPS Android chooser

Canonical source stem: `source-adyen-docs-payment-methods-eps-android`
Pinned raw: `raw/adyen/docs/payment-methods/eps/android/2026-09-15.md` (SHA-256 `5bfbf6902301cb1110f95777d604379807de2fb9ef5a3e255cf993b6af3b8d67`)
Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-eps-android.md`

## Q1 — What is this page for, and what should a reader not infer?

The page is an Android route selector, linking EPS Drop-in and Components children (`raw/adyen/docs/payment-methods/eps/android/2026-09-15.md:15-27`) plus the four base Sessions/Advanced Android integration guides (`:29-36`). It is not a full method implementation guide and gives no EPS request fields, SDK or Checkout API minimum, issuer bank list, callback steps or evidence of merchant enablement/payment success. Those details must be checked in the linked implementation sources.

## Q2 — What capability and prerequisite matter most?

The two choices are all-in-one Android Drop-in and the `EPSComponent` route that the page says handles the EPS redirect (`:19-27`). Build the matching main integration first; the page links Drop-in Sessions, Components Sessions, Drop-in Advanced and Components Advanced (`:29-36`). This chooser does not decide which flow a merchant already uses or prove the redirect completed.
