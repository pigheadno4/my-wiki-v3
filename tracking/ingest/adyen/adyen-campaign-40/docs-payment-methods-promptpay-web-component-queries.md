# docs-payment-methods-promptpay-web-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-promptpay-web-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2019-modified page captured on 2026-09-15 adds PromptPay to existing Web Components and distinguishes Sessions and Advanced prerequisites (pinned raw lines 5–19, 21–37). It provides Component mounting and setup guidance but no QR action, shopper completion or final-outcome sequence; its See also list routes to Web Components, webhooks and API Explorer (lines 39–98). It does not prove current enablement or payment success. Canonical source stem: `source-adyen-docs-payment-methods-promptpay-web-component`.

## Q2 — What are the central prerequisites, version conditions and warnings?

Both flows require existing Web Components integrations and contacting Support to add PromptPay in Customer Area (pinned raw lines 25–37). No method-specific API fields are stated; the page calls `/sessions` default for Components v5.0.0+ and points to `/payments` for an additional use case (lines 47–52). For v6, it imports `PromptPay` and constructs `new PromptPay(checkout)`; v5.x.x or earlier uses `checkout.create('promptpay')` (lines 39–45, 64–84). The v6 import link targets a Drop-in URL despite the Components context (line 41). Testing guidance uses real details/small amounts and a TEST Customer Area check, while live acceptance requires Support addition in the live Customer Area (lines 86–92); this is guidance, not evidence of execution. Canonical source stem: `source-adyen-docs-payment-methods-promptpay-web-component`.
