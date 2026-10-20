# C23 Classic Platforms HOP appearance retrieval checks

## Q1 — Where can the platform customize HOP appearance, and what can change?

In Classic Customer Area, a user with **Manage HOP settings** goes to **Platform > Configure > Hosted Onboarding** (raw lines 31–37). The guide covers header placement, logo, background image/color, and an additional platform FAQ URL under Adyen's FAQ (raw lines 21–27, 39–42, 44–80). Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-hop-appearance]] → [[raw/adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/hop-appearance/2026-09-15]].

## Q2 — What role, file and scope limits constrain these controls?

Each appearance task requires **Manage HOP settings**; an Admin user handles missing access (raw lines 35, 48, 62, 77). Logo: at most 400 × 128 pixels, JPG/JPEG/PNG/SVG, 100 KB (raw lines 52–56). Background image: JPEG/PNG/SVG, 5 MB; background color: `#RRGGBB` (raw lines 66–71). This page is Classic-only and points further onboarding-flow customization to `/getOnboardingUrl` parameters rather than detailing it here (raw lines 19, 29); appearance changes do not evidence completed verification. Forward route: [[index]] → [[adyen-index]] → [[adyen-classic-platforms]] → [[source-adyen-docs-classic-platforms-onboard-users-hosted-onboarding-page-hop-appearance]] → [[raw/adyen/docs/classic-platforms/onboard-users/hosted-onboarding-page/hop-appearance/2026-09-15]].
