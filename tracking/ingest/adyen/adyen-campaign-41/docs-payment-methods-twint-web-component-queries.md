# docs-payment-methods-twint-web-component retrieval checks

Route: [[index]] → [[adyen-index]] → [[adyen-online-payments]] → [[source-adyen-docs-payment-methods-twint-web-component]].

## Q1 — What is this source for, and what cannot be inferred?

The 2026-09-15 guide adds TWINT to existing Web Components in Sessions or Advanced flow, with redirect setup, `Twint` initialization, recurring tokens and a later capture section (pinned raw lines 15–76, 78–117, 125–167, 216–282). It does not show a concrete redirect response, return/details request or final payment webhook, and cannot prove current merchant enablement, issued token, captured funds or payment success. Canonical source stem: `source-adyen-docs-payment-methods-twint-web-component`.

## Q2 — What are central prerequisites, lifecycle limits and warnings?

Sessions requires Web Components Sessions, Checkout API v68+, redirect handling and Customer Area addition, with no TWINT-specific `/sessions` parameters or configuration (pinned raw lines 29–60). Advanced requires its corresponding flow, redirect handling and Customer Area addition, and states no extra `/payments` parameters; its section does not repeat the v68 minimum (lines 125–167). Both sections import/initialize `Twint` and describe `storePaymentMethod` plus shopper reference, `recurring.token.created` webhook, then stored ID/`ContAuth` with Subscription or UnscheduledCardOnFile (lines 46–76, 78–117, 135–208). The later capture section states automatic default capture, seven-day authorization expiry under Manual, partial capture without multiple partial captures and automatic cancellation of the remainder; its prose says `modificationAmount` while the JSON example uses `amount` (lines 216–243). TEST checks and a live Customer Area request are separate gates (lines 119–123, 210–214). Canonical source stem: `source-adyen-docs-payment-methods-twint-web-component`.
