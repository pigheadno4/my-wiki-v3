---
title: "Adyen Classic Platforms: Automatic store split configuration"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/split-configuration-for-stores"
raw_files:
  - "adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15.md"
tags: [adyen, classic-platforms, stores, split-payments, pos]
---

## Overview

This 2021-modified, 2026-09-15-captured guide is for **Classic Adyen for Platforms**, not the newer Marketplace/Platforms split-configuration API. For a store-based integration, a Customer Area split configuration can apply commission fees automatically to payments processed through that store after it is attached to a Classic account-holder store. The page directs new implementations to a different new-integration guide. [[adyen-classic-platforms]]

## Scope and prerequisites

- The guide says **stores are available only for Classic point-of-sale and partner-platform integrations** in this context; a platform must use stores, have Support enable split configuration, and give its Customer Area user `Manage split configuration settings`. A listed `ecommerce` channel condition does not remove the stated store/integration prerequisite. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 78–86]].
- Create a named split configuration in Customer Area and retain its UUID. Add rules with channel, scheme/payment method, currency, fixed fee and variable fee; the channel/scheme/currency combination must be unique for each rule. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 84–104]].
- Attach the UUID and `virtualAccount` (the holder’s `accountCode` for the split amount) in `storeDetails` through Classic Account API `/updateAccountHolder`. The examples use a **TEST** Account API **v6** endpoint for a new or existing store. The request is **asynchronous**: rely on `ACCOUNT_HOLDER_UPDATED` notification for the final result before treating the store update as effective. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 106–171]].

## Rule routing and fallback

- A rule has a fixed fee, percentage fee or both, plus defined channel, currency and payment-method conditions. A transaction must meet **all** conditions. If no rule matches, **all funds go to the liable account**; the guide recommends a catchall `any` rule. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 28–42]].
- When multiple rules match, the priority order is **currency, payment method, funding source, channel**. The worked examples at raw lines 55–76 illustrate selection and a commission amount sent to the liable account; they are not a live split or settlement record. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 46–76]].
- Split instructions in a **payment or capture API request override** the store automatic split for that transaction. After a successful store create/update, the source says Adyen evaluates transactions processed through it; request submission alone does not prove this transition or funds movement. See [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 42–44, 169–171]].

## Detail locators

- Classic scope, rule conditions, no-match liable fallback and API override: [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 15–44]].
- Priority hierarchy, examples and integration/role prerequisites: [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 46–82]].
- Customer Area UUID, Classic Account API v6 TEST examples, destinations and asynchronous notification: [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|raw lines 84–171]].

## Related

- [[adyen-classic-platforms]] — Classic account-holder/store context.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/split-configuration-for-stores/2026-09-15|Automatic store split configuration (captured 2026-09-15)]]
