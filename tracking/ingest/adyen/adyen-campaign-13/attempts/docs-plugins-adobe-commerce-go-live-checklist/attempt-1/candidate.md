---
title: "Adobe Commerce go-live checklist"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/go-live-checklist"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/go-live-checklist/2026-09-15.md"
tags: [adyen, adobe-commerce, go-live, webhooks, live-payments]
---

## Overview

Adyen's Adobe Commerce plugin go-live checklist (page metadata last modified 2023-05-03; captured 2026-09-15) lists account, finance, risk/compliance, API, webhook, and real-payment test preparations for a live environment. Test setup is not copied to live. This is a preparation and test plan, not proof that a particular merchant is enabled, compliant, live, or has completed any payment or capture. The separately version-qualified plugin implementation baseline is [[adyen-magento2]].

## Key takeaways

- Configure the live Customer Area and Adobe Commerce admin panel separately: merchant accounts if needed; distinct live users with task-appropriate roles and account access; live payment methods and checkout order. Confirm shopper statement behavior through the stated support route. Payout bank-account details, payout schedule and reconciliation reports are separate finance checks; Reserve is optional and described for refunds or other expenses when in-process funds are insufficient (raw lines 19–68).
- Review live risk settings, fraud/chargeback notifications and the recommended CAPTCHA defense against card testing. The page warns that Visa/Mastercard 3D Secure enrollment can take up to seven days. Its compliance section calls for a merchant SAQ A assessment, recommends the default card component, says Adobe Commerce's PCI DSS 4.0.1 CSP script-integrity requirements apply regardless of SAQ A, calls for plugin v9.17.0 or later to meet those Adobe Commerce requirements, and assigns additional compliance review to customized/headless front ends; accessibility compliance remains merchant-owned (raw lines 70–102). These are source-dated checklist statements, not a compliance certification.
- Generate a live API key and client key; put the client key and live API key/endpoints into the indicated Adobe Commerce settings. The checklist names Merchant PAL webservice, Merchant Recurring, Checkout webservice and Checkout encrypted cardholder data as live API credential permissions. Do not substitute test credentials or infer credential validity from this page (raw lines 104–117).
- Configure live webhooks with the live credentials and HMAC key; enable non-default `OFFER_CLOSED` to close abandoned orders, accept the event types needed by the integration, and test Standard Webhook configuration. The example successful response is HTTP 200. The page also calls out the plugin cronjob that handles webhook events; an HTTP response by itself does not prove a corresponding order update or financial outcome (raw lines 119–139).
- Perform end-to-end scenarios with real payment details after live configuration. Such payments incur fees. The checklist asks for a successful real payment per offered method, refused and fraud examples, conditional manual capture/cancel and multiple-partial-capture checks, and successful/failed-challenge 3D Secure cases. Capture/cancel checks apply only to the stated capture settings, and the list does not establish that a particular test succeeded (raw lines 141–161). This page supplies no stored-token migration procedure or proof that tokens moved between environments.

## Detail locators

- Test/live separation, account users/methods, payout and reconciliation: raw lines 19–68.
- Risk, 3D Secure enrollment, PCI/CSP and accessibility: raw lines 70–102.
- Live API/client keys, roles and endpoint configuration: raw lines 104–117.
- Live webhook credentials, events, acceptance and cron test: raw lines 119–139.
- Fee-bearing real-payment scenarios and capture/3DS conditions: raw lines 141–161.

## Related

- [[adyen-magento2]] — Adobe Commerce plugin concept and separately version-qualified implementation baseline.
- [[adyen]] — Adyen provider page.

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/go-live-checklist/2026-09-15|Adobe Commerce go-live checklist, captured 2026-09-15]]
