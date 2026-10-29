# Fixed retrieval checks — docs-payment-methods-atome-react-native-component

## Q1 — Purpose and supported flow

**Query:** Does Atome React Native Component support Sessions, and what does this guide cover?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-atome-react-native-component.md` → `raw/adyen/docs/payment-methods/atome/react-native-component/2026-09-15.md`.

**Answer:** The page explicitly says React Native Components do not support Sessions; it is an Advanced-flow method add-on with /payments fields, redirect response and test/live setup (raw 23–53, 781–823). It does not prove current account availability or successful payment. Canonical stem: `https://docs.adyen.com/payment-methods/atome/react-native-component`.

## Q2 — Request, redirect and material warnings

**Query:** What must a React Native Components Advanced integration send for Atome, and which sample/link caveats matter?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Start with existing Advanced React Native Components, redirect handling and Customer Area enablement (31–41); no Atome-specific Component configuration is added (43–47). The /payments table marks type atome, name, email, phone, billing address, lineItems and countryCode required, with deliveryAddress optional when same as billing; use MY/MYR or SG/SGD (49–64). The SG/SGD TEST v72 sample has an HTTPS returnUrl (71–129), whose suitability for an app's return flow must be checked. Its curl lacks a continuation before -d (75–76). The response is RedirectShopper despite the “successful payment” heading (781–793). The labeled Components prerequisite URL at line 39 uses integration=Drop-in; nearby redirect/payment links at lines 40/53 use integration=Components for base navigation, without any claim that the mismatched link resolves. Partial refund specifies amount (795–803); sandbox account needs Adyen contact and live acceptance needs Support (805–823). The separate overview has portable-electronics and capture qualifications absent from this add-on. Canonical stem: `https://docs.adyen.com/payment-methods/atome/react-native-component`; pinned raw: `raw/adyen/docs/payment-methods/atome/react-native-component/2026-09-15.md`.
