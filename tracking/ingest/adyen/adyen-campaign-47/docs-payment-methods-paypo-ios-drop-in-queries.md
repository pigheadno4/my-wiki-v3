# Fixed retrieval checks — docs-payment-methods-paypo-ios-drop-in

## Q1 — Purpose and scope

**Query:** What does the PayPo iOS Drop-in guide add, and does its redirect sample show payment completion?

**Expected route:** `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-paypo-ios-drop-in.md` → `raw/adyen/docs/payment-methods/paypo/ios-drop-in/2026-09-15.md`.

**Answer:** It is a PayPo-specific add-on for existing iOS Drop-in Sessions and Advanced integrations (raw 15–34, 444–454). The Advanced response is RedirectShopper/action.type redirect, a next action rather than completed authorization or capture (846–860). TEST examples do not prove current live account eligibility. Canonical stem: `https://docs.adyen.com/payment-methods/paypo/ios-drop-in`.

## Q2 — Time, capture, fields and iOS warnings

**Query:** What are PayPo's iOS offer/payment clocks and capture constraints, and which flow details matter?

**Expected route:** same root → provider → concept → source → pinned raw.

**Answer:** Sessions needs iOS Drop-in, Checkout API v68+, Customer Area PayPo, shopper name/email; billing/delivery are optional (29–47). Advanced needs existing iOS Drop-in with redirect handling, type paypo, name/email, optional addresses (448–474). No PayPo-specific Drop-in configuration is added (422–426, 456–460). The offer link lasts up to 72 hours before authorization; shopper acceptance makes it Authorised and starts the 30-day payment period. Only full capture is possible; automatic immediate capture is configurable in live Customer Area, or manual capture uses the original PSP reference (390–420, 862–892). Sessions uses illustrative app-scheme returnUrl (65), while Advanced uses an HTTPS website returnUrl (495), so implement actual iOS return handling. Request curl examples omit continuation before -d (58–59, 485–486). TEST verification code and status route are at 432–442/898–908; live acceptance needs a separate request (442, 908). Canonical stem: `https://docs.adyen.com/payment-methods/paypo/ios-drop-in`; pinned raw: `raw/adyen/docs/payment-methods/paypo/ios-drop-in/2026-09-15.md`.
