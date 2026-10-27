---
title: "Adyen SEPA Direct Debit iOS integration routes"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/sepa-direct-debit/ios"
raw_files:
  - "adyen/docs/payment-methods/sepa-direct-debit/ios/2026-09-15.md"
tags: [adyen, sepa-direct-debit, ios, drop-in, components, integration-routes]
---

## Overview

This 2026-09-15 Adyen page is a **route selector** for adding SEPA Direct Debit to an iOS app. It links the method-specific **Drop-in** and **Components** guides and four main iOS integration routes: Sessions/Advanced × Drop-in/Components. It supplies no request schema, SDK or Checkout API minimum, mandate process, payment response, capture or settlement outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Method guide choices:** Drop-in is described as Adyen's all-in-one UI route. Components points to a `SEPADirectDebitComponent` guide. These labels identify distinct iOS implementation choices, not interchangeable flows or verified account eligibility. (raw lines 19–27)
- **Base before add-on:** The page instructs readers to create the main integration first. It links iOS Drop-in with Sessions, iOS Components with Sessions, iOS Drop-in with Advanced, and iOS Components with Advanced. The linked child method guides own implementation requirements and outcomes; this chooser does not establish any of them. (raw lines 29–36)
- **Scope limit:** This captured route selector does not prove a shopper mandate, SEPA debit authorization, settled funds, current merchant enablement or a successful live payment. For method-level mandate, notice, refund and chargeback context, consult [[source-adyen-docs-payment-methods-sepa-direct-debit]]; for channel-specific request steps use the selected iOS child guide. (raw lines 15–36)

## Detail locators

- iOS SEPA identity and Drop-in/Components routes: pinned raw lines 15–27.
- Main integration prerequisite and four Sessions/Advanced route links: pinned raw lines 29–36.

## Related

- [[source-adyen-docs-payment-methods-sepa-direct-debit-ios-drop-in]] — iOS Drop-in add-on
- [[source-adyen-docs-payment-methods-sepa-direct-debit-ios-component]] — iOS Components add-on
- [[source-adyen-docs-payment-methods-sepa-direct-debit]] — method-level risks and obligations
- [[adyen-online-payments]] — provider integration context
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/sepa-direct-debit/ios/2026-09-15|SEPA Direct Debit iOS route selector, 2026-09-15]]
