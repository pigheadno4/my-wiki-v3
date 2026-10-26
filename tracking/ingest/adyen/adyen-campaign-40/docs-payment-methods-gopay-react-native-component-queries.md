# docs-payment-methods-gopay-react-native-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-gopay-react-native-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 page is a GoPay add-on to React Native Components. It explicitly excludes Sessions Components and covers Advanced redirect, tokenization and recurring continuation (pinned raw lines 15–31, 35–59, 110–131, 358–383). It does not prove current account enablement, token issuance or payment success; token creation is described after settlement, and final recurring-payment status is directed to webhooks (lines 124–131, 350–357, 380–383). Canonical source stem: `source-adyen-docs-payment-methods-gopay-react-native-component`.

## Q2 — What are central prerequisites, capability and warnings?

Advanced requires existing React Native Components, redirect handling and Customer Area addition, with `gopay_wallet`, `browserInfo` and applicable `channel` marked required for initial `/payments` (pinned raw lines 35–59). The integration-type link says Drop-in despite Components text/other links; the IDR example uses web/Windows data and contains a missing shell continuation after `-X POST` plus an invalid quoted nested `browserInfo` value, so it is not a runnable React Native recipe (lines 39–40, 63–91). First-payment token creation uses `storePaymentMethod`, shopper reference and recurring model, with `storedPaymentMethodId` delivered by a post-settlement webhook (lines 118–131). Subscription uses `ContAuth`; its snippets leave fields blank (lines 133–169). CardOnFile requires shopper PIN redirect and `/payments/details` on return; final processed status comes by `AUTHORISATION` webhook (lines 358–383). Testing routes to Support, and live acceptance requires a live Customer Area request (lines 385–391). Canonical source stem: `source-adyen-docs-payment-methods-gopay-react-native-component`.
