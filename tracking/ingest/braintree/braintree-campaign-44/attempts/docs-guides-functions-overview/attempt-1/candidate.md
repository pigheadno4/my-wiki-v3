---
title: "Braintree Functions Overview"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/functions/overview"
raw_files:
  - "braintree/docs/guides/functions/overview-2026-09-16.md"
tags: [braintree, functions, api, triggers, custom-code]
---

## Overview

This collected Braintree Functions overview presents a documentation preview for executing provided code through the Braintree API. It describes Braintree-ecosystem triggers executing uploaded code on the Braintree platform, while that code interacts with partners or vendors the business works with and, in some cases, maps a vendor response back to Braintree.

## Key takeaways

- The page frames Functions as opening the Braintree API to execute provided code, with possible uses including authorization for payment methods Braintree does not natively accept, accounting-system transactions, vendor fraud scoring, and custom workflows. These are examples, not guaranteed capabilities for a particular account.
- Braintree defines the triggers; the provided code is responsible for partner and vendor interactions, with response mapping needed only in some cases.
- The overview says Functions can work with an existing Braintree integration.

Scope: this is an unversioned webpage snapshot fetched on 2026-09-16 whose availability notice calls it a documentation preview and provides an email inquiry route. It does not label Functions as beta or establish current availability, account eligibility, an exact runtime or SDK, client-versus-server placement, an execution environment, or successful code or payment execution.

## Detail locators

- `AVAILABILITY` preview and inquiry route — lines 17–18.
- API-opening purpose and example workflow categories — lines 20–22.
- `How Functions Works`: Braintree triggers, uploaded code, partner/vendor interaction, and conditional response mapping — lines 23–28.
- Fraud-services and custom-payments examples, plus the existing-integration statement — lines 29–44.
- `Next Steps` navigation to CLI, payment-method, fraud, streaming, import, advanced, and publishing guides — lines 45–54; these links are navigation, not evidence for their targets' behavior.

## Related

- [[braintree]]
- [[braintree-payment-platform]]
- [[source-braintree-docs-guides-functions-advanced]]
- [[source-braintree-docs-guides-functions-cli-reference]]
- [[source-braintree-docs-guides-functions-accept-new-payment-method]]
- [[source-braintree-docs-guides-functions-act-on-fraud]]
- [[source-braintree-docs-guides-functions-import-data]]

## Raw Sources

- [[raw/braintree/docs/guides/functions/overview-2026-09-16|Braintree Functions Overview — fetched 2026-09-16]]
