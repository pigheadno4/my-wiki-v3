---
title: "Braintree Satispay Local Payment Method"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/satispay"
raw_files:
  - "braintree/docs/guides/local-payment-methods/satispay-2026-09-16.md"
tags: [braintree, local-payment-methods, satispay, italy, limited-release]
---

## Overview

This collected, unversioned Braintree page is a short availability and applicability record for Satispay as a Local Payment Method. It marks the method as limited release, limits buyer availability to Italy, and routes prospective integrations to Braintree's separate Local Payment Method integration guides. The 2026-09-16 snapshot does not establish current availability, merchant enablement, buyer eligibility, integration completion or a successful payment.

## Key takeaways

- The page says Satispay is currently in limited release and available only to buyers in Italy. That current-tense statement is preserved as snapshot evidence rather than a live availability guarantee.
- Its applicability row identifies the payment type as `satispay`, buyer country as Italy, seller-country scope as the captured label `EEA+ CH+ UK`, currency as `EUR`, and customer transaction limits from `0.01 EUR` through `99,999 EUR`. The page does not define the plus signs in the seller-country label, so this entry does not expand them.
- The page directs merchants that want to integrate Satispay to separate integration guides. It contains no Satispay-specific request, approval, token, webhook, capture, settlement or funding procedure.

## Evidence boundaries

> [!warning] Limited-release and applicability scope
> The page's limited-release notice and captured country, currency and amount row do not prove current program availability, account enablement or individual buyer eligibility. Recheck current and account-specific conditions before relying on the route.

> [!warning] Setup and execution scope
> The integration-guide link is navigation, not evidence that setup or a payment was executed. This short page names no client platform, SDK version, server API, Sandbox or Production environment, payment-state transition, settlement state or merchant-funding outcome.

## Detail locators

- Limited-release notice, Italy-buyer restriction and integration-guide route: `### Overview`, lines 20-21.
- Payment type, buyer country, seller-country label, currency and customer transaction limits: table under `### Overview`, lines 23-25.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected pages were not used as factual authority for this source entry; they are exact-file navigation for follow-on platform setup work:

- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|JavaScript v3 Local Payment Methods configuration guide]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16|Android v5 Local Payment Methods configuration guide]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16|iOS v7 Local Payment Methods configuration guide]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/satispay-2026-09-16|Braintree Satispay guide]] - complete collected page covering limited-release availability, applicability and the generic integration-guide route
