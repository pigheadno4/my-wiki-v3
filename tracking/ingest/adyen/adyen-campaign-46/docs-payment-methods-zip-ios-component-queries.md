# Fixed retrieval checks — docs-payment-methods-zip-ios-component

## Q1 — Purpose and scope

**Query:** What does Adyen's Zip iOS Component page add, and does it prove live enablement or a completed payment?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-zip-ios-component.md` → `raw/adyen/docs/payment-methods/zip/ios-component/2026-09-15.md`.

**Answer:** It adds Zip to an existing iOS Components integration, with Sessions as default for Components v5.0.0+ and a /payments additional-use-case tab. The page is a captured TEST-oriented guide, not live enablement or payment proof. Live Zip acceptance needs a separate live Customer Area request (raw 15–34, 1681–1687). Canonical stem: `https://docs.adyen.com/payment-methods/zip/ios-component`.

## Q2 — Redirect, versioned Component and recurring setup

**Query:** How does Zip iOS Component use Sessions or /payments, handle redirect, and create/use a recurring token?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** The /sessions and /payments parameter tables have blank Required cells, so their shopper/address/line-item entries are documented fields rather than all mandatory (raw 32–44, 681–694). The /payments path has clickAndCollect for pickup (691), a redirect action response (1375–1389), and an AU/AUD app-scheme example (701–755). For v5+ the app uses InstantPaymentComponent and the flow-specific delegate; v4 uses generic Component (1391–1446). Token creation requires storePaymentMethod and shopperReference, with recurring.token.created arriving after settlement and recurring lifecycle webhook setup (1448–1469); future /payments uses storedPaymentMethodId, same shopperReference, ContAuth, and Subscription or UnscheduledCardOnFile (1471–1481). Warn that the /payments curl contains an unrendered hint marker (711–714), old Java recurring code names recurringDetailReference (1524–1527), some older recurring samples have HTTPS returnUrl (1530), and TEST/live Customer Area steps differ (1681–1687). Example return/redirect does not prove successful authorization or settlement. Canonical stem: `https://docs.adyen.com/payment-methods/zip/ios-component`; pinned raw: `raw/adyen/docs/payment-methods/zip/ios-component/2026-09-15.md`.
