---
title: "Adyen payments apps for Shopify"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/shopify"
raw_files:
  - "adyen/docs/plugins/shopify/2026-09-15.md"
tags: [adyen, shopify, plugin, ecommerce]
---

## Overview

This 2025-modified Adyen webpage snapshot guides installation, configuration, testing, and live-account transition for the **Adyen Payments - Credit Cards** and **Adyen - Alternative Payments** apps on a Shopify store. It does not specify a plugin version or establish live merchant eligibility, supported methods for a particular country/currency, or a successful order, capture, refund, or payout. See [[adyen]] and [[adyen-shopify]].

## Key takeaways

- Shopify **Checkout Extensibility** is required. The page first routes merchants to Adyen test-account setup and the separate supported-payment-method list. Payment methods can be requested for a merchant account in test or live Customer Area; a request is not approval or availability for the store (raw lines 23–49).
- Install and activate the Credit Cards app before setting up the Alternative Payments app (raw lines 51–116). Connecting an account uses **Authorize with Adyen** and a Customer Area **Grant access** step. The guide limits selection to **one merchant account per region**; selecting more causes an error and requires re-authentication (lines 62–78). The document does not name granted permission scopes or a package version.
- In the Credit Cards app, the guide says Apple Pay and Google Pay do **not** need enabling in Adyen Customer Area; other payment methods do. It directs test mode to avoid charging the payment method used for testing, and instructs disabling test mode for live use (raw lines 80–94). Alternative Payments setup then syncs Customer Area-enabled methods to Shopify (lines 96–116).
- The guide recommends a duplicate store for rollback and tests both successful and unsuccessful flows, including 3DS2, missing shipping address for digital goods, and cardholder-name triggers with Adyen test cards (raw lines 118–193). These fixtures are test inputs, not proof of actual payment or order outcomes. The non-happy-flow table labels **Incorrect CVC** with the trigger `INVALID_CARD_NUMBER` (line 150); preserve that source mismatch rather than relabeling the trigger.
- Going live requires approval of a live Adyen account, configuring it separately because test settings do **not** copy, and requesting payment methods again in live Customer Area. The guide then has the merchant disconnect the test account, connect/activate the live account, and repeat end-to-end testing (raw lines 195–219). Disconnecting the test connection is an explicit configuration change, not evidence of a live payment.

## Detail locators

- `Requirements` and `Step 1`, raw lines 25–49: Checkout Extensibility, test account, method list, and merchant-account requests.
- `Steps 2–4`, raw lines 51–116: app dependency, account authorization, regional selection, wallet setup, mode, and method sync.
- `Test your integration`, raw lines 118–193: testing advice, failure triggers, test cards and 3DS2 fixtures.
- `Go live`, raw lines 195–219: live approval, separate configuration, test disconnection and live activation.

## Related

- [[adyen-shopify]] — Shopify-app integration route.
- [[adyen-online-payments]] — provider-wide payment lifecycle; platform-specific conditions remain here.

## Raw Sources

- [[raw/adyen/docs/plugins/shopify/2026-09-15|Shopify, fetched 2026-09-15]]
