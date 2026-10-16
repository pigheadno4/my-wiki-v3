---
title: "Adyen for Platforms integration and go-live checklist"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/integration-checklist"
raw_files:
  - "adyen/docs/platforms/integration-checklist/2026-09-15.md"
tags: [adyen, platforms, integration, onboarding, split-payments, go-live]
---

## Overview

This 2023-last-modified [[adyen]] for Platforms checklist, captured 2026-09-15, sequences account structure, API credentials, webhooks, components, user onboarding and verification, payment splits, payouts, internal transfers, reconciliation, and test-to-live preparation. Its test examples and checklist are guidance for a **platform** integration, not evidence that any merchant or user is verified, authorized for a capability, processing live payments, or receiving bank funds. [[adyen-platforms]]

## Key takeaways

- Before building, the page instructs the platform to design its implementation with an Adyen implementation manager. It calls for familiarity with distinct company and merchant accounts, stores, balance platform, account holders, balance accounts, legal entities, verified transfer instruments, and business lines. An account holder's capabilities specify what a user can do; a legal entity carries verification data, a balance account holds platform/user funds, and a transfer instrument represents a user's payout bank account. These objects must not be collapsed into a single merchant or seller identity.
- Development preparation separates Balance Platform/Transfers/FX/session credentials, Legal Entity Management/session credentials, and company-scoped Checkout/Management credentials. Server-side libraries are **optional**, while the listed API credentials and webhook configuration support the documented integration. The raw includes many test-environment API/library examples, including a test card `Authorised` response; these examples do not demonstrate live credentials, payment capture or settlement. See the raw locators for versioned sample calls.
- The page describes webhook endpoint/acknowledgment configuration and HMAC security, plus optional prebuilt components using server-created authentication sessions. For onboarding it recommends hosted onboarding (invite or API-initiated) and also describes API-only onboarding. Adyen must verify user information before the platform can process payments for users and pay out to them; API-only setup includes a transfer instrument that Adyen must verify before payout, terms/PCI steps, and verification/capability updates. A created resource, webhook, or onboarding invitation is not completed verification or granted payout capability.
- For payment processing, the platform must book funds and fees to the correct user and platform liable balance accounts. Automatic store-level split profiles are an option; **Adyen checks the profile at capture**, so a change after authorization but before capture applies to capture, and transaction-specific capture split instructions override the profile. Manual split routes exist for online Checkout API and in-person Terminal API. Split configuration is not itself proof of authorization, capture, settlement or payout.
- Managed payouts are **recommended**, with custom payouts also offered; these bank-account payouts differ from internal transfers between balance accounts. Report downloads require a reports credential from the Adyen contact and authenticated GET after report generation. To go live, apply for a live account, explicitly replicate test setup, switch credentials/endpoints, and run end-to-end checks for resources, successful and refused payments, payouts, verification errors, webhooks and reports. The checklist says test setup is not replicated automatically. Live-readiness steps do not establish that these checks or financial outcomes occurred.

## Detail locators

- **Implementation design and platform resource identities:** raw lines 19–45.
- **Optional libraries, credential families and test API/library examples:** raw lines 47–1040; test Checkout response around lines 1039–1040.
- **Webhook/component setup and onboarding variants/verification:** raw lines 1042–1189.
- **Pay-in splits, capture-time profile precedence, payouts and internal transfers:** raw lines 1191–1264.
- **Report credentials and test-to-live checklist:** raw lines 1266–1312.

## Related

- [[adyen-platforms]]
- [[adyen-webhooks]]
- [[adyen-reporting]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/platforms/integration-checklist/2026-09-15|Adyen for Platforms integration checklist — collected 2026-09-15]]
