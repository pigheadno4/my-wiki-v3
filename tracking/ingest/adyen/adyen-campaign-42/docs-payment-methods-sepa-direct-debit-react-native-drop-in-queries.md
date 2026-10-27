# Fixed-query evidence — SEPA Direct Debit React Native Drop-in

Canonical source stem: `source-adyen-docs-payment-methods-sepa-direct-debit-react-native-drop-in`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-sepa-direct-debit-react-native-drop-in]]`

## Q1 — Purpose, scope, and inference boundary

This is the 2026-09-15 method-specific **React Native Drop-in** add-on for existing Sessions or Advanced integrations, not a full base integration guide (raw lines 15–25, 29–35, 892–902). It does not establish a React Native SDK version, current account enablement, valid shopper mandate, or funded payment. The Advanced example calls a response successful yet shows `resultCode: Received`; final authorization/capture/settlement cannot be inferred from it (raw lines 948–967). The method overview holds mandate, notice and chargeback context.

## Q2 — Central capability, prerequisites, and warnings

Sessions requires Checkout API v68+, Customer Area method addition, and an existing React Native Drop-in integration, with no extra ordinary `/sessions` parameters or SEPA configuration (raw lines 29–47). Its Sessions prerequisite label links to an Advanced-flow URL, a source-navigation mismatch (raw line 33 versus line 41). Advanced needs an existing integration with `direct` action handling; `/payments` uses SEPA owner name and unencrypted IBAN, plus a billing address for the listed non-EEA SEPA IBAN countries/territories (raw lines 896–945). Nonautomatic capture requires delayed or manual capture; multiple partial capture needs Support enablement (raw lines 958–967). For recurring, standard tokenization fields lead to a `recurring.token.created` stored ID and shopper-absent Subscription/UnscheduledCardOnFile `/payments`; the explicit-permission/schedule wording is a strong recommendation here (raw lines 49–59, 258–290, 571–597, 1328–1358, 1639–1665). Live SEPA acceptance requires a request in the live Customer Area (raw lines 878–890, 1946–1958).
