# docs-payment-methods-promptpay-android-drop-in retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-promptpay-android-drop-in]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 page adds PromptPay to existing Android Drop-in in Sessions or Advanced flow (pinned raw lines 15–37). It does not explain QR action generation, shopper confirmation, expiry or final webhook sequence; the page ends with links to the Android Drop-in guide, webhooks and API Explorer (lines 67–71). It does not prove current merchant enablement or payment success. Canonical source stem: `source-adyen-docs-payment-methods-promptpay-android-drop-in`.

## Q2 — What are central prerequisites, capability and warnings?

Sessions and Advanced each require their matching existing Android Drop-in integration and PromptPay added in Customer Area (pinned raw lines 25–37). The page says no additional PromptPay `/sessions` or `/payments` fields and no extra Drop-in configuration in either flow (lines 39–57); ordinary main-flow requirements remain governed by the linked guides. It instructs tests with real details/small amounts and Customer Area status checks; live acceptance requires contacting Support to add PromptPay in the live Customer Area (lines 59–65). Those instructions do not prove transactions were run or enablement granted. Canonical source stem: `source-adyen-docs-payment-methods-promptpay-android-drop-in`.
