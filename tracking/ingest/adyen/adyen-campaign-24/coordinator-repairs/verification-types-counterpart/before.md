---
title: "Adyen Platforms upfront and staggered verification"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/verification-overview/verification-types"
raw_files:
  - "adyen/docs/platforms/verification-overview/verification-types/2026-09-15.md"
tags: [adyen, platforms, verification, onboarding, payouts]
---

## Overview

This 2026-09-15 Adyen Platforms snapshot compares upfront and staggered collection of user verification information. Upfront collection seeks the full required information at onboarding; staggered collection initially seeks minimum information and then additional information as a user's tier changes. This is a platform-user verification model, not a description of Classic marketplace or issuing eligibility. See [[adyen]] and [[adyen-platforms]] for provider and platform context.

## Key takeaways

- The page states that users in upfront verification must complete full verification before they can process payments and receive payouts through the platform. It advises platforms to collect verification data upfront because the receive-payments capability is automatically requested for their users. A capability request does not itself establish that processing or payouts are allowed, enabled, executed, or settled. Upfront information is verified after an account holder is created; the page says users then need no additional information solely because they reach a higher tier.
- Only payment facilitators can request staggered verification, through an Adyen contact. Under that arrangement, the initially collected minimum depends on processing volume, country/region and other relevant factors. Additional required information is collected as needed and Adyen verifies it to enable or continue account-holder payouts. A higher processed amount than the current tier limit moves a user to a higher tier, but processing volume is not the only trigger. The source gives no numeric limits or universal time to verification.
- When a staggered user moves to a higher tier, payouts are temporarily disallowed until additional verification checks are completed. Adyen says it reports the change and required data by webhook; after the user supplies data and Adyen verifies it, payouts are allowed again. This is a conditional permission statement, not proof of any actual payout or bank receipt.
- There are four tiers, determined by user country, legal-entity type and processed amount. Triggered verification checks or requests for high-risk capabilities may also cause a move to a higher tier. The processed-amount currency is AUD for Australia, USD for the United States, CAD for Canada, NZD for New Zealand, SGD for Singapore, HKD for Hong Kong, and EUR for other countries/regions. Currency assignments are not threshold values.
- The page names no API credential or role and provides no account-specific eligibility or current verification result. Linked required-information, capability and verification-overview pages own detailed requirements and statuses.

## Detail locators

- Two collection modes, payment/payout condition, and upfront recommendation versus automatic receive-payments request: raw lines 19–24. Upfront account-holder sequence: lines 26–28. Payment-facilitator eligibility and Adyen-contact request: lines 30–34.
- Higher-tier payout interruption, webhook notification and verification condition: lines 34–38. Four-tier factors, non-volume triggers and processed-amount currencies: lines 40–56. Linked required information and capabilities: lines 58–61.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform onboarding and verification context.
- [[source-adyen-docs-platforms-verification-overview]] — broader verification-process and capability-status guide.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — capability request, allowed and enabled distinctions.

## Related raw API references

- The source links to required KYC information, country and legal-entity requirements, verification tiers, and user capabilities. Those linked guides require separate reading for specific eligibility or capability-state decisions.

## Raw Sources

- [[raw/adyen/docs/platforms/verification-overview/verification-types/2026-09-15|Adyen Docs: Verification types (2026-09-15 snapshot)]]
