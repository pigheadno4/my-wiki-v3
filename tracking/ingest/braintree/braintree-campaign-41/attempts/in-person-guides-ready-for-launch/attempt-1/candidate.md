---
title: "Braintree In-Person Ready for Launch"
type: source
date_ingested: 2026-10-06
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/in-person/guides/ready-for-launch"
raw_files:
  - "braintree/in-person/guides/ready-for-launch-2026-09-16.md"
tags: [braintree, in-person, production-launch, card-reader, graphql]
---

## Overview

This 2026-09-16 collected, unversioned [[braintree]] website guide is a production-launch readiness route for Braintree In-Person integrations. It organizes certification, contract and account onboarding, production credentials and merchant-account access, reader procurement, account-level feature configuration, and launch-day environment checks. It is a checklist and coordination guide, not proof of current availability, production approval for a particular integration, reader-online state, or a successful live payment.

## Key takeaways

- Braintree suggests a demo and code review with the merchant's Solutions Engineer and Integration Engineer, followed by necessary integration changes, before the documented green light for production launch. The page warns teams to include review and follow-up changes in the development timeline.
- Production account setup depends on the account structure designed with the PayPal engineering team and does not begin until a Braintree contract is signed. Production reader shipment likewise requires an executed PayPal contract, and reader procurement, staging, deployment, availability, and lead time must be planned with the PayPal team.
- After the Production Account exists, an account admin should generate production API keys. The API user must have access to the required production Merchant Account IDs (MAIDs), and the production keys and MAIDs must be configured in the integration and sent with API requests. Production Control Panel users and roles remain merchant-managed in the sensitive production environment.
- Features listed in the pre-launch configuration section should be successfully tested in Sandbox and integrated before production enablement; some configuration work can occur only after the production account exists. The raw locator preserves the feature-specific enablement and setup routes for blind credits, Vaulting, offline processing, QR payments, partial and incremental authorizations, Overcapture, prompts, card-data collection, custom idle screens, and L2/L3 data.
- The readiness questionnaire also asks about onboarded MAIDs, production readers, tested use cases, integration certification, an agreed launch timeline, and production Control Panel users, while explicitly noting that requirements for POS, ERP, OMS, e-commerce, or other integrated systems are additional. Launch day requires the production GraphQL endpoint and production keys, production location IDs and reader pairing, a tested firmware version, compliant networking, and a production setup test.

## Material warnings

> [!warning] Readiness and outcome boundary
> A completed checklist, configured production endpoint, paired reader, or setup test does not itself prove current product availability, production approval for a particular integration, reader-online state, or successful authorization, capture, settlement, or funding. Those outcomes require separate evidence.

> [!warning] Contract, access and environment gates
> The captured guide says production account setup and production reader shipment are gated by signed contracts. API success in production additionally depends on the production GraphQL endpoint, Production Account API keys, and API-user access to the required production MAIDs; Sandbox configuration or testing is not interchangeable with those production conditions.

## Detail locators

- Suggested demo and code review, necessary follow-up changes, green-light wording and timeline warning: `## Certify Your Integration`, lines 19-24.
- Account-structure coordination, signed-contract prerequisite and early onboarding guidance: `## Production Account Setup`, lines 27-32.
- Production key generation, account-admin role, API-user MAID access, integration configuration, and request usage: `## Production Account Setup`, lines 34-34.
- Production Control Panel users, permission segmentation, MAID-scoped access and merchant-owned setup: `### Create users in the Braintree Control Panel`, lines 37-42.
- Production reader procurement, staging, deployment, lead-time and contract-before-shipment conditions: `## Ordering Production Card Readers`, lines 45-53.
- Sandbox-before-production rule and account/team configuration routes for optional capabilities: `## Pre-Launch Configuration Checklist`, lines 56-60.
- Production account, MAID, reader, testing, certification, timeline and user questions plus other-system boundary: `## Launch Readiness Questionnaire`, lines 61-65.
- Network, production endpoint and keys, production location IDs and reader pairing, tested firmware, setup test, and explicit GraphQL endpoint reminder: `## Launch Checklist`, lines 66-71.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-in-person]]

## Related raw API references

- [[raw/braintree/in-person/guides/testing-your-integration-2026-09-16|Testing Your Integration]] - unread navigation linked by the readiness questionnaire
- [[raw/braintree/in-person/guides/setup-reader-2026-09-16|Setup Reader]] - unread launch-day network, location and pairing navigation
- [[raw/braintree/in-person/guides/making-a-transaction-2026-09-16|Making a Transaction]] - unread navigation for feature-specific transaction behavior

## Raw Sources

- [[raw/braintree/in-person/guides/ready-for-launch-2026-09-16|Braintree In-Person Ready for Launch]] - complete collected production-launch readiness guide
