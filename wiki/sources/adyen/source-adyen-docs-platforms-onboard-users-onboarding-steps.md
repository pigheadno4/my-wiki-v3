---
title: "Adyen Platforms onboarding steps filter landing page"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/onboard-users/onboarding-steps"
raw_files:
  - "adyen/docs/platforms/onboard-users/onboarding-steps/2026-09-15.md"
tags: [adyen, platforms, onboarding, verification, navigation]
---

## Overview

This 2026-09-15 Adyen for Platforms export is an onboarding-steps filter landing page. It says the interactive page is used to determine information required for a user and how to submit it to Adyen, but the pinned export contains no concrete step sequence or requirement result because Location and Legal entity/legal arrangement type are unselected. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Filter dimensions:** The page lists onboarding type (hosted or API-only), hosted flow (on invite or API-initiated), version, location, and legal-entity/legal-arrangement type. The export's current selection is hosted onboarding, on invite, version 4; that is a selected view, not a universal prerequisite or a statement about every account.
- **Missing result:** The page explicitly says to select all required filters on the interactive page or add missing query parameters to the .md export, naming Location and Legal entity/legal arrangement type. Its location and entity-type lists are filter options, not a complete eligibility matrix or verification requirements for any particular user.
- No roles, terms/consent mechanics, resource creation order, API calls, status transition or verification outcome appear in this pinned export. Use a fully selected page or separate approved source for those details; do not infer them from this navigation-only snapshot.

## Detail locators

- Purpose and available filter dimensions: pinned raw lines 15-29.
- Current hosted/on-invite/v4 selection and missing Location/entity filters: pinned raw lines 31-37.

## Related

- [[adyen-platforms]] — platform onboarding concept and reciprocal source route.
- [[source-adyen-docs-platforms-onboard-users]] — separate hosted/API-only overview.
- [[source-adyen-docs-platforms-verification-requirements]] — separate verification-requirements overview.

## Raw Sources

- [[raw/adyen/docs/platforms/onboard-users/onboarding-steps/2026-09-15|Adyen Onboarding steps for platforms, captured 2026-09-15]]
