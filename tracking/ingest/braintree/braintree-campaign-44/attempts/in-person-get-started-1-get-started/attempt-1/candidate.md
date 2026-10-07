---
title: "Braintree In-Person Request Dev Kit"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/get-started-1/get-started"
raw_files:
  - "braintree/in-person/get-started-1/get-started-2026-09-16.md"
tags: [braintree, in-person, dev-kit, sandbox, card-reader]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] onboarding page explains how to request an In-Person Dev Kit for testing hardware and the API with a Braintree Sandbox Account. It is an approval-gated Dev Kit request and preparation route, not a client- or server-SDK integration guide: it provides no credential configuration, does not establish current eligibility or kit delivery, and does not prove reader readiness or a test or production payment outcome.

## Key takeaways

- After a PayPal/Braintree Account Executive approves moving forward, the page says a requester may ask for a Dev Kit containing a card reader that communicates with the Braintree Sandbox environment and test cards designed for continued card-present transaction testing.
- The documented request action is to contact a PayPal/Braintree Account Executive or Solutions Engineer. A requester not yet working with an Account Executive is directed to the linked sales form for more information.
- Receiving a Dev Kit requires either a signed NDA with PayPal/Braintree or existing Braintree merchant status. The page directs the requester to discuss the NDA with the PayPal sales representative before requesting the kit.
- While waiting for the kit, the page routes readers to configure a Braintree Sandbox Account, review the In-Person Technical Overview, and view the Braintree developer documentation; those linked pages, rather than this request page, hold the setup and implementation details.

## Material warning

> [!warning] Sandbox readers are not production readers
> The page explicitly says the Sandbox readers supplied in the Dev Kit are incompatible with production environments and cannot read production cards.

## Detail locators

- Page purpose—testing hardware and the API with a Dev Kit and Braintree Sandbox Account: introduction, lines 14-16.
- Account Executive approval, Dev Kit reader environment and card-present test-card contents: `### Requesting a Dev Kit`, lines 19-21.
- Account Executive, Solutions Engineer and sales-form request routes: note under `### Requesting a Dev Kit`, lines 23-24.
- Sandbox configuration, technical-overview and developer-doc navigation while waiting: `### While you wait for your test kit to arrive`, lines 27-36.
- Production incompatibility and production-card restriction: note, lines 40-41.
- Signed-NDA or existing-merchant receipt conditions: `### Requirements to receive a Dev Kit`, lines 44-46.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/get-started-1/configure-sandbox-2026-09-16|Configure a Braintree Sandbox Account]] - unread Sandbox-configuration navigation
- [[raw/braintree/in-person/about/technical-overview-2026-09-16|Braintree In-Person Technical Overview]] - unread technical-overview navigation
- [[raw/braintree/in-person/get-started-1/integration-checklist-2026-09-16|Braintree In-Person Integration Checklist]] - unread next-step navigation

## Raw Sources

- [[raw/braintree/in-person/get-started-1/get-started-2026-09-16|Braintree In-Person Request Dev Kit]] - complete collected Dev Kit request and eligibility page
