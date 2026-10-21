---
title: "Adyen Marketplace Terms of Service components"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/components-overview/before-payment/terms-of-service-component"
raw_files:
  - "adyen/docs/marketplaces/components-overview/before-payment/terms-of-service-component/2026-09-15.md"
tags: [adyen, marketplaces, platforms, ui-components, onboarding, terms-of-service]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace page introduces **Accept Terms of Service** and **Manage Terms of Service** UI components within [[adyen-platform-components]]. It says they display legal documents, capture acceptance, show current status and provide signed-copy downloads in a portal's API-only onboarding flow. The pinned page is a short overview with a version **4.0.x placeholder**, not a usable version-4 integration procedure or proof that a particular user accepted terms.

## Key takeaways

- The Onboarding components are compatible only with legal entities created with **Legal Entity Management API v3 or v4**. That API version condition is separate from the component-library version. See raw lines 23 and 35–45.
- The page says the Terms of Service components cover document display and acceptance workflows with less custom API wiring. It recommends them within API-only onboarding, but says they cover **Terms of Service documents only**; other onboarding parts still require separate API calls. The listed components are **Accept Terms of Service** and **Manage Terms of Service**, for current-document acceptance, status viewing and signed-copy download. See raw lines 25–33.
- Feature guidance may vary by library version. Despite saying to select a version, the pinned page contains no version-4 implementation steps: its only version-specific section says documentation for **4.0.x is not yet available** and directs readers to **3.32.x** for current integration steps. Do not infer session policy, UI callbacks, legal effect or technical API steps for 4.0.x from this overview. See raw lines 35–45.
- The component description is a proposed user flow, not evidence that a signed copy exists, a user accepted a specific terms version, onboarding passed verification, or payment/payout capabilities were enabled. The page's next steps are navigation to onboarding steps and the component library hub. See raw lines 25–33 and 47–50.

## Detail locators

- LEM API v3/v4 compatibility and Terms component scope: raw lines 23–27.
- Accept/Manage inventory and described tasks: raw lines 29–33.
- Library-version qualification and 4.0.x placeholder/3.32.x pointer: raw lines 35–45.
- Onboarding and component-library navigation: raw lines 47–50.

## Related

- [[adyen]] — provider profile.
- [[adyen-platform-components]] — canonical UI component-suite concept.
- [[adyen-platforms]] — modern platform onboarding context.
- [[source-adyen-docs-marketplaces-components-overview]] — parent Marketplace component inventory.
- [[source-adyen-docs-marketplaces-onboard-users-components]] — broader onboarding component scope.

## Raw Sources

- [[raw/adyen/docs/marketplaces/components-overview/before-payment/terms-of-service-component/2026-09-15|Marketplace Terms of Service components — pinned 2026-09-15 raw snapshot]]
