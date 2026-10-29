# C45 Clearpay React Native Drop-in retrieval queries

Canonical source stem: `source-adyen-docs-payment-methods-clearpay-react-native-drop-in`

Full pinned raw path: `raw/adyen/docs/payment-methods/clearpay/react-native-drop-in/2026-09-15.md`

Route: `[[index]]` → `[[adyen-index]]` → `[[adyen-online-payments]]` → `[[source-adyen-docs-payment-methods-clearpay-react-native-drop-in]]` → `[[raw/adyen/docs/payment-methods/clearpay/react-native-drop-in/2026-09-15]]`.

## Q1 — purpose and scope

**Query:** What does this Clearpay React Native Drop-in guide cover, and does the GB/GBP example prove merchant availability?

**Answer path:** Raw opening lines 15–23 describe method-specific additions to an existing React Native Drop-in, with Sessions and Advanced sections. The linked overview `raw/adyen/docs/payment-methods/clearpay/2026-09-15.md` lines 23–31 identifies the UK Clearpay brand and GB/GBP matrix. The child GB/GBP TEST request is a fixture; it does not prove a merchant's live enablement, successful authorisation, capture or settlement.

## Q2 — central capability, prerequisites and warnings

**Query:** What does the React Native Drop-in guide require for Sessions and Advanced, and what lifecycle/example issues matter?

**Answer path:** Sessions requirements lines 29–36 specify base flow, Checkout API v68+, redirect handling and Customer Area addition; request table lines 40–53 marks shopper/country/address/items required, phone optional. The Sessions base-flow link at line 33 actually targets an Advanced URL, whereas lines 35 and 42 target Sessions. Advanced requirements lines 217–223 and request table lines 233–246 add method-specific data; example lines 248–310 sets `clearpay`, and initial response lines 312–326 redirects without proving final payment. Capture lines 124–143 and 330–349 set 13-day/one-day test deadlines and partial-capture remainder rules. Refund/cancel lines 145–156 and 351–360 separate before/after capture. Discount lines 158–194 and 362–396 say £1 off Item #2 but show quantity two at -100 and a 200-minor-unit total decrease, plus missing comma. Curl examples lines 58–63 and 251–256 lack continuation before `-d`. Sandbox/live lines 196–211 and 398–413 require regional test setup and a live Customer Area request.
