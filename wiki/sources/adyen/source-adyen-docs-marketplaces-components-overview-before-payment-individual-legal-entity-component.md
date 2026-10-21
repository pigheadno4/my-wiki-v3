---
title: "Marketplace Individual Legal Entity components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/before-payment/individual-legal-entity-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/before-payment/individual-legal-entity-component/2026-09-15.md"
tags: [adyen, marketplaces, components, onboarding, legal-entities]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace page introduces prebuilt **Create Individual** and **Manage Individual** UI components for collecting individual users' identity details and documents and managing verification within a platform portal. It recommends them for the individual-entity portion of an API-only onboarding flow; the rest of that flow still needs API calls. [[adyen-platform-components]]

## Key takeaways

- Onboarding components are compatible only with legal entities created through Legal Entity Management API **v3 or v4**. That condition applies to the legal entity, not proof that a particular component library version or onboarding session is ready. See raw lines 19–25.
- The page says these components handle personal-detail capture, identity-document upload, status monitoring and updates, reducing custom sensitive-data and upload logic. It lists **Create Individual** and **Manage Individual**, but limits them to individual legal entities; other parts of API-only onboarding remain a platform implementation task. See raw lines 25–33.
- Feature guidance depends on library version. The captured page's version section is a placeholder: it says **v4.0.x documentation is not yet available** and routes readers to **v3.32.x** for integration steps. This page supplies no actual component initialization steps and does not prove v4.0.x behavior, verification completion or account activation. See raw lines 35–45.

## Detail locators

- **Purpose, LEM v3/v4 compatibility and individual-only scope:** raw lines 15–27.
- **Named components and stated functions:** raw lines 29–35.
- **Version choice and missing v4.0.x integration documentation:** raw lines 35–45.
- **Onboarding/component-library navigation:** raw lines 47–50.

## Related

- [[adyen-platform-components]]
- [[adyen-platforms]]
- [[source-adyen-docs-marketplaces-components-overview|Marketplace component inventory]]
- [[source-adyen-docs-marketplaces-onboard-users-onboarding-steps|Onboarding step context]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/before-payment/individual-legal-entity-component/2026-09-15|Adyen Marketplace Individual Legal Entity component page — collected 2026-09-15]]
