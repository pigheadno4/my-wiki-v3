---
title: "Adyen SEPA Direct Debit React Native Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/react-native-component/2026-09-15.md"
tags: [adyen, sepa-direct-debit, react-native, components, recurring]
---

## Overview

Adyen's 2026-09-15 SEPA Direct Debit React Native Component guide adds method-specific steps to an existing integration. This page explicitly says React Native Components do not support Sessions flow and documents only Advanced flow for this method. That page-specific statement does not erase the wrapper concept's general Sessions capability. See [[adyen]] and [[adyen-react-native-sdk]].

## Key takeaways

- The Advanced route requires an existing React Native Components integration, `action.type: direct` handling, and SEPA Direct Debit added in Customer Area. No SEPA-specific Component configuration is needed. The integration-type row says Components but its base-guide URL contains `integration=Drop-in`; the action and payment links point to Components, so the Drop-in URL should not be treated as evidence of a Drop-in prerequisite (raw lines 25-53).
- For `/payments`, the page marks `paymentMethod.sepa.ownerName` and `paymentMethod.sepa.ibanNumber` required and instructs merchants not to encrypt the IBAN. It requires billing street, house number/name, postal code, city and country for IBANs from its listed non-EEA SEPA countries or territories. The primary curl example uses Checkout TEST v72 but has no shell continuation after `-X POST`, leaving `-d` outside the command; it illustrates request fields and is not copy-ready shell (raw lines 65-85). Several initial-token language snippets omit the account fields despite the prose requirement, so they are incomplete field templates rather than evidence that those fields are optional; the Ruby example also uses dotted symbol keys (raw lines 53-85, 122-465).
- The response example is labeled successful and shows `resultCode: Received`; that example alone does not prove final debit or settlement (raw lines 87-95). If automatic capture is not used, the page requires delayed automatic capture or a manual `/payments/{paymentPspReference}/captures` request. It says authorizations do not expire and multiple partial captures require Support enablement (raw lines 97-106).
- The method-level [[source-adyen-docs-payment-methods-sepa-direct-debit]] requires a shopper-accepted mandate, including an active authorization action, before debiting, and notice at least one day before each debit (method overview raw lines 29, 37-61, 83-85). Those obligations are distinct from this Component page's strong recommendation to ask explicit permission for future recurring charges (component raw line 114).
- The page documents tokenization for `Subscription` and `UnscheduledCardOnFile` and directs initial token creation to standard tokenization parameters. Its examples headed “Create a SEPA token” omit `storePaymentMethod` (raw lines 118-145, 147-465); the related token-creation guide says to set it to `true` for first `/payments` token creation (token guide raw lines 441-451). These examples are incomplete tokenization templates; no runtime token outcome can be inferred. When a token is created, `recurring.token.created` supplies `storedPaymentMethodId`. Subsequent `/payments` examples pair the ID with `shopperReference`, `ContAuth`, and the applicable recurring model. Tokenized payments are scoped to shopper-absent scenarios (component raw lines 467-498, 778-805).
- The guide supplies test account/IBAN fixtures and points to test Customer Area for test status. Live SEPA acceptance requires a separate request in live Customer Area; the examples and fixtures do not establish live enablement (raw lines 1085-1097).

## Detail locators

- Component flow availability, Advanced prerequisites and no extra configuration: raw lines 25-53.
- Account and billing fields, request/response example, capture: raw lines 53-106.
- Method-level mandate and pre-debit notice: SEPA overview raw lines 29, 37-61, 83-85.
- Initial token creation and language examples, including missing `storePaymentMethod`: component raw lines 108-465; token guide raw lines 441-451.
- Token webhook, absent-shopper restriction and subscription examples: raw lines 467-776.
- Unscheduled card-on-file examples: raw lines 778-1083.
- Test fixtures and live request: raw lines 1085-1097.

## Related raw API references

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/2026-09-15|SEPA Direct Debit method overview (relevant mandate and notice passage read)]]
- [[raw/adyen/docs/online-payments/tokenization/create-tokens/2026-09-15|Create tokens guide (relevant `/payments` field table read)]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/react-native-component/2026-09-15|SEPA Direct Debit React Native Component (2026-09-15 snapshot)]]
