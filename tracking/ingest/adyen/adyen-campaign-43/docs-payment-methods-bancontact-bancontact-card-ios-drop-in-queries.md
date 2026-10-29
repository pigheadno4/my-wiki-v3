# Fixed retrieval checks — Bancontact card iOS Drop-in

Route: `wiki/index.md` → `wiki/adyen-index.md` → `wiki/concepts/adyen-online-payments.md` → `wiki/sources/adyen/source-adyen-docs-payment-methods-bancontact-bancontact-card-ios-drop-in.md`.

## Q1. What is this source's purpose and scope, and what cannot be inferred?

This 2026-09-15 source covers **Bancontact card** in existing **iOS Drop-in** Sessions and Advanced flows, including card/3DS differences, no-extra-card-fields, WIP recurring and TEST/live routes (primary raw `raw/adyen/docs/payment-methods/bancontact/bancontact-card/ios-drop-in/2026-09-15.md:15-60,62-119,458-491`; canonical source stem `source-adyen-docs-payment-methods-bancontact-bancontact-card-ios-drop-in`). It is not the Bancontact mobile app/QR flow, a complete base Drop-in integration, a WIP account approval or proof of payment settlement. No additional **card-specific** fields does not mean no base `/sessions` or `/payments` requirements (`:45-60`). The co-badged TEST card can route to Bancontact or Visa based on setup (`:468`).

## Q2. What are the central capabilities, prerequisites and warnings?

Bancontact card lacks CVC except a co-badged CVC field may appear; 3DS is mandatory and separate captures unsupported, with iOS Drop-in redirecting the shopper to the issuer website (`:19-25`). Existing Sessions or Advanced iOS Drop-in and Bancontact card Customer Area addition are prerequisites (`:27-43`). The guide calls `/sessions` the default for **Drop-in v5.0.0+**, gives `/payments` for added use cases, and requires no Bancontact-specific extra request fields or Drop-in config for v5+/v4.x (`:45-60`). Recurring is **WIP-gated**, with signup, eligibility and amount limits, initial SCA/consent and issuer liability retained (`:62-81`). Store initial payment details using `storePaymentMethod` plus shopper reference; after settlement token webhook supplies stored ID; later `/payments` uses it with matching reference, `ContAuth` and Subscription or UnscheduledCardOnFile (`:83-119`). TEST routing for the BCMC/Visa card depends on setup, and live acceptance requires Bancontact card in live Customer Area (`:458-491`).
