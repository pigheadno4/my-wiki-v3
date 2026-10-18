---
title: "Adyen Capital getting-started roadmap"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/get-started"
raw_files:
  - "adyen/docs/capital/get-started/2026-09-15.md"
tags: [adyen, capital, platforms, integration, test-live]
---

## Overview

This Adyen Capital getting-started guide was last modified 2022-10-26 and captured 2026-09-15. It gives a platform integration roadmap from scoping and design through build, test, and separate live setup. It is process guidance, not evidence of current product eligibility, a financing offer, accepted terms, grant execution, or funds received.

## Key takeaways

- The stated prerequisites are an **Adyen for Platforms** integration, a user operating in a supported Capital country/region, and contacting Adyen sales to register interest. The page links a supported-region anchor but does not itself list jurisdictions or account-specific eligibility criteria. Its dated requirements are not confirmation that a particular platform or user is currently eligible.
- During scope and design, the Adyen contact works with the platform on Capital-related financial-regulation compliance, required account-holder capabilities, and integration choice. The two named paths are Adyen UI components or a custom API-only interface using Capital API/library. This is a design choice, not a grant or compliance approval.
- For components, the page routes to the UI component guide and integration steps. For API-only work, it names distinct steps: get grant offers, show Terms of Service, disburse a grant, get grant details, and manage disbursements. These are linked lifecycle guides, not evidence that any one step occurred. Test-account credentials permit building in the test environment; they do not imply live access.
- The platform is responsible for testing what it builds in Adyen's test environment. Adyen recommends testing again after live configuration. Test setup is **not replicated** to the live account: the platform must recreate configuration and test in live, then follow the go-live checklist. Passing test checks or completing configuration does not prove a live offer, approved user, accepted contract, grant payout, bank receipt, or repayment.
- This page is a navigation/sequence source. Concrete capability states, regional product availability, credential roles, offer terms and grant-event outcomes belong to the linked dedicated sources and actual account evidence.

## Detail locators

- `## Requirements`: Platforms prerequisite, supported-region link, sales contact.
- `## How it works`: scope/design, build, test and live setup sequence.
- `## 1. Scope and design your implementation`: Adyen contact, compliance, capabilities and component/API-only paths.
- `## 2. Build your integration`: component routes and API-only offer/terms/disbursement/detail-management links.
- `## 3. Test your integration` / `## 4. Configure your live account`: test responsibility, nonreplicated setup and live retest.

## Related

- [[adyen-capital]] — main Capital concept and dated product-region route.
- [[adyen-platforms]] — parent Platforms context.
- [[source-adyen-docs-capital-integration-checklist]] — detailed setup and go-live checks.
- [[adyen]] — provider profile.

## Raw Sources

- [[raw/adyen/docs/capital/get-started/2026-09-15|Adyen Capital get started (last modified 2022-10-26; fetched 2026-09-15)]]
