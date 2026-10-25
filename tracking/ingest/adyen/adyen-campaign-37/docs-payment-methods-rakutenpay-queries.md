# Rakuten Pay overview retrieval questions

## Q1 — What is this page's purpose and scope, and what cannot be inferred?

It describes a Japan Rakuten Pay digital wallet with desktop/mobile shopper redirect to Rakuten Pay and return to the merchant page, and states **Ecommerce and IPP** availability (raw line 19; [[source-adyen-docs-payment-methods-rakutenpay]]). It does not define IPP, establish current merchant eligibility, or make shopper return proof of authorization, capture or settlement. The Web/native/API-only and other links are navigation, not child implementation facts (lines 25–73). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay]] → [[raw/adyen/docs/payment-methods/rakutenpay/2026-09-15]].

## Q2 — What capability and qualification does the overview provide?

Its **Wallets/Redirect/JP/JPY** row marks recurring, refunds including partial/multiple partial, separate and partial captures, and chargebacks positive, while **multiple partial captures** is negative (raw lines 21–23). Most positive marks say **“See note”**, yet no such explanatory note appears in this pinned page (full raw lines 15–80), so the conditions cannot be resolved from the overview. These historical marks do not show a configured merchant, an executed refund/capture or final transaction success. Integration routes include Web, iOS, Android, React Native, Flutter and API-only (lines 25–61), with Pay by Link/in-person links following (lines 63–73); child specifics need their own sources ([[source-adyen-docs-payment-methods-rakutenpay]]). Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-rakutenpay]] → [[raw/adyen/docs/payment-methods/rakutenpay/2026-09-15]].
