---
title: "Bancontact card iOS Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/ios-drop-in/2026-09-15.md"
tags: [adyen, bancontact, card, ios, drop-in, 3d-secure, tokenization]
---

## Overview

This 2026-09-15 guide adds **Bancontact card** to an existing **iOS Drop-in** Sessions or Advanced integration. It describes card/3DS differences, method-specific no-extra-field/configuration scope, WIP-gated recurring tokens and TEST/live gates. It is distinct from Bancontact mobile app/QR acceptance and is not proof of enabled live processing or a successful payment. [[adyen]] [[adyen-online-payments]] [[adyen-ios-sdk]]

## Key takeaways

- **Card/3DS:** Bancontact card lacks CVC, though a co-badged card may display a CVC field. **3D Secure is mandatory**, and separate captures are not supported. iOS Drop-in securely collects card details and redirects to the issuer website for 3DS. These card statements do not describe Bancontact mobile wallet handoff. See raw lines 19–25 and [[source-adyen-docs-payment-methods-bancontact]].
- **Flow/version:** start with matching iOS Drop-in Sessions or Advanced integration and add Bancontact card in Customer Area. The page says no **Bancontact-card-specific** additional fields on `/sessions` or `/payments`; `/sessions` is called the default for Drop-in **v5.0.0+**, with `/payments` for an additional use case. Both v5.0.0+ and v4.x.x tabs say no required card-specific Drop-in configuration. This does not waive base-flow fields, 3DS handling or merchant setup. See raw lines 27–60.
- **Recurring WIP gate:** the page recommends explicit shopper permission and says recurring goes through **Bancontact Wallet Initiated Program**. WIP needs signup/Support enablement, excludes some companies and has transaction amount limits. Its described first transaction includes shopper SCA/consent; later WIP transactions do not need SCA, and the issuer remains liable (the page says no liability shift). Do not read the tokenization statement as universal Bancontact recurring availability. See raw lines 62–81. [[adyen-tokenization]]
- **Token lifecycle:** create an initial token with `storePaymentMethod=true` and a shopper reference (at least three characters) on `/sessions` or `/payments`; after **settlement** the `recurring.token.created` lifecycle webhook supplies `storedPaymentMethodId`. A later server `/payments` uses `paymentMethod.storedPaymentMethodId`, matching shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`; the sample uses `type=bcmc` and EUR. Support configures recurring TEST. See raw lines 83–119 and 121–456.
- **TEST/live:** the BCMC/Visa co-badged test card can route to **Bancontact or Visa depending on payment-method setup**; `holderName=DECLINED` simulates refusal. TEST results are inspectable in test Customer Area. Live acceptance requires adding Bancontact card in live Customer Area. Test fixtures and example token IDs do not demonstrate a real authorization, routing or settlement. See raw lines 458–491.

## Detail locators

- Card/CVC/3DS/capture scope and iOS issuer redirect: raw lines 15–25.
- Sessions/Advanced setup, v5 default and no-extra-method-fields/config: raw lines 27–60.
- WIP permission, eligibility, amount, SCA and liability qualifications: raw lines 62–81.
- Token creation after settlement and future `/payments` fields/examples: raw lines 83–456.
- Co-badged TEST routing, decline fixture and live gate: raw lines 458–491.

## Related

- [[adyen-online-payments]] — Bancontact card payment route.
- [[adyen-ios-sdk]] — iOS Drop-in/3DS handoff context.
- [[adyen-tokenization]] — WIP-gated recurring token lifecycle.
- [[source-adyen-docs-payment-methods-bancontact]] — card/mobile overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/ios-drop-in/2026-09-15|Bancontact card iOS Drop-in, captured 2026-09-15]]
