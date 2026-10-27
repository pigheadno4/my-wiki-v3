# Fixed-query evidence — SEPA Direct Debit Web Drop-in

Canonical source stem: `source-adyen-docs-payment-methods-sepa-direct-debit-web-drop-in`
Retrieval route: `[[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-sepa-direct-debit-web-drop-in]]`

## Q1 — Purpose, scope, and inference boundary

This is Adyen's 2026-09-15 add-on for SEPA Direct Debit in an **existing Web Drop-in** integration. It splits instructions by server-side Sessions and Advanced flows (raw lines 15–25, 29–35, 900–910). It does not itself constitute the full base Drop-in guide, establish current account enablement, or prove payment funding. Its Advanced “successful payment” illustration has `resultCode: Received` (raw lines 962–970), which should not be treated as settled funds. The method overview is the route for broader mandate and settlement/chargeback context.

## Q2 — Central capability, prerequisites, and warnings

Sessions needs existing Web Drop-in, Checkout API v68+, and Customer Area method setup; no extra ordinary `/sessions` fields are required, while `SepaDirectDebit` import is optional (raw lines 29–53). Advanced needs its own existing Web Drop-in/action handling, method setup, `paymentMethod.sepa.ownerName`, unencrypted `sepa.ibanNumber`, and billing address for the listed non-EEA SEPA IBAN countries/territories (raw lines 904–959). With nonautomatic capture the guide gives delayed or manual capture routes and says SEPA authorizations do not expire; multiple partial capture needs Support enablement (raw lines 972–981). It describes Subscription/UnscheduledCardOnFile tokenization, recommends explicit permission and transparent schedule/amount, identifies `recurring.token.created` as the stored-ID event, and uses shopper-absent `/payments` for token reuse (raw lines 55–65, 264–268, 1342–1373, 1653–1679). Live SEPA acceptance requires a live Customer Area request (raw lines 884–898, 1960–1974).
