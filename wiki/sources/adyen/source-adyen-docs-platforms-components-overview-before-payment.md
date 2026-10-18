---
title: "Adyen Platforms before-payment components"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/components-overview/before-payment"
raw_files:
  - "adyen/docs/platforms/components-overview/before-payment/2026-09-15.md"
tags: [adyen, platforms, ui-components, onboarding, transfer-instruments]
---

## Overview

This 2026-09-15 Adyen for Platforms before-payment components page is a short navigation hub. It says platforms onboard users and verify identity/business information before accepting payments on their behalf, and points to Onboarding components through which users submit information within the platform UI. Its named child is the Transfer Instrument component route.

## Key takeaways

- The Transfer Instrument card describes bank-account add, update and delete actions, instant-verification or document-upload paths, and verification-status viewing. This is a link description, not a complete integration specification or evidence that any bank account passed verification.
- The page links separately to the detailed Transfer Instrument component guide, Onboarding components, and the general component-library overview. The child guides own exact LEM/API version, credential/session roles, product, region, status and payout implications; this hub does not define them.
- A rendered onboarding component or submitted information does not establish completed user verification, permission to accept payments, a payout destination's current validity, or a live financial operation.

## Detail locators

- Opening paragraph: before-payment onboarding purpose and in-portal submission.
- `#### Transfer Instrument`: named child route and card description.
- `## See also`: Onboarding components and general component-library links.

## Related

- [[adyen-platform-components]] — main component-suite concept.
- [[source-adyen-docs-platforms-components-overview-before-payment-transfer-instrument-component]] — detailed Transfer Instrument component guide.
- [[adyen-platforms]] — parent Platforms context.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/platforms/components-overview/before-payment/2026-09-15|Adyen before-payment components hub (fetched 2026-09-15)]]
