---
title: "Adyen partner integration checklist"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/partners/integration-checklist"
raw_files:
  - "adyen/docs/partners/integration-checklist/2026-09-15.md"
tags: [adyen, partners, integration-checklist, ecommerce, point-of-sale]
---

## Overview

Adyen's partner integration checklist guides a partner through scoping, building, documenting, testing and onboarding an ecommerce or in-person integration for its customers. It distinguishes required flow support from optional configuration and architecture choices. The checklist is planning and implementation guidance; completing its listed steps does not itself approve a partner, enable a merchant account, establish seller or merchant-of-record identity, or prove any payment, refund, capture or payout succeeded. See [[adyen]] and [[adyen-partners]] for provider and partner context.

## Key takeaways

- A partner integration must support multi-store setups, including multiple merchant accounts under one company account. The partner chooses payment methods by channel/location and appropriate account structure; the page does not assign legal-entity or seller roles for a particular deployment. Management API and OAuth are optional ways to automate customer configuration. Management API use needs additional API-credential roles; OAuth is described as customer-delegated API access, with detailed consent, scopes and token handling left to its separate guide.
- Adyen lists required online-flow coverage for payment modifications (refund, cancellation, authorization adjustment, delayed/separate capture), 3D Secure 2 where required, application information, webhooks for status changes, response/error handling, and result-code mapping. A capture-on-shipment flow is an example enabled by modification support, not a universal requirement. Region-specific requirements may add flows or features. An initial API response or checkout view is not the full payment lifecycle; webhook and result handling are separate checklist topics.
- In-person requirements include application information, terminal security, referenced/unreferenced refunds, receipts, in-progress cancellation, transaction-status verification when communication fails, and terminal logging. E2EE is the stated terminal security solution; P2PE is opt-in and limited to some terminal models. Details of refunds, status checks, terminal security and receipts belong to the linked guides.
- For online architecture, choose a server-side flow for the use case and connect it to Drop-in, Components or custom UI. The page says customer-facing headless use with their own UI must use API-only implementation. Security/compliance routes include integration security, PCI DSS and PSD2 SCA for European processing. This checklist is not a compatibility matrix or proof that a specific solution satisfies those requirements.
- The partner is responsible for integration documentation, including supported features/regions, configuration guides and end-to-end testing instructions. Adyen recommends a pilot with at least one customer before wider onboarding. Before customers process payments through the integration, the page says they must apply for a live account, submit an AOC or SAQ, and sign a contract with Adyen; customers should test and complete required integration steps before go-live. These prerequisites do not mean a test account, checklist completion or pilot grants live approval.

## Detail locators

- Nine-step partner scoping/build/document/go-live sequence: raw lines 17–33. Optional Management API/OAuth and credential-role caveat: `## Scope the configuration and maintenance flows for your integration`, lines 35–43. Payment-method selection and mandatory multi-account support: lines 45–53.
- Online modification, authentication, application information, webhooks, response/error and result-code coverage, plus regional qualification: `### Online payments` under integration requirements, lines 59–76. In-person required flows, P2PE model limit and logging: lines 78–86.
- Optional feature discovery, online client/server choices, API-only headless condition and in-person architecture: lines 88–128. Security, PCI and European SCA routes: `## Review security and compliance requirements`, lines 130–134.
- Channel-specific build checklist links and documentation responsibility: lines 136–156. Testing, pilot, customer live-account/AOC-or-SAQ/contract conditions: `## Prepare for go-live`, lines 158–174.

## Related

- [[adyen]] — provider context.
- [[adyen-partners]] — partner application and integration route.
- [[adyen-account-structure]] — company/merchant account hierarchy, separate from partner approval and legal seller identity.

## Related raw API references

- The raw checklist links to OAuth, Management API, API credential roles, online/POS channel checklists, webhooks, result codes, security/PCI guides and customer live-account steps. Their detailed permissions, payloads, tests and outcome rules need their own source evidence.

## Raw Sources

- [[raw/adyen/docs/partners/integration-checklist/2026-09-15|Adyen Docs: Partner integration checklist (2026-09-15 snapshot)]]
