---
title: "Braintree PayPal Here on Braintree"
type: source
date_ingested: 2026-10-05
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/articles/guides/paypal-here"
raw_files:
  - "braintree/articles/guides/paypal-here-2026-09-16.md"
tags: [braintree, paypal-here, in-store-payments, point-of-sale, historical]
---

## Overview

This pinned Braintree snapshot describes linking a PayPal Here in-store integration to Braintree so its transactions can be viewed alongside online Braintree transactions and managed through the Braintree Control Panel or API. It is a historical, product-specific retrieval route, not evidence that PayPal Here is currently supported, that a merchant is eligible or enabled, that the linked SDK remains available, or that a payment operation succeeded.

## Key takeaways

- The page separates the PayPal Here in-store channel from online Braintree transactions while describing a linked management view. It does not make PayPal Here a generic Braintree online-payment route.
- The snapshot states merchant availability in the US, UK and Australia, while limiting PayPal Here payment-information vaulting to the US. These are page-scoped historical statements, not present eligibility evidence.
- PayPal Here is not enabled by default on the account. The page routes onboarding to a separate enablement guide and therefore does not establish enablement from possession of a Braintree account alone.
- Once enabled, the page says PayPal Here transactions can be viewed and managed in the Braintree Control Panel or API and can be submitted for settlement, authorizations voided and refunds issued. This documented capability is not proof of execution, settlement, refund completion or current operational support.
- For a custom point-of-sale application, vaulting is tied to use of the PayPal Here SDK; on first enablement, the page says OAuth automatically authorizes PayPal Here to add to the Braintree Vault. The page does not supply an SDK version, current SDK-support status, OAuth scopes, token lifecycle or failure behavior.

## Evidence boundaries

> [!warning] Historical support and deprecation boundary
> The immutable page was collected on 2026-09-16, but it contains no deprecation, retirement or current-support notice. Treat it as evidence of the documented PayPal Here integration model at that snapshot only; verify present product and SDK status separately.

> [!warning] Payment-channel and execution boundary
> The documented transactions originate from the PayPal Here in-store channel and become visible or manageable through Braintree after linking and enablement. The page does not establish online-checkout eligibility, merchant-specific activation, reader or SDK operability, OAuth success, vault-write success, transaction authorization, settlement, refund completion or funding.

## Detail locators

- Linked in-store transaction visibility alongside online Braintree transactions and US-only in-store card saving: opening paragraph, raw line 16.
- Historical fee statement that PayPal Here on Braintree adds no cost above standard PayPal Here pricing: `## Fees`, raw lines 19-21; not current or merchant-specific pricing evidence.
- Stated merchant regions and US-only vaulting availability: `## Compatibility`, raw lines 24-26.
- Account enablement prerequisite and delegated onboarding route: `## Setup`, raw lines 29-31.
- Control Panel and API management surfaces plus the displayed PayPal Here fields: `## How it works`, raw lines 34-52.
- Settlement submission, authorization void and refund actions: `## How it works`, raw line 54.
- Custom POS application, PayPal Here SDK and first-enablement OAuth-to-Vault statement: `## How it works`, raw line 56.
- Aggregate transaction-search route and `PayPal Here` payment-method type: `## Reporting`, raw lines 59-61.
- PayPal-directed support route: `## Contact`, raw lines 64-66.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Management surface: [[braintree-control-panel]]

## Raw Sources

- [[raw/braintree/articles/guides/paypal-here-2026-09-16|Braintree PayPal Here on Braintree guide]] - complete collected page covering the historical in-store integration, regional and vaulting scope, enablement, management actions, custom-POS OAuth prerequisite and reporting route
