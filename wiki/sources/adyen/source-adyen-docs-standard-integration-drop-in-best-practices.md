---
title: "Adyen Standard Web Drop-in best practices"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/standard/integration/drop-in/best-practices"
raw_files:
  - "adyen/docs/standard/integration/drop-in/best-practices/2026-09-15.md"
tags: [adyen, online-payments, standard-integration, web-drop-in, checkout-security]
---

## Overview

This 2026-09-15 [[adyen]] page gives implementation guidance specifically for a **Standard online-payments Web Drop-in** integration, within [[adyen-online-payments]]. It covers client lifecycle, custom-button safety, browser/redirect constraints, resource loading and testing. These are integration practices and dated compatibility recommendations; they do not prove that a payment method is enabled, a shopper was authorized, or funds settled.

## Key takeaways

- Initialize `AdyenCheckout` and mount Drop-in **once** when ready to display methods. React StrictMode and hooks can rerun effects; execute instance creation/mounting on the **client** under SSR because Drop-in needs `window` and `document`. The page's React snippet has a malformed hook import path and mounts from an effect keyed to `dropin` without a once-only guard, so treat it as illustrative rather than paste-ready proof of single mounting. See raw lines 33–69.
- For a **custom pay button**, disable it as soon as an attempt starts and use `beforeSubmit` to reject an in-progress submission. The snippet contains an ellipsis placeholder and no shown reset of its in-progress flag after completion/failure, so it is not a complete retry/error design. The prose mentions Pay-button and Enter-key attempts but describes `beforeSubmit` as triggered by button selection; verify keyboard behavior in the actual integration. **PayPal, Klarna and Click to Pay do not support the custom button** here; use Drop-in's button for those methods. See raw lines 71–111.
- Use **HTTPS in LIVE**; HTTP is described only for local testing. Cross-domain iframe hosting breaks redirect flows, so if an iframe is unavoidable the page says host it on the parent domain. For native mobile apps it recommends avoiding WebViews and names Android Custom Tabs or iOS SFSafariViewController instead. See raw lines 113–136.
- The browser-version table is a dated support snapshot. Drop-in may set risk cookie `_RP_UID`; extensions can block iframe/elements needed by payment methods. These observations do not establish behavior for a particular browser/session. See raw lines 138–167.
- Prefer the Adyen Web npm package for client resources; when embedding script/CSS, align the URL region with LIVE endpoints and Drop-in `environment`. The page recommends SRI `integrity` and `crossorigin`, with version-specific hashes in release notes. Its URL table shows `checkoutshopper-...cdn.adyen.com`, but the v6.33.0 SRI example uses `checkoutshopper-live.adyen.com`; do not mix host, version and hash from these separate examples without verification. A hash mismatch prevents the browser loading the asset. See raw lines 175–218.
- Test a working integration in a secure context and on real mobile devices. The Uplift section is a recommendation to inspect optimization opportunities, not proof of improved conversion or account feature activation. See raw lines 169–173 and 220–230.

## Detail locators

- **Standard Drop-in scope, one-time mounting, React example and SSR:** raw lines 19–69.
- **Custom-button duplicate prevention and method exceptions:** raw lines 71–111.
- **HTTPS, iframe/WebView and browser tables:** raw lines 113–158.
- **Cookie, extensions and Uplift guidance:** raw lines 160–173.
- **Regional resources, SRI and host mismatch:** raw lines 175–218.
- **Testing and child navigation:** raw lines 220–236.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-standard-integration-drop-in]]

## Raw Sources

- [[raw/adyen/docs/standard/integration/drop-in/best-practices/2026-09-15|Adyen Standard Drop-in best practices — collected 2026-09-15]]
