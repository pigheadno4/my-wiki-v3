# Android cards Drop-in retrieval checks

Q1. Which integration does the page extend, and what must already be in place?

It adds cards to an existing Android Drop-in integration, labeled v5.0.0 (released October 2023); earlier versions have a separate guide (raw lines 15–21). Both Sessions and Advanced tabs require the matching Drop-in flow at minimum v5.0.0 and cards added in Customer Area (lines 23–39). Forward route: [[index]] → [[adyen-index]] → [[adyen-android-sdk]] → [[source-adyen-docs-payment-methods-cards-android-drop-in]] → [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15]].

Q2. What limits apply to token-storage examples and live-payment readiness?

The guide recommends explicit permission for future recurring payments (raw line 360), while Sessions token examples differ between `askForConsent` and `enabled` (lines 376–428, 530–546); Advanced asks for a storage switch and uses separate `/payments` examples (lines 998–1034). The examples use test endpoints and `test_` card details; the live checklist separately calls for test payments, adding cards in live Customer Area, PCI DSS assessment and SAQ A submission (lines 2489–2499). A request example or token webhook is not an authorization, capture or settlement result. Forward route: [[index]] → [[adyen-index]] → [[adyen-android-sdk]] → [[source-adyen-docs-payment-methods-cards-android-drop-in]] → [[raw/adyen/docs/payment-methods/cards/android-drop-in/2026-09-15]].
