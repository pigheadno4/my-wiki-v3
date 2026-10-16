---
title: "Customize the Adobe Commerce plugin | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/adobe-commerce/customize"
raw_files:
  - "adyen/docs/plugins/adobe-commerce/customize/2026-09-15.md"
tags: [adyen, adobe-commerce, customization, extensions, upgrades]
---

## Overview

This 2026-09-15 [[adyen]] Docs guide explains how an Adobe Commerce plugin integrator can put checkout or behavior customizations in a separate module. It is an implementation pattern for an existing Adobe Commerce plugin integration, not a deployed module, a version compatibility guarantee or a successful payment-flow test. [[adyen-magento2]]

## Key takeaways

- Adyen recommends an additional custom module instead of changing the default Adyen plugin module. Editing the default module may put Adyen support at risk and require more effort for upgrades or troubleshooting. A new major release requires reviewing its release notes and migration guide for breaking changes affecting custom code.
- The guide's sequence is to create a module dependent on `Adyen_Payment`, add it to Composer, implement the customization and deploy it. It describes dependency-injection class overrides, Adobe Commerce before/after/around method plugins, and checkout layout/CSS/JavaScript changes as distinct patterns. A class override can alter payment-processing behavior, so the chosen extension point and payment lifecycle need review.
- Code blocks are examples, not an exact package-qualified recipe. The Composer requirement uses `YOUR_ADYEN_PAYMENTS_PLUGIN_VERSION`, the displayed JSON includes an inline comment, and example directory/module names vary. Resolve a real package version and valid files against the target Adobe Commerce/plugin release before use. The page does not establish that its snippets compile or remain supported in every later version.
- Deployment commands include Composer autoload, Magento setup upgrade, dependency-injection compilation and cache operations. The guide advises staging/development tests before live deployment, automated and manual UI tests, test cards for payment-processing changes, and then a go-live checklist. Reading or running the sample commands alone cannot prove security, compatibility, payment authorization, capture, refund or settlement behavior.

## Detail locators

- **Support, upgrade and integration requirements:** raw lines 19–31.
- **Custom module/Composer skeleton and version placeholder:** raw lines 33–121.
- **Class overrides, method plugins and checkout UI patterns:** raw lines 123–206.
- **Deployment commands, testing and live-checklist route:** raw lines 208–238.

## Related

- [[adyen]]
- [[adyen-magento2]]
- [[source-github-adyen-magento2]] — separately versioned repository baseline

## Raw Sources

- [[raw/adyen/docs/plugins/adobe-commerce/customize/2026-09-15|Adyen Adobe Commerce customization guide — collected 2026-09-15]]
