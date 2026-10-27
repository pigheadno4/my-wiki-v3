---
title: "Adyen ACH Direct Debit iOS Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/ach-direct-debit/ios-component"
raw_files:
  - "adyen/docs/payment-methods/ach-direct-debit/ios-component/2026-09-15.md"
tags: [adyen, ach-direct-debit, ios, components, sessions, advanced-flow, bank-debit]
---

## Overview

This 2026-09-15 Adyen guide adds ACH Direct Debit to an **existing iOS Components** integration, with separate Sessions and Advanced server-side instructions. It gives method-specific prerequisites, `ACHDirectDebitComponent` initialization and test values, and states that no additional ACH-specific `/sessions` or `/payments` parameters are needed (raw lines 44, 137). It does not specify an iOS SDK version, a complete payment-result lifecycle or current merchant eligibility. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-ach-direct-debit]].

## Key takeaways

- **Sessions:** Requires an existing iOS Components Sessions integration, **Checkout API v68 or later**, ACH added in Customer Area, and subscription to `DIRECT_DEBIT_NOTICE_OF_CHANGE_NOTIFICATION` to learn of outdated shopper bank details. It says no ACH-specific `/sessions` parameters or extra component configuration are needed. The `Merchant allow bank-refund` role listed alongside these requirements is explicitly conditional on **issuing a refund** through API or Customer Area, not a stated prerequisite for taking an ACH payment. (raw lines 25–50)
- **Advanced:** Requires an existing Advanced iOS Components integration, the same change-notice webhook and ACH Customer Area setup. It also says no extra ACH configuration or `/payments` parameters are needed. The **Advanced Components** prerequisite label links to an `integration=Drop-in` URL, while the later payment link points to Components; verify the correct base guide. This section does not state the Sessions-only v68 minimum for Advanced. (raw lines 92–137)
- **Native component:** Both flows name `ACHDirectDebitComponent`. The Sessions sample checks for `ACHDirectDebitPaymentMethod`, constructs the component, sets its delegate to the session and presents the view controller; Advanced similarly sets the delegate to `self`. Both Swift snippets leave `configuration:` without a value and are not copy-ready. This incomplete placeholder does not override the page's statement that no **additional ACH-specific** configuration is needed. (raw lines 52–72, 112–131)
- **Outcome and method duties:** This page does not state an ACH authorization, capture, settlement or refund outcome procedure. Its change-notice webhook serves **outdated banking details**, not payment success. The related ACH overview records non-real-time bank authorization, US-entity eligibility, consumer account validation, B2B allowlisting, signed mandate/SEC obligations, returns and settled-only refund conditions. Thus no-extra-method-fields and a presented component do not establish a valid authorization, verified account, approved merchant or settled funds. (raw lines 37, 44, 103, 137; [[source-adyen-docs-payment-methods-ach-direct-debit]])
- **Testing:** For test payments, the page allows any owner name and correctly formatted account/routing numbers. For a test return, it says to prefix `ownerName` with `chargeback:` and an ACH reason code, for example `chargeback:R01`. These are test cases, not proof of live payment or bank-account validation. A separate live activation procedure is not described here. (raw lines 74–90, 139–155)

## Detail locators

- Sessions prerequisites, conditional refund permissions, change-notice webhook and v68+ minimum: pinned raw lines 25–38.
- Sessions no-extra-fields/configuration and incomplete Swift initialization sample: pinned raw lines 40–72.
- Sessions test account/routing and chargeback trigger: pinned raw lines 74–90.
- Advanced prerequisite link mismatch, roles, webhook and setup: pinned raw lines 92–104.
- Advanced no-extra-config/request fields and incomplete Swift initialization sample: pinned raw lines 106–137.
- Repeated Advanced test values and related links: pinned raw lines 139–161.
- ACH method-level eligibility, mandates/SEC, bank authorization, returns and refunds: [[source-adyen-docs-payment-methods-ach-direct-debit]].

## Related

- [[adyen-online-payments]] — online bank-debit integration context
- [[adyen-ios-sdk]] — wider iOS SDK context, separate from this method guide
- [[source-adyen-docs-payment-methods-ach-direct-debit]] — ACH bank-account, authorization, mandate, return and refund context
- [[adyen]] — provider

## Raw Sources

- [[raw/adyen/docs/payment-methods/ach-direct-debit/ios-component/2026-09-15|ACH Direct Debit iOS Component, 2026-09-15]]
