---
title: "Adyen Alipay+ iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay-plus/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay-plus/ios-drop-in/2026-09-15.md"
tags: [adyen, alipay-plus, ios, drop-in, wallets, redirect]
---

## Overview

This 2026-09-15 Adyen guide adds Alipay+ to an existing iOS Drop-in integration in Sessions or Advanced flow. It specifies method-specific setup, Advanced redirect handling and a no-TEST-environment/live-testing boundary. It does not establish underlying-wallet eligibility, current merchant enablement or a completed payment. See [[adyen]], [[adyen-ios-sdk]] and [[source-adyen-docs-payment-methods-alipay-plus]] for the separately qualified network overview.

## Key takeaways

- Sessions requires an existing iOS Drop-in Sessions integration, Checkout API v68 or later, and Alipay+ added in Customer Area. The page specifies no extra method fields for the base `/sessions` request and no additional Alipay+ Drop-in configuration. Advanced requires an existing iOS Drop-in Advanced integration, redirect handling for `action.type: redirect`, and Customer Area setup; it specifies no extra method fields for the base `/payments` request or extra configuration. The v68+ prerequisite is stated in the Sessions section only.
- The guide states **no test environment for Alipay+**. It recommends live penny tests using an Alipay+ wallet app configured with a credit or debit card, then viewing payment details in the live Customer Area. This is a recommendation for actual live-value activity, not a TEST fixture or proof of authorization, capture or settlement; no such activity was performed for this source.
- **Setup-label conflict:** both requirements rows say to add **Alipay+**, while the live-enable sentence says to submit a request for **Alipay** in the live Customer Area. The page does not resolve whether that Alipay request enables Alipay+ or any specific underlying wallet. Confirm the requested method and wallet coverage with the provider before relying on the wording. The Alipay+ overview separately describes wallet-by-wallet onboarding review, so one guide's method label does not imply universal wallet approval.
- The page has no method-specific return/result or webhook procedure. Base integration and wallet-specific outcome handling remain separate authority; redirect setup and shopper return are not final payment evidence.

## Detail locators

- Sessions prerequisites, no-extra-fields `/sessions`, no extra configuration: pinned raw lines 25–46.
- Sessions no-TEST/live-penny recommendation and Alipay versus Alipay+ live-request label: pinned raw lines 48–60.
- Advanced prerequisites and redirect handling, no extra configuration/base `/payments` fields: pinned raw lines 62–84.
- Advanced repeated no-TEST/live-penny and live-request wording: pinned raw lines 86–98.

## Related

- [[adyen-ios-sdk]] — native Drop-in and merchant-server boundaries
- [[source-adyen-docs-payment-methods-alipay-plus]] — network scope and separate underlying-wallet onboarding review
- [[adyen-online-payments]] — Sessions/Advanced and redirect lifecycle context

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay-plus/ios-drop-in/2026-09-15|Alipay+ iOS Drop-in guide, 2026-09-15]]
