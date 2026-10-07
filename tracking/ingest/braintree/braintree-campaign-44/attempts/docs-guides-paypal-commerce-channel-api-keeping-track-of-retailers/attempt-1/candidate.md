---
title: "Braintree PayPal Commerce Channel API — Keeping Track of Retailers"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers"
raw_files:
  - "braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers-2026-09-16.md"
tags: [braintree, paypal-commerce-channel-api, retailers, onboarding, offboarding, webhooks]
---

## Overview

This collected, unversioned Braintree website guide describes server-to-server retailer onboarding and offboarding webhook messages for a channel using the PayPal Commerce Channel API. It is scoped to retailers granting or revoking the channel's authorization and to delivery at the destination URL supplied during Channel API setup; no environment or SDK version is named. The 2026-09-16 snapshot is historical evidence, not proof of current API availability or any particular retailer's or channel's eligibility, setup, message delivery, or payment or order execution. See [[braintree]] and the provider-level route [[braintree-payment-platform]].

## Key takeaways

- The guide recommends looking up products only for retailers that authorized the channel. It tells the channel to use onboarding and offboarding messages to maintain its list of authorized retailers.
- An onboarding message follows a retailer granting the channel permission to query the API for that retailer's products and create orders for its store. The example identifies the event with `topic: retailer`, `action: created`, and a retailer domain.
- An offboarding message follows a retailer revoking that authorization. The example uses `topic: retailer` and `action: deleted`; after offboarding, retailer-specific access tokens and client credentials are no longer valid.
- Delivery is attempted immediately after a successful onboarding or offboarding event. If the receiving server does not return HTTP 200 in under 10 seconds, the guide says delivery is retried several times over the next 12 hours, with an increasing delay after each attempt.

## Detail locators

- **Purpose, authorization boundary, destination, and list maintenance:** `Keeping Track of Retailers` (raw lines 14–22).
- **Onboarding condition and example payload:** `Onboarding` (raw lines 23–40).
- **Offboarding condition, example payload, and credential invalidation:** `Offboarding` (raw lines 42–61).
- **Acknowledgement threshold and redelivery window:** `Retry and failure logic` (raw lines 62–67).

## Related

- [[braintree]]
- [[braintree-payment-platform]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal-commerce-channel-api/keeping-track-of-retailers-2026-09-16|Braintree PayPal Commerce Channel API — Keeping Track of Retailers (2026-09-16 snapshot)]]
