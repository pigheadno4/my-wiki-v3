---
title: "Adyen Docs: Migrate to Checkout API"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/2026-09-15.md"
tags: [adyen, online-payments, checkout-api, classic-api, migration]
---

## Overview

This Adyen guide, last modified 2025-07-02 and captured 2026-09-15, explains migration from Classic API to Checkout API for online payments. Adyen says Classic API is no longer developed or updated and recommends Checkout API. The guide's main path targets Checkout API **v72 or later**. It also describes a narrower Classic v68 → Checkout v68 interim route that may require another upgrade if deprecated. This is historical documentation, not proof of current API availability or a successful merchant migration. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- Migration changes authentication, authorization, and modification requests. The task list depends on the existing integration: server-only needs credential, endpoint, and request-object changes; CSE/JWE, 3D Secure, tokenization, local methods, SOAP, and partner integrations add their own work. The existing Classic integration may continue processing live payments during migration. See raw lines 28–39, 58–73, and 75–83.
- The Checkout credential needs the **Checkout webservice role**; configure desired additional response data in Customer Area. API keys or basic authentication still authorize server API requests. Drop-in/Components additionally require a client key and allowed origins. Checkout requests require JSON; XML request objects must be converted. See raw lines 85–100, 148–156, and 3221–3229.
- The endpoint table maps Classic `/authorise` to Checkout `/payments`, post-3DS/redirect details to `/payments/details`, and refund, cancellation, capture, reversal, and amount adjustment to payment-reference routes. It gives separate `/cancels` for cancellation without a PSP reference, plus session and stored-method routes. **Voiding a pending refund has no Checkout API counterpart in this table.** Base URLs, environment, live prefix and region matter. See raw lines 102–146 and operation examples at 2349–2614.
- Card request shape changes from Classic encrypted-card `additionalData` to Checkout `paymentMethod`; unencrypted card handling requires PCI compliance. Checkout token requests specify `shopperInteraction` and `recurringProcessingModel` rather than relying on Customer Area's Recurring toggle, and token lifecycle setup includes a tokenization webhook. See raw lines 160–307, 307–914, and 3143–3169.
- `/payments` can return an `action` requiring voucher, QR, redirect, await, SDK, or 3DS handling. Voucher/QR/await/SDK examples wait for a webhook result; redirect return data can be submitted server-side to `/payments/details`, while a shopper who does not return is resolved via webhook. The `/payments/details` sample reports a **current status**, not a general guarantee that every action completed. See raw lines 2747–2763 and 2764–3123.
- Classic CSE does not work with Checkout API; the guide offers Card Component, Custom Card Component, and JWE replacements. Standard v1 webhooks are described as unchanged, but SOAP webhook format, tokenization webhooks, or differently structured AUTHORISATION notifications can still need migration checks. PCI scope depends on integration type; the guide says API-only to API-only with a custom interface has no PCI impact and Components can lower scope. See raw lines 3199–3239.

## Important qualifications and source tensions

- The base-URL table gives Checkout test as `https://checkout-test.adyen.com/checkout/{VERSION}` (raw 108–111), whereas the guide's Checkout curl examples use `https://checkout-test.adyen.com/v72/...` (for example raw 1773–1776 and 2383–2387). Verify an actual endpoint path for the chosen API version and environment; do not combine those patterns as if internally consistent.
- The redirect walkthrough says to send `redirectResult` to `/payments/details` (raw 2906–2919), while the later v67+ authentication note says authorization occurs before redirect back and `/payments/details` is no longer needed **to authorize** (raw 3129–3133). Keep the distinction between retrieving/confirming a result and performing authorization; the guide does not fully reconcile the wording.
- The guide's opening says webhooks do not change (raw 34–39), narrowed later to standard v1 webhooks with exceptions for SOAP, tokenization, and differing AUTHORISATION structure (raw 3211–3219). Its examples are historical illustrations, not validated runnable code: the Classic redirect 3DS JSON lacks a comma after `browserInfo` (raw 1752–1764), the Classic reversal sample URL says `captureOrRefund` while prose links `cancelOrRefund` (raw 2511–2516), and some library samples omit request-object construction (raw 2938–3107).

## Detail locators

- Feature matrix, scoped task matrix, interim version and Sessions trade-off: raw lines 41–83.
- Credential, URL, endpoint, request-format and card-field mappings: raw lines 85–307.
- Stored-card creation and one-off/subscription examples: raw lines 307–914.
- Native and redirect 3DS examples, including language-specific SDK snippets: raw lines 915–2347.
- Modification examples and third-party 3DS data: raw lines 2349–2741.
- Additional actions, redirect return, webhook and status examples: raw lines 2747–3123.
- Auth, tokenization, wallets/local methods, CSE, webhooks, security, PCI and enhanced-scheme migration: raw lines 3125–3250. Google Pay requires v67+ in this guide; v71+ moves enhanced scheme data to root `enhancedSchemeData` (raw 3174–3182, 3240–3250).
- Performance recommendations, errors, libraries, testing and live coexistence/go-live: raw lines 3252–3295.

## Related

- [[adyen-online-payments]] — Adyen online payment architecture and source routes.
- [[source-adyen-docs-online-payments-upgrade-your-integration-migrate-to-checkout-api-upgrade-api-library]] — separate, version-qualified Java API library migration guide.

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/2026-09-15|Migrate to Checkout API, 2026-09-15 capture]]
