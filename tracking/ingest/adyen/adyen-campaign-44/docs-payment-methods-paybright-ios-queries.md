# PayBright iOS retrieval checks

## Q1 — Purpose, scope, and what not to infer

**Question:** What does the PayBright iOS page establish?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paybright-ios]] → [[raw/adyen/docs/payment-methods/paybright/ios/2026-09-15]]. It is an iOS chooser linking PayBright Drop-in and Redirect Component child guides plus base iOS Sessions guides (raw lines 21–35). It gives no detailed API/SDK requirements or transaction outcome. Its link labels do not prove current merchant eligibility or successful payment.

## Q2 — Central capability, prerequisites, and warnings

**Question:** Which iOS paths are linked, and can a new merchant integrate PayBright?

**Answer route:** [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-paybright-ios]] → [[raw/adyen/docs/payment-methods/paybright/ios/2026-09-15]]. The page links all-in-one Drop-in and a Redirect Component, with general iOS Sessions routes at the end (raw lines 23–35). It expressly states that Adyen will not accept new PayBright integrations after Affirm acquired PayBright (raw line 19). See [[source-adyen-docs-payment-methods-paybright-ios-drop-in]] or [[source-adyen-docs-payment-methods-paybright-ios-component]] for actual implementation details and [[source-adyen-docs-payment-methods-paybright]] for product scope.
