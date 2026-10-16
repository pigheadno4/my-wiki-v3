---
title: "Adobe Commerce troubleshooting"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/troubleshooting"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/troubleshooting/2026-09-15.md"
tags: [adyen, adobe-commerce, troubleshooting, webhooks]
---

## Overview

Adyen's Adobe Commerce plugin troubleshooting guide (page metadata last modified 2023-05-19; captured 2026-09-15) walks through checkout and order-status diagnostics before contacting support. It covers cache and extension conflicts, logs, webhook acceptance and cron processing, selected payment API errors, payment-method visibility, customizations, and release/version checks. It is guidance for investigating a symptom, not evidence of a fix or a successful payment, capture, or order transition. The version-qualified plugin implementation baseline lives at [[adyen-magento2]] and should not be inferred from this older page.

## Key takeaways

- For missing or malfunctioning payment methods, clear Adobe Commerce and full-page caches including Varnish, then temporarily disable third-party plugins to isolate possible interference. These checks do not establish a root cause by themselves (raw lines 25–34).
- Use `var/log/adyen/error.log` for plugin/PHP errors and `var/log/exception.log` for Adobe Commerce errors; the latter also contains unrelated entries. `info.log` records Adyen API request/response JSON, `notification.log` records received webhooks, and `cronjob.log` traces their use in order-status updates (raw lines 36–58).
- An order status that does not update may involve an `OFFER_CLOSED` event not enabled for abandoned orders, webhooks not received, accepted, or stored, or cron not processing them or updating the order. The Customer Area endpoint test expects a successful HTTP acknowledgment such as 202. The guide names missing HMAC, mismatched notification credentials (often test/live mixing), and IP/server responses such as 302 or 401 as possible failures; acknowledgment alone does not establish order or financial outcome (raw lines 68–110).
- For queued notifications marked **Processing** and **Done** = **No**, the page directs contacting the technical team to restart cron. It also documents a technical-team database requeue step that changes `adyen_notification` Processing/Done from 1 to 0 and adjusts creation dates for notifications older than five days. These are conditional data-changing instructions, not a blanket retry; inspect the source and affected records before any operation. No operation was performed here (raw lines 112–118).
- For the generic order-placement error, inspect the `/payments` JSON response in `info.log`. In its examples, 500/code 905 suggests checking payment-method setup and contacting Support if persistent; 422/code 135 calls for `StateOrProvince` in the billing address. For a missing method, inspect additional setup, the `/paymentMethods` request's country/region and currency, and whether the response includes it. The examples do not classify every error or authorize a payment retry (raw lines 120–158).
- Customized plugins receive limited support; reproduce a suspected issue on a clean installation before attributing it. Check release notes and the installed version via Customer Area **Payment Device Version** or `merchantApplication.version` in `info.log`, then use GitHub issues or Support if unresolved (raw lines 162–191).

## Detail locators

- Preflight and cache/third-party isolation: raw lines 19–34.
- Log purposes and separation: raw lines 36–58.
- Order-status diagnosis, webhook endpoint test, credentials, HMAC, delivery and cron: raw lines 68–110.
- Notification queue and technical-team requeue conditions: raw lines 112–118.
- Payment error examples and payment-method visibility checks: raw lines 120–158.
- Customizations, release/version checks and support routes: raw lines 162–191.

## Related

- [[adyen-magento2]] — Adobe Commerce plugin concept and separately version-qualified implementation baseline.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/troubleshooting/2026-09-15|Adobe Commerce troubleshooting, captured 2026-09-15]]
