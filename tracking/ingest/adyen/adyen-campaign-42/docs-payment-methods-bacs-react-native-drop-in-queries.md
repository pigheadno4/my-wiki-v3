# Fixed-query evidence — BACS React Native Drop-in

Canonical source stem: `source-adyen-docs-payment-methods-bacs-react-native-drop-in`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-bacs-react-native-drop-in]]`

## Q1 — Purpose, scope, and inference boundary

This 2026-09-15 page is a BACS Direct Debit add-on to **existing React Native Drop-in** Sessions or Advanced integrations, not a complete base guide (raw lines 15–35, 414–424). It does not establish current BACS merchant enablement, a valid DDI, cleared/settled funds or successful debit: the guide says `Received` is tracked for success using webhooks, and its Advanced sample also shows `Received` (raw lines 400, 805–818, 873). The BACS overview supplies DDI, clearing, notice and chargeback authority.

## Q2 — Central capability, prerequisites, and warnings

Sessions needs Checkout API v68+, Customer Area setup and required `shopperEmail` in `/sessions`; its prerequisite URL points to Advanced despite a Sessions label, and no extra BACS configuration is stated (raw lines 29–45, 341–345). Advanced needs Customer Area setup and handling labeled `Direct`; `/payments` requires shopper email, `directdebit_GB`, holder name, account number and bank location ID (raw lines 418–444). The Advanced response prose states `Direct`, but its adjacent JSON shows a `voucher` action with PDF mandate URL and `Received`; do not infer a settled payment or choose one action shape from this conflict (raw lines 805–818). The recurring route adds `shopperReference` and `storePaymentMethod: true` to initial `/payments`, stores the ID on `recurring.token.created`, and later uses stored ID/same shopper reference/`ContAuth`; change of date or amount requires advance notice under the cited Guarantee, while explicit permission and each-payment notice are strong recommendations here (raw lines 347–400, 820–873). Live acceptance needs a request in the live Customer Area (raw lines 402–412, 875–885).
