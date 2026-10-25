---
title: "FPX Online Banking Malaysia React Native Component | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/react-native-component/2026-09-15.md"
tags: [adyen, fpx, malaysia, react-native, components, redirect]
---

## Overview

This [[adyen]] page is the FPX Online Banking Malaysia add-on for an existing **React Native Components Advanced-flow** integration. It explicitly says React Native Components do **not** support Sessions flow. The method-specific page requires redirect handling and Customer Area setup, but supplies no issuer list or final payment-result contract. See [[adyen-online-payments]] and [[adyen-react-native-sdk]]. The separate [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia|FPX overview]] carries the MY/MYR method and asynchronous outcome context.

## Key takeaways

- **Only the Advanced Component route is described:** The Sessions section is marked unavailable. Advanced requires an existing React Native Components integration, handling `action.type: redirect`, and FPX Online Banking Malaysia added in Customer Area. Its prerequisite label and linked URL disagree about Components versus Drop-in; see the warning below. See raw lines 25–41.
- **Method-specific additions:** The page states no FPX-specific Component configuration parameters and no additional `/payments` parameters for the existing Advanced flow. These are scoped add-on statements; the merchant still needs the base integration's ordinary server request and redirect/result handling. See raw lines 43–53.
- **Test/live scope:** It instructs testing with an issuer ID available to the Online Banking Malaysia Component for the relevant country/region, checking test payments in Customer Area, and submitting a request for Online Banking Malaysia in the live Customer Area before live acceptance. It does not list issuer IDs or demonstrate a completed payment. See raw lines 55–61.

> [!warning] Components/Drop-in link mismatch
> The Advanced prerequisite calls for **React Native Components**, but its main-guide URL contains `integration=Drop-in`; the adjacent redirect and payment links contain `integration=Components`. The page does not reconcile this navigation conflict. Use the stated Advanced Components scope, and verify the intended base guide before implementation. See raw lines 39–40 and 53.

## Detail locators

- Sessions unsupported: raw lines 25–29. Advanced requirements: raw lines 31–41.
- No method-specific configuration or `/payments` additions: raw lines 43–53.
- Test issuer-ID wording, test-payment Customer Area route and live request gate: raw lines 55–61. The page does not provide a React Native SDK version, API minimum, issuer-ID values, callback implementation or final webhook status procedure.

## Related

- [[adyen-online-payments]] — main integration architecture and source route.
- [[adyen-react-native-sdk]] — version-qualified React Native wrapper context, separate from this unversioned method guide.
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]] — method-level MY/MYR and asynchronous-result overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/react-native-component/2026-09-15|FPX React Native Component, 2026-09-15 snapshot]]
