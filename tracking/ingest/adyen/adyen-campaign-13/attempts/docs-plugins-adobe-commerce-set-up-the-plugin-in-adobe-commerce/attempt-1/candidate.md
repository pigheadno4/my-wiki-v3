---
title: "Adyen Adobe Commerce plugin installation and configuration"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/2026-09-15.md"
tags: [adyen, adobe-commerce, magento2, plugin, installation, webhooks]
---

## Overview

This 2024-last-modified, 2026-09-15-captured Adyen guide describes installing `adyen/module-payment` in Adobe Commerce, running background processing, configuring test/live credentials and order management, then proceeding to payment-method and go-live guides. It is a **procedure**, not evidence a particular store ran it or that a payment, order, capture, refund or settlement succeeded. Check the exact package/version compatibility against [[adyen-magento2]] and [[source-github-adyen-magento2]]; this page's unpinned Composer commands must not be treated as an installed `11.0.0` record. See [[adyen]].

## Key takeaways

- **Installation and cache:** The guide assumes Composer in the Adobe Commerce folder, then lists `composer require adyen/module-payment`, enabling `Adyen_Payment`, running `bin/magento setup:upgrade`, and flushing cache. If a cache layer such as Varnish is used, `/adyen/process/*` must be excluded from caching. These are operational changes, including setup scripts, and were **not executed** by this ingest. The optional `adyen/adyen-magento2-expresscheckout` module requires Adobe Commerce 2.4.4+ and Adyen plugin 8.8.0+ per this dated guide, followed by its own enable/upgrade/cache steps; actual compatibility must be checked for the selected package releases.
- **Background processing and cleanup:** Server cron is required for webhooks, cache updates and unfinished-order closure; the page says `adyen_payment` cron generation interval is one minute. RabbitMQ is an optional webhook-processing alternative once queueing and Commerce's **Webhook processor = Queue** are configured. Optional payment-response cleanup is disabled by default and, if enabled, removes `adyen_payment_response` rows for cancelled, complete or closed orders at midnight **server time**. Enabling it changes retained state; none of these settings proves webhooks were processed.
- **Initial configuration and destructive reconfiguration:** Adyen Customer Area setup is a prerequisite. Automated setup is available for plugin 8.4.0+ and uses an API key to configure settings; **reconfiguring** with it loses the older configuration. Manual setup is available for all plugin versions and requires separately generating/configuring credentials. Both choose test or live environment and merchant account; the automated table says the client key and webhook Basic-auth credentials are fetched/generated, whereas the manual table requests API/client keys, webhook Basic-auth username/password and HMAC key. Do not mix test and live credentials. The manual table appears internally inconsistent: it describes the **Client key** as an “API key” and the **Webhook Password** as a “username.” Verify credential identities against the linked Customer Area setup guide before applying them.
- **Region, currency and order settings:** In manual setup, the Front-end Resource Region must match the live endpoint region; the guide mentions NEA from v11.0.0 for Japan. **Charged Currency** defaults to display currency, with a base/global/website alternative that can only be changed outside the UI. Capture Delay should match Adyen Customer Area's manual or automatic setting; open-invoice methods, PayPal manual capture and SEPA have their own settings/Support conditions. These choices configure processing and do not by themselves show a capture succeeded.
- **Webhook-driven order states:** The guide distinguishes new-order state before webhook result, `AUTHORISATION`-confirmed authorization, capture-result confirmation via `AUTHORISATION` for immediate capture or `CAPTURE` for manual capture, and cancellation after `CANCEL_OR_REFUND`. Bank-transfer/SEPA pending webhook receipt is optional and requires Customer Area settings. A configured Adobe Commerce status is not independent proof of financial finality or fulfillment.

## Detail locators

- `## Step 1: Install the plugin`, lines 19–52: Composer/module/setup/cache commands and cache exclusion.
- `### (Optional) Use Express Checkout flows`, lines 54–85: separate module and dated minimum-version claims.
- `## Step 2: Run cron`, lines 87–112: one-minute group, optional RabbitMQ, and disabled-by-default midnight cleanup.
- `## Step 3: Configure the plugin in Adobe Commerce`, lines 114–170: Customer Area prerequisite, automated/manual version boundary, destructive reconfiguration, environment, credential and currency/region fields; manual table inconsistencies at lines 161–165.
- `## Step 4: Configure order management settings`, lines 172–203: capture/open-invoice/PayPal/SEPA settings and webhook-dependent order states.
- `## Next steps`, lines 205–221: separate payment-method, stored-method and live-account guides.

## Related

- [[adyen-magento2]] — exact-version implementation concept and reciprocal source route.
- [[source-github-adyen-magento2]] — pinned `adyen/module-payment@11.0.0` implementation baseline and compatibility boundary.
- [[source-adyen-docs-plugins-adobe-commerce]] — plugin overview and major-version docs table.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/set-up-the-plugin-in-adobe-commerce/2026-09-15|Adobe Commerce plugin setup, captured 2026-09-15]]
