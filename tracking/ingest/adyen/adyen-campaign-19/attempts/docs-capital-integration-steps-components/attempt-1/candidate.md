---
title: "Integration steps for UI components | Adyen Capital"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/capital/integration-steps-components"
raw_files:
  - "adyen/docs/capital/integration-steps-components/2026-09-15.md"
tags: [adyen, capital, platforms, components, integration]
---

## Overview

This 2026-09-15 Adyen Capital integration guide describes embedding Capital Overview and Capital Offer Platform Experience components in a platform portal, including session authentication, client setup, optional localization/customization and alternate component flows. It is component setup guidance, not evidence of a user offer, verified eligibility, accepted financing terms, grant disbursement, repayment or bank receipt. See [[adyen]], [[adyen-capital]], and [[adyen-platform-components]].

## Key takeaways

- The page requires Adyen for Platforms integration, a Balance Platform API key with **Capital Component: Manage** for Session authentication, account-holder `getGrantOffers` capability, and Adyen configuration for Capital. In this component implementation, financing funds can be paid only to the user's balance account; transfer-instrument payout is unsupported, even though other Capital product routes may differ. Check language/country/browser availability in linked guides (raw lines 27–50).
- The platform server creates a `POST /sessions` token using HTTPS origin, an account-holder-scoped policy, **Capital Component: Manage** role and `product: platform`; the front end receives the session object through its refresh callback. The guide then installs the Platform Experience library and mounts Overview or Offer (raw lines 72–186, 190–312). A token or mounted component proves neither capability allowed nor financed funds booked.
- Overview embeds Offer by default; integrators may hide an unqualified state, interrupt the flow, or render Offer separately/screen-selectively. `getState` distinguishes `isUnqualified`, `isPreQualified`, `hasRequestedGrants` and `isInUnsupportedRegion` in this library snapshot. These are component state labels, not underwriting decisions or live grant lifecycle evidence (raw lines 54–70, 228–241, 382–503).
- `onFundsRequest` is described as firing after a successful grant **request**; `onOfferSelect` after successful offer selection. Neither callback proves that a grant was approved or disbursed. The separate `onFundsRequest` signatures differ between Overview (requested grant data plus early-renewal grant ID) and Offer (requested grant data) (raw lines 209–226).
- Features depend on library version. `availableTranslations` is deprecated, `environment` defaults to test, and live origin requires HTTPS. The guide offers optional localization/appearance customization and version-specific SRI for embedded scripts/styles (raw lines 27–31, 98–105, 166–172, 198–203, 314–380, 505–525).

## Detail locators

- Product/component prerequisites and balance-account-only disbursement path: raw lines 37–50.
- Server session policy, client installation and initializer details: raw lines 72–312.
- State and callback semantics: raw lines 209–235; alternative UI use cases: raw lines 382–503.
- Version/deprecation, locale, appearance and supported-language list: raw lines 27–31, 166–172, 198–203, 314–380, 505–525.

## Related

- [[adyen-capital]]
- [[adyen-platform-components]]
- [[source-adyen-docs-capital-manage-user-capabilities]]

## Raw Sources

- [[raw/adyen/docs/capital/integration-steps-components/2026-09-15|Pinned Adyen Capital component integration guide]]
