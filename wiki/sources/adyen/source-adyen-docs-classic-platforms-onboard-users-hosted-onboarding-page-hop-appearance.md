---
title: "Adyen Classic Platforms HOP appearance customization"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page/hop-appearance"
raw_files:
  - "adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/hop-appearance/2026-09-15.md"
tags: [adyen, classic-platforms, hosted-onboarding, appearance, customer-area]
---

## Overview

This 2026-09-15-modified Classic Adyen for Platforms guide, captured the same day, describes changing the Hosted Onboarding Page (HOP) appearance in Customer Area: header, logo, background and an additional FAQ URL. It directs new implementations to a separate newer integration guide. [[adyen]] [[adyen-classic-platforms]]

## Key takeaways

- Appearance changes use Customer Area **Platform > Configure > Hosted Onboarding** and require the Customer Area user's **Manage HOP settings** role; without it, the guide directs them to an Admin user (raw lines 31–37, 44–50, 58–64, 73–80). These are platform configuration steps, not account-holder verification results.
- The default-header choice places the logo at top left and language selector/Help button in the header. Without a header, the logo moves to top center and language selector/Help button to the bottom (raw lines 31–42).
- The logo upload is limited to 400 × 128 pixels, JPG/JPEG/PNG/SVG and 100 KB; the background image accepts JPEG/PNG/SVG up to 5 MB. Alternatively the background color takes a `#RRGGBB` hexadecimal value (raw lines 44–71).
- An additional FAQ URL appears under Adyen's FAQ when account holders select Help (raw lines 73–80). The page distinguishes these Customer Area appearance controls from further onboarding-flow customization through `/getOnboardingUrl` parameters; it does not specify those flow parameters here (raw lines 21–29).

## Detail locators

- Classic-only scope and the appearance versus URL-parameter distinction: raw lines 19–29. Role, Customer Area route and header positions: raw lines 31–42.
- Logo role and file limits: raw lines 44–56. Background role, image limits and color format: raw lines 58–71. FAQ role and additional-URL field: raw lines 73–80.

## Related

- [[adyen-classic-platforms]] — older platform model.
- [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page]] — HOP onboarding and verification flow.
- [[adyen-platforms]] — separate newer platform model.

## Raw Sources

- [[raw/adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/hop-appearance/2026-09-15|Classic HOP appearance, captured 2026-09-15]]
