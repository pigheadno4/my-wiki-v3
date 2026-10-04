---
title: "Braintree Local Payment Methods Overview"
type: source
date_ingested: 2026-10-04
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/local-payment-methods/overview"
raw_files:
  - "braintree/docs/guides/local-payment-methods/overview-2026-09-16.md"
  - "braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16.md"
tags: [braintree, local-payment-methods, regional-payments, non-instant-payments, payment-limits]
---

## Overview

This collected Braintree developer-guide overview describes Local Payment Methods as region-specific bank, wallet or other payment choices and provides a customer-country inventory with transaction-limit locators. It is an unversioned overview route to configuration, custom client integration and server integration; it does not itself document a client or server SDK version, execution environment or completed payment flow. The 2026-09-16 snapshot does not establish current support, merchant enablement, buyer eligibility or successful execution.

## Key takeaways

- The captured table labels 15 methods as currently supported and associates them with customer countries and any stated transaction limits. Use the table as snapshot inventory, not as uniform availability evidence: MyBank is separately marked limited access, and Swish is qualified as supported only for Braintree Web SDK integrations. Method-country and limit details remain at the raw locator below.
- The table explicitly labels Boleto Bancário, Multibanco and OXXO as non-instant. It does not classify every other listed method as instant, so absence of the label is not proof of instant completion.
- The same page lists Giropay and Klarna Pay Now / SOFORT in the currently-supported table while separately saying PayPal stopped supporting Giropay from July 1, 2024 and Sofort from April 18, 2024. The snapshot does not resolve that internal inconsistency.
- Vaulting payment methods and creating recurring transactions are stated as unsupported for Local Payment Methods.
- The page's integration sequence is configuration, custom client integration and server integration. This overview does not document initiation, nonce creation, webhook notification, transaction association, settlement or funding semantics; those stages require the applicable platform, method and server documentation.

## Evidence boundaries

> [!warning] Inventory and applicability conflict
> The current-support table and the dated Giropay and Sofort end-of-support notices conflict within the same snapshot. MyBank has limited access and Swish is Web-SDK-only. Preserve method, country, access and platform qualifications rather than treating the inventory as a guarantee of current availability.

> [!warning] Unresolved currency tension
> The fully read same-date article-level Local Payment Methods owner says transactions are automatically presented in euros, while this developer overview expresses customer transaction limits in EUR as well as PLN, BRL, GBP, MXN and SEK. The sources do not explain whether limit denomination and presentment currency differ, and this entry does not harmonize them. Consult the exact method documentation before making a currency claim.

> [!warning] Lifecycle and environment boundary
> The overview labels only three methods non-instant and supplies navigation to client and server work. It provides no SDK version, Sandbox or Production execution evidence, or method-wide rule connecting initiation, a nonce, a webhook notification, transaction creation, settlement and merchant funding. Keep those as distinct evidence points.

## Detail locators

- Regional bank, wallet and other-method identity with iDEAL and Bancontact examples: `# Overview`, raw line 16.
- Customer-country inventory and stated transaction limits: `## Supported payment methods`, raw lines 21-39.
- Giropay and Sofort dated end-of-support notices: `## Supported payment methods > IMPORTANT`, raw lines 41-46.
- MyBank limited access and Swish Web SDK-only qualification: `## Supported payment methods > AVAILABILITY`, raw lines 49-54.
- Unsupported vaulting and recurring transactions: `## Recurring transactions and Vault support`, raw lines 57-59.
- Configuration, custom-client and server-integration routes: `## Integration steps`, raw lines 62-67.
- Supporting article's blanket EUR-presentment statement: `## Availability`, supporting raw line 21.
- Supporting article's client/server setup route and customer-confirmation funding wording: `## Setup`, supporting raw line 31, and `### Funding`, supporting raw line 44.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Article-level Local Payment Methods owner: [[source-braintree-payment-methods-local-payment-methods]]

## Related raw API references

The following collected files were not used as factual authority for this entry; they are exact-file navigation for platform, lifecycle and environment follow-up:

- [[raw/braintree/docs/guides/local-payment-methods/configuration/javascript/v3-2026-09-16|Braintree Local Payment Methods configuration — JavaScript v3]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/android/v5-2026-09-16|Braintree Local Payment Methods configuration — Android v5]]
- [[raw/braintree/docs/guides/local-payment-methods/configuration/ios/v7-2026-09-16|Braintree Local Payment Methods configuration — iOS v7]]
- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/android/v5-2026-09-16|Braintree Local Payment Methods custom client — Android v5]]
- [[raw/braintree/docs/guides/local-payment-methods/client-side-custom/ios/v7-2026-09-16|Braintree Local Payment Methods custom client — iOS v7]]
- [[raw/braintree/docs/guides/local-payment-methods/server-side/node-2026-09-16|Braintree Local Payment Methods server integration — Node.js]]
- [[raw/braintree/docs/guides/local-payment-methods/testing-go-live/node-2026-09-16|Braintree Local Payment Methods testing and go-live — Node.js]]
- [[raw/braintree/docs/reference/general/webhooks/local-payment-methods/node-2026-09-16|Braintree Local Payment Methods webhook reference — Node.js]]

## Raw Sources

- [[raw/braintree/docs/guides/local-payment-methods/overview-2026-09-16|Braintree Local Payment Methods developer overview]] - fully read pinned snapshot covering regional identity, customer-country inventory, transaction-limit locators, deprecation and access qualifications, vaulting and recurring-use limits, and integration routes
- [[raw/braintree/articles/guides/payment-methods/local-payment-methods-2026-09-16|Braintree Local Payment Methods article]] - fully read same-date supporting authority used only for the article-owner route and unresolved EUR-presentment and funding-wording boundaries
