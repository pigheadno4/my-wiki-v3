---
title: "Adyen Docs: Upgrade to Android v5.0.0"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/upgrade-to-android-5-0-0"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/upgrade-to-android-5-0-0/2026-09-15.md"
tags: [adyen, android, sdk, drop-in, components, migration]
---

## Overview

Adyen's Android migration guide lists breaking integration changes for apps moving from Android v4.13.3 or earlier to v5.0.0. It covers build dependencies, configuration, Drop-in and Component methods, Component views, launch calls, imports, and optional action handling. This is version-specific documentation, not evidence that an SDK migration or payment flow was executed successfully.

## Key takeaways

- The guide recommends Checkout API v70; it does not state that v70 is a minimum requirement. Its build table specifies compile and target SDK 34 and named dependency versions for this migration snapshot. Consult the raw table before updating a project.
- In the configuration object, `shopperLocale`, `environment`, and `clientKey` are required. `amount` is conditional on showing the amount on the Pay button. The guide distinguishes `Environment.TEST` for testing from a live environment for go-live.
- For Drop-in, replace `makePaymentsCall` with `onSubmit` and `makeDetailsCall` with `onAdditionalDetails`; `onActivityResult` is no longer applicable. Launching with `DropIn.startPayment` now takes the documented context, launcher, deserialized `/paymentMethods` response, configuration, and service class; a result intent can no longer launch Drop-in.
- For Components, remove the observer methods, implement `ComponentCallback` for `onSubmit`, `onAdditionalDetails`, and `onError`, and use `AdyenComponentView` instead of per-Component views. In the guide's advanced-flow example, the merchant server makes `/payments` and `/payments/details` requests. The Component launch uses `PROVIDER.get` with the activity or fragment, payment method, configuration, and callback.
- The guide also calls for fixing moved or renamed imports and avoiding classes marked internal by Restricted API lint. Its optional action-handling step says payment method Components can handle required actions; the card example handles redirect and threeDS2 without separate RedirectComponent or Adyen3DS2Component implementations. A different-page action flow can use `GenericActionComponent`.
- Although the page is titled as a v5.0.0 upgrade, its configuration and launching sections explicitly introduce v5.3.0 links. Preserve that distinction when applying those examples to an exact SDK version.

## Detail locators

- Raw lines 15–24: migration starting version and Checkout API v70 recommendation.
- Raw lines 25–47: compile/target SDK 34 and exact dependency-version table.
- Raw lines 49–112: conditional versus required configuration properties and separate Drop-in/Components examples; v5.3.0 configuration links.
- Raw lines 114–179: Drop-in method replacement, Component callback and merchant-server roles, and required `AdyenComponentView`.
- Raw lines 181–242: Drop-in and Component launch parameters, `/paymentMethods` inputs, result-intent removal, and v5.3.0 launch links.
- Raw lines 244–257: import and internal-API changes, plus optional Component action handling.

## Related

- [[adyen]]
- [[adyen-android-sdk]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-upgrade-your-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/upgrade-to-android-5-0-0/2026-09-15|Adyen Android v5 migration guide snapshot (2026-09-15)]]
