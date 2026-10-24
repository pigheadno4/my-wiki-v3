---
title: "Adyen MoMo Wallet Web Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/momo-wallet/web-component"
raw_files:
  - "adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15.md"
tags: [adyen, momo, wallet, web, components, recurring-payments]
---

## Overview

This 2026-09-15 Adyen page describes MoMo-specific additions to an **existing Web Components** integration, with separate Sessions and Advanced server-side flows. It uses a redirect Component for the base payment path and describes an optional recurring-token path. The page is supplemental to the main integration guides; it does not establish current MoMo merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Sessions requires an existing Web Components Sessions flow, Checkout API v68 or later, `action.type: redirect` handling and MoMo added in Customer Area. Advanced requires an existing Web Components Advanced flow, redirect handling and the Customer Area addition; this page states no distinct Advanced API minimum. Both import `Redirect` from Adyen Web, say no MoMo-specific configuration parameters are needed, and say no extra base `/sessions` or `/payments` fields are needed. The normal main-flow request, redirect-return and outcome duties still apply.
- Both flow examples initialize `Redirect` with a `momo_wallet` type and mount it to a container. The JavaScript snippet renders `type:momo_wallet` without quotes or a defined variable, so it is not a self-contained, copy-ready example; check the actual method type and selected Adyen Web version before implementation. No Adyen Web version is specified on this page.
- **Recurring is an explicit exception to the no-extra-base-fields text.** For token creation, the guide requires `storePaymentMethod: true` and a unique `shopperReference` in `/payments`, plus a server able to receive Recurring tokens lifecycle events. It says `recurring.token.created` is sent after the initial payment has settled and carries `storedPaymentMethodId`. A later `/payments` request uses that ID, the same shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed intervals. The page does not spell out a shopper consent UI or assert that a token request itself proves settlement or a later charge.
- The recurring examples use TEST clients/endpoints and VND amounts; they are illustrative, not a general currency or country eligibility rule. The Java example calls `setRecurringDetailReference` with the token even though the prose and other examples call for `storedPaymentMethodId`, and its amount is VND 15000 while neighboring examples use VND 1000. Verify the chosen API/library version and field mapping before using the snippets.
- In TEST, the guide directs a mobile-browser shopper to a MoMo test-app download link and a desktop-browser shopper to scan a QR code with the test app, using MoMo-provided test credentials for the chosen scenario. Test payment status can be checked in the test Customer Area. Before accepting LIVE MoMo payments, it says to request MoMo in the live Customer Area. Download, QR scan, redirect, token webhook or request acceptance alone does not prove final authorization, capture, settlement or refund; this page supplies no separate final-outcome procedure.

## Detail locators

- Page identity and Sessions/Advanced selection: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 15–23.
- Sessions prerequisites, no extra base request/configuration, Redirect import and initializer snippet: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 25–72.
- Sessions recurring token creation, post-settlement webhook and later token-request fields: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 74–111.
- Sessions TEST/VND examples including Java token-field and amount discrepancies: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 113–310.
- TEST app/QR/credential paths and live Customer Area request: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 312–321, repeated at 601–610.
- Advanced prerequisites, Redirect import/init, no extra base `/payments` fields and recurring route: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 323–400.
- Advanced TEST/VND recurring examples and Java discrepancy: [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|MoMo Web Component raw]], lines 402–599.

## Related

- [[adyen-online-payments]] — Web Components, server flow and outcome context.
- [[adyen-tokenization]] — stored-method lifecycle and consent context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/momo-wallet/web-component/2026-09-15|Adyen MoMo Web Component guide (2026-09-15 snapshot)]]
