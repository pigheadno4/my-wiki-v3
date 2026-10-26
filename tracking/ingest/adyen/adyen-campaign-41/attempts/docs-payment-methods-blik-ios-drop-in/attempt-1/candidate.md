---
title: "Adyen BLIK iOS Drop-in guide"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/blik/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/blik/ios-drop-in/2026-09-15.md"
tags: [adyen, blik, ios, drop-in, oneclick, tokenization]
---

## Overview

This 2026-09-15 captured Adyen guide adds BLIK to an existing iOS Drop-in integration. It requires at least Drop-in v3.8.0, routes to a Sessions-flow base guide, gives separate `/sessions` and `/payments` material, and describes code payments plus BLIK OneClick consent and token notification. Its `Pending` response and waiting screen are intermediate; the `AUTHORISATION` webhook is the stated outcome signal. This guide does not prove current account eligibility, native callback behavior or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- The prerequisites are an existing iOS Drop-in integration at v3.8.0 or later and BLIK added in test Customer Area. The only linked base integration is iOS Drop-in Sessions. The `/sessions` tab says BLIK needs no extra fields or method-specific Drop-in configuration and calls `/sessions` the default for Drop-in v5.0.0 or later. The page does not document an Advanced base path or a Checkout API minimum; its v68 `/payments` URLs are examples. Code-payment live setup requires adding BLIK to live Customer Area.
- In the `/payments` material, code discovery uses `/paymentMethods` with PL, PLN and minor-unit amount; the text says a shopper previously signed up for OneClick may also receive `storedPaymentMethods.type: blik`. The code request names `paymentMethod.type: blik` and the six-digit `paymentMethod.blikCode`. It illustrates `resultCode: Pending` and an `await` action, then instructs a waiting screen while the shopper confirms in the BLIK app. `Pending` is not final authorization. The page lists `Refused` for an incorrect code and says the `AUTHORISATION` webhook's `success` field gives the completed/failed outcome.
- Despite the iOS Drop-in title and statement that no BLIK-specific Drop-in configuration is needed, the `/payments` section tells the merchant to show BLIK and a code-entry field, and after a webhook says to redirect the shopper to a website. These are generic website-oriented instructions embedded in the native guide; they do not establish an iOS Drop-in callback or mandate a separate merchant-built code field for the Drop-in path. Its result heading also says to use the initial `/payments` `resultCode`, while the same section says to wait for webhooks to know the outcome.
- The OneClick section asks for `shopperReference` in discovery and says to include the stored method's `label` so the shopper recognizes the issuer. Its `/payments` text repeats a `blikCode` and adds `shopperReference`, `storePaymentMethod: true` and `recurringProcessingModel: CardOnFile` to request consent for later no-code payments. If consent is given, it says a `recurring.token.created` webhook carries `storedPaymentMethodId`, `eventId` and `shopperReference`; the Recurring tokens life cycle webhook must be enabled. This documents a consent/token-creation path, not a complete later no-code `/payments` request or permission for arbitrary recurring charges. The BLIK overview table marks recurring unsupported; that mark and this narrower OneClick token flow should remain distinguished, not flattened into general recurring support.
- The OneClick curl body is malformed: it quotes `storePaymentMethod` as a string and omits a comma after `recurringProcessingModel`. The label prose names `additionalData.BLIK.APP_LABEL`, while the sample uses `Blik.APP_LABEL` and an example expiration dated before this captured page. Resolve exact field casing and request types against the relevant API authority. The guide's code-payment test uses code `999000`; its OneClick live section additionally says to seek BLIK certification/enablement and add BLIK in live Customer Area. These examples and instructions do not prove an executed test, certification or live enablement.

## Detail locators

- iOS Drop-in v3.8.0, test setup, no configuration, `/sessions` and v5.0.0 default: pinned raw lines 15–52.
- Code discovery and `/payments` fields/examples: pinned raw lines 54–387; `Pending`/`await` response and waiting/webhook/result sections: lines 389–443.
- OneClick discovery, label, consent fields and malformed curl example: pinned raw lines 447–492.
- OneClick response and webhook outcome: pinned raw lines 494–536; token webhook and app-label prose/example mismatch: lines 538–559.
- OneClick test and certification/live steps: pinned raw lines 561–574.

## Related

- [[adyen-online-payments]] — main provider online-payment concept
- [[adyen-tokenization]] — provider token lifecycle concept; OneClick scope remains source-qualified
- [[source-adyen-docs-payment-methods-blik]] — BLIK overview and historical capability marks

## Raw Sources

- [[raw/adyen/docs/payment-methods/blik/ios-drop-in/2026-09-15|BLIK iOS Drop-in guide, 2026-09-15]]
