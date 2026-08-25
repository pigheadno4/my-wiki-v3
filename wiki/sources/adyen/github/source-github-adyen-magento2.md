---
title: "GitHub: Adyen/adyen-magento2"
type: source
date_ingested: 2026-08-25
original_format: github-repo
raw_files:
  - "github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/manifest.json"
tags: [adyen, adobe-commerce, magento2, checkout, webhooks, pos, vault, github-repository]
---

## Overview

`Adyen/adyen-magento2` is Adyen's payment plugin for Adobe Commerce. This cumulative page begins with package-qualified release `adyen/module-payment@11.0.0` at exact SHA `4206983499d829ef695185ac78af06b9bdfe96c6`, covering storefront and headless checkout, payment modifications, stored methods, webhooks, POS Cloud, gift cards, and donations.

Repository: <https://github.com/Adyen/adyen-magento2>

## Evidence boundary

- The 528-file snapshot is immutable; 206 reviewed paths form the routine ingest capsule. Other retained files remain available for a focused query or approved supplement.
- The source proves implementation at `adyen/module-payment@11.0.0`. It does not prove merchant enablement, payment-method availability, geography, account configuration, or current support policy.
- The plugin depends on independently versioned Adyen Web and PHP API libraries. Their delegated behavior must be checked against their own package histories.
- Tests were excluded by collection policy. Configuration, schemas, storefront templates, JavaScript, PHP implementation, and release evidence were retained.

## Grounding excerpts

> "The plugin integrates card component (Secured Fields) using Adyen Checkout for all card payments."
>
> `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/README.md:4-5`

> "This plugin is compatible with Magento version 2.4.8 only."
>
> `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/README.md:15-16`

> "Make sure that your Magento cron is running every minute."
>
> `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/README.md:76-77`

> "Current Checkout API version: v71"
>
> `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/release-notes.md:22`

> "Current Checkout Component version: 6.35.0"
>
> `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/release-notes.md:23`

## Compatibility and installation

The Composer package is `adyen/module-payment@11.0.0`. It supports Magento 2.4.8 only and requires PHP 8.2, 8.3, 8.4, or 8.5; Magento Framework `>=103.0.8`; Vault `>=101.2.8`; and `adyen/php-api-library ^29.0.0`. Installation enables `Adyen_Payment` and runs Magento setup upgrade.

The plugin uses Checkout API v71 and bundles Adyen Checkout Components 6.35.0. These versions differ from independently retained Adyen client and server repositories and should not be silently substituted when answering version-specific questions.

## Payment-method discovery and presentation

The payment-method request is assembled from trusted quote amount and currency plus merchant account, country, locale, shopper reference, shopper interaction, and channel (`Web`, `iOS`, or `Android`). The response is filtered, sorted, and enriched with stored methods before Magento renders cards or generic method Components.

The retained storefront supports cards and stored cards, Apple Pay, Google Pay, PayPal through Adyen, Cash App Pay, Amazon Pay, Affirm, Boleto, Ratepay, Facilypay, gift cards, generic redirect or Component methods, multishipping, Pay by Link, and POS Cloud. Presence in code is an adapter capability, not proof that a method will be returned for a merchant and shopper.

## Headful and headless checkout

The standard checkout retrieves methods, places the Magento order, sends `/payments`, persists response data required for follow-up actions, and submits `/payments/details`. Version 11.0.0 returns structured refusal and error information from details handling instead of collapsing those outcomes into an unstructured failure.

REST and GraphQL APIs expose payment-method retrieval, state data, additional-details submission, payment-status checks, gift-card operations, POS Cloud, and token deactivation for guest and authenticated carts. Guest routes resolve masked IDs; customer routes verify cart or order ownership. A custom headless frontend remains responsible for securely collecting shopper details, rendering methods, invoking backend endpoints, handling actions, and deciding how to present status.

## Modifications and order state

Capture, refund, and cancel clients build Checkout modification requests with deterministic idempotency hashes. The plugin supports automatic and manual capture, partial or multiple captures, and refund handling against payment, capture, or order references. Invoice, credit-memo, and order helpers coordinate Magento totals and statuses with Adyen responses.

Authorization is not always final order completion. In manual-capture flows, asynchronous capture webhooks update payment and order state. Version 11.0.0 corrects partial-payment invoicing and order-status consistency, refactors capture-mode resolution, improves authorized-amount comparison, and stops duplicating `cc_type` into payment `additional_information`.

## Gift cards, POS, and Giving

Gift-card balance and payment flows support partial payment and multiple gift cards, with remaining order amount reflected in checkout totals. POS Cloud lets checkout select a terminal, funding source, and installments before sending a Terminal API payment request. Giving retrieves donation campaigns and submits donations after the underlying payment flow, with retry handling for failed donation requests.

These are distinct lifecycles. A gift-card balance, terminal response, or donation response must not be generalized into card-not-present payment completion.

## Vault and recurring credentials

Vault builders and method renderers support `CardOnFile`, `Subscription`, and `UnscheduledCardOnFile`. The plugin creates Magento payment tokens from Adyen recurring details and can disable a token both locally and through Adyen's recurring API. Recurring-contract and token-created webhooks reconcile later token events.

Vault and Instant Purchase require configured recurring-detail response fields. Repository support does not establish shopper consent, merchant eligibility, or correct recurring-use classification for a specific payment.

## Webhooks, validation, and cron

The webhook acceptor validates event payloads and live/test context, while the delegated webhook module handles HMAC verification. Accepted notifications are persisted and processed asynchronously by the `adyen_payment` cron group. Handlers cover authorization, capture, refund, recurring contracts, and recurring-token creation, and processing records failures for retries or investigation.

The README requires Magento cron every minute. Notification processing deliberately waits until records are at least two minutes old so Magento order persistence and save events can finish. Separate jobs clean state data, processed webhook rows, expired orders, server IP data, and, in 11.0.0, stale `adyen_payment_response` rows.

## `11.0.0` release findings

Release `11.0.0` is a major boundary from `10.10.3`. It enables the NEA region, upgrades Checkout Components to 6.35.0 and the PHP API Library dependency to v29, adds stale payment-response cleanup, and fixes partial-payment invoice and order-state consistency. It also includes breaking or contract-sensitive changes to additional information, payment-method sorting/filtering, `/payments/details` failures, authorized amount comparison, and capture-mode lookup.

This is the first retained exact-SHA baseline. Architecture described above is cumulative behavior present at 11.0.0 and must not be described as introduced by this release unless the release notes say so.

> [!warning] Source-code caveat
> `buildCheckoutComponent` declares callbacks for additional details, submit, and error, but the generic payment-method renderer passes an additional cancel callback before submit and error. JavaScript ignores the sixth argument, so the initial checkout configuration appears to misalign these callbacks. Component-level configuration may override them later, and no retained tests or runtime proof establish shopper impact. Treat this as a code-review concern requiring upstream or runtime verification, not a confirmed production failure.

The release notes also say the unused `supports_auto_capture` flag was removed, while retained configuration still contains the flag for `adyen_iris`. This may be a method-specific exception or incomplete cleanup; do not generalize the release-note statement to every method without focused verification.

## Related

- [[changelog-github-adyen-magento2]] - package-qualified release ledger
- [[adyen-magento2]] - plugin architecture and query boundary
- [[adyen-php-api-library]] - independently versioned server dependency
- [[adyen-terminal-api]] - in-person Terminal API concepts
- [[recurring-payments]] - recurring and stored-credential concepts
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/manifest.json`
- Release manifest: `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/manifest.json`
- Release notes: `raw/github/adyen/adyen-magento2/releases/module-payment/11.0.0/2026-08-25/release-notes.md`
- README: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/README.md`
- Composer metadata: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/composer.json`
- Checkout configuration: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/etc/config.xml`
- REST routes: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/etc/webapi.xml`
- GraphQL schema: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/etc/schema.graphqls`
- Standard webhook acceptor: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/Model/Webhook/StandardWebhookAcceptor.php`
- Checkout builder: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/view/frontend/web/js/model/adyen-checkout.js`
- Generic payment renderer: `raw/github/adyen/adyen-magento2/snapshots/2026-08-25-4206983/files/view/frontend/web/js/view/payment/method-renderer/adyen-pm-method.js`
