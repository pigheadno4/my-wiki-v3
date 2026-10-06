---
title: "Braintree In-Person Partners Overview"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/partners/overview"
raw_files:
  - "braintree/in-person/partners/overview-2026-09-16.md"
tags: [braintree, in-person, partners, graphql, platform]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website overview describes partner-specific considerations for a Braintree In-Person GraphQL integration. It says the GraphQL API behaves the same for partners and merchants, while generally describing partners as software providers that bundle Braintree into software used by multiple merchants. It is a design and coordination overview, not evidence that a software provider is an approved or official partner, that a merchant or country is eligible, that an account or reader has been provisioned, or that a payment succeeded.

## Key takeaways

- The page generally describes partners as software providers integrating Braintree into a bundled solution for many merchants, with POS, order-management, call-center and ecommerce providers as examples. It directs readers to PayPal/Braintree sales for available partner models and fit; that contact route is not approval or enrollment proof.
- For a multi-merchant integration using basic authentication, each merchant has its own API-key set tied to its Braintree Gateway Account, so the partner integration must make keys configurable per merchant. The statement is specific to the documented basic-authentication example and does not establish a universal credential model for every integration route.
- Because Braintree account-structure models can affect deposits, reporting, user management and other solution behavior, the page recommends a flexible account hierarchy and discussion with a Solutions Engineer. This is architectural guidance, not a claim that one hierarchy applies to every merchant, platform or country.
- Official PayPal partners are required to send a partner BN code for tracking merchants and volume over the partner integration and are told to discuss its transmission with a Solutions Engineer. The requirement is scoped to official partners; the page does not say that possessing or sending a BN code confers partner approval.
- Recommended partner-solution calls are presented as additions to the basic charge and refund calls used for MVP functionality. The raw table preserves the named reader health, firmware-update, location-creation, pairing, line-item-display and custom-prompt routes and their stated use cases; a request, setup action or documented route does not prove feature provisioning, reader state, displayed output or payment outcome.

## Material warnings

> [!warning] Partner and availability boundary
> This collected website page does not define partner acceptance criteria or establish official-partner status, country coverage, merchant eligibility, account provisioning, feature enablement or current availability. Its examples and recommendations are not universal partner/platform capabilities.

> [!warning] Setup and payment boundary
> Per-merchant key configuration, account-hierarchy design, BN-code transmission, location creation, reader pairing, display requests and other recommended calls are integration or operational steps. They do not by themselves prove approval, successful provisioning, reader-online state, authorization, capture, refund, settlement or funding.

## Detail locators

- Shared GraphQL behavior and partner-specific scope: introductory paragraph, line 16.
- General partner definition, example software-provider types and sales-team route for models or fit: `## Who is considered a Partner?`, lines 19-21.
- Per-merchant configurable API keys, basic-authentication example and Gateway Account relationship: `## API Key Management`, lines 24-26.
- Account-model consequences, flexible-hierarchy recommendation and Solutions Engineer consultation: `## Account Structure`, lines 29-31.
- Official-partner BN-code requirement and tracking purpose: `## Partner Tracking/Audit`, lines 34-36.
- Recommended partner-solution calls, MVP charge/refund relationship and feature/use-case table: `## Recommended Functionality For Partner Solutions`, lines 39-52.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/guides/api-authentication-2026-09-16|API Authentication]] - unread navigation for basic-authentication details
- [[raw/braintree/in-person/get-started-1/account-structure-2026-09-16|Account Structure]] - unread navigation for account-hierarchy models
- [[raw/braintree/in-person/guides/additional-api-calls-2026-09-16|Additional API Calls]] - unread navigation for reader health and related operations
- [[raw/braintree/in-person/guides/setup-reader-2026-09-16|Setup Reader]] - unread navigation for location creation and reader pairing
- [[raw/braintree/in-person/guides/display-information-2026-09-16|Display Information]] - unread navigation for line-item display behavior
- [[raw/braintree/in-person/guides/custom-prompts-2026-09-16|Custom Prompts]] - unread navigation for prompt behavior

## Raw Sources

- [[raw/braintree/in-person/partners/overview-2026-09-16|Braintree In-Person Partners Overview]] - complete collected partner-considerations overview
