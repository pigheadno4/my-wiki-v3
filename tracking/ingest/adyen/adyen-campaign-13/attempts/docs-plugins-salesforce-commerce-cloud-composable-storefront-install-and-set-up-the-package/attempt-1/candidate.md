---
title: "Adyen Salesforce Composable Storefront package setup"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/plugins/salesforce-commerce-cloud/composable-storefront/install-and-set-up-the-package"
raw_files:
  - "adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/install-and-set-up-the-package/2026-09-15.md"
tags: [adyen, salesforce-commerce-cloud, composable-storefront, pwa, integration]
---

## Overview

This [[adyen]] guide sets up the Salesforce Commerce Cloud (SFCC) Composable Storefront integration using the `@adyen/adyen-salesforce-pwa` npm package together with the `int_adyen_PWA` companion cartridge. The cartridge adds Business Manager metadata, custom SCAPI endpoints and a hook for payment/order and webhook work beyond standard SCAPI; the PWA package supplies checkout components and server routes. The guide is setup and testing guidance, not evidence that a storefront is deployed, a payment is authorised, or an order is fulfilled. See [[adyen-salesforce-commerce-cloud]] for the provider integration route.

## Key takeaways

- The dated prerequisites list Salesforce PWA Kit **v3.12.0 or later**, Node **v22 or later**, npm **v11 or later**, a connected SFCC sandbox, configured sites/locales/currencies/inventory, WebDAV credentials, Salesforce-enabled Managed Runtime with **Admin** permission, and Commerce API **Customization with Hooks**. These are source requirements for this Composable Storefront path; the page does not pin an npm package version for its base install. [Raw: Requirements, lines 27–43]
- Install/build the companion cartridge, import site-specific payment, object-extension and job metadata, and set its Business Manager cartridge path. Its Notify endpoint stores webhooks for scheduled processing; Create Order assigns an order number before payment where gift cards require it; Get Order retrieves order details. The PWA setup then imports Adyen SSR routes **before** default Salesforce and custom routes, renders `AdyenCheckout` on checkout/confirmation pages, and supplies error/redirect routes. [Raw: Steps 1–3, lines 45–197]
- `AdyenCheckout` needs shopper `authToken`, site, locale, navigation and basket props. Its `returnUrl` is optional but, when used, must have a protocol, be URL-encoded for non-ASCII content and exclude personal information. Optional back-navigation and error-recovery hooks clean up redirect failures; the documented cleanup **fails pending Salesforce orders and recreates the basket**, so it changes order state. Locale/currency settings belong to the PWA site configuration. [Raw: Steps 4–6, lines 199–391]
- A new Adyen API key is skipped for an existing SFRA or SiteGenesis integration if one is already available. Standard webhook setup for this path specifies the site-ID URL, JSON, TLSv1.3, Basic authentication and HMAC key, and selects `OFFER_CLOSED`; `AUTHORISATION` is implemented by default. Webhooks are stored as SFCC custom objects, then the scheduled **Process** job updates order payment status and **Clean** deletes processed instances; a one-minute frequency is recommended. The guide says webhooks cannot be tested on localhost. [Raw: Steps 7–8, lines 392–481]
- Managed Runtime setup is Salesforce-enabled and environment-specific. The required configuration includes Adyen API/client keys, merchant account, test/live environment, webhook user/password and HMAC, Salesforce Commerce API/site/instance identifiers and scopes; a live URL prefix is conditional on live use. Keep secrets out of logs and inject them at runtime. From package **v4.3.0**, a JavaScript options object can supply supported configuration keys, with site-specific options taking precedence over site-specific environment variables, then global options, then global environment variables. The page says a deployment connects one region, MRT organization, SFCC site and Adyen Customer Area account, yet also describes a single host serving multiple sites through per-site options. Treat that as an unresolved scope tension, not proof of multi-site support for a specific deployment. [Raw: Step 9, lines 484–644, especially 510 and 555–623]
- Optional features have separate qualifications: Level 2/3 card data and Giving start at package **v4.3.0**; Giving needs a matching-currency campaign and donation-token-capable non-gift-card payment method. The separate in-person terminal path starts at **v4.4.0**, uses site/store-specific Terminal API settings, and requires the current shopper's store ID to be among configured active store IDs. Standard ecommerce Drop-in does not require terminal settings. Existing SFRA/SiteGenesis Adyen stores need page migration; test-card payments and Customer Area test status checks precede the separate payment-method and live steps. [Raw: Optional Steps 10–13, lines 645–831; Migrate pages and Testing, lines 832–849]
- This 2026-09-15 snapshot has embedded last-modified metadata from 2024. Examples and configuration do not establish current package compatibility, supported payment-method eligibility, successful webhook delivery, live payment or order outcomes, refunds, or settlement.

## Detail locators

- Versions and Salesforce-side prerequisites: `Requirements`, lines 27–43.
- Cartridge metadata, SCAPI endpoints, WebDAV/build/import and site path: `Step 1`, lines 45–107.
- PWA project, npm package, SSR route order and checkout/redirect page overrides: `Steps 2–3`, lines 108–197.
- Component props and redirect/order cleanup effects: `Steps 4–5`, lines 199–366.
- Locale/currency site configuration: `Step 6`, lines 367–391.
- API key reuse condition, webhook authentication/events and Salesforce Process/Clean jobs: `Steps 7–8`, lines 392–481.
- MRT enablement/deployment, required variables, options precedence, site-scope tension and secret warning: `Step 9`, lines 482–644.
- Optional country list, Level 2/3, Giving and terminal payments with package-version boundaries: `Steps 10–13`, lines 645–831.
- Existing-page migration, test-card check and next routes: `Migrate pages`, `Testing`, and `Next steps`, lines 832–860.

## Related

- [[adyen]] — provider page.
- [[adyen-salesforce-commerce-cloud]] — SFCC integration concept route.
- [[adyen-webhooks]] — general Adyen webhook behavior; this guide owns its SFCC processing setup.

## Raw Sources

- [[raw/adyen/docs/plugins/salesforce-commerce-cloud/composable-storefront/install-and-set-up-the-package/2026-09-15|Adyen Salesforce Composable Storefront setup (2026-09-15)]]
