---
title: "Adyen Docs: Upgrade your Java API library for Checkout API v72"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api/upgrade-api-library"
raw_files:
  - "adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/upgrade-api-library/2026-09-15.md"
tags: [adyen, java, api-library, checkout-api, migration, online-payments]
---

## Overview

This Adyen migration page addresses online-payment integrations with a payments server using the Java API library. Its 2026-09-15 snapshot directs an upgrade from an earlier `adyen-java-api-library` version, such as v4.1.0, to v40.0.0 or later to support **Checkout API v72**. The Java library version and Checkout API version are distinct. The page gives use-case-based server-code examples; it does not document a one-to-one Classic API call conversion or prove deployed library behavior.

## Key takeaways

- Adyen calls this a major product, feature, and architecture upgrade and says there is no linear path. Identify the integration's own use cases, compare the current Checkout API version with v72 using the API Diff Tool, and map supported models before changing server code. The named use cases include Sessions or Advanced payments, webhooks, authorization adjustments, subscriptions, and gift cards.
- The example initializes a Java `Client` and `PaymentsApi` with `Environment.LIVE`, a live endpoint URL prefix, and an **API key**. The live prefix is an endpoint configuration in this example; the page does not establish a universal region or prefix for every merchant. The API key is server configuration, distinct from the HMAC key used to verify webhooks.
- The `paymentMethods` and card `payments` request examples are explicitly for the **Advanced flow**. They are not a requirement that a Sessions integration make those same calls. The card example uses test encrypted-card strings as illustrative input, not evidence of a real payment or a complete production request.
- For payment webhooks, the sample parses a `NotificationRequest`, selects its first item, validates its HMAC, and only then shows asynchronous event consumption. A separate Balance Platform/Management example validates the HMAC from the `hmacsignature` header before invoking a handler. These are different webhook examples; do not treat the sample's first-item assumption as a general batch-processing guarantee.
- The guide shows `RequestOptions` carrying an `idempotency-key` for a request and catching `ApiException` to inspect status, response body, and `ApiError`. After upgrading, it instructs testing all supported use cases, webhook processing, error scenarios, and payment flows in the test environment. Documentation and examples do not establish that those tests passed.

## Detail locators

- Raw lines 15–27: Java library and Checkout API v72 version identities, major-upgrade rationale, payments-server requirement.
- Raw lines 29–47: API Diff Tool scope and use-case-first migration, including Sessions/Advanced, webhook, adjustment, subscription, and gift-card routes.
- Raw lines 49–73: server-code update pattern, live-environment client setup, live endpoint prefix, API key, and `PaymentsApi` initialization.
- Raw lines 75–113: Advanced-only `paymentMethods` and card `payments` examples, including illustrative test card strings.
- Raw lines 115–157: payment-webhook and other-webhook HMAC examples, first-item selection, and handler boundary.
- Raw lines 159–193: idempotency header and `ApiException` handling examples.
- Raw lines 195–210: test-environment checklist and linked API/library references.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-upgrade-your-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/upgrade-your-integration/migrate-to-checkout-api/upgrade-api-library/2026-09-15|Adyen Java API library upgrade guide snapshot (2026-09-15)]]
