---
title: "Braintree In-Person Account Structure"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/get-started-1/account-structure"
raw_files:
  - "braintree/in-person/get-started-1/account-structure-2026-09-16.md"
tags: [braintree, in-person, account-structure, merchant-account, location-id, production-readiness]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide describes the Braintree account hierarchy and planning choices for an In-Person deployment. It distinguishes the gateway account and merchant account tiers from the virtual-only location layer, then compares store- and brand-oriented merchant-account structures. It is account-design evidence, not proof of current product availability, production enablement, reader-online state, or a successful payment.

## Key takeaways

- The guide describes the Braintree Gateway Account as the highest account tier, also calling it a Merchant ID, Public ID or Production ID, and says one gateway account can contain multiple merchant accounts. Its summary associates that umbrella with multiple merchant accounts, a shared token vault and aggregated reporting.
- A Merchant Account ID (MAID) can represent a business channel such as ecommerce, wholesale, mobile or in-store retail; within retail, the guide says the represented structure may extend to brands or physical store locations. The page places bank-account configuration for disbursements, settlement reporting, some configuration, user access and permissions, Amex service-establishment numbers, invoicing and MCC configuration at this level; those listed responsibilities are page-scoped structure guidance, not evidence that a particular account has been configured.
- The Location ID is described as a flexible, virtual-only layer. Readers are paired to this layer, multiple readers may share one Location ID, and one reader can be paired to only one Location ID at a time. The page says certain functionality such as PayPal and Venmo in-person QR payments is enabled at this layer and that a Location ID typically represents one physical store; this identifies the configuration layer, not merchant eligibility or actual enablement. The page also says Location ID does not appear in Braintree reporting and routes location-level reconciliation within one MAID to a separate reporting guide.
- The guide compares a merchant account for each store with a merchant account for each brand. Its table describes differences in disbursement, fee visibility, reporting, invoicing, management effort and store-level cost allocation, and recommends the store-oriented structure when granular store reporting is needed while recommending the brand-oriented structure for a business with many stores. These are documented planning implications and suggested use cases, not universal outcomes independent of merchant configuration, country or contractual setup.
- The account-structure decision is consequential: the guide says it is important to get right during initial setup, asks the merchant to consider deposit aggregation, Amex contracting, reporting, user permissions, store-opening frequency and legal-entity boundaries, and instructs the merchant to discuss the final decision with a PayPal Solutions Engineer or Integration Engineer.
- Account design is a pre-go-live activity, but the guide separately says production-environment setup takes time and can proceed in parallel with integration development. A Sandbox structure, Location ID or reader association therefore does not establish production provisioning or any authorization, capture, settlement or funding result.

## Material warnings

> [!warning] Structure decisions require account-specific review
> The guide explicitly directs the merchant to discuss the final account-structure decision with a PayPal Solutions Engineer or Integration Engineer. The comparison table and examples should not be universalized across legal entities, countries, contracts or merchant configurations.

> [!warning] Sandbox and outcome boundary
> Designing or configuring account structure, including a Sandbox structure or Location ID, is distinct from production-environment setup. This collected website page does not prove production enablement, current product or SDK support, reader-online status, or successful payment processing.

## Detail locators

- Gateway Account names, hierarchy and umbrella functions: `### Gateway Account`, lines 25-30.
- Merchant Account ID aliases, channel/store representations and account-level responsibilities: `### Merchant Account ID`, lines 35-63.
- Location ID role, reader-pairing cardinality, QR configuration layer, reporting boundary and screensaver configuration: `### Location ID`, lines 66-86.
- One-MAID-per-store and brand-oriented comparison, including disbursement, fees, reporting, invoicing, operational implications and suggested uses: `## One MAID per store VS One MAID for all stores`, lines 94-105.
- Initial-design importance, required PayPal engineering discussion and merchant decision questions: `## Account Structure Considerations`, lines 108-131.
- Production-environment timing and separation from integration development: `## Preparing for Go Live!`, lines 136-138.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/articles/control-panel/important-gateway-credentials-2026-09-16|Important Gateway Credentials]] - unread identifier and Control Panel navigation
- [[raw/braintree/in-person/guides/setup-reader-2026-09-16|Setup Reader]] - unread Location ID creation and reader-pairing navigation
- [[raw/braintree/in-person/get-started-1/configure-sandbox-2026-09-16|Configure Sandbox]] - unread next-step Sandbox navigation
- [[raw/braintree/in-person/guides/api-authentication-2026-09-16|API Authentication]] - unread next-step authentication navigation
- [[raw/braintree/in-person/guides/paypal-and-venmo-qrc-2026-09-16|PayPal and Venmo QR Code Payments]] - unread feature-specific navigation
- [[raw/braintree/in-person/guides/reporting-and-reconciliation-2026-09-16|Reporting and Reconciliation]] - unread location-level reconciliation navigation

## Raw Sources

- [[raw/braintree/in-person/get-started-1/account-structure-2026-09-16|Braintree In-Person Account Structure]] - complete collected guide covering gateway, merchant-account and Location ID hierarchy, structure tradeoffs and production-planning boundaries
