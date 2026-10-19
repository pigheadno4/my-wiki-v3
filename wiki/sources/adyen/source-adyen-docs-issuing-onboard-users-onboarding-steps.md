---
title: "Adyen Issuing: onboarding steps selector"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/onboard-users/onboarding-steps"
raw_files:
  - "adyen/docs/issuing/onboard-users/onboarding-steps/2026-09-15.md"
tags: [adyen, issuing, onboarding, verification]
---

## Overview

This 2026-09-15 Issuing onboarding-steps capture is a **verification-requirements selector**, not a completed country- and entity-specific checklist. It says the interactive page determines required user information and submission methods after filters are selected. The exported snapshot shows hosted onboarding and version 4, but omits location and legal-entity/legal-arrangement type; those missing filters prevent a concrete requirement result. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Available filters are hosted versus API-only onboarding, version, location, and legal entity/legal arrangement type (individual, organization, sole proprietorship). The snapshot lists locations but does not select one.
- The current selection is **Hosted onboarding, version 4**. The page directs readers to select all required filters interactively or add the missing query parameters to the Markdown URL to export a concrete result. No country-specific data fields, document list, consent step, API payload or verification outcome is present in this pinned raw.
- Treat this source as navigation to the filtered requirements. Do not infer requirements for any user, region or onboarding method from this unfiltered capture, or treat it as proof of an approved/active account holder or issued card.

## Detail locators

- Raw lines 15–21 identify the Issuing onboarding-steps and verification-requirements purpose.
- Raw lines 23–28 enumerate onboarding, version, location and entity-type filters.
- Raw lines 30–35 give the hosted v4 selection and explain how to obtain a concrete filtered export.

## Related

- [[adyen-issuing]] — Issuing program context.
- [[adyen]] — provider context.
- [[adyen-index]] — provider navigation.

## Raw Sources

- [[raw/adyen/docs/issuing/onboard-users/onboarding-steps/2026-09-15|Adyen Issuing onboarding-steps selector, captured 2026-09-15]]
