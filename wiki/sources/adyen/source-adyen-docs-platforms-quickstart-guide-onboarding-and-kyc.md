---
title: "Adyen Platforms onboarding and verification quickstart"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/quickstart-guide/onboarding-and-kyc"
raw_files:
  - "adyen/docs/platforms/quickstart-guide/onboarding-and-kyc/2026-09-15.md"
tags: [adyen, platforms, onboarding, kyc, verification]
---

## Overview

This 2026-09-15 Adyen for Platforms quickstart explains how a platform onboards its users (called account holders here), collects KYC information and follows their verification. It is process guidance for a platform and its users, not a record that any user passed verification, obtained a capability, became eligible for payout or received funds. The page does not specify a complete test-to-live activation procedure.

## Key takeaways

- Users must complete onboarding and KYC checks before they can be paid out. The platform retains the user relationship and handles required-data collection, failed-check follow-up, expectations and communication; the page says Adyen does not communicate directly with those users.
- Hosted onboarding is recommended for most platforms. On invite, the platform requests an account holder in Customer Area and creates a hosted link. API-initiated hosted onboarding creates resources and a link through API calls. API-only onboarding gives the platform its own UI and data/API flow, with higher integration and maintenance effort. The recommendation is not a universal mandate.
- Legal entity types include individuals, organizations, sole proprietorships, trusts and unincorporated partnerships. Availability, required verification data and accepted formats depend on the operating country or region and entity type. Follow the linked requirement pages for the specific case; this quickstart does not settle a particular user's eligibility.
- Full upfront verification is the default. The page describes staggered verification as an option some ecommerce platforms use as transaction volume grows and directs platforms to discuss fit with their Adyen representative. Automated review comes first; inconclusive or unverifiable data can move to manual review, and unvalidated data produces an error. Manual review is generally within 48 hours, with Support escalation if longer, not a guaranteed deadline or approval. The page recommends account-holder webhook notifications and error-code handling.
- The page describes remaining PCI documentation obligations: a platform may submit SAQ-D or a QSA-provided AoC; users sign a simplified PCI questionnaire in hosted onboarding, while API-only flows generate and present SAQ-A. It says users must accept Adyen Terms of Service before taking actions on the platform: hosted flow presents them, while API-only flow must generate and present them. Its statement about verification/payout compliance responsibility transferring when users accept the Terms is conditional page guidance, not independent proof of a particular contractual or regulatory allocation.
- Customer Area KYC views require specific user roles. KYC summary/timeline and uploaded documents help investigate checks; the KYC insights dashboard requires enablement by an Adyen representative. For manual reviews beyond 48 hours, the support request includes account-holder/legal-entity references, the issue and whether it occurs in test or live. Viewing a status or filing a request does not establish capability activation or a payout result.

## Detail locators

- `# Onboarding and verification`: prerequisite, platform-user relationship and terms.
- `## Onboarding types`: hosted invite, API-initiated hosted, API-only and recommendation.
- `## Legal entity types`: supported categories and country/entity-dependent requirements.
- `## Verification process`, `### Automated data review`, `### Manual data review`: upfront/staggered conditions, fallback and support timing.
- `## PCI documentation and Adyen’s Terms of Service`: platform/user documentation and acceptance branches.
- `### Use the Customer Area`, `## Insights and monitoring`, `## Support`: roles, verification views, dashboard enablement and test/live escalation context.

## Related

- [[adyen-platforms]] — provider platform model and source route.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/quickstart-guide/onboarding-and-kyc/2026-09-15|Adyen onboarding and verification quickstart (fetched 2026-09-15)]]
